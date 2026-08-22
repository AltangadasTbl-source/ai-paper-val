# Statistical Consistency Pass 1

## Scope and method

**Reviewer execution:** fresh `gpt-5.6-terra` / high-effort statistical-pass-1 specialist (runtime ID is recorded by the coordinator in `agent_execution_manifest.md`).

**Assigned scope:** canonical relationships `S001` through `S038` (all 38 records in `statistics/relationship_inventory.md`), using their cited fresh mapper records and the supplied direct PDFs/layout assets only. No web source, legacy audit derivative, severity judgment, validity disposition, or correction was used.

For every applicable result, this pass checked printed interval order and containment of the printed estimate; sign/direction against the named arm order and displayed group values; effect-measure/model/scale labels; repetitions after exact endpoint/population/model matching; direct count/denominator/percentage arithmetic; and P/test/statistic/SE compatibility only where the supplied source identified a compatible calculation. A failure to reproduce a model-dependent statistic without its needed model inputs is recorded as a limitation, not as a conclusion.

`SF` identifiers below are lane-local discovery records, not stable candidate IDs. Every record, including every `SF` record, is **Pending Human Adjudication**.

## Relationship-by-relationship completion record

| S ID | Fresh evidence checked | PASS_1_COMPLETE finding | Candidate references |
|---|---|---|---|
| S001 | DOC-001 PDF pp. 1, 5-6; MS001 | MD -0.27 is within -1.74 to 1.19; endpoints ordered; repeated abstract/table/narrative values match; two-sided t-test rule supplied. P=.71 is directionally compatible. | None |
| S002 | DOC-001 PDF p. 6; MS002 | Sensitivity P=.72 is a lone model result. Random-effect GLMM is named, but no estimate/test statistic/SE is supplied for mechanical reproduction. Narrative statement is not contradictory. | None — missing GLMM output/variance definition. |
| S003 | DOC-001 PDF p. 6; MS003 | MD -0.56 is within -1.61 to 0.49; endpoint order and group-mean direction (5.4 minus 6.0) agree to display rounding. No P is printed. | None |
| S004 | DOC-001 PDF pp. 1, 6; MS004 | MD 0.39 is within -1.09 to 1.89 and agrees with 9.6 minus 9.2 to rounding. Abstract/Table 2 repeat. Inverse-Gaussian GLM is named; no SE or model output is supplied to reproduce P=.58. | None |
| S005 | DOC-001 PDF pp. 6-7; MS005 | HR 0.94 lies in 0.80-1.09, has ordered positive-ratio endpoints, and P=.41 is compatible with a null-crossing CI. Table mean-difference and curve HR are separately labelled estimands. Schoenfeld P=.21 is a proportional-hazards diagnostic, not the treatment-effect P. | None |
| S006 | DOC-001 PDF pp. 1, 6; MS006 | MD -0.60 lies in -3.52 to 2.31 and equals 20.4 minus 21.0 to shown precision. Abstract/Table 2 agree. No GLM inputs exist to reproduce P=.68. | None |
| S007 | DOC-001 PDF pp. 6-7; MS007 | HR 1.02 lies in 0.87-1.19, endpoints ordered, and P=.83 is compatible with the null-crossing CI. Table mean-difference and curve HR are explicitly different estimands. Schoenfeld P=.82 is diagnostic only. | None |
| S008 | DOC-001 PDF p. 6; MS008 | ICU-mortality point estimate/CI order/P were checked. The article Methods calls mortality rates Cox HRs, whereas the Table 2 row and footnote call ICU mortality RR; the printed RR also does not reproduce from its printed risks under the stated RR label. | SF001, SF002 |
| S009 | DOC-001 PDF p. 6; MS009 | Hospital-mortality CI is ordered and contains 1.06. Its Table 2 RR label is the same label family as S008; the printed RR does not reproduce from its printed risks under that label. | SF003 |
| S010 | DOC-001 PDF pp. 1, 6; MS010 | HR 1.12 lies in 0.90-1.40; endpoints ordered; P=.30 compatible with null-crossing CI; abstract/table match. Cox model and two-sided rule supplied, but time-to-event data/SE are not supplied. | None |
| S011 | DOC-001 PDF pp. 1, 6-7; MS011 | HR 1.07 lies in 0.87-1.31; endpoints ordered; P=.54 compatible; abstract/table/Figure 2B agree. Schoenfeld P=.13 is a diagnostic. | None |
| S012 | DOC-001 PDF pp. 1, 6; MS012 | CI is ordered and contains RR 0.86, but 17/448 divided by 23/462 is 0.762 (about 0.76), not 0.86 under the printed risk-ratio label. Abstract/table agree with each other. | SF004 |
| S013 | DOC-001 PDF pp. 1, 6; MS013 | CI is ordered and contains RR 1.07, but 19/450 divided by 17/462 is 1.147 (about 1.15), not 1.07 under the printed risk-ratio label. Abstract/table agree with each other. | SF005 |
| S014 | DOC-001 PDF pp. 1, 6; MS014 | CI is ordered and contains RR 1.16, but 8/448 divided by 6/462 is 1.375 (about 1.38), not 1.16 under the printed risk-ratio label. Abstract/table agree with each other. | SF006 |
| S015 | DOC-001 PDF pp. 1, 6; MS015 | CI is ordered and contains RR 1.00, but 51/449 divided by 52/464 is 1.014 (about 1.01), not 1.00 to two decimals under the printed risk-ratio label. Abstract/table agree with each other. | SF007 |
| S016 | DOC-001 PDF p. 6; MS016 | CI is ordered and contains RR 0.84, but 20/448 divided by 28/463 is 0.738 (about 0.74), not 0.84 under the printed risk-ratio label. | SF008 |
| S017 | DOC-001 PDF p. 6; MS017 | CI is ordered and contains RR 0.87, but 12/448 divided by 16/463 is 0.775 (about 0.78), not 0.87 under the printed risk-ratio label. | SF009 |
| S018 | DOC-001 PDF p. 6; MS018 | CI is ordered and contains RR 1.15, but 149/343 divided by 132/361 is 1.188 (about 1.19), not 1.15 under the printed risk-ratio label. | SF010 |
| S019 | DOC-001 PDF p. 6; MS019 | CI is ordered and contains RR 1.03, but 54/477 divided by 52/484 is 1.054 (about 1.05), not 1.03 under the printed risk-ratio label. | SF011 |
| S020 | DOC-001 PDF p. 7; MS020 | HR 0.99 lies in 0.86-1.14, endpoints ordered, P=.92 compatible with a null-crossing CI, and curve arm/time labels are unambiguous. Kaplan-Meier/Cox identity is distinct from the VFD t-test. Schoenfeld P=.68 is diagnostic. | None |
| S021 | DOC-001 PDF p. 6; DOC-004 PDF p. 9; MS021 | Both subgroup point estimates are within ordered printed intervals and signs agree with group means to rounding. The same inside-ICU values are labelled IQR in the main paper but 95% CI in eTable 5. | SF012 |
| S022 | DOC-001 PDF p. 4; MS022 | This is an analysis-method relationship, not a numerical result. Mixed longitudinal model, random intercepts, and continuous time are named, but no matching numerical model output is in DOC-001. | None — no applicable numerical reconciliation. |
| S023 | DOC-001 PDF p. 4; MS023 | Two-sided alpha=.05 and no multiplicity adjustment are stated. This is a global interpretation rule, not an individual effect estimate. | None — no applicable numerical reconciliation. |
| S024 | DOC-002 PDF p. 19; DOC-003 PDF p. 11; US001 | Protocol/SAP planned 397 per arm with a 1-day difference, common SD 5, 80% power, two-sided alpha=.05, then 20% simple inflation to 476 per arm (397 x 1.20 = 476.4, consistent with an integer planning target). Actual enrollment is a later result, not a contradiction. | None |
| S025 | DOC-002 PDF p. 33; US002 | Planned Cox/95%-confidence/ITT-per-protocol description. No reported point estimate, interval, or test statistic in this record. | None — planned-analysis-only relationship. |
| S026 | DOC-002 PDF pp. 33-35; US003 | Planned test/model catalogue only. Each prospective procedure has no result here; no result-to-rule calculation is applicable. | None — planned-analysis-only relationship. |
| S027 | DOC-003 PDF pp. 11-13; US004 | SAP rule identifies VFD Student t test/mean difference and liberation Kaplan-Meier/log-rank. Main-paper matched VFD result uses a mean difference/t test; no conflict is printed. | None |
| S028 | DOC-003 PDF p. 13; US005 | SAP distinguishes 28/90-day Cox HR from ICU/hospital RR and other binary-outcome RR. This agrees with Table 2's 28/90-day HR labels and its ICU/hospital RR footnote, but exposes the main-article generic mortality-HR wording recorded in SF001. | SF001 (cross-location model-label comparison) |
| S029 | DOC-003 PDF pp. 13-15; US006 | Planned per-protocol, subgroup-interaction, and exploratory-model definitions. No individual results in this record; main eTable 5 labels interaction P values, not within-subgroup P values. | None — no direct numerical result in this record. |
| S030 | DOC-003 PDF pp. 21-22; US007 | Amendment table expressly distinguishes planned-versus-final-paper identities and says the paper changed to t test/mean difference and Gaussian subgroup GLM. These stated changes are not result contradictions. | None |
| S031 | DOC-004 PDF p. 5/eTable 1; US008 | All-mode rows were checked for count/percentage arithmetic and interval order (IQRs). The supplied source does not name a per-cell exact test, so P values were not recomputed. Printed `<.001` values are finite-precision inequality displays, not display-zero candidates. | None |
| S032 | DOC-004 PDF p. 6/eTable 2; US009 | Mode-stratum N values sum to eTable 1 N at each time point (452/463, 391/410, 321/343, 272/296). Most IQRs are ordered; Other-mode intermediate PEEP after titration is printed 8 (5-1), whose endpoints are reversed and do not contain 8. Per-cell P test is unnamed. | SF013 |
| S033 | DOC-004 PDF p. 7/eTable 3; US010 | Mode-stratum N values match eTable 2/eTable 1 totals. Direct count/percentage checks agree to rounding except the printed `35.` is an incomplete precision display for 7/20 (35.0), with no contradictory number. The two `---` cells are zero-count comparisons with no P printed, not P=0. | None |
| S034 | DOC-004 PDF p. 8/eTable 4; US011 | Rows containing explicit numerator/denominator reproduce their percentages. Four count-plus-percent rows lack printed denominators and do not reconcile with the displayed arm-header Ns; source does not state the alternative denominators needed to reproduce them. `P=1.00` is ordinary finite-precision display; `NA` is not a test. | SF014, SF015, SF016, SF017 |
| S035 | DOC-004 PDF p. 9/eTable 5; US012 | All 18 mean differences lie within their printed ordered 95% CIs. Signs agree with low minus intermediate means to the displayed rounding; one interaction P is printed per modifier. The inside-ICU interval-label mismatch is cross-recorded as SF012. | SF012 |
| S036 | DOC-004 PDF p. 10/eFigure 1; US013 | Graphical cumulative VFD curves have arm, axis, and 0-28 day scale but no printed estimate/CI/test/P; no numerical statistical calculation is applicable. | None |
| S037 | DOC-004 PDF pp. 11-13/eFigures 2-4; US014 | Distribution figures have no printed numerical estimate, interval, test, or P. | None — no applicable numerical reconciliation. |
| S038 | DOC-005 PDF p. 1; US015 | Direct source contains no applicable statistical relationship. | None — documented no-applicable scope. |

## Lane-local candidate records

### SF001 — Mortality effect-measure/model label conflict

**Candidate statement:** DOC-001's Statistical Analysis says mortality rates were reported as Cox-model hazard ratios, while Table 2 identifies ICU and hospital mortality estimates as risk ratios; the supplied SAP specifically plans ICU/hospital mortality as RR and 28/90-day mortality as Cox HR.

**Category:** Measure, label, or scale inconsistency.

**Exact source locations:** `jama_simonis_2018_oi_180108.pdf` PDF p. 4 (Statistical Analysis) and p. 6 (Table 2, footnotes c-d); `joi180108supp2_prod.pdf` PDF p. 13 (Secondary outcomes).

**Printed values/statements:** Main Methods: “ICU and hospital length of stay and mortality rates were compared using Kaplan-Meier survival curves and reported as hazard ratios calculated from a Cox proportional hazard model.” Table 2 labels ICU mortality `RR, 1.11 (0.96-1.27)` and hospital mortality `RR, 1.06 (0.93-1.22)`; footnote c says “Effect estimate is risk ratio.” The SAP separately says ICU/hospital mortality RR and 28/90-day mortality Cox HR.

**Rule and calculation:** A result cannot simultaneously be called an HR and an RR without a supplied explanation that the general Methods sentence excludes ICU/hospital mortality. This is a direct label/model comparison, not an attempt to infer an unreported model.

**Alternative source-grounded interpretation:** The Table 2 footnotes and SAP may be the specific definitions, with the main Methods wording overbroad; the package does not explicitly resolve the scope of the generic “mortality rates” sentence.

**Human question:** Which effect measure and model were used for ICU and hospital mortality, and should the main Methods sentence or the Table 2 label/footnote be revised for consistency?

### SF002 — ICU-mortality RR does not reproduce from printed risks

**Candidate statement:** Under Table 2's explicit RR label, ICU-mortality risks yield 1.17, not the printed RR 1.11.

**Category:** Statistical reporting inconsistency.

**Exact source location:** `jama_simonis_2018_oi_180108.pdf` PDF p. 6, Table 2 ICU mortality and footnote c.

**Printed values:** Low 132/450 (29.3%); intermediate 115/458 (25.1%); `RR, 1.11 (0.96-1.27)`.

**Rule and calculation:** Printed-risk ratio = `(132/450) / (115/458) = 1.167`, which rounds to 1.17 (not 1.11).

**Alternative source-grounded interpretation:** The estimate may derive from an unreported time-to-event or modeled analysis, consistent with the HR/RR label conflict in SF001; the supplied Table 2 footnote nevertheless calls it an RR.

**Human question:** What numerator/denominator population and RR estimator generated 1.11, and is it the same estimand as the printed risks?

### SF003 — Hospital-mortality RR does not reproduce from printed risks

**Candidate statement:** Under Table 2's explicit RR label, hospital-mortality risks yield 1.09, not the printed RR 1.06.

**Category:** Statistical reporting inconsistency.

**Exact source location:** `jama_simonis_2018_oi_180108.pdf` PDF p. 6, Table 2 hospital mortality and footnote c.

**Printed values:** Low 151/477 (31.7%); intermediate 140/484 (28.9%); `RR, 1.06 (0.93-1.22)`.

**Rule and calculation:** `(151/477) / (140/484) = 1.094`, which rounds to 1.09 (not 1.06).

**Alternative source-grounded interpretation:** A model-derived or differently defined population estimate may have been printed, but the supplied source neither names such a model for this row nor qualifies the RR label.

**Human question:** What estimator/population generated 1.06, and should the table identify it if it is not the ratio of the displayed risks?

### SF004 — ARDS RR does not reproduce from printed risks

**Candidate statement:** Under Table 2's explicit RR label, ARDS risks yield 0.76, not the printed RR 0.86.

**Category:** Statistical reporting inconsistency.

**Exact source location:** `jama_simonis_2018_oi_180108.pdf` PDF p. 6, Table 2 ARDS and footnote c.

**Printed values:** Low 17/448 (3.8%); intermediate 23/462 (5.0%); `RR, 0.86 (0.59-1.24)`.

**Rule and calculation:** `(17/448) / (23/462) = 0.762`, which rounds to 0.76 (not 0.86).

**Alternative source-grounded interpretation:** A different, unreported RR estimator or analysis population may have been used.

**Human question:** What calculation or population produced RR 0.86 under the table's RR label?

### SF005 — Pneumonia RR does not reproduce from printed risks

**Candidate statement:** Under Table 2's explicit RR label, pneumonia risks yield 1.15, not the printed RR 1.07.

**Category:** Statistical reporting inconsistency.

**Exact source location:** `jama_simonis_2018_oi_180108.pdf` PDF p. 6, Table 2 pneumonia and footnote c.

**Printed values:** Low 19/450 (4.2%); intermediate 17/462 (3.7%); `RR, 1.07 (0.78-1.47)`.

**Rule and calculation:** `(19/450) / (17/462) = 1.147`, which rounds to 1.15 (not 1.07).

**Alternative source-grounded interpretation:** A different, unreported RR estimator or analysis population may have been used.

**Human question:** What calculation or population produced RR 1.07 under the table's RR label?

### SF006 — Pneumothorax RR does not reproduce from printed risks

**Candidate statement:** Under Table 2's explicit RR label, pneumothorax risks yield 1.38, not the printed RR 1.16.

**Category:** Statistical reporting inconsistency.

**Exact source location:** `jama_simonis_2018_oi_180108.pdf` PDF p. 6, Table 2 pneumothorax and footnote c.

**Printed values:** Low 8/448 (1.8%); intermediate 6/462 (1.3%); `RR, 1.16 (0.73-1.84)`.

**Rule and calculation:** `(8/448) / (6/462) = 1.375`, which rounds to 1.38 (not 1.16).

**Alternative source-grounded interpretation:** A different, unreported RR estimator or analysis population may have been used.

**Human question:** What calculation or population produced RR 1.16 under the table's RR label?

### SF007 — Atelectasis RR does not reproduce from printed risks

**Candidate statement:** Under Table 2's explicit RR label, atelectasis risks yield 1.01, not the printed RR 1.00.

**Category:** Statistical reporting inconsistency.

**Exact source location:** `jama_simonis_2018_oi_180108.pdf` PDF p. 6, Table 2 atelectasis and footnote c.

**Printed values:** Low 51/449 (11.4%); intermediate 52/464 (11.2%); `RR, 1.00 (0.81-1.23)`.

**Rule and calculation:** `(51/449) / (52/464) = 1.014`, which rounds to 1.01 (not 1.00).

**Alternative source-grounded interpretation:** The one-hundredths difference may reflect a model-derived estimator or an unreported precision/analysis population, neither of which is defined for this row.

**Human question:** What calculation or population produced RR 1.00 under the table's RR label?

### SF008 — Extrapulmonary-infection RR does not reproduce from printed risks

**Candidate statement:** Under Table 2's explicit RR label, extrapulmonary-infection risks yield 0.74, not the printed RR 0.84.

**Category:** Statistical reporting inconsistency.

**Exact source location:** `jama_simonis_2018_oi_180108.pdf` PDF p. 6, Table 2 extrapulmonary infection and footnote c.

**Printed values:** Low 20/448 (4.5%); intermediate 28/463 (6.0%); `RR, 0.84 (0.60-1.18)`.

**Rule and calculation:** `(20/448) / (28/463) = 0.738`, which rounds to 0.74 (not 0.84).

**Alternative source-grounded interpretation:** A different, unreported RR estimator or analysis population may have been used.

**Human question:** What calculation or population produced RR 0.84 under the table's RR label?

### SF009 — Extrapulmonary-sepsis RR does not reproduce from printed risks

**Candidate statement:** Under Table 2's explicit RR label, extrapulmonary-sepsis risks yield 0.78, not the printed RR 0.87.

**Category:** Statistical reporting inconsistency.

**Exact source location:** `jama_simonis_2018_oi_180108.pdf` PDF p. 6, Table 2 extrapulmonary sepsis and footnote c.

**Printed values:** Low 12/448 (2.7%); intermediate 16/463 (3.5%); `RR, 0.87 (0.56-1.33)`.

**Rule and calculation:** `(12/448) / (16/463) = 0.775`, which rounds to 0.78 (not 0.87).

**Alternative source-grounded interpretation:** A different, unreported RR estimator or analysis population may have been used.

**Human question:** What calculation or population produced RR 0.87 under the table's RR label?

### SF010 — Delirium RR does not reproduce from printed risks

**Candidate statement:** Under Table 2's explicit RR label, delirium risks yield 1.19, not the printed RR 1.15.

**Category:** Statistical reporting inconsistency.

**Exact source location:** `jama_simonis_2018_oi_180108.pdf` PDF p. 6, Table 2 delirium and footnote c.

**Printed values:** Low 149/343 (43.4%); intermediate 132/361 (36.6%); `RR, 1.15 (0.99-1.34)`.

**Rule and calculation:** `(149/343) / (132/361) = 1.188`, which rounds to 1.19 (not 1.15).

**Alternative source-grounded interpretation:** A different, unreported RR estimator or analysis population may have been used.

**Human question:** What calculation or population produced RR 1.15 under the table's RR label?

### SF011 — Tracheostomy RR does not reproduce from printed risks

**Candidate statement:** Under Table 2's explicit RR label, tracheostomy risks yield 1.05, not the printed RR 1.03.

**Category:** Statistical reporting inconsistency.

**Exact source location:** `jama_simonis_2018_oi_180108.pdf` PDF p. 6, Table 2 tracheostomy and footnote c.

**Printed values:** Low 54/477 (11.3%); intermediate 52/484 (10.7%); `RR, 1.03 (0.84-1.26)`.

**Rule and calculation:** `(54/477) / (52/484) = 1.054`, which rounds to 1.05 (not 1.03).

**Alternative source-grounded interpretation:** A different, unreported RR estimator or analysis population may have been used.

**Human question:** What calculation or population produced RR 1.03 under the table's RR label?

### SF012 — Same subgroup intervals labelled IQR in main text and 95% CI in eTable 5

**Candidate statement:** The main-paper subgroup narrative labels its inside- and outside-ICU mean-difference intervals as IQR, whereas DOC-004 eTable 5 presents the same values under `Mean Difference (95% CI)`.

**Category:** Measure, label, or scale inconsistency.

**Exact source locations:** `jama_simonis_2018_oi_180108.pdf` PDF p. 6, Subgroups and Exploratory Analyses; `joi180108supp3_prod.pdf` PDF p. 9, eTable 5 Start of ventilation.

**Printed values:** Main text: inside ICU `mean difference, -2.50 [IQR, -4.63 to -0.36]`; outside ICU `1.45 [IQR, -0.52 to 3.43]`; interaction P=.01. eTable 5 header: `Mean Difference (95% CI)` and the same two estimates/limits.

**Rule and calculation:** Exact repeated point and endpoint values map to one matched subgroup analysis; an IQR describes a distribution while a 95% CI describes inferential uncertainty. The printed values themselves are properly ordered and contain their point estimates.

**Alternative source-grounded interpretation:** The main narrative may contain a label/transcription error; the eTable's explicitly labelled inferential column may represent the intended designation.

**Human question:** Are the repeated intervals 95% CIs as eTable 5 states, and should the main-text `IQR` labels be corrected?

### SF013 — Reversed and non-containing PEEP IQR in eTable 2

**Candidate statement:** eTable 2 prints the Other-mode intermediate after-titration PEEP as `8 (5-1)`, whose endpoints are reversed and do not contain its median.

**Category:** Numeric or arithmetic inconsistency.

**Exact source location:** `joi180108supp3_prod.pdf` PDF p. 6, eTable 2, Other Mode of Ventilation, after titration on day of randomization, PEEP cmH2O, intermediate tidal volume.

**Printed values:** `8 (5-1)`, P=.50.

**Rule and calculation:** For the table's stated median (IQR) format, endpoint order requires lower <= upper and the median should lie within the displayed IQR. Here 5 > 1 and 8 is outside 5-1.

**Alternative source-grounded interpretation:** One endpoint may have been transcribed or typeset incorrectly; the unnamed per-cell P-value test does not resolve the interval display.

**Human question:** What are the correct intermediate-group PEEP quartiles for this cell?

### SF014 — Sedative-infusion percentages do not reconcile with displayed arm Ns

**Candidate statement:** eTable 4 lists sedative infusion counts/percentages that do not reproduce from its displayed arm-header Ns and does not print the denominators that would reproduce them.

**Category:** Denominator, proportion, or total inconsistency.

**Exact source location:** `joi180108supp3_prod.pdf` PDF p. 8, eTable 4, Sedative infusion and arm headers.

**Printed values:** Arm headers low n=477 and intermediate n=484; sedative infusion low `320 (70.6)` and intermediate `333 (72.1)`.

**Rule and calculation:** `320/477 = 67.1%`, not 70.6%; `333/484 = 68.8%`, not 72.1%. The displayed percentages imply approximately 453 and 462 denominators, respectively, but those denominators are not printed for this row.

**Alternative source-grounded interpretation:** The source may have used an unstated complete-case subset rather than header Ns.

**Human question:** What denominators were used for sedative infusion, and should they be displayed?

### SF015 — Analgesic-infusion percentages do not reconcile with displayed arm Ns

**Candidate statement:** eTable 4 lists analgesic infusion counts/percentages that do not reproduce from its displayed arm-header Ns and does not print the denominators that would reproduce them.

**Category:** Denominator, proportion, or total inconsistency.

**Exact source location:** `joi180108supp3_prod.pdf` PDF p. 8, eTable 4, Analgesic infusion and arm headers.

**Printed values:** Arm headers low n=477 and intermediate n=484; analgesic infusion low `277 (61.1)` and intermediate `273 (59.1)`.

**Rule and calculation:** `277/477 = 58.1%`, not 61.1%; `273/484 = 56.4%`, not 59.1%. The displayed percentages imply approximately 453 and 462 denominators, respectively, but those denominators are not printed for this row.

**Alternative source-grounded interpretation:** The source may have used an unstated complete-case subset rather than header Ns.

**Human question:** What denominators were used for analgesic infusion, and should they be displayed?

### SF016 — Neuromuscular-blockade percentages do not reconcile with displayed arm Ns

**Candidate statement:** eTable 4 lists neuromuscular-blockade counts/percentages that do not reproduce from its displayed arm-header Ns and does not print the denominators that would reproduce them.

**Category:** Denominator, proportion, or total inconsistency.

**Exact source location:** `joi180108supp3_prod.pdf` PDF p. 8, eTable 4, Neuromuscular blockade and arm headers.

**Printed values:** Arm headers low n=477 and intermediate n=484; neuromuscular blockade low `53 (11.7)` and intermediate `60 (13.0)`.

**Rule and calculation:** `53/477 = 11.1%`, not 11.7%; `60/484 = 12.4%`, not 13.0%. The displayed percentages imply approximately 453 and 462 denominators, respectively, but those denominators are not printed for this row.

**Alternative source-grounded interpretation:** The source may have used an unstated complete-case subset rather than header Ns.

**Human question:** What denominators were used for neuromuscular blockade, and should they be displayed?

### SF017 — Vasopressor-use percentages do not reconcile with displayed arm Ns

**Candidate statement:** eTable 4 lists vasopressor-use counts/percentages that do not reproduce from its displayed arm-header Ns and does not print the denominators that would reproduce them.

**Category:** Denominator, proportion, or total inconsistency.

**Exact source location:** `joi180108supp3_prod.pdf` PDF p. 8, eTable 4, Use of vasopressors and arm headers.

**Printed values:** Arm headers low n=477 and intermediate n=484; vasopressor use low `363 (80.0)` and intermediate `353 (76.4)`.

**Rule and calculation:** `363/477 = 76.1%`, not 80.0%; `353/484 = 72.9%`, not 76.4%. The displayed percentages imply approximately 454 and 462 denominators, respectively, but those denominators are not printed for this row.

**Alternative source-grounded interpretation:** The source may have used an unstated complete-case subset rather than header Ns.

**Human question:** What denominators were used for vasopressor use, and should they be displayed?

## Display-zero and inference safeguards

No coherent `P = 0`, `p = 0.000`, or equivalent display-zero P value occurs in the assigned records. Several entries use `<.001`, which are finite-precision inequality displays; eTable 3 uses `---` where both event counts are zero, which is no P result. Neither notation is a candidate. No tiny-tail calculation was performed.

## Completion, counts, and limitations

- **PASS_1_COMPLETE relationships:** 38/38 (`S001`-`S038`), including planned-only, graphical-only, and no-applicable records.
- **Lane-local candidate records:** 17 (`SF001`-`SF017`); all require human adjudication and must be de-duplicated against other lanes before any stable `C` ID is assigned.
- **No-candidate relationship records:** 25 (some records share a cross-record candidate, so the relationship/candidate totals are not additive).
- **Key limitations:** No individual-level data, event times, model matrices, SEs, degrees of freedom, covariance, or per-cell eTable test definitions were supplied. Exact P/CI compatibility was therefore not recomputed for model-dependent estimates. The observed RR-versus-printed-risk discrepancies are reported only under the table's explicit RR label; unreported alternate model/population explanations remain open human questions.
