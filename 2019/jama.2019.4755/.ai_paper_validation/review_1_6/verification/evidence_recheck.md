# Workflow 1.6 Mechanical Evidence Recheck

Status: COMPLETE for C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016. All sixteen stable IDs remain Pending Human Adjudication. These are evidence-record facts, without scientific adjudication or a prescribed final correction.

Runtime ID: 01a12871-ed60-7951-bfc9-08725b3b7034; role qc16_evidence_rechecker; model gpt-6.1-sol; reasoning effort high; start mode FRESH_SPAWN. The complete current candidate ledger, normative scope and review contract, routing preflight, tooling record, source inventory and complete source coverage were read. Old candidate sets and old review decisions were not used.

## Authority, tooling and complete scope

The supplied PDFs were final authority. All thirteen unique physical pages containing the registered comparisons were freshly rendered directly from the supplied sources and visually inspected, including three additional enlarged budget-page renders. Current and reused OCR/native text were locators only. PDF physical pages, rather than printed footers, determine every link: for example protocol PDF page 60 has printed footer page 59 of 61. No web, GPU, arbitrary Python, source change, or reused-artifact change was used.

Producing engine for every derivative listed here: direct pdftoppm, Poppler 26.01.0, CPU. Commands used the pattern `pdftoppm -f N -l N -r DPI -singlefile -png SOURCE OUTPUT_PREFIX`. Outputs are below review_1_6/preprocessing/. Two additional result-page layout locators were produced by direct pdftotext, Poppler 26.01.0, using `pdftotext -layout -f N -l N SOURCE OUTPUT.txt`. Arithmetic was independently reproduced using JavaScript numeric expressions; it does not substitute for visual confirmation.

| Source | Physical PDF pages | DPI | Fresh derivatives, relative to review_1_6/preprocessing/ |
|---|---|---:|---|
| jama_brenner_2019_oi_190039.pdf | 5 | 170 | recheck-main-p5.png |
| joi190039supp3_prod.pdf | 6, 7 | 155 | recheck-results-p6.png; recheck-results-p7.png |
| joi190039supp2_prod.pdf | 6, 8 | 130 | recheck-SAP-p6.png; recheck-SAP-p8.png |
| joi190039supp1_prod.pdf | 14, 26, 53, 56, 59, 60, 61, 62 | 130 | recheck-protocol-p14.png; recheck-protocol-p26.png; recheck-protocol-p53.png; recheck-protocol-p56.png; recheck-protocol-p59.png; recheck-protocol-p60.png; recheck-protocol-p61.png; recheck-protocol-p62.png |
| joi190039supp1_prod.pdf | 60 | 350 | recheck-protocol-p60-detail.png |
| joi190039supp1_prod.pdf | 61 | 240 | recheck-protocol-p61-detail.png |
| joi190039supp1_prod.pdf | 62 | 220 | recheck-protocol-p62-detail.png |
| joi190039supp3_prod.pdf | 6, 7 | Not applicable | recheck-results-p6-layout.txt; recheck-results-p7-layout.txt |

No extraction or source-location limitation remains for the registered comparisons. Definitions missing from the supplied package remain explicit human questions; they are not missing scientific coverage.

## Classification and evidence-state summary

All registered location roles and primary relationship codes remain unchanged. C001-C005 compare REPORT content within one results document each and are S_W. C006-C016 compare prospective analysis, operational, or financial PLAN content and are P_P. No PLAN text is a conflicting comparator in C001-C005, and no REPORT text is a conflicting comparator in C006-C016. Corroboration does not add P_R or S_C. Each candidate has exactly one substantive relationship code, so precedence P_R > P_P > S_C > S_W produces the stated primary code directly.

Three input-alignment facts require special attention: C011 has no stated participant base for optional blood purchases; C015 has no stated per-meeting application of its one cost bundle; C016 has no established identity of payment recipient/component. These are record_input_error, rather than reproduced arithmetic discrepancies. The source inputs themselves were read correctly, but the proposed mismatch depends on unsupported alignment and its residual cannot be settled. The IDs remain present. C006's p. 8 comparator describes the qualitative FD Hb/Hp cutoff, while p. 6 describes the FOBGold categorical variable; therefore identical test identity is not inferred. Its directly observed missing mass unit remains within the p. 6 paired-threshold expression, with the p. 8 fully stated concentration unit as contextual support.

| ID | Primary category | Relationship type | All relationships | Compared document roles | Review domain | Evidence state | Determining recheck fact |
|---|---|---|---|---|---|---|---|
| C001 | Measure, label, or scale inconsistency | S_W | S_W | REPORT main Table 3 vs REPORT main Table 2 | report_internal_inconsistency | recorded_candidate | Visibly blank Test cell; qualitative count values reproduce its arm predictive values. |
| C002 | Measure, label, or scale inconsistency | S_W | S_W | REPORT results eTable 5 vs REPORT results eTable 4 | report_internal_inconsistency | recorded_candidate | Visible eTable 5 unit stops at [µg; eTable 4 shows [µg Hb/g]. |
| C003 | Numeric or arithmetic inconsistency | S_W | S_W | REPORT results eTable 5 vs REPORT results eTable 4 | statistical_results | recorded_candidate | Minus-only visible point cell; counts reproduce -18.20431248 percentage points. |
| C004 | Numeric or arithmetic inconsistency | S_W | S_W | REPORT results eTable 5 vs REPORT results eTable 4 | statistical_results | recorded_candidate | Minus-only visible point cell; counts reproduce -25.71428571 percentage points. |
| C005 | Numeric or arithmetic inconsistency | S_W | S_W | REPORT results eTable 5 vs REPORT results eTable 4 | statistical_results | recorded_candidate | Minus-only visible point cell; counts reproduce -21.57258065 percentage points. |
| C006 | Measure, label, or scale inconsistency | P_P | P_P | PLAN SAP p. 6 section 3.2 paired 17 µg Hb/g expression vs PLAN SAP p. 6 section 3.2 10.2 Hb/g expression; PLAN SAP p. 8 complete FD threshold unit corroborates only | plan_material | recorded_candidate | p. 6 directly omits µg before 10.2 Hb/g in its paired-threshold expression. |
| C007 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol duration field vs PLAN dated schedule | plan_material | recorded_candidate | 60-month total beside January 2012 preparation and June 2017 study-end schedule; intended total endpoints missing. |
| C008 | Measure, label, or scale inconsistency | P_P | P_P | PLAN protocol working-day phrase vs PLAN parenthetical hours | plan_material | recorded_candidate | Literal 3 working days (72 hours) equivalence printed without a working-calendar definition. |
| C009 | Measure, label, or scale inconsistency | P_P | P_P | PLAN protocol summary volumes vs PLAN tube-specific options | plan_material | recorded_candidate | General 9-10 mL each versus explicitly listed 8.5 mL serum option. |
| C010 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol category 6 total vs PLAN components and total definition | plan_material | recorded_candidate | Dot in 1.704 confirmed; decimal branch rounds to subtotal, thousands branch differs by 1702 EUR. |
| C011 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol supplies total vs PLAN tube-price/quantity footnote | plan_material | record_input_error | No purchasing participant base; optional consent directly prevents assuming 2400 purchases. |
| C012 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol insurance amount vs PLAN attached formula | plan_material | recorded_candidate | 23.50 x 2400 = 56400, whereas attached total is 67116; exact ratio 1.19 has no printed modifier. |
| C013 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol 16 category totals vs PLAN overall budget | plan_material | recorded_candidate | Printed category sum 507605 differs from 505570 by 2035 EUR. |
| C014 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol printing line vs PLAN linked printing footnote | plan_material | recorded_candidate | Attached printing estimates 3000 and 3500 EUR differ by 500; scope/version absent. |
| C015 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol meeting total vs PLAN linked cost/frequency footnote | plan_material | record_input_error | 480 + 500 = 980 reconciles printed bundle; applying 480 separately to all four meetings is unsupported. |
| C016 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol center incentive vs PLAN practice-related budget footnote | plan_material | record_input_error | 30 x 2000 = 60000 reconciles; identity with the 75-EUR study-center incentive is not established. |

Evidence-state counts: recorded_candidate 13; not_reproduced 0; repaired_residual 0; record_input_error 3. All sixteen IDs require human adjudication. Mechanical suggested-disposition derivation is left to the coordinator under the normative scope; no disposition is assigned here.

## C001 — Men's Table 3 test identity

- **Location found:** Yes. [Main PDF p. 5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 3 Men third row, Test cell; comparator Table 2 Men Qualitative 10.2 row on the same physical page. Fresh render recheck-main-p5.png confirms the physical anchors.
- **Source value/text matched:** Yes. Third men's row Test cell is visibly blank, cutoff 10.2; aspirin PPV 27.5, NPV 89.2; placebo PPV 20, NPV 90.3; contrasts 7.5 (-6.4 to 20.2) and -1.1 (-5.3 to 3.0). The preceding men's rows explicitly show Quantitative at 10.2 and 17.0.
- **Comparator matched:** Yes. Table 2 Men Qualitative 10.2 aspirin TP 28, FN 43, TN 354, FP 74; placebo TP 12, FN 43, TN 400, FP 48. Both tables identify the intention-to-screen analysis and day 2 after the single dose.
- **Consistency rule applicable:** Yes, for explicit test identity associated with each diagnostic row. Matching counts are a diagnostic identity check, not proof that a missing label was intentionally qualitative.
- **Calculation/logical comparison reproduced:** Yes. PPV 100 x 28/102 = 27.45098039 and 100 x 12/60 = 20; NPV 100 x 354/397 = 89.16876574 and 100 x 400/443 = 90.29345372. Raw PPV difference 7.45098039 and NPV difference -1.12468798 round to the displayed 7.5 and -1.1. All four arm values round to the printed values at one decimal. This reproduces the missing-label observation, without an arithmetic inconsistency.
- **Necessary inputs available / exact missing inputs:** All count and displayed-value inputs available. Missing: intended Test label or an explicit continuation/omitted-label convention for this cell.
- **Source-grounded alternative:** An intended continuation of the preceding Quantitative label is possible as layout, but would produce a repeated quantitative 10.2 row and would not match those quantitative counts. Qualitative is strongly inferred from matched values and table structure, but is not printed in this cell.
- **Direct observation versus inference:** Blank cell and values direct; intended qualitative identity and downstream misclassification mechanism inferred.
- **Exact remaining human question:** Which test is intended for the men's third Table 3 row at cutoff 10.2, and is the blank Test cell an omitted label that needs clarification?
- **Classification confirmation:** REPORT Table 3 and REPORT Table 2, both observed results within the main article; primary/all S_W; measure/label category; report_internal_inconsistency. No role or relationship correction. Other documents would only corroborate intended identity.
- **Evidence state and determining fact:** recorded_candidate, because the source cell is blank and the matched qualitative counts reproduce its values. Pending Human Adjudication.

## C002 — Visible eTable 5 concentration unit

- **Location found:** Yes. [Results supplement p. 7](../../../joi190039supp3_prod.pdf#page=7), eTable 5 Cutoff header, compared with [p. 6](../../../joi190039supp3_prod.pdf#page=6), eTable 4 Cutoff header. [Main p. 5](../../../jama_brenner_2019_oi_190039.pdf#page=5) is unit corroboration only.
- **Source value/text matched:** Yes. Fresh visible page 7 header shows Cutoff followed by [µg, with no visible Hb/g] in that column. The abbreviation line defines g and Hb. Thresholds remain 10.2 and 17.0.
- **Comparator matched:** Yes. Fresh page 6 header visibly shows [µg Hb/g]. Main Tables 2/3 also show µg Hb/g; they do not independently conflict with the results supplement's intact header.
- **Consistency rule applicable:** Yes. µg alone labels mass; the adjacent fully stated label is mass of hemoglobin per gram. Matching thresholds and table context support the concentration-unit intention; there is no justified numeric unit conversion.
- **Calculation/logical comparison reproduced:** Yes as a dimensional/text comparison. Native fresh p. 7 layout text contains Hb/g] displaced below the ordinary visible header position, but the direct PDF rendering does not display that complete header. Native text is recorded without treating it as visible printed content.
- **Necessary inputs available / exact missing inputs:** Visible headers and matched cutoffs available. Missing: intended complete visible unit and any deliberate abbreviation/layout convention.
- **Source-grounded alternative:** Displaced/clipped PDF text or intended abbreviated typography can explain the difference; the hidden text does not make the ordinary displayed concentration unit complete.
- **Direct observation versus inference:** Incomplete visible header direct; clipping/production mechanism inferred.
- **Exact remaining human question:** Is the eTable 5 cutoff unit intended to be µg Hb/g, and should the full concentration denominator be visible in this header?
- **Classification confirmation:** Both substantive comparison locations are REPORT within one results supplement; primary/all S_W; measure/label category; report_internal_inconsistency. Main-report corroboration is not an additional S_C discrepancy. No classification correction.
- **Evidence state and determining fact:** recorded_candidate; incomplete visible unit persists on the direct fresh render despite recoverable displaced native text. Pending Human Adjudication.

## C003 — Women's quantitative 10.2 PPV contrast

- **Location found:** Yes. [Results p. 7](../../../joi190039supp3_prod.pdf#page=7), eTable 5 Women Quantitative 10.2 Difference in PPV; comparator [p. 6](../../../joi190039supp3_prod.pdf#page=6), eTable 4 matched Women Quantitative 10.2 count row.
- **Source value/text matched:** Yes. Visible PPV aspirin 15.9 and placebo 34.1; point cell shows a minus glyph with no magnitude; interval [-34.7, -1.3]. Fresh native text contains a displaced 18.2 fragment on a lower line, distinct from the visible cell.
- **Comparator matched:** Yes. Same per-protocol day-2 quantitative 10.2 result: aspirin TP 11 and FP 58; placebo TP 14 and FP 27. Fresh page 6 confirms all counts.
- **Consistency rule applicable:** Yes. PPV equals TP/(TP+FP) for the unadjusted diagnostic reproduction; the contrast is aspirin minus placebo as established by neighboring rows. This is a point-contrast visibility check, not reconstruction of the interval.
- **Calculation/logical comparison reproduced:** Yes. Aspirin 100 x 11/69 = 15.94202899; placebo 100 x 14/41 = 34.14634146; exact diagnostic difference -18.20431248 percentage points, rounding to -18.2. This independently confirms the ledger's -18.20431 approximation. Subtracting rounded displayed arms gives -18.2 as well.
- **Necessary inputs available / exact missing inputs:** Counts, arms and interval available. Missing: whether the minus-only visible cell intentionally marks an omitted estimate, and the intended visible reporting/layout convention. Interval variance inputs are not needed for this registered observation and were not invented.
- **Source-grounded alternative:** Minus as a missing-value symbol or displaced glyphs could explain the display. Hidden native digits support a possible layout cause; they do not establish a visible magnitude.
- **Direct observation versus inference:** Minus-only cell and interval direct; numerical point reconstruction and production explanation inferred.
- **Exact remaining human question:** Does this source cell intentionally omit the PPV point contrast, or should a magnitude be visible alongside its 95% interval?
- **Classification confirmation:** Both eTables are REPORT in the same results supplement; primary/all S_W; numeric/arithmetic category; statistical_results. No classification correction.
- **Evidence state and determining fact:** recorded_candidate; the point magnitude is absent from the ordinary visible source while matched inputs imply a finite contrast. Pending Human Adjudication.

## C004 — Women's quantitative 17.0 PPV contrast

- **Location found:** Yes. [Results p. 7](../../../joi190039supp3_prod.pdf#page=7), eTable 5 Women Quantitative 17.0 Difference in PPV; comparator [p. 6](../../../joi190039supp3_prod.pdf#page=6), matched eTable 4 row.
- **Source value/text matched:** Yes. Visible aspirin PPV 17.1, placebo 42.9; point cell minus only; interval [-48.4, -0.7]. Fresh native extraction has displaced 25.7, without a visible corresponding magnitude.
- **Comparator matched:** Yes. Per-protocol quantitative 17.0 aspirin TP 6, FP 29; placebo TP 9, FP 12. Population, day and threshold match.
- **Consistency rule applicable:** Yes for raw-count PPV and aspirin-minus-placebo point contrast; no interval or significance recomputation is required.
- **Calculation/logical comparison reproduced:** Yes. 100 x 6/35 = 17.14285714; 100 x 9/21 = 42.85714286; exact diagnostic difference -25.71428571 percentage points, rounding to -25.7. Subtracting rounded arms gives -25.8, illustrating why rounded-arm subtraction must not replace matched-count arithmetic. The registered defect is missing visible digits, not that rounding difference.
- **Necessary inputs available / exact missing inputs:** All counts, displayed arms and interval available. Missing: intended point-estimate visibility/dash convention for this cell.
- **Source-grounded alternative:** An intentionally omitted estimate or layout displacement; the interval and complete arms remain visible and no dash convention is supplied.
- **Direct observation versus inference:** Minus-only cell direct; count-derived -25.7 and explanation of displaced text inferred.
- **Exact remaining human question:** Is a numeric PPV contrast intended to be shown in this quantitative 17.0 cell, and what explains the visible minus-only display?
- **Classification confirmation:** REPORT eTable 5 versus REPORT eTable 4 within one document; primary/all S_W; numeric/arithmetic; statistical_results. No classification correction.
- **Evidence state and determining fact:** recorded_candidate; visible magnitude remains absent, and exact counts reproduce a nonmissing contrast. Pending Human Adjudication.

## C005 — Women's qualitative 10.2 PPV contrast

- **Location found:** Yes. [Results p. 7](../../../joi190039supp3_prod.pdf#page=7), eTable 5 Women Qualitative 10.2 Difference in PPV; comparator [p. 6](../../../joi190039supp3_prod.pdf#page=6), matched eTable 4 row.
- **Source value/text matched:** Yes. Visible aspirin PPV 9.7, placebo 31.2; point cell minus only; interval [-38.9, -3.9]. Displaced native fragment 21.6 exists outside the ordinarily visible magnitude location.
- **Comparator matched:** Yes. Per-protocol qualitative 10.2 aspirin TP 6, FP 56; placebo TP 10, FP 22.
- **Consistency rule applicable:** Yes for PPV raw-count reproduction and its point contrast. No arbitrary tie-rounding convention is imposed on displayed 31.2.
- **Calculation/logical comparison reproduced:** Yes. Aspirin 100 x 6/62 = 9.67741935; placebo 100 x 10/32 = 31.25; exact diagnostic difference -21.57258065 percentage points, rounding to -21.6. Rounded-arm subtraction gives -21.5, so it cannot govern the reconstructed contrast. The placebo 31.2 is at a rounding tie and is not independently registered as a contradiction.
- **Necessary inputs available / exact missing inputs:** Counts, arm values and interval available. Missing: intended visible contrast and dash/reporting convention; a tie-rounding rule is not needed for this candidate.
- **Source-grounded alternative:** Intentional omitted point estimate or displaced PDF text. Neither makes a magnitude visible in the source cell.
- **Direct observation versus inference:** Minus-only cell/interval direct; raw-count contrast and layout explanation inferred.
- **Exact remaining human question:** Should the qualitative 10.2 women's PPV cell display a numeric contrast with this interval, or does the dash have an intentional reporting meaning?
- **Classification confirmation:** Same results supplement REPORT comparison; primary/all S_W; numeric/arithmetic; statistical_results. No classification correction.
- **Evidence state and determining fact:** recorded_candidate; minus-only source cell remains confirmed with a finite count-derived contrast. Pending Human Adjudication.

## C006 — SAP lower-threshold mass-unit symbol

- **Location found:** Yes. [SAP p. 6](../../../joi190039supp2_prod.pdf#page=6), section 3.2 categorical FOBGold test-variable definition; contextual comparator [SAP p. 8](../../../joi190039supp2_prod.pdf#page=8), primary-analysis threshold statement.
- **Source value/text matched:** Yes. p. 6 visibly prints the paired expression 17 µg Hb/g feces and 10.2 Hb/g feces, with µg absent before 10.2. No OCR-loss explanation is needed.
- **Comparator matched:** Unit labels yes; exact same-test identity is not assumed. p. 8 prints 17 µg Hb/g feces and a 10.2 µg Hb/g feces FD Hb/Hp Complex quick-test threshold. The p. 8 lower threshold belongs to the qualitative test, whereas p. 6 calls 10.2 a lower threshold of the FOBGold categorical variable. This distinction corrects any suggestion that the two quoted 10.2 thresholds are necessarily the same test-specific endpoint.
- **Consistency rule applicable:** Yes to standalone mass-unit completeness within p. 6's paired concentration labels. It is not a numeric conversion or test-identity discrepancy.
- **Calculation/logical comparison reproduced:** Yes. The literal unit string differs: 17 includes µg; 10.2 omits it on p. 6. p. 8 shows the complete concentration label for 10.2 in its own test context. No arithmetic needed.
- **Necessary inputs available / exact missing inputs:** Visible unit expressions available. Missing: whether µg is intentionally inherited from the preceding threshold, and intended standalone lower-threshold notation. Same-test alignment is not a necessary input to the observed omission and is expressly not claimed.
- **Source-grounded alternative:** Shared/inherited µg in one parenthetical expression may be intentional editorial shorthand. This supports a bounded label question, not a changed cutoff value.
- **Direct observation versus inference:** Missing mass-unit symbol direct; omitted-versus-shared-symbol editorial intention inferred.
- **Exact remaining human question:** Should 10.2 in the primary-variable definition explicitly carry µg Hb/g feces, or is the symbol deliberately shared with the preceding threshold?
- **Classification confirmation:** Both locations are prospective SAP PLAN content; primary/all P_P; measure/label; plan_material. No role/type correction; comparator matching is narrowed as explained above.
- **Evidence state and determining fact:** recorded_candidate; the directly registered missing mass-unit symbol is present as an omission in the exact p. 6 source. The cross-page same-test assumption is removed without erasing that observed label question. Pending Human Adjudication.

## C007 — Trial-duration endpoints

- **Location found:** Yes. [Protocol p. 14](../../../joi190039supp1_prod.pdf#page=14), section 3.11 Study duration, introductory end definition and detailed duration schedule.
- **Source value/text matched:** Yes. Total trial duration 60 months; clinical phase 48 months; preparation Q1 2012 / January 2012; first subject in Q2 2013 / June 2013; last subject out Q2 2017 / June 2017; report completed Q1 2018 / March 2018. Study end is explicitly the date when the last patient completed the study.
- **Comparator matched:** Yes as adjacent duration and milestone fields in the same detailed schedule. The schedule does not expressly define the start milestone for the 60-month total; preparation is an inferred possible start, not an established denominator-equivalent endpoint.
- **Consistency rule applicable:** Conditional calendar-month difference only. The source supplies dates, but a definitive equality rule for total duration needs its start/end definition.
- **Calculation/logical comparison reproduced:** Yes conditionally. January 2012 to June 2017 = 12 x 5 + 5 = 65 months; January 2012 to March 2018 = 74; June 2013 to June 2017 = 48, which matches the clinical-phase field. Unspecified within-month days can move the 65-month estimate by less than about one month, not to 60. The total-duration basis is not established merely by selecting those milestones.
- **Necessary inputs available / exact missing inputs:** All printed dates and total available. Missing: start and end milestones expressly assigned to total trial duration and whether early preparation is excluded.
- **Source-grounded alternative:** Total could cover a different funded interval or exclude initial preparation; clinical phase and later reporting are separately identified. No invented June 2012 start is treated as source fact.
- **Direct observation versus inference:** Adjacent 60/48-month fields and milestone dates direct; choosing preparation-to-end as the total interval inferred.
- **Exact remaining human question:** Which start/end milestones define the 60-month total, and should that duration field or the dated schedule explicitly identify its basis?
- **Classification confirmation:** PLAN prospective duration schedule versus PLAN duration field; primary/all P_P; numeric/arithmetic; plan_material. No classification correction. Classification ambiguity concerns endpoint applicability, not content role.
- **Evidence state and determining fact:** recorded_candidate; the registered issue is explicitly the unspecified total-duration basis next to the dated detailed schedule, which remains after recheck. It is not represented as an unconditional proved 65-versus-60 duration contradiction. Pending Human Adjudication.

## C008 — Working-day/hour equivalence

- **Location found:** Yes. [Protocol p. 53](../../../joi190039supp1_prod.pdf#page=53), Appendix 1 second assessor's return deadline. The PDF page's printed footer is 52 of 61.
- **Source value/text matched:** Yes. Second assessment form is returned within the next 3 working days (72 hours). Nearby investigator alternatives distinguish 24 hours and next working day; nearby expedited deadlines explicitly use calendar days.
- **Comparator matched:** Yes. Working days and parenthetical 72 hours are directly attached in the same sentence, not taken from unrelated deadlines.
- **Consistency rule applicable:** Yes to unit equivalence, conditionally on the operational working calendar. Three continuously elapsed 24-hour days = 72 hours. The source does not define working days as continuous elapsed days.
- **Calculation/logical comparison reproduced:** Yes. 3 x 24 = 72 elapsed hours. If a nonworking interval intervenes, three working days need not end 72 elapsed hours later. The ledger's Monday-Friday example is only hypothetical and is not a package-defined working-week rule or an actual event; no external workday rule is imported.
- **Necessary inputs available / exact missing inputs:** Exact phrase and attached hours available. Missing: operational working-day calendar, treatment of nonworking days, and whether hours are elapsed or working hours.
- **Source-grounded alternative:** All intervening days may be working days, or the parenthesis could describe a typical continuous interval; this can reconcile a particular occasion but supplies no general calendar definition.
- **Direct observation versus inference:** Literal printed equivalence direct; an intervening nonworking-period counterexample conditional/inferred.
- **Exact remaining human question:** Does the parenthesis mean 72 elapsed hours or three working days, and which operational calendar governs the equivalence?
- **Classification confirmation:** PLAN operational phrase versus PLAN attached time expression; primary/all P_P; measure/label; plan_material. No classification correction.
- **Evidence state and determining fact:** recorded_candidate; the direct attached equivalence remains with its operational unit definition missing. Pending Human Adjudication.

## C009 — General and serum-specific tube volumes

- **Location found:** Yes. [Protocol p. 56](../../../joi190039supp1_prod.pdf#page=56), Appendix 2 Blood withdrawal opening paragraph and tube-specific list.
- **Source value/text matched:** Yes. Optional blood sampling uses four extra tubes 9-10 mL each, two EDTA and two serum. Serum-specific text gives 8.5-9 mL; one listed serum product is 8.5 mL. EDTA range is 9-10 mL.
- **Comparator matched:** Yes. The opening four-tube statement and serum options describe the same optional blood withdrawal, explicitly two tubes of each type.
- **Consistency rule applicable:** Yes to exact stated per-tube range versus specific allowed volume, subject to whether the general integer range is rounded/nominal.
- **Calculation/logical comparison reproduced:** Yes. 8.5 < 9. For the smallest listed options, 2 x 8.5 + 2 x 9 = 35 mL, versus the opening literal minimum 4 x 9 = 36 mL. This total is a diagnostic consequence, not a reported actual withdrawal volume.
- **Necessary inputs available / exact missing inputs:** Both ranges, product volume and tube counts available. Missing: explicit nominal-volume/rounding convention or serum exception to the opening summary.
- **Source-grounded alternative:** The integer 9 may be a rounded summary of 8.5; the protocol does not mark the general range approximate. Optionality changes whether blood is drawn, not the discrepancy between these stated per-tube labels.
- **Direct observation versus inference:** Ranges and 8.5 option direct; implied total and deliberate rounding explanation inferred.
- **Exact remaining human question:** Should the general per-tube range include 8.5 mL or explicitly identify rounding/a serum-tube exception?
- **Classification confirmation:** PLAN operational summary versus PLAN operational product list; primary/all P_P; measure/label; plan_material. No classification correction.
- **Evidence state and determining fact:** recorded_candidate; the specific allowed 8.5 mL volume remains below the literal general 9 mL minimum. Pending Human Adjudication.

## C010 — Pharmacovigilance subtotal and 1.704 separator

- **Location found:** Yes. [Protocol p. 60](../../../joi190039supp1_prod.pdf#page=60), budget category 6 and its six components; [p. 61](../../../joi190039supp1_prod.pdf#page=61), double-asterisk sum-of-components definition.
- **Source value/text matched:** Yes. Category 6 total 28,922 EUR. Components 884; 2,272; 15,600; 8,616; 1.704; 1,548 EUR. Enlarged direct p. 60 render confirms a dot, rather than silently reading a comma, in 1.704.
- **Comparator matched:** Yes. Those are the six nested components immediately under category 6. The preceding 2,886 continuation belongs to category 4 and is not included. The double-asterisk definition indicates sum of following component costs.
- **Consistency rule applicable:** Yes to component sum, but magnitude requires the explicit unresolved separator interpretation.
- **Calculation/logical comparison reproduced:** Yes. Sum excluding ambiguous item = 28,920. Thousands interpretation adds 1704 to give 30,624, exceeding 28,922 by 1702. Decimal interpretation adds 1.704 to give 28,921.704, which rounds to 28,922 at whole-euro precision. Consequently an unconditional statement that the subtotal arithmetic is wrong is not supported; the registered separator-dependent question is reproduced.
- **Necessary inputs available / exact missing inputs:** All printed components, subtotal and total definition available. Missing: applicable decimal/thousands separator and monetary fractional-precision convention for this item.
- **Source-grounded alternative:** Decimal 1.704 EUR exactly explains the rounded total, while a thousands separator gives a much larger amount. Other nearby thousands amounts use commas; the package has mixed monetary punctuation and does not declare a universal locale rule. No external national separator rule is imposed.
- **Direct observation versus inference:** Dot and values direct; interpretation of 1.704 as 1704 or 1.704 and cause of mismatch conditional.
- **Exact remaining human question:** Does 1.704 denote 1704 EUR or 1.704 EUR, and which subtotal and separator convention is intended for this component?
- **Classification confirmation:** PLAN financial components versus PLAN financial total/definition; primary/all P_P; numeric/arithmetic; plan_material. No classification correction.
- **Evidence state and determining fact:** recorded_candidate; the registered ambiguity is source-confirmed, with both arithmetic branches reproduced and one branch reconciling. This is not a disproven transcription, and not an unconditional budget-error claim. Pending Human Adjudication.

## C011 — Optional blood-supply procurement base

- **Location found:** Yes. [Protocol p. 60](../../../joi190039supp1_prod.pdf#page=60), category 12 supplies subitem linked to footnote 9; [p. 61](../../../joi190039supp1_prod.pdf#page=61), footnote 9; [p. 14](../../../joi190039supp1_prod.pdf#page=14), 2400 randomized/2000 analyzed targets. [p. 56](../../../joi190039supp1_prod.pdf#page=56) directly supplies optional-consent context.
- **Source value/text matched:** Yes. Supplies total 2388 EUR; two plasma tubes and two serum tubes per person; 100 plasma tubes cost 27.7 EUR; 100 serum tubes cost 26.6 EUR. Enlarged direct p. 61 render confirms serum 26.6, superseding the reused locator's 26.9. The current ledger already uses 26.6, so there is no ledger transcription repair.
- **Comparator matched:** Quantity and price yes; purchasing participant base no. The 2400 and 2000 numbers concern randomization and analysis, not an explicitly attached blood-purchase quantity. Footnote 9 supplies no N. p. 56 expressly requires consent to optional blood sampling and permits study participation without blood.
- **Consistency rule applicable:** Price x quantities is applicable only after a purchasing base is supplied. Treating randomization N as the tube-purchase N is unsupported by the source.
- **Calculation/logical comparison reproduced:** Conditional arithmetic yes, registered numeric mismatch no. At N=2400, 48 packs of each kind cost 48 x (27.7+26.6) = 2606.4 EUR, 218.4 above the table. At N=2000, cost = 2172 EUR. Per-person fractional-pack cost is 1.086 EUR; 2388/1.086 = 2198.895028 people. N=2200 gives 44 packs each and 2389.2 EUR, within the price-rounding uncertainty implied by one-decimal per-pack prices. None of these N values is the supplied purchase base. Whole-pack procurement, optional uptake, prior stocks or discounts are also unspecified.
- **Necessary inputs available / exact missing inputs:** Prices and per-person tube counts available. Missing: planned blood-consenting participants or tube-purchasing N, stock/discount assumptions, pack rounding and whether prices are nominal estimates.
- **Source-grounded alternative:** Optional consent can make purchased tubes fewer than 2400 participants' allocation. The table amount can be compatible with a roughly 2200-person estimate at stated price precision; this is illustrative, not a proposed source value.
- **Direct observation versus inference:** 2388, 27.7, 26.6 and optionality direct; selecting N=2400 or N=2000, implied N and procurement modifiers inferred.
- **Exact remaining human question:** What participant number, optional uptake estimate or procurement modifier was used for 2388 EUR, and should that base accompany the per-person tube-price footnote?
- **Classification confirmation:** PLAN financial total versus PLAN prospective quantities/prices and optional sampling; primary/all P_P; numeric/arithmetic; plan_material. No role/type correction. Applicability of the N alignment is corrected: randomization N is not an established purchasing denominator.
- **Evidence state and determining fact:** record_input_error. The mismatch calculation rests on an unsupported purchase-base alignment; the residual cannot be settled without the missing procurement basis. Correct reading does not establish an unconditional source arithmetic contradiction. Pending Human Adjudication.

## C012 — Insurance formula and budget amount

- **Location found:** Yes. [Protocol p. 61](../../../joi190039supp1_prod.pdf#page=61), category 15 insurance linked to footnote 15; [p. 62](../../../joi190039supp1_prod.pdf#page=62), footnote 15.
- **Source value/text matched:** Yes. Insurance 67,116 EUR; attached formula 23.50 EUR/person x 2400. Direct enlarged renders confirm rate and amount.
- **Comparator matched:** Yes. Explicit footnote 15 attaches the per-person formula to category 15, with the same planned 2400-person base. Unlike C011, the denominator is printed in this item's own formula.
- **Consistency rule applicable:** Yes to multiplication and agreement with the linked total; unprinted modifiers remain possible but are not substituted into the source.
- **Calculation/logical comparison reproduced:** Yes. 23.50 x 2400 = 56,400; 67,116 - 56,400 = 10,716 EUR. 67,116/56,400 = 1.19 exactly. Implied unit amount is 27.965 EUR/person. A half-cent rate-rounding uncertainty x 2400 is 12 EUR, far below the difference.
- **Necessary inputs available / exact missing inputs:** Rate, N and attached amount available. Missing: any addition, tax/overhead rule or rate convention accounting for exact 1.19. General tax and overhead fields are visibly blank, not zero, and are not a defined insurance modifier.
- **Source-grounded alternative:** An unprinted 19% addition mathematically reconciles the total. The factor is diagnostic evidence of a possible adjustment, not source evidence that a particular tax rule applies. No external tax convention is used.
- **Direct observation versus inference:** Formula and amount direct; 1.19 ratio derived and causal interpretation inferred.
- **Exact remaining human question:** Does 67,116 EUR include an unprinted 19% addition or another adjustment, and what modifier or unit rate belongs in the attached formula?
- **Classification confirmation:** PLAN financial table versus PLAN attached financial formula; primary/all P_P; numeric/arithmetic; plan_material. No classification correction.
- **Evidence state and determining fact:** recorded_candidate; explicit attached multiplication differs from its budget amount, with a named unprinted-modifier question remaining. Pending Human Adjudication.

## C013 — Overall budget from sixteen category totals

- **Location found:** Yes. [Protocol p. 59](../../../joi190039supp1_prod.pdf#page=59), categories 1-4; [p. 60](../../../joi190039supp1_prod.pdf#page=60), 5-12; [p. 61](../../../joi190039supp1_prod.pdf#page=61), 13-16 and overall study budget.
- **Source value/text matched:** Yes. Fresh direct pages confirm all sixteen top-level category amounts in stable order: 13383, 153000, 30950, 24790, 3000, 28922, 40642, 12731, 60000, 3400, 2430, 24881, 500, 6800, 67116, 35060 EUR; overall 505570 EUR.
- **Comparator matched:** Yes. All entries are visibly the sixteen numbered top-level categories of the same financial statement. Continuation components, including the first p. 60 and p. 61 rows, are not counted again. Printed category 6 total 28922 is used unchanged, independently of C010's component ambiguity.
- **Consistency rule applicable:** Yes to the overall sum of numbered category totals. The source gives no exception, credit or overlap definition.
- **Calculation/logical comparison reproduced:** Yes. Sum = 507605 EUR; sum minus overall 505570 = 2035 EUR. Sixteen half-euro rounding errors plus half a euro for the overall total allow only 8.5 EUR. No component reconstruction or assumed tax modifier enters this calculation.
- **Necessary inputs available / exact missing inputs:** Every category total and the overall total available. Missing: any exclusion, overlap, credit, revision or other adjustment defining a different inclusion rule.
- **Source-grounded alternative:** Budget-version or inclusion adjustment could explain the difference. Blank tax/overhead/funding cells do not supply a numeric adjustment, and no adjustment is printed at the overall row.
- **Direct observation versus inference:** All totals direct; sum/difference derived; cause of difference inferred.
- **Exact remaining human question:** Which inclusion rule or adjustment reconciles 505570 EUR with the 507605 EUR sum of the sixteen printed category totals?
- **Classification confirmation:** PLAN financial category totals versus PLAN overall financial amount; primary/all P_P; numeric/arithmetic; plan_material. No classification correction.
- **Evidence state and determining fact:** recorded_candidate; independent top-level addition reproduces the 2035-EUR difference. Pending Human Adjudication.

## C014 — Printing table/footnote amounts

- **Location found:** Yes. [Protocol p. 61](../../../joi190039supp1_prod.pdf#page=61), category 16 printing orders subitem linked to footnote 16; [p. 62](../../../joi190039supp1_prod.pdf#page=62), footnote 16.
- **Source value/text matched:** Yes. Table printing line 3000 EUR; footnote states printing for all study documents at 3500 EUR, with possible further color-printing costs. Footnote separately estimates flyers at 350-500 EUR and questionnaires at 1045 EUR, excluding value-added tax for that questionnaire amount.
- **Comparator matched:** Yes. The numbered footnote attachment is direct. Whether table and prose include exactly the same document/tax scope is not defined, so no extra assumption about tax inclusion is made.
- **Consistency rule applicable:** Yes to the matched attached amount comparison, conditional on any missing scope/version definition. Ancillary flyer/questionnaire estimates are not assumed exhaustive components of all documents.
- **Calculation/logical comparison reproduced:** Yes. 3500 - 3000 = 500 EUR. Rounding of two whole-euro amounts cannot explain it. Possible additional color costs do not turn the printed 3500 into 3000, but the footnote and line could represent different estimates or scopes.
- **Necessary inputs available / exact missing inputs:** Both amounts and footnote attachment available. Missing: intended document subset, tax inclusion and estimate/version identity if different.
- **Source-grounded alternative:** The table may be a narrower subset or earlier estimate; footnote contains tax qualifications for one component and possible further costs, rather than an explicit reconciliation.
- **Direct observation versus inference:** Attached differing amounts direct; differing scope, tax basis or revision explanation inferred.
- **Exact remaining human question:** Is the 3000-EUR printing line a different subset or estimate from the attached 3500-EUR all-documents footnote, and which scope/value should accompany each?
- **Classification confirmation:** PLAN financial table versus PLAN linked financial footnote; primary/all P_P; numeric/arithmetic; plan_material. No classification correction.
- **Evidence state and determining fact:** recorded_candidate; attached total estimates visibly differ by 500 EUR and no scope/version rule settles the difference. Pending Human Adjudication.

## C015 — Meeting cost-bundle attendance/frequency basis

- **Location found:** Yes. [Protocol p. 61](../../../joi190039supp1_prod.pdf#page=61), category 16 meeting/hotel subitem linked to footnote 18; [p. 62](../../../joi190039supp1_prod.pdf#page=62), footnote 18.
- **Source value/text matched:** Yes. Table amount 980 EUR. Footnote one meeting per year, four meetings total; hotel 80 EUR, travel 80 EUR for three people = 480 EUR; plus possible further 500 EUR.
- **Comparator matched:** Frequency, cost bundle and attachment yes. A per-meeting repetition of the 480-EUR bundle is not stated. The footnote labels one supplied bundle and an overall four-meeting schedule without defining repetition, attendance or allocation.
- **Consistency rule applicable:** Yes to the printed explicit bundle arithmetic; conditional only to multiplying that bundle by four. The latter is an unsupported alignment assumption, not a supplied rule.
- **Calculation/logical comparison reproduced:** Printed bundle reconciles: (80+80) x 3 = 480; 480+500 = 980, exactly the table amount. If all four meetings separately incurred the same 480 bundle and the further 500 applied once, total would be 4 x 480 + 500 = 2420, 1440 above the line. That is a hypothetical diagnostic, not an observed budget contradiction.
- **Necessary inputs available / exact missing inputs:** Printed frequency, bundle and total available. Missing: whether hotel/travel is per meeting or aggregate, which meetings have travel/hotel attendance, whether further 500 is once or per meeting, and allocation to other budget rows.
- **Source-grounded alternative:** The one bundle may be aggregate, travel may be needed for only one meeting, or other meetings may be local/otherwise allocated. The directly printed 480+500 already reconciles 980.
- **Direct observation versus inference:** Four-meeting phrase, bundle, 980 and exact reconciliation direct/derived; assuming identical attendance/costs at every meeting inferred.
- **Exact remaining human question:** Do the hotel/travel amounts for three people apply per meeting or across the four-meeting schedule, and what attendance/allocation rule was used for 980 EUR?
- **Classification confirmation:** PLAN prospective meeting budget versus PLAN attached operational cost description; primary/all P_P; numeric/arithmetic; plan_material. No role/type correction; per-meeting applicability is corrected to unestablished.
- **Evidence state and determining fact:** record_input_error; the proposed fourfold comparison rests on unsupported cost-frequency alignment, while explicit supplied bundle arithmetic reconciles. A residual question cannot be settled without its basis. not_reproduced is not assigned because the registered conditional frequency/allocation question is not explicitly disproven by a known per-meeting/aggregate definition. Pending Human Adjudication.

## C016 — Center versus practice payment component identity

- **Location found:** Yes. [Protocol p. 26](../../../joi190039supp1_prod.pdf#page=26), section 6.9 recruitment incentive; [p. 60](../../../joi190039supp1_prod.pdf#page=60), category 9 practice-related compensation; [p. 61](../../../joi190039supp1_prod.pdf#page=61), attached footnote 6.
- **Source value/text matched:** Yes. Section 6.9 study centers receive 75 EUR for each recruited patient, payable after receipt of colonoscopy/histology results or completion under the stated no-colonoscopy-within-three-months trigger. Category 9 table 60000 EUR; attached footnote 30 EUR for each completed case, 30 x 2000 EUR.
- **Comparator matched:** Amounts and footnote attachment yes; identical recipient/payment component no. The source uses study centers in the recruitment paragraph and practice-related compensation in the table. It does not explicitly state that 30 is the same full incentive as 75 rather than a distinct component or recipient. Recruited and completed case populations are also not established as identical payment bases.
- **Consistency rule applicable:** Yes to 30 x 2000; equality of the two unit rates requires component/recipient identity that is unavailable.
- **Calculation/logical comparison reproduced:** Budget formula reconciles exactly: 30 x 2000 = 60000. Numeric rate difference 75-30 = 45 EUR is direct arithmetic, but does not prove same-payment disagreement. Applying 75 to 2000 would give 150000, and to 2400 would give 180000; neither is a supplied category-9 payment denominator/rate combination.
- **Necessary inputs available / exact missing inputs:** Rates, payment triggers and 2000 denominator available. Missing: whether the study-center and practice rates refer to one full payment, a split component, different recipients, or distinct estimate versions; corresponding eligibility denominators.
- **Source-grounded alternative:** The 30-EUR item may be a component or separate practice reimbursement and 75 may be the full center incentive. Differences in recruitment/completion eligibility may also matter. The package provides no explicit bridging payment definition.
- **Direct observation versus inference:** Printed 75, 30, trigger and table formula direct; same-payment identity, multiplying the wrong rate/base and prior-version explanation inferred.
- **Exact remaining human question:** Is 30 EUR per completed case practice compensation the same payment as 75 EUR per recruited patient study-center incentive, or a distinct component/recipient, and how should those payment definitions be distinguished?
- **Classification confirmation:** PLAN recruitment incentive versus PLAN financial table/formula; primary/all P_P; numeric/arithmetic; plan_material. No role/type correction; same-payment alignment is corrected to unestablished.
- **Evidence state and determining fact:** record_input_error; identical recipient/component alignment is not supplied and the actual category-9 formula reconciles, so whether a residual discrepancy exists cannot be settled. Pending Human Adjudication.

## Handoff and bounded limitations

Covered exactly sixteen IDs: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016. Thirteen registered conditional/direct comparisons remain recorded_candidate; three unsupported alignment comparisons are record_input_error. No assigned ID was deleted, merged, renumbered, or scientifically adjudicated. No transcription repair changes the current ledger's source numbers; the fresh serum 26.6 confirms the ledger against an older 26.9 locator. Exact PPV diagnostics and the p. 8 SAP test-context limitation are supplied for later lanes.

Remaining limitations are the named source definitions in the individual cards. They concern intended visible labels/layout, total-duration endpoints, working-calendar semantics, nominal volumes, component monetary separator, optional procurement base, insurance modifier, overall-budget inclusion, printing scope, meeting-cost repetition, and payment component identity. The supplied package cannot settle these; they remain bounded human questions rather than inferred production causes or conclusions about the trial.
