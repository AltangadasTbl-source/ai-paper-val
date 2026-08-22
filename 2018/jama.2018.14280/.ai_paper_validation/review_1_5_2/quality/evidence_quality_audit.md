# Final Evidence-Quality Audit

## Audit scope and boundaries

This audit covers all five supplied direct sources; all 21 rows in `coverage_manifest.md`; every row in `source_coverage.md`; canonical relationships N001-N047 and S001-S038; numeric, cross-source, statistical-pass-1, and statistical-pass-2 checker outputs; the stable candidate ledger; the mechanical evidence recheck; and the current agent-execution manifest. Only supplied PDFs and fresh Workflow 1.5.2 artifacts were used. No web source, external literature, legacy audit derivative, old candidate set, or old extraction was used as evidence or as a discovery boundary.

Discovery records explicitly cover all 47 numeric/reporting relationships and all 38 inferential-statistical relationships. No target count, top-N rule, review queue, sampling rule, candidate cap, or early stopping boundary controlled discovery. No stable candidate is based solely on a very small P value displayed as zero. The `<.001`, `---`, `NA`, and `P=1.00` displays were handled as non-candidate display or test-availability conventions where applicable.

All findings below remain **Pending Human Adjudication**. This artifact does not rank, suppress, renumber, merge, or assign a scientific disposition to any stable candidate.

## Coverage and integrity audit

| Audit unit | Result | Evidence-quality finding |
|---|---:|---|
| Direct sources | 5/5 | DOC-001 through DOC-005 are inventoried with filename, type, size, SHA-256, page count, role, and fresh availability. |
| Direct-source units | 94/94 | Every source row has reusable units 0, fresh-required units equal to total units, mapped units equal to total units, and `COMPLETE`. Totals are 94/0/94/94. |
| Source hashes | 5/5 unchanged | Freshly recomputed SHA-256 values exactly match `source_hashes_before.sha256`. |
| Numeric relationships | 47/47 | N001-N047 are present once in the canonical inventory and explicitly covered by the numeric checker. |
| Statistical relationships | 38/38 per pass | S001-S038 are present once in the canonical inventory and explicitly marked `PASS_1_COMPLETE` and `PASS_2_COMPLETE`. |
| Statistical agents | 2 distinct fresh agents | Pass 1 is `/root/statistics_pass_1`, Terra/high/FRESH_SPAWN; pass 2 is `/root/statistics_pass_2`, Terra/high/FRESH_SPAWN. The IDs are distinct. |
| Stable candidates | 23/23 | Ledger and evidence-recheck sets are identical: C001-C023. This audit also contains C001-C023 exactly once. |
| Current agent manifest | 10/10 current executions represented | The coordinator and all currently completed specialist roles, including this quality auditor, appear once with one primary artifact path. A report-generator row must be added if a separate report agent is spawned. |
| Coverage-manifest stages | 12/12 required stages present | All required stage names are present. Every row has one undecorated relative artifact path. Nineteen rows are complete; evidence-quality and report-generation rows were pending when this audit began. |

Main mapping covers DOC-001 pages 1-9. Support mapping covers DOC-002 pages 1-49, DOC-003 pages 1-22, DOC-004 pages 1-13, and DOC-005 page 1, including documented no-applicable scope. Dense tables and figures are assigned through their canonical N and S records; source-unit coverage is not limited to candidate-producing pages.

## Correctable defect register

Five supportable defects require coordinator repair. None changes, deletes, or combines a stable candidate.

**Coordinator repair note:** All five listed defects were repaired after audit: both coverage scopes now enumerate C001-C023; the quality row is complete; XF003 uses the correct 475/482 tobacco totals; XF004 links SAP pages 3 and 5; and the C023 recheck wording now reflects the corrected ledger. The report row remains pending only until report assembly.

1. **Coverage row `quality-001`:** replace its generic exact scope with the explicit enumeration `C001 C002 C003 C004 C005 C006 C007 C008 C009 C010 C011 C012 C013 C014 C015 C016 C017 C018 C019 C020 C021 C022 C023`, and change its status to `COMPLETE` after this artifact is saved.
2. **Coverage row `report-001`:** replace its generic exact scope with the same explicit C001-C023 enumeration. Keep it pending until the complete report is assembled, then change it to `COMPLETE`.
3. **Cross-source checker XF003, affecting C004 provenance:** correct `Tobacco categories total 475 in each arm` to `475 in the low arm and 482 in the intermediate arm`; replace the diagnostic `111/475=23.4%` with `111/482=23.0%`. The current candidate ledger and evidence recheck already contain the correct 475/482 arithmetic.
4. **Cross-source checker XF004, affecting C023 provenance:** replace the second SAP locator `PDF p. 6` with `PDF p. 5`, and provide separate page-qualified links for SAP PDF pages 3 and 5. The direct PDF and fresh extraction place the two August 22 occurrences on PDF pages 3 and 5.
5. **Evidence recheck C023:** remove the stale statement that the current ledger gives SAP PDF page 6. The current ledger already correctly gives SAP PDF pages 3 and 5. Retain the direct source confirmation at pages 3 and 5.

The future final-report cards must use the exact required human template, with every subfield blank: `Validity: __`, `Importance: __`, `Action: __`, `Initials: __`, and `Notes: __`. No final report existed at this audit cutoff, so report-level placeholder identity and ledger/recheck/report ID equality must be confirmed after report generation.

## C001 — Reversed endpoint in the eTable 2 PEEP interquartile range

- **Source grounding:** DOC-004 directly prints intermediate-arm PEEP `8 (5–1)` and defines continuous cells as median (interquartile range).
- **Exact location:** `joi180108supp3_prod.pdf`, PDF p. 6, eTable 2, Other Mode of Ventilation, after titration on randomization day, intermediate arm, PEEP.
- **Rule/calculation:** For `median (lower–upper)`, lower <= median <= upper; `5 <= 8` but `8 <= 1` is false.
- **Observation/inference separation:** The reversed, non-containing endpoint is printed. A transcription or truncation mechanism and any replacement endpoint are inferred and remain unknown.
- **Alternative interpretation:** One endpoint may be mistyped; no supplied source establishes the intended value.
- **Human question:** What are the intended lower and upper quartiles?
- **Duplicate handling/provenance:** NF001, SF013, and XF002 concern the same cell and ordering rule and were correctly combined before stable IDs.
- **Report-card readiness:** Source evidence, rule, calculation, alternative, and human question are sufficient; do not propose an endpoint correction.

## C002 — At-risk-for-ARDS percentages use undisclosed denominators

- **Source grounding:** DOC-001 prints `292 (61.6)` and `290 (60.3)` beneath arm headers 477 and 484.
- **Exact location:** `jama_simonis_2018_oi_180108.pdf`, PDF p. 5, Table 1, Patients at risk for ARDS.
- **Rule/calculation:** `292/477=61.2%` and `290/484=59.9%`; 474 and 481 reproduce 61.6% and 60.3% to one decimal.
- **Observation/inference separation:** Header-total calculations fail. Available-case denominators and three missing observations per arm are diagnostic inferences.
- **Alternative interpretation:** Variable-specific denominators may have been used without disclosure.
- **Human question:** What denominators and missing counts generated this row?
- **Duplicate handling/provenance:** NF002 is the candidate source; XF003 is contextual block-level overlap. This row is distinct from C003-C006 because its printed values and denominator identity are distinct.
- **Report-card readiness:** Complete and source-grounded.

## C003 — Septic-shock percentages use undisclosed denominators

- **Source grounding:** DOC-001 prints `82 (17.6)` and `74 (15.5)` beneath arm headers 477 and 484.
- **Exact location:** `jama_simonis_2018_oi_180108.pdf`, PDF p. 5, Table 1, Septic shock.
- **Rule/calculation:** `82/477=17.2%` and `74/484=15.3%`; examples 466 and 477 reproduce the printed percentages, but rounded percentages do not uniquely identify denominators.
- **Observation/inference separation:** Non-reproduction from headers is direct. Available-case populations are inferred.
- **Alternative interpretation:** Smaller variable-specific denominators may apply.
- **Human question:** What exact denominators and missingness rule generated 17.6% and 15.5%?
- **Duplicate handling/provenance:** NF003 with XF003 context; distinct from other Table 1 rows by printed values and comparator.
- **Report-card readiness:** Complete if the report preserves the non-uniqueness of inferred denominators.

## C004 — Tobacco-use categories use undisclosed denominators

- **Source grounding:** The four DOC-001 tobacco categories sum to 475 low and 482 intermediate while headers are 477 and 484; percentages reproduce 475/482.
- **Exact location:** `jama_simonis_2018_oi_180108.pdf`, PDF p. 5, Table 1, Patient tobacco use.
- **Rule/calculation:** `106+97+75+197=475`; `111+97+80+194=482`; for example `106/475=22.3%` and `111/482=23.0%`.
- **Observation/inference separation:** Category sums and percentage bases are printed/calculated. Missing records outside the printed `Unknown` category are inferred.
- **Alternative interpretation:** Available-case denominators may intentionally exclude two additional records per arm.
- **Human question:** Were 475 and 482 intended, and how were the two unrepresented patients per arm classified?
- **Duplicate handling/provenance:** NF004 and XF003 concern this same tobacco block; retained separately from C005-C006 because the category set and denominator relationship differ.
- **Report-card readiness:** Ready after the XF003 arithmetic wording is repaired as specified above.

## C005 — Alcohol-use categories use undisclosed denominators

- **Source grounding:** DOC-001 alcohol categories total 475 and 482, below headers 477 and 484, and percentages reproduce the smaller totals.
- **Exact location:** `jama_simonis_2018_oi_180108.pdf`, PDF p. 5, Table 1, Patient alcohol use.
- **Rule/calculation:** `121+47+26+59+222=475`; `92+61+30+56+243=482`; `121/475=25.5%`, `92/482=19.1%`.
- **Observation/inference separation:** The sums and percentage bases are direct; the missing-data mechanism is inferred.
- **Alternative interpretation:** Variable-specific available-case denominators may have been intended.
- **Human question:** Should 475/482 and two missing observations per arm be disclosed?
- **Duplicate handling/provenance:** NF005/XF003; distinct printed category block and values.
- **Report-card readiness:** Complete and source-grounded.

## C006 — ICU-admission categories use undisclosed denominators

- **Source grounding:** DOC-001 prints surgical/medical `82/393` and `79/403` beneath arm headers 477/484.
- **Exact location:** `jama_simonis_2018_oi_180108.pdf`, PDF p. 5, Table 1, Reason for ICU admission.
- **Rule/calculation:** `82+393=475`, `79+403=482`; percentages reproduce 475/482, including `82/475=17.3%` and `79/482=16.4%`.
- **Observation/inference separation:** Short category totals and smaller percentage bases are direct; unclassified or missing status is inferred.
- **Alternative interpretation:** Surgical/medical status may be available for 475 and 482 patients only.
- **Human question:** What denominators and missing categories apply?
- **Duplicate handling/provenance:** NF010/XF003; separate from C004-C005 because it uses a distinct binary categorization.
- **Report-card readiness:** Complete and source-grounded.

## C007 — Sedative-infusion percentages omit effective denominators

- **Source grounding:** DOC-004 prints `320 (70.6)` and `333 (72.1)` under headers 477/484, while its note defines number/total (%).
- **Exact location:** `joi180108supp3_prod.pdf`, PDF p. 8, eTable 4, Sedative infusion.
- **Rule/calculation:** Header calculations are 67.1% and 68.8%; `320/453=70.6%` and `333/462=72.1%`.
- **Observation/inference separation:** Header mismatch and recovering denominators are reproducible; a complete-case mechanism is inferred.
- **Alternative interpretation:** An unstated complete-case subset may apply.
- **Human question:** Were 453 and 462 used, and what records were excluded or missing?
- **Duplicate handling/provenance:** NF006, SF014, and XF005 are genuine duplicates for this row; distinct from C008-C010 by row values.
- **Report-card readiness:** Complete and source-grounded.

## C008 — Analgesic-infusion percentages omit effective denominators

- **Source grounding:** DOC-004 prints `277 (61.1)` and `273 (59.1)` under headers 477/484.
- **Exact location:** `joi180108supp3_prod.pdf`, PDF p. 8, eTable 4, Analgesic infusion.
- **Rule/calculation:** Header calculations are 58.1% and 56.4%; `277/453=61.1%` and `273/462=59.1%`.
- **Observation/inference separation:** The mismatch is direct; the population and missingness mechanism are inferred.
- **Alternative interpretation:** A 453/462 complete-case subset may apply.
- **Human question:** What exact row totals and missing-data rule generated the percentages?
- **Duplicate handling/provenance:** NF007/SF015/XF005 were combined for this row; distinct from adjacent co-intervention rows.
- **Report-card readiness:** Complete and source-grounded.

## C009 — Neuromuscular-blockade percentages omit effective denominators

- **Source grounding:** DOC-004 prints `53 (11.7)` and `60 (13.0)` under headers 477/484.
- **Exact location:** `joi180108supp3_prod.pdf`, PDF p. 8, eTable 4, Neuromuscular blockade.
- **Rule/calculation:** Header calculations are 11.1% and 12.4%; `53/453=11.7%` and `60/462=13.0%`.
- **Observation/inference separation:** The mismatch is printed/reproducible; a shared complete-case population is inferred.
- **Alternative interpretation:** Row-specific available-case denominators may apply.
- **Human question:** What denominators and exclusions or missing observations underlie the row?
- **Duplicate handling/provenance:** NF008/SF016/XF005 were combined; distinct row and values from C007-C008/C010.
- **Report-card readiness:** Complete and source-grounded.

## C010 — Vasopressor-use percentages omit effective denominators

- **Source grounding:** DOC-004 prints `363 (80.0)` and `353 (76.4)` under headers 477/484.
- **Exact location:** `joi180108supp3_prod.pdf`, PDF p. 8, eTable 4, Use of vasopressors.
- **Rule/calculation:** Header calculations are 76.1% and 72.9%; `363/454=80.0%` and `353/462=76.4%`.
- **Observation/inference separation:** The mismatch and recovering denominators are reproducible; whether nearby complete-case populations are shared is inferred.
- **Alternative interpretation:** The low-arm denominator may equal an explicitly printed nearby denominator, but the source does not define population identity.
- **Human question:** Were 454 and 462 used, and why do they differ from the arm totals and nearby intermediate denominator 464?
- **Duplicate handling/provenance:** NF009/SF017/XF005 were combined; distinct co-intervention row and effective denominator pair.
- **Report-card readiness:** Complete and source-grounded.

## C011 — Mortality effect-measure wording conflicts with Table 2 and the SAP

- **Source grounding:** DOC-001 Methods describes ICU/hospital length of stay and mortality rates using Kaplan-Meier/Cox HRs; DOC-001 Table 2 and DOC-003 SAP label ICU/hospital mortality RRs, reserving HRs for 28-/90-day mortality.
- **Exact location:** DOC-001 PDF p. 4, Statistical Analysis; DOC-001 PDF p. 6, Table 2 and footnotes; DOC-003 `joi180108supp2_prod.pdf`, PDF p. 13.
- **Rule/calculation:** Same outcomes should have consistent model/effect-measure labels. The semantic mapping is Methods HR/Cox versus Table/SAP RR for ICU/hospital mortality.
- **Observation/inference separation:** The differing printed descriptions are direct. An overbroad Methods sentence is a possible explanation, not an established correction.
- **Alternative interpretation:** The Methods sentence may have intended only time-indexed mortality, with another sentence covering ICU/hospital binary outcomes.
- **Human question:** Which model and effect measure were used, and what scope was intended by the Methods sentence?
- **Duplicate handling/provenance:** SF001 is distinct from C012-C013: C011 checks labels/model wording, whereas C012-C013 compare each printed RR with displayed risks.
- **Report-card readiness:** Complete and source-grounded; keep label consistency separate from numeric RR reproduction.

## C012 — ICU-mortality RR does not reproduce from printed risks

- **Source grounding:** DOC-001 prints low `132/450`, intermediate `115/458`, and RR 1.11.
- **Exact location:** `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, ICU mortality and footnote c.
- **Rule/calculation:** Crude low/intermediate risk ratio `(132/450)/(115/458)=1.168231884`, rounding to 1.17 rather than 1.11.
- **Observation/inference separation:** Printed margins and diagnostic ratio are direct/reproducible. A weighted, stratified, model-based, or different-population estimator is inferred and not supplied.
- **Alternative interpretation:** The reported RR may use a non-crude estimator or population.
- **Human question:** What estimator, direction, population, weights, or strata generated 1.11?
- **Duplicate handling/provenance:** SF002 only; distinct from C011's label rule and all other outcome rows.
- **Report-card readiness:** Complete if the crude ratio is explicitly described as a diagnostic from printed margins, not a substitute analysis.

## C013 — Hospital-mortality RR does not reproduce from printed risks

- **Source grounding:** DOC-001 prints `151/477`, `140/484`, and RR 1.06.
- **Exact location:** `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, hospital mortality and footnote c.
- **Rule/calculation:** `(151/477)/(140/484)=1.094399521`, rounding to 1.09 rather than 1.06.
- **Observation/inference separation:** The displayed-margin diagnostic is direct; any alternate estimator or population is inferred.
- **Alternative interpretation:** An implementation not recoverable from the displayed margins may underlie 1.06.
- **Human question:** What exact analysis generated RR 1.06?
- **Duplicate handling/provenance:** SF003; distinct outcome/result from C012 and distinct rule from C011.
- **Report-card readiness:** Complete with diagnostic-boundary wording.

## C014 — ARDS RR does not reproduce from printed risks

- **Source grounding:** DOC-001 prints `17/448`, `23/462`, and RR 0.86.
- **Exact location:** `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, Development of ARDS and footnote c.
- **Rule/calculation:** `(17/448)/(23/462)=0.762228261`, rounding to 0.76 rather than 0.86.
- **Observation/inference separation:** The printed-risk ratio mismatch is direct; alternate estimator/population explanations are inferred.
- **Alternative interpretation:** A model-derived or differently defined analysis population may apply.
- **Human question:** What estimator and denominator population produced 0.86?
- **Duplicate handling/provenance:** SF004; separate outcome and printed values.
- **Report-card readiness:** Complete with diagnostic-boundary wording.

## C015 — Pneumonia RR does not reproduce from printed risks

- **Source grounding:** DOC-001 prints `19/450`, `17/462`, and RR 1.07.
- **Exact location:** `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, Development of pneumonia and footnote c.
- **Rule/calculation:** `(19/450)/(17/462)=1.147450980`, rounding to 1.15 rather than 1.07.
- **Observation/inference separation:** The displayed-margin mismatch is direct; an alternate estimator/population is inferred.
- **Alternative interpretation:** Information beyond the displayed margins may have been used.
- **Human question:** What computation and population generated RR 1.07?
- **Duplicate handling/provenance:** SF005; separate printed row and result.
- **Report-card readiness:** Complete with diagnostic-boundary wording.

## C016 — Pneumothorax RR does not reproduce from printed risks

- **Source grounding:** DOC-001 prints `8/448`, `6/462`, and RR 1.16.
- **Exact location:** `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, Pneumothorax and footnote c.
- **Rule/calculation:** `(8/448)/(6/462)=1.375`, rounding to 1.38 rather than 1.16.
- **Observation/inference separation:** The printed-margin mismatch is direct; any model or alternate analysis set is inferred.
- **Alternative interpretation:** A procedure using information beyond the displayed margins may apply.
- **Human question:** What computation and analysis set generated RR 1.16?
- **Duplicate handling/provenance:** SF006; separate row/result.
- **Report-card readiness:** Complete with diagnostic-boundary wording.

## C017 — Atelectasis RR does not reproduce from printed risks

- **Source grounding:** DOC-001 prints `51/449`, `52/464`, and RR 1.00.
- **Exact location:** `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, Atelectasis and footnote c.
- **Rule/calculation:** `(51/449)/(52/464)=1.013534350`, rounding to 1.01 rather than 1.00.
- **Observation/inference separation:** The small printed-margin discrepancy is direct. Separate estimation or greater unprinted precision is inferred.
- **Alternative interpretation:** A separately estimated effect or undocumented reporting convention could print as 1.00.
- **Human question:** What estimator and rounding rule produced RR 1.00?
- **Duplicate handling/provenance:** SF007; retained as its own printed row despite a smaller difference than neighboring RR candidates.
- **Report-card readiness:** Complete, but the report must preserve the small magnitude and open estimator explanation without impact overstatement.

## C018 — Extrapulmonary-infection RR does not reproduce from printed risks

- **Source grounding:** DOC-001 prints `20/448`, `28/463`, and RR 0.84.
- **Exact location:** `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, Extrapulmonary infection and footnote c.
- **Rule/calculation:** `(20/448)/(28/463)=0.738201531`, rounding to 0.74 rather than 0.84.
- **Observation/inference separation:** The margin-derived discrepancy is direct; estimator/population explanations are inferred.
- **Alternative interpretation:** An unspecified procedure beyond the displayed margins may apply.
- **Human question:** What procedure and population produced RR 0.84?
- **Duplicate handling/provenance:** SF008; separate row/result.
- **Report-card readiness:** Complete with diagnostic-boundary wording.

## C019 — Extrapulmonary-sepsis RR does not reproduce from printed risks

- **Source grounding:** DOC-001 prints `12/448`, `16/463`, and RR 0.87.
- **Exact location:** `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, Extrapulmonary sepsis and footnote c.
- **Rule/calculation:** `(12/448)/(16/463)=0.775111607`, rounding to 0.78 rather than 0.87.
- **Observation/inference separation:** The displayed-margin mismatch is direct; a non-crude estimator/population is inferred.
- **Alternative interpretation:** A broader inferential implementation may apply, but is not identified.
- **Human question:** What estimator and analysis set generated RR 0.87?
- **Duplicate handling/provenance:** SF009; separate outcome/result.
- **Report-card readiness:** Complete with diagnostic-boundary wording.

## C020 — Delirium RR does not reproduce from printed risks

- **Source grounding:** DOC-001 prints `149/343`, `132/361`, and RR 1.15.
- **Exact location:** `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, Delirium and footnote c.
- **Rule/calculation:** `(149/343)/(132/361)=1.188024560`, rounding to 1.19 rather than 1.15.
- **Observation/inference separation:** The printed-margin mismatch is direct; alternate model/population explanations are inferred.
- **Alternative interpretation:** A non-crude analysis or different population may underlie the RR.
- **Human question:** What computation and analysis population produced RR 1.15?
- **Duplicate handling/provenance:** SF010; separate row and analysis denominators.
- **Report-card readiness:** Complete with diagnostic-boundary wording.

## C021 — Tracheostomy RR does not reproduce from printed risks

- **Source grounding:** DOC-001 prints `54/477`, `52/484`, and RR 1.03.
- **Exact location:** `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, Need for tracheostomy and footnote c.
- **Rule/calculation:** `(54/477)/(52/484)=1.053701016`, rounding to 1.05 rather than 1.03.
- **Observation/inference separation:** The displayed-margin mismatch is direct; an alternative estimator/population is inferred.
- **Alternative interpretation:** A procedure not reducible to displayed margins may apply.
- **Human question:** What exact analysis generated RR 1.03?
- **Duplicate handling/provenance:** SF011; separate outcome/result.
- **Report-card readiness:** Complete with diagnostic-boundary wording.

## C022 — The same subgroup intervals are labelled IQR and 95% CI

- **Source grounding:** DOC-001 labels two subgroup bounds `IQR`; DOC-004 eTable 5 prints identical point estimates/bounds under `Mean Difference (95% CI)`.
- **Exact location:** DOC-001 `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Subgroups and Exploratory Analyses; DOC-004 `joi180108supp3_prod.pdf`, PDF p. 9, eTable 5.
- **Rule/calculation:** The point estimates and all four endpoints match exactly; the interval labels differ for the same outcome, subgroups, and contrast.
- **Observation/inference separation:** Label disagreement is direct. A main-narrative transcription error is inferred.
- **Alternative interpretation:** The eTable heading might not describe these rows, although its single explicit interval heading supports the 95% CI reading.
- **Human question:** Are these 95% CIs, and which source wording should be clarified?
- **Duplicate handling/provenance:** SF012 and XF001 are genuine duplicates; C022 is distinct from subgroup arithmetic checks because its rule is cross-source measure-label identity.
- **Report-card readiness:** Complete and source-grounded.

## C023 — Enrollment completion dates differ by two days

- **Source grounding:** DOC-001 reports enrollment through August 20, 2017; DOC-003 states enrollment was complete August 22, 2017.
- **Exact location:** DOC-001 `jama_simonis_2018_oi_180108.pdf`, PDF pp. 1 and 5; DOC-003 `joi180108supp2_prod.pdf`, PDF pp. 3 and 5.
- **Rule/calculation:** The two descriptions concern completion of enrollment for the same trial; August 22 is two calendar days after August 20.
- **Observation/inference separation:** The printed dates and two-day difference are direct. Last randomization versus administrative completion is an inferred explanation.
- **Alternative interpretation:** The dates may denote distinct operational events not defined in the supplied package.
- **Human question:** What operational event does each date represent, and what was the last enrollment/randomization date?
- **Duplicate handling/provenance:** XF004 only; both occurrences within each source are retained as provenance for one cross-document date relationship.
- **Report-card readiness:** Source evidence is sufficient after the XF004 locator and stale recheck wording are repaired. Use SAP PDF pages 3 and 5, never page 6.

## Report-generation controls

The complete report must contain C001-C023 once each, with the exact card labels in `report_spec.md`. Each card must retain direct observation separately from diagnostic inference, identify source-grounded alternatives, and ask the unresolved human question. Any downstream-impact sentence must be conditional and bounded to what a data extractor, systematic review, meta-analysis, or guideline could copy if the candidate is confirmed; no propagation or paper-level conclusion change is established by the supplied package.

Every source-PDF evidence link must end in its exact `#page=N`. In particular, C023 uses DOC-003 pages 3 and 5. No candidate mentions a literal-zero P display as part of its basis, so no `Independent contradiction beyond P=0 display` field is required for C001-C023.

After the five repairs and report assembly, recheck exact ID-set equality across `candidate_ledger.md`, `verification/evidence_recheck.md`, this audit, and the final Markdown report; then confirm that every human adjudication subfield is exactly `__`.

## Audit completion

- Stable IDs covered: C001-C023 (23/23).
- Source rows covered: DOC-001-DOC-005 (5/5; 94/94 units).
- Canonical relationships covered: N001-N047 (47/47) and S001-S038 (38/38 in both passes).
- Coverage-manifest rows covered: 21/21.
- Current agent-manifest rows covered: 10/10.
- Correctable defects identified: 5.
- Limitation: the final report and its report-generation execution record were not yet present, so report ID equality, exact human placeholders, final evidence links, token metadata, and report-generation manifest completion require post-assembly confirmation.
- Canonical audit artifact: `quality/evidence_quality_audit.md`.
