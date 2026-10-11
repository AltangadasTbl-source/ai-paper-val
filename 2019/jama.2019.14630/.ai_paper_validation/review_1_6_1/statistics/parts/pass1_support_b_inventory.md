# Statistical relationship inventory — pass 1 support-B part

Status: PASS_1_COMPLETE. Runtime agent: root/statistics_one_b. Fixed model/effort: gpt-6.1-sol/high; start mode FRESH_SPAWN. This part is owned solely by this fresh statistical pass-1 shard. Pass 2 must use a different newly spawned runtime agent.

## Exact scope and provenance

DOC-004, REPORT: eTable 6 PDF p.16; eTable 7 pp.17–20 (p.20 footnotes included); eTable 8 pp.21–22; eTable 9 pp.23–24; eFigure 3 p.27. There are 10 assigned PDF pages, 61 table variable/population families, 100 between-group time/population contrasts, 300 modeled estimates with 95% CIs (two arm changes and one between-group difference per contrast), 122 baseline arm summaries, 12 figure families with all 48 arm/time distributions, and 4 associated statistical-method/scale records. Stable scope: S401–S477, 77 records. Both time rows and all arms are retained in each applicable family; MI and completer eTable 9 blocks have distinct IDs.

Read QUALITY_CONTROL_SCOPE.md and the entire Workflow 1.6.1 review contract; settings, AGENTS, current routing/tooling, source/evidence inventories, and assigned current mapper views were also read. No old candidate, checker, screening, disposition, classification or final report supplied discovery scope. Sources and reusable assets are preserved.

Evidence locators: current checker_views/results_tables_6_9.md, support_semantic_index.md, results_figures_administrative.md; current main_quantitative_evidence.md used only for matching context. Native layout is the curator's source-matched Poppler pdftotext 26.01.0 extraction of DOC-004. Retained direct-source page images p.16 and p.23 were inspected for the potentially notable score changes and population/test comparison; retained figure_render-27.png was inspected in full. Retained image-engine version is not recorded. No new derivative, OCR, Python, GPU, web access, or source modification was used.

Source links in this part are relative to statistics/parts. Canonical merge into statistics/relationship_inventory.md must shorten their prefix by one directory.

## Shared source-grounded checks and named missing inputs

Each table-family record below includes its complete baseline summaries, both applicable time rows, all three change estimates/intervals, P values, exact source page, population, unit and model context. All displayed change estimates lie within their displayed CIs, and every displayed lower endpoint is no greater than its upper endpoint. Signs of the modeled I-minus-C differences agree with the displayed arm-change directions, allowing each printed quantity its half-unit display interval. Every row received review; none were sampled.

General REPORT methods on DOC-001 p.4 state two-sided tests, P<.05, exploratory secondary analyses with no additional type I error adjustment, mixed-effects linear changes and site/participant/family random intercepts. The assigned table footnotes explicitly state site and couple random factors and 95% CIs. They do not name the statistic used for each P value, its degrees of freedom, exact contrast covariance, variance estimator, or CI construction. eTable 9 does not supply imputation-specific degrees of freedom, pooling formula, or exact variable-by-arm missing counts. These missing definitions preclude exact CI-to-P reconstruction; they are recorded without assumptions. No supplied statistic or standard error occurs in this assigned scope. No numeric normal-theory reconstruction is treated as the reported test.

The tables identify modeled estimates, not crude differences. Differences from subtraction of rounded arm means do not establish a contradiction of the stated models. Baseline-replacement sensitivities, multiple-imputation analyses and completer analyses have different source-established matching keys. No equality of these result families is assumed. Baseline descriptive cross-location comparisons are peripheral; eTable 9 risk-factor contributor counts need not equal nutritional-FFQ counts. No superiority/noninferiority/equivalence margin, interim boundary or stopping conclusion is printed in these assigned tables/figure; the main source calls this interim dietary report preliminary and secondary analyses exploratory. No such decision was inferred.

For every record, PASS_1_COMPLETE denotes completion of checks, including named-input limitations, rather than an adjudication. A future pass-2 reviewer must reconcile the record with the complete ledger/screening/recheck facts and add PASS_2_COMPLETE.

## Complete table-family records

### S401 — eTable 6: 17-item er-MedDiet (0–17)

- **Exact location and document role:** REPORT DOC-004 eTable 6, [PDF p.16](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=16>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 17-item er-MedDiet (0 to
 17)
   Baseline, mean (SD)                 8.5 (2.6)               8.6 (2.7)
   6-month change                  3.8 (3.7 to 3.9)         1.7 (1.6 to 1.8)          2.1 (2 to 2.3)     <0.001
   12-month change                 3.9 (3.8 to 4.0)         1.9 (1.8 to 2.0)         2.0 (1.9 to 2.2)    <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S402 — eTable 6: MDS (0–9)

- **Exact location and document role:** REPORT DOC-004 eTable 6, [PDF p.16](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=16>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 MDS (Trichopolou 0 to 9)
   Baseline, mean (SD)                 4.3 (1.7)               4.3 (1.6)
   6-month change                  0.1 (0.1 to 0.2)       -0.3 (-0.4 to -0.2)        0.4 (0.3 to 0.5)    <0.001
   12-month change                 0.1 (0.1 to 0.2)       -0.3 (-0.4 to -0.3)        0.4 (0.4 to 0.5)    <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S403 — eTable 6: MEDAS (0–14)

- **Exact location and document role:** REPORT DOC-004 eTable 6, [PDF p.16](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=16>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 MEDAS (0 to 14)
   Baseline, mean (SD)                 7.6 (1.9)               7.6 (1.9)
   6-month change                  2.3 (2.2 to 2.3)         1.3 (1.2 to 1.3)         1.0 (0.9 to 1.1)    <0.001
   12-month change                 2.4 (2.3 to 2.5)         1.5 (1.4 to 1.6)         0.9 (0.8 to 1.0)    <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S404 — eTable 6: PDQS (0–42)

- **Exact location and document role:** REPORT DOC-004 eTable 6, [PDF p.16](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=16>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 PDQS (0 to 42)
   Baseline, mean (SD)                21.0 (3.7)               21.0 (3.7)
   6-month change                  4.0 (3.9 to 4.2)         2.0 (1.8 to 2.1)         2.1 (1.9 to 2.3)    <0.001
   12-month change                 4.0 (3.9 to 4.2)         2.1 (2.0 to 2.3)         1.9 (1.7 to 2.1)    <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S405 — eTable 7: Olive oil (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.17](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=17>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Olive oil (g/week)
   Baseline, median (IQR)          350 (175, 350)            350 (175, 350)
   6-month change                   23 (18 to 27)             26 (22 to 30)               -3 (-9 to 3)      0.27
   12-month change                  30 (26 to 34)             38 (34 to 42)              -7 (-13 to -2)     0.01
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S406 — eTable 7: Refined olive oil (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.17](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=17>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Refined olive oil
 (g/week)
   Baseline, median (IQR)             0 (0, 70)                  0 (0, 70)
   6-month change                 -32 (-35 to -29)           -31 (-34 to -28)             -1 (-5 to 4)      0.72
   12-month change                -33 (-36 to -29)           -35 (-38 to -32)             3 (-2 to 7)       0.26
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S407 — eTable 7: EVOO (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.17](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=17>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 EVOO (g/week)
   Baseline, median (IQR)           175 (70, 350)             175 (70, 350)
   6-month change                   54 (49 to 59)             56 (51 to 61)               -3 (-9 to 4)      0.47
   12-month change                  63 (58 to 68)             73 (68 to 78)             -10 (-17 to -3)     0.004
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S408 — eTable 7: Nuts (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.17](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=17>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Nuts (g/week)
   Baseline, median (IQR)           60 (28, 165)               60 (14, 165)
   6-month change                 105 (100 to 110)            61 (56 to 67)              43 (36 to 51)     <0.001
   12-month change                100 (95 to 106)             73 (68 to 78)              28 (20 to 35)     <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S409 — eTable 7: Fruits (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.17](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=17>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Fruits (g/week)
   Baseline, median (IQR)       2,287 (1,523, 3,200)      2,287 (1,494,
                                                          3,281)
   6-month change                 306 (256 to 356)          144 (94 to 193)             162 (92 to 233)    <0.001
   12-month change                369 (319 to 419)          215 (166 to 265)            154 (83 to 224)    <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S410 — eTable 7: Vegetables (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.17](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=17>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Vegetables (g/week)
   Baseline, median (IQR)       2,168 (1,621, 2,814)      2,130 (1,596,
                                                          2,863)
   6-month change                 287 (254 to 321)          116 (83 to 149)         171 (124 to 218)       <0.001
   12-month change                295 (261 to 328)           126 (93 to 159)        169 (121 to 216)       <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S411 — eTable 7: Cereals (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.17](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=17>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Cereals (g/week)
   Baseline, median (IQR)         877 (627, 1,432)          870 (645, 1,432)
   6-month change               -152 (-170 to -133)          -70 (-89 to -51)       -82 (-108 to -55)      <0.001
   12-month change              -183 (-202 to -165)         -87 (-106 to -68)       -96 (-123 to -70)      <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S412 — eTable 7: Whole grains (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.18](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=18>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Whole grains (g/week)
  Baseline, median                109 (0, 525)              98 (0, 525)
  (IQR)
  6-month change               238 (221 to 255)            54 (37 to 70)          184 (160 to 208)         <0.001
   12-month change             197 (180 to 214)            56 (39 to 73)          141 (117 to 165)         <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S413 — eTable 7: Refined grains (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.18](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=18>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Refined grains (g/week)
  Baseline, median             779 (425, 1,475)          779 (412, 1,474)
  (IQR)
  6-month change              -475 (-496 to -454)      -172 (-193 to -152)      -303 (-332 to -273)        <0.001
   12-month change            -467 (-488 to -446)      -203 (-224 to -182)      -264 (-294 to -235)        <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S414 — eTable 7: Legumes (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.18](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=18>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Legumes (g/week)
  Baseline, median               120 (88, 180)            120 (88, 176)
  (IQR)
  6-month change                 33 (30 to 36)             14 (11 to 17)               19 (15 to 23)       <0.001
   12-month change               35 (32 to 38)             17 (14 to 20)               17 (13 to 22)       <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S415 — eTable 7: Fish (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.18](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=18>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Fish (g/week)
  Baseline, median              673 (472, 918)            682 (475, 918)
  (IQR)
  6-month change                 90 (79 to 101)            35 (23 to 46)               55 (40 to 71)       <0.001
   12-month change               90 (79 to 102)            27 (16 to 38)               63 (47 to 79)       <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S416 — eTable 7: Meat (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.18](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=18>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Meat (g/week)
  Baseline, median             993 (760, 1,263)          994 (776, 1,271)
  (IQR)
  6-month change               -95 (-107 to -83)         -70 (-82 to -58)          -25 (-42 to -8)          0.01
   12-month change             -104 (-116 to -92)        -95 (-107 to -83)             -9 (-26 to 8)        0.31
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S417 — eTable 7: Red meat (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.18](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=18>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Red meat (g/week)
  Baseline, median              290 (150, 497)            300 (150, 520)
  (IQR)
  6-month change               -99 (-106 to -92)         -59 (-66 to -51)         -40 (-51 to -30)         <0.001
   12-month change             -104 (-112 to -97)        -71 (-79 to -64)         -33 (-43 to -22)         <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S418 — eTable 7: Processed meat (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.18](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=18>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Processed meat
 (g/week)
   Baseline, median             227 (143, 317)            227 (143, 322)
   (IQR)
   6-month change               -55 (-60 to -50)         -38 (-43 to -33)         -17 (-24 to -10)         <0.001
   12-month change              -55 (-60 to -50)         -47 (-52 to -42)              -9 (-16 to -1)       0.02
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S419 — eTable 7: Pastries (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.18](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=18>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Pastries (g/week)
  Baseline, median               121 (42, 275)            114 (42, 261)
  (IQR)
  6-month change               -94 (-100 to -88)         -42 (-48 to -36)         -52 (-61 to -43)         <0.001
   12-month change              -93 (-99 to -87)         -54 (-60 to -47)         -39 (-48 to -30)         <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S420 — eTable 7: Dairy (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.19](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=19>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Dairy (g/week)
   Baseline, median            2,100 (1,532,          2,200 (1,548, 3,597)
   (IQR)                           2,959)
   6-month change              19 (-24 to 63)          -125 (-168 to -82)         144 (83 to 205)          <0.001
   12-month change             -29 (-72 to 14)        -166 (-209 to -123)         137 (76 to 198)          <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S421 — eTable 7: Total yogurt (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.19](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=19>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Total yogurt (g/week)
   Baseline, median            375 (58, 875)              375 (58, 875)
   (IQR)
   6-month change             103 (84 to 122)             7 (-11 to 26)               95 (69 to 122)       <0.001
   12-month change              77 (58 to 96)             -4 (-22 to 15)              81 (54 to 107)       <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S422 — eTable 7: Fermented dairy (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.19](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=19>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Fermented dairy
 (g/week)
   Baseline, median            550 (300, 975)           575 (300, 1,025)
   (IQR)
   6-month change              83 (64 to 103)             -6 (-25 to 14)              89 (61 to 117)       <0.001
   12-month change              63 (43 to 82)             -14 (-33 to 6)              76 (49 to 104)       <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S423 — eTable 7: Low-fat dairy (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.19](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=19>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Low-fat dairy (g/week)
   Baseline, median            658 (0, 1,775)            687 (0, 1,775)
   (IQR)
   6-month change             283 (243 to 324)            56 (15 to 96)          228 (170 to 285)          <0.001
   12-month change            230 (189 to 271)            -4 (-45 to 36)         234 (177 to 292)          <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S424 — eTable 7: Whole-fat dairy (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.19](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=19>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Whole-fat dairy
 (g/week)
   Baseline, median              0 (0, 375)                 0 (0, 375)
   (IQR)
   6-month change           -147 (-167 to -126)         -98 (-118 to -77)         -49 (-78 to -20)         0.001
   12-month change          -130 (-151 to -110)         -87 (-107 to -67)         -44 (-72 to -15)         0.003
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S425 — eTable 7: Total alcohol intake (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.19](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=19>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Total alcohol intake
 (g/week)
   Baseline, median              32 (5, 98)                36 (5, 103)
   (IQR)
   6-month change              -12 (-14 to -9)             -5 (-8 to -3)              -6 (-10 to -3)       0.001
   12-month change             -11 (-13 to -8)             -4 (-6 to -1)              -7 (-10 to -3)       <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S426 — eTable 7: Red wine (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 7, [PDF p.19](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=19>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Red wine (g/week)
   Baseline, median               0 (0, 29)                 0 (0, 29)
   (IQR)
   6-month change                1 (-1 to 2)                2 (0 to 3)                 -1 (-3 to 1)         0.36
   12-month change                1 (0 to 3)                2 (1 to 4)                 -1 (-3 to 1)         0.36
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S427 — eTable 8: Total energy (kcal/day)

- **Exact location and document role:** REPORT DOC-004 eTable 8, [PDF p.21](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=21>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Total energy Intake (kcal/d)
   Baseline, mean (SD)                2,355 (544)             2,369 (555)
   6-month change                 -151 (-168 to -135)       -67 (-83 to -50)     -85 (-108 to -61)       <0.001
   12-month change                -154 (-170 to -137)       -66 (-83 to -49)     -88 (-111 to -64)       <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S428 — eTable 8: Total protein (%E)

- **Exact location and document role:** REPORT DOC-004 eTable 8, [PDF p.21](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=21>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Total protein (%E)
   Baseline, mean (SD)                 16.8 (2.8)              16.8 (2.8)
   6-month change                   1.0 (1.0 to 1.1)         0.1 (0 to 0.2)           0.9 (0.8 to 1)     <0.001
   12-month change                  0.9 (0.8 to 1.0)         0 (-0.1 to 0.1)         0.9 (0.8 to 1.1)    <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S429 — eTable 8: Total carbohydrate (%E)

- **Exact location and document role:** REPORT DOC-004 eTable 8, [PDF p.21](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=21>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Total carbohydrate (%E)
   Baseline, mean (SD)                 40.7 (6.8)              40.4 (6.9)
   6-month change                  -2.9 (-3.1 to -2.7)       -1.6 (-1.8 to -         -1.3 (-1.6 to -1)   <0.001
                                                                  1.4)
   12-month change                 -3.2 (-3.4 to -3.0)       -2.0 (-2.2 to -     -1.2 (-1.5 to -0.9)     <0.001
                                                                  1.8)
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S430 — eTable 8: Total fat (%E)

- **Exact location and document role:** REPORT DOC-004 eTable 8, [PDF p.21](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=21>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Total fat (%E)
   Baseline, mean (SD)                 39.5 (6.6)              39.7 (6.5)
   6-month change                   2.1 (1.9 to 2.4)        1.6 (1.4 to 1.8)         0.6 (0.3 to 0.9)    <0.001
   12-month change                  2.5 (2.3 to 2.7)        2.1 (1.8 to 2.3)         0.4 (0.1 to 0.8)     .006
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S431 — eTable 8: SFA (%E)

- **Exact location and document role:** REPORT DOC-004 eTable 8, [PDF p.21](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=21>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 SFA (%E)
   Baseline, mean (SD)                  9.9 (2.0)                10 (2)
   6-month change                  -0.9 (-0.9 to -0.8)       -0.5 (-0.6 to -     -0.4 (-0.5 to -0.3)     <0.001
                                                                  0.4)
   12-month change                 -0.8 (-0.9 to -0.7)       -0.5 (-0.6 to -     -0.3 (-0.4 to -0.2)     <0.001
                                                                  0.5)
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S432 — eTable 8: MUFA (%E)

- **Exact location and document role:** REPORT DOC-004 eTable 8, [PDF p.21](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=21>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 MUFA (%E)
   Baseline, mean (SD)                 20.5 (4.7)              20.6 (4.6)
   6-month change                   3.0 (2.9 to 3.2)        2.0 (1.9 to 2.2)         1.0 (0.8 to 1.2)    <0.001
   12-month change                  3.4 (3.2 to 3.5)        2.6 (2.5 to 2.8)         0.7 (0.5 to 1.0)    <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S433 — eTable 8: MUFA:SFA ratio

- **Exact location and document role:** REPORT DOC-004 eTable 8, [PDF p.22](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=22>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Ratio MUFA:SFA
   Baseline, mean (SD)                       2.1 (0.5)              2.1 (0.5)
   6-month change                        0.6 (0.5 to 0.6)       0.3 (0.3 to 0.4)        0.2 (0.2 to 0.3)   <0.001
   12-month change                       0.6 (0.6 to 0.6)       0.4 (0.4 to 0.4)        0.2 (0.1 to 0.2)   <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S434 — eTable 8: PUFA (%E)

- **Exact location and document role:** REPORT DOC-004 eTable 8, [PDF p.22](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=22>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 PUFA (%E)
   Baseline, mean (SD)                       6.4 (1.9)              6.4 (1.8)
   6-month change                        1.1 (1.1 to 1.2)       0.7 (0.6 to 0.7)        0.5 (0.4 to 0.5)   <0.001
   12-month change                       1.1 (1.0 to 1.2)       0.7 (0.7 to 0.8)        0.4 (0.3 to 0.5)   <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S435 — eTable 8: Total alcohol (%E)

- **Exact location and document role:** REPORT DOC-004 eTable 8, [PDF p.22](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=22>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Total alcohol (%E)
   Baseline, median (IQR)                     1 (0, 4)               2 (0, 4)
   6-month change                       -0.3 (-0.4 to -0.2)      -0.1 (-0.2 to 0)       -0.2 (-0.3 to 0)    0.02
   12-month change                      -0.2 (-0.3 to -0.1)      0 (-0.1 to 0.1)        -0.2 (-0.3 to -     0.01
                                                                                             0.1)
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S436 — eTable 8: Fiber (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 8, [PDF p.22](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=22>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Fiber (g/week)
   Baseline, mean (SD)                       184 (63)               182 (60)
   6-month change                         35 (33 to 37)           14 (12 to 16)          21 (18 to 24)     <0.001
   12-month change                        32 (30 to 34)           16 (14 to 18)          16 (13 to 19)     <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S437 — eTable 8: Long-chain omega-3 fatty acids (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 8, [PDF p.22](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=22>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Long chain w-3 fatty acids
 (g/week)
   Baseline, median (IQR)                     5 (4, 9)               5 (4, 9)
   6-month change                        0.9 (0.8 to 1.1)       0.4 (0.3 to 0.5)        0.6 (0.4 to 0.7)   <0.001
   12-month change                       0.9 (0.8 to 1.1)       0.4 (0.3 to 0.5)        0.6 (0.4 to 0.7)   <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S438 — eTable 8: Cholesterol (mg/week)

- **Exact location and document role:** REPORT DOC-004 eTable 8, [PDF p.22](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=22>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Cholesterol (mg/week)
   Baseline, mean (SD)                     2,651 (793)            2,687 (825)
   6-month change                        -191 (-216 to -         -147 (-172 to -        -44 (-79 to -8)     0.02
                                              166)                    122)
   12-month change                       -187 (-213 to -         -182 (-207 to -        -6 (-41 to 30)      0.75
                                              162)                    157)
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S439 — eTable 8: Sodium (g/week)

- **Exact location and document role:** REPORT DOC-004 eTable 8, [PDF p.22](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=22>).
- **Population / denominators:** Baseline-replacement sensitivity; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 6 and 12 months (separate rows); within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Site and intracluster/couple random factors; means and 95% CIs from mixed-effect models. All missing follow-up values replaced with baseline values.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
 Sodium (g/week)
   Baseline, median (IQR)               22.2 (17.9, 27.1)      22.2 (17.9, 27.4)
   6-month change                       -2.7 (-2.9 to -2.5)    -1.6 (-1.8 to -1.4)      -1.1 (-1.4 to -    <0.001
                                                                                             0.8)
   12-month change                      -2.8 (-3.0 to -2.6)    -1.7 (-1.9 to -1.4)      -1.1 (-1.4 to -    <0.001
                                                                                             0.8)
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Main-paper same-variable results are MI, not this baseline-replacement result; their numerical equality is not expected. Main sensitivity context identifies eTables 6–8 as post hoc baseline replacement.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S440 — eTable 9: Weight (kg) — MI

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.23](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=23>).
- **Population / denominators:** Multiple-imputation block ONLY; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Chained-equation imputation and all printed predictors/fractions retained in S476.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
Weight (kg) — MI
Baseline mean (SD): I 86.5 (12.9), C 86.3 (13.0)
12-month modeled change (95% CI): I -3.6 (-3.9 to -3.4), C -0.8 (-1.0 to -0.5)
Between-group difference (95% CI): -2.9 (-3.2 to -2.6); P <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Matched main risk-factor narrative is MI at 12 months when supplied (waist −3.3 [−3.6,−2.9], SBP −1.9 [−2.7,−1.1], both P<.001); these match their corresponding rows. Figures show distributions/proportions rather than the same modeled contrast.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S441 — eTable 9: Waist (cm) — MI

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.23](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=23>).
- **Population / denominators:** Multiple-imputation block ONLY; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Chained-equation imputation and all printed predictors/fractions retained in S476.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
Waist (cm) — MI
Baseline mean (SD): I 108 (9.6), C 108 (9.7)
12-month modeled change (95% CI): I -4.4 (-4.6 to -4.1), C -1.1 (-1.3 to -0.9)
Between-group difference (95% CI): -3.3 (-3.6 to -2.9); P <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Matched main risk-factor narrative is MI at 12 months when supplied (waist −3.3 [−3.6,−2.9], SBP −1.9 [−2.7,−1.1], both P<.001); these match their corresponding rows. Figures show distributions/proportions rather than the same modeled contrast.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S442 — eTable 9: BMI (kg/m²) — MI

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.23](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=23>).
- **Population / denominators:** Multiple-imputation block ONLY; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Chained-equation imputation and all printed predictors/fractions retained in S476.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
BMI (kg/m²) — MI
Baseline mean (SD): I 32.6 (3.4), C 32.6 (3.5)
12-month modeled change (95% CI): I -1.4 (-1.4 to -1.3), C -0.3 (-0.3 to -0.2)
Between-group difference (95% CI): -1.1 (-1.2 to -1.0); P <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Matched main risk-factor narrative is MI at 12 months when supplied (waist −3.3 [−3.6,−2.9], SBP −1.9 [−2.7,−1.1], both P<.001); these match their corresponding rows. Figures show distributions/proportions rather than the same modeled contrast.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S443 — eTable 9: Serum cholesterol (mg/dL) — MI

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.23](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=23>).
- **Population / denominators:** Multiple-imputation block ONLY; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Chained-equation imputation and all printed predictors/fractions retained in S476.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
Serum cholesterol (mg/dL) — MI
Baseline mean (SD): I 197 (37.5), C 197 (37.7)
12-month modeled change (95% CI): I -3.0 (-4.2 to -1.7), C -1.8 (-3.1 to -0.6)
Between-group difference (95% CI): -1.1 (-2.9 to 0.7); P 0.23
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Matched main risk-factor narrative is MI at 12 months when supplied (waist −3.3 [−3.6,−2.9], SBP −1.9 [−2.7,−1.1], both P<.001); these match their corresponding rows. Figures show distributions/proportions rather than the same modeled contrast.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S444 — eTable 9: LDL-c (mg/dL) — MI

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.23](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=23>).
- **Population / denominators:** Multiple-imputation block ONLY; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Chained-equation imputation and all printed predictors/fractions retained in S476.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
LDL-c (mg/dL) — MI
Baseline mean (SD): I 121 (32.2), C 121 (32.2)
12-month modeled change (95% CI): I -2.9 (-4.0 to -1.8), C -2.3 (-3.4 to -1.2)
Between-group difference (95% CI): -0.6 (-2.2 to 1.0); P 0.48
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Matched main risk-factor narrative is MI at 12 months when supplied (waist −3.3 [−3.6,−2.9], SBP −1.9 [−2.7,−1.1], both P<.001); these match their corresponding rows. Figures show distributions/proportions rather than the same modeled contrast.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S445 — eTable 9: HDL-c (mg/dL) — MI

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.23](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=23>).
- **Population / denominators:** Multiple-imputation block ONLY; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Chained-equation imputation and all printed predictors/fractions retained in S476.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
HDL-c (mg/dL) — MI
Baseline mean (SD): I 48 (11.8), C 48 (11.7)
12-month modeled change (95% CI): I 2.0 (1.7 to 2.3), C 0.9 (0.6 to 1.2)
Between-group difference (95% CI): 1.1 (0.7 to 1.6); P <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Matched main risk-factor narrative is MI at 12 months when supplied (waist −3.3 [−3.6,−2.9], SBP −1.9 [−2.7,−1.1], both P<.001); these match their corresponding rows. Figures show distributions/proportions rather than the same modeled contrast.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S446 — eTable 9: NonHDL-c (mg/dL) — MI

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.24](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=24>).
- **Population / denominators:** Multiple-imputation block ONLY; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Chained-equation imputation and all printed predictors/fractions retained in S476.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
NonHDL-c (mg/dL) — MI
Baseline mean (SD): I 149 (35.1), C 149 (35.1)
12-month modeled change (95% CI): I -4.9 (-6.0 to -3.7), C -2.9 (-4.1 to -1.7)
Between-group difference (95% CI): -1.9 (-3.6 to -0.3); P 0.02
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Matched main risk-factor narrative is MI at 12 months when supplied (waist −3.3 [−3.6,−2.9], SBP −1.9 [−2.7,−1.1], both P<.001); these match their corresponding rows. Figures show distributions/proportions rather than the same modeled contrast.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S447 — eTable 9: Cholesterol:HDL-c ratio — MI

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.24](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=24>).
- **Population / denominators:** Multiple-imputation block ONLY; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Chained-equation imputation and all printed predictors/fractions retained in S476.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
Cholesterol:HDL-c ratio — MI
Baseline mean (SD): I 4.3 (1.1), C 4.2 (1)
12-month modeled change (95% CI): I -0.2 (-0.3 to -0.2), C -0.1 (-0.1 to -0.1)
Between-group difference (95% CI): -0.1 (-0.2 to -0.1); P <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Matched main risk-factor narrative is MI at 12 months when supplied (waist −3.3 [−3.6,−2.9], SBP −1.9 [−2.7,−1.1], both P<.001); these match their corresponding rows. Figures show distributions/proportions rather than the same modeled contrast.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S448 — eTable 9: Triglycerides (mg/dL) — MI

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.24](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=24>).
- **Population / denominators:** Multiple-imputation block ONLY; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Chained-equation imputation and all printed predictors/fractions retained in S476.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
Triglycerides (mg/dL) — MI
Baseline mean (SD): I 151 (76.4), C 153 (78.3)
12-month modeled change (95% CI): I -12.8 (-15.4 to -10.3), C -2.9 (-5.4 to -0.4)
Between-group difference (95% CI): -9.9 (-13.6 to -6.3); P <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Matched main risk-factor narrative is MI at 12 months when supplied (waist −3.3 [−3.6,−2.9], SBP −1.9 [−2.7,−1.1], both P<.001); these match their corresponding rows. Figures show distributions/proportions rather than the same modeled contrast.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S449 — eTable 9: SBP (mmHg) — MI

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.24](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=24>).
- **Population / denominators:** Multiple-imputation block ONLY; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Chained-equation imputation and all printed predictors/fractions retained in S476.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
SBP (mmHg) — MI
Baseline mean (SD): I 140 (17.1), C 139 (16.6)
12-month modeled change (95% CI): I -4.1 (-4.7 to -3.5), C -2.2 (-2.8 to -1.7)
Between-group difference (95% CI): -1.9 (-2.7 to -1.1); P <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Matched main risk-factor narrative is MI at 12 months when supplied (waist −3.3 [−3.6,−2.9], SBP −1.9 [−2.7,−1.1], both P<.001); these match their corresponding rows. Figures show distributions/proportions rather than the same modeled contrast.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S450 — eTable 9: DBP (mmHg) — MI

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.24](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=24>).
- **Population / denominators:** Multiple-imputation block ONLY; all included randomized participants, I n=3,272, C n=3,311.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Chained-equation imputation and all printed predictors/fractions retained in S476.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
DBP (mmHg) — MI
Baseline mean (SD): I 81 (10), C 81 (9.8)
12-month modeled change (95% CI): I -2.4 (-2.8 to -2.1), C -1.5 (-1.8 to -1.2)
Between-group difference (95% CI): -1 (-1.4 to -0.5); P <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** Matched main risk-factor narrative is MI at 12 months when supplied (waist −3.3 [−3.6,−2.9], SBP −1.9 [−2.7,−1.1], both P<.001); these match their corresponding rows. Figures show distributions/proportions rather than the same modeled contrast.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S451 — eTable 9: Weight (kg) — CC

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.23](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=23>).
- **Population / denominators:** Completers-only block ONLY; I n=2,840, C n=2,946.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Completers-only block is separate from MI.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
Weight (kg) — CC
Baseline mean (SD): I 86.5 (12.9), C 86.3 (13)
12-month modeled change (95% CI): I -3.8 (-4.1 to -3.6), C -0.8 (-1.0 to -0.5)
Between-group difference (95% CI): -3.1 (-3.4 to -2.7); P <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** The MI block and main MI results are separate analysis populations. Printed completer denominator is not assigned to main dietary or graphical results.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S452 — eTable 9: Waist (cm) — CC

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.23](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=23>).
- **Population / denominators:** Completers-only block ONLY; I n=2,840, C n=2,946.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Completers-only block is separate from MI.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
Waist (cm) — CC
Baseline mean (SD): I 107 (9.6), C 108 (9.7)
12-month modeled change (95% CI): I -4.4 (-4.7 to -4.2), C -1.1 (-1.3 to -0.9)
Between-group difference (95% CI): -3.3 (-3.7 to -3.0); P <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** The MI block and main MI results are separate analysis populations. Printed completer denominator is not assigned to main dietary or graphical results.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S453 — eTable 9: BMI (kg/m²) — CC

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.23](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=23>).
- **Population / denominators:** Completers-only block ONLY; I n=2,840, C n=2,946.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Completers-only block is separate from MI.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
BMI (kg/m²) — CC
Baseline mean (SD): I 32.5 (3.4), C 32.5 (3.5)
12-month modeled change (95% CI): I -1.4 (-1.5 to -1.3), C -0.3 (-0.4 to -0.2)
Between-group difference (95% CI): -1.1 (-1.3 to -1.0); P <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** The MI block and main MI results are separate analysis populations. Printed completer denominator is not assigned to main dietary or graphical results.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S454 — eTable 9: Serum cholesterol (mg/dL) — CC

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.23](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=23>).
- **Population / denominators:** Completers-only block ONLY; I n=2,840, C n=2,946.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Completers-only block is separate from MI.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
Serum cholesterol (mg/dL) — CC
Baseline mean (SD): I 196 (37), C 197 (37.6)
12-month modeled change (95% CI): I -2.9 (-4.2 to -1.7), C -1.9 (-3.1 to -0.6)
Between-group difference (95% CI): -1.1 (-2.8 to 0.7); P 0.24
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** The MI block and main MI results are separate analysis populations. Printed completer denominator is not assigned to main dietary or graphical results.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S455 — eTable 9: LDL-c (mg/dL) — CC

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.23](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=23>).
- **Population / denominators:** Completers-only block ONLY; I n=2,840, C n=2,946.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Completers-only block is separate from MI.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
LDL-c (mg/dL) — CC
Baseline mean (SD): I 120 (32), C 121 (32.1)
12-month modeled change (95% CI): I -2.9 (-4.0 to -1.8), C -2.3 (-3.4 to -1.2)
Between-group difference (95% CI): -0.6 (-2.2 to 1.0); P 0.45
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** The MI block and main MI results are separate analysis populations. Printed completer denominator is not assigned to main dietary or graphical results.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S456 — eTable 9: HDL-c (mg/dL) — CC

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.23](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=23>).
- **Population / denominators:** Completers-only block ONLY; I n=2,840, C n=2,946.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Completers-only block is separate from MI.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
HDL-c (mg/dL) — CC
Baseline mean (SD): I 48 (11.9), C 48 (11.7)
12-month modeled change (95% CI): I 2.2 (1.8 to 2.5), C 0.9 (0.6 to 1.2)
Between-group difference (95% CI): 1.3 (0.8 to 1.7); P <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** The MI block and main MI results are separate analysis populations. Printed completer denominator is not assigned to main dietary or graphical results.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S457 — eTable 9: NonHDL-c (mg/dL) — CC

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.24](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=24>).
- **Population / denominators:** Completers-only block ONLY; I n=2,840, C n=2,946.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Completers-only block is separate from MI.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
NonHDL-c (mg/dL) — CC
Baseline mean (SD): I 148 (34.7), C 149 (34.9)
12-month modeled change (95% CI): I -5.2 (-6.4 to -4.0), C -2.7 (-3.9 to -1.6)
Between-group difference (95% CI): -2.5 (-4.2 to -0.8); P 0.004
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** The MI block and main MI results are separate analysis populations. Printed completer denominator is not assigned to main dietary or graphical results.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S458 — eTable 9: Cholesterol:HDL-c ratio — CC

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.24](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=24>).
- **Population / denominators:** Completers-only block ONLY; I n=2,840, C n=2,946.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Completers-only block is separate from MI.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
Cholesterol:HDL-c ratio — CC
Baseline mean (SD): I 4.3 (1.1), C 4.2 (1)
12-month modeled change (95% CI): I -0.3 (-0.3 to -0.2), C -0.1 (-0.1 to -0.1)
Between-group difference (95% CI): -0.1 (-0.2 to -0.1); P <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** The MI block and main MI results are separate analysis populations. Printed completer denominator is not assigned to main dietary or graphical results.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S459 — eTable 9: Triglycerides (mg/dL) — CC

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.24](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=24>).
- **Population / denominators:** Completers-only block ONLY; I n=2,840, C n=2,946.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Completers-only block is separate from MI.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
Triglycerides (mg/dL) — CC
Baseline mean (SD): I 148 (72.4), C 150 (74.1)
12-month modeled change (95% CI): I -14.6 (-17.2 to -12.1), C -4.2 (-6.7 to -1.7)
Between-group difference (95% CI): -10.4 (-14 to -6.9); P <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** The MI block and main MI results are separate analysis populations. Printed completer denominator is not assigned to main dietary or graphical results.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S460 — eTable 9: SBP (mmHg) — CC

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.24](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=24>).
- **Population / denominators:** Completers-only block ONLY; I n=2,840, C n=2,946.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Completers-only block is separate from MI.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
SBP (mmHg) — CC
Baseline mean (SD): I 139 (17.1), C 139 (16.6)
12-month modeled change (95% CI): I -3.9 (-4.5 to -3.3), C -2.2 (-2.7 to -1.6)
Between-group difference (95% CI): -1.7 (-2.6 to -0.9); P <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** The MI block and main MI results are separate analysis populations. Printed completer denominator is not assigned to main dietary or graphical results.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S461 — eTable 9: DBP (mmHg) — CC

- **Exact location and document role:** REPORT DOC-004 eTable 9, [PDF p.24](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=24>).
- **Population / denominators:** Completers-only block ONLY; I n=2,840, C n=2,946.
- **Time / contrast / reference:** 12 months only; within-arm baseline-to-follow-up changes; between-group contrast intervention minus control, control reference.
- **Model / confidence level:** Mixed-effect models with site and intracluster/couple random factors; means and 95% CIs. Completers-only block is separate from MI.
- **Printed values:** Columns in the retained layout for eTables 6–8 are I change (95% CI), C change (95% CI), I-minus-C difference (95% CI), P; baseline rows use their printed SD or IQR. eTable 9 below is transcribed exclusively from the named block.

```text
DBP (mmHg) — CC
Baseline mean (SD): I 81 (9.9), C 81 (9.7)
12-month modeled change (95% CI): I -2.5 (-2.8 to -2.2), C -1.5 (-1.8 to -1.2)
Between-group difference (95% CI): -1.0 (-1.5 to -0.6); P <0.001
```

- **Pass-1 checks:** All supplied arm and difference point estimates contained; endpoints ordered; displayed direction coherent; source model/population attribution identified; no qualifying method contradiction. Exact P/statistic/standard-error compatibility is limited by the specifically named missing inputs in the shared checks. Baseline dispersions are not treated as standard errors.
- **Matched-result context:** The MI block and main MI results are separate analysis populations. Printed completer denominator is not assigned to main dietary or graphical results.
- **Inclusion outcome:** No emitted finding for this record after four-criterion self-screen; possible modeled/crude, display-precision and unmatched-analysis observations are consolidated in the checker Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

## Complete eFigure 3 distribution families

### S462 — eFigure 3: Energy intake (SD)

- **Exact location and document role:** REPORT DOC-004 eFigure 3, [PDF p.27](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=27>).
- **Population / denominator:** Randomized arm labels intervention and control; exact graphical contributor counts and MI/completer identity not printed. No table denominator assigned by assumption.
- **Time / all series:** 6-month I (purple), 6-month C (gray), 12-month I (purple), 12-month C (gray); all four box-and-whisker distributions visually inspected.
- **Scale / printed values:** Changes in common units of baseline SD; horizontal ticks −3, −2, −1, 0, 1, 2, 3. No exact numerical median, quartile, whisker endpoint, confidence interval, effect estimate, P value, standard error or test statistic printed. Plot label: Energy intake (SD).
- **Direction / visual observation:** Intervention relative to control lower. Both time points: I median left of C, I/C boxes near or below zero. These statements describe graphical positions, not extracted numerical estimates. Whiskers and all boxes cross or span zero in the broader distributions; no confidence-interval interpretation assigned.
- **Pass-1 checks:** Time/arm/scale matched; figure direction compatible with raw-unit nutrient changes after distinguishing observed distributions from modeled means. Median containment in boxes and ordered graphical box endpoints observed. Exact standardized numerical reproduction cannot be attempted because baseline SD choice/graph contributor population and exact coordinates are unreported. No qualifying statistical-method contradiction from the assigned caption.
- **Inclusion outcome:** No emitted finding; missing exact plot coordinates/population and assumed CI tests are excluded as conditional/unreported.
- **Pass 1:** PASS_1_COMPLETE.

### S463 — eFigure 3: Protein intake, %kcal (SD)

- **Exact location and document role:** REPORT DOC-004 eFigure 3, [PDF p.27](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=27>).
- **Population / denominator:** Randomized arm labels intervention and control; exact graphical contributor counts and MI/completer identity not printed. No table denominator assigned by assumption.
- **Time / all series:** 6-month I (purple), 6-month C (gray), 12-month I (purple), 12-month C (gray); all four box-and-whisker distributions visually inspected.
- **Scale / printed values:** Changes in common units of baseline SD; horizontal ticks −3, −2, −1, 0, 1, 2, 3. No exact numerical median, quartile, whisker endpoint, confidence interval, effect estimate, P value, standard error or test statistic printed. Plot label: Protein intake, %kcal (SD).
- **Direction / visual observation:** Intervention relative to control higher. Both times: I median right of C; positive I central location. These statements describe graphical positions, not extracted numerical estimates. Whiskers and all boxes cross or span zero in the broader distributions; no confidence-interval interpretation assigned.
- **Pass-1 checks:** Time/arm/scale matched; figure direction compatible with raw-unit nutrient changes after distinguishing observed distributions from modeled means. Median containment in boxes and ordered graphical box endpoints observed. Exact standardized numerical reproduction cannot be attempted because baseline SD choice/graph contributor population and exact coordinates are unreported. No qualifying statistical-method contradiction from the assigned caption.
- **Inclusion outcome:** No emitted finding; missing exact plot coordinates/population and assumed CI tests are excluded as conditional/unreported.
- **Pass 1:** PASS_1_COMPLETE.

### S464 — eFigure 3: CHO intake, %kcal (SD)

- **Exact location and document role:** REPORT DOC-004 eFigure 3, [PDF p.27](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=27>).
- **Population / denominator:** Randomized arm labels intervention and control; exact graphical contributor counts and MI/completer identity not printed. No table denominator assigned by assumption.
- **Time / all series:** 6-month I (purple), 6-month C (gray), 12-month I (purple), 12-month C (gray); all four box-and-whisker distributions visually inspected.
- **Scale / printed values:** Changes in common units of baseline SD; horizontal ticks −3, −2, −1, 0, 1, 2, 3. No exact numerical median, quartile, whisker endpoint, confidence interval, effect estimate, P value, standard error or test statistic printed. Plot label: CHO intake, %kcal (SD).
- **Direction / visual observation:** Intervention relative to control lower. Both times: I median left of C; negative central locations. These statements describe graphical positions, not extracted numerical estimates. Whiskers and all boxes cross or span zero in the broader distributions; no confidence-interval interpretation assigned.
- **Pass-1 checks:** Time/arm/scale matched; figure direction compatible with raw-unit nutrient changes after distinguishing observed distributions from modeled means. Median containment in boxes and ordered graphical box endpoints observed. Exact standardized numerical reproduction cannot be attempted because baseline SD choice/graph contributor population and exact coordinates are unreported. No qualifying statistical-method contradiction from the assigned caption.
- **Inclusion outcome:** No emitted finding; missing exact plot coordinates/population and assumed CI tests are excluded as conditional/unreported.
- **Pass 1:** PASS_1_COMPLETE.

### S465 — eFigure 3: Fat intake, %kcal (SD)

- **Exact location and document role:** REPORT DOC-004 eFigure 3, [PDF p.27](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=27>).
- **Population / denominator:** Randomized arm labels intervention and control; exact graphical contributor counts and MI/completer identity not printed. No table denominator assigned by assumption.
- **Time / all series:** 6-month I (purple), 6-month C (gray), 12-month I (purple), 12-month C (gray); all four box-and-whisker distributions visually inspected.
- **Scale / printed values:** Changes in common units of baseline SD; horizontal ticks −3, −2, −1, 0, 1, 2, 3. No exact numerical median, quartile, whisker endpoint, confidence interval, effect estimate, P value, standard error or test statistic printed. Plot label: Fat intake, %kcal (SD).
- **Direction / visual observation:** Intervention relative to control higher. Both times: I median right of C; positive central locations. These statements describe graphical positions, not extracted numerical estimates. Whiskers and all boxes cross or span zero in the broader distributions; no confidence-interval interpretation assigned.
- **Pass-1 checks:** Time/arm/scale matched; figure direction compatible with raw-unit nutrient changes after distinguishing observed distributions from modeled means. Median containment in boxes and ordered graphical box endpoints observed. Exact standardized numerical reproduction cannot be attempted because baseline SD choice/graph contributor population and exact coordinates are unreported. No qualifying statistical-method contradiction from the assigned caption.
- **Inclusion outcome:** No emitted finding; missing exact plot coordinates/population and assumed CI tests are excluded as conditional/unreported.
- **Pass 1:** PASS_1_COMPLETE.

### S466 — eFigure 3: SFA intake, %kcal (SD)

- **Exact location and document role:** REPORT DOC-004 eFigure 3, [PDF p.27](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=27>).
- **Population / denominator:** Randomized arm labels intervention and control; exact graphical contributor counts and MI/completer identity not printed. No table denominator assigned by assumption.
- **Time / all series:** 6-month I (purple), 6-month C (gray), 12-month I (purple), 12-month C (gray); all four box-and-whisker distributions visually inspected.
- **Scale / printed values:** Changes in common units of baseline SD; horizontal ticks −3, −2, −1, 0, 1, 2, 3. No exact numerical median, quartile, whisker endpoint, confidence interval, effect estimate, P value, standard error or test statistic printed. Plot label: SFA intake, %kcal (SD).
- **Direction / visual observation:** Intervention relative to control lower. Both times: I median left of C; negative central locations. These statements describe graphical positions, not extracted numerical estimates. Whiskers and all boxes cross or span zero in the broader distributions; no confidence-interval interpretation assigned.
- **Pass-1 checks:** Time/arm/scale matched; figure direction compatible with raw-unit nutrient changes after distinguishing observed distributions from modeled means. Median containment in boxes and ordered graphical box endpoints observed. Exact standardized numerical reproduction cannot be attempted because baseline SD choice/graph contributor population and exact coordinates are unreported. No qualifying statistical-method contradiction from the assigned caption.
- **Inclusion outcome:** No emitted finding; missing exact plot coordinates/population and assumed CI tests are excluded as conditional/unreported.
- **Pass 1:** PASS_1_COMPLETE.

### S467 — eFigure 3: MUFA intake, %kcal (SD)

- **Exact location and document role:** REPORT DOC-004 eFigure 3, [PDF p.27](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=27>).
- **Population / denominator:** Randomized arm labels intervention and control; exact graphical contributor counts and MI/completer identity not printed. No table denominator assigned by assumption.
- **Time / all series:** 6-month I (purple), 6-month C (gray), 12-month I (purple), 12-month C (gray); all four box-and-whisker distributions visually inspected.
- **Scale / printed values:** Changes in common units of baseline SD; horizontal ticks −3, −2, −1, 0, 1, 2, 3. No exact numerical median, quartile, whisker endpoint, confidence interval, effect estimate, P value, standard error or test statistic printed. Plot label: MUFA intake, %kcal (SD).
- **Direction / visual observation:** Intervention relative to control higher. Both times: I median right of C; positive central locations. These statements describe graphical positions, not extracted numerical estimates. Whiskers and all boxes cross or span zero in the broader distributions; no confidence-interval interpretation assigned.
- **Pass-1 checks:** Time/arm/scale matched; figure direction compatible with raw-unit nutrient changes after distinguishing observed distributions from modeled means. Median containment in boxes and ordered graphical box endpoints observed. Exact standardized numerical reproduction cannot be attempted because baseline SD choice/graph contributor population and exact coordinates are unreported. No qualifying statistical-method contradiction from the assigned caption.
- **Inclusion outcome:** No emitted finding; missing exact plot coordinates/population and assumed CI tests are excluded as conditional/unreported.
- **Pass 1:** PASS_1_COMPLETE.

### S468 — eFigure 3: RATIO MUFA:SFA (SD)

- **Exact location and document role:** REPORT DOC-004 eFigure 3, [PDF p.27](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=27>).
- **Population / denominator:** Randomized arm labels intervention and control; exact graphical contributor counts and MI/completer identity not printed. No table denominator assigned by assumption.
- **Time / all series:** 6-month I (purple), 6-month C (gray), 12-month I (purple), 12-month C (gray); all four box-and-whisker distributions visually inspected.
- **Scale / printed values:** Changes in common units of baseline SD; horizontal ticks −3, −2, −1, 0, 1, 2, 3. No exact numerical median, quartile, whisker endpoint, confidence interval, effect estimate, P value, standard error or test statistic printed. Plot label: RATIO MUFA:SFA (SD).
- **Direction / visual observation:** Intervention relative to control higher. Both times: I median right of C; positive central locations. These statements describe graphical positions, not extracted numerical estimates. Whiskers and all boxes cross or span zero in the broader distributions; no confidence-interval interpretation assigned.
- **Pass-1 checks:** Time/arm/scale matched; figure direction compatible with raw-unit nutrient changes after distinguishing observed distributions from modeled means. Median containment in boxes and ordered graphical box endpoints observed. Exact standardized numerical reproduction cannot be attempted because baseline SD choice/graph contributor population and exact coordinates are unreported. No qualifying statistical-method contradiction from the assigned caption.
- **Inclusion outcome:** No emitted finding; missing exact plot coordinates/population and assumed CI tests are excluded as conditional/unreported.
- **Pass 1:** PASS_1_COMPLETE.

### S469 — eFigure 3: PUFA intake, %kcal (SD)

- **Exact location and document role:** REPORT DOC-004 eFigure 3, [PDF p.27](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=27>).
- **Population / denominator:** Randomized arm labels intervention and control; exact graphical contributor counts and MI/completer identity not printed. No table denominator assigned by assumption.
- **Time / all series:** 6-month I (purple), 6-month C (gray), 12-month I (purple), 12-month C (gray); all four box-and-whisker distributions visually inspected.
- **Scale / printed values:** Changes in common units of baseline SD; horizontal ticks −3, −2, −1, 0, 1, 2, 3. No exact numerical median, quartile, whisker endpoint, confidence interval, effect estimate, P value, standard error or test statistic printed. Plot label: PUFA intake, %kcal (SD).
- **Direction / visual observation:** Intervention relative to control higher. Both times: I median right of C; positive central locations. These statements describe graphical positions, not extracted numerical estimates. Whiskers and all boxes cross or span zero in the broader distributions; no confidence-interval interpretation assigned.
- **Pass-1 checks:** Time/arm/scale matched; figure direction compatible with raw-unit nutrient changes after distinguishing observed distributions from modeled means. Median containment in boxes and ordered graphical box endpoints observed. Exact standardized numerical reproduction cannot be attempted because baseline SD choice/graph contributor population and exact coordinates are unreported. No qualifying statistical-method contradiction from the assigned caption.
- **Inclusion outcome:** No emitted finding; missing exact plot coordinates/population and assumed CI tests are excluded as conditional/unreported.
- **Pass 1:** PASS_1_COMPLETE.

### S470 — eFigure 3: FIBER intake (SD)

- **Exact location and document role:** REPORT DOC-004 eFigure 3, [PDF p.27](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=27>).
- **Population / denominator:** Randomized arm labels intervention and control; exact graphical contributor counts and MI/completer identity not printed. No table denominator assigned by assumption.
- **Time / all series:** 6-month I (purple), 6-month C (gray), 12-month I (purple), 12-month C (gray); all four box-and-whisker distributions visually inspected.
- **Scale / printed values:** Changes in common units of baseline SD; horizontal ticks −3, −2, −1, 0, 1, 2, 3. No exact numerical median, quartile, whisker endpoint, confidence interval, effect estimate, P value, standard error or test statistic printed. Plot label: FIBER intake (SD).
- **Direction / visual observation:** Intervention relative to control higher. Both times: I median right of C; positive central locations. These statements describe graphical positions, not extracted numerical estimates. Whiskers and all boxes cross or span zero in the broader distributions; no confidence-interval interpretation assigned.
- **Pass-1 checks:** Time/arm/scale matched; figure direction compatible with raw-unit nutrient changes after distinguishing observed distributions from modeled means. Median containment in boxes and ordered graphical box endpoints observed. Exact standardized numerical reproduction cannot be attempted because baseline SD choice/graph contributor population and exact coordinates are unreported. No qualifying statistical-method contradiction from the assigned caption.
- **Inclusion outcome:** No emitted finding; missing exact plot coordinates/population and assumed CI tests are excluded as conditional/unreported.
- **Pass 1:** PASS_1_COMPLETE.

### S471 — eFigure 3: CHOLESTEROL intake (SD)

- **Exact location and document role:** REPORT DOC-004 eFigure 3, [PDF p.27](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=27>).
- **Population / denominator:** Randomized arm labels intervention and control; exact graphical contributor counts and MI/completer identity not printed. No table denominator assigned by assumption.
- **Time / all series:** 6-month I (purple), 6-month C (gray), 12-month I (purple), 12-month C (gray); all four box-and-whisker distributions visually inspected.
- **Scale / printed values:** Changes in common units of baseline SD; horizontal ticks −3, −2, −1, 0, 1, 2, 3. No exact numerical median, quartile, whisker endpoint, confidence interval, effect estimate, P value, standard error or test statistic printed. Plot label: CHOLESTEROL intake (SD).
- **Direction / visual observation:** Intervention relative to control largely overlapping. Both times: distributions around zero with broad overlap; no numerical ranking or P reconstructed. These statements describe graphical positions, not extracted numerical estimates. Whiskers and all boxes cross or span zero in the broader distributions; no confidence-interval interpretation assigned.
- **Pass-1 checks:** Time/arm/scale matched; figure direction compatible with raw-unit nutrient changes after distinguishing observed distributions from modeled means. Median containment in boxes and ordered graphical box endpoints observed. Exact standardized numerical reproduction cannot be attempted because baseline SD choice/graph contributor population and exact coordinates are unreported. No qualifying statistical-method contradiction from the assigned caption.
- **Inclusion outcome:** No emitted finding; missing exact plot coordinates/population and assumed CI tests are excluded as conditional/unreported.
- **Pass 1:** PASS_1_COMPLETE.

### S472 — eFigure 3: w-3 intake (SD)

- **Exact location and document role:** REPORT DOC-004 eFigure 3, [PDF p.27](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=27>).
- **Population / denominator:** Randomized arm labels intervention and control; exact graphical contributor counts and MI/completer identity not printed. No table denominator assigned by assumption.
- **Time / all series:** 6-month I (purple), 6-month C (gray), 12-month I (purple), 12-month C (gray); all four box-and-whisker distributions visually inspected.
- **Scale / printed values:** Changes in common units of baseline SD; horizontal ticks −3, −2, −1, 0, 1, 2, 3. No exact numerical median, quartile, whisker endpoint, confidence interval, effect estimate, P value, standard error or test statistic printed. Plot label: w-3 intake (SD).
- **Direction / visual observation:** Intervention relative to control higher. Both times: I median right of C; positive I central locations. These statements describe graphical positions, not extracted numerical estimates. Whiskers and all boxes cross or span zero in the broader distributions; no confidence-interval interpretation assigned.
- **Pass-1 checks:** Time/arm/scale matched; figure direction compatible with raw-unit nutrient changes after distinguishing observed distributions from modeled means. Median containment in boxes and ordered graphical box endpoints observed. Exact standardized numerical reproduction cannot be attempted because baseline SD choice/graph contributor population and exact coordinates are unreported. No qualifying statistical-method contradiction from the assigned caption.
- **Inclusion outcome:** No emitted finding; missing exact plot coordinates/population and assumed CI tests are excluded as conditional/unreported.
- **Pass 1:** PASS_1_COMPLETE.

### S473 — eFigure 3: Alcohol intake, %kcal (SD)

- **Exact location and document role:** REPORT DOC-004 eFigure 3, [PDF p.27](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=27>).
- **Population / denominator:** Randomized arm labels intervention and control; exact graphical contributor counts and MI/completer identity not printed. No table denominator assigned by assumption.
- **Time / all series:** 6-month I (purple), 6-month C (gray), 12-month I (purple), 12-month C (gray); all four box-and-whisker distributions visually inspected.
- **Scale / printed values:** Changes in common units of baseline SD; horizontal ticks −3, −2, −1, 0, 1, 2, 3. No exact numerical median, quartile, whisker endpoint, confidence interval, effect estimate, P value, standard error or test statistic printed. Plot label: Alcohol intake, %kcal (SD).
- **Direction / visual observation:** Intervention relative to control slightly lower. Both times: narrow near-zero distributions, I slightly left of C. These statements describe graphical positions, not extracted numerical estimates. Whiskers and all boxes cross or span zero in the broader distributions; no confidence-interval interpretation assigned.
- **Pass-1 checks:** Time/arm/scale matched; figure direction compatible with raw-unit nutrient changes after distinguishing observed distributions from modeled means. Median containment in boxes and ordered graphical box endpoints observed. Exact standardized numerical reproduction cannot be attempted because baseline SD choice/graph contributor population and exact coordinates are unreported. No qualifying statistical-method contradiction from the assigned caption.
- **Inclusion outcome:** No emitted finding; missing exact plot coordinates/population and assumed CI tests are excluded as conditional/unreported.
- **Pass 1:** PASS_1_COMPLETE.

## Associated method, missingness, and unit records

### S474 — Baseline-value replacement sensitivity rule

- **Exact locations and roles:** REPORT DOC-004 [eTable 6 p.16](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=16>), [eTable 7 p.17](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=17>), [eTable 8 p.21](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=21>); REPORT main Statistical Analysis [p.4](<../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4>).
- **Printed rule and affected families:** Replace all missing values with baseline; included randomized I3,272/C3,311; 6- and 12-month means (95% CI) fitted with mixed models; all S401–S439. Main source explicitly describes this post hoc sensitivity, distinct from MI and completers.
- **Check / missing definition:** Zero change for an individually replaced value follows the source rule. It does not establish that the fitted marginal mean equals a contributor-weighted crude mean. Model fitting weights and individual missing/observed score changes are unavailable. A direct aggregate scaling of main MI/completer means cannot adjudicate this method.
- **Inclusion outcome / limitations:** No qualifying internally contradictory step; no alternative method proposed. MODELED versus crude observation recorded once in the checker.
- **Pass 1:** PASS_1_COMPLETE.

### S475 — Mixed-effect model and test attribution

- **Exact locations and roles:** REPORT DOC-004 model footnotes [p.16](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=16>), [p.17](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=17>), [p.19](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=19>), [p.20](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=20>), [p.21](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=21>), [p.22](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=22>), [p.24](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=24>); REPORT main Statistical Analysis [p.4](<../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4>).
- **Printed statements:** Means (95% CI) calculated using mixed effect models taking into account site and intra-cluster correlations (couples) as random factors. Main source identifies three-level linear model with random intercepts site, participant and family cluster; two-sided tests, P<.05, exploratory secondary analyses and no additional type I error adjustment.
- **Check:** Repeated observations and family/site dependence are explicitly addressed. Abbreviated footnotes do not assert omission of participant dependence. Each table's P applies to its labeled between-group change contrast. There is no source-grounded independent-sample, variance-estimator or covariance contradiction.
- **Precisely missing inputs:** Named per-cell test statistic/test family (e.g. Wald versus likelihood ratio), degrees of freedom, exact covariance matrix/standard errors, CI construction and MI-specific pooling details. Exact estimate–CI–P equality cannot be inferred from a normal approximation. No supplied standard error/test statistic can be crosschecked.
- **Decision rules:** No NI/equivalence margin, multiplicity/interim boundary or stopping conclusion in the assigned displays. No such hypothesis/decision mapping was supplied or inferred.
- **Inclusion outcome:** No emitted finding; missing test-specific details alone screened as CONDITIONAL_OR_UNREPORTED.
- **Pass 1:** PASS_1_COMPLETE.

### S476 — eTable 9 MICE, predictors, fractions, and separate populations

- **Exact locations and roles:** REPORT DOC-004 [eTable 9 p.23](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=23>) and [p.24](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=24>).
- **Printed populations:** MI all included randomized I3,272/C3,311 (sum6,583); completers-only I2,840/C2,946 (sum5,786); 12-month change only. S440–S450 and S451–S461 keep these distinct.
- **Printed method:** Multiple imputation using chained equations; predictors intervention group, sex, age at baseline, smoking status, educational level, physical activity, baseline BMI, total energy intake, and baseline value of variable to be imputed.
- **Every printed imputation fraction:** BMI5%; body weight4.7%; waist9.4%; serum cholesterol10.1%; HDL-c10.8%; LDL-c10.9%; nonHDL-c10.9%; cholesterol:HDL10.9%; triglycerides10.3%; SBP6.1%; DBP6.2%.
- **Check / missing definitions:** Fractions vary by variable, so one overall completer count is not asserted by the source to equal every variable-specific observed count. Exact by-arm observed counts, denominator used for each fraction and common-completer selection rule are not printed. No integer reverse calculation is promoted to a contradiction. Nutrition completer counts concern a different instrument. General main imputation description is not assumed to override this table's explicit chained-equation method.
- **Inclusion outcome:** No emitted finding; unmatched-population and missing-definition observations screened once in the checker.
- **Pass 1:** PASS_1_COMPLETE.

### S477 — Units, conversion factors, and figure standardization

- **Exact locations and roles:** REPORT DOC-004 [eTables 6 p.16](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=16>), [7 p.17](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=17>), [8 p.21](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=21>), [8 p.22](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=22>), [9 p.24](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=24>), [eFigure3 p.27](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=27>).
- **Printed scales and units:** Scores er-MedDiet0–17/MDS0–9/MEDAS0–14/PDQS0–42; foods g/week; energy kcal/d; protein/carbohydrate/fat/SFA/MUFA/PUFA/alcohol %E; MUFA:SFA unitless; fiber and omega-3 g/week; cholesterol mg/week; sodium g/week. Risk units kg/cm/kg/m²/mg/dL/mmHg or ratio as each family above.
- **Printed conversion factors:** Cholesterol, HDL-c and LDL-c mg/dL ×0.0259 gives mmol/L; triglycerides mg/dL ×0.0113. No corresponding mmol/L result printed for numerical agreement checking.
- **Printed figure definition:** Changes expressed in common units of baseline standard deviations after6 and12months in control/intervention. Labels %kcal and table %E immediately refer to percentage of energy; SD on figure is standardization, not a printed standard error or CI.
- **Check / missing definitions:** Units and directions coherent once energy percentages, raw weekly totals and dimensionless standardized changes are separated. No reported converted pair, exact plotted standardized quantile or arm/pooled-SD denominator is supplied for mechanical recomputation. No missing conversion or preferred transformation is proposed.
- **Inclusion outcome:** No emitted finding; display/scale context and unreported graphical definitions handled under checker exclusions.
- **Pass 1:** PASS_1_COMPLETE.

## Completion and limitations

All 77 S records have PASS_1_COMPLETE. The complete assigned table data, including every time cell/arm, the p.20 continuation footnote, eTable9 fractions/predictors/conversions and all48 eFigure3 distributions, were covered. No scientific source-unit or assigned-family gap. Exact per-cell test statistics, standard errors, degrees of freedom and covariance are unreported; exact graph coordinates/contributor counts and baseline-SD denominator are unreported. These limitations constrain mechanical reproduction but create no finding by themselves. Findings0; consolidated excluded observations8, documented in checkers/parts/statistical_pass_1_support_b.md. No severity, validity, disposition or correction is assigned.

