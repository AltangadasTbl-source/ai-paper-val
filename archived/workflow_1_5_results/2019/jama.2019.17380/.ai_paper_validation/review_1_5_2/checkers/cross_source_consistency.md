# Cross-Source Consistency Check

## Scope and method

**Status: COMPLETE.** This checker reviewed every freshly mapped canonical numeric/reporting relationship `N001` through `N062` and every canonical inferential-statistical relationship `S001` through `S039`. Evidence was restricted to the supplied PDFs and fresh native/layout text and rendered-page assets in this review directory. No prior audit derivative was used as evidence.

For each matched occurrence, the comparison first matched population, analysis set, follow-up time, intervention contrast, model/adjustment, measure, scale, unit, reference group, direction, and displayed precision. Protocol and addendum values were treated as planned definitions rather than observed-result comparators unless the source identified the same implemented result.

## Complete relationship coverage

| Relationship IDs checked | Matched-source scope | Result |
|---|---|---|
| N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016 | Main abstract, methods, results narrative, Table 1, Figure 1, Table 2 and captions; trial-population, time, denominator, and unit matches | COMPLETE — no cross-source candidate observation. Displayed totals, rounding, and explicitly different analysis populations were compatible. |
| N017, N018, N019, N020 | Main abstract, Key Points, results narrative, Table 2, and Figure 2 vitamin-D panels | COMPLETE — no cross-source candidate observation. The Table 2 values, repeated primary-result estimates, directions, units, and vitamin-D Figure 2 counts match after accounting for the displayed measurement time. |
| N021 | Main Figure 2 panel B versus Table 2 omega-3 rows | COMPLETE — qualifying observation `XSC-001` recorded below. |
| N022 | Main Figure 2 panel D versus eTable 6 omega-3 rows and factorial arm identities | COMPLETE — qualifying observation `XSC-002` recorded below. |
| N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033, N034, N035 | Main narrative, Table 3, Figures 3-4, captions/footnotes, and relevant supplement tables/figures | COMPLETE — qualifying observations `XSC-003` and `XSC-004` concern the Figure 3 and Figure 4 subgroup column labels. All other matched measures, rate-versus-count distinctions, event definitions, analysis-set notes, and repeated values had no cross-source candidate observation. |
| N036, N037, N038, N039, N040, N041, N062 | Protocol and analytic-plan addendum versus the implemented article/supplement definitions | COMPLETE — no cross-source candidate observation. Planned 4-year/co-primary definitions, target enrollment, and planned analysis details differ from later implemented 5-year/addendum specifications, but the documents identify these as planning-stage material; this is not a same-result contradiction. |
| N042, N043, N044, N045, N046, N047, N048, N049, N050, N051, N052, N053, N054, N055, N056, N057, N058 | Supplementary methods and eTables 1-11 versus matched main tables/narrative where applicable | COMPLETE — no cross-source candidate observation. Complete-case, adherent, available-case, and UTI-excluded analyses were not compared as if identical populations; eGFR differences and urine-ACR ratios retained their stated scales; incidence rates were not treated as event counts. |
| N059 | eFigure 2 versus eTable 6 vitamin-D rows and Figure 3 | COMPLETE — qualifying observation `XSC-005` recorded below. |
| N060 | eFigure 3 versus eTable 6 omega-3 rows and Figure 4 | COMPLETE — qualifying observation `XSC-006` recorded below. |
| N061 | Data-sharing statement | COMPLETE — no result-bearing numeric comparison applicable. |
| S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020 | Main abstract, narrative, Tables 2-3, Figures 3-4, captions/footnotes, and methods | COMPLETE — no additional cross-source candidate observation. Repetitions matched at their printed precision; effect direction/reference and CI/P-value labels were preserved. |
| S021, S022, S023, S039 | Protocol and addendum statistical definitions/power/monitoring rules | COMPLETE — no same-result cross-source candidate observation. These are planned definitions, not competing reports of an observed analysis. |
| S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036 | Supplement calibration, eTables 4-10, and matching main-paper result definitions | COMPLETE — no additional cross-source candidate observation. Population changes and model/scale differences were explicit; rate, hazard-ratio, mean-difference, and ratio quantities were not conflated. |
| S037 | eFigure 2, eTable 6, and Figure 3 | COMPLETE — qualifying observation `XSC-005` recorded below; printed interaction P values and graphical ratio direction otherwise matched their stated vitamin-D comparison. |
| S038 | eFigure 3, eTable 6, and Figure 4 | COMPLETE — qualifying observation `XSC-006` recorded below; printed interaction P values and graphical ratio direction otherwise matched their stated omega-3 comparison. |

## Qualifying cross-source observations

### XSC-001 — Figure 2 omega-3 eGFR participant counts duplicate the vitamin-D counts

- **Category:** Cross-document numeric inconsistency; denominator, proportion, or total inconsistency.
- **Exact source locations:** [Main article Figure 2, PDF p. 7](<../../../../jama_de_boer_2019_oi_190122.pdf#page=7>); [main article Table 2, PDF p. 8](<../../../../jama_de_boer_2019_oi_190122.pdf#page=8>).
- **Printed evidence:** Figure 2 panel B, “eGFR by omega-3 fatty acids vs placebo,” prints placebo counts `607`, `459`, and `438`, and omega-3 counts `701`, `531`, and `496` at baseline, year 2, and year 5. Those are the panel-A vitamin-D counts. Table 2's omega-3 rows print active `657`, `499`, `472` and placebo `651`, `491`, `462` for the same eGFR outcome and time points.
- **Comparison logic:** Both displays are for the randomized omega-3-versus-placebo contrast and eGFR at baseline/year 2/year 5. The measure and time points match; the Figure 2 panel-B counts do not match the same-contrast Table 2 counts and instead equal the vitamin-D panel counts.
- **Supported alternatives:** The figure numbers could be an unreconciled display/production duplication, or Figure 2 may intend a distinct plotting-data subset. The panel caption says that numbers are participants contributing data at each time point and supplies no distinct population definition that would explain the printed omega-3 values.
- **Human verification steps:** Check the figure-generation dataset and the panel-B plotting code/output; confirm the omega-3 group labels and exact contributing-data counts at each time point.

### XSC-002 — Figure 2 omega-3 urine-ACR participant counts duplicate the vitamin-D counts

- **Category:** Cross-document numeric inconsistency; denominator, proportion, or total inconsistency.
- **Exact source locations:** [Main article Figure 2, PDF p. 7](<../../../../jama_de_boer_2019_oi_190122.pdf#page=7>); [Supplement eTable 6, PDF p. 11](<../../../../joi190122supp2_prod.pdf#page=11>).
- **Printed evidence:** Figure 2 panel D, “Urine ACR by omega-3 fatty acids vs placebo,” prints placebo `609`, `463`, `440` and omega-3 `702`, `529`, `505`. These are the panel-C vitamin-D counts. eTable 6's omega-3 rows print active `658`, `502`, `478` and placebo `653`, `490`, `467` for baseline/year 2/year 5 urine ACR.
- **Comparison logic:** Both displays identify the same omega-3-versus-placebo contrast, urine-ACR measure, and three time points. The Figure 2 panel-D counts do not agree with eTable 6's same-contrast counts and instead match Figure 2 panel C's vitamin-D counts.
- **Supported alternatives:** A figure-specific subset could in principle differ, but the Figure 2 caption identifies the numbers as participants contributing data at each time point and gives no separate omega-3 subset definition. A duplicated vitamin-D count row is therefore a source-grounded alternative explanation.
- **Human verification steps:** Check the panel-D source data and production proofs; verify the omega-3 arm assignment and the contributing urine-ACR counts at all three time points.

### XSC-003 — Figure 3 participant-count columns map to the opposite vitamin-D arms

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [Main article Figure 3, PDF p. 8](<../../../../jama_de_boer_2019_oi_190122.pdf#page=8>); [main article Table 2, PDF p. 8](<../../../../jama_de_boer_2019_oi_190122.pdf#page=8>).
- **Printed evidence:** Figure 3, titled “Effects of Vitamin D vs Placebo,” labels its overall columns `Placebo` `N=703`, mean eGFR change `−13.1 (14.4)`, and `Vitamin D` `N=609`, `−12.3 (14.8)`. Table 2 labels the vitamin-D active arm `N=701` baseline (and 496 at year 5) and placebo `N=607` baseline (and 438 at year 5). The Figure 3 overall group sizes align with randomized vitamin-D active `703` and placebo `609`, not with their Figure 3 labels; the active-directed displayed mean (`−12.3`) is printed below the column labelled Vitamin D but that column has the placebo-size `609`.
- **Comparison logic:** Figure 3's N columns place the randomized vitamin-D active total under placebo and the placebo total under vitamin D. Its overall mean changes remain aligned with the printed treatment headings and Table 2, so the reproducible mismatch is limited to participant counts.
- **Supported alternatives:** The N columns may be transposed while headings, mean-change values, and forest estimates remain as printed; no supplied source defines 703 as vitamin-D placebo and 609 as active vitamin D.
- **Human verification steps:** Verify the Figure 3 participant-count columns against randomization assignments and determine whether any subgroup estimate also requires remapping without assuming that it does.

### XSC-004 — Figure 4 participant-count columns map to the opposite omega-3 arms

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [Main article Figure 4, PDF p. 9](<../../../../jama_de_boer_2019_oi_190122.pdf#page=9>); [main article Table 2, PDF p. 8](<../../../../jama_de_boer_2019_oi_190122.pdf#page=8>).
- **Printed evidence:** Figure 4, titled “Effects of Omega-3 Fatty Acids vs Placebo,” labels its overall columns `Placebo` `N=659`, mean eGFR change `−13.1 (14.8)`, and `Omega-3 Fatty Acids` `N=653`, `−12.2 (14.5)`. Table 2 labels omega-3 active `N=657` baseline and placebo `N=651` baseline. The Figure 4 overall group sizes align with randomized omega-3 active `659` and placebo `653`, but are printed under the opposite labels.
- **Comparison logic:** Figure 4's N columns place the randomized omega-3 active total under placebo and the placebo total under omega-3. Its overall mean changes remain aligned with the printed headings and Table 2, limiting the reproducible mismatch to participant counts.
- **Supported alternatives:** The N columns may be transposed while headings, mean-change values, and forest estimates remain as printed; no different arm definition is supplied.
- **Human verification steps:** Verify Figure 4's participant-count columns against randomization assignments and determine whether any subgroup estimate also requires remapping without assuming that it does.

### XSC-005 — eFigure 2 participant-count columns map to the opposite vitamin-D arms

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [Supplement eFigure 2, PDF p. 18](<../../../../joi190122supp2_prod.pdf#page=18>); [Supplement eTable 6, PDF p. 11](<../../../../joi190122supp2_prod.pdf#page=11>).
- **Printed evidence:** eFigure 2 labels `Placebo` overall `N=703`, geometric mean change ratio `3.02 (4.10)`, and `Active intervention` `N=609`, `2.97 (4.50)`. eTable 6 labels vitamin-D active baseline `N=702`, year-5 ratio `2.97`, and placebo baseline `N=609`, year-5 ratio `3.02`.
- **Comparison logic:** The eFigure places randomized active N=703 under Placebo and placebo N=609 under Active intervention. Its `3.02` placebo and `2.97` active changes agree with eTable 6 under the printed headings; only the N columns are reproducibly mismapped.
- **Supported alternatives:** The participant-count columns may be transposed while headings, changes, and forest direction remain as printed. Randomized-versus-measured availability explains 703 versus 702 but not the N-column mapping.
- **Human verification steps:** Check eFigure 2's participant-count columns against allocation data and determine whether any subgroup estimate also requires remapping without presuming a broader reversal.

### XSC-006 — eFigure 3 participant-count columns map to the opposite omega-3 arms

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [Supplement eFigure 3, PDF p. 19](<../../../../joi190122supp2_prod.pdf#page=19>); [Supplement eTable 6, PDF p. 11](<../../../../joi190122supp2_prod.pdf#page=11>).
- **Printed evidence:** eFigure 3 labels `Placebo` overall `N=659`, geometric mean change ratio `3.05 (4.16)`, and `Active intervention` `N=653`, `2.94 (4.48)`. eTable 6 labels omega-3 active baseline `N=658`, year-5 ratio `2.94`, and placebo baseline `N=653`, year-5 ratio `3.05`.
- **Comparison logic:** The eFigure places randomized active N=659 under Placebo and placebo N=653 under Active intervention. Its `3.05` placebo and `2.94` active changes agree with eTable 6 under the printed headings; only the N columns are reproducibly mismapped.
- **Supported alternatives:** The participant-count columns may be transposed while headings, changes, and forest direction remain as printed. Randomized-versus-measured availability explains 659 versus 658 but not the N mapping.
- **Human verification steps:** Check eFigure 3's participant-count columns against allocation data and determine whether any subgroup estimate also requires remapping without presuming a broader reversal.

## Limitations

- The supplied package contains no raw participant-level data or figure-production files, so this checker cannot determine whether a label/count display issue arose in source data, analytic programming, or final production.
- Planned protocol and later implemented analyses legitimately differ in endpoint timing and definitions; they were not treated as contradictory observed results without a matched-result identity.
- This artifact records observations only. It assigns no stable candidate ID and makes no adjudication.
