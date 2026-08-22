# Quantitative Quality-Control Consistency Review — Workflow 1.5.1

## Pending Human Adjudication

Every candidate in this report is **Pending Human Adjudication**. These are source-grounded quantitative reporting quality-control observations, not findings of invalidity or determinations of correction. Small preventable reporting defects can matter for downstream evidence extraction; this report does not claim propagation, a conclusion change, or serious harm.

## Executive Quality-Control Summary

Complete review of the supplied package identified **9** stable quantitative reporting-consistency candidates: C001 through C009. The review covered all 149 direct-source PDF pages and all mapped quantitative relationships without a candidate cap, review queue, top-N subset, or deferred-by-cap section. No candidate was created from a coherent display-zero P value.

The cards retain the printed evidence, comparison rule, bounded alternative interpretations, and a specific human question. They do not select replacement values or assign a final correction.

## Package and Reused-Evidence Provenance

The package contains five supplied PDFs and no supplied workbook, CSV, DOC, DOCX, participant-level dataset, analysis code, or table-production source. Direct-source identity was recorded before review in [source_hashes_before.sha256](review_1_5_1/source_hashes_before.sha256). The direct-source inventory is [source_inventory.md](review_1_5_1/source_inventory.md):

| Source ID | Direct source | Pages | SHA-256 |
|---|---|---:|---|
| DOC-001 | [main article, PDF p. 1](../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=1) | 14 | `9da22a99ae26fb643cd89b38f256e3c9363a5d94df39a32513cfa1ff0928612b` |
| DOC-002 | [Supplement 1, PDF p. 1](../joi190106supp1_prod_1635377898.47058.pdf#page=1) | 75 | `ed7b6aa10f5e7c9525e219854322f57b50741f093a9c541396834400c461fb43` |
| DOC-003 | [Supplement 2, PDF p. 1](../joi190106supp2_prod_1635377898.49605.pdf#page=1) | 30 | `7a7176632ceca33fd510640dde6394387f8aa686c0e16f6fa87c875b3cc3d9e8` |
| DOC-004 | [Supplement 3, PDF p. 1](../joi190106supp3_prod_1635377898.49725.pdf#page=1) | 29 | `e53756553fffe2d0c8a6176339ab33e6e15285ca7c791c06c6595dfe9743b170` |
| DOC-005 | [Supplement 4, PDF p. 1](../joi190106supp4_prod_1635377898.50723.pdf#page=1) | 1 | `fcc0c94cc98fb1437769cd96fd5b756d2cf0a13cc2e73d81c8661b62f7d1b7c3` |

Reusable source-matched native/layout text and selected rendered/OCR assets were inventoryed and hashed before review in [reused_artifact_hashes_before.sha256](review_1_5_1/reused_artifact_hashes_before.sha256). They served only as locators and transcription aids; direct PDF pages are the evidence authority. The complete fitness and coverage register is [evidence_asset_inventory.md](review_1_5_1/evidence_asset_inventory.md).

## Scope, Complete Coverage, and Exclusions

The stable review unit was one PDF page. [source_coverage.md](review_1_5_1/source_coverage.md) records complete mapping for each source:

| Source ID | Total units | Reusable | Fresh-required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 14 | 14 | 0 | 14 | COMPLETE |
| DOC-002 | 75 | 0 | 75 | 75 | COMPLETE |
| DOC-003 | 30 | 0 | 30 | 30 | COMPLETE |
| DOC-004 | 29 | 29 | 0 | 29 | COMPLETE |
| DOC-005 | 1 | 0 | 1 | 1 | COMPLETE |
| **Total** | **149** | **43** | **106** | **149** | **COMPLETE** |

The scope prioritized numeric, denominator/proportion/total, inferential-statistical, cross-document numeric, measure/label/scale, and rate-versus-count consistency. Protocol and SAP statements were not treated as observed-result comparators without a matched population, estimand, time point, and model. A literal very small P-value display would not be a candidate on formatting alone; no such candidate was registered. The complete stage and shard record is [coverage_manifest.md](review_1_5_1/coverage_manifest.md).

## Quantitative and Statistical Relationship Coverage

The numeric inventory contains **269** canonical N relationships, documented in [numeric_relationship_inventory.md](review_1_5_1/relationships/numeric_relationship_inventory.md). The statistical inventory contains **777** canonical S relationships, documented in [relationship_inventory.md](review_1_5_1/statistics/relationship_inventory.md).

Statistical pass 1 and the independent pass 2 each recorded every S001-S777 as complete. Both passes used the supplied-source-compatible checks of point-estimate containment, interval ordering, sign/direction, labels, matched repetitions, and CI/P display coherence where the printed two-sided model and 95% CI supported that check. No unsupported reconstruction of SEs, test statistics, degrees of freedom, covariance, or tiny P values was performed. Pass records are [statistical_pass_1.md](review_1_5_1/checkers/statistical_pass_1.md) and [statistical_pass_2.md](review_1_5_1/checkers/statistical_pass_2.md).

## Candidate Index

| ID | Category | Short description |
|---|---|---|
| [C001](#c001--etable-2-assigns-the-n3311-column-a-second-intervention-group-label) | Measure, label, or scale inconsistency | eTable 2 assigns two labels to N=3,311. |
| [C002](#c002--etable-2-red-wine-median-lies-above-its-printed-upper-quartile) | Numeric or arithmetic inconsistency | Red-wine median exceeds printed upper IQR endpoint. |
| [C003](#c003--all-randomized-red-wine-baseline-summaries-differ-between-etables-2-and-7) | Cross-document numeric inconsistency | Baseline red-wine summaries differ across two tables. |
| [C004](#c004--pdqs-baseline-mean-differs-between-the-principal-and-baseline-value-carried-forward-tables) | Cross-document numeric inconsistency | Baseline PDQS means differ across tables. |
| [C005](#c005--intervention-baseline-energy-sd-differs-between-table-3-and-etable-8) | Cross-document numeric inconsistency | Intervention baseline energy SD differs. |
| [C006](#c006--baseline-body-weight-summaries-differ-between-table-1-and-etable-9) | Cross-document numeric inconsistency | Baseline body-weight summaries differ. |
| [C007](#c007--baseline-bmi-means-differ-between-table-1-and-etable-9) | Cross-document numeric inconsistency | Baseline BMI means differ. |
| [C008](#c008--figure-4-threshold-labels-do-not-preserve-the-methods-boundary-operators) | Measure, label, or scale inconsistency | Figure 4 and Methods use different threshold operators. |
| [C009](#c009--etable-4-total-olive-oil-baseline-row-conflicts-with-the-tables-medianiqr-convention) | Measure, label, or scale inconsistency | Olive-oil baseline label conflicts with table convention. |

## Candidate Evidence Cards

## C001 — eTable 2 assigns the N=3,311 column a second intervention-group label

**Adjudication status:** Pending Human Adjudication

**Candidate statement:** The eTable 2 opening header assigns `Intervention group` to both N=3,272 and N=3,311, whereas the continuation and main Table 2 identify N=3,311 as control.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Supplement 3 eTable 2 opening header — PDF p. 3](../joi190106supp3_prod_1635377898.49725.pdf#page=3); [Supplement 3 eTable 2 continuation — PDF p. 5](../joi190106supp3_prod_1635377898.49725.pdf#page=5); [main article Table 2 — PDF p. 5](../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5).

**Source evidence:** The opening page prints `Intervention group` over N=3,272 and again over N=3,311. The continued table and the main table pair N=3,311 with `Control group`.

**Reported-versus-comparator:** The same displayed N=3,311 column is labelled intervention on the opening page and control on the continuation and main table.

**Reasoning procedure:** Match the repeated denominator and table column across the opening and continuation headers, then compare its group identity.

**Calculation:** This is a text-identity comparison: N=3,311 has two incompatible arm labels within a fixed two-arm display.

**Alternative source-grounded interpretations:** The opening heading may be a localized production error while the numerical column retains the control-group order. No supplied source documents a distinct N=3,311 intervention population.

**Mechanical evidence recheck:** All three direct pages were found; the opening label, continuation label, main-table comparator, arm Ns, and table context match the ledger. Table-production source is unavailable.

**Quality-control relevance:** A treatment-arm heading identifies the population from which displayed values are extracted.

**Potential downstream evidence impact:** If confirmed, a data extractor could assign the N=3,311 column to the wrong arm. The package does not establish that this occurred or that any conclusion changed.

**Human verification steps:** Inspect the table-production source and confirm the intended N=3,311 heading and its column contents.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — eTable 2 red-wine median lies above its printed upper quartile

**Adjudication status:** Pending Human Adjudication

**Candidate statement:** The intervention baseline red-wine entry is printed as `33 (0, 29)` g/week while the footnote defines baseline values as median (IQR).

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [Supplement 3 eTable 2 red-wine row and footnote — PDF p. 7](../joi190106supp3_prod_1635377898.49725.pdf#page=7).

**Source evidence:** The printed intervention entry is `33 (0, 29)` g/week, and the page states that baseline data are median (IQR).

**Reported-versus-comparator:** Median 33 is compared with the printed upper IQR endpoint 29.

**Reasoning procedure:** Apply the ordering rule for a `median (Q1, Q3)` display.

**Calculation:** `0 ≤ 33 ≤ 29` is false; the median exceeds the printed upper endpoint by `33 − 29 = 4` g/week.

**Alternative source-grounded interpretations:** The median, an IQR endpoint, or row/column alignment may be a production error. The supplied PDFs do not identify the intended replacement.

**Mechanical evidence recheck:** The direct page confirms the row, arm, unit, median, endpoints, and median/IQR footnote. Participant-level observations and the intended values are unavailable.

**Quality-control relevance:** A median/IQR display requires an ordered central value and quartile endpoints.

**Potential downstream evidence impact:** If confirmed, an extractor could copy an internally incompatible baseline red-wine summary. The package does not show downstream reuse or a changed conclusion.

**Human verification steps:** Recompute the entry from the intended participant set and quantile convention; verify the row alignment and source output.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — all-randomized red-wine baseline summaries differ between eTables 2 and 7

**Adjudication status:** Pending Human Adjudication

**Candidate statement:** ETable 2 prints red-wine baseline medians `33` and `4`, whereas eTable 7 prints `0` and `0` for the same named arms, units, displayed arm Ns, and median/IQR convention.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [Supplement 3 eTable 2 — PDF p. 7](../joi190106supp3_prod_1635377898.49725.pdf#page=7); [Supplement 3 eTable 7 — PDF p. 19](../joi190106supp3_prod_1635377898.49725.pdf#page=19).

**Source evidence:** ETable 2 gives intervention/control `33 (0, 29)` and `4 (0, 29)` g/week. ETable 7 gives `0 (0, 29)` in both arms. Each table displays N=3,272/N=3,311.

**Reported-versus-comparator:** Intervention is 33 versus 0 g/week and control is 4 versus 0 g/week; IQR endpoints match.

**Reasoning procedure:** Match baseline measure, unit, arm, displayed Ns, and summary convention across the two all-randomized tables.

**Calculation:** The printed median differences are `33 − 0 = 33` and `4 − 0 = 4` g/week. Integer display precision does not reconcile either difference.

**Alternative source-grounded interpretations:** ETable 7 may use an unstated analysis-specific baseline subset or handling path despite the identical displayed arm Ns.

**Mechanical evidence recheck:** Both direct pages, headings, Ns, medians, IQRs, and units were confirmed. Row-specific baseline records, denominators, and calculation output are absent.

**Quality-control relevance:** Matched baseline summaries need an explicit population or handling distinction when their printed values differ.

**Potential downstream evidence impact:** If confirmed, an extractor could select different baseline red-wine medians depending on the table used. No propagation or conclusion change is established.

**Human verification steps:** Identify the row-level baseline records, denominators, and handling rule for each table and recompute both summaries.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — PDQS baseline mean differs between the principal and baseline-value-carried-forward tables

**Adjudication status:** Pending Human Adjudication

**Candidate statement:** Main Table 2 prints baseline PDQS mean 21.1 in both arms, while eTable 6 prints 21.0 in both arms under the same displayed arm Ns and 0-42 scale.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [main article Table 2 — PDF p. 5](../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5); [Supplement 3 eTable 6 — PDF p. 16](../joi190106supp3_prod_1635377898.49725.pdf#page=16).

**Source evidence:** Main Table 2 gives `21.1 (3.7)` in both arms; eTable 6 gives `21.0 (3.7)` in both arms with N=3,272/N=3,311.

**Reported-versus-comparator:** Each arm mean is 21.1 versus 21.0; the printed SDs and Ns match.

**Reasoning procedure:** Match the scale, baseline time point, arms, displayed Ns, and mean/SD convention before comparing one-decimal means.

**Calculation:** `21.1 − 21.0 = 0.1` point in each arm; SD difference is 0.0.

**Alternative source-grounded interpretations:** An unstated analysis-specific baseline set, unreported unrounded values, or different rounding/truncation may account for the difference.

**Mechanical evidence recheck:** Both direct pages confirm the pairs, scale, Ns, and summary type. Row-level denominators, unrounded means, and software output are unavailable.

**Quality-control relevance:** A baseline score shown in two displays should be matchable or explicitly population-qualified.

**Potential downstream evidence impact:** If confirmed, an extractor could record 21.0 or 21.1 as the baseline PDQS mean. This 0.1-point display difference is not evidence of a changed trial conclusion.

**Human verification steps:** Compare exact PDQS baseline records, row denominators, unrounded means, and rounding rules for both displays.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — intervention baseline energy SD differs between Table 3 and eTable 8

**Adjudication status:** Pending Human Adjudication

**Candidate statement:** Intervention baseline energy is 2355 kcal/d in both displays, but its SD is 555 in Table 3 and 544 in eTable 8; the matched control entry agrees.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [main article Statistical Analysis — PDF p. 4](../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4); [main article Table 3 — PDF p. 7](../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=7); [Supplement 3 eTable 8 — PDF p. 21](../joi190106supp3_prod_1635377898.49725.pdf#page=21).

**Source evidence:** Table 3 gives intervention/control `2355 (555)`/`2369 (555)` kcal/d. ETable 8 gives `2,355 (544)`/`2,369 (555)` under the same displayed arm Ns. The main article states that follow-up, not baseline, values were imputed in the main analysis.

**Reported-versus-comparator:** Intervention SD is 555 versus 544; intervention mean and both control fields match.

**Reasoning procedure:** Match baseline energy, unit, arm, displayed N, and mean/SD label across the two displays.

**Calculation:** `555 − 544 = 11` kcal/d. Integer rounding of one common SD cannot produce both printed integers.

**Alternative source-grounded interpretations:** ETable 8 may use an unstated baseline set or separate extraction; one SD may instead be a production error.

**Mechanical evidence recheck:** Direct pages confirm means, SDs, units, Ns, and the baseline-imputation statement. Participant records, row denominator, SD convention, and calculation output are unavailable.

**Quality-control relevance:** Dispersion is a separately extractable baseline quantity.

**Potential downstream evidence impact:** If confirmed, an extractor could copy 544 or 555 as the intervention baseline energy SD for descriptive or variance-based reuse. No conclusion impact is demonstrated.

**Human verification steps:** Recompute the intervention baseline energy SD for each table’s exact row population and inspect table-generation output.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — baseline body-weight summaries differ between Table 1 and eTable 9

**Adjudication status:** Pending Human Adjudication

**Candidate statement:** Table 1 and the all-randomized eTable 9 panel print different baseline weight means in both arms and a different intervention SD despite the same displayed arm Ns.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [main article Table 1 — PDF p. 4](../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4); [Supplement 3 eTable 9 — PDF p. 23](../joi190106supp3_prod_1635377898.49725.pdf#page=23).

**Source evidence:** Table 1 prints `86.7 (13.0)`/`86.4 (13.0)` kg. ETable 9 prints `86.5 (12.9)`/`86.3 (13.0)` kg with N=3,272/N=3,311.

**Reported-versus-comparator:** Intervention mean differs by 0.2 kg and SD by 0.1 kg; control mean differs by 0.1 kg and control SD matches.

**Reasoning procedure:** Match baseline weight, unit, arm, displayed N, and mean/SD convention, then compare each printed field.

**Calculation:** `86.7 − 86.5 = 0.2`, `13.0 − 12.9 = 0.1`, `86.4 − 86.3 = 0.1`, and `13.0 − 13.0 = 0.0` kg.

**Alternative source-grounded interpretations:** ETable 9 may use an outcome-specific baseline set or processing path while displaying the overall arm N.

**Mechanical evidence recheck:** Both direct pages confirm all values and labels. Row-specific weight denominators, participant values, unrounded outputs, and baseline handling are unavailable.

**Quality-control relevance:** Arm-specific baseline means and SDs should carry an explicit population distinction when they differ.

**Potential downstream evidence impact:** If confirmed, a baseline-characteristics extractor could copy different weight summaries from the article and supplement. No occurrence or conclusion change is asserted.

**Human verification steps:** Establish row denominators and baseline handling for both tables, then regenerate arm-specific means and SDs.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — baseline BMI means differ between Table 1 and eTable 9

**Adjudication status:** Pending Human Adjudication

**Candidate statement:** Table 1 prints baseline BMI mean 32.5 in both arms, while the all-randomized eTable 9 panel prints 32.6 in both arms with the same displayed arm Ns and matching SDs.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [main article Table 1 — PDF p. 4](../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4); [Supplement 3 eTable 9 — PDF p. 23](../joi190106supp3_prod_1635377898.49725.pdf#page=23).

**Source evidence:** Table 1 prints `32.5 (3.4)`/`32.5 (3.5)`; eTable 9 prints `32.6 (3.4)`/`32.6 (3.5)` kg/m² under N=3,272/N=3,311.

**Reported-versus-comparator:** Each arm mean differs by 0.1 kg/m²; the SDs match.

**Reasoning procedure:** Match baseline BMI, unit/derivation, arms, displayed Ns, and mean/SD convention, then compare one-decimal means.

**Calculation:** `32.6 − 32.5 = 0.1` kg/m² in each arm; SD differences are zero.

**Alternative source-grounded interpretations:** Different participant records, individual-level derivation paths, or rounding conventions may have been used despite identical displayed group Ns.

**Mechanical evidence recheck:** Both direct pages confirm values, units, arm Ns, and BMI definition. Participant-level height/weight, row denominators, unrounded BMI, and derivation order are absent.

**Quality-control relevance:** A baseline BMI mean has two printed one-decimal values without a stated population or derivation distinction.

**Potential downstream evidence impact:** If confirmed, an extractor could record 32.5 or 32.6 as the arm baseline BMI mean. No paper-level interpretation change is established.

**Human verification steps:** Reproduce BMI using the exact records and derivation/rounding rules used for both tables.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Figure 4 threshold labels do not preserve the Methods boundary operators

**Adjudication status:** Pending Human Adjudication

**Candidate statement:** Methods defines clinically meaningful changes with inclusive `at least` boundaries, while Figure 4 prints strict greater-than signs for ten classifications and omits the diastolic operator.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [main article Outcomes — PDF p. 4](../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4); [main article Figure 4 — PDF p. 10](../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10).

**Source evidence:** Methods uses `at least` for 5% weight/BMI/waist/lipid thresholds, 5 mm Hg systolic, 2.5 mm Hg diastolic, and 5% HDL; it specifies a 10% triglyceride reduction. Figure 4 prints `>5%`, `>10%`, and `>5 mm Hg`; the diastolic label is `Reduction 2.5 mm Hg` without an operator.

**Reported-versus-comparator:** Inclusive `≥ x` includes equality, strict `> x` excludes it, and the diastolic figure label states neither operator.

**Reasoning procedure:** Match each outcome and threshold magnitude across Methods and Figure 4, then compare the natural-language and symbolic operators.

**Calculation:** For the percentage and systolic classifications, `≥ x` and `> x` differ at exactly x. For diastolic blood pressure, `≥ 2.5` is compared with an operator-free `2.5` label.

**Alternative source-grounded interpretations:** Figure `>` may be compact typography for the inclusive Methods rule, and the omitted diastolic operator may be typographic. Identical percentages could occur if no observation lay exactly at a boundary.

**Mechanical evidence recheck:** Both direct pages confirm the threshold magnitudes and wording. Classification code, measurement precision, and boundary-case counts are unavailable.

**Quality-control relevance:** The boundary operator defines which observations are classified as clinically meaningful changes.

**Potential downstream evidence impact:** If confirmed, an extractor could encode an inclusive or strict threshold differently when reusing the outcome definition. The package does not establish changed percentages or a changed conclusion.

**Human verification steps:** Inspect classification code and boundary-case counts; identify the implemented operator before harmonizing labels.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — eTable 4 total-olive-oil baseline row conflicts with the table’s median/IQR convention

**Adjudication status:** Pending Human Adjudication

**Candidate statement:** ETable 4 labels total-olive-oil baseline as mean (SD) but prints `350 (175, 350)` while its footnote and parallel food tables define that form as median (IQR).

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Supplement 3 eTable 4 row — PDF p. 10](../joi190106supp3_prod_1635377898.49725.pdf#page=10); [Supplement 3 eTable 4 footnote — PDF p. 11](../joi190106supp3_prod_1635377898.49725.pdf#page=11); [Supplement 3 eTable 2 comparator — PDF p. 3](../joi190106supp3_prod_1635377898.49725.pdf#page=3); [Supplement 3 eTable 7 comparator — PDF p. 17](../joi190106supp3_prod_1635377898.49725.pdf#page=17).

**Source evidence:** P. 10 prints `Baseline, mean (SD)` and `350 (175, 350)` in both arms. P. 11 says baseline food data are median (IQR); eTables 2 and 7 label matching total-olive-oil triples median (IQR).

**Reported-versus-comparator:** The row label assigns mean/SD, while the table footnote and parallel displays assign median/Q1/Q3 to the same three-value form.

**Reasoning procedure:** Compare the row-specific statistic label with the table-wide footnote and matched total-olive-oil baseline labels in parallel tables.

**Calculation:** Under median (IQR), the triple maps to median 350, Q1 175, and Q3 350. Under mean (SD), two parenthetical values are supplied where one SD would ordinarily be defined; the statistic types do not reconcile without an explicit exception.

**Alternative source-grounded interpretations:** A row-specific convention may exist but is not printed; otherwise the row label may be localized production text inconsistent with the footnote.

**Mechanical evidence recheck:** Direct rendered pages confirm row label, values, footnote, and parallel comparators. Baseline denominator, participant values, calculation output, and any exception are absent.

**Quality-control relevance:** Mean/SD and median/IQR are distinct extractable summary types.

**Potential downstream evidence impact:** If confirmed, an extractor could classify `350 (175, 350)` as mean/SD rather than median/IQR. No downstream occurrence or paper-level conclusion effect is established.

**Human verification steps:** Inspect baseline calculations and table-production source to identify the intended statistic type and fields.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed, the observations could affect how a later extractor transcribes an arm label, baseline summary, dispersion value, threshold rule, or summary-statistic type into a systematic review, meta-analysis, guideline evidence table, or other downstream evidence product. This is a bounded extraction risk only. The supplied package does not establish that any value propagated, that a meta-analysis or guideline used it, or that the paper’s conclusions would change.

## Limitations and Missing Definitions

The complete limitations register is [limitations.md](review_1_5_1/limitations.md). In brief, no participant-level data, analysis code, table-production source, or source-supported replacement values are supplied. Row-specific baseline denominators, unrounded summaries, quantile and SD computation details, BMI derivation order, and Figure 4 classification code are unavailable where relevant. The supplied statistical reporting does not provide contrast-specific SEs, test statistics, degrees of freedom, covariance, variance estimators, or a calculation rule that would support exact CI-to-P reconstruction. Graphical figure coordinates were not invented. These limitations do not remove any mapped source unit or stable candidate.

## Human Adjudication Checklist

- Confirm each cited direct-source location and printed transcription.
- Determine whether the compared displays have the same population, time point, estimand, handling rule, and calculation path.
- Inspect author-controlled source data, analysis code, and table-production outputs where available.
- Record decisions only in the five blank fields in each candidate card, retaining the source evidence and ID.
- Do not infer a replacement value or paper-level conclusion change from this quality-control report alone.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

The complete durable-artifact record is [coverage_manifest.md](review_1_5_1/coverage_manifest.md). Pre-review direct-source and reused-artifact checksums are linked above. Direct PDFs were treated read-only; source-matched text, OCR, rendering, and maps were reused only as aids, while cited PDF pages are the authoritative evidence. Final post-assembly hash comparison and mechanical validation are coordinator completion steps.

### Agent execution

[agent_execution_manifest.md](review_1_5_1/agent_execution_manifest.md) records the coordinator and all specialist agents. The validator-safe normalized runtime IDs for the two independent statistical passes are `root/statistics_pass_1` and `root/statistics_pass_2`, both `gpt-5.6-terra` at `high` reasoning effort and `FRESH_SPAWN` start mode. The report generator is `root/report_generator`, `gpt-5.6-terra` at `medium` effort and `FRESH_SPAWN` mode.

### Performance profile

- **Target basis:** Five supplied PDFs totaling 149 pages; 43 source-matched reusable page units and 106 fresh direct-source page units; one 75-page protocol, one 30-page SAP, a 29-page results supplement with multiple tables/figures, mixed native/layout and visual-table needs, and the required two full statistical passes and evidence audits. This is moderately larger than the 102-page/81-fresh calibration package.
- **Total source units:** 149
- **Fresh-source units:** 106
- **Target elapsed minutes:** 50-85
- **Started UTC:** 2026-08-18T23:15:34Z
- **Finished UTC:** 2026-08-18T23:53:15Z
- **Observed elapsed minutes:** 37.7
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Input tokens | Cached input tokens | Cache-write tokens | Output tokens | Reasoning tokens | Total tokens | Known token cost (USD) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.6-sol | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 |
| gpt-5.6-terra | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 |

Per-agent and per-model accounting detail is in [token_usage_summary.md](review_1_5_1/token_usage_summary.md) after the accounting window closes. Totals count input plus output tokens only; cached input and cache-write are input subsets, and reasoning is an output subset. Any listed amount is a token-only API-equivalent estimate under the dated pricing snapshot, not an invoice; non-token tools, containers, storage, subscriptions, taxes, and other vendor charges are excluded.
