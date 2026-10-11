# Cross-source consistency check

## Scope and method

- **Assigned relationship scope:** global numeric/reporting relationships N001-N068 and global statistical/inferential relationships S001-S036 (104 relationships in total).
- **Inputs used:** the new Workflow 1.5.1 numeric and statistical inventories, new main/support evidence maps and page extracts, and the supplied main article and supplied Results Supplement, Protocol, and SAP PDFs. Reused text and maps were used to locate records; the printed PDF pages were checked for each observation below.
- **Matching rule:** results were compared only after matching population, time horizon, intervention contrast, analysis framework, effect/summary measure, scale/unit, reference direction, and displayed precision. Protocol/SAP planning statements and PRO-SCAN/external-feasibility records were retained in their own context and were not compared as achieved TARGET Protein results.
- **Local keys:** `XC01` onward are checker-local observations only. They are not candidate IDs and express no adjudication.

## Relationship coverage

| Relationship family | IDs checked | Cross-source conclusion |
|---|---|---|
| Main trial design, definitions, flow, treatment composition, primary/secondary results, baseline, biochemical, exposure, discharge, readmission, and subgroup descriptive material | N001-N028 | Matched occurrences were checked. The ventilation-summary label, Bayesian-secondary-summary label, and day-10 urea summary label are recorded below. Other matched values agree after their stated population/time/model differences and rounding are retained. |
| Results-Supplement methods, eTables, eFigures, and ICEMAN material | N029-N052 | Checked against their applicable main-paper occurrence or internal repeated occurrence. The Period 2 Usual alive-at-day-90 rendering is recorded below. No separate conflict was retained for the RRT interaction annotation after direct visual checking showed the eFigure 7 annotation is `p<0.001`, consistent with the ICEMAN form. |
| Protocol handling/definitions, external feasibility, and PRO-SCAN records | N053-N067 | Checked as planning, external, or distinct-substudy material. No matched achieved-result conflict: different populations, periods, or estimands explain nonidentical figures. |
| SAP planned enrolment | N068 | Checked as a prospective planned total, not a final analysed-total statement; no matched-result conflict. |
| Main final effects and models | S001-S015 | Checked across abstract, narrative, Table 2, Figure 3, and supplied Results Supplement. Exact repetitions agree; `.02`/`.023`, `.11`/`.106`, and `.47`/`.468` are compatible displayed-precision pairs. The two Table 2 summary-label observations are recorded below. |
| Results-Supplement final methods | S016-S021 | Checked against the final main reporting. The supplement explicitly distinguishes the final Tobit ventilation analysis and the Bayesian quantile/credible-interval analysis; no unsupported planned-versus-final conflict was retained. |
| Protocol, PRO-SCAN, and SAP statistical plans/external feasibility | S022-S036 | Checked in their prospective/external contexts. Differences from final methods are not treated as conflicts when the supplied supplement states the final method or when the source concerns another study/substudy. |

## Checker-local observations requiring human verification

### XC01 — Table 2 ventilation descriptive-summary label does not match its printed form

- **Matched result and locations:** full intention-to-treat groups; duration of invasive ventilation in hours. Main article [abstract, p1](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1) reports a *mean difference* of 6.8 hours (95% CI, −3.0 to 16.5). Main article [Table 2, p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7) labels the group row `Duration of invasive ventilation, mean (SD), h` and prints augmented `84.0 (35.0 to 178.9)` and usual `78.0 (33.2 to 161.0)`. Results Supplement [eTable 10, p18](../../../joi250040supp3_prod_1753124024.38098.pdf#page=18) uses a central value plus two bounds for the period-specific ventilation summaries (for example, Period 2 Usual `72.0 (32.0, 148.0)`).
- **Direct observation:** an SD is one dispersion value, whereas each Table 2 parenthesis prints two endpoints joined by `to`; the format is not a `mean (SD)` presentation. The treatment-effect label `Mean difference, 6.8 (−3.0 to 16.5)` is a distinct model-based effect and does not make a two-endpoint group parenthesis an SD.
- **Comparison rule:** for the same outcome, population, and hour scale, the descriptive-summary label must identify the form actually printed. The observation concerns the descriptive summary label, not whether the supplied mean-difference model is appropriate.
- **Inference and alternatives:** the label likely should identify a median plus an interval (such as IQR), or another two-bound summary. A layout/production error in the label, an omitted label qualifier, or an unreported alternative summary convention could explain it; the supplied material does not establish which correction is intended.
- **Human question:** What descriptive statistic and dispersion/range are `84.0 (35.0 to 178.9)` and `78.0 (33.2 to 161.0)` intended to represent, and should the Table 2 label be revised accordingly?

### XC02 — Table 2 Bayesian quantile secondary-analysis row is labelled `mean (SD)` despite a median-based result

- **Matched result and locations:** primary outcome, full intention-to-treat population, augmented-minus-usual contrast. Main article [Table 2, p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7) labels the Bayesian row `No. of days free of the index hospital and alive at day 90 (bayesian quantile mixed model), mean (SD)` and prints `62.0 (0 to 77)` versus `64.0 (0 to 77)`, with `Median difference, −1.50 (−3.86 to 0.90)`. Results Supplement [secondary analyses, p5](../../../joi250040supp3_prod_1753124024.38098.pdf#page=5) states that the Bayesian quantile mixed-effects model presents the treatment coefficient as a `difference in medians` and a 95% credible interval; [eFigure 6, p27](../../../joi250040supp3_prod_1753124024.38098.pdf#page=27) repeats the median difference −1.50 with 95% CrI −3.86 to 0.90.
- **Direct observation:** the Table 2 group-summary label says `mean (SD)`, while its own effect label and the matched supplement method/result identify a quantile median difference; the group parentheses also contain two endpoints rather than a single SD.
- **Comparison rule:** a matched outcome, population, contrast, and Bayesian quantile analysis should not be described as a mean/SD group summary when the associated reported estimand is explicitly a difference in medians, unless the source expressly states that descriptive means/SDs are intentionally shown. No such statement was located in the supplied pages.
- **Inference and alternatives:** this is a measure/label inconsistency. It may be a copied label from the preceding linear-model row, or Table 2 may deliberately pair a median estimand with separately computed means/SDs; the printed two-endpoint format and supplied supplement favor the first explanation, but only the authors/production record can resolve it.
- **Human question:** Were the Bayesian-row group values intended as median (IQR) values, and should `mean (SD)` be replaced with the correct descriptive label?

### XC03 — Discussion calls the day-10 urea summaries means while the reported values are medians

- **Matched result and locations:** group-specific blood urea at study day 10, mmol/L. Main article [Biochemical Outcomes, p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5) says the *median (IQR)* day-10 concentrations were augmented `13.0 (8.2-18.8)` and usual `10.6 (7.1-15.4)` mmol/L. Main article [Discussion, p8](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=8) states, `mean urea concentrations at day 10 were higher in the augmented protein group`.
- **Direct observation:** the same time point, groups, analyte, and unit are described as median (IQR) in Results and as mean in Discussion. No day-10 mean values are printed in the matched Results text.
- **Comparison rule:** a cross-location summary-statistic label must preserve the reported measure when referring to the same matched group comparison. The direction (higher in augmented protein) agrees; the issue is mean-versus-median labeling, not direction or a recalculated value.
- **Inference and alternatives:** `mean` may be ordinary nontechnical prose, a copy-editing substitution, or a reference to unprinted means. The supplied article gives no unprinted mean result that would establish the latter.
- **Human question:** Does the Discussion sentence refer to the reported median day-10 urea comparison and, if so, should `mean` be changed to `median` (or should a distinct mean analysis be identified)?

### XC04 — eTable 10 prints a comma instead of a decimal point in one matched percentage

- **Matched result and locations:** Results Supplement [eTable 10, p18](../../../joi250040supp3_prod_1753124024.38098.pdf#page=18), `Alive at day 90 [n (%)]`, Period 2 Usual Protein (`n = 530`), prints `383 (72, 3%)`. The same cell’s count and column denominator give 383/530 × 100 = 72.264...%, which displays as 72.3% to one decimal. Adjacent cells in the same matched row use decimal points, including `323 (67.3%)`, `258 (77.0%)`, and `229 (76.8%)`.
- **Direct observation:** the printed comma makes this one percentage read `72, 3%`, unlike the table’s own decimal convention. The count and denominator support the numeric content `72.3%` but do not change the character printed in the source.
- **Comparison rule:** within a single row with one-decimal percentages, the percentage separator should be rendered consistently; the denominator check supports the apparent intended decimal rendering.
- **Inference and alternatives:** this may be a localized punctuation/production error, or a locale-specific decimal separator inadvertently introduced in one cell. The supplied source cannot establish the intended production correction beyond the count/denominator calculation.
- **Human question:** Should the Period 2 Usual Protein cell be rendered `383 (72.3%)`?

## Directly resolved seed check

The maps retained an RRT/renal-failure interaction inequality question. Direct visual review of Results Supplement [eFigure 7, p28](../../../joi250040supp3_prod_1753124024.38098.pdf#page=28) shows the RRT interaction annotation as `p<0.001`, and the matched ICEMAN renal-failure form on [p31](../../../joi250040supp3_prod_1753124024.38098.pdf#page=31) says `P<0.001`. The same outcome, subgroup, interaction framework, and displayed threshold match. Accordingly, no cross-source observation is registered for that map-seed transcription discrepancy.

## Counts and limitations

- **Relationships checked:** 104/104 assigned global relationships (N001-N068 and S001-S036).
- **Checker-local observations recorded:** 4 (`XC01-XC04`).
- **Not retained as differences:** planned-versus-final method/sample-size statements, distinct PRO-SCAN/external-feasibility records, and compatible precision pairs were not treated as matched-result conflicts. No coherent display-zero P value was encountered or used as an observation.
- **Limitations:** the supplied package has no participant-level data or fitted-model outputs, so model-based quantities were not recomputed. Graphical values were compared only when a printed figure/table label supplied an exact value; the underlying direct PDF remains the authority for human verification.
