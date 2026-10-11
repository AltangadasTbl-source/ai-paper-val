# Complete exact-source evidence recheck

All 57 stable IDs are covered by three disjoint fresh-agent parts below. Each original part is preserved. Visual PDF evidence governs over native-text transcription where inequality glyphs differ.

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


# Mechanical evidence recheck: PLAN candidates C021–C038

Scope: all 18 assigned stable IDs C021–C038, separately rechecked against supplied protocol and SAP PDFs. All IDs remain Pending Human Adjudication. This artifact records evidence facts only. The complete registration header, the assigned cards and applicable scope/contract were read; no old review supplied scientific input. Exact direct-source text and source-rendered images, rather than prior OCR transcriptions, determine the observations below.

## Source-authority and tooling record

Direct engines: Poppler pdftotext/pdftoppm 26.01.0, CPU only, as available in tooling_record.md. Commands: `pdftotext -layout -f N -l N SOURCE preprocessing/recheck_plans_SOURCE_N.txt` and `pdftoppm -r 100 -f N -l N -singlefile -png SOURCE preprocessing/recheck_plans_SOURCE_N`. Actual output prefix is `.ai_paper_validation/review_1_6/preprocessing/recheck_plans_protocol_N` for joi190092supp2_prod.pdf and `recheck_plans_sap_N` for joi190092supp3_prod.pdf. Protocol text pages: 9, 11, 16, 22, 26, 27, 42, 43, 44, 45, 52, 53, 81, 86, 87, 103, 110, 115, 117, 123, 124, 125, 126, 127. Visually inspected rendered protocol pages: 11, 16, 22, 26, 27, 42, 43, 44, 45, 52, 53, 86, 87, 103, 110, 115, 117, 123, 124, 125, 126, 127. SAP text pages: 9, 10, 24, 25, 26, 27, 50, 65, 66, 67, 68. Visually inspected rendered SAP pages: 9, 10, 24, 26, 27, 50, 65, 66, 67, 68. No OCR was necessary. No source or pre-existing reusable artifact was modified. Native text was used to locate strings; exact page appearance was read for the comparisons and inequality/unit labels.

Links in this part are relative to its verification directory and use physical PDF page numbers. The source original protocol is dated September 4, 2012; final protocol January 6, 2017 Version 4.5. The original and final SAPs are dated January 29, 2013 and March 9, 2017. All their prospective instructions and background power inputs are PLAN by content. Historical versions within either bundle remain PLAN. No REPORT location participates in these 18 comparisons; primary relationship and All relationships are P_P for every ID, and review domain is plan_material. Later revised values do not retrospectively remove a printed inconsistency within an original version. No new P_R relationship is created by corroboration.

## C021 — Planned maximum-follow-up completion predates eligible completion

- **Location found:** Yes: [protocol PDF p11, Table 1](../../../joi190092supp2_prod.pdf#page=11).
- **Source value/text matched:** Enrollment November 2012 through May 2015; finish six-month follow-up plus one-month window through December 2015; finish maximum twelve-month follow-up plus one-month window through July 2015; database lock/analysis through April 2016. Visually matched.
- **Comparator matched:** Yes: these are neighboring rows of the same original timeline, referring to study enrollment and follow-up completion.
- **Consistency rule applicable:** A maximum-follow-up completion for the stated enrollment cohort cannot precede its six-month follow-up completion or twelve months after its final entrants, absent a subset qualifier.
- **Calculation or logical comparison reproduced:** May 2015 plus twelve months is May 2016; adding the stated one-month window gives approximately June 2016. July 2015 is two months after May 2015 and five months before December 2015. Month-only boundary uncertainty cannot remove the approximately eleven-month maximum-window gap.
- **Necessary inputs available:** Enrollment endpoint, stated durations/window and completion dates are supplied. No actual enrollment records are needed for the printed planning comparison.
- **Exact missing inputs or definitions:** Whether the July 2015 row refers to a restricted subset or an earlier enrollment cutoff; neither qualifier is printed.
- **Source-grounded alternative interpretation:** July 2015 could be a stale forecast or a subset deadline. The final protocol is a disclosed later version and is not this same-version comparator.
- **Direct observation versus inferred explanation:** Dates and labels are direct; a stale forecast or calendar typo is an explanation, not established fact. Applying twelve months to the latest allowed entrant is the stated planning-rule inference.
- **Classification confirmed/corrected:** Numeric or arithmetic inconsistency; PLAN p11 timeline versus PLAN same timeline; P_P; All relationships P_P; plan_material. No correction.
- **Evidence state:** recorded_candidate. Decisive fact: same-version timeline prints maximum follow-up completion before both the stated cohort's eligible twelve-month completion and its six-month completion.
- **Exact remaining human question:** Which cohort/enrollment cutoff is intended for July 2015, and how does that row reconcile with May 2015 enrollment ending and December 2015 six-month completion?

## C022 — Original leukocyte classification leaves exactly 1000/μL without a class

- **Location found:** Yes: [protocol PDF p16, Table 3 leukocyte row](../../../joi190092supp2_prod.pdf#page=16).
- **Source value/text matched:** Non-serious: >1,000 and <2,500/μL lasting less than one month. Serious: <2,500 lasting more than one month or ≤999/μL. All symbols visually matched.
- **Comparator matched:** Yes: paired non-serious/serious cells for the same analyte and original version.
- **Consistency rule applicable:** Threshold bins intended to classify an acute abnormal value should have a defined class at their displayed boundary.
- **Calculation or logical comparison reproduced:** For 1,000/μL lasting less than one month, 1,000>1,000 is false; 1,000≤999 is false; the more-than-one-month condition is false. Neither displayed cell classifies that test value.
- **Necessary inputs available:** Both inequalities, unit and duration qualifiers are supplied; zero integer-count tolerance.
- **Exact missing inputs or definitions:** The intended inclusive boundary or discretionary classification for exactly 1,000/μL. No actual patient value is supplied or claimed.
- **Source-grounded alternative interpretation:** A positive lower bound intended as ≥1,000, or serious intended as ≤1,000, would close the gap. Later final-version thresholds are a separate disclosed context.
- **Direct observation versus inferred explanation:** Printed gap is direct; the boundary-value substitution is a logical demonstration. An intended inequality or patient consequence is not established.
- **Classification confirmed/corrected:** Measure, label, or scale inconsistency; PLAN Table 3 versus PLAN same row; P_P; All relationships P_P; plan_material. No correction.
- **Evidence state:** recorded_candidate. Decisive fact: the exact integer 1,000 fails both displayed acute-bin rules.
- **Exact remaining human question:** Which original adverse-event class should receive 1,000 leukocytes/μL lasting less than one month?

## C023 — Original platelet classes overlap at 20000/μL

- **Location found:** Yes: [protocol PDF p16, Table 3 platelet row](../../../joi190092supp2_prod.pdf#page=16).
- **Source value/text matched:** Non-serious: 20,000 to 75,000/μL lasting less than one month. Serious: ≤20,000/μL or <75,000/μL lasting greater than one month. Visually matched.
- **Comparator matched:** Yes: same analyte and original paired-bin row.
- **Consistency rule applicable:** A classification lookup should assign the same boundary value uniquely, unless precedence or an open interval is specified.
- **Calculation or logical comparison reproduced:** Under inclusive interpretation of “20,000 to 75,000,” an acute 20,000 belongs to that range and satisfies ≤20,000. Both cells apply. This is a zero-tolerance exact-boundary comparison.
- **Necessary inputs available:** Printed thresholds, duration and common unit; inclusive meaning of “to” remains an assumption explicitly stated here.
- **Exact missing inputs or definitions:** Whether “to” excludes its lower endpoint, and whether serious classification takes precedence when both bins apply.
- **Source-grounded alternative interpretation:** An open non-serious lower boundary or priority for serious events can reconcile operational coding. Final-version <20,000 is a later version, not a contradictory REPORT observation.
- **Direct observation versus inferred explanation:** The printed endpoints are direct; overlap follows conditional inclusive interpretation. No observed platelet event is reconstructed.
- **Classification confirmed/corrected:** Measure, label, or scale inconsistency; PLAN versus PLAN in Table 3; P_P; All relationships P_P; plan_material. No correction.
- **Evidence state:** recorded_candidate. Decisive fact: the registered conditional endpoint overlap is reproduced, pending the named interval-inclusion/precedence definition.
- **Exact remaining human question:** Is 20,000/μL intended as serious or non-serious, and is the non-serious lower endpoint open or subject to serious-event precedence?

## C024 — Original AST/ALT event class differs at supplied boundary values

- **Location found:** Yes: [protocol PDF p16, Table 3](../../../joi190092supp2_prod.pdf#page=16), [p52, §6.1](../../../joi190092supp2_prod.pdf#page=52), [p53, §6.1 continuation and §6.2](../../../joi190092supp2_prod.pdf#page=53).
- **Source value/text matched:** Table: non-serious 2 to 5 times ULN; serious >5 times ULN. Prose non-serious examples: >2 but <5 times ULN. Serious prose: ≥5 times ULN. Symbols and continuation across pp52–53 visually matched.
- **Comparator matched:** Yes: the original protocol's AST/ALT adverse-event thresholds, not a cross-version change.
- **Consistency rule applicable:** The same analyte at the same exact multiple should have consistent serious/non-serious boundary labeling, absent explicit precedence.
- **Calculation or logical comparison reproduced:** At 5×ULN, 5>5 is false but 5≥5 is true. The Table 3 serious rule excludes the value and §6.2 includes it. If “2 to 5” is inclusive, Table 3 further labels it non-serious. At 2×ULN, the table interval and non-exhaustive §6.1 example also differ in inclusion; the stronger explicit serious-boundary comparison is at five.
- **Necessary inputs available:** Exact thresholds, analytes and ULN multiplier; zero boundary tolerance.
- **Exact missing inputs or definitions:** Table-versus-prose precedence and inclusion convention for “to.” The non-serious example list is expressly an example list, not a complete bin definition.
- **Source-grounded alternative interpretation:** Table precedence, prose precedence or a clinical checklist may resolve operational coding. An example's omission of 2× alone need not contradict a complete classification.
- **Direct observation versus inferred explanation:** Different > and ≥ signs are direct; the coding consequences follow boundary substitution. No final trial event is recoded here.
- **Classification confirmed/corrected:** Measure, label, or scale inconsistency; PLAN original Table 3 versus PLAN original adverse-event prose; P_P; All relationships P_P; plan_material. No correction; the exact-five comparator governs.
- **Evidence state:** recorded_candidate. Decisive fact: >5 and ≥5 classify the exact-five serious-event boundary differently within the original version.
- **Exact remaining human question:** Which original instruction controls serious/non-serious classification at exactly 5×ULN for AST/ALT, and how should Table 3 and §6.2 be read together?

## C025 — Same-drug follow-up extension receives alternate-drug phase label

- **Location found:** Yes: [protocol PDF p22, prednisone initial-dose paragraph](../../../joi190092supp2_prod.pdf#page=22), [p26, §4.1.1](../../../joi190092supp2_prod.pdf#page=26), [p27, Table 10 and §4.1.2](../../../joi190092supp2_prod.pdf#page=27); p9 prospective aim description also located by direct text.
- **Source value/text matched:** P22 holds 7.5 mg/day for first six months “until the end of Phase I” and allows further reduction “in Phase II, if patients continue on the same medication as Phase I.” P26–27 call continuation on the randomized medication Phase I (6–12 months); Phase II rescue switches to the alternate treatment. Visually matched primary comparators.
- **Comparator matched:** Yes: continuation on the same initial medication after six months versus formal phase definitions.
- **Consistency rule applicable:** A named phase attached to the same drug/time continuation should agree with its operational definition.
- **Calculation or logical comparison reproduced:** Same first drug plus months 6–12 maps to Phase I extension under Table 10 and §4.1.1; p22 names that same-drug continuation Phase II. Formal Phase II on p27 maps to a different drug after failure.
- **Necessary inputs available:** Drug continuation, phase labels, six-month transition and rescue definition. No actual follow-up data are needed.
- **Exact missing inputs or definitions:** Whether p22 uses Phase II informally for the second six-month period rather than the formally defined rescue phase.
- **Source-grounded alternative interpretation:** Local steroid-taper prose may use a chronological phase convention. That interpretation is not explicitly distinguished from the formal visit-schedule convention.
- **Direct observation versus inferred explanation:** Labels and conditions are direct; a local alternative phase vocabulary or template error is inferred. No dosing outcome is claimed.
- **Classification confirmed/corrected:** Measure, label, or scale inconsistency; PLAN original p22 versus PLAN original pp26–27; P_P; All relationships P_P; plan_material. No correction.
- **Evidence state:** recorded_candidate. Decisive fact: the source labels same-drug post-six-month continuation both Phase I and Phase II.
- **Exact remaining human question:** Does the p22 taper permission on the same medication refer to Phase I extension months 6–12, or does “Phase II” have a separate local chronological meaning?

## C026 — Original visit-window column states weeks for day-valued entries

- **Location found:** Yes: [protocol PDF p26, Table 9](../../../joi190092supp2_prod.pdf#page=26), [p27, Table 10](../../../joi190092supp2_prod.pdf#page=27).
- **Source value/text matched:** Both headers say “Window (weeks)”; populated cells explicitly show ±15 days and −15 to +30 days. Visually matched.
- **Comparator matched:** Yes: header versus cells in each same original-version table.
- **Consistency rule applicable:** The column's stated unit should agree with the cells' stated interval units.
- **Calculation or logical comparison reproduced:** ±15 days = ±15/7 weeks, approximately ±2.143 weeks; −15/+30 days = approximately −2.143/+4.286 weeks. Reading the header as ±15 weeks instead would introduce a factor seven; the explicit cells themselves specify days.
- **Necessary inputs available:** Header, populated intervals and day/week relationship; exact dimensional comparison.
- **Exact missing inputs or definitions:** Which layer of labeling was intended as controlling. No uncertainty about the literal cell unit remains.
- **Source-grounded alternative interpretation:** Cell units override a stale template header and can make human scheduling fully unambiguous.
- **Direct observation versus inferred explanation:** Header/cell unit difference is direct. A sevenfold scheduling error is only a hypothetical extraction consequence, not observed.
- **Classification confirmed/corrected:** Measure, label, or scale inconsistency; PLAN table header versus PLAN same-table cells; P_P; All relationships P_P; plan_material. No correction.
- **Evidence state:** recorded_candidate. Decisive fact: both tables directly print a weeks header above day-labeled cells.
- **Exact remaining human question:** Should the column header be read as days, or should each explicit cell unit govern independently despite the weeks header?

## C027 — Original Month 6 window differs across adjoining Phase I schedule tables

- **Location found:** Yes: [protocol PDF p26, Table 9 Month 6](../../../joi190092supp2_prod.pdf#page=26), [p27, Table 10 Month 6](../../../joi190092supp2_prod.pdf#page=27).
- **Source value/text matched:** Table 9 M6-I (II) window −15 to +30 days; Table 10 M6-I window ±15 days, since Phase I baseline/treatment administration. Visually matched.
- **Comparator matched:** The Phase I part of Table 9 and Table 10 share M6-I, Month 6 and the initial baseline. Phase II's parenthetical counterpart is not used as this comparator.
- **Consistency rule applicable:** Matched visit-code/time windows should agree if they govern the same assessment.
- **Calculation or logical comparison reproduced:** Lower endpoint −15 agrees; upper endpoints +30 and +15 differ by 15 days. All printed cell units are days regardless of the independent C026 header issue.
- **Necessary inputs available:** Visit codes, baseline qualifiers, months and interval endpoints; exact day comparison.
- **Exact missing inputs or definitions:** Whether a narrower extension-entry window is separately intended, or a single Month 6 assessment must satisfy both tables.
- **Source-grounded alternative interpretation:** The primary endpoint could accept +30 days while entry into extension requires +15 days. The adjoining tables do not state that distinction.
- **Direct observation versus inferred explanation:** Repeated code and unequal endpoints are direct. Treating the rows as one assessment is an explicit alignment inference with a named alternative.
- **Classification confirmed/corrected:** Numeric or arithmetic inconsistency; PLAN original p26 versus PLAN original p27; P_P; All relationships P_P; plan_material. No correction.
- **Evidence state:** recorded_candidate. Decisive fact: matching printed Phase I M6-I rows have unequal upper-window limits, with any separate-entry interpretation still needing definition.
- **Exact remaining human question:** Are the two Phase I M6-I rows one assessment or separate endpoint/extension-entry assessments, and which upper limit governs each?

## C028 — Tumbling-E score formula requires more letters on one line than the line contains

- **Location found:** Yes: [protocol PDF p43, scoring clause](../../../joi190092supp2_prod.pdf#page=43), [p44, scoring continuation/Snellen rule](../../../joi190092supp2_prod.pdf#page=44), [p124, final scoring clause](../../../joi190092supp2_prod.pdf#page=124), [p125, final Snellen rule](../../../joi190092supp2_prod.pdf#page=125).
- **Source value/text matched:** Both versions require “10 or more letters of the first line” correctly read at 4 meters for the +30 score rule. Both state Snellen equivalent from the most difficult line having at least 4 of 5 letters correct. The highest attainable score is 100. Visually matched.
- **Comparator matched:** Same Tumbling-E chart scoring context and line-count description within each version. The letter-chart procedure elsewhere is not substituted.
- **Consistency rule applicable:** A qualifying correct-letter count on a single five-letter line cannot exceed the number of letters on that line.
- **Calculation or logical comparison reproduced:** At most five correct letters can occur on a five-letter line; ten exceeds five by five. The maximum total-score arithmetic is not the mismatch: 70+30=100 is coherent. The registered first-line criterion remains the comparator.
- **Necessary inputs available:** The ten-letter first-line wording and five-letter line description; exact discrete counts. The page does not supply an alternative meaning of “first line.”
- **Exact missing inputs or definitions:** Whether “first line” means total chart letters or some multi-row grouping; actual chart artwork and score form resolving this wording are not supplied at these locations.
- **Source-grounded alternative interpretation:** Ten total letters across at least two five-letter rows could be the intended qualification and would avoid the impossible single-row condition.
- **Direct observation versus inferred explanation:** Literal words and 4-of-5 line definition are direct; identifying a wording error rather than an unusual multi-row meaning is an explanation, not a final correction.
- **Classification confirmed/corrected:** Numeric or arithmetic inconsistency; PLAN scoring clauses versus PLAN same-version line definition, repeated in the bound versions; P_P; All relationships P_P; plan_material. No correction.
- **Evidence state:** recorded_candidate. Decisive fact: the single-line ten-letter requirement cannot be met under the source's five-letter line description, pending the named meaning of “first line.”
- **Exact remaining human question:** Does “10 or more letters of the first line” mean ten total chart letters, and what observable qualification should govern the 4-meter count plus 30?

## C029 — Tumbling-E low-vision/scoring thresholds do not cover the same letter counts

- **Location found:** Yes: [protocol PDF p42, testing procedure](../../../joi190092supp2_prod.pdf#page=42), [p43, one-meter testing and scoring](../../../joi190092supp2_prod.pdf#page=43), [p44, scoring/analysis](../../../joi190092supp2_prod.pdf#page=44), [p123, final testing procedure](../../../joi190092supp2_prod.pdf#page=123), [p124, final scoring](../../../joi190092supp2_prod.pdf#page=124), [p125, analysis continuation](../../../joi190092supp2_prod.pdf#page=125).
- **Source value/text matched:** Procedure: less than ten total letters at 4 meters leads to one-meter testing; less than ten at one meter leads to low-vision testing. Scoring: three or fewer largest-line letters at 4 meters uses the one-meter count; three or fewer letters at one meter requires low-vision testing and uses the converted result for analysis. Visually matched in both versions.
- **Comparator matched:** The wording is matched, but not a single common quantity/action: total-chart counts, largest-line counts, test administration and analysis encoding are different inputs/stages.
- **Consistency rule applicable:** Only conditionally. A contradiction would require the testing trigger and the scoring/encoding threshold to be identical, exclusive classification rules. The supplied text does not establish exclusivity.
- **Calculation or logical comparison reproduced:** Five one-meter letters satisfies 5<10 and fails 5≤3; nine total four-meter letters with five on the largest line satisfies total<10 and fails largest-line≤3. These substitutions reproduce different triggers, not by themselves incompatible instructions. “If ≤3, test” does not mean “if >3, do not test.”
- **Necessary inputs available:** Printed thresholds, stages and count units are supplied.
- **Exact missing inputs or definitions:** Whether a 4–9-letter result is stored simultaneously with low-vision testing, and which measurement is selected for analysis. The complete data-entry/analysis mapping for these counts is absent from the compared passages.
- **Source-grounded alternative interpretation:** Perform low-vision testing below ten to collect additional information, but reserve replacing the numerical letter score with a low-vision-derived logMAR result for three or fewer. The text's separate testing/scoring sections permit this interpretation.
- **Direct observation versus inferred explanation:** Distinct thresholds are direct. Registration's inference that the differing tests imply an inconsistent encoding is unsupported without the missing selection rule; no patient result or analyzed scale is shown.
- **Classification confirmed/corrected:** Measure, label, or scale inconsistency remains the registered conditional category; all compared locations are PLAN; P_P; All relationships P_P; plan_material. Roles/relationships unchanged. Comparison interpretation corrected: different stage/unit thresholds are not established as identical exclusive bins.
- **Evidence state:** record_input_error. Decisive fact: the registered mismatch assumes alignment of nonexclusive procedure and encoding rules using different count units; direct source does not supply that alignment, and residual analysis selection cannot be settled from the passages.
- **Exact remaining human question:** For one-meter 4–9 letters, or fewer than ten four-meter total letters with more than three on the largest line, can both letter and low-vision measurements be recorded, and which value is selected for analysis?

## C030 — Vitreous-cell grades both include zero cells

- **Location found:** Yes: [protocol PDF p45, vitreous-cell table](../../../joi190092supp2_prod.pdf#page=45), [p127, final vitreous-cell table](../../../joi190092supp2_prod.pdf#page=127).
- **Source value/text matched:** Grade 0: No cells; grade 0.5+: 0 to 5 cells. Subsequent grades 6–10, 11–20, 21–50 and >50. Both versions specify this collected measure is not part of criteria for controlled inflammation. Visually matched.
- **Comparator matched:** Yes: paired bins for one count scale in each version.
- **Consistency rule applicable:** A count-to-grade lookup should assign zero uniquely absent a sampling/precedence distinction.
- **Calculation or logical comparison reproduced:** Zero means no cells and lies in the explicitly printed 0–5 interval. Both grade 0 and 0.5+ match literally; zero count has no rounding ambiguity.
- **Necessary inputs available:** Counts, grade labels and same field-size definition are supplied.
- **Exact missing inputs or definitions:** Any positive-count lower bound or distinction between truly absent cells and observed occasional cells across fields.
- **Source-grounded alternative interpretation:** “0 to 5” may colloquially describe trace/occasional cells despite a zero sampled field. That sampling convention is not printed in the bin definition.
- **Direct observation versus inferred explanation:** Duplicate zero coverage is direct; different actual coding or any primary outcome impact is not demonstrated.
- **Classification confirmed/corrected:** Measure, label, or scale inconsistency; PLAN grade bins versus PLAN same table; P_P; All relationships P_P; plan_material. No correction.
- **Evidence state:** recorded_candidate. Decisive fact: both displayed grade bins include zero under literal count lookup.
- **Exact remaining human question:** What distinguishes grade 0 from grade 0.5+ when zero cells are counted, and is the latter interval intended to have a positive lower bound?

## C031 — Original white-cell event example changes numeric scale without a unit marker

- **Location found:** Yes: [protocol PDF p16, Table 3](../../../joi190092supp2_prod.pdf#page=16), [p53, §6.1 continuation](../../../joi190092supp2_prod.pdf#page=53).
- **Source value/text matched:** Table 3 leukocyte threshold <2,500/μL (with other duration/lower-limit qualifiers); non-serious example says “reduction of white blood cell count to below 2.5” without a WBC unit or multiplier. The adjacent creatinine value has mg/dL, so that unit cannot be transferred to WBC. Visually matched.
- **Comparator matched:** Same leukocyte/WBC non-serious-event concept; the example is not an exhaustive classification rule and does not supply a scale.
- **Consistency rule applicable:** A numerical laboratory boundary requires an explicit or unambiguously inherited unit/scale for extraction. The registered candidate is an omitted scale label, not an asserted literal threshold disagreement.
- **Calculation or logical comparison reproduced:** 2,500/2.5=1,000. If the example uses thousands/μL, 2.5×10³/μL=2,500/μL; if it uses 10⁹/L, 2.5×10⁹/L=2,500/μL. The numbers can reconcile; carrying unchanged cells/μL into unitless 2.5 would be an unsupported assumption.
- **Necessary inputs available:** The two printed numeric forms and the table unit are supplied; exact factor comparison is possible.
- **Exact missing inputs or definitions:** The example's WBC unit/multiplier and whether its 2.5 is intended to restate the Table 3 upper non-serious threshold. Duration/lower-limit qualifiers also do not appear in the example.
- **Source-grounded alternative interpretation:** An omitted conventional rescaled laboratory unit fully explains the numeric forms. A brief illustrative example need not repeat all classification qualifiers.
- **Direct observation versus inferred explanation:** Missing unit is direct; a thousandfold threshold error is not observed. The rescaling is a conditional reconciliation, not evidence that either numerical boundary is wrong.
- **Classification confirmed/corrected:** Measure, label, or scale inconsistency; PLAN table unit versus PLAN unitless example; P_P; All relationships P_P; plan_material. No role/type/category correction. Framing explicitly restricted to the omitted scale label.
- **Evidence state:** recorded_candidate. Decisive fact: the source supplies the unitless numerical boundary as registered, leaving a reproducible missing-unit question; it does not support assuming the same unit for both values.
- **Exact remaining human question:** What unit/multiplier is intended for “below 2.5,” and is it the rescaled counterpart of below 2,500/μL in Table 3?

## C032 — Mycophenolate maintenance bottle described as 30-day supply contains 16⅔ days at full dose

- **Location found:** Yes: [protocol PDF p86, §3.1.2 maintenance dose](../../../joi190092supp2_prod.pdf#page=86), [p87, §3.1.4 packaging](../../../joi190092supp2_prod.pdf#page=87).
- **Source value/text matched:** MMF dose 1.5 g twice daily, explicitly three pills AM and three PM. P87 says maintenance-dose bottles contain thirty days plus buffer, and MMF supplied in 100-pill bottles; baseline gives one maintenance bottle plus fourteen-day introductory dose; subsequent monthly supply is 200 pills. Visually matched.
- **Comparator matched:** Yes: full maintenance dose versus maintenance-bottle duration label. Individual-bottle and monthly-dispensing quantities are kept distinct.
- **Consistency rule applicable:** Duration supplied equals pill count divided by the stated daily pill use, when a single bottle is called a thirty-day supply.
- **Calculation or logical comparison reproduced:** Six pills/day; 100/6=16⅔ days. Thirty days requires 180 pills before buffer; shortfall to that label is eighty pills. Monthly 200/6=33⅓ days and baseline 14+100/6=30⅔ days are coherent under their separate statements.
- **Necessary inputs available:** Maintenance pills per day, single-bottle count, duration claim and actual dispensing amounts.
- **Exact missing inputs or definitions:** Whether “maintenance dose bottles” describes a multi-bottle dispensing package collectively or each bottle individually.
- **Source-grounded alternative interpretation:** Two MMF bottles make the monthly thirty-day-plus-buffer package. Baseline one bottle only needs to bridge approximately sixteen days after the introductory period; the source's dispensing schedule thus does not show patient undersupply.
- **Direct observation versus inferred explanation:** Counts and dose are direct; bottle-level duration arithmetic is derived. Patient undersupply or dispensing error is not established.
- **Classification confirmed/corrected:** Numeric or arithmetic inconsistency; PLAN final dose versus PLAN final bottle-content/duration prose; P_P; All relationships P_P; plan_material. No correction.
- **Evidence state:** recorded_candidate. Decisive fact: a single 100-pill maintenance bottle cannot itself meet the stated thirty-day-plus-buffer description at six pills/day, while collective dispensing remains a stated alternative.
- **Exact remaining human question:** Does the thirty-day maintenance-bottle statement mean each 100-pill MMF bottle or the two-bottle monthly package?

## C033 — Final letter-chart refraction Chart R has two numeric version identifiers

- **Location found:** Yes: [protocol PDF p103, manifest refraction](../../../joi190092supp2_prod.pdf#page=103), [p110, letter-chart equipment description](../../../joi190092supp2_prod.pdf#page=110).
- **Source value/text matched:** P103: Chart R, Precision Vision Chart Version 2110. P110: Charts 1, 2 and R, Precision Vision Charts 2110, 2111 and 2112 respectively; Chart R used for all manifest subjective refractions. Visually matched.
- **Comparator matched:** Refraction chart name and use match; the two catalog/version identifiers differ. Their actual layouts/calibration or any changed quantitative outcome scale do not have supplied matched evidence.
- **Consistency rule applicable:** Identifier identity is applicable to chart naming. A quantitative scale inconsistency requires an additional source-grounded link between the differently numbered charts and a different count/scale/result interpretation; numeric identifiers themselves are not quantities.
- **Calculation or logical comparison reproduced:** “Respectively” maps R to 2112 on p110, while p103 maps R to 2110. Identifier equality fails. Subtracting two catalog numbers has no meaningful scientific magnitude, so no outcome-scale calculation follows.
- **Necessary inputs available:** Names, identifiers and intended refraction use. They suffice for a textual equipment-identity observation only.
- **Exact missing inputs or definitions:** Chart artwork/calibration, whether 2110 and 2112 differ in optotypes but have interchangeable quantitative scales, and any supplied affected count/statistic/scale alignment.
- **Source-grounded alternative interpretation:** Two charts can be refraction alternatives with identical scoring geometry, or a catalog mapping can have a labeling typo. Neither establishes an inconsistent reported numerical outcome.
- **Direct observation versus inferred explanation:** Different identifiers are direct. A changed acuity scale, wrong administered chart or changed trial result is unsupported inference.
- **Classification confirmed/corrected:** Retain registered Measure, label, or scale inconsistency as the proposed domain of the unresolved comparison; all compared content is PLAN; P_P; All relationships P_P; plan_material. Roles/type unchanged. Scope-alignment assumption corrected: catalog IDs alone do not demonstrate a quantitative scale mismatch.
- **Evidence state:** record_input_error. Decisive fact: registration aligns two numerical equipment identifiers with an outcome-scale inconsistency without supplied calibration or quantitative-result counterpart; residual quantitative relevance cannot be settled from the package.
- **Exact remaining human question:** Are 2110 and 2112 interchangeable refraction charts on the same quantitative scale, and what supplied numeric outcome or scale definition, if any, differs between them?

## C034 — Intermediate E-chart sphere retest uses a lens different from its next conditional

- **Location found:** Yes: [protocol PDF p115, lens guide](../../../joi190092supp2_prod.pdf#page=115), [p117, intermediate 6/30–6/60 sphere branch](../../../joi190092supp2_prod.pdf#page=117).
- **Source value/text matched:** Guide specifies sphere probes/increments +1.00/−1.00/+1.00 for intermediate acuity. Branch: if −1.00 does not allow more letters or makes vision worse, retest using +0.50; next two conditionals assess +1.00 as better/same or worse. No intervening presentation of +1.00 is printed. Visually matched.
- **Comparator matched:** Yes: probe action and its immediately subsequent branch labels in the same intermediate-acuity sequence.
- **Consistency rule applicable:** A conditional assessing a specified probe should name the probe actually administered or state the intervening probe change.
- **Calculation or logical comparison reproduced:** +1.00−(+0.50)=0.50 diopter, and +1.00 is twice +0.50. The instructions provide the +0.50 response but condition the next action on +1.00; zero tolerance for prescribed lens identity.
- **Necessary inputs available:** Exact probe powers, ordered steps and intermediate-acuity group.
- **Exact missing inputs or definitions:** Whether +0.50 is a deliberate additional probe and an omitted +1.00 presentation is assumed, or whether a numerical label was carried over.
- **Source-grounded alternative interpretation:** The note permits changing lens guides if acuity improves significantly. Here the immediate trigger is failure of −1.00 to improve letters, so that note does not explicitly supply the missing +1.00 step; an earlier improvement could nevertheless motivate a guide change.
- **Direct observation versus inferred explanation:** Lens numbers and sequence are direct. A copied lens label or skipped step is an explanation, not a correction prescribed here.
- **Classification confirmed/corrected:** Numeric or arithmetic inconsistency; PLAN final lens/action versus PLAN subsequent conditional; P_P; All relationships P_P; plan_material. No correction.
- **Evidence state:** recorded_candidate. Decisive fact: sequential retest and response branch name different lens powers without a printed intervening +1.00 test.
- **Exact remaining human question:** After the −1.00 intermediate-acuity probe fails, is the retest +0.50 or +1.00, and which response governs the subsequent branch?

## C035 — Final cataract category list omits the expressly defined grade 3

- **Location found:** Yes: [protocol PDF p125, cataract-grade definitions](../../../joi190092supp2_prod.pdf#page=125), [p126, category prose and embedded scale figure](../../../joi190092supp2_prod.pdf#page=126).
- **Source value/text matched:** P125 standard 1 indicates clinical presence, 2 clinical significance, 3 severe occurrence; half grades allowed. P126 prose list is <1, 1, 1.5, 2, 2.5, >3. Visual inspection additionally finds exact 3 marked on each illustrated opacity severity scale, separate from >3 below it.
- **Comparator matched:** Yes: defined grade 3 and illustrated grade 3 versus same final-version prose category list for all three opacity types.
- **Consistency rule applicable:** An explicitly defined/illustrated grade should have a category in the stated category list.
- **Calculation or logical comparison reproduced:** 3 is not <1, not 1/1.5/2/2.5, and not >3. Thus the list omits exact 3. The image itself includes both 3 and >3, so >3 cannot be silently read as the only figure category embracing three.
- **Necessary inputs available:** Standard definitions, list and contemporaneous scale figure. Exact ordinal value has no rounding tolerance.
- **Exact missing inputs or definitions:** Whether the clinical form includes 3 separately and whether the prose list intended to enumerate the same image/form categories completely.
- **Source-grounded alternative interpretation:** The figure can guide correct grade 3 assignment despite its omission from prose. A form may also contain grade 3; no supplied form value is asserted here.
- **Direct observation versus inferred explanation:** Prose omission and figure's exact 3 labels are direct. An omitted list item is a possible production explanation; no trial cataract count changes are shown.
- **Classification confirmed/corrected:** Measure, label, or scale inconsistency; PLAN grade-standard prose/figure versus PLAN final category list; P_P; All relationships P_P; plan_material. No role/type/category correction; the figure is added as direct corroborating source evidence, not a new relationship.
- **Evidence state:** recorded_candidate. Decisive fact: both the standard prose and embedded scale define grade 3, while the category list contains >3 and omits 3.
- **Exact remaining human question:** Should exact grade 3 appear separately in the listed cataract categories, and does the clinical form follow the illustrated scale including 3?

## C036 — Individual block-size probability wording

- **Location found:** Yes: [original SAP PDF p9, §2.4.3](../../../joi190092supp3_prod.pdf#page=9), [p10, continuation](../../../joi190092supp3_prod.pdf#page=10), [final SAP p50, §2.4.3](../../../joi190092supp3_prod.pdf#page=50).
- **Source value/text matched:** Choose a block of size four with probability 2/3, size six with probability 1/3; “Individuals have a higher probability of being in a block of size 6 because the blocks are larger.” Visually matched in both versions.
- **Comparator matched:** The numerical block-selection law and individual-probability prose match. The comparator implied by “higher” is not stated explicitly.
- **Consistency rule applicable:** Participant weighting is proportional to block size times block-selection probability for a long sequence of complete blocks; this is a prospective expectation, not a realized finite-list count.
- **Calculation or logical comparison reproduced:** Expected participant weights are 4×2/3=8/3 and 6×1/3=2; normalization total 14/3 yields size-four fraction 4/7=57.1429% and size-six fraction 3/7=42.8571%. Size-six is lower than size-four by 1/7=14.2857 percentage points. However 3/7 is higher than its block-selection probability 1/3 by 2/21=9.5238 percentage points.
- **Necessary inputs available:** Block sizes and selection probabilities; exact fractions permit both comparisons.
- **Exact missing inputs or definitions:** Whether “higher” compares six with four, or individual probability with the one-third probability of selecting a size-six block; no finite stopping rule/realized block composition is reported here.
- **Source-grounded alternative interpretation:** The wording can describe size bias relative to 1/3, which is numerically coherent. It need not claim six exceeds four. A stopped list also need not realize the long-run proportions exactly.
- **Direct observation versus inferred explanation:** Probabilities and unqualified comparative wording are direct; taking size-four as the comparator is registration's conditional interpretation. No allocation imbalance is observed.
- **Classification confirmed/corrected:** Numeric or arithmetic inconsistency; PLAN block law versus PLAN individual-probability wording, within each bound-version context; P_P; All relationships P_P; plan_material. No correction; retain explicit comparator ambiguity.
- **Evidence state:** recorded_candidate. Decisive fact: under the registered size-six-versus-size-four interpretation the ordering is contradicted, while the source leaves the alternative higher-than-block-probability comparator unstated. The mismatch remains conditional on that named missing definition.
- **Exact remaining human question:** Does “higher probability” mean higher than size-four membership or higher than the one-third block-selection probability, and should that comparator be stated?

## C037 — Hazard drug label attached to historical median

- **Location found:** Yes: [original SAP PDF p24, secondary outcome 2](../../../joi190092supp3_prod.pdf#page=24), [final SAP p65, secondary outcome 2](../../../joi190092supp3_prod.pdf#page=65).
- **Source value/text matched:** λC defined as methotrexate hazard, λI as mycophenolate mofetil hazard; historical median approximately 3.5 months attributed to mycophenolate; note sets λC=log(2)/3.5 months for the calculation. Visual inspection matched Greek subscripts that native text loses.
- **Comparator matched:** Yes: same-page hazard-arm definitions, historical median drug attribution and calculation note in each version. Numeric-tail and statistical-pass-1 duplicate provenance preserved as the same candidate (N656/N686 and S041/S066).
- **Consistency rule applicable:** A drug-specific median used to parameterize a drug-labeled exponential hazard should maintain the same named drug, unless an explicit planning re-assignment is stated.
- **Calculation or logical comparison reproduced:** log(2)/3.5=0.1980420516 per month. The historical median's source drug is MMF, which the preceding definition maps to λI; the note instead places the input in λC, labeled MTX. This reproduces the arm-attribution comparison, not the independent 2.47-month power claim.
- **Necessary inputs available:** Drug names, hazard-symbol definitions, median and parameter note. Symbol identity cannot be repaired by numerical rounding.
- **Exact missing inputs or definitions:** Whether the historical MMF median is intentionally reused as an MTX/control planning assumption, or hazard/drug labels were exchanged. No extra fitted hazard input is needed to see the attribution difference.
- **Source-grounded alternative interpretation:** A planning assumption may deliberately assign an MMF historical median to the control arm; symmetric power equations can leave some numeric power results unchanged after arm exchange. The page does not explicitly describe that re-assignment.
- **Direct observation versus inferred explanation:** The crossed printed drug/symbol attribution is direct. Intended control anchoring, copied drug label or exchanged symbol is an explanation; no observed survival result or power error is declared.
- **Classification confirmed/corrected:** Measure, label, or scale inconsistency; PLAN historical background input versus PLAN same-page prospective hazard definition/calculation; P_P; All relationships P_P; plan_material. No correction. Historical literature descriptions remain PLAN because they are supplied within planning content.
- **Evidence state:** recorded_candidate. Decisive fact: the historical MMF median is parameterized under the displayed MTX hazard symbol, with deliberate re-anchoring not specified.
- **Exact remaining human question:** Is the 3.5-month input intentionally assigned to MTX's λC despite its historical MMF attribution, or should its drug/symbol association differ?

## C038 — Rescue sequence/count and probability-index reversal

- **Location found:** Yes: [original SAP PDF p25, sequence index definition](../../../joi190092supp3_prod.pdf#page=25), [p26, enrollment/formula/probability definitions](../../../joi190092supp3_prod.pdf#page=26), [p27, power table/summary](../../../joi190092supp3_prod.pdf#page=27), [final SAP p66, assumptions and index](../../../joi190092supp3_prod.pdf#page=66), [p67, enrollment/formula/power headers](../../../joi190092supp3_prod.pdf#page=67), [p68, power rows/summary](../../../joi190092supp3_prod.pdf#page=68).
- **Source value/text matched:** Initial N0=108 per arm; r1=.9; initial A success .60, B success .40; r2=.95. Enrollment B/A=58.3, completion 55.4; A/B=38.9, completion 36.9. Index j0 means B rescue after A failure and j1 A rescue after B failure; prose n1=58,n0=38. Power headers A then B and B then A have main-row counts 58 and 38 respectively; probabilities B after A .42 and A after B .15, power 87%. Definitions p0=MTX rescue after MMF failure; p1=MMF rescue after MTX failure. Summary 58 Drug A/38 Drug B. Exact table cell positions and subscripts visually matched in both versions.
- **Comparator matched:** Yes for the sequence labels: A/B in enrollment means A first, B second, and A then B is the same sequence in the power table. Numeric-tail and statistical-pass-1 duplicate provenance retained (N659–N661/N693–N697 and S042/S073/S074/S076/S077/S078/S079/S080/S083).
- **Consistency rule applicable:** Sequence counts from unchanged initial success/retention assumptions should retain their A/B treatment-stage identity when moved to the table called the main scenario; linked n and p indices should keep one consistent sequence key.
- **Calculation or logical comparison reproduced:** A then B: 108×.9×(1−.60)=38.88→38.9 enrolling; multiplying .95 gives 36.936→36.9 completing. B then A: 108×.9×(1−.40)=58.32→58.3 enrolling; multiplying .95 gives 55.404→55.4 completing. Rounding enrollment down gives 38 for A then B and 58 for B then A; the first power row labels those sequences 58 and 38. The twenty-person reversal exceeds flooring/one-decimal tolerance. The j0/j1 and n0/n1 statements consistently link n0=38 to A→B and n1=58 to B→A; aligning p0/p1 with the table's MMF .42 rescue attribution reverses those sequence identities. This latter mapping is conditional on unchanged A/B drug identity, unlike the directly reproduced sequence-count reversal.
- **Necessary inputs available:** All numerical assumptions, enrollment/completion cells, sequence headers, index and probability definitions, and main-scenario statement. No observed rescue outcomes are needed. Reconstructing exact power is not required for the identity mismatch.
- **Exact missing inputs or definitions:** Whether A/B were deliberately recoded between enrollment and power sections; whether the power main scenario changed rather than copied the expected-enrollment scenario; and whether summary Drug A/B names initial or rescue treatment. No explicit recoding appears in these passages.
- **Source-grounded alternative interpretation:** Re-labeling A/B or choosing a different main sensitivity scenario can explain unequal count assignment. Summary 58 Drug A may mean rescue A, which agrees with B/A enrollment, rather than initial A; this ambiguity does not erase the power table's explicit “A, then B” sequence header. A .42 historical MMF probability supplies one side of the probability key but not a complete declared A/B recoding.
- **Direct observation versus inferred explanation:** Enrollment and power sequence headers/cells are direct. Same unchanged main scenario is an explicit alignment inference supported by the prose but bounded by absent recoding; an actual power failure or observed trial denominator error is not established.
- **Classification confirmed/corrected:** Denominator, proportion, or total inconsistency remains canonical because the concrete primary comparator is the twenty-person sequence-count reversal; preliminary label/scale provenance is retained. PLAN original/final rescue planning versus PLAN same-version power tables; P_P; All relationships P_P; plan_material. No role/type/category correction. All duplicate comparators are preserved; probability/index attribution is distinguished from the primary directly matched sequence counts.
- **Evidence state:** recorded_candidate. Decisive fact: both SAP versions print expected A→B enrollment 38.9 and B→A 58.3, then label the main power row A→B 58 and B→A 38, absent a declared recoding/change.
- **Exact remaining human question:** Which sequence receives 58 versus 38 in the main power scenario, were A/B deliberately redefined, and how should n0/p0 and n1/p1 and the summary's initial-versus-rescue drug labels be aligned?

## Mechanical field table for coordinator

| ID | Primary category | Relationship type | All relationships | Compared document roles | Evidence state |
|---|---|---|---|---|---|
| C021 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN original protocol p11 timeline rows vs PLAN same rows | recorded_candidate |
| C022 | Measure, label, or scale inconsistency | P_P | P_P | PLAN original protocol p16 non-serious vs PLAN serious leukocyte thresholds | recorded_candidate |
| C023 | Measure, label, or scale inconsistency | P_P | P_P | PLAN original protocol p16 non-serious vs PLAN serious platelet thresholds | recorded_candidate |
| C024 | Measure, label, or scale inconsistency | P_P | P_P | PLAN original protocol p16 AST/ALT table vs PLAN pp52–53 adverse-event prose | recorded_candidate |
| C025 | Measure, label, or scale inconsistency | P_P | P_P | PLAN original protocol p22 same-drug taper label vs PLAN pp9,26–27 phase definitions | recorded_candidate |
| C026 | Measure, label, or scale inconsistency | P_P | P_P | PLAN original protocol pp26–27 window headers vs PLAN same-table day cells | recorded_candidate |
| C027 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN original protocol p26 M6-I window vs PLAN p27 M6-I window | recorded_candidate |
| C028 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol pp43,124 first-line count vs PLAN pp44,125 five-letter-line definition | recorded_candidate |
| C029 | Measure, label, or scale inconsistency | P_P | P_P | PLAN protocol pp42–44,123–125 testing triggers vs PLAN scoring/analysis triggers | record_input_error |
| C030 | Measure, label, or scale inconsistency | P_P | P_P | PLAN protocol pp45,127 grade zero vs PLAN same-table grade 0.5+ | recorded_candidate |
| C031 | Measure, label, or scale inconsistency | P_P | P_P | PLAN original protocol p16 WBC unit vs PLAN p53 unitless example | recorded_candidate |
| C032 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN final protocol p86 full maintenance dose vs PLAN p87 bottle content/duration | recorded_candidate |
| C033 | Measure, label, or scale inconsistency | P_P | P_P | PLAN final protocol p103 Chart R identifier vs PLAN p110 Chart R identifier | record_input_error |
| C034 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN final protocol p115 guide and p117 retest vs PLAN p117 subsequent lens conditional | recorded_candidate |
| C035 | Measure, label, or scale inconsistency | P_P | P_P | PLAN final protocol p125 grade standard and p126 figure vs PLAN p126 category prose | recorded_candidate |
| C036 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN original SAP pp9–10/final p50 block law vs PLAN individual-probability wording | recorded_candidate |
| C037 | Measure, label, or scale inconsistency | P_P | P_P | PLAN original SAP p24/final p65 historical MMF median vs PLAN same-page MTX hazard symbol | recorded_candidate |
| C038 | Denominator, proportion, or total inconsistency | P_P | P_P | PLAN original SAP pp25–27/final pp66–68 enrollment sequence counts vs PLAN power-table sequence/index labels | recorded_candidate |

Completed: 18/18 assigned IDs. States: 16 recorded_candidate, 2 record_input_error. No extraction gap. Remaining limitations are named within each card: interval inclusion/precedence, visit/phase alignment, testing-versus-encoding selection, omitted WBC scale, package-versus-bottle meaning, chart calibration/outcome-scale relevance, unnamed probability comparator, and planning-arm/sequence recoding. No candidate ID was removed, merged or renumbered during recheck.


# Mechanical evidence recheck: C039–C057

Assigned scope: C039, C040, C041, C042, C043, C044, C045, C046, C047, C048, C049, C050, C051, C052, C053, C054, C055, C056, C057. All 19 IDs were rechecked separately. Each remains Pending Human Adjudication. Evidence states describe the record, not an adjudication.

Authority and engines: direct supplied PDFs; fresh Poppler 26.01.0 `pdftotext -layout -f N -l N` derivatives `preprocessing/recheck_cross_stats_main_N.txt` for main pages 4,6,7,8; `recheck_cross_stats_results_N.txt` for results pages 5,6,11,12,14,15; `recheck_cross_stats_protocol_N.txt` for protocol pages 81,136; and `recheck_cross_stats_sap_N.txt` for SAP pages 16,17,18,26,27,31,46,57,58,60,61,67,68,71. Protocol pages 81 and 136 have unusable native text and were read visually from current-run source page rasters `protocol_middle_p81.png` and `plan_tail_protocol_136.png`. Source-linked current-run main page 8 raster `numeric_main_p008.png` was also read. Fresh direct Poppler `pdftoppm -r 100 -f N -l N -singlefile -png` source rasters `recheck_cross_stats_results_N.png` for pages 5,6,14,15 and `recheck_cross_stats_sap_N.png` for pages 16,17,58,61,67,68 were read visually. Mathematical signs in rasters govern over the text derivatives. All new derivatives are below review_1_6/preprocessing; no source or reused asset was modified. CPU-only R 4.5.2 reproduced C050/C052/C057 calculations using `preprocessing/recheck_cross_stats_calculations.R`, with results in `preprocessing/recheck_cross_stats_calculations.txt`; R was auxiliary arithmetic, not scientific orchestration.

Role assignments are content-based: main article and result eTables are REPORT; prospective protocol/manual and original/final SAP versions are PLAN. No plan that merely corroborates one side adds a discrepancy relationship.

## C039 — Six-month numbness/tingling counts and unresolved field identity

- **Location found:** Yes: REPORT [main p8 Table 3](../../../jama_rathinam_2019_oi_190092.pdf#page=8) and REPORT [results p12 eTable 6](../../../joi190092supp1_prod.pdf#page=12).
- **Source value/text matched:** Main nonserious systemic “Numbness or tingling” is MTX 25 (23.4%), MMF 18 (16.7%), under patients reporting at least one adverse event at six months.
- **Comparator matched:** eTable 6, “Six-Month Patient-Reported Other Systemic Adverse Events,” prints “Numbness/tingling” 13 (12.1%)/11 (10.2%), with N107/N108 and patients reporting at least one event.
- **Consistency rule applicable:** Same-variable, same-period, same-patient-stream counts should match; however, same-variable identity is not established by similar labels. The explicit “Other Systemic” title supports a distinct response stream as a possible interpretation.
- **Calculation/logical comparison reproduced:** Printed differences are 25−13=12 and 18−11=7. This is an observed count difference, but does not reproduce an unconditional same-variable inconsistency.
- **Necessary inputs available:** Counts, arms, six-month period and patient-level rather than event-level measure are available.
- **Exact missing inputs/definitions:** Field IDs, structured-versus-additional symptom provenance, aggregation and deduplication rules, and a crosswalk showing whether both rows represent the same safety variable.
- **Source-grounded alternative interpretation:** Main Table 3 may summarize the neurologic-function checklist item (eTable 1 p6 defines it as numbness or tingling), while eTable 6 explicitly summarizes patient-reported other systemic events. Different streams can yield different counts without numeric error.
- **Direct observation versus inferred explanation:** Counts and titles are observed; common-field identity and a specific data-collection mechanism are inferred and unconfirmed.
- **Exact remaining human question:** Do these rows share a field and aggregation rule, or do 25/18 and 13/11 summarize different questionnaire/event streams?
- **Classification:** Primary category Cross-document numeric inconsistency; primary S_C; all S_C; REPORT main p8 versus REPORT results p12. No role or relationship correction.
- **Evidence state:** `record_input_error`. Decisive fact: the registered comparison relies on unsupported field alignment; the package does not settle whether a residual same-variable mismatch exists. This does not erase the directly observed count difference.

## C040 — Mood counts and unresolved union membership

- **Location found:** Yes: REPORT [main p8 Table 3](../../../jama_rathinam_2019_oi_190092.pdf#page=8), REPORT [results p11 eTable 5](../../../joi190092supp1_prod.pdf#page=11).
- **Source value/text matched:** “Mood changes (self-reported, not requiring therapy)” 33 (30.8%)/26 (24.1%).
- **Comparator matched:** “Six-Month Patient-Reported Mood-Related Adverse Events,” “Any mood-related adverse event” 22 (20.6%)/19 (17.6%), N107/N108, counts of patients reporting at least one event.
- **Consistency rule applicable:** A subset cannot exceed its union, but the main checklist item must first be shown to belong to this specific appendix union. That inclusion is not printed.
- **Calculation/logical comparison reproduced:** 33>22 by 11 and 26>19 by 7. No overlapping subrow sum was used. A conditional set-containment problem exists if the main row belongs to the appendix union; unconditional membership is unestablished.
- **Necessary inputs available:** Arm, period, patient count, appendix union label and main nonserious mood label.
- **Exact missing inputs/definitions:** Questionnaire-field crosswalk, whether “Any” includes the structured mood-change item or only additional mood descriptions, and the union/deduplication algorithm.
- **Source-grounded alternative interpretation:** The appendix's detailed patient-reported symptom taxonomy may summarize a separate additional-response field, while main Table 3 uses the mood-change checklist category defined in eTable 1 p6.
- **Direct observation versus inferred explanation:** The two count pairs and labels are observed; subset membership and separate-stream mechanisms are inferences.
- **Exact remaining human question:** Does eTable 5 “Any” include the main structured mood item, and what fields and union rule produced 33/26 versus 22/19?
- **Classification:** Denominator, proportion, or total inconsistency; S_C; all S_C; REPORT main p8 versus REPORT results p11. No correction to category or relationships.
- **Evidence state:** `record_input_error`. Decisive fact: union membership required by the registered set rule is an unsupported alignment assumption and cannot be settled from supplied definitions.

## C041 — Creatinine lower-bound inequality

- **Location found:** Yes: REPORT [main p8](../../../jama_rathinam_2019_oi_190092.pdf#page=8), REPORT [results p5 eTable 1](../../../joi190092supp1_prod.pdf#page=5), PLAN [protocol p81 Table 3](../../../joi190092supp2_prod.pdf#page=81) and [p136 §6.1](../../../joi190092supp2_prod.pdf#page=136), with inequalities visually confirmed.
- **Source value/text matched:** Main nonserious creatinine “>1.5 to <2 mg/dL lasting <28 d,” counts 1/0.
- **Comparator matched:** Results definition and both plan locations use ≥1.5 to <2 mg/dL.
- **Consistency rule applicable:** Strict and inclusive inequalities classify exactly 1.5 differently; same numeric unit, adverse-event category and persistence condition are matched.
- **Calculation/logical comparison reproduced:** 1.5 satisfies x≥1.5 and does not satisfy x>1.5. The label mismatch is reproduced.
- **Necessary inputs available:** Printed lower/upper boundaries, mg/dL, <28-day rule and report counts.
- **Exact missing inputs/definitions:** Exact-boundary laboratory observations, implemented coding, and any later amended threshold; these are needed only to determine count consequences.
- **Source-grounded alternative interpretation:** Main row may abbreviate an inclusive implemented boundary, or an unprovided amended rule may exist.
- **Direct observation versus inferred explanation:** Inequalities differ directly; any changed count or production mechanism is not observed.
- **Exact remaining human question:** Was exactly 1.5 classified using the inclusive definition, and does the article label reflect the implemented rule?
- **Classification:** Measure, label, or scale inconsistency; P_R; all P_R, S_C. REPORT main differs from PLAN and REPORT results; the latter is a genuine report-report comparator.
- **Evidence state:** `recorded_candidate`, determined by the visually confirmed > versus ≥ boundary.

## C042 — Fever temperature cutpoint

- **Location found:** Yes: REPORT [main p8](../../../jama_rathinam_2019_oi_190092.pdf#page=8), REPORT [results p6 definition](../../../joi190092supp1_prod.pdf#page=6), [p14](../../../joi190092supp1_prod.pdf#page=14), [p15](../../../joi190092supp1_prod.pdf#page=15).
- **Source value/text matched:** Main “Fever <39°C for 12 h,” 11/18 patients.
- **Comparator matched:** p6 nonserious fever for 12 hours “>100.6 to 103°F/39.5°C”; serious ≥103°F/39.5°C. pp14–15 label fever <103 degrees for 12 hours; their six-to-twelve-month counts are not compared to six-month counts.
- **Consistency rule applicable:** Matched category definitions use different temperature boundaries even when periods of observed events differ.
- **Calculation/logical comparison reproduced:** (103−32)×5/9=39.4444°C; 39°C converts to 102.2°F. Thus the printed 39°C boundary differs from the appendix 103°F/39.5°C category definition.
- **Necessary inputs available:** Units, numeric thresholds, duration and category labels.
- **Exact missing inputs/definitions:** Whether main integer 39 was intended as a coarse abbreviation, actual coding boundary and any amended definition; observations near the boundary are needed for count impact.
- **Source-grounded alternative interpretation:** Main may coarsely shorten 39.5 to 39 or label a different threshold; neither is explicitly explained.
- **Direct observation versus inferred explanation:** Labels and conversion are direct/derived facts; individual reclassification is unobserved.
- **Exact remaining human question:** What temperature cutpoint and inequality generated the six-month 11/18 counts, and what was intended by “<39°C”?
- **Classification:** Measure, label, or scale inconsistency; S_C; all S_C; REPORT main versus REPORT results. The appendix's own ≤/strict boundary topic remains a separate candidate.
- **Evidence state:** `recorded_candidate`, determined by the different displayed category cutpoints.

## C043 — Hemoglobin boundary with corrected supplement transcription

- **Location found:** Yes: REPORT [main p8](../../../jama_rathinam_2019_oi_190092.pdf#page=8), REPORT [results p5](../../../joi190092supp1_prod.pdf#page=5), [p14](../../../joi190092supp1_prod.pdf#page=14), [p15](../../../joi190092supp1_prod.pdf#page=15), PLAN [protocol p81](../../../joi190092supp2_prod.pdf#page=81), all visually inspected.
- **Source value/text matched:** Main low hemoglobin >6.5 to <9 g/dL for <28 days, 2/3 patients; results pp14–15 also use >6.5.
- **Comparator matched:** Direct raster p5 eTable 1 reads **≥6.5 to <9**, not >6.5; its serious definition is <6.5 or persistent <9. PLAN p81 likewise reads ≥6.5 to <9 with serious <6.5. Fresh native extraction incorrectly loses the underline in ≥ and cannot govern transcription.
- **Consistency rule applicable:** Exactly 6.5 for less than 28 days belongs to the inclusive nonserious definition, but not the strict row labels.
- **Calculation/logical comparison reproduced:** x=6.5 satisfies ≥6.5 and fails >6.5. Main/plan mismatch remains; corrected p5 adds main-versus-supplement and supplement-internal definition-versus-later-label comparisons.
- **Necessary inputs available:** Boundary values, units, duration, direct images and main/later result labels.
- **Exact missing inputs/definitions:** Actual laboratory coding and exact-boundary observations; whether strict labels are shorthand or an amendment.
- **Source-grounded alternative interpretation:** Implemented categories may consistently use ≥6.5, with strict > retained only in result-row labels. No count change is inferable.
- **Direct observation versus inferred explanation:** The p5 ≥ symbol and main/later > symbols are observed; a label-production explanation remains inferred.
- **Exact remaining human question:** Was exactly 6.5 included in nonserious counts, and why do main/later rows differ from the inclusive definition?
- **Classification:** Measure, label, or scale inconsistency; P_R; **all P_R, S_C, S_W**. REPORT main and later supplement rows differ from PLAN p81; REPORT main p8 differs from REPORT results p5; within REPORT results p5 differs from pp14–15. Correction: p5 is inclusive and corroborates PLAN, but becomes a substantive comparator against the strict report labels. Primary precedence remains P_R.
- **Evidence state:** `recorded_candidate`. The original p5 transcription is disproven, but the registered main-versus-plan boundary mismatch remains directly reproduced; its exact-boundary question is unchanged rather than a new residual question.

## C044 — Leukocyte boundary reconciles after visual glyph correction

- **Location found:** Yes: REPORT [results p5](../../../joi190092supp1_prod.pdf#page=5), PLAN [protocol p81](../../../joi190092supp2_prod.pdf#page=81); REPORT [main p8](../../../jama_rathinam_2019_oi_190092.pdf#page=8) supplies the nonserious row only.
- **Source value/text matched:** Direct source raster eTable 1 serious acute leukocyte boundary reads **≤1,000/µL**, not the registered <1,000. Native text loses the underline. Nonserious is >1,000 and <2,500 lasting <28 days.
- **Comparator matched:** PLAN serious ≤1,000; nonserious >1,000 to <2,500. Persistent low counts are also described; the main nonserious row does not contradict this rule.
- **Consistency rule applicable:** Compare the actual strict/inclusive category boundaries at exactly 1,000.
- **Calculation/logical comparison reproduced:** At x=1,000 both REPORT and PLAN classify acute counts as serious; neither nonserious category includes x=1,000. Registered discrepancy is explicitly disproven.
- **Necessary inputs available:** Both exact source inequalities, same cells/µL units and duration conditions.
- **Exact missing inputs/definitions:** None needed to settle this registered printed-boundary comparison; patient-level laboratory values are unnecessary.
- **Source-grounded alternative interpretation:** The registered < arose from failed text extraction of ≤; the source itself reconciles.
- **Direct observation versus inferred explanation:** ≤ in both source images is observed. Extraction glyph loss is evidenced by the native derivative, without making an inference about author intent.
- **Exact remaining human question:** No boundary-consistency question remains for these compared locations; human review can inspect the ≤ glyph and retained record.
- **Classification:** Measure, label, or scale inconsistency; P_R; all P_R; REPORT results p5 versus PLAN p81. Relationship describes the registered comparison even though its evidence state changes; no extra relationship from the corroborating main nonserious row.
- **Evidence state:** `not_reproduced`, determined by direct source ≤1,000 matching PLAN ≤1,000 and disproving the registered < comparator.

## C045 — ALT/AST five-times-ULN boundary

- **Location found:** Yes: REPORT [main p8](../../../jama_rathinam_2019_oi_190092.pdf#page=8), [results p5](../../../joi190092supp1_prod.pdf#page=5), [p14](../../../joi190092supp1_prod.pdf#page=14); PLAN [protocol p81](../../../joi190092supp2_prod.pdf#page=81), [p136](../../../joi190092supp2_prod.pdf#page=136), visually inspected.
- **Source value/text matched:** Main and results define nonserious 2 to 5 times ULN for <28 days and serious >5 times ULN, or persistent 2 to 5. Main counts 14/8 nonserious and 3/2 serious; later supplement counts concern a different period.
- **Comparator matched:** PLAN nonserious 2 to <5 and serious ≥5, in both table and adverse-event prose. All relevant strict/inclusive symbols visually match this reading.
- **Consistency rule applicable:** If printed “2 to 5” includes its upper endpoint, exactly 5 for <28 days is nonserious under REPORT and serious under PLAN; REPORT serious >5 definitely excludes exactly 5.
- **Calculation/logical comparison reproduced:** x=5 satisfies PLAN ≥5 and fails REPORT >5. Persistence ≥28 days is a separate coherent route and does not resolve an acute exact-5 boundary.
- **Necessary inputs available:** ULN scale, numerical boundaries and persistence labels.
- **Exact missing inputs/definitions:** Implemented inclusivity of “2 to 5,” laboratory code, exact-boundary observations, and any rule amendment.
- **Source-grounded alternative interpretation:** Report labels may compress a half-open 2-to-<5 interval, with >5 serious itself an abbreviated ≥5 label; or a distinct implemented boundary was used.
- **Direct observation versus inferred explanation:** Printed ≥5 versus >5 is directly observed; proposed coding and count impacts are unobserved.
- **Exact remaining human question:** How was exactly 5×ULN classified before 28 days, and do the result-row boundaries describe that code?
- **Classification:** Measure, label, or scale inconsistency; P_R; all P_R. REPORT locations agree with one another on their printed boundaries; PLAN locations agree with one another, so neither S_C nor P_P is added.
- **Evidence state:** `recorded_candidate`, determined by directly different plan/report exact-5 serious boundaries.

## C046 — Per-protocol adherence definition

- **Location found:** Yes: REPORT [main p6 narrative](../../../jama_rathinam_2019_oi_190092.pdf#page=6), [p7 Figure 2 model 4 and footnote e](../../../jama_rathinam_2019_oi_190092.pdf#page=7), PLAN [original SAP p31](../../../joi190092supp3_prod.pdf#page=31), [final SAP p71 §4.1](../../../joi190092supp3_prod.pdf#page=71).
- **Source value/text matched:** Report “Per protocol” includes missed less than 20% of doses, n184, 61/90 versus 54/94, OR1.56 (0.84–2.96), P=.17.
- **Comparator matched:** Both SAP versions exclude major deviations or noncompliance defined as less than 50% of study drug received by self report or pill counts at study visits.
- **Consistency rule applicable:** Complementary missed/received percentages under the same expected-dose basis give distinct adherence cutoffs for this named numerical sensitivity result.
- **Calculation/logical comparison reproduced:** <20% missed implies >80% received; exclusion of <50% received permits ≥50% on that criterion. A participant receiving 70% passes the latter and fails the former. 90+94=184 matches the report population.
- **Necessary inputs available:** Labels, thresholds, n184 and its arm counts; the result concretely links the population mismatch to numbers.
- **Exact missing inputs/definitions:** Participant exclusions, equivalence of adherence denominators, major-deviation handling and whether model 4 implements SAP per-protocol or an additional sensitivity subset.
- **Source-grounded alternative interpretation:** A stricter adherent-subset sensitivity may intentionally be reported under a broad “per protocol” label.
- **Direct observation versus inferred explanation:** Cutoffs differ as printed; differences in which actual people were included and consequent estimates are not reconstructed.
- **Exact remaining human question:** Was n184 intended as the SAP per-protocol population or a separate >80%-received sensitivity population, and what participant inclusion rule was used?
- **Classification:** Analysis-unit or population inconsistency; P_R; all P_R; REPORT main versus PLAN SAP. Original/final SAP agree, so no P_P.
- **Evidence state:** `recorded_candidate`, determined by different explicit adherence rules attached to the named population/result.

## C047 — Report noninferiority interpretation versus plan criterion

- **Location found:** Yes: REPORT [main p4](../../../jama_rathinam_2019_oi_190092.pdf#page=4), PLAN [final SAP p61 item 16](../../../joi190092supp3_prod.pdf#page=61), plan clause visually confirmed.
- **Source value/text matched:** Main MTX−MMF risk difference 9.5%, CI −5.3% to 21.8%, and lower bound −5.3 excludes the prespecified 10% margin, giving evidence of MTX noninferiority.
- **Comparator matched:** SAP states MTX noninferior if the lower limit of the 95% CI for treatment success at six months is “less than 10%”; one-sided comparison and 10% margin are stated, but the exact signed contrast is not.
- **Consistency rule applicable:** For the REPORT MTX−MMF contrast and 10-point allowable loss, a lower bound above −10% excludes such loss; a lower bound <+10% is a different criterion. This compares formal rule wording, not merely whether the actual −5.3 satisfies both inequalities.
- **Calculation/logical comparison reproduced:** −5.3>−10; a hypothetical lower bound −50 would also satisfy the printed <+10 rule while permitting a loss beyond the margin. A reverse MMF−MTX contrast would require an upper loss bound rather than the written lower bound.
- **Necessary inputs available:** Report orientation, observed CI, plan margin, lower-bound name and less-than direction.
- **Exact missing inputs/definitions:** Signed NI estimand in the plan, intended endpoint/direction, original test specification and any amendment.
- **Source-grounded alternative interpretation:** A sign, inequality or bound-name transcription in the plan, or an unprovided amended decision rule, could explain the different formal wording.
- **Direct observation versus inferred explanation:** Both decision statements and observed interval are read directly; intended formal NI rule is not inferred as fact.
- **Exact remaining human question:** Which signed contrast, bound, inequality and margin sign were prespecified and used to interpret the −5.3% bound?
- **Classification:** Statistical reporting inconsistency; P_R; all P_R; REPORT main p4 versus PLAN final SAP p61. C051 uses a different plan-internal comparator and remains separate.
- **Evidence state:** `recorded_candidate`, determined by the directly different formal decision-rule wording, conditional on the explicitly missing plan estimand.

## C048 — Rescue-success OR model description

- **Location found:** Yes: REPORT [main p4 methods](../../../jama_rathinam_2019_oi_190092.pdf#page=4), [p6 Table 2 OR header/footnote b and switched row](../../../jama_rathinam_2019_oi_190092.pdf#page=6), [p7 narrative](../../../jama_rathinam_2019_oi_190092.pdf#page=7); PLAN [final SAP p61 Specific Aim 2](../../../joi190092supp3_prod.pdf#page=61).
- **Source value/text matched:** Report applies the same primary logistic model at 12 months; table OR footnote b specifies treatment fixed and study site random. Switched-drug success is 20/29 versus 7/20, OR4.17 (1.32–13.16), P=.02; p7 rounded OR4.2 is coherent.
- **Comparator matched:** Aim 2 primary rescue logistic predictors are treatment group and reason for failure of the first drug, lack of efficacy versus any other reason.
- **Consistency rule applicable:** Printed adjustment/model labels for the same rescue-success result can be compared; site and failure-reason adjustment are different described structures. Unknown realized design matrices cannot be equated or reconstructed from marginal counts.
- **Calculation/logical comparison reproduced:** The REPORT label omits the PLAN failure-reason predictor and describes site random effects. No adjusted OR was recomputed; equality or inequality of actual coefficients is not established.
- **Necessary inputs available:** Exact rescue outcome, new-treatment contrast, table result, report model label and plan predictors.
- **Exact missing inputs/definitions:** Actual rescue design matrix, included covariates, site-effect implementation, model output and any disclosed change applying to this result.
- **Source-grounded alternative interpretation:** Failure reason may have been included but omitted from the compressed label; report may give a supplementary or amended rescue model.
- **Direct observation versus inferred explanation:** The labels differ directly; omission from the actual fitted model and consequent OR change are not observed.
- **Exact remaining human question:** Did the model producing OR4.17 include failure reason, site random effects, both or another structure, and how does it relate to the planned Aim 2 primary analysis?
- **Classification:** Statistical reporting inconsistency; P_R; all P_R; REPORT main versus PLAN final SAP. No report-internal mismatch from the coherently rounded p7 result.
- **Evidence state:** `recorded_candidate`, determined by a reproduced model-description mismatch with actual fitted covariates explicitly unavailable.

## C049 — Dose-reduction Fisher versus logistic test label

- **Location found:** Yes: REPORT [main p4 methods](../../../jama_rathinam_2019_oi_190092.pdf#page=4), [p6 result](../../../jama_rathinam_2019_oi_190092.pdf#page=6), PLAN [final SAP p61 item 15](../../../joi190092supp3_prod.pdf#page=61).
- **Source value/text matched:** Report states dose reductions compared using Fisher exact test; 21 (19.6%) MTX versus 15 (13.8%) MMF, P=.27.
- **Comparator matched:** Plan states dose reduction compared by arm using logistic regression based on treatment and other covariates as needed.
- **Consistency rule applicable:** These are distinct explicitly named inferential procedures for the same dose-reduction arm comparison.
- **Calculation/logical comparison reproduced:** Fisher exact comparison is not the named logistic-regression coefficient inference. The plan's Fisher provision for major protocol deviations does not redefine its separate dose-reduction item.
- **Necessary inputs available:** Outcome, arm comparison, report result and both test labels.
- **Exact missing inputs/definitions:** Actual analysis call, amendment or supplementary-analysis designation, and whether logistic comparison was separately conducted.
- **Source-grounded alternative interpretation:** Report could intentionally describe an unadjusted supplementary Fisher comparison or an amended analysis.
- **Direct observation versus inferred explanation:** Test names differ directly; actual analysis amendment or omission of planned analysis is unproven.
- **Exact remaining human question:** What test generated P=.27, and was the logistic comparison replaced, separately performed or represented only by this supplementary result?
- **Classification:** Statistical reporting inconsistency; P_R; all P_R; REPORT main versus PLAN final SAP. C057 compares the numerical Fisher output/printing precision, a distinct comparator.
- **Evidence state:** `recorded_candidate`, determined by the two directly different test descriptions.

## C050 — Missed-dose mean/SD versus Welch P

- **Location found:** Yes: REPORT [main p4 methods](../../../jama_rathinam_2019_oi_190092.pdf#page=4), [p6 Table 2 and narrative](../../../jama_rathinam_2019_oi_190092.pdf#page=6).
- **Source value/text matched:** Table and narrative both label mean (SD) missed-dose percentages 4.6 (1.0) versus 4.3 (0.5), P=.87.
- **Comparator matched:** Methods say missed doses compared by Welch t test and significance assessed with two-sided P. Table patient headers n96/n98 are not an explicit adherence-test sample size.
- **Consistency rule applicable:** A participant-level two-sample Welch test of the same means and SDs must satisfy its mean/SD/sample-size identity; the conservative check only requires each sample size ≥2 for a sample SD.
- **Calculation/logical comparison reproduced:** Under nearest-tenth summary rounding, mean difference ≥0.20 and SDs ≤1.05 and ≤0.55. Consequently absolute t ≥0.20/sqrt((1.05²+0.55²)/2)=0.238619994509. Welch degrees of freedom ≥1 because its variance-component denominator cannot exceed the square of their sum. The conservative df1 two-sided P bound is 0.850878358724, reproduced by R `2*pt(-t_bound,df=1)`; .87 requires ≥.865 under nearest-hundredth P rounding. Thus these same participant-level summaries cannot yield the attached .87 under the declared Welch rule. No n96/n98 assumption was used.
- **Necessary inputs available:** Mean values, dispersion numbers explicitly labeled SD, Welch definition and attached P.
- **Exact missing inputs/definitions:** Exact adherence variable, sample sizes, whether dispersion is truly SD rather than SE, unrounded summaries, transformation and printing conventions.
- **Source-grounded alternative interpretation:** Dispersion could have been SE, or the test could concern raw counts/transformed observations while different summaries were printed. Different actual n alone cannot resolve the conservative same-summary bound.
- **Direct observation versus inferred explanation:** Means/SD labels/P/test are observed; the bound is a diagnostic derived from those labels. Any alternative variable or mistaken label is unconfirmed.
- **Exact remaining human question:** Which variable and analysis-set n entered the Welch test, are 1.0/0.5 SD or SE, and is P=.87 attached to those same summaries?
- **Classification:** Statistical reporting inconsistency; S_W; all S_W; REPORT main p4 versus REPORT main p6.
- **Evidence state:** `recorded_candidate`, determined by the reproduced conservative bound under the same-summary and stated-label interpretation; named missing definitions remain explicit.

## C051 — Plan-internal noninferiority decision rule

- **Location found:** Yes: PLAN [final SAP p61 item 16](../../../joi190092supp3_prod.pdf#page=61), [p46 comparative aim](../../../joi190092supp3_prod.pdf#page=46), [p57 coding](../../../joi190092supp3_prod.pdf#page=57).
- **Source value/text matched:** MTX noninferior if lower limit of 95% CI for six-month treatment success is less than 10%, with a 10% margin; direct raster confirms “less than.”
- **Comparator matched:** Plan aim compares success fraction MMF versus MTX; p57 codes MTX=0 and MMF=1, success=1, establishing a comparative rather than absolute-success objective, while item 16 does not explicitly define its contrast.
- **Consistency rule applicable:** A comparative allowable-loss NI criterion must restrict the appropriate confidence bound. Lower<+10 does not enforce a 10-point bound on loss of MTX success for the common contrasts implied by the plan.
- **Calculation/logical comparison reproduced:** For MTX−MMF, arbitrarily negative lower bounds satisfy lower<+10 despite permitting losses >10. For MMF−MTX loss, an upper bound is relevant. For MTX success alone, lower<10 does not establish comparative loss. These logical counterexamples reproduce the plan-internal rule question without report evidence.
- **Necessary inputs available:** Margin, group comparison, coding, confidence-bound endpoint and inequality.
- **Exact missing inputs/definitions:** NI estimand, sign, signed margin, intended bound endpoint and formal test.
- **Source-grounded alternative interpretation:** Clause may have a sign/direction/bound-name transcription defect or refer to an unprovided signed loss estimand.
- **Direct observation versus inferred explanation:** Printed wording/coding are observed; hypothetical counterexamples are diagnostic, not trial data; intended amended rule is unknown.
- **Exact remaining human question:** What contrast/quantity, signed boundary, confidence endpoint and inequality were intended for this exact plan criterion?
- **Classification:** Statistical reporting inconsistency; P_P; all P_P; PLAN final SAP p61 versus PLAN final SAP pp46/57. REPORT is context only here; C047 separately compares REPORT to PLAN.
- **Evidence state:** `recorded_candidate`, determined by the printed plan-internal comparative-rule question with its missing estimand stated.

## C052 — Detectable rescue difference 17 versus 25 points

- **Location found:** Yes: PLAN [original SAP p26 prose/formula](../../../joi190092supp3_prod.pdf#page=26), [p27 power table/summary](../../../joi190092supp3_prod.pdf#page=27), [final SAP p67](../../../joi190092supp3_prod.pdf#page=67), [p68](../../../joi190092supp3_prod.pdf#page=68); final formula and table read visually.
- **Source value/text matched:** Prose says approximately 80% power to detect a difference of 17% when MMF success is .42.
- **Comparator matched:** 80% row .42/.17, n1=58/n0=38; summary says difference 25%, success probability 42%, same sample counts and two-tailed alpha .05.
- **Consistency rule applicable:** Absolute difference in two probabilities is their subtraction, distinct from either lower success probability. The displayed normal-CDF power formula permits an auxiliary scenario check.
- **Calculation/logical comparison reproduced:** .42−.17=.25, or 25 points. R reproduces source-formula power 0.802453166564 for .42/.17; literal 17-point difference .42/.25 gives 0.428097397721 under the same formula/counts. This diagnostic does not repair sequence alignment, separately registered elsewhere.
- **Necessary inputs available:** Explicit success probabilities, scenario counts, formula, alpha and prose/summary comparison.
- **Exact missing inputs/definitions:** Whether “difference 17%” means the lower success probability or a distinct omitted scenario; author-intended scenario alignment.
- **Source-grounded alternative interpretation:** 17% may name the lower-group probability rather than the difference; an unprinted alternative scenario could explain the prose.
- **Direct observation versus inferred explanation:** 17%, 25%, .42/.17 and table labels are observed; the suggested prose intent is inference. Powers are source-formula diagnostics, not observed trial inference.
- **Exact remaining human question:** Does 17% denote lower success probability or an absolute detectable difference, and which scenario did the prose intend?
- **Classification:** Numeric or arithmetic inconsistency; P_P; all P_P; PLAN original/final SAP prose versus PLAN table/summary. Historical planning values remain PLAN.
- **Evidence state:** `recorded_candidate`, determined by reproduced .42−.17=.25 and the conflicting printed difference descriptions.

## C053 — Country-interaction coefficient absent from named equation

- **Location found:** Yes: PLAN [original SAP p16 Equation 1](../../../joi190092supp3_prod.pdf#page=16), [p17 first paragraph](../../../joi190092supp3_prod.pdf#page=17), both visually inspected.
- **Source value/text matched:** Equation 1 contains intercept, treatment b1 and site terms b2i/b3i/b4i; null b1=0 with one-df LRT. It has no country-by-treatment b12 term.
- **Comparator matched:** Next page explicitly calls Wald T-test of b12=0 “in Equation (1)” for treatment-country interaction. The visual source confirms b12, not b1.
- **Consistency rule applicable:** A test coefficient assigned to an identified displayed equation must exist in that equation or a supplied equivalent parameterization.
- **Calculation/logical comparison reproduced:** Comparing the displayed term list to b12 shows no b12 or interaction term. Exploratory model (d) has country interaction but is not labeled Equation 1.
- **Necessary inputs available:** Displayed model, coefficient list, test coefficient, named equation and model descriptions.
- **Exact missing inputs/definitions:** Equation/model actually intended for b12 and its coefficient mapping.
- **Source-grounded alternative interpretation:** The test may intend exploratory model (d), or an omitted interaction term/model reference.
- **Direct observation versus inferred explanation:** Absence of b12 from printed Equation 1 is observed; intended model substitution is inferred.
- **Exact remaining human question:** Which supplied model and coefficient define the country-interaction test called b12 in Equation 1?
- **Classification:** Statistical reporting inconsistency; P_P; all P_P; PLAN original SAP equation versus PLAN next-page test statement.
- **Evidence state:** `recorded_candidate`, determined by the directly reproduced equation/coefficient identity mismatch.

## C054 — Zero interaction null and stated difference

- **Location found:** Yes: PLAN [original SAP p17](../../../joi190092supp3_prod.pdf#page=17), [final SAP p58](../../../joi190092supp3_prod.pdf#page=58), exact formulas visually confirmed.
- **Source value/text matched:** Anatomical term β3X3 and interaction β13X1X3 are added; the hypothesis is β13=0.
- **Comparator matched:** Both passages immediately explain this as “i.e. that there is a difference in treatment efficacy between the anatomic locations, controlling for country.” X3 codes the two anatomical groups 0/1.
- **Consistency rule applicable:** In this supplied interaction parameterization, a zero interaction means no difference in the treatment log-odds coefficient between X3=0 and X3=1.
- **Calculation/logical comparison reproduced:** Treatment coefficient is β1 for X3=0 and β1+β13 for X3=1; their difference is β13, zero under the named null. The “i.e.” statement describes a nonzero alternative instead.
- **Necessary inputs available:** Coding, added terms, zero hypothesis and interpretation.
- **Exact missing inputs/definitions:** Intended null-versus-alternative meaning of the explanatory prose; no fitted interaction output needed.
- **Source-grounded alternative interpretation:** Prose may intend “test whether there is a difference” or describe the alternative rather than equate it to the null.
- **Direct observation versus inferred explanation:** Formula/null/words are observed; stated coefficient difference is algebra; intended prose meaning remains inferred.
- **Exact remaining human question:** Does the difference prose describe the alternative, and how should its explicit equivalence to β13=0 be read?
- **Classification:** Statistical reporting inconsistency; P_P; all P_P; all compared content is prospective SAP material in the same bound bundle.
- **Evidence state:** `recorded_candidate`, determined by the observed zero-null versus nonzero-difference interpretation and reproduced algebra.

## C055 — Final SAP Equation 1 model reference

- **Location found:** Yes: PLAN [final SAP p57 primary model](../../../joi190092supp3_prod.pdf#page=57), [p58 subgroup](../../../joi190092supp3_prod.pdf#page=58), [p60 Bayesian item](../../../joi190092supp3_prod.pdf#page=60), [p61 continuation](../../../joi190092supp3_prod.pdf#page=61), and PLAN [original SAP p16 Equation 1](../../../joi190092supp3_prod.pdf#page=16).
- **Source value/text matched:** Final primary analysis uses treatment predictor and study-site random intercept; no displayed numbered Equation 1 is supplied there. Final subgroup says begin with Equation (1); Bayesian continuation uses likelihood corresponding to Equation (1).
- **Comparator matched:** Printed numbered Equation 1 in the bound SAP's original version uses fixed site coefficients. The final primary paragraph and literal displayed referent differ in site structure.
- **Consistency rule applicable:** A model-reference label should identify the intended parameterization, or state a mapping when final and original specifications differ.
- **Calculation/logical comparison reproduced:** Original displayed fixed-site equation and final random-intercept primary paragraph are distinct specifications; final references do not supply a matching numbered formula or explicit mapping. No fitted analysis output is reconstructed.
- **Necessary inputs available:** Original equation and final primary/subgroup/Bayesian references.
- **Exact missing inputs/definitions:** Final numbered equation or explicit mapping; whether subgroup/Bayesian analyses deliberately retained fixed-site specifications.
- **Source-grounded alternative interpretation:** “Equation 1” may informally mean the final primary model despite a stale number, or explicitly mean a retained fixed-site model for these analyses.
- **Direct observation versus inferred explanation:** Reference and specifications are observed; intended old versus final referent is unresolved, and no claim about the actual report model follows.
- **Exact remaining human question:** Does final “Equation 1” mean the final random-intercept model, the original fixed-site equation or a separate retained model for subgroup/Bayesian work?
- **Classification:** Measure, label, or scale inconsistency; P_P; all P_P; PLAN final/original SAP model references. The fixed-to-random amendment by itself is not the discrepancy.
- **Evidence state:** `recorded_candidate`, determined by the unmatched final model reference, pending its explicitly missing mapping.

## C056 — Twelve-month same-Wald/model assertion

- **Location found:** Yes: PLAN [original SAP p16 primary](../../../joi190092supp3_prod.pdf#page=16), [p18 twelve-month item](../../../joi190092supp3_prod.pdf#page=18), [final SAP p57 primary](../../../joi190092supp3_prod.pdf#page=57), [p58 twelve-month item](../../../joi190092supp3_prod.pdf#page=58).
- **Source value/text matched:** Both primary sections use treatment coefficient zero and one-df likelihood-ratio test; final primary treatment/site-random model has no anatomical interaction.
- **Comparator matched:** Both twelve-month sections say the same statistical model “(and Wald procedure)” as primary, then state that treatment and treatment/anatomic-location interaction coefficients both equal zero.
- **Consistency rule applicable:** A “same” model/procedure statement should match the referenced test and contrast; distinct LRT/Wald labels and single-versus-joint coefficient nulls do not identify the same printed procedure/contrast without explanation.
- **Calculation/logical comparison reproduced:** Primary named procedure is LRT, not Wald; primary null is one treatment coefficient, while twelve-month joint null includes anatomical interaction absent from the printed final primary model. No assertion that realized LRT and Wald P values must differ is used.
- **Necessary inputs available:** Model/test definitions, one-df primary null and explicit twelve-month joint null.
- **Exact missing inputs/definitions:** Twelve-month model and contrast, any primary Wald definition, and intended meaning of “same.”
- **Source-grounded alternative interpretation:** Twelve-month analysis may deliberately use an expanded anatomical-interaction model and Wald test while retaining an older “same” clause. A model can permit both tests, but the text does not specify this mapping.
- **Direct observation versus inferred explanation:** Printed test names and nulls differ; intended expansion or realized test output is unknown.
- **Exact remaining human question:** Which model and joint contrast define the twelve-month test, and is its Wald procedure deliberately different from the primary one-df LRT?
- **Classification:** Statistical reporting inconsistency; P_P; all P_P; PLAN primary versus PLAN twelve-month statements within both SAP versions.
- **Evidence state:** `recorded_candidate`, determined by reproduced printed procedure/contrast identity mismatch.

## C057 — Dose-reduction Fisher output and P precision

- **Location found:** Yes: REPORT [main p4 Fisher/two-sided methods](../../../jama_rathinam_2019_oi_190092.pdf#page=4), [p6 dose-reduction result](../../../jama_rathinam_2019_oi_190092.pdf#page=6), with overall arm denominators 107/109 also in p4 results.
- **Source value/text matched:** 21 (19.6%) versus 15 (13.8%) dose reductions, P=.27; main methods Fisher exact and two-sided P; original software R3.51 is listed.
- **Comparator matched:** Standard probability-ordering two-sided Fisher for displayed 21/107 and 15/109 gives .276681552078. Direct counts imply 86/94 complements. R4.5.2 `fisher.test` reproduced that value; exposed-MMF108 sensitivity gives .278466774702.
- **Consistency rule applicable:** Under the standard R two-sided Fisher convention and nearest-hundredth rounding, .27668 displays .28, not .27. This is explicitly conditional on tail and printing conventions; source does not state a nearest-rounding promise.
- **Calculation/logical comparison reproduced:** R calculation of the exact displayed 2×2 table and the alternative 108 denominator both round to .28 at nearest hundredth. Printed .27 is compatible with truncation of .27668. This is a small precision question, not a significance or conclusion claim.
- **Necessary inputs available:** Reduction numerators, displayed arm denominators/proportions, test label and P.
- **Exact missing inputs/definitions:** Exact analysis 2×2 table, original R call/version behavior, conditional-tail convention and truncation/rounding rule.
- **Source-grounded alternative interpretation:** P may have been truncated to two decimals; different inclusion or tail convention may have generated the display. Source does not identify which.
- **Direct observation versus inferred explanation:** Counts/P/test label are observed; the standard-convention exact P is an auxiliary reconstruction; a particular formatting mistake is not established.
- **Exact remaining human question:** What exact table, Fisher-tail convention and printing rule produced P=.27 for 21 versus 15 dose reductions?
- **Classification:** Statistical reporting inconsistency; S_W; all S_W; REPORT main methods versus REPORT main result. C049 has PLAN logistic versus REPORT Fisher as its different comparator and remains separate.
- **Evidence state:** `recorded_candidate`, determined by reproduced conditional same-table Fisher/nearest-rounding mismatch, with the unprovided printing convention explicitly preserved.

## Classification field handoff

| ID | Primary category | Relationship type | All relationships | Compared document roles | Evidence state |
|---|---|---|---|---|---|
| C039 | Cross-document numeric inconsistency | S_C | S_C | REPORT main p8 versus REPORT results p12 | record_input_error |
| C040 | Denominator, proportion, or total inconsistency | S_C | S_C | REPORT main p8 versus REPORT results p11 | record_input_error |
| C041 | Measure, label, or scale inconsistency | P_R | P_R, S_C | REPORT main p8 versus REPORT results p5 and PLAN protocol pp81/136 | recorded_candidate |
| C042 | Measure, label, or scale inconsistency | S_C | S_C | REPORT main p8 versus REPORT results pp6/14/15 | recorded_candidate |
| C043 | Measure, label, or scale inconsistency | P_R | P_R, S_C, S_W | REPORT main p8 and REPORT results pp14/15 versus REPORT results p5 and PLAN protocol p81 | recorded_candidate |
| C044 | Measure, label, or scale inconsistency | P_R | P_R | REPORT results p5 versus PLAN protocol p81 | not_reproduced |
| C045 | Measure, label, or scale inconsistency | P_R | P_R | REPORT main p8 and REPORT results pp5/14 versus PLAN protocol pp81/136 | recorded_candidate |
| C046 | Analysis-unit or population inconsistency | P_R | P_R | REPORT main pp6/7 versus PLAN original/final SAP pp31/71 | recorded_candidate |
| C047 | Statistical reporting inconsistency | P_R | P_R | REPORT main p4 versus PLAN final SAP p61 | recorded_candidate |
| C048 | Statistical reporting inconsistency | P_R | P_R | REPORT main pp4/6/7 versus PLAN final SAP p61 | recorded_candidate |
| C049 | Statistical reporting inconsistency | P_R | P_R | REPORT main pp4/6 versus PLAN final SAP p61 | recorded_candidate |
| C050 | Statistical reporting inconsistency | S_W | S_W | REPORT main p4 versus REPORT main p6 | recorded_candidate |
| C051 | Statistical reporting inconsistency | P_P | P_P | PLAN final SAP p61 versus PLAN final SAP pp46/57 | recorded_candidate |
| C052 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN original/final SAP pp26/67 prose versus PLAN pp27/68 table/summary | recorded_candidate |
| C053 | Statistical reporting inconsistency | P_P | P_P | PLAN original SAP p16 equation versus PLAN p17 coefficient test | recorded_candidate |
| C054 | Statistical reporting inconsistency | P_P | P_P | PLAN original/final SAP pp17/58 null versus PLAN same passages interpretation | recorded_candidate |
| C055 | Measure, label, or scale inconsistency | P_P | P_P | PLAN final SAP pp57/58/60/61 references versus PLAN original SAP p16 equation | recorded_candidate |
| C056 | Statistical reporting inconsistency | P_P | P_P | PLAN original/final SAP pp16/57 primary test versus PLAN pp18/58 twelve-month test | recorded_candidate |
| C057 | Statistical reporting inconsistency | S_W | S_W | REPORT main p4 methods versus REPORT main p6 result | recorded_candidate |

Coverage result: 19 of 19 assigned IDs; 16 recorded_candidate, 2 record_input_error, 1 not_reproduced. No missing-tool limitation. Source native-text glyph failures are explicitly corrected at C043/C044; rasters close confirmation gaps. Remaining human inputs are individually named in every card, especially field alignment C039/C040, actual rescue design C048, NI estimand C047/C051, adherence-test variable/dispersion C050, and Fisher printing rule C057.
