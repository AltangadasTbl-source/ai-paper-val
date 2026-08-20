# Evidence Quality Audit

This is a neutral quality-control audit of the complete workflow 1.5.1 evidence chain. It does not assign severity, scientific disposition, acceptance, rejection, or a correction. Every stable candidate remains **Pending Human Adjudication**.

## Coverage and execution audit

- **Direct-source closure:** Five supplied PDFs contain 149 stable PDF-page units. The five `source_coverage.md` rows reconcile exactly: 43 reusable units plus 106 fresh-required units equal 149 total units, and 149 mapped units equal 149 total units. Each row is `COMPLETE`.
- **Reusable and fresh-required closure:** DOC-001 pp. 1-14 and DOC-004 pp. 1-29 have source-matched reusable coverage. DOC-002 pp. 1-75, DOC-003 pp. 1-30, and DOC-005 p. 1 were freshly extracted and mapped. The mapping artifacts explicitly record result-relevant content or a no-applicable-unit determination for every page.
- **Integrity:** All five current direct-source SHA-256 values match `source_hashes_before.sha256`. All 98 nonblank entries in `reused_artifact_hashes_before.sha256` recheck successfully against the current reusable artifacts.
- **Coverage manifest:** The manifest has 33 data rows, and each Artifact cell contains one plain relative path. At audit time 31 rows were `COMPLETE`; the `evidence_quality` and `report_generation` rows remained `PENDING`. Every artifact named by a complete row resolved locally. This audit creates `quality/evidence_quality_audit.md`; the coordinator must update that row to `COMPLETE`. The report-generation path and status cannot close until the report generator writes the canonical report.
- **Statistical manifest scopes:** The `statistics_pass_1` and `statistics_pass_2` coverage rows enumerate every individual ID from S001 through S777 and name one artifact each.
- **Relationship closure:** The canonical numeric inventory contains N001 through N269, with all 269 receiving a coherent, no-applicable, or candidate record. The canonical statistical inventory contains S001 through S777. Both statistical checker artifacts, the appended inventory register, and the repaired coverage-manifest rows record full pass coverage.
- **Statistical execution:** `agent_execution_manifest.md` records two distinct fresh statistical agents: `/root/statistics_pass_1` and `/root/statistics_pass_2`, each using `gpt-5.6-terra`, `high`, and `FRESH_SPAWN`. Pass 1 covers S001-S777 before stable registration; pass 2 revisits S001-S777 after C001-C008 and the mechanical recheck, emits the distinct later observation registered as C009, and C009 has a subsequent source recheck.
- **Execution-manifest completion:** The current coordinator and all specialists used through this audit appear once with one primary artifact. The coordinator must add the report generator and any later repair agent when those model calls occur.
- **No count boundary:** Current 1.5.1 inventories, mappings, checkers, and the stable ledger consistently state complete source/relationship scope and no candidate limit. The reusable-asset inventory marks legacy selection material stale and says it was not used as discovery scope. No durable artifact contains a top-N queue, deferred-by-cap set, ranked subset, or stopping rule based on the nine-candidate count.
- **Display-zero exclusion:** No `P = 0`, `p = 0.000`, or equivalent display zero occurs in S001-S777, and no stable card mentions one. No candidate relies on finite precision, underflow, or nonzero-tail reasoning; therefore the conditional independent-contradiction field is not applicable to C001-C009.
- **Stable-ID closure:** `candidate_ledger.md` and `verification/evidence_recheck.md` each contain exactly C001, C002, C003, C004, C005, C006, C007, C008, and C009. This audit returns the same set. The final report must return the same set without deletion, merger, renumbering, ranking, or suppression.
- **Category and tone:** Every stable card uses exactly one category from `QUALITY_CONTROL_SCOPE.md` and uses neutral quality-control wording. The preliminary QC-X0002 checker category was repaired to the single category `Cross-document numeric inconsistency`, and its closing section now uses neutral follow-up wording.
- **Mapper cross-reference:** The support mapping correctly assigns DOC-003 pp. 25-27 to SUP-S008-S012; the earlier false SUP-S011-S018 cross-reference was repaired without changing scientific scope.

## Candidate-card audit conventions

For each stable ID below, direct observations are separated from explanations, calculations are reproducible from printed inputs, missing definitions are named, potential duplicate relationships are assessed under the workflow's same-values/same-comparator/same-rule test, and potential downstream impact is bounded to what an evidence extractor could copy if a human confirms the observation. The source pages were checked directly from the supplied PDFs; no cited pagination is false.

## C001 — eTable 2 assigns the N=3,311 column a second intervention-group label

- **Candidate statement:** The opening eTable 2 header labels both N=3,272 and N=3,311 as intervention, while the same continued table and main Table 2 identify N=3,311 as control.
- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** DOC-004 PDF pp. 3 and 5; DOC-001 PDF p. 5. All cited PDF-page links in the ledger and recheck resolve to these direct sources and end in truthful page fragments.
- **Source evidence:** DOC-004 p. 3 prints `Intervention group` over both Ns. DOC-004 p. 5 prints `Control group` over N=3,311. DOC-001 p. 5 also identifies n=3311 as control.
- **Reported-versus-comparator:** N=3,311 is paired with `Intervention group` on the opening page and `Control group` on the continuation and main table.
- **Reasoning procedure:** Match the same continued-table column by arm N, then compare its group label. This is a text-identity rule; it does not reconstruct any effect estimate.
- **Calculation:** `N=3,311 + Intervention group` conflicts with `N=3,311 + Control group` under a fixed two-arm table structure.
- **Observation and inference boundary:** The inconsistent printed labels are direct observations. A localized table-production error and the inference that the numerical column still contains control data are possible explanations, not source facts.
- **Alternative source-grounded interpretations:** A table-specific group definition could resolve the wording, but none is printed. The continuation structure instead supports consistent arm ordering.
- **Mechanical evidence recheck:** All cited text, arm Ns, and continuation identity were found on the direct rendered pages. No numeric input is missing for the label comparison; the intended production heading remains unavailable.
- **Duplicate-relationship audit:** C001 is not a duplicate of C009. They involve different tables, labels, comparators, and rules. Shared table-production mechanisms would not make them the same relationship.
- **Quality-control relevance:** A treatment-arm label determines which column a reader attributes to intervention or control.
- **Potential downstream evidence impact:** If confirmed, an extractor could assign eTable 2 baseline or change values to the wrong arm. The supplied package does not establish that this occurred or that any paper-level conclusion changes.
- **Human verification steps:** Inspect the table-production source; confirm the intended N=3,311 header and whether all p. 3 values follow the continuation's control-arm ordering.
- **Exact remaining human question:** Is the N=3,311 heading on DOC-004 p. 3 intended to read `Control group`, and does the column contain control values throughout?
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — eTable 2 red-wine median lies above its printed upper quartile

- **Candidate statement:** The eTable 2 intervention baseline red-wine entry is `33 (0, 29)` under a median (IQR) convention, placing the median above Q3.
- **Category:** Numeric or arithmetic inconsistency.
- **Exact source locations:** DOC-004 PDF p. 7; the ledger and recheck link to the direct page truthfully.
- **Source evidence:** The row prints `33 (0, 29)` g/week, and the same page states that baseline data are median (IQR).
- **Reported-versus-comparator:** Printed median 33 is compared with printed Q1 0 and Q3 29.
- **Reasoning procedure:** Apply the necessary quartile-order identity `Q1 <= median <= Q3` to the printed triple.
- **Calculation:** `0 <= 33 <= 29` is false because `33 - 29 = 4` g/week. Integer display rounding cannot remove the four-unit ordering conflict.
- **Observation and inference boundary:** The triple and summary convention are direct observations. Which field or row alignment is unintended cannot be inferred from the package.
- **Alternative source-grounded interpretations:** The median, upper quartile, or row alignment may contain a production error; participant-level data and intended values are absent.
- **Mechanical evidence recheck:** The row and footnote were found together on the direct source page, and the ordering calculation reproduces exactly.
- **Duplicate-relationship audit:** C002 and C003 share the eTable 2 value but are not duplicates. C002 tests internal quartile ordering within one entry; C003 compares baseline medians across two tables.
- **Quality-control relevance:** The printed summary is internally impossible under its stated convention.
- **Potential downstream evidence impact:** If confirmed, a data extractor could copy an impossible baseline median/IQR into a descriptive table or sensitivity-analysis comparison. No conclusion effect is established.
- **Human verification steps:** Recalculate the intervention red-wine quartiles from the intended baseline records and inspect the table-production row alignment.
- **Exact remaining human question:** What participant set and quantile calculation produced this entry, and what median, Q1, and Q3 were intended?
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — all-randomized red-wine baseline summaries differ between eTables 2 and 7

- **Candidate statement:** ETable 2 prints red-wine baseline medians `33` and `4`, whereas eTable 7 prints `0` and `0` for the same named arms, units, displayed arm Ns, and median/IQR convention.
- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-004 PDF pp. 7 and 19; both cited links and page numbers are truthful.
- **Source evidence:** ETable 2 gives intervention/control `33 (0, 29)` and `4 (0, 29)`. ETable 7 gives `0 (0, 29)` in both arms. Both print N=3,272/N=3,311 and g/week.
- **Reported-versus-comparator:** Intervention medians differ by `33 - 0 = 33` g/week; control medians differ by `4 - 0 = 4` g/week; the IQR endpoints match.
- **Reasoning procedure:** Match baseline measure, unit, arm labels, displayed Ns, and summary convention across the two all-randomized sensitivity tables, then compare the printed fields.
- **Calculation:** The two arm-specific differences are 33 and 4 g/week, respectively. No display rounding at integer precision reconciles either difference.
- **Observation and inference boundary:** The printed mismatches are direct. The stronger claim that follow-up missing-value handling cannot affect these rows assumes identical baseline records; row-specific records and denominators are not supplied.
- **Alternative source-grounded interpretations:** ETable 7 may use an unstated analysis-specific baseline subset or handling path despite the same displayed arm Ns. The headings do not document that distinction.
- **Mechanical evidence recheck:** Both direct pages, headings, Ns, medians, IQRs, and units were found; calculations reproduce. Missing inputs are the row-specific baseline records, denominators, and analysis code.
- **Duplicate-relationship audit:** C003 is distinct from C002 because the comparator and rule differ. It also is not merged with C004-C007, which concern different variables and table pairs.
- **Quality-control relevance:** Cross-table baseline summaries should be matchable or explicitly population-qualified for extraction.
- **Potential downstream evidence impact:** If confirmed, an extractor could select different baseline red-wine medians depending on the supplement table used. The package does not show that such reuse occurred or that study conclusions change.
- **Human verification steps:** Identify the exact baseline records and denominator used by each table; recompute both arm summaries under their documented handling rules.
- **Exact remaining human question:** Which baseline population and handling rule produced each red-wine row, and what medians should each table report?
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — PDQS baseline mean differs between the principal and baseline-value-carried-forward tables

- **Candidate statement:** Main Table 2 prints baseline PDQS mean 21.1 in both arms, while eTable 6 prints 21.0 in both arms under the same displayed arm Ns and 0-42 scale.
- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 PDF p. 5 and DOC-004 PDF p. 16; both page citations are truthful.
- **Source evidence:** Main Table 2 prints `21.1 (3.7)`/`21.1 (3.7)`; eTable 6 prints `21.0 (3.7)`/`21.0 (3.7)` with N=3,272/N=3,311.
- **Reported-versus-comparator:** Each arm's mean differs by `21.1 - 21.0 = 0.1` point; SDs and displayed Ns match.
- **Reasoning procedure:** Match measure, baseline time, scale, arms, displayed Ns, and mean/SD convention, then compare at the printed one-decimal precision.
- **Calculation:** Both arm differences equal 0.1 point, and both SD differences equal 0.0.
- **Observation and inference boundary:** The displayed differences are direct. Identical displayed Ns do not prove identical row-level baseline records; asserting which mean is intended would be unsupported.
- **Alternative source-grounded interpretations:** An unstated analysis-specific baseline set, unreported unrounded values, or a different rounding/truncation path could account for the difference.
- **Mechanical evidence recheck:** The direct pages confirm both pairs, scale, Ns, and summary type. Row-specific denominators, unrounded means, and software output are missing.
- **Duplicate-relationship audit:** C004 is a separate PDQS relationship and is not merged with the weight, BMI, energy, or red-wine comparisons.
- **Quality-control relevance:** A baseline score used for cross-table comparison has two printed values without a stated distinction.
- **Potential downstream evidence impact:** If confirmed, an extractor could record 21.0 or 21.1 as the arm baseline PDQS mean. The 0.1-point display difference is not evidence of a changed trial conclusion.
- **Human verification steps:** Compare exact PDQS baseline records, row denominators, unrounded means, and rounding rules for the two displays.
- **Exact remaining human question:** Were identical baseline inputs used, and what unrounded values and rounding rule produced 21.1 versus 21.0?
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — intervention baseline energy SD differs between Table 3 and eTable 8

- **Candidate statement:** The intervention baseline energy mean is 2355 kcal/d in both displays, but its SD is 555 in main Table 3 and 544 in eTable 8; the matched control entry agrees.
- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 PDF pp. 4 and 7; DOC-004 PDF p. 21. The pagination and links are truthful.
- **Source evidence:** Table 3 gives intervention/control `2355 (555)`/`2369 (555)`. ETable 8 gives `2,355 (544)`/`2,369 (555)` under the same displayed arm Ns. DOC-001 p. 4 says follow-up, not baseline, values were imputed in the main analysis.
- **Reported-versus-comparator:** Intervention SD 555 versus 544; intervention mean and both control fields match.
- **Reasoning procedure:** Match baseline energy, kcal/d, arm, displayed N, and mean/SD label across locations, then compare the displayed dispersion field.
- **Calculation:** `555 - 544 = 11` kcal/d. Integer rounding of one common SD cannot produce both displayed integers.
- **Observation and inference boundary:** The 11-unit printed difference is direct. The source does not establish identical row-specific baseline denominators or which calculation is intended.
- **Alternative source-grounded interpretations:** ETable 8 may use an unstated baseline set or separate extraction; one SD may instead be a production error.
- **Mechanical evidence recheck:** The source pages confirm the means, SDs, units, Ns, and main baseline-imputation statement. Participant records, row denominator, SD convention, and calculation output are unavailable.
- **Duplicate-relationship audit:** C005 is distinct from C004, C006, and C007 because its measure, table pair, printed field, and comparator differ.
- **Quality-control relevance:** Dispersion is a distinct extractable quantitative field used to describe baseline variability.
- **Potential downstream evidence impact:** If confirmed, an extractor could copy 544 or 555 as the intervention baseline energy SD, affecting a descriptive or variance-based reuse. No paper-level conclusion impact is demonstrated.
- **Human verification steps:** Recompute the intervention baseline energy SD for each table's exact row population and inspect the table-generation output.
- **Exact remaining human question:** What baseline denominator, records, SD definition, and output produced 555 and 544?
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — baseline body-weight summaries differ between Table 1 and eTable 9

- **Candidate statement:** Table 1 and the all-randomized eTable 9 panel print different baseline weight means in both arms and a different intervention SD despite the same displayed arm Ns.
- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 PDF p. 4 and DOC-004 PDF p. 23; both citations are truthful.
- **Source evidence:** Table 1 prints `86.7 (13.0)`/`86.4 (13.0)` kg. ETable 9 prints `86.5 (12.9)`/`86.3 (13.0)` kg with N=3,272/N=3,311.
- **Reported-versus-comparator:** Intervention mean differs by 0.2 kg and SD by 0.1 kg; control mean differs by 0.1 kg and control SD matches.
- **Reasoning procedure:** Match baseline weight, kg, arm, displayed N, and mean/SD convention, then compare each printed field.
- **Calculation:** `86.7 - 86.5 = 0.2`, `13.0 - 12.9 = 0.1`, `86.4 - 86.3 = 0.1`, and `13.0 - 13.0 = 0.0` kg.
- **Observation and inference boundary:** The displayed differences are direct. Overall arm Ns do not prove identical nonmissing weight records, and no correction can be selected from the PDFs.
- **Alternative source-grounded interpretations:** ETable 9 may use an outcome-specific baseline set or processing path while displaying the overall arm N. Neighboring completer values do not identify whether entries were copied or recalculated.
- **Mechanical evidence recheck:** Both direct pages confirm all printed fields and labels. Row-specific weight denominators, participant values, unrounded outputs, and baseline handling are missing.
- **Duplicate-relationship audit:** C006 and C007 share the table pair and may share a production mechanism, but different measures and derivations make them distinct relationships under the contract.
- **Quality-control relevance:** Arm-specific baseline means and SDs are separately extractable values that should carry an explicit population distinction when they differ.
- **Potential downstream evidence impact:** If confirmed, a baseline-characteristics extractor could copy different weight summaries from the main article and supplement. No occurrence or conclusion change is asserted.
- **Human verification steps:** Establish exact row denominators and baseline handling for both tables and regenerate arm-specific means and SDs.
- **Exact remaining human question:** Which baseline records, denominators, and rounding rules underlie each weight display?
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — baseline BMI means differ between Table 1 and eTable 9

- **Candidate statement:** Table 1 prints baseline BMI mean 32.5 in both arms, while the all-randomized eTable 9 panel prints 32.6 in both arms with the same displayed arm Ns and matching SDs.
- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 PDF p. 4 and DOC-004 PDF p. 23; both cited pages are truthful.
- **Source evidence:** Table 1 prints `32.5 (3.4)`/`32.5 (3.5)`; eTable 9 prints `32.6 (3.4)`/`32.6 (3.5)` kg/m2 under N=3,272/N=3,311.
- **Reported-versus-comparator:** Each arm mean differs by 0.1 kg/m2; SDs match.
- **Reasoning procedure:** Match baseline BMI, unit/derivation, arms, displayed Ns, and mean/SD convention, then compare one-decimal means.
- **Calculation:** `32.6 - 32.5 = 0.1` kg/m2 in each arm; SD differences are zero.
- **Observation and inference boundary:** The printed difference is direct. Whether BMI was recomputed from different inputs, rounded differently, or summarized on a different set is not stated.
- **Alternative source-grounded interpretations:** The tables may use different participant records, individual-level derivation paths, or rounding conventions despite the same displayed group Ns.
- **Mechanical evidence recheck:** Both direct pages confirm values, units, arm Ns, and BMI definition. Participant-level height/weight, row denominators, unrounded BMI, and derivation order are absent.
- **Duplicate-relationship audit:** C007 is not merged with C006 because BMI and weight are different reported quantities, even if a shared processing mechanism is possible.
- **Quality-control relevance:** The baseline BMI mean has two printed one-decimal values without a stated population or derivation distinction.
- **Potential downstream evidence impact:** If confirmed, an extractor could record 32.5 or 32.6 as the arm baseline BMI mean. No change in paper-level interpretation is established.
- **Human verification steps:** Reproduce BMI from the exact records and derivation/rounding rules used for both tables.
- **Exact remaining human question:** Were identical records and BMI derivation steps used, and what unrounded means produced 32.5 versus 32.6?
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Figure 4 threshold labels do not preserve the Methods boundary operators

- **Candidate statement:** Methods defines clinically meaningful changes with inclusive `at least` boundaries, while Figure 4 prints strict greater-than signs for ten classifications and omits the diastolic operator.
- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** DOC-001 PDF pp. 4 and 10; direct page citations are truthful.
- **Source evidence:** Methods uses `at least` for 5% weight/BMI/waist/lipid thresholds, 5 mm Hg systolic, 2.5 mm Hg diastolic, and 5% HDL; it specifies a 10% triglyceride reduction. Figure 4 prints `>5%`, `>10%`, and `>5 mm Hg`, while its diastolic label is `Reduction 2.5 mm Hg` without an operator.
- **Reported-versus-comparator:** Inclusive `>= x` and strict `> x` differ at equality; the diastolic figure label does not state either operator.
- **Reasoning procedure:** Match each outcome and threshold magnitude across Methods and Figure 4, then translate the natural-language and symbol operators logically.
- **Calculation:** For nine percentage classifications and systolic blood pressure, `>= x` includes values equal to x while `> x` excludes them. For diastolic blood pressure, `>= 2.5` is compared with an operator-free `2.5` label.
- **Observation and inference boundary:** The operator wording is direct. Whether the analysis code used inclusive or strict comparisons and whether any participant lay exactly at a threshold cannot be inferred from the percentages.
- **Alternative source-grounded interpretations:** Figure `>` may be compact typography for the inclusive Methods rule, and the diastolic operator may be a typographic omission. Identical percentages could result if no observation was on a boundary.
- **Mechanical evidence recheck:** All threshold magnitudes and operators were found on the direct pages. Classification code, measurement precision, and boundary-case counts are unavailable.
- **Duplicate-relationship audit:** C008 is one repeated label-boundary rule across 11 Figure 4 outcomes. The shared comparator and consistency rule justify one stable candidate rather than 11 separate IDs.
- **Quality-control relevance:** The boundary operator defines which observations are classified as clinically meaningful changes.
- **Potential downstream evidence impact:** If confirmed, an extractor could encode an inclusive or strict threshold differently when reusing the outcome definition. The package does not establish changed percentages or a changed conclusion.
- **Human verification steps:** Inspect classification code and boundary-case counts; identify the implemented operator and harmonize only after human adjudication.
- **Exact remaining human question:** Which operator and measurement precision were implemented for each Figure 4 classification, and how should the Methods and figure labels state that rule?
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — eTable 4 total-olive-oil baseline row conflicts with the table's median/IQR convention

- **Candidate statement:** ETable 4 labels total-olive-oil baseline as mean (SD) but prints a three-value form `350 (175, 350)` while its footnote and parallel food tables define that form as median (IQR).
- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** DOC-004 PDF pp. 10 and 11, with matched comparators on pp. 3 and 17. All links and page fragments are truthful.
- **Source evidence:** P. 10 prints `Baseline, mean (SD)` and `350 (175, 350)` in both arms. P. 11 states that baseline data are median (IQR). ETable 2 p. 3 and eTable 7 p. 17 label the identical values median (IQR).
- **Reported-versus-comparator:** The row label assigns a mean/SD convention, while the table footnote and parallel rows assign median/Q1/Q3 to the same display structure.
- **Reasoning procedure:** Compare the row-specific statistic label with the table-wide footnote and the matched total-olive-oil baseline labels in parallel tables.
- **Calculation:** Under median (IQR), the triple maps to median 350, Q1 175, and Q3 350. Under the printed mean (SD) label, two parenthetical values are supplied where one SD would ordinarily be defined. The statistic types therefore do not reconcile without an exception.
- **Observation and inference boundary:** The label conflict and identical parallel triples are direct. Treating `mean (SD)` as the production error or deciding the intended statistic requires unavailable records.
- **Alternative source-grounded interpretations:** A row-specific convention may exist but is not printed; otherwise the row label may be localized production text inconsistent with its table footnote.
- **Mechanical evidence recheck:** Direct rendered pages confirm row label, values, footnote, neighboring conventions, and parallel comparators. Baseline row denominator, participant values, calculation output, and any exception are absent.
- **Duplicate-relationship audit:** C009 is distinct from C001 because it concerns summary-statistic type rather than treatment-arm identity and uses different comparators and rules.
- **Quality-control relevance:** Mean/SD and median/IQR are different extractable summary types and should not label one display interchangeably.
- **Potential downstream evidence impact:** If confirmed, an extractor could classify `350 (175, 350)` as mean/SD rather than median/IQR. No downstream occurrence or paper-level conclusion effect is established.
- **Human verification steps:** Inspect completer baseline calculations and the table-production source; identify the intended statistic type and fields.
- **Exact remaining human question:** What baseline participant set and calculation produced the triple, and is the row intended as median (IQR) or supported by a documented mean (SD) exception?
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Audit completion status

- **Stable IDs covered:** C001, C002, C003, C004, C005, C006, C007, C008, C009.
- **Per-card arithmetic or logical comparisons reproduced:** 9 of 9.
- **False PDF pagination found:** 0.
- **Candidates based only on a display-zero P value:** 0.
- **Post-registration duplicate candidates found:** 0; related relationships are explicitly distinguished above.
- **Human adjudication placeholders:** Every subfield in this artifact uses the exact blank placeholder `__`.
- **Outstanding coordinator completion tasks:** Mark evidence quality complete; generate the complete C001-C009 report and update its manifest row; add all later agents to the execution manifest and token ledger; complete end-of-run integrity, rendering, and validation.
