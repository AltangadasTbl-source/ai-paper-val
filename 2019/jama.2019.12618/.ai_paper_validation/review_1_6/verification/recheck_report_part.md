# Workflow 1.6 Mechanical Evidence Recheck — REPORT Part

Assigned scope: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018, C019, C020. Every ID remains Pending Human Adjudication. Evidence states below record source facts, not adjudications. Other stable IDs are assigned to separate recheck agents and are outside this part.

The main article and Supplement 1 are REPORT by content: they present observed trial results, result definitions and result tables. A definition table embedded in the results supplement is not a prospective plan merely because it defines a measurement. All compared locations were checked against supplied PDFs through new direct Poppler layout extraction and source-linked page images. Existing current-run extracts located pages; they did not determine the readings. No legacy review was read.

## Direct-source tooling and derivative record

Recorded direct tools were available. Engine: Poppler 26.01.0, CPU only. New derivatives are confined to `review_1_6/preprocessing/`:

- `pdftotext -layout -f 1 -l 8 jama_rathinam_2019_oi_190092.pdf .ai_paper_validation/review_1_6/preprocessing/recheck_report_main_p1_p8_layout.txt`.
- `pdftotext -layout -f 5 -l 15 joi190092supp1_prod.pdf .ai_paper_validation/review_1_6/preprocessing/recheck_report_supp1_p5_p15_layout.txt`.
- `pdftoppm -f 3 -l 4 -r 100 -png jama_rathinam_2019_oi_190092.pdf .ai_paper_validation/review_1_6/preprocessing/recheck_report_main`: outputs `recheck_report_main-03.png` and `recheck_report_main-04.png`.
- `pdftoppm -f 7 -l 7 -r 100 -singlefile -png jama_rathinam_2019_oi_190092.pdf .ai_paper_validation/review_1_6/preprocessing/recheck_report_main_p7`: output `recheck_report_main_p7.png`.
- `pdftoppm -f 5 -l 7 -r 100 -png joi190092supp1_prod.pdf .ai_paper_validation/review_1_6/preprocessing/recheck_report_supp1`: outputs `recheck_report_supp1-05.png`, `recheck_report_supp1-06.png`, `recheck_report_supp1-07.png`.

Visually inspected source-linked current-run images: `numeric_main_p005.png`, `main_p006.png`, `numeric_main_p008.png`, `numeric_results_p10.png`, `numeric_results_p14.png`, `numeric_results_p15.png`; also all six new render outputs listed above. Main page 6 superscript attachments were inspected visually, individually, for C007–C013. Arithmetic was independently reproduced using direct JavaScript arithmetic, not Python scientific orchestration. No extraction/OCR disagreement affects the C001–C020 source readings. Separately, visual inspection of Supplement 1 page 5 showed a hemoglobin underline absent from native text; that fact was sent to the coordinator for the distinct C043 scope.

## C001 — Baseline mycophenolate macular-edema percentage

- **Location found:** Yes; [main PDF page 5, Table 1 eye-level header and macular-edema row](../../../jama_rathinam_2019_oi_190092.pdf#page=5), directly extracted and visually inspected.
- **Source value/text matched:** Yes: mycophenolate macular edema is `55 (27.3)`.
- **Comparator matched:** Yes: the eye-level header is `n = 201 eyes`; footnote a defines otherwise-unmarked entries as No. (%). Footnote e states the macular-edema exclusion; it does not print a different row denominator or rounding rule.
- **Consistency rule applicable:** A percentage from the printed integer count and denominator should reconcile under ordinary nearest one-decimal rounding; tolerance is 0.05 percentage point. The diagnostic is conditional on that rounding convention.
- **Calculation reproduced:** `100 × 55 / 201 = 27.363184%`, which rounds to 27.4%, outside the 27.3% display interval [27.25%, 27.35%). A denominator below 201 after exclusions would increase the percentage and cannot explain 27.3% by nearest rounding.
- **Necessary inputs available:** Count, header denominator and precision are available. **Exact missing inputs or definitions:** The implemented rounding convention and any row-specific population definition are not explicitly supplied.
- **Source-grounded alternative interpretation:** Truncation would yield 27.3%. A different eligible-eye population is mentioned through footnote e, but no smaller eligible denominator can explain this particular lower displayed percentage under nearest rounding.
- **Direct observation versus inferred explanation:** The printed 55, 27.3 and 201 are direct observations; the mismatch under nearest rounding is reproduced. Truncation or a production mechanism is an inference, not established fact.
- **Exact remaining human question:** What denominator and rounding convention produced `55 (27.3)` in this row?
- **Classification:** Primary category `Denominator, proportion, or total inconsistency`; compared roles REPORT main Table 1 row versus REPORT same-table header/footnotes; relationship `S_W`; all relationships `S_W`. Confirmed without correction; no plan comparator is involved.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** The visually confirmed numerator, header denominator and one-decimal percentage fail the stated nearest-rounding rule; the missing convention is named.
- **Status:** Pending Human Adjudication.

## C002 — Methotrexate nonserious liver percentage

- **Location found:** Yes; [main PDF page 8, Table 3 liver and allergic-reaction rows](../../../jama_rathinam_2019_oi_190092.pdf#page=8), with repeated liver values in [page 1 abstract](../../../jama_rathinam_2019_oi_190092.pdf#page=1) and [page 7 Adverse Events](../../../jama_rathinam_2019_oi_190092.pdf#page=7).
- **Source value/text matched:** Yes: methotrexate elevated ALT/AST is `14 (13.0)`; abstract and narrative repeat 14 and 13.0%.
- **Comparator matched:** Yes: methotrexate header `n = 107`; the same Table 3 allergic-reaction row is `14 (13.1)`.
- **Consistency rule applicable:** Identical numerators under the same printed patient denominator and percentage convention should produce identical displayed percentages; ordinary one-decimal rounding has 0.05-point tolerance.
- **Calculation reproduced:** `100 × 14 / 107 = 13.084112%`, nearest one decimal 13.1%, not 13.0%. The other `14 (13.1)` row supplies a directly printed within-table comparator.
- **Necessary inputs available:** All printed numerator/denominator/precision inputs are available. **Exact missing inputs or definitions:** Any row-specific liver denominator or differing rounding rule is unstated.
- **Source-grounded alternative interpretation:** A truncated liver percentage or an unstated population restriction might explain 13.0%; neither explains the differing convention between identically counted rows without additional information.
- **Direct observation versus inferred explanation:** The two different percentages attached to 14 are observed; their common-denominator arithmetic is reproduced. Copying, truncation and row-specific eligibility are possible explanations only.
- **Exact remaining human question:** Why do the liver and allergic-reaction rows display different percentages for 14 methotrexate patients, and was a different liver denominator or rounding rule used?
- **Classification:** `Denominator, proportion, or total inconsistency`; REPORT main table/narrative/abstract versus REPORT same main-table header and row; `S_W`; all `S_W`. Confirmed.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** Direct-source readings preserve the same-numerator percentage difference and the nearest-rounding discrepancy.
- **Status:** Pending Human Adjudication.

## C003 — Number eligible to switch treatment

- **Location found:** Yes; [main PDF page 7, Prespecified 12-Month Outcomes](../../../jama_rathinam_2019_oi_190092.pdf#page=7), [page 6 Table 2](../../../jama_rathinam_2019_oi_190092.pdf#page=6), and [page 3 Figure 1](../../../jama_rathinam_2019_oi_190092.pdf#page=3), including direct visual checks.
- **Source value/text matched:** Yes: page 7 says `Forty-nine of the 68 eligible patients` with failure in the first six months and without a serious laboratory event switched.
- **Comparator matched:** Yes: Table 2 failure counts are 32 and 42, with safety failures 3 and 2. Figure 1 lists safety ineligibility 3 and 2, unwillingness to switch 9 and 11, and switchers 20 and 29.
- **Consistency rule applicable:** If eligibility is defined by analyzed treatment failure less the displayed safety exclusions, its exact integer total should reconcile. This rule is conditional because eligibility may include an additional criterion.
- **Calculation reproduced:** `32 + 42 = 74`; `74 − (3 + 2) = 69`, compared with 68. Independently, `20 + 29 + 9 + 11 = 69` switchers plus those unwilling to switch.
- **Necessary inputs available:** All displayed aggregate counts are available. **Exact missing inputs or definitions:** Patient-level membership in the 68 and all switch-eligibility exclusions are not supplied.
- **Source-grounded alternative interpretation:** Figure 1 also discloses one mycophenolate patient who never received medication because of a postrandomization contraindication. That could explain an additional exclusion only if the patient belonged to the analyzed failures and was omitted from switch eligibility; the package does not establish that linkage. Other eligibility exclusions are likewise possible. The death appears in pre-six-month loss and cannot simply be subtracted again from analyzed failures.
- **Direct observation versus inferred explanation:** The 68, 74 and five safety exclusions are printed facts. Treating the five exclusions as exhaustive or attributing the difference to the untreated patient is inference.
- **Exact remaining human question:** Which extra patient or eligibility criterion, if any, reduces the displayed 69 failures without safety exclusions to 68 eligible switchers?
- **Classification:** `Denominator, proportion, or total inconsistency`; REPORT main narrative versus REPORT main table and figure; `S_W`; all `S_W`. Confirmed; the untreated-patient explanation is corroborating context rather than a new relationship.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** The exact-count discrepancy reproduces under the registered eligibility rule, with its exhaustive-eligibility assumption explicitly unresolved.
- **Status:** Pending Human Adjudication.

## C004 — Lost-to-follow-up label and missed-visit total

- **Location found:** Yes; [main PDF page 4, Results](../../../jama_rathinam_2019_oi_190092.pdf#page=4), [page 3 Figure 1](../../../jama_rathinam_2019_oi_190092.pdf#page=3), and [page 7 missing-primary-outcome narrative](../../../jama_rathinam_2019_oi_190092.pdf#page=7), visually inspected and directly extracted.
- **Source value/text matched:** Yes: page 4 calls `22 patients (10.2%)` lost to follow-up.
- **Comparator matched:** Yes: Figure 1 separately labels 9 and 10 lost before the six-month visit, and 2 and 1 who missed that visit; page 7 says 22 of 216 missed the primary outcome visit.
- **Consistency rule applicable:** A labeled total should identify the population represented by its constituent categories. Exact counts have no rounding tolerance; the percentage itself is coherent.
- **Calculation reproduced:** Lost categories total `9 + 10 = 19`; missed-visit categories total `2 + 1 = 3`; all missing primary outcomes total `19 + 3 = 22`. Also `100 × 22 / 216 = 10.185185%`, which rounds to 10.2%.
- **Necessary inputs available:** Category counts and narrative totals are available. **Exact missing inputs or definitions:** Whether “lost to follow-up” is intentionally used as an umbrella for all absent primary visits is not defined.
- **Source-grounded alternative interpretation:** The Results sentence may use the broader term informally, while Figure 1 distinguishes temporary missed visits from losses. The 22 is numerically consistent with total missingness under that broader interpretation.
- **Direct observation versus inferred explanation:** The category names and counts differ directly; this is a population-label question, not an arithmetic error in the 22/216 percentage.
- **Exact remaining human question:** Does the page 4 “lost to follow-up” population deliberately include the three separately labeled missed six-month visits?
- **Classification:** `Denominator, proportion, or total inconsistency`; REPORT main Results versus REPORT main Figure 1 and missingness narrative; `S_W`; all `S_W`. Confirmed, because the concrete issue is the composition of the reported total.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** The 22-label comparison remains as registered pending the named umbrella-population definition.
- **Status:** Pending Human Adjudication.

## C005 — Majority wording with a displayed 50.0%

- **Location found:** Yes; [main PDF page 7, Prespecified 12-Month Outcomes](../../../jama_rathinam_2019_oi_190092.pdf#page=7), directly extracted and visually inspected.
- **Source value/text matched:** Yes: “with the majority (50.0% for methotrexate and 55.0% for mycophenolate mofetil) discontinuing prednisone.”
- **Comparator matched:** Yes: the explicit methotrexate percentage is 50.0%, and the preceding sentence gives successes 48/60 and 40/54. The ledger's auxiliary reference to eligible sizes “60/48” is not the printed two-group continuation denominator: the actual denominator pair is 60/54; the actual success-count pair is 48/40.
- **Consistency rule applicable:** A strict majority of an individual group is greater than half. Applicability to each separate treatment group is conditional because the sentence can refer to the pooled group.
- **Calculation reproduced:** Exactly 50% is half, not a strict majority. A printed 50.0% alone allows an underlying value within about 0.05 percentage point of half; it does not prove a strict excess. As a diagnostic only, if the percentages use the 48 and 40 successful patients, 24/48 = 50% and 22/40 = 55%, while pooled 46/88 = 52.2727% would be a majority. These inferred numerators are not supplied results.
- **Necessary inputs available:** Wording, percentages, continuation denominators and success counts are available. **Exact missing inputs or definitions:** Prednisone-discontinuation numerators, denominators and whether “majority” is pooled or group-specific are absent.
- **Source-grounded alternative interpretation:** A pooled majority is compatible with the displayed group percentages. The proximity to the successful-patient sentence supports, but does not establish, a success-only population.
- **Direct observation versus inferred explanation:** The wording/50.0% tension is observed; exact discontinuation counts and a pooled majority are inferred possibilities. The incorrect auxiliary ledger denominator is corrected here without changing the primary registered wording question.
- **Exact remaining human question:** Does “majority” refer to pooled patients or each treatment group, and what discontinuation population underlies 50.0% and 55.0%?
- **Classification:** `Numeric or arithmetic inconsistency`; REPORT main wording versus REPORT same-sentence proportions; `S_W`; all `S_W`. Confirmed; the auxiliary denominator correction does not change the comparison's roles or type.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** The registered conditional wording comparison is reproduced, while the exact target of “majority” remains unspecified; no claim of a proven pooled-group contradiction is made.
- **Status:** Pending Human Adjudication.

## C006 — Serious versus serous retinal-detachment exclusion

- **Location found:** Yes; [main PDF page 5 Table 1 footnote e](../../../jama_rathinam_2019_oi_190092.pdf#page=5) and [page 6 Table 2 footnote m](../../../jama_rathinam_2019_oi_190092.pdf#page=6), both visually inspected.
- **Source value/text matched:** Yes: Table 1 says macular edema excludes Vogt-Koyanagi-Harada patients with a “serious retinal detachment”; its edema counts are 42 and 55.
- **Comparator matched:** Yes: Table 2 says eyes with macular edema exclude those with a “serous retinal detachment” in that setting, and its thickness row shows [42] and [55].
- **Consistency rule applicable:** Definitions of the quantitative eye population should agree if these linked edema/thickness summaries use the same exclusion. “Serious” and “serous” are different printed descriptors; no arithmetic tolerance applies to that label comparison.
- **Calculation reproduced:** The word comparison and repeated count pair 42/55 reproduce. Count equality alone cannot establish identical eye membership.
- **Necessary inputs available:** Both exclusion statements and displayed count pairs are available. **Exact missing inputs or definitions:** Eye-level membership and whether seriousness or serous morphology was the actual inclusion criterion are absent.
- **Source-grounded alternative interpretation:** A typographic substitution could explain the wording. Different populations could also produce the same aggregate counts; their identity is not proven.
- **Direct observation versus inferred explanation:** The adjective mismatch is directly visible. A typo, a changed exclusion, and any resulting participant reclassification are inferred possibilities.
- **Exact remaining human question:** Do both quantitative summaries use the same serous-detachment exclusion, or do their populations differ as the two adjectives imply?
- **Classification:** `Analysis-unit or population inconsistency`; REPORT main Table 1 definition/counts versus REPORT main Table 2 definition/counts; `S_W`; all `S_W`. Confirmed as a concrete quantitative-population-label question, not a general design criticism.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** The directly visible different exclusions attach to the linked 42/55 quantitative populations, with actual membership explicitly unknown.
- **Status:** Pending Human Adjudication.

## C007 — Efficacy-failure superscript c

- **Location found:** Yes; [main PDF page 6 Table 2 efficacy row and footnotes c/d](../../../jama_rathinam_2019_oi_190092.pdf#page=6). Superscript c was visually inspected in `main_p006.png`.
- **Source value/text matched:** Yes: Efficacy carries c and displays 26/32 (81) and 38/42 (90).
- **Comparator matched:** Yes: footnote c defines treatment success; footnote d explicitly defines failure due to efficacy.
- **Consistency rule applicable:** A printed superscript's literal lookup should attach the appropriate definition to its labeled outcome. Exact marker identity applies, with no numeric tolerance.
- **Calculation reproduced:** Row marker c maps to the success definition, although the row is under reasons for treatment failure; the separate efficacy-failure definition is d. The mismatch is the reference attachment, not a claim that 26 or 38 is wrong.
- **Necessary inputs available:** Marker, row label, counts, and both definitions are available. **Exact missing inputs or definitions:** The intended editorial attachment is not supplied.
- **Source-grounded alternative interpretation:** A systematic production offset may explain the markers. Success could be referenced as a conceptual complement, but the attached definition does not itself state efficacy failure and a dedicated failure definition exists beside it.
- **Direct observation versus inferred explanation:** The c/c lookup is direct; production offset and authorial intent are inferred.
- **Exact remaining human question:** Which definition was intended to accompany efficacy failures 26/32 and 38/42?
- **Classification:** `Measure, label, or scale inconsistency`; REPORT main row versus REPORT main footnotes; `S_W`; all `S_W`. Confirmed.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** Visual confirmation preserves the registered c-to-success attachment.
- **Status:** Pending Human Adjudication.

## C008 — Intolerability superscript d

- **Location found:** Yes; [main PDF page 6 Table 2 intolerability row and footnotes d/e](../../../jama_rathinam_2019_oi_190092.pdf#page=6); row superscript visually inspected.
- **Source value/text matched:** Yes: Intolerability carries d; counts are 3/32 (9) and 2/42 (5).
- **Comparator matched:** Yes: footnote d defines efficacy failure by failure to achieve treatment success or persistent worsening inflammation; e defines inability or unwillingness to continue due to adverse effects.
- **Consistency rule applicable:** Literal superscript lookup should identify the row's labeled failure definition; exact marker comparison has no tolerance.
- **Calculation reproduced:** d leads to efficacy failure rather than the stated intolerability category. The counts remain read in their printed row and are not reassigned.
- **Necessary inputs available:** All marker/category/definition inputs are available. **Exact missing inputs or definitions:** Intended footnote attachment is unstated.
- **Source-grounded alternative interpretation:** A production offset is plausible; it is not evidence about the actual reasons for individual failures.
- **Direct observation versus inferred explanation:** Attached d and its efficacy definition are observed; the mechanism causing the attachment is inferred.
- **Exact remaining human question:** Which definition should identify the intolerability counts 3/32 and 2/42?
- **Classification:** `Measure, label, or scale inconsistency`; REPORT main row versus REPORT main footnotes; `S_W`; all `S_W`. Confirmed.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** The exact visually observed d lookup reproduces the registered label-definition mismatch.
- **Status:** Pending Human Adjudication.

## C009 — Safety superscript e

- **Location found:** Yes; [main PDF page 6 Table 2 safety row and footnotes e/f](../../../jama_rathinam_2019_oi_190092.pdf#page=6), including visual superscript confirmation.
- **Source value/text matched:** Yes: Safety carries e; counts are 3/32 (9) and 2/42 (5).
- **Comparator matched:** Yes: e defines intolerability; f defines an abnormal laboratory result meeting the serious-adverse-event threshold as safety failure.
- **Consistency rule applicable:** Literal marker lookup should attach the labeled safety criterion, rather than another reason for treatment failure. No tolerance applies to marker identity.
- **Calculation reproduced:** e attaches the adverse-effect inability/unwillingness definition to Safety. Equal numerical counts in the intolerability row do not equate the definitions.
- **Necessary inputs available:** Marker, row label and both definitions are available. **Exact missing inputs or definitions:** The intended printed attachment is not stated elsewhere as a correction.
- **Source-grounded alternative interpretation:** A production offset may explain the mismatched marker; no reassignment of patients or counts follows.
- **Direct observation versus inferred explanation:** The e/e attachment is directly visible; production mechanism is inferred.
- **Exact remaining human question:** Which definition should accompany the safety-failure counts 3/32 and 2/42?
- **Classification:** `Measure, label, or scale inconsistency`; REPORT main row versus REPORT main footnotes; `S_W`; all `S_W`. Confirmed.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** The attached e leads to the directly printed intolerability definition, reproducing the registered comparison.
- **Status:** Pending Human Adjudication.

## C010 — Anatomical-subgroup P-value superscripts f

- **Location found:** Yes; [main PDF page 6 Table 2 anatomical-subgroup P values and footnotes f/g](../../../jama_rathinam_2019_oi_190092.pdf#page=6), with both small f markers visually inspected.
- **Source value/text matched:** Yes: intermediate-subgroup P .07 and posterior/panuveitis P .02 each carry f.
- **Comparator matched:** Yes: footnote f describes laboratory safety failure; g gives the anatomical-subtype/treatment interaction P = .004.
- **Consistency rule applicable:** A note attached to a subgroup inferential result should describe a relevant result or definition. Exact marker lookup applies; this is not a recalculation of the subgroup P values.
- **Calculation reproduced:** Both f markers lead to a failure-definition footnote unrelated to the attached P values; the printed interaction note is g.
- **Necessary inputs available:** Both P values, both markers and footnotes are available. **Exact missing inputs or definitions:** The intended notes for these P values are not established by an editorial correction.
- **Source-grounded alternative interpretation:** A marker offset is plausible; the P values may themselves be correct. Neither P .07 nor .02 is treated as the interaction P .004.
- **Direct observation versus inferred explanation:** The identical f lookups and different note content are direct observations; editorial offset is an inference.
- **Exact remaining human question:** Which note was intended for subgroup P .07 and .02, and how should their markers identify the separate interaction result?
- **Classification:** `Measure, label, or scale inconsistency`; REPORT main subgroup cells versus REPORT main footnotes; `S_W`; all `S_W`. Confirmed.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** Visual source confirmation reproduces both registered f attachments.
- **Status:** Pending Human Adjudication.

## C011 — Continuation superscript g

- **Location found:** Yes; [main PDF page 6 Table 2 continuation row and footnotes g/h](../../../jama_rathinam_2019_oi_190092.pdf#page=6), visually inspected.
- **Source value/text matched:** Yes: Continued on randomized antimetabolite carries g and shows 48/60 (80) and 40/54 (74).
- **Comparator matched:** Yes: g gives the anatomical interaction P = .004; h identifies the 60 originally methotrexate and 54 originally mycophenolate patients continuing the same antimetabolite.
- **Consistency rule applicable:** A reference on this row should supply a relevant definition of its continuation population; exact marker lookup applies.
- **Calculation reproduced:** g points to the anatomical-interaction note rather than the continuation-population note. The 60/54 denominator identification exists as h on the same page.
- **Necessary inputs available:** Row marker, counts and both footnotes are available. **Exact missing inputs or definitions:** Intended attachment is not explicitly amended.
- **Source-grounded alternative interpretation:** The interaction footnote could theoretically be an additional reference, but its relevance to continuation is unstated. A production offset is supported as a pattern, not proven as a mechanism.
- **Direct observation versus inferred explanation:** The g lookup and denominator note h are printed facts; the explanation for that linkage is inferred.
- **Exact remaining human question:** Which footnote should define the continuation row's 60/54 population?
- **Classification:** `Measure, label, or scale inconsistency`; REPORT main row versus REPORT main footnotes; `S_W`; all `S_W`. Confirmed.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** The exact g attachment reproduces the registered continuation/interaction-note mismatch.
- **Status:** Pending Human Adjudication.

## C012 — Switching superscript h

- **Location found:** Yes; [main PDF page 6 Table 2 switching row and footnotes h/i](../../../jama_rathinam_2019_oi_190092.pdf#page=6), visually inspected; [page 7 switching narrative](../../../jama_rathinam_2019_oi_190092.pdf#page=7) independently matches the received-drug contrast.
- **Source value/text matched:** Yes: Switched to other antimetabolite carries h; cells are 20/29 (69) and 7/20 (35).
- **Comparator matched:** Yes: h describes continuers 60/54; i identifies 29 originally mycophenolate patients switching to methotrexate and 20 originally methotrexate patients switching to mycophenolate.
- **Consistency rule applicable:** The marker should identify the row's actual treatment/population contrast. This matters because received medication reverses original assignment in the switchers.
- **Calculation reproduced:** h maps to continuing randomized treatment, not the 29/20 switched-drug populations. The separate i footnote and page 7 prose explain the switching contrast; counts remain assigned to the printed received-drug columns.
- **Necessary inputs available:** Markers, counts, continuation and switching definitions are available. **Exact missing inputs or definitions:** Intended superscript attachment is not corrected in the source.
- **Source-grounded alternative interpretation:** A production offset plausibly accounts for this. No inference that the switch-success numerators are themselves erroneous is warranted.
- **Direct observation versus inferred explanation:** The h/h lookup contradicts the switching-population label directly; the editorial cause is inferred.
- **Exact remaining human question:** Which footnote was intended to identify treatment assignment and the 29/20 denominators for switched patients?
- **Classification:** `Measure, label, or scale inconsistency`; REPORT main row versus REPORT main footnotes/narrative; `S_W`; all `S_W`. Confirmed.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** Visual confirmation preserves the registered h-to-continuation linkage.
- **Status:** Pending Human Adjudication.

## C013 — Missed-dose superscript i

- **Location found:** Yes; [main PDF page 6 Table 2 missed-dose row and footnotes i/j](../../../jama_rathinam_2019_oi_190092.pdf#page=6), with direct visual inspection of i.
- **Source value/text matched:** Yes: Missed doses, mean (SD), % carries i; cells are 4.6 (1.0) and 4.3 (0.5), P .87.
- **Comparator matched:** Yes: i describes switchers 29/20; j defines missed doses over total expected doses throughout the patient's trial enrollment. The page 6 prose discusses weekly methotrexate and daily mycophenolate missed-dose proportions.
- **Consistency rule applicable:** A marker on a dose-ratio summary should identify its relevant ratio/population definition; marker lookup is exact. The registered candidate does not test the P value.
- **Calculation reproduced:** i maps to the switching population rather than the missed/expected-dose definition supplied by j. No dose numerator can be reconstructed from the means alone.
- **Necessary inputs available:** Printed marker, mean/SD summaries and both footnotes are available. **Exact missing inputs or definitions:** Intended attachment and detailed adherence-analysis population are not explicitly supplied.
- **Source-grounded alternative interpretation:** The i reference could imply a switcher-specific adherence subset, but the prose does not state that restriction and the dose-ratio definition remains unattached. A production offset is possible.
- **Direct observation versus inferred explanation:** The i lookup and the separate ratio definition are direct observations; a population restriction or offset is inferred.
- **Exact remaining human question:** What adherence population and definition apply to 4.6%/4.3%, and which note was intended to accompany that row?
- **Classification:** `Measure, label, or scale inconsistency`; REPORT main dose row versus REPORT main footnotes/prose; `S_W`; all `S_W`. Confirmed.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** The visually confirmed i marker points to the registered switching comparator rather than the dose-ratio definition.
- **Status:** Pending Human Adjudication.

## C014 — Randomized header and exposed safety denominator

- **Location found:** Yes; [main PDF page 8 Table 3 header/footnote b](../../../jama_rathinam_2019_oi_190092.pdf#page=8), [main page 3 Figure 1](../../../jama_rathinam_2019_oi_190092.pdf#page=3), and REPORT [Supplement 1 page 10 eTable 4](../../../joi190092supp1_prod.pdf#page=10), [page 11 eTable 5](../../../joi190092supp1_prod.pdf#page=11), [page 12 eTable 6](../../../joi190092supp1_prod.pdf#page=12). Main pages 3/8 and eTable 4 were visually inspected; all locations were checked with fresh direct layout extraction.
- **Source value/text matched:** Yes: Table 3 mycophenolate header is n = 109, explicitly marked b; footnote b says one patient never received the drug due to a postrandomization contraindication.
- **Comparator matched:** Yes: Figure 1 states 109 randomized and 108 received allocated intervention. The results supplement explicitly uses N = 108 and states 108 received medication. Table 3 examples remain fatigue 59 (54.6), headache 45 (41.7), ocular hypertension 13 (12.0), other systemic 63 (58.3).
- **Consistency rule applicable:** Safety proportions must use the relevant exposed population. Reading the header together with its attached exclusion footnote identifies 109 randomized minus one untreated, or 108 exposed; treating the header alone as an exhaustive safety denominator is not applicable to the complete source statement.
- **Calculation reproduced:** `109 − 1 = 108`. On 108, the four examples are 54.629630%, 41.666667%, 12.037037%, and 58.333333%, rounding to every printed percentage. On 109 they would instead be 54.1%, 41.3%, 11.9%, and 57.8%; that diagnostic merely shows why the footnote matters.
- **Necessary inputs available:** Both randomized and exposed counts, exclusion explanation and displayed safety numerators are available. **Exact missing inputs or definitions:** None is required to reconcile the registered safety-percentage arithmetic. Whether authors wish to label the header “randomized” explicitly is an editorial question, not a remaining demonstrated arithmetic contradiction.
- **Source-grounded alternative interpretation:** The table header reports randomized allocation size while its directly attached footnote removes the unexposed patient for safety percentages. The supplement and Figure 1 explicitly corroborate this interpretation.
- **Direct observation versus inferred explanation:** All population counts and the exclusion footnote are direct observations; subtraction and proportions reproduce reconciliation. A hidden denominator or unexplained population change need not be inferred.
- **Exact remaining human question:** Should Table 3 explicitly distinguish its randomized header n = 109 from the exposed percentage denominator 108 for easier extraction? No unresolved arithmetic question remains for the registered comparison.
- **Classification:** `Denominator, proportion, or total inconsistency`; registered compared roles REPORT main table/header/figure versus REPORT results-supplement safety headers; relationship `S_C`; all `S_C, S_W`. Retained as the historical comparison's classification, with the fact that the complete source now reconciles it. No `P_R` is introduced: the cited SAP safety-population statement merely corroborates the exposed interpretation and is not a separate discrepancy comparator.
- **Evidence state:** `not_reproduced`. **Determining recheck fact:** The exact footnote and explicit Figure 1 exposed count supply 108 and reproduce the printed percentages, disproving the registered assumption that all percentages must use the standalone 109 header.
- **Status:** Pending Human Adjudication.

## C015 — Mycophenolate eye-floaters percentage

- **Location found:** Yes; REPORT [Supplement 1 page 10 eTable 4 eye-floaters row/header/footnote](../../../joi190092supp1_prod.pdf#page=10), directly extracted and visually inspected.
- **Source value/text matched:** Yes: the mycophenolate eye-floaters cell is 5 (4.7).
- **Comparator matched:** Yes: mycophenolate N = 108 and footnote confirms 108 received medication; methotrexate N = 107 also has 5 (4.7).
- **Consistency rule applicable:** A patient percentage should equal count divided by that column's exposed denominator under ordinary nearest one-decimal rounding, allowing 0.05 percentage point.
- **Calculation reproduced:** `100 × 5 / 108 = 4.629630%`, which rounds to 4.6%; its distance from printed 4.7 is 0.070370 point. `100 × 5 / 107 = 4.672897%` rounds to 4.7% for the other column.
- **Necessary inputs available:** Count, explicit exposed denominator and precision are available. **Exact missing inputs or definitions:** Any eye-floaters-specific denominator or exceptional rounding rule is unstated.
- **Source-grounded alternative interpretation:** A row denominator 107 could produce 4.7%, but that would require a missing patient not disclosed by this table. A copied percentage is a possible mechanism, not an observation.
- **Direct observation versus inferred explanation:** The printed 5/4.7/108 mismatch is directly confirmed and calculated; unreported missingness or copying is inferred.
- **Exact remaining human question:** What row denominator and rounding convention produced mycophenolate 5 (4.7) under N = 108?
- **Classification:** `Denominator, proportion, or total inconsistency`; REPORT results-supplement row versus REPORT same-table header/footnote; `S_W`; all `S_W`. Confirmed.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** The source image confirms 4.7 rather than an OCR artifact, and the printed exposed denominator yields 4.6 under the stated rounding rule.
- **Status:** Pending Human Adjudication.

## C016 — Mycophenolate serious-diarrhea percentage after switching

- **Location found:** Yes; REPORT [Supplement 1 page 15 eTable 9 Serious Systemic diarrhea row](../../../joi190092supp1_prod.pdf#page=15), directly extracted and visually inspected.
- **Source value/text matched:** Yes: mycophenolate cell is 1 (3.4).
- **Comparator matched:** Yes: its column N = 20; the neighboring methotrexate column is N = 29. The row is under Serious Systemic, not the nonserious diarrhea row.
- **Consistency rule applicable:** The within-column patient proportion should reconcile with its own stated denominator under one-decimal rounding; 0.05-point tolerance applies.
- **Calculation reproduced:** `100 × 1 / 20 = 5.0%`, not 3.4%; `100 × 1 / 29 = 3.448276%` would round to 3.4% using the other column denominator.
- **Necessary inputs available:** Exact numerator, both headers, row label and precision are available. **Exact missing inputs or definitions:** Any serious-diarrhea-specific mycophenolate denominator is not disclosed.
- **Source-grounded alternative interpretation:** An alternate row population or misplaced input could account for the cell, but no such definition is supplied. The fact that the other denominator reproduces 3.4% does not establish the production mechanism.
- **Direct observation versus inferred explanation:** The within-column mismatch is observed and reproduced; borrowing the other denominator is an inferred explanation only.
- **Exact remaining human question:** What numerator and denominator generated the mycophenolate serious-diarrhea 1 (3.4) cell under N = 20?
- **Classification:** `Denominator, proportion, or total inconsistency`; REPORT result row versus REPORT same-table header; `S_W`; all `S_W`. Confirmed.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** Direct-source inspection confirms every printed input and reproduces the 1.6-percentage-point disagreement.
- **Status:** Pending Human Adjudication.

## C017 — Inclusive versus strict ocular-hypertension threshold

- **Location found:** Yes; REPORT [Supplement 1 page 5 eTable 1](../../../joi190092supp1_prod.pdf#page=5), [page 14 eTable 8](../../../joi190092supp1_prod.pdf#page=14), [page 15 eTable 9](../../../joi190092supp1_prod.pdf#page=15), and [main PDF page 8 Table 3](../../../jama_rathinam_2019_oi_190092.pdf#page=8), all directly extracted and visually inspected.
- **Source value/text matched:** Yes: eTable 1 nonserious ocular hypertension is `≥24 mm Hg`.
- **Comparator matched:** Yes: the main Table 3 and eTables 8/9 nonserious labels use `>24 mm Hg`. Main Table 3 footnote a points to the supplied eTable 1 definitions. The eTable 8 counts are 3/1; eTable 9 counts are 2/3; these different time/population counts are not equated.
- **Consistency rule applicable:** Threshold labels for the referenced event should agree. Exact inequality membership has zero tolerance.
- **Calculation reproduced:** At a measured value of 24, `24 ≥ 24` is true and `24 > 24` is false. The discrepancy is the printed boundary, not evidence of a wrong count.
- **Necessary inputs available:** Boundary symbols, event identity and the article's definition-reference footnote are available. **Exact missing inputs or definitions:** The implemented threshold and presence of observations exactly at 24 are unknown.
- **Source-grounded alternative interpretation:** The strict symbols could be shorthand or typographic substitutes, or an undisclosed threshold distinction could exist. The supplied labels do not establish which count includes equality.
- **Direct observation versus inferred explanation:** The ≥/> difference is direct; any resulting count change or underlying coding explanation is inferred.
- **Exact remaining human question:** Did the reported nonserious ocular-hypertension counts include values exactly equal to 24 mm Hg, and which boundary was implemented?
- **Classification:** `Measure, label, or scale inconsistency`; REPORT results-supplement definition versus REPORT main results and REPORT same-supplement result rows; `S_C`; all `S_C, S_W`, applying S_C precedence. Confirmed. The registered protocol citation merely supports the article's strict boundary and was not used as an independent discrepancy comparator; it does not create `P_R`.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** Visually confirmed explicit inequality symbols differ for the same referenced event; actual equality-case membership remains a named missing input.
- **Status:** Pending Human Adjudication.

## C018 — Serious ocular-hypertension result label

- **Location found:** Yes; REPORT [Supplement 1 page 5 eTable 1 serious definition](../../../joi190092supp1_prod.pdf#page=5), [page 14 eTable 8 Serious Ocular row](../../../joi190092supp1_prod.pdf#page=14), and corroborating [page 15 eTable 9 serious row](../../../joi190092supp1_prod.pdf#page=15), directly extracted and visually inspected.
- **Source value/text matched:** Yes: eTable 1 serious ocular hypertension is `Surgery required (laser or incisional)`.
- **Comparator matched:** Yes: eTable 8 under Serious Ocular labels the count `Ocular hypertension >24mm Hg`, 1 (1.6) and 0 (0.0). Its nonserious row uses the same pressure label. eTable 9 explicitly labels its serious row `surgery required`.
- **Consistency rule applicable:** A quantitative seriousness label should preserve or clearly reference its defining criterion. Pressure alone and surgery-required are not equivalent definitions. This is a conditional label comparison, not proof of misclassification.
- **Calculation reproduced:** The serious-row pressure label duplicates the nonserious threshold, while the defined serious criterion is surgery. `100 × 1 / 62 = 1.612903%` rounds to 1.6%; `0/56 = 0%` is coherent.
- **Necessary inputs available:** Serious definition, row heading, row label, counts and headers are available. **Exact missing inputs or definitions:** Whether the counted patient required surgery and whether the label is deliberately abbreviated are not supplied.
- **Source-grounded alternative interpretation:** The Serious Ocular heading may implicitly invoke the surgery definition despite the abbreviated row label. eTable 9 shows that the fuller label was used for another population; it does not identify the eTable 8 patient.
- **Direct observation versus inferred explanation:** The differing definitions/labels are observed. Misclassification, surgery actually performed and a production abbreviation are not established.
- **Exact remaining human question:** Does the eTable 8 serious ocular-hypertension count represent a surgery-required case, and is its pressure label an abbreviation of that criterion?
- **Classification:** `Measure, label, or scale inconsistency`; REPORT results-supplement definition versus REPORT same-supplement serious row; `S_W`; all `S_W`. Confirmed.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** The observed pressure-only label lacks the explicitly supplied surgery criterion, leaving the registered conditional label question unresolved.
- **Status:** Pending Human Adjudication.

## C019 — Serious cataract surgery and not-applicable definition

- **Location found:** Yes; REPORT [Supplement 1 page 5 eTable 1 cataract definition](../../../joi190092supp1_prod.pdf#page=5), [page 15 eTable 9 Serious Ocular cataract-surgery row](../../../joi190092supp1_prod.pdf#page=15), and [page 7 generic serious-event definitions](../../../joi190092supp1_prod.pdf#page=7), all directly extracted and visually inspected.
- **Source value/text matched:** Yes: nonserious cataract is visually significant cataract/cataract surgery indicated; serious cataract is `Not applicable (n/a)`.
- **Comparator matched:** Yes: eTable 9 reports Serious Ocular `Cataract surgery`, methotrexate 1 (3.4), mycophenolate 0 (0.0), under N = 29/20.
- **Consistency rule applicable:** A nonzero event under a category declared not applicable requires another stated basis for seriousness. A separate generic serious-event criterion could reconcile the classification; absent linkage, this is a conditional definition question.
- **Calculation reproduced:** n/a and a nonzero serious cataract-surgery entry are different printed category assignments. `100 × 1 / 29 = 3.448276%` rounds to 3.4%; no percentage error is registered here.
- **Necessary inputs available:** Cataract definition, serious row, counts and generic definitions are available. **Exact missing inputs or definitions:** The individual event's seriousness criterion and the applicability of generic criteria to the listed cataract category are not specified.
- **Source-grounded alternative interpretation:** Page 7 defines hospitalization and intervention to prevent permanent impairment/damage as serious occurrences. Actual cataract surgery might meet one of these generic criteria even though the cataract row has no separate serious grading. That is a supplied-source alternative, not proof of reconciliation for this patient.
- **Direct observation versus inferred explanation:** n/a and the one serious cataract surgery are direct observations; hospitalization, preventive intervention or a table-label mechanism are inferred possibilities.
- **Exact remaining human question:** Which supplied serious-event criterion supports the one serious cataract-surgery entry despite the cataract definition's n/a serious column?
- **Classification:** `Measure, label, or scale inconsistency`; REPORT results-supplement category definition versus REPORT same-supplement result, with REPORT generic-definition context; `S_W`; all `S_W`. Confirmed.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** The direct-source category tension reproduces; generic seriousness criteria provide a named conditional interpretation without identifying the counted event's actual basis.
- **Status:** Pending Human Adjudication.

## C020 — Fever “to 103” versus strict upper endpoint

- **Location found:** Yes; REPORT [Supplement 1 page 6 eTable 1 fever definition](../../../joi190092supp1_prod.pdf#page=6), [page 14 eTable 8 fever row](../../../joi190092supp1_prod.pdf#page=14), and [page 15 eTable 9 fever row](../../../joi190092supp1_prod.pdf#page=15), directly extracted and visually inspected.
- **Source value/text matched:** Yes: nonserious definition is `>100.6 to 103°F/39.5°C`, and serious is `≥103°F/39.5°C`.
- **Comparator matched:** Yes: both later nonserious fever labels read `Fever <103 degrees for 12 hours`. Counts are 3/3 under N = 62/56 and 4/1 under N = 29/20.
- **Consistency rule applicable:** Explicit endpoint definitions can be compared exactly. However, “to 103” does not specify a mathematical inclusion symbol at its upper end; assuming that “to” necessarily means ≤ is not justified by the printed text.
- **Calculation reproduced:** Under an inclusive interpretation, exactly 103 would satisfy both the nonserious “to” interval and the explicit serious ≥103 interval and would be excluded by the later <103 labels. Under an exclusive interpretation, the definition and later labels reconcile. Both comparisons are reproducible; the source does not select the first. Counts themselves reconcile: 3/62 = 4.8%, 3/56 = 5.4%, 4/29 = 13.8%, 1/20 = 5.0%, at one decimal.
- **Necessary inputs available:** All printed labels, counts and serious-boundary inequality are available. **Exact missing inputs or definitions:** The intended inclusivity of “to 103” and actual temperatures at the boundary are not supplied.
- **Source-grounded alternative interpretation:** The explicit serious ≥103 criterion and later nonserious <103 labels support reading “to 103” as up to but excluding 103, producing a coherent partition. This is not conclusively forced by the ordinary-language range wording.
- **Direct observation versus inferred explanation:** The different wording is direct; an inclusive upper endpoint and resulting overlap are inferred, conditional interpretations rather than directly printed contradictions.
- **Exact remaining human question:** Is the upper endpoint in “>100.6 to 103” intended to exclude exactly 103°F, as the later nonserious labels indicate?
- **Classification:** `Measure, label, or scale inconsistency`; REPORT results-supplement definition versus REPORT same-supplement later labels; `S_W`; all `S_W`. Confirmed as the registered comparison's content roles/type, while its necessary inclusive interpretation is not established. No temperature-conversion candidate is added.
- **Evidence state:** `record_input_error`. **Determining recheck fact:** The contradiction requires treating the ambiguous “to” wording as an inclusive ≤ endpoint, an unsupported input interpretation; whether any residual endpoint discrepancy exists cannot be settled from the package. The stable ID remains intact.
- **Status:** Pending Human Adjudication.

## Recheck classification table

| ID | Primary category | Relationship type | All relationships | Compared document roles | Evidence state |
|---|---|---|---|---|---|
| C001 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT main Table 1 row vs REPORT same-table header/footnotes | recorded_candidate |
| C002 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT main Table 3 liver row/abstract/narrative vs REPORT main header/allergic-reaction row | recorded_candidate |
| C003 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT main switch-eligibility narrative vs REPORT main failure/safety table and flow | recorded_candidate |
| C004 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT main lost-to-follow-up narrative vs REPORT main flow/missingness narrative | recorded_candidate |
| C005 | Numeric or arithmetic inconsistency | S_W | S_W | REPORT main majority wording vs REPORT same-sentence percentages | recorded_candidate |
| C006 | Analysis-unit or population inconsistency | S_W | S_W | REPORT main Table 1 exclusion/counts vs REPORT main Table 2 exclusion/counts | recorded_candidate |
| C007 | Measure, label, or scale inconsistency | S_W | S_W | REPORT main efficacy row c vs REPORT main success/efficacy footnotes | recorded_candidate |
| C008 | Measure, label, or scale inconsistency | S_W | S_W | REPORT main intolerability row d vs REPORT main efficacy/intolerability footnotes | recorded_candidate |
| C009 | Measure, label, or scale inconsistency | S_W | S_W | REPORT main safety row e vs REPORT main intolerability/safety footnotes | recorded_candidate |
| C010 | Measure, label, or scale inconsistency | S_W | S_W | REPORT main anatomical P cells f vs REPORT main safety/interaction footnotes | recorded_candidate |
| C011 | Measure, label, or scale inconsistency | S_W | S_W | REPORT main continuation row g vs REPORT main interaction/continuation footnotes | recorded_candidate |
| C012 | Measure, label, or scale inconsistency | S_W | S_W | REPORT main switching row h vs REPORT main continuation/switching footnotes | recorded_candidate |
| C013 | Measure, label, or scale inconsistency | S_W | S_W | REPORT main missed-dose row i vs REPORT main switching/dose-ratio footnotes | recorded_candidate |
| C014 | Denominator, proportion, or total inconsistency | S_C | S_C, S_W | REPORT main randomized safety header/footnote/percentages vs REPORT results-supplement exposed headers | not_reproduced |
| C015 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT results-supplement eTable 4 floaters cell vs REPORT same-table exposed header/footnote | recorded_candidate |
| C016 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT results-supplement eTable 9 serious-diarrhea cell vs REPORT same-table header | recorded_candidate |
| C017 | Measure, label, or scale inconsistency | S_C | S_C, S_W | REPORT results-supplement ocular definition vs REPORT main Table 3 and REPORT same-supplement later rows | recorded_candidate |
| C018 | Measure, label, or scale inconsistency | S_W | S_W | REPORT results-supplement serious ocular definition vs REPORT same-supplement serious row | recorded_candidate |
| C019 | Measure, label, or scale inconsistency | S_W | S_W | REPORT results-supplement serious cataract definition vs REPORT same-supplement serious surgery result | recorded_candidate |
| C020 | Measure, label, or scale inconsistency | S_W | S_W | REPORT results-supplement fever range wording vs REPORT same-supplement strict-endpoint rows | record_input_error |

Completed: 20 of 20 assigned IDs. Evidence states: 18 `recorded_candidate`, one `not_reproduced` (C014), one `record_input_error` (C020), zero `repaired_residual`. No source-access, rendering or tooling limitation remains in this scope. Patient-level memberships, implemented rounding conventions, intended marker attachments, and endpoint inclusivity remain named human questions where applicable. All IDs and all supplied sources were preserved.

