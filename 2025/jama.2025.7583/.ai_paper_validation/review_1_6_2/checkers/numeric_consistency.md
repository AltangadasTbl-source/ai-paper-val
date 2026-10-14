# Numeric Consistency Review

Reviewer runtime ID: 01a12bc4-5fd4-75e2-83e5-902a2215ae7a. Scope: all 119 supplied physical PDF pages, complete fresh maps and every applicable numerical relationship family N001–N112 in `../relationships/numeric_relationship_inventory.md`. Main9, protocol63, administrative23, results supplement15, SAP9 pages. Complete quantitative review: participant screening/randomization/intervention receipt/follow-up/evaluability/imputation, every baseline numerator/denominator/percentage and subgroup total, every outcome/safety row, every forest population/subgroup, every center and recurrence-criterion cell, all complication rows including zeros, historical comparative primary-result cells, and plan count definitions/targets. Scientific gaps: none.

The source-linked complete maps and source/asset inventories were read as locators, without old findings, candidate conclusions or reports. QUALITY_CONTROL_SCOPE.md and the complete workflow1.6.2 review contract govern screening. Numeric half-unit interval arithmetic, followed by the remaining gap divided by the absolute printed value, was applied; relative discrepancy≤.05 is screened out. A model-based estimate is not required to equal a crude estimate. Counts with distinct stated population definitions remain distinct.

Exact source confirmation: pinned package-local PyMuPDF1.26.4 via bundled `pdf_tools.py text` and `render` on main p.5, derivatives `../preprocessing/numeric-checker-main-p5.txt` (sorted layout) and `../preprocessing/numeric-checker-main-p5.png` (CPU,200dpi). Both source native text and visual current-source rendering match the printed finding inputs. No OCR or external evidence used. No sources/reused assets modified.

## Findings

### F-NUM-001

**Title:** Midline-shift sample counts exceed the unilateral-only populations stated in the same display.

**Relationships:** N037 (Table1 unilateral CSDH) and N041 (midline-shift sample); both source locations below are REPORT, within the same article/display. Proposed relationship type: S_W; all relationships: S_W.

**Exact source locations and document roles:** [REPORT main article physical PDF p.5, printed p.131, Table1 initial imaging results](../../../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=5): Unilateral CSDH row; Midline shift, median (IQR), mm row; right continuation footnote d. Both comparison sides are REPORT, based on the retrospective baseline trial-results content.

**Printed inputs:** Unilateral CSDH: embolization127 (74.3%), standard care130 (76.0%). Midline shift: embolization10 (7–13) [n=161]; standard care10.5 (7–14) [n=161]. The midline-shift label carries superscript d, whose footnote reads “Data provided for unilateral CSDH only.” Treatment-group headers n=171 each. These count/sample inputs and the superscript/footnote linkage are visible in the current supplied source.

**Rule and calculation:** A patient-level sample restricted to unilateral CSDH cannot have more patients than the unilateral population in its treatment arm. Applying the mandatory half-unit intervals gives embolization unilateral count [126.5,127.5], standard-care unilateral count [129.5,130.5], and each printed midline-shift sample [160.5,161.5]. Even allowing every unilateral participant to contribute, feasible sample upper limits are127.5 and130.5. The minimum gaps are160.5−127.5=33 and160.5−130.5=30 patients. Relative discrepancies against the printed sample161 are33/161=0.2049689 and30/161=0.1863354, both greater than0.05. The unrounded direct count excesses are34 and31. This is one repeated pattern affecting both arms.

**Focus area:** A, counts and denominators.

**Proposed review domain:** statistical_results.

**Qualifying route:** Route A, category 3.

**Affected result or extracted value:** The embolization and standard-care sample sizes underlying baseline midline-shift medians10mm and10.5mm, and the population those medians describe.

**Why context does not resolve it:** RouteA category3 applies to reproduced counts within one display. The same table permits n161 under the full-arm size171 but expressly restricts the midline-shift row to unilateral CSDH, with only127/130 such patients. The immediate context does not establish whether the sample counts or the population restriction supplies the intended extraction population. This concerns the printed sample sizes and their numerical population constraint, rather than a wording-only difference.

**Alternatives and missing definition:** The n161 samples might include bilateral as well as unilateral participants, with the footnote population restriction differing from the analyzed population; alternatively the counts may refer to a different set or unit. Neither alternative is stated. The table labels patient characteristics and presents no repeated-scan or hemisphere-level sample definition. The underlying individual measurements are not supplied.

**Exact human question:** Do the midline-shift medians include all participants with available measurements or only participants with unilateral CSDH, and what are the participant sample sizes in each arm for those medians?

## Excluded observations

Only apparent issues examined and not emitted are listed here; reconciled checks are recorded in the N inventory.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main p.5 Table1 treatment, burr-hole/trephine rows | Standard-care surgery counts146+18=164 against printed denominator163. Half-unit numerator-sum interval[163,165] overlaps denominator[162.5,163.5]; gap0. Printed percentages89.6+11.0=100.6% have at most0.5-point interval gap against100%, relative.005. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p.1 abstract and p.4 Figure1 | Completed308 differs from observed primary-endpoint evaluable162+157=319. Figure1 distinguishes discontinued follow-up from endpoint evaluability and allows recurrence before death;342−15−19=308. | CONTEXT_RESOLVES |
| REPORT main p.6 Figure2/Table2 and results supplement p.9 eFigure2; p.14 STEM eTable4 | Adjusted/imputed ORs or risk differences need not equal crude quantities from displayed observed counts. The supplied primary and sensitivity model labels establish adjustment/imputation; STEM summary does not state crude/unadjusted estimation. No effect-measure-label conflict is reproduced. | MODEL_VERSUS_CRUDE |
| REPORT main p.4 Figure1 and results supplement p.9 eFigure2 nonembolized-exclusion sensitivity | Treated145 differs from sensitivity observed denominator138. The sensitivity is labeled multiple imputation; observed fractions exclude unavailable outcomes.171−26=145 treated and145−138=7 without observed outcomes is compatible with the nine experimental unavailable outcomes. | CONTEXT_RESOLVES |
| REPORT results supplement p.14 eTable4 MAGIC-MT | Percentages6.7 and9.9 give central difference−3.2 versus printed−3.3. Half-unit input difference interval[−3.3,−3.1] overlaps printed difference[−3.35,−3.25]; gap0. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN protocol pp.9–10,50 and SAP pp.4–5 sample size; REPORT main p.3 target |142 per group with20% loss implies355 overall under division by retention, compared with342 printed. Half-unit inputs yield total[351.553,358.491], printed[341.5,342.5], minimum gap9.053 and relative9.053/342=.02647≤.05. This numerical target-inflation observation does not qualify after precision; statistical power/design reproduction remains assigned to the statistical reviewer. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN protocol p.48 and SAP p.5 interim; REPORT main p.3 |129/342=37.7193% compared with37.5% information fraction. Input ratio interval[37.5182,37.9209]% overlaps printed[37.45,37.55]%;gap0. | ROUNDING_OR_DISPLAY_PRECISION |

## Coverage and limitations

Reviewed112 stable numeric families; one consolidated finding; seven excluded observations. Every mapped applicable count family is complete. Review required no additional shard because112≤120. Every source page has complete mapping; no numerical display row was sampled or omitted. The plan-only blank forms, device administrative details and bibliography contain no observed event/patient-count relationship; numerical population/design definitions relevant to the report are retained in the inventory.

Limitations: raw participant measurements, imputed results and unprinted historical arm denominators are absent. These limit reconstructing models and event totals but do not limit the within-display sample constraint finding. Some reusable extraction engine versions are undocumented; the emitted finding is checked against exact current-source text and rendering. No Office/workbook/CSV sources were supplied. Findings have no candidate IDs, severity, adjudication or disposition.

