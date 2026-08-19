# Evidence-Quality Audit

## Audit scope and coverage status

The final evidence-quality audit covered the complete source inventory, evidence-asset inventory, both quantitative extractions, `N001` through `N068`, `S001` through `S021`, all numeric and cross-source checker output, both statistical passes, the stable candidate ledger, the mechanical evidence recheck, every row of `source_coverage.md` and `coverage_manifest.md`, and `agent_execution_manifest.md`.

- All three direct-source rows close: 46 total units equal 46 reusable units plus 0 fresh-required units, and 46 units are mapped. The zero fresh-required count follows complete usable source-linked reusable maps; direct PDFs remained authoritative for candidate recheck.
- Every coverage-manifest row contains one plain relative artifact path. All completed upstream stages have complete status. Candidate registration and recheck each explicitly enumerate C001, C002, C003, C004, C005, C006, and C007. Evidence quality has the same assigned set; report generation remains the next stage.
- Discovery was rebuilt from complete source-linked mappings and relationship inventories. No old candidate list, review queue, desired count, top-N rule, or early stopping boundary controlled discovery. The evidence-quality audit itself found the omitted N029 relationship and caused C007 to be appended without changing C001 through C006.
- Statistical pass 1 and pass 2 are complete for every S ID from S001 through S021. Their fresh, distinct agent IDs are `/root/statistical_pass_1` and `/root/statistical_pass_2`; both are recorded as `gpt-5.6-terra`, high reasoning effort, and `FRESH_SPAWN`.
- Source hashes remain unchanged for 3 of 3 direct sources, and reusable-artifact hashes remain unchanged for 74 of 74 inventoried assets. Every local PDF link in the candidate ledger and evidence recheck resolves, and every candidate link ends in a truthful `#page=N` fragment.
- No stable candidate mentions `P = 0`, `p = 0.000`, or an equivalent display zero. No independent-contradiction field is therefore required. No candidate is based on finite precision, underflow, or mathematical nonzero-tail reasoning.
- The seven primary categories use exact labels from `QUALITY_CONTROL_SCOPE.md`. Observations, calculations, alternatives, missing definitions, and human questions are separated. No stable ID is ranked, suppressed, merged after registration, assigned severity, or given a scientific disposition. Every ID remains **Pending Human Adjudication**.

## Repairs completed through the coordinator

The audit identified and the coordinator repaired three supportable defects. N029 and the numeric checker had incorrectly said that all Table 1 diagnosis percentages reconciled; the direct page instead shows that the Hyperlipidemia percentages reproduce only with the opposite arm denominators. This relationship was registered as C007 and received a complete exact-source recheck. The main extraction and numeric checker were corrected to record that DOC-001 PDF p. 7 does restate the HbA1c coefficient in `mg/dL`. The C005 alternative was also corrected because ordinary two-decimal truncation, like ordinary rounding, cannot bridge the printed estimate/standard-error ratio to the displayed t statistic.

The ledger and recheck now contain identical stable-ID sets. C002 and C003 are possible production-related neighbors but not duplicate relationships: they are separately labeled outcome rows that can be extracted independently. The other repeated checker proposals concern the same printed relationship and were merged before stable IDs with their provenance retained.

The final report cards have not yet been generated. For every card, the report generator must include every exact field required by `report_spec.md`, bound downstream impact to the specific value, unit, denominator, label, or endpoint a later evidence product could copy, and avoid any claim that the paper-level conclusion is wrong. Every human-adjudication block must use these exact blank subfields:

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C001 — HbA1c daily-rate unit conflicts with the table scale

- **Evidence and calculation audit:** DOC-001 PDF pp. 1 and 7 both print `-0.0002 mg/dL` with the same interval; Table 4 on PDF p. 8 labels HbA1c as `%`. The categorical unit comparison is reproducible, and all three page links are truthful.
- **Assumption and missing definition:** The comparison assumes that the named HbA1c response scale applies to the treatment-by-time coefficient unless a transform is stated. The modeled scale, unit per day, and any transformation are absent and remain the exact human question.
- **Duplicate, impact, and wording audit:** Numeric, statistical, and cross-source records describe the same unit conflict and were properly merged. The ledger makes no paper-conclusion claim. Any report-card downstream statement must be limited to copying the wrong outcome unit or scale.
- **Card readiness:** Ledger and recheck together supply the source evidence, comparator, rule, calculation, alternative, and human question. The final report must add the prescribed relevance, bounded downstream-impact, verification-step, and blank adjudication fields.
- **Status:** Pending Human Adjudication.

## C002 — Total-cholesterol percentage-point difference does not reconcile with printed counts

- **Evidence and calculation audit:** DOC-001 Table 5 on PDF p. 9 prints `9/64 (14.1%)`, `6/62 (9.7%)`, and `4.3`. The exact difference is 4.385080... percentage points and displays as 4.4; the printed percentages also subtract to 4.4. The page link and arithmetic are reproducible.
- **Assumption and missing definition:** Applicability of the header denominators is supported by the row percentages, but a measure-specific evaluable denominator, weighting rule, or missing-data convention is not supplied. Those inputs remain the human question.
- **Duplicate, impact, and wording audit:** C002 is not duplicative of C003 because Total cholesterol is a distinct labeled outcome row. No conclusion impact is claimed. Any downstream statement must be limited to extraction of this row's percentage-point effect.
- **Card readiness:** The current evidence supports a neutral candidate card; the final report must retain the alternative calculation convention and exact blank adjudication fields.
- **Status:** Pending Human Adjudication.

## C003 — LDL percentage-point difference does not reconcile with printed counts

- **Evidence and calculation audit:** DOC-001 Table 5 on PDF p. 9 independently prints the LDL vector `9/64 (14.1%)`, `6/62 (9.7%)`, and `4.3`. The exact and displayed-percentage calculations both display as 4.4, not 4.3.
- **Assumption and missing definition:** A separate LDL-specific denominator or estimator is not stated. The possibility that the neighboring rows share an unprinted calculation mechanism is an inferred explanation, not an observation.
- **Duplicate, impact, and wording audit:** The repeated numeric vector may share a production mechanism with C002, but the distinct LDL label makes it a separate extractable relationship under the merge rule. No conclusion impact is asserted; downstream scope is limited to this LDL row.
- **Card readiness:** The source, rule, arithmetic, alternative, and human question are complete for report generation, subject to the required exact blank adjudication fields.
- **Status:** Pending Human Adjudication.

## C004 — Incident-cancer model label does not follow the printed DIC and I-squared rule

- **Evidence and calculation audit:** DOC-003 PDF p. 4 prints the within-3-DIC and strict `I2 >25%` rule; PDF p. 5 prints fixed DIC 27.06, random DIC 27.93, displayed I-squared 25, and `random`. The DIC difference is 0.87 and the displayed comparison `25 > 25` is false.
- **Assumption and missing definition:** The diagnostic applies the printed rule to displayed inputs. An unrounded I-squared above 25%, an inclusive internal threshold, or another internal rule could explain the label. The unrounded value and exact selection convention are absent.
- **Duplicate, impact, and wording audit:** N062 and S015 address the same row and rule and were properly merged. The candidate does not establish which model is scientifically preferable or that a conclusion changes. Downstream impact must be limited to extraction of the selected-model label and associated result.
- **Card readiness:** The conditional nature of the displayed-precision comparison and the missing unrounded value must remain explicit in the final card, with blank adjudication fields.
- **Status:** Pending Human Adjudication.

## C005 — Egger estimate and standard error do not reproduce the printed t statistic at displayed precision

- **Evidence and calculation audit:** DOC-003 PDF p. 21 prints estimate -0.47, standard error 0.77, t=-0.59, and P=.57. The point ratio is -0.610389.... Under ordinary nearest-hundredth rounding, the attainable absolute-ratio interval is 0.600 through below 0.620915, disjoint from the 0.585 through below 0.595 interval that displays as 0.59. Ordinary two-decimal truncation also cannot bridge the values.
- **Assumption and missing definition:** The consistency rule is conditional on the adjacent estimate and standard error being the numerator and denominator for the printed t statistic. The exact Egger test definition, parameter mapping, unrounded inputs, degrees of freedom, and sidedness are absent. No P-value reconstruction is supported or made.
- **Duplicate, impact, and wording audit:** This relationship is distinct. Statistical pass 2 correctly records and resolves the pass-1 diagnostic disagreement without an adjudicative conclusion. Any downstream statement must be limited to copying this estimate/SE/t vector.
- **Card readiness:** The final card must preserve the conditional rule and the possible distinct parameter, variance estimate, or output field; it must not state the mismatch as unconditional or infer a mechanism. Exact blank adjudication fields remain required.
- **Status:** Pending Human Adjudication.

## C006 — ASCEND is excluded for all stroke but included in the total-stroke forest plot

- **Evidence and calculation audit:** DOC-003 PDF p. 9 marks ASCEND all stroke not included because only ischaemic stroke is reported; p. 16 prints 12 studies and totals 73,883/72,317; p. 24 prints 13 total-stroke rows and totals 81,623/80,057, including the same ASCEND `240/7740` versus `263/7740` vector shown in the ischaemic-stroke panel. Both arm-total differences equal 7,740 exactly. DOC-002 p. 7 is truthful contextual evidence; the direct all-stroke comparator is DOC-003 p. 9.
- **Assumption and missing definition:** The endpoint-membership comparison keeps the Bayesian HR and frequentist RR analyses distinct. A model-specific convention allowing an ischaemic-only proxy in the frequentist total-stroke panel is possible but unstated. The endpoint rule and extraction record are absent.
- **Duplicate, impact, and wording audit:** N068, S019, S021, and the checker proposals describe one endpoint-membership/count relationship and were properly merged. No paper-level effect or conclusion change is asserted. Downstream scope must be limited to the study count, denominators, endpoint membership, and result that could be extracted.
- **Card readiness:** The final card must retain the distinct-model caveat and exact human question, plus the required blank adjudication fields.
- **Status:** Pending Human Adjudication.

## C007 — Hyperlipidemia percentages reproduce only with the opposite arm denominators

- **Evidence and calculation audit:** DOC-001 Table 1 on PDF p. 5 prints olanzapine `n=64`, `18 (29.0)` and placebo `n=62`, `19 (29.7)`. Own-arm calculations display as 28.1% and 30.6%; opposite-arm calculations display exactly as 29.0% and 29.7%. The source page, arithmetic, and exact-source recheck are complete.
- **Assumption and missing definition:** The rule uses the printed arm headers because the row supplies no other denominator. Unstated evaluable denominators, missing status, or transposition are alternatives, not observed mechanisms. The table-production record is absent.
- **Duplicate, impact, and wording audit:** C007 is a distinct Table 1 baseline-comorbidity relationship and duplicates no existing stable ID. It was appended without renumbering or suppressing any earlier candidate. No conclusion impact is asserted; downstream scope is limited to copying the two hyperlipidemia percentages or counts.
- **Card readiness:** The final card must include the own-arm and opposite-arm calculations, preserve the human denominator question, and use exact blank adjudication fields.
- **Status:** Pending Human Adjudication.

## Audit conclusion

After the documented coordinator repairs, every stable ID from C001 through C007 has a complete ledger entry and mechanical recheck with truthful pagination, matched printed facts, a reproducible or explicitly conditional rule, separated observation and inference, a source-grounded alternative, and an exact human question. The candidate set is suitable for neutral report assembly, not for automated scientific disposition. Remaining limitations are recorded in `limitations.md`.
