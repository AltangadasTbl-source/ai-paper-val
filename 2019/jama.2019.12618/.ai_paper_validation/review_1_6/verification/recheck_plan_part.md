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
