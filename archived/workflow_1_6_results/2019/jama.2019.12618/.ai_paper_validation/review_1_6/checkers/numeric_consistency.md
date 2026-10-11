# Complete Workflow 1.6 numeric consistency review

Canonical merged scope: all 497 numeric and definition groups, N001-N079, N100-N243, N300-N454 and N600-N718, covering the complete supplied main article and support sources. The four disjoint checker parts below retain their original local scope statements and provenance. All assigned relationships are COMPLETE; the candidate ledger performs the documented duplicate merges and stable registration.

## Preserved main numeric consistency checker

Exact assigned scope: main REPORT PDF 1–10, N001–N079. All 79 COMPLETE; every grouped table entry checked.14distinct candidates; no stableC IDs, severity, evidence disposition, or adjudication assigned. Every compared location below is REPORT by main-article content. All remain questions for human adjudication. No candidate count limit. Source: [main article](../../../jama_rathinam_2019_oi_190092.pdf#page=1). Full rule/status coverage: [numeric inventory](../relationships/numeric_relationship_inventory.md).

Direct source confirmation: p5 andp8 rendered from supplied PDF usingPoppler 26.01.0 into preprocessing/numeric_main_p005.png and numeric_main_p008.png; p6 directrender preprocessing/main_p006.png visually inspected. p3/4/7 exact native source text read. Every footnote candidate visually confirmed at source page6. Rounding tolerance±.05percentage point for one decimal; count and literal-marker equality exact. No web, old conclusions, Python, or source mutation.

## MAIN-NUM-01 — F baseline macular edema percentage

- **Relationships:** N062.
- **Compared locations and roles:** REPORT main article p5 Table1 eye header F n201 and macular edema55(27.3).
- **Evidence:** [main PDF](../../../jama_rathinam_2019_oi_190092.pdf#page=5).
- **Printed inputs, rule and reproducible calculation:** 100×55/201=27.363184%; nearest0.1=27.4%; printed27.3 interval[27.25,27.35) excludes calculated value by.013184point.
- **Tolerance:** ±0.05percentage point per one-decimal percent; exact integer counts.
- **Direct observation versus inference:** Printed values/words/markers above are observed directly; calculations follow their printed labels. Production error, row-specific population, or author's intended wording is inferred only as an alternative.
- **Alternatives and missing inputs:** A denominator202 would yield27.2277%=27.2, so cannot explain27.3; a different denominator or truncation could apply but is not stated. Other rows use ordinary rounding.
- **Quality-control relevance:** Misalignment can affect extraction of the named count, percentage, outcome definition or population into downstream evidence tables. No paper-conclusion effect inferred.
- **Exact human question:** What eye denominator and rounding convention produced55(27.3), given the printed201-eye denominator?

## MAIN-NUM-02 — M nonserious liver percentage

- **Relationships:** N004,N077,N078.
- **Compared locations and roles:** REPORT main article p8 Table3 M n107 and nonserious elevated ALT/AST14(13.0); repeated p1abstract/p7Adverse Events14[13.0%].
- **Evidence:** [main PDF](../../../jama_rathinam_2019_oi_190092.pdf#page=8).
- **Printed inputs, rule and reproducible calculation:** 100×14/107=13.084112%; nearest0.1=13.1; printed13.0 interval[12.95,13.05) excludes it. Same Table3 allergic reaction14(13.1) uses identical numerator and header denominator.
- **Tolerance:** ±0.05percentage point per one-decimal percent; exact integer counts.
- **Direct observation versus inference:** Printed values/words/markers above are observed directly; calculations follow their printed labels. Production error, row-specific population, or author's intended wording is inferred only as an alternative.
- **Alternatives and missing inputs:** Truncation or row-specific population could generate13.0, but same14 numerator elsewhere13.1 and unchanged denominator require clarification.
- **Quality-control relevance:** Misalignment can affect extraction of the named count, percentage, outcome definition or population into downstream evidence tables. No paper-conclusion effect inferred.
- **Exact human question:** Why are identical14/107 counts displayed13.0 for liver abnormalities and13.1 for allergic reaction, and which rounding/population rule applies?

## MAIN-NUM-03 — Switch-eligible total

- **Relationships:** N068,N066.
- **Compared locations and roles:** REPORT main article p7 Prespecified12-Month Outcomes49 of 68 eligible failures without serious laboratory AE; p6Table2 failures32+42, safety3+2; p3Fig1 safety-ineligible3+2.
- **Evidence:** [main PDF](../../../jama_rathinam_2019_oi_190092.pdf#page=7).
- **Printed inputs, rule and reproducible calculation:** Reported failure total32+42=74; subtract5safety exclusions=69, differing printed68 by1. Flow unwilling9+11=20 plus49 switched=69.
- **Tolerance:** Exact count/definition/marker identity; printed50.0% uses±.05point; other printed percentages retain their displayed precision.
- **Direct observation versus inference:** Printed values/words/markers above are observed directly; calculations follow their printed labels. Production error, row-specific population, or author's intended wording is inferred only as an alternative.
- **Alternatives and missing inputs:** Eligibility could exclude one additional failure for another reason; the same68 sentence may implicitly apply more criteria. Death occurred among preprimary loss, so it cannot automatically be subtracted again from74 analyzed failures.
- **Quality-control relevance:** Misalignment can affect extraction of the named count, percentage, outcome definition or population into downstream evidence tables. No paper-conclusion effect inferred.
- **Exact human question:** Which additional patient/eligibility criterion reduces74−5=69 to printed68, or is the printed eligible count based on another denominator?

## MAIN-NUM-04 — Primary loss label aggregates missed visits

- **Relationships:** N011,N021,N076.
- **Compared locations and roles:** REPORT main article p4Results22(10.2%) 'lost to follow-up'; p3Fig1M9lost/F10lost plusM2/F1missed6 months; p7missingness22missed primary visit.
- **Evidence:** [main PDF](../../../jama_rathinam_2019_oi_190092.pdf#page=4).
- **Printed inputs, rule and reproducible calculation:** 9+10=19 explicitly lost before6 months;2+1=3 missed visit;19+3=22 absent primary information. Printed22 lost combines two separately labeled categories.
- **Tolerance:** Exact count/definition/marker identity; printed50.0% uses±.05point; other printed percentages retain their displayed precision.
- **Direct observation versus inference:** Printed values/words/markers above are observed directly; calculations follow their printed labels. Production error, row-specific population, or author's intended wording is inferred only as an alternative.
- **Alternatives and missing inputs:** Lost could be intended as umbrella missing-primary outcome; that convention is not stated and differs figure wording.
- **Quality-control relevance:** Misalignment can affect extraction of the named count, percentage, outcome definition or population into downstream evidence tables. No paper-conclusion effect inferred.
- **Exact human question:** Does22 lost mean19 lost plus3temporarily missed, and should the same population label distinguish these categories?

## MAIN-NUM-05 — Half described as majority

- **Relationships:** N067.
- **Compared locations and roles:** REPORT main article p7 Prespecified12-Month Outcomes 'majority (50.0% for methotrexate and55.0% for mycophenolate mofetil) discontinuing prednisone'.
- **Evidence:** [main PDF](../../../jama_rathinam_2019_oi_190092.pdf#page=7).
- **Printed inputs, rule and reproducible calculation:** Strict majority requires>50%;50.0% display interval[49.95,50.05) centers on half. The named eligible sizes60/48 yield exacthalf30/60 or24/48; no prednisone numerator/denominator printed.
- **Tolerance:** Exact count/definition/marker identity; printed50.0% uses±.05point; other printed percentages retain their displayed precision.
- **Direct observation versus inference:** Printed values/words/markers above are observed directly; calculations follow their printed labels. Production error, row-specific population, or author's intended wording is inferred only as an alternative.
- **Alternatives and missing inputs:** Majority might refer pooled groups rather than each group:50.0 and 55.0 could yield pooled>50. Narrative punctuation leaves that possibility; precise prednisone denominator absent.
- **Quality-control relevance:** Misalignment can affect extraction of the named count, percentage, outcome definition or population into downstream evidence tables. No paper-conclusion effect inferred.
- **Exact human question:** Does majority refer pooled participants or each drug group, and what prednisone-discontinuation numerators/denominators underlie50.0%/55.0%?

## MAIN-NUM-06 — Edema exclusion adjective

- **Relationships:** N062,N071.
- **Compared locations and roles:** REPORT main article p5Table1footnotee excludesVKHpatients with 'serious retinal detachment'; p6Table2footnotem excludesVKHpatients with 'serous retinal detachment', same42/55edema eyes.
- **Evidence:** [main PDF](../../../jama_rathinam_2019_oi_190092.pdf#page=5).
- **Printed inputs, rule and reproducible calculation:** The printed exclusion labels differ: serious describes seriousness; serous describes morphology. Baseline edema42/55 and6 months thickness[42]/[55] are linked quantitative populations.
- **Tolerance:** Exact count/definition/marker identity; printed50.0% uses±.05point; other printed percentages retain their displayed precision.
- **Direct observation versus inference:** Printed values/words/markers above are observed directly; calculations follow their printed labels. Production error, row-specific population, or author's intended wording is inferred only as an alternative.
- **Alternatives and missing inputs:** Typographic error is plausible, or distinct exclusion criteria may have been intended. Aggregate equality42/55 cannot establish identical included eyes.
- **Quality-control relevance:** Misalignment can affect extraction of the named count, percentage, outcome definition or population into downstream evidence tables. No paper-conclusion effect inferred.
- **Exact human question:** Are baseline42/55edema counts and follow-up42/55thickness counts defined by the same serous-detachment exclusion, or were different criteria used?

## MAIN-NUM-07 — Efficacy marker links to success definition

- **Relationships:** N015,N066.
- **Compared locations and roles:** REPORT main article p6Table2 'Efficacy' superscriptc,26/32(81) and38/42(90); footnotec defines treatment success; footnoted defines efficacy failure.
- **Evidence:** [main PDF](../../../jama_rathinam_2019_oi_190092.pdf#page=6).
- **Printed inputs, rule and reproducible calculation:** Exact marker lookupc gives success definition, contradicting efficacy-failure row; nearbyd explicitly defines failure due efficacy. Numeric counts correctly sum but definition attachment differs.
- **Tolerance:** Exact count/definition/marker identity; printed50.0% uses±.05point; other printed percentages retain their displayed precision.
- **Direct observation versus inference:** Printed values/words/markers above are observed directly; calculations follow their printed labels. Production error, row-specific population, or author's intended wording is inferred only as an alternative.
- **Alternatives and missing inputs:** Systematic production marker shift is plausible; cannot prescribe correction before human review.
- **Quality-control relevance:** Misalignment can affect extraction of the named count, percentage, outcome definition or population into downstream evidence tables. No paper-conclusion effect inferred.
- **Exact human question:** Which definition should accompany efficacy-failure26/32and38/42, given attachedc defines success?

## MAIN-NUM-08 — Intolerability marker links to efficacy definition

- **Relationships:** N015,N066.
- **Compared locations and roles:** REPORT main article p6Table2 'Intolerability' superscriptd,3/32(9),2/42(5); footnoted defines efficacy failure; footnotee defines intolerability.
- **Evidence:** [main PDF](../../../jama_rathinam_2019_oi_190092.pdf#page=6).
- **Printed inputs, rule and reproducible calculation:** Exact lookupd maps to not achieving efficacy success, rather than inability/unwillingness due adverse effects.
- **Tolerance:** Exact count/definition/marker identity; printed50.0% uses±.05point; other printed percentages retain their displayed precision.
- **Direct observation versus inference:** Printed values/words/markers above are observed directly; calculations follow their printed labels. Production error, row-specific population, or author's intended wording is inferred only as an alternative.
- **Alternatives and missing inputs:** Production shift is plausible; efficacy/intolerability counts cannot be reassigned from printed record.
- **Quality-control relevance:** Misalignment can affect extraction of the named count, percentage, outcome definition or population into downstream evidence tables. No paper-conclusion effect inferred.
- **Exact human question:** Which failure definition is intended for intolerability3/32and2/42 given attachedd defines efficacy?

## MAIN-NUM-09 — Safety marker links to intolerability definition

- **Relationships:** N015,N066.
- **Compared locations and roles:** REPORT main article p6Table2 'Safety' superscripte,3/32(9),2/42(5); footnotee defines intolerability; footnotef defines abnormal-laboratory safety failure.
- **Evidence:** [main PDF](../../../jama_rathinam_2019_oi_190092.pdf#page=6).
- **Printed inputs, rule and reproducible calculation:** Exact lookupe maps safety counts to inability/unwillingness due adverse effects, whilef provides safety threshold.
- **Tolerance:** Exact count/definition/marker identity; printed50.0% uses±.05point; other printed percentages retain their displayed precision.
- **Direct observation versus inference:** Printed values/words/markers above are observed directly; calculations follow their printed labels. Production error, row-specific population, or author's intended wording is inferred only as an alternative.
- **Alternatives and missing inputs:** Production shift is plausible; equal3/2counts with intolerability do not make definitions interchangeable.
- **Quality-control relevance:** Misalignment can affect extraction of the named count, percentage, outcome definition or population into downstream evidence tables. No paper-conclusion effect inferred.
- **Exact human question:** Which definition belongs to safety3/32and2/42 given attachede describes intolerability?

## MAIN-NUM-10 — Anatomical subgroup P markers link to safety definition

- **Relationships:** N025.
- **Compared locations and roles:** REPORT main article p6Table2 intermediate P.07 superscriptf and posterior/panuveitis P.02superscriptf; footnotef defines safety failure; footnoteg gives subtype×treatment interactionP.004.
- **Evidence:** [main PDF](../../../jama_rathinam_2019_oi_190092.pdf#page=6).
- **Printed inputs, rule and reproducible calculation:** Both repeatedf attachments refer to safety abnormal laboratory definition unrelated to subgroupP.07/.02. Interaction noteP.004 isg elsewhere.
- **Tolerance:** Exact count/definition/marker identity; printed50.0% uses±.05point; other printed percentages retain their displayed precision.
- **Direct observation versus inference:** Printed values/words/markers above are observed directly; calculations follow their printed labels. Production error, row-specific population, or author's intended wording is inferred only as an alternative.
- **Alternatives and missing inputs:** BothPmarkers share samef/rule/comparator and are one candidate; wrong marker does not imply wrong subgroup Pvalues.
- **Quality-control relevance:** Misalignment can affect extraction of the named count, percentage, outcome definition or population into downstream evidence tables. No paper-conclusion effect inferred.
- **Exact human question:** What note was intended for subgroupP.07and.02, and how should interactionP.004 relate to their markers?

## MAIN-NUM-11 — Continuation marker links to interaction P

- **Relationships:** N067.
- **Compared locations and roles:** REPORT main article p6Table2 'Continued on randomized antimetabolite'g48/60(80),40/54(74); footnoteg subtype×treatment interactionP.004; footnoteh continuing60M/54F.
- **Evidence:** [main PDF](../../../jama_rathinam_2019_oi_190092.pdf#page=6).
- **Printed inputs, rule and reproducible calculation:** Exact lookupg provides anatomical interactionP.004 rather than explaining continuation denominators60/54.
- **Tolerance:** Exact count/definition/marker identity; printed50.0% uses±.05point; other printed percentages retain their displayed precision.
- **Direct observation versus inference:** Printed values/words/markers above are observed directly; calculations follow their printed labels. Production error, row-specific population, or author's intended wording is inferred only as an alternative.
- **Alternatives and missing inputs:** Interaction note could be deliberately repeated here but no relevance to continuation denominator is stated; systematic shift plausible.
- **Quality-control relevance:** Misalignment can affect extraction of the named count, percentage, outcome definition or population into downstream evidence tables. No paper-conclusion effect inferred.
- **Exact human question:** Which note defines continuation60/54 denominators, given the continued row points to interactionP.004?

## MAIN-NUM-12 — Switch marker links to continuation population

- **Relationships:** N014,N068.
- **Compared locations and roles:** REPORT main article p6Table2 'Switched to other antimetabolite'h20/29(69),7/20(35); footnoteh sayscontinued60originalM/54originalF; footnotei says29originalF→M/20originalM→F; p7narrative confirmsreceived-drug contrast.
- **Evidence:** [main PDF](../../../jama_rathinam_2019_oi_190092.pdf#page=6).
- **Printed inputs, rule and reproducible calculation:** Exact lookuph describes continuers60/54, incompatible with row switch denominators29/20;i supplies correct received-drug mapping.
- **Tolerance:** Exact count/definition/marker identity; printed50.0% uses±.05point; other printed percentages retain their displayed precision.
- **Direct observation versus inference:** Printed values/words/markers above are observed directly; calculations follow their printed labels. Production error, row-specific population, or author's intended wording is inferred only as an alternative.
- **Alternatives and missing inputs:** Headers alone could look like original randomization, so footnote mapping matters; production shift plausible.
- **Quality-control relevance:** Misalignment can affect extraction of the named count, percentage, outcome definition or population into downstream evidence tables. No paper-conclusion effect inferred.
- **Exact human question:** Which footnote and treatment assignment convention should define switched20/29and7/20, given attachedh describes continuers?

## MAIN-NUM-13 — Missed-dose marker links to switched participants

- **Relationships:** N069.
- **Compared locations and roles:** REPORT main article p6Table2 'Missed doses, mean(SD), %'i4.6(1.0),4.3(.5),P.87; footnotei says29F→M/20M→F; footnotej definesmissed/expected doses.
- **Evidence:** [main PDF](../../../jama_rathinam_2019_oi_190092.pdf#page=6).
- **Printed inputs, rule and reproducible calculation:** Exact lookupi defines switching patients instead of missed/expected dose denominator. j defines expected-dose ratio but is not attached to that row. This single comparator/row candidate includes unattachedj observation.
- **Tolerance:** Exact count/definition/marker identity; printed50.0% uses±.05point; other printed percentages retain their displayed precision.
- **Direct observation versus inference:** Printed values/words/markers above are observed directly; calculations follow their printed labels. Production error, row-specific population, or author's intended wording is inferred only as an alternative.
- **Alternatives and missing inputs:** Could imply adherence only among switchers rather than initial trial patients, though narrative saysweeklyM/dailyF; production shift plausible.
- **Quality-control relevance:** Misalignment can affect extraction of the named count, percentage, outcome definition or population into downstream evidence tables. No paper-conclusion effect inferred.
- **Exact human question:** Which adherence population and denominator applies to4.6%/4.3%, and should missed-dose row referencej rather than switcheri?

## MAIN-NUM-14 — F safety header and percentage denominator

- **Relationships:** N010,N077,N078.
- **Compared locations and roles:** REPORT main article p8Table3 F header n109 and footnote b one F never received; p3Fig1F 108received; p8F fatigue59(54.6),headache45(41.7),ocularhypertension13(12.0),others63(58.3); repeatedp7fatigue/headache.
- **Evidence:** [main PDF](../../../jama_rathinam_2019_oi_190092.pdf#page=8).
- **Printed inputs, rule and reproducible calculation:** 59/109=54.1284%→54.1 versus54.6;45/109=41.2844→41.3 versus41.7;13/109=11.9266→11.9 versus12.0;63/109=57.7982→57.8 versus58.3. Using108 gives54.6/41.7/12.0/58.3. All 36Fpairedrows reconcile108; distinct fromM14 rounding candidate.
- **Tolerance:** ±0.05percentage point per one-decimal percent; exact integer counts.
- **Direct observation versus inference:** Printed values/words/markers above are observed directly; calculations follow their printed labels. Production error, row-specific population, or author's intended wording is inferred only as an alternative.
- **Alternatives and missing inputs:** Header may deliberately showrandomizedN and footnote b implyexposed 108, adequately explaining percentages to a reader who infers subtraction. Percent denominator is not explicitly labeled108.
- **Quality-control relevance:** Misalignment can affect extraction of the named count, percentage, outcome definition or population into downstream evidence tables. No paper-conclusion effect inferred.
- **Exact human question:** Does Table 3 F header n109 denote randomized enrollment while percentages use108exposed, and should safety percentage denominator be stated explicitly?

## Expanded Table3 arithmetic coverage

All 36pairedrows checked. F 108 is exposure-based diagnostic supported by Figure1 and footnote b, not silently substituted for printed109. CandidateMAIN-NUM-14 concerns this shared header/denominator rule; MAIN-NUM-02 concerns different M rounding rule. Duplicate equal numerators across AE types are not candidates by themselves, since outcomes can overlap.

| Exact event row | Mprinted count(percent) | Calculation M/107 nearest0.1 | Fprinted count(percent) | Calculation F/108 nearest0.1 | Status |
|---|---|---|---|---|---|
| Ocular hypertension | 10(9.3) | 9.3458→9.3 | 13(12.0) | 12.0370→12.0 | COMPLETE |
| Vitreous hemorrhage | 3(2.8) | 2.8037→2.8 | 3(2.8) | 2.7778→2.8 | COMPLETE |
| Suspect/confirmed glaucoma | 2(1.9) | 1.8692→1.9 | 2(1.9) | 1.8519→1.9 | COMPLETE |
| IOP<5withoutdamage | 0 | 0.0000→0.0 | 1(0.9) | 0.9259→0.9 | COMPLETE |
| Cataract surgery indicated | 5(4.7) | 4.6729→4.7 | 2(1.9) | 1.8519→1.9 | COMPLETE |
| Self-report vision decrease | 9(8.4) | 8.4112→8.4 | 19(17.6) | 17.5926→17.6 | COMPLETE |
| Eye pain | 9(8.4) | 8.4112→8.4 | 4(3.7) | 3.7037→3.7 | COMPLETE |
| Serious glaucoma | 0 | 0.0000→0.0 | 1(0.9) | 0.9259→0.9 | COMPLETE |
| Retinal detachment | 1(0.9) | 0.9346→0.9 | 0 | 0.0000→0.0 | COMPLETE |
| NonseriousALT/AST | 14(13.0) | 13.0841→13.1 | 8(7.4) | 7.4074→7.4 | COMPLETE; MAIN-NUM-02 |
| Lowhemoglobin | 2(1.9) | 1.8692→1.9 | 3(2.8) | 2.7778→2.8 | COMPLETE |
| Lowleukocytes | 3(2.8) | 2.8037→2.8 | 1(0.9) | 0.9259→0.9 | COMPLETE |
| Creatinine | 1(0.9) | 0.9346→0.9 | 0 | 0.0000→0.0 | COMPLETE |
| SeriousALT/AST | 3(2.8) | 2.8037→2.8 | 2(1.9) | 1.8519→1.9 | COMPLETE |
| Fatigue | 62(57.9) | 57.9439→57.9 | 59(54.6) | 54.6296→54.6 | COMPLETE |
| Headache | 55(51.4) | 51.4019→51.4 | 45(41.7) | 41.6667→41.7 | COMPLETE |
| Mood changes | 33(30.8) | 30.8411→30.8 | 26(24.1) | 24.0741→24.1 | COMPLETE |
| Hairloss | 6(5.6) | 5.6075→5.6 | 2(1.9) | 1.8519→1.9 | COMPLETE |
| Nausea | 42(39.3) | 39.2523→39.3 | 30(27.8) | 27.7778→27.8 | COMPLETE |
| Muscleweakness | 32(29.9) | 29.9065→29.9 | 26(24.1) | 24.0741→24.1 | COMPLETE |
| Numbness | 25(23.4) | 23.3645→23.4 | 18(16.7) | 16.6667→16.7 | COMPLETE |
| Nonseriousdiarrhea | 25(23.4) | 23.3645→23.4 | 24(22.2) | 22.2222→22.2 | COMPLETE |
| Dyspnea | 21(19.6) | 19.6262→19.6 | 22(20.4) | 20.3704→20.4 | COMPLETE |
| Nonseriousvomiting | 26(24.3) | 24.2991→24.3 | 24(22.2) | 22.2222→22.2 | COMPLETE |
| Allergicreaction | 14(13.1) | 13.0841→13.1 | 11(10.2) | 10.1852→10.2 | COMPLETE |
| Fever | 11(10.3) | 10.2804→10.3 | 18(16.7) | 16.6667→16.7 | COMPLETE |
| CHF/arrhythmia | 4(3.7) | 3.7383→3.7 | 2(1.9) | 1.8519→1.9 | COMPLETE |
| Systemicinfection | 25(23.4) | 23.3645→23.4 | 27(25.0) | 25.0000→25.0 | COMPLETE |
| Othernonserioussystemic | 65(60.7) | 60.7477→60.7 | 63(58.3) | 58.3333→58.3 | COMPLETE |
| Death | 1(0.9) | 0.9346→0.9 | 0 | 0.0000→0.0 | COMPLETE |
| Seriousdiarrhea | 0 | 0.0000→0.0 | 1(0.9) | 0.9259→0.9 | COMPLETE |
| Disability | 1(0.9) | 0.9346→0.9 | 0 | 0.0000→0.0 | COMPLETE |
| Hospitalization | 2(1.9) | 1.8692→1.9 | 2(1.9) | 1.8519→1.9 | COMPLETE |
| Seriousinfection | 0 | 0.0000→0.0 | 1(0.9) | 0.9259→0.9 | COMPLETE |
| Seriousvomiting | 1(0.9) | 0.9346→0.9 | 0 | 0.0000→0.0 | COMPLETE |
| Otherserious | 3(2.8) | 2.8037→2.8 | 1(0.9) | 0.9259→0.9 | COMPLETE |

Thresholds: all Table3 event rows retain original units and comparators:ocular>24/<5mmHg,ALT/AST2–5×ULN<28d versus>5×ULNor2–5×ULN≥28d,hemoglobin>6.5/<9g/dL,leukocytes>1000/<2500perμL,creatinine>1.5/<2mg/dL,fever<39°Cfor12h. Equality gaps in threshold language are not current numerical contradictions absent patient at a boundary. Creatinineconversion×88.4 yields1.5→132.6 and2→176.8μmol/L; no contradictorySIvalue printed. Safety ≥1patient counts nonexclusive and must not be summed to reconstruct14serious events.

Statistical handoff: S009 means (SD)4.6(1.0)vs4.3(.5) with P.87 and specified Welch test requires complete fresh inferential consistency review. Numeric stage does not duplicate that inferential candidate. AdjustedOR/RD versus crude proportions, Table2 inferred mean effects versus descriptive median changes, and clustering/mixed-model labels are reserved for complete statistical/model alignment review. No missing model detail alone emitted.

Completion:79/79relationship records,10/10mainpages,all 36AEpairedrows,all Table1entries and groupedgradecells,14distinct candidates,scientific coverage limitations: None. Humanquestions above identify precise missingpopulation/definition/convention where applicable.

# Numeric consistency checker: non-plan results supplement

Exact scope: DOC-002 joi190092supp1_prod.pdf PDF pp1-16, numeric relationships N100-N243 (NR001-NR144), and DOC-005 joi190092supp4_prod.pdf p1 administrative page. Two complete inventory parts contain95 and49 relationships. Main article and PLAN checks are assigned to other agents. No old candidates, review decisions or reports were read. No web used. All locations below are REPORT by content. No stable C IDs, judgments or dispositions assigned.

Method: source-linked reusable Poppler layout text plus current direct `pdftotext -layout` streams for pp3-12 and14-16; current Poppler26.01.0 renders of p10,p14,p15 visually inspected. Render command: `pdftoppm -f N -l N -scale-to 1600 -singlefile -png joi190092supp1_prod.pdf .ai_paper_validation/review_1_6/preprocessing/numeric_results_pN`. The three derivatives are numeric_results_p10.png, numeric_results_p14.png and numeric_results_p15.png under preprocessing. No OCR or Python extraction needed. Sources and reused assets unchanged.

## Complete checks

Every count/percentage cell in eTables2,4-6,8-9 was recalculated with its printed column N. Patient percentages are distinguished from event counts and person-time rates. The nine enrollment counts sum216; their whole-percent shares sum100 and individually reconcile within0.5 percentage points. All adverse-event counts lie within their column N. Any-event unions are at least the largest component count and at most the component sum; overlapping row counts are not added as mutually exclusive subgroups. Six-month exposure population107+108=215 plus one untreated randomized MMF participant is internally coherent. Continuing N62/56 and switching N29/20 are different populations/time windows; no baseline denominator substitution. Except the two cells below, all one-decimal shares reconcile within0.05 percentage points. Every eligibility, threshold/duration, serious-category, dose, unit and scale group was checked. Unreported CBC/creatinine units and thresholds at which no observed value is supplied do not alone establish numeric inconsistencies. Methotrexate BID on Day1 corresponds20mg or15mg per week; MMF BID on all7 days corresponds2g/day or1g/day. These are coherent reduced-dose patterns. Repeated values in distinct overlapping event rows do not establish copying. DOC-005 availability date is administrative and supplies no applicable outcome relationship.

Six distinct source-grounded observations follow; there is no finding-count target. The label comparisons are conditional on the printed eTable1 definitions being the applicable definitions for the reported eTables8/9. No changed event count is inferred.

## Observation A — Mycophenolate eye-floaters percentage

- Relationships: N152/NR053.
- Compared locations and roles: REPORT [DOC-002 p10 eTable4 eye floaters MMF cell](../../../joi190092supp1_prod.pdf#page=10); REPORT same-page MMF header N=108 and footnote108 exposed participants.
- Printed inputs:5(4.7), N108. Direct render confirms4.7, so this is not an extraction artifact.
- Rule/calculation/tolerance:100×5/108=4.6296296%, nearest one decimal4.6%; 4.7−4.6296296=0.0703704 percentage points exceeds0.05 rounding tolerance. MTX5/107=4.6728972→4.7 is coherent but does not supply the MMF denominator.
- Direct observation: printed numerator, percentage and column denominator do not reconcile under ordinary one-decimal rounding. Inference: a copied percentage or different row denominator is possible, not established.
- Alternatives: an unreported row-specific denominator107 would yield4.7; the table explicitly supplies108, and no row-specific missingness is disclosed. Count, percentage or header could be the input needing clarification.
- Quality-control relevance: an extracted patient proportion may differ from the printed population definition; bounded downstream transcription risk only.
- Exact human question: Is the MMF eye-floaters row calculated from108 exposed patients, or was a different row denominator used; which printed input explains5(4.7)?

## Observation B — Mycophenolate serious-diarrhea percentage after switch

- Relationships: N240/NR141.
- Compared locations and roles: REPORT [DOC-002 p15 eTable9 Serious Systemic, Diarrhea MMF cell](../../../joi190092supp1_prod.pdf#page=15); REPORT same-page MMF header N=20.
- Printed inputs:1(3.4), N20; directly confirmed in current source image.
- Rule/calculation/tolerance:100×1/20=5.0%; printed3.4 differs by1.6 percentage points, exceeding0.05. The neighboring MTX denominator29 would give100/29=3.4482759→3.4, but does not apply to the MMF column.
- Direct observation: numerator/percentage/header mismatch. Inference: use of the other column denominator is a plausible mechanism only.
- Alternatives: row-specific denominator29, a different numerator, or misplaced column label would require clarification; no row-specific population is stated.
- Quality-control relevance: affects extraction of a serious-event patient proportion in the switch population; no conclusion impact inferred.
- Exact human question: What numerator and denominator generated the MMF serious-diarrhea1(3.4) cell under N20?

## Observation C — Ocular hypertension threshold inclusion differs

- Relationships: N118/NR019, N197/NR098, N219/NR120.
- Compared locations and roles: REPORT [DOC-002 p5 eTable1 nonserious ocular hypertension](../../../joi190092supp1_prod.pdf#page=5), versus REPORT [p14 eTable8 nonserious ocular row](../../../joi190092supp1_prod.pdf#page=14) and REPORT [p15 eTable9 nonserious ocular row](../../../joi190092supp1_prod.pdf#page=15).
- Printed inputs: definition≥24mmHg; result rows>24mmHg. p14 reports3(4.8)/1(1.8) under N62/56; p15 reports2(6.9)/3(15.0) under N29/20.
- Rule/calculation/tolerance: threshold labels for the same named event should agree; x=24 satisfies x≥24 but not x>24. Logical comparison has zero numeric tolerance. The associated percentages reconcile; the issue concerns the event definition.
- Direct observation: inclusive and strict threshold symbols differ. Inference: whether any participant at exactly24 was classified differently is unknown.
- Alternatives: the > labels may be shorthand for≥; an explicitly changed criterion may have been applied. No such distinction is disclosed within these report tables. No count correction is asserted.
- Quality-control relevance: prevents incompatible extraction of the event threshold supporting patient counts.
- Exact human question: Did eTables8/9 count ocular hypertension at≥24 or strictly>24mmHg, and how should their labels align with eTable1?

## Observation D — Serious ocular hypertension result label uses pressure criterion

- Relationships: N118/NR019, N199/NR100 (N223/NR124 provides corroboration only).
- Compared locations and roles: REPORT [DOC-002 p5 eTable1 serious ocular hypertension](../../../joi190092supp1_prod.pdf#page=5), versus REPORT [p14 eTable8 Serious Ocular row](../../../joi190092supp1_prod.pdf#page=14).
- Printed inputs: serious definition Surgery required(laser or incisional); p14 serious row Ocular hypertension>24mmHg with MTX1(1.6), MMF0(0.0), N62/56. p15 serious row explicitly says surgery required and corroborates the definition.
- Rule/calculation/tolerance: a counted serious event should retain its defining severity criterion. Pressure>24 is the same description printed in the nonserious row on p14 and does not express surgery required. Percentages1/62×100=1.6129→1.6 and0/56=0 are coherent; exact category-label comparison has no arithmetic tolerance.
- Direct observation: reported serious-row label omits/replaces the supplied surgery criterion and duplicates the pressure description of the nonserious row. Inference: underlying patient may have required surgery; source does not show individual event details.
- Alternatives: abbreviated label under a Serious Ocular heading may imply surgery without restating it; alternatively a different seriousness rule was used. This is a conditional label-consistency question, not evidence that the patient was misclassified.
- Quality-control relevance: reader may treat a pressure-only threshold as the definition of the reported serious count.
- Exact human question: Does the p14 serious ocular-hypertension count represent surgery-required cases, and is>24mmHg an abbreviated or different serious-event criterion?

## Observation E — Serious cataract count versus not-applicable definition

- Relationships: N132/NR033, N224/NR125.
- Compared locations and roles: REPORT [DOC-002 p5 eTable1 Cataract serious column](../../../joi190092supp1_prod.pdf#page=5), versus REPORT [p15 eTable9 Serious Ocular Cataract surgery](../../../joi190092supp1_prod.pdf#page=15); REPORT [p7 generic hospitalization/intervention serious definitions](../../../joi190092supp1_prod.pdf#page=7) supplies a potential alternative.
- Printed inputs: p5 nonserious Visually significant cataract/cataract surgery indicated, serious Not applicable(n/a). p15 serious cataract surgery MTX1(3.4), MMF0(0.0), N29/20.
- Rule/calculation/tolerance: a category marked n/a in the stated event definitions conflicts with a nonzero result explicitly under that serious category unless a separate criterion applies. 100×1/29=3.4482759→3.4 is arithmetically coherent. Category comparison exact, no rounding tolerance.
- Direct observation: a nonzero serious cataract result appears despite serious cataractn/a. Inference: the event may have met a generic hospitalization or intervention criterion; participant detail not provided.
- Alternatives: surgery was separately serious due to hospitalization/preventing permanent impairment, distinguishing actual surgery from merely indicated surgery. The generic p7 rules make this possible, but the table does not explain which applies to this count.
- Quality-control relevance: consistent serious/nonserious labeling matters for safety-count extraction; no clinical judgment is made.
- Exact human question: Which stated serious-event criterion supports the one cataract-surgery patient in eTable9 despite eTable1 marking serious cataractn/a?

## Observation F — Fever upper endpoint differs between definitions and result labels

- Relationships: N130/NR031, N213/NR114, N237/NR138.
- Compared locations and roles: REPORT [DOC-002 p6 eTable1 Fever for12hours](../../../joi190092supp1_prod.pdf#page=6), versus REPORT [p14 eTable8 Non-Serious Systemic fever](../../../joi190092supp1_prod.pdf#page=14) and REPORT [p15 eTable9 same row](../../../joi190092supp1_prod.pdf#page=15).
- Printed inputs: p6 nonserious>100.6 to103°F/39.5°C, serious≥103°F/39.5°C; p14/p15 nonserious Fever<103degrees for12hours. Result counts p14 MTX3(4.8), MMF3(5.4); p15 MTX4(13.8), MMF1(5.0).
- Rule/calculation/tolerance: the upper endpoint described as to103 differs from explicitly<103 if to includes the endpoint; exactly103 also meets the printed serious≥103 criterion. Exact logical endpoint comparison, zero tolerance. All row percentages reconcile. Conversion103°F→39.444°C is compatible with approximate temperature-threshold display; no conversion candidate emitted.
- Direct observation: the printed upper-bound descriptions differ. Inference: inclusive interpretation of to103 creates a boundary overlap; no measured participant temperature at103 is supplied.
- Alternatives: to103 may mean up to but excluding103, making the results labels clarify rather than change the definition. This ambiguity must be preserved; no observed-event reclassification is inferred.
- Quality-control relevance: the quantitative fever endpoint defining reported patient counts is not consistently explicit.
- Exact human question: Does the nonserious fever definition exclude exactly103°F, as eTables8/9 state, and is to103 in eTable1 intended as an exclusive upper endpoint?

## Handoff and limitations

Inventories: relationships/numeric_results_part1.md (95 complete N rows) and relationships/numeric_results_part2.md (49 complete N rows). Checker scope144 relationships, six emitted observations. No extraction or scientific-coverage gap. Conditional label observations identify missing event-specific explanations rather than asserting changed counts. Footnotes referring to nonexistent eFigure2 are locator defects without an independent numeric inconsistency and are not emitted. Statistical interaction P values are delegated to the statistical checker. No source-preservation limitation.
# Numeric consistency checker: protocol PDF pages1–128

Fresh disjoint numeric review of DOC-003, joi190092supp2_prod.pdf. Two bounded units: PE-N001–066 (globalN300–N365;66 relationships) and NPM001–089 (globalN366–N454;89 relationships), total155/155 groups checked. All constituent table rows, diagrams, grade categories, window columns and dose conversions were checked; arithmetic, totals, populations, denominators, missingness, scales, units, rate/count, reference/ordering, rounding and repeated-value tests were applied where meaningful. Prospective rules, administrative counts, instrument identifiers and historical estimates were kept distinct from observed trial results. No minimum/maximum or early stopping used. No old candidate/reports, external evidence, web or Python extraction used.

Every candidate below concerns PLAN content exclusively, including historical background and both prospectively supplied versions. All compared locations are PLAN; provisional relationship solely P_P. Document-role assignments follow content. Later amended rules alone were not candidates. NP-A–NP-O are local checker labels only; stable C IDs, judgments and dispositions are not assigned. No enrolled-patient effect, study-conclusion impact or actual event recoding is claimed. Candidates identify preventable quantitative or label ambiguity that could propagate when plan definitions are reused; human questions delimit missing information.

## Complete relationship coverage

All66 early and89 middle groups have one row each in ../relationships/numeric_protocol_early.md and ../relationships/numeric_protocol_middle.md. Every constituent row of originalTables1–10, finalTables1–10, trial-lens/axis-step tables, inflammation/cataractscales, source visual diagrams and equipment-unit conversions was examined. The original6–12extension timeline and original/finalboundaries were matched bydocumentversion. No inferentialtest/Pvaluewasprinted in these155numericgroups; the originalone-thirdinterimruleisassignedtostatisticalreview. No display-zerocandidate arose.

Fresh locator derivatives: preprocessing/numeric_protocol_source_pN.txt forN=11,16,22,26,27,36,43,44,45,50,52,53,87,103,110,117,123,124,125,126,127. Directcommand pdftotext -layout -f N -l N joi190092supp2_prod.pdf OUTPUT, Poppler26.01.0. These are new derivatives, not edits to supplied sources or reused assets. Existing mapped visualsourceimages pp15/19/80 and all14freshmiddlepages remain source-linked. Rechecker should visually confirm every cited page; text is locator, not final authority. Scientific coverage limitations: none. Missing supplied definitions are recorded in specific human questions.

## Source-grounded candidates

### NP-A: Planned maximum-follow-up completion predates eligible completion

- Relationships: N307 / PE-N008.
- Compared locations and document roles: [DOC-003 PDF p11](../../../joi190092supp2_prod.pdf#page=11) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: Table1: enrollment November2012–May2015; six-month follow-up+one-month window throughDecember2015; maximum12-month follow-up+one-month window throughJuly2015; database lock/analysis throughApril2016.
- Reproducible rule/calculation and tolerance: The latest May2015 entrants require at least May2016 for12months, and approximatelyJune2016 includingone-month window. July2015 is only2months afterMay2015, and is earlier than the separately printed December2015 six-month completion. Calendar arithmetic permits±1month ambiguity in month-only dates; discrepancy≥10months remains.
- Direct observation versus inference: Direct observation: all four dates are printed in one original-version table. Inference: follow-up duration is applied to the latest permissible entrant, rather than an actual enrollment record.
- Alternatives and missing definitions: July2015 could be a stale projected date or a subset deadline; table says finish maximum follow-up, without a subset qualifier. Later2017-version schedule is a disclosed different version and does not create this candidate.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Which enrollment cutoff and population are intended for the July 2015 maximum follow-up completion, and how does that date reconcile with the original May 2015 enrollment end?

### NP-B: Original leukocyte classification leaves exactly1000/μL without a class

- Relationships: N318 / PE-N019.
- Compared locations and document roles: [DOC-003 PDF p16](../../../joi190092supp2_prod.pdf#page=16) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: Table3: non-serious leukocytes >1000 and<2500/μL lasting less than1month; serious<2500 lastingmorethan1month or≤999/μL.
- Reproducible rule/calculation and tolerance: For a newly observed count exactly1000/μL,1000>1000 isfalse and1000≤999 isfalse. Before1month, neither printed class contains this value. Tolerance0 cells/μL for integer printed cutoffs.
- Direct observation versus inference: Direct observation: strict >1000 and≤999 differ by an uncovered integer. Inference: acute1000/μL test value demonstrates the gap; no patient with this value is claimed.
- Alternatives and missing definitions: Could reflect intended integer≥1000 non-serious or≤1000 serious, or discretionary clinical grading; finalversionp81 uses≤1000 and thus is a separate amended context.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Which class is intended for a leukocyte count exactly 1000/μL lasting less than one month in the original protocol?

### NP-C: Original platelet classes overlap at20000/μL

- Relationships: N318 / PE-N019.
- Compared locations and document roles: [DOC-003 PDF p16](../../../joi190092supp2_prod.pdf#page=16) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: Table3: non-serious platelets20000to75000/μL lasting less than1month; serious≤20000/μL or<75000/μL lastinggreaterthan1month.
- Reproducible rule/calculation and tolerance: For a count20000/μL newly observed, an inclusive20,000–75,000 interval includes it and≤20,000 also includes it. Exact printed integer boundary; tolerance0.
- Direct observation versus inference: Direct observation: same table supplies overlapping endpoints. Inference: interpreting “to” inclusively makes class non-unique at20000.
- Alternatives and missing definitions: Lower bound “to” could be intended open despite usual inclusive range notation; finalversionp81 serious<20000 is a different version and not independent mismatch.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Is 20000/μL a serious or non-serious platelet abnormality in the original Table 3, and is the lower boundary of its non-serious range inclusive?

### NP-D: Original AST/ALT event class differs at supplied boundary values

- Relationships: N320 / PE-N021; N364 / PE-N065.
- Compared locations and document roles: [DOC-003 PDF p16](../../../joi190092supp2_prod.pdf#page=16) (PLAN); [DOC-003 PDF p52](../../../joi190092supp2_prod.pdf#page=52) (PLAN); [DOC-003 PDF p53](../../../joi190092supp2_prod.pdf#page=53) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: p16Table3: non-serious AST/ALT2to5×ULN; serious>5×ULN. p52§6.1 example abnormal findings>2but<5×ULN. p53§6.2 serious≥5×ULN.
- Reproducible rule/calculation and tolerance: At exactly5×ULN, Table3 places value in2–5 non-serious range and excludesitfrom>5serious;§6.2 includes5 asserious. At exactly2×ULN Table3 includes2 but§6.1 example excludesit. Tolerance0 at dimensionless printed endpoints; primary contradiction is the explicit5×class boundary.
- Direct observation versus inference: Direct observation: same2012MOP has different inequalities for matching laboratory analytes. Inference: boundary-value substitutions reveal mutually different labels; no actual AE counts reconstructed.
- Alternatives and missing definitions: §6.1 examples could be nonexhaustive, so2×alone neednotcontradict. Table3mayhavepriority over prose, or viceversa, but no precedence printed. Finalversion amended Table3 notthecandidate.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: For original-protocol adverse-event coding, is AST/ALT exactly 5×ULN serious or non-serious, and which original section controls the boundaries?

### NP-E: Same-drug follow-up extension receives alternate-drug phase label

- Relationships: N328 / PE-N029; N303 / PE-N004; N334 / PE-N035.
- Compared locations and document roles: [DOC-003 PDF p9](../../../joi190092supp2_prod.pdf#page=9) (PLAN); [DOC-003 PDF p22](../../../joi190092supp2_prod.pdf#page=22) (PLAN); [DOC-003 PDF p26](../../../joi190092supp2_prod.pdf#page=26) (PLAN); [DOC-003 PDF p27](../../../joi190092supp2_prod.pdf#page=27) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: p22: held7.5mg/day first6months “untiltheendofPhaseI”; further corticosteroid reduction allowed “inPhaseII, ifpatientscontinueonthesamemedicationasPhaseI.” p26§4.1.1 andp27Table10: same-drug extension PhaseI6–12months; p27§4.1.2: PhaseII alternate-treatment rescue afterfailure.
- Reproducible rule/calculation and tolerance: Identity rule: a continuation onthefirstdrug atmonths6–12 maps toPhaseI6–12, whilePhaseII issecond-drug rescue. The same continuation is labeledPhaseII onp22 andPhaseI onpp26–27. Exact label/time/drug alignment; tolerance0.
- Direct observation versus inference: Direct observation: originalversion uses both phase labels for the same-drug continuation. Inference: steroid-taper phase indexing could be mis-extracted if p22 isreadliterally.
- Alternatives and missing definitions: “PhaseII” might mean a general second6-monthperiod inthatparagraph; elsewhereformalPhaseII isalternate-drug rescue. No efficacy conclusion inferred.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Does the p22 permission for further tapering on the same medication apply to Phase I months 6–12, or to formal Phase II alternate-drug rescue?

### NP-F: Original visit-window column states weeks for day-valued entries

- Relationships: N334 / PE-N035.
- Compared locations and document roles: [DOC-003 PDF p26](../../../joi190092supp2_prod.pdf#page=26) (PLAN); [DOC-003 PDF p27](../../../joi190092supp2_prod.pdf#page=27) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: p26Table9 andp27Table10 columnheader “Window(weeks)”; cells explicitly±15days and−15to+30days.
- Reproducible rule/calculation and tolerance: Dimensional identity: a day-valued interval has unitsdays, notweeks. ±15days=±15/7weeks≈±2.143weeks, not±15weeks;−15/+30days=−2.143/+4.286weeks. Exact unit label; rounding0.001week shown onlyforcalculation.
- Direct observation versus inference: Direct observation: header andcells use incompatible displayed units. Inference: header-only extraction could expand window sevenfold; actual scheduling error notclaimed.
- Alternatives and missing definitions: Explicit cell units may fully disambiguate human use; header could be a carried template label. This limitscandidate to labeling.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Which unit is intended for the original Tables 9–10 Window column, and should its header be interpreted together with each cell's explicit days?

### NP-G: Original Month6 window differs across adjoining phase-I schedule tables

- Relationships: N334 / PE-N035.
- Compared locations and document roles: [DOC-003 PDF p26](../../../joi190092supp2_prod.pdf#page=26) (PLAN); [DOC-003 PDF p27](../../../joi190092supp2_prod.pdf#page=27) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: p26Table9 PhaseI0–6months: Month6M6-I window−15to+30days. p27Table10 PhaseI6–12months: Month6M6-I window±15days.
- Reproducible rule/calculation and tolerance: Samebaseline,codeM6-I,timeMonth6: lower limits−15 agree; upperlimits30vs15 differ15days. Exact day endpoints; tolerance0.
- Direct observation versus inference: Direct observation: overlapping Month6 rows in originalversion provide different windows. Inference: matchingtheMonth6 primary/extensiontransitionvisit assumesoneassessmentservesboth.
- Alternatives and missing definitions: Table10Month6 might mean a separateextensionentryassessment or require a narrowerwindow for extension, while theprimaryendpointallows+30days; distinction isnotnamed.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Are these two M6-I rows the same visit, and is its permitted upper window +15 or +30 days when defining extension entry and the six-month endpoint?

### NP-H: Tumbling-E score formula requires more letters on one line than the line contains

- Relationships: N351 / PE-N052; N449 / NPM084.
- Compared locations and document roles: [DOC-003 PDF p43](../../../joi190092supp2_prod.pdf#page=43) (PLAN); [DOC-003 PDF p44](../../../joi190092supp2_prod.pdf#page=44) (PLAN); [DOC-003 PDF p124](../../../joi190092supp2_prod.pdf#page=124) (PLAN); [DOC-003 PDF p125](../../../joi190092supp2_prod.pdf#page=125) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: Originalp43 andfinalp124 scoring: “If10ormorelettersofthefirstline” correctat4m, score=correct4mletters+30. p44/p125 Snellen rule describes at least4of5letters correctly on a line.
- Reproducible rule/calculation and tolerance: A five-letterline permits atmost5correct; requested10first-linecorrect>5by5. Integerlettercounts allow0 tolerance. Formula total70+30=100 itself is coherent; inconsistencyis first-line qualifying condition.
- Direct observation versus inference: Direct observation: bothversions repeat the first-line10letter clause and4of5rowdescription. Inference: takingfirstline literallymakesqualifierunattainable; sourceforms/table may clarifyintendedtotal.
- Alternatives and missing definitions: “firstline” could be a wording error for totalletters, or encompass two rows informally. Distinguish this clause from separate low-vision threshold candidateNP-I.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Does “10 or more letters of the first line” mean total letters across the chart, and what observable criterion enables the four-meter letter score plus 30?

### NP-I: Tumbling-E low-vision/scoring thresholds do not cover the same letter counts

- Relationships: N347 / PE-N048; N348 / PE-N049; N351 / PE-N052; N447 / NPM082; N449 / NPM084.
- Compared locations and document roles: [DOC-003 PDF p42](../../../joi190092supp2_prod.pdf#page=42) (PLAN); [DOC-003 PDF p43](../../../joi190092supp2_prod.pdf#page=43) (PLAN); [DOC-003 PDF p44](../../../joi190092supp2_prod.pdf#page=44) (PLAN); [DOC-003 PDF p123](../../../joi190092supp2_prod.pdf#page=123) (PLAN); [DOC-003 PDF p124](../../../joi190092supp2_prod.pdf#page=124) (PLAN); [DOC-003 PDF p125](../../../joi190092supp2_prod.pdf#page=125) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: pp42–43 andp123 procedure: <10totallettersat4m→1m; <10totallettersat1m→lowvision. pp43–44,p124–125 scoring:≤3correctlettersofthelargestlineat4m→1mscore;≤3lettersat1m→lowvision.
- Reproducible rule/calculation and tolerance: At1m count4–9 satisfies<10 butnot≤3; e.g.5<10true and5≤3false. At4m total9with5correctlargest-lineletters satisfies<10total butnot≤3largest-line. Integercounts; tolerance0. SameE-chart/version comparisons; letter-chartp112<20isadifferentprocedure andnotaninputhere.
- Direct observation versus inference: Direct observation: procedure/scoring use different thresholds andcountunits(total versusline). Inference: constructed counts exhibitundefined/inconsistentmapping; no patient-specificmeasurementclaimed.
- Alternatives and missing definitions: Low-visiontesting could be performedbelow10 while numericalletter-score remains usableuntil≤3, with separateencodingrules. Package'swithin-scopeprose doesn'tstate this split.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: For E-chart one-meter counts 4–9, and four-meter totals below 10 with more than three largest-line letters correct, should a letter score, low-vision category, or both be recorded, and which threshold controls analysis?

### NP-J: Vitreous-cell grades both include zero cells

- Relationships: N355 / PE-N056; N453 / NPM088.
- Compared locations and document roles: [DOC-003 PDF p45](../../../joi190092supp2_prod.pdf#page=45) (PLAN); [DOC-003 PDF p127](../../../joi190092supp2_prod.pdf#page=127) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: BothTables: grade0=“Nocells”; grade0.5+=“0to5cells”; highergrades1+=6–10,2+=11–20,3+=21–50,4+>50.
- Reproducible rule/calculation and tolerance: 0cells satisfies nocells andinclusive0–5. Integercount0 requiresno rounding; tolerance0. This is asecondarycollectedcellscale, explicitlynotprimary inflammationcontrol.
- Direct observation versus inference: Direct observation: two displayed bins overlap atzero in bothversions. Inference: literal lookupmakesgradeambiguous; no actualgradecount difference demonstrated.
- Alternatives and missing definitions: 0to5 could colloquially mean occasionalobservedcells versus trulyabsentcells, requiring aqualifiernotprinted. TheprimaryAC/hazeendpointisnotclaimedaffected.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Should zero vitreous cells receive grade 0 or 0.5+, and does the 0.5+ interval have an unstated positive lower boundary or sampling distinction?

### NP-K: Original white-cell event example changes numeric scale without a unit marker

- Relationships: N364 / PE-N065; N318 / PE-N019.
- Compared locations and document roles: [DOC-003 PDF p16](../../../joi190092supp2_prod.pdf#page=16) (PLAN); [DOC-003 PDF p53](../../../joi190092supp2_prod.pdf#page=53) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: p16Table3 leukocyte thresholds >1000and<2500/μL or≤999/μL. p53§6.1 example WBC reduction “tobelow2.5”, no WBC unit stated in this example.
- Reproducible rule/calculation and tolerance: 2500/2.5=1000. Values reconcile onlyif2.5 is expressed inthousandcells/μL(10³/μL) or10⁹/L ratherthan cells/μL; printedTable3 unit cannotbe carried unchanged. Exact factor1000; tolerance0 forscaleidentity.
- Direct observation versus inference: Direct observation: the samenon-seriousWBCconcept is printedas2500/μL versus2.5withoutunit. Inference: missingunitmaydenoteaconventionalrescaling, ratherthan thresholdconflict.
- Alternatives and missing definitions: Laboratories commonly use scaled WBCunits; an omittedunit here couldexplainbothvalues. This is aconditional scale-labelcandidate, not aclaimthat2.5literallymeans2.5cells/μL.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: What unit and scale are intended for “below 2.5” in original §6.1, and is this the same non-serious event boundary as Table 3 below 2500/μL?

### NP-L: Mycophenolate maintenance bottle described as30-day supply contains16⅔days at full dose

- Relationships: N402 / NPM037; N403 / NPM038; N401 / NPM036.
- Compared locations and document roles: [DOC-003 PDF p86](../../../joi190092supp2_prod.pdf#page=86) (PLAN); [DOC-003 PDF p87](../../../joi190092supp2_prod.pdf#page=87) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: p86 MMF maintenance1.5gBID=3pillsAM+3pillsPM (500mgpill),6pills/day. p87 maintenancebottles “30days’worth…plusadditionalpillsasabuffer”; MMF bottles100pills each. Monthlydispense200pills; baseline14-day introductory+100pillmaintenance.
- Reproducible rule/calculation and tolerance: Full-dose30daysrequires30×6=180pills beforebuffer;100/6=16.667days, short80pills/13.333days. Monthly200/6=33.333days coherentbuffer. Baseline14+100/6=30.667dayscoherentfirst-monthsupply. Exact pillarithmetic tolerance0pills; durationsreportedto0.001day.
- Direct observation versus inference: Direct observation: bottle-level30-day claim and100pillcount conflict at printed full-dose regimen. Inference: computed duration is bottle-level, not assertionofpatientundersupply.
- Alternatives and missing definitions: General30-daysupplymightmean a dispensingpackageoftwobottles ratherthansinglebottle; baselineonlyneedsremaining≈16days. Reviseddefinitioncouldfullyexplain operationalintent.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Does “maintenance dose bottles will contain 30 days’ worth” refer to individual MMF 100-pill bottles or to the monthly 200-pill dispensing package?

### NP-M: Final letter-chart refraction Chart R has two numeric version identifiers

- Relationships: N420 / NPM055; N429 / NPM064.
- Compared locations and document roles: [DOC-003 PDF p103](../../../joi190092supp2_prod.pdf#page=103) (PLAN); [DOC-003 PDF p110](../../../joi190092supp2_prod.pdf#page=110) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: p103: ChartR “PrecisionVisionChartVersion2110” forrefraction. p110: Charts1,2,R correspond “2110,2111and2112,respectively”; ChartR usedforallmanifestsubjectiverefraction.
- Reproducible rule/calculation and tolerance: Respectivelymapping yieldsChartR2112, which differs fromChartR2110onp103 by2intheidentifier. Identifier identity, notnumericmagnitudecomparison; tolerance0.
- Direct observation versus inference: Direct observation: samefinalMOP namesChartRforidenticalrefractionusewithtwoidentifiers. Inference: twochartversions cannotbeunambiguouslyselectedfromtheselabels.
- Alternatives and missing definitions: Couldbealternativecatalogversions ormappingordererror; chartIDs notclinicalresults and no actualdeviceuseclaimed. Tumbling-E2305b isaseparatechartfamily.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Which Precision Vision numeric version is intended for the final letter-chart Chart R refraction procedure: 2110 or 2112, or are both interchangeable variants?

### NP-N: Intermediate E-chart sphere retest uses a lens different from its next conditional

- Relationships: N441 / NPM076; N438 / NPM073.
- Compared locations and document roles: [DOC-003 PDF p115](../../../joi190092supp2_prod.pdf#page=115) (PLAN); [DOC-003 PDF p117](../../../joi190092supp2_prod.pdf#page=117) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: p115 mediumacuity guide specifies sphere±1.00D trial/increment. p117 intermediate6/30–6/60 branch: if−1.00doesnotimproveletters, “retestusingthe+0.50lens”; nextlines branchon “Ifthe+1.00lens…” better/sameorworse.
- Reproducible rule/calculation and tolerance: Same sequential retest should supplythelens evaluatedby immediatelyfollowingconditional: +0.50versus+1.00 differ0.50D, factor2. Exact prescribedlenspower; tolerance0D.
- Direct observation versus inference: Direct observation: onebranch changes numeric lens label without anintervening1.00Dpresentation. Inference: interpretingconditionalasthere-testresponse createsunmatchedprobe/result.
- Alternatives and missing definitions: NOTEallowschangingtriallensesifacuityimprovessignificantly, buttriggerhereisfailureof−1.00toimproveletters; +0.50mightbeadeliberateadditionalprobe whose conditional wasnotwritten.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: After the intermediate E-chart −1.00 D probe fails to improve the letters read, should the retest use +0.50 D or +1.00 D, and which probe's response governs the next branch?

### NP-O: Final cataract category list omits the expressly defined grade3

- Relationships: N451 / NPM086; N452 / NPM087.
- Compared locations and document roles: [DOC-003 PDF p125](../../../joi190092supp2_prod.pdf#page=125) (PLAN); [DOC-003 PDF p126](../../../joi190092supp2_prod.pdf#page=126) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: p125 opacitystandards1=clinicalpresence,2=clinicalsignificance,3=severeoccurrence; halfgradesallowed(example1.5). p126 allopacitytypes severitycategories “<1,1,1.5,2,2.5,>3”.
- Reproducible rule/calculation and tolerance: Value3 is expresslydefined but belongs to none ofthelistedcategories:3not<1,not1/1.5/2/2.5,and3not>3. Exact ordinalgrade, tolerance0.
- Direct observation versus inference: Direct observation: prose standard3 andcategorylist>3 arebothprinted. Inference: mapping astandard3measurementtoalistcategory isundefined; no actualcataractdistributionclaimed.
- Alternatives and missing definitions: Finalcategorycouldintentionallymean≥3, orformsallow3separately despiteproselist. Missing comparator definition requireshumanreview.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Which category receives an opacity matching the grade 3 standard, and is the final category intended as >3 or ≥3?

## Completion

155 quantitative relationship groups checked;15 distinct document-grounded local candidates emitted. All repeated manifestations of the same mismatch are grouped on one card. Other checks reconcile or lack an independently supplied contradiction, with reasons in the two complete inventories. Original/finalprotocolchanges were respected as disclosedcontexts, ratherthancomparedasidenticalrules. Nocandidateisregistered solelyforanunreportedmodeldetail orforvery-smallPdisplayzero. NoassignedstableCIDs, severity, validity, dispositions orfinalcorrections.

# Numeric consistency checker: assigned PLAN tail and SAP

Scope: 119 global numeric relationship groups N600–N718, with all constituent printed values preserved in `../relationships/numeric_plan_tail.md`. This is a fresh numeric review. All source locations are PLAN by content. Three distinct candidate observations are emitted below without stable candidate IDs or AI adjudications. Their repeated occurrences across original/final SAP are provenance of the same observation, not additional candidate counts.

## Complete check record

### Protocol tail: N600–N638 (N-PT001–039)

- N600: Miami nine-point figure is a named photographic scale, not nine participants or a trial outcome; no other assigned image contradicts its point count.
- N601: activity thresholds refer to AC/haze/retinal-choroidal inflammation, not edema alone; ≥1+ and the separate edema exception have different clinical predicates. No numeric contradiction follows.
- N602: duplicate observers are two people at baseline/6mo/12mo/failure; primary observer is explicitly used for the primary endpoint. These are measurement sources, not duplicate participant counts.
- N603: certification ≥80%, remedial retest for <80%; thresholds partition without overlap or gap.
- N604: five qualifying consecutive patients, grades within one; >one triggers extension and all-zero patients excluded. No arithmetic inconsistency between attempted and qualifying samples.
- N605: 20°×20°/49 sections/16 ART versus 30°×5°/seven sections/25 ART are separate scans. Repeated settings at PDF130–131 agree; two scans per eye.
- N606: Heidelberg quality ≥20 and central-subfield thickness each eye; quality score is not µm or an event count.
- N607: one cube plus one five-line raster per eye; image-only PDF133 directly viewed. Caption is exactly “512x218 HD”; no supplied competing acquisition dimension, so no conjectural correction from outside specifications.
- N608: Cirrus quality ≥5 is a different device scale from Heidelberg ≥20; image-only PDF134 mapped visually. No same-scale comparison is assumed.
- N609: at least two qualified operators is a minimum staffing count, distinct from two observer measurements and two eyes.
- N610: photo baseline/6mo/12mo/failure schedule agrees between PDF135 and143; failure substitutes earlier visit. NEI and Miami grades are separate photographic scale labels.
- N611: laboratory measurements include counts, percentages and analytes; CD4 restricted sites and baseline/3/6/12mo differ explicitly from general visit labs. No sum of nonexclusive test populations is asserted.
- N612: twice-ULN nonserious lab stop with one-month normalization/resumption rule versus immediate serious failure are distinct thresholds. Earlier restart explicitly permitted.
- N613: laboratory SAE immediate failure/no PhaseII switch; nonlaboratory SAE in N617 has conditional review. Different SAE subclasses do not contradict.
- N614: AST/ALT interval [2,5)×ULN and creatinine [1.5,2)mg/dL are internally ordered; IOP>24mmHg uses its own scale. WBC≤2.5 has no unit printed here: a missing local unit alone does not establish a competing numeric value/unit.
- N615: AST/ALT≥5×ULN joins [2,5) nonserious interval at five without overlap/gap; qualitative SAE categories may overlap and must not be summed.
- N616: onset/resolution each visit and SAE notice within24h are different clocks; no arithmetic conflict.
- N617: nonlaboratory relatedness review versus lab SAE immediate failure is disclosed distinction; six-month follow-up and six-month DSMC reporting are different schedules; death24h agrees with SAE24h.
- N618: rows observations, columns variables; NA is missing, not zero; no realized workbook denominator supplied.
- N619: pill count each visit and missed-dose logs have no actual count supplied; no adherence percentage inferred.
- N620: BSCVA letters plus Snellen equivalent are paired representations, not summed scales; no conversion data supplied.
- N621: clinical primary observer versus masked reading-center NEI/Miami and OCT morphology are different measures; no identical result is supplied for conflict.
- N622: hemoglobin ≤10 changed to ≤9 explicitly on1March2013. Historical values9–10 are amendment rationale, not contemporaneous conflicting threshold.
- N623: week2±3days and phaseI later safety visits7/8/10/11 are explicit distinct windows; surgery next6mo applies eligibility rather than success.
- N624: sequential site additions and three-month timeline movement have explicit amendment dates; no fixed contemporaneous site total in these clauses.
- N625: masking bags and prior-four-week steroid injection exclusion are disclosed amendments, not a count mismatch.
- N626: 14days→4weeks and60→90days have explicit revisions; 4weeks=28days under literal week arithmetic. They are not asserted equivalent to the prior durations.
- N627: old/new eligibility carried forward to PDF150 under8May2014 revision; population matching retains this boundary.
- N628: old90day activity, four-week steroid treatment/rebound thresholds and 1mg/kg are prior criteria.
- N629: new180day activity/rebound, ≥10mg/day for≥90days and injection4–180days are revised criteria; lower/upper bounds ordered. Native “³” is inequality encoding resolved in mapper, not cubic dose.
- N630: named eligible disease categories do not supply disjoint participant counts; no sum possible.
- N631: Riyadh addition and prednisone7.5mg/day maintained target are explicitly dated amendments, not a success failure numerator.
- N632: acuteVKH≥4weeks and baseline examination up to7days prior apply distinct eligibility/time predicates.
- N633: additional IND-VFQ at Indian sites, NEI-VFQ all sites, Miami preferred photographic scale, NEI eligibility and first90day edema injections are distinct fields/explicit amendments. No incompatible numeric result supplied.
- N634: remove month6 from6–12mo table is explicit version update; no silent duplicate visit count.
- N635: prior-IMT twelve-month window, >12mo earlier exception and any-time biologic exclusion distinguish drug classes; administrative7→10day submission has explicit amendment.
- N636: persistence≥28days crosses nonserious to serious laboratory-event classification; agrees with one-month language at practical scheduling precision, not an exact asserted calendar-day equality. CD4 restrictions repeat N611.
- N637: PhaseII usual two-week entry with explicit exception and omitted repeated forms has no actual duplicate/absent baseline count.
- N638: paper-to-REDCap replacement explicit dated operational amendment; no arm allocation counts supplied.

### Original SAP: N639–N665 (N-SAPE001–027)

- N639–N642: six-month primary endpoint, six-to-twelve-month continuation and four-week rescue visits retain distinct time origins and denominators.5mo sustained≥28days is an additional endpoint, not an equality between calendar month and28days. Secondary percentages/rates/SAE discontinuation remain distinct measures.
- N643–N644: four enumerated original sites match four identifier codes;5characters=1digit+1letter+3digits;4J101 conforms. Three randomization columns count correctly. Blocks4 probability2/3 and6 probability1/3 sum to1. Individual block-probability prose needs the size weighting in candidate PT-NUM-A.
- N645: five eye classes generate5×5=25 combinations. Requires oneC: eligible cells=5+4=9 and ineligible16. Every cell matches that rule; no double count of(C,C).
- N646: four baseline rows×five outcomes plus five baselineE NA cells=25; E denotes absent/never-assessable baseline and does not supply an observed six-month failure. Fail* exception is explicit.
- N647–N649: both-eye patient success versus selected eye outcomes has explicit unit distinction. Worst-to-date assignment versus baseline nonassessable exceptions are prospective rules without a realized conflicting numerator. “two observations per patient” can refer to the two timepoints and is not alone a quantified clash with eye-level analysis.
- N650–N652: anatomy0/1 and treatment0/1 are separate coding variables; −2/+4week windows are asymmetric by design. Four sites require three nonreference indicators, matching the printed reference rule.12mo success requires both6/12mo observations; logMAR2.0 is an assigned missing-eye value, not two letters or a person count. Edema patient denominator and thickness eye measurements retained.
- N653:108×2=216; .6−.4=.2; (.6+.4)/2=.5;10%loss leaves97.2 per arm in expected counts. Inferential80%power compatibility assigned stat lane.
- N654: all25cells checked: each drugB probability equals drugA plus detectable difference (20+18=38,20+21=41;30+20=50,30+23=53;40+20=60,40+23=63;50+20=70,50+22=72;60+19=79,60+21=81). All lie in[0,100]. Statistical power under subgroup composition belongs stat lane.
- N655: sequential .9×.95=.855 retention;108×.855=92.34 if additional5% conditional, vs91.8 if additive15% total. Wording “additional” alone does not settle that convention; no printed fixed twelve-month count contradicts either.
- N656:3.5mo median and lambdaC namedMTX versus historical medianMMF produce candidate PT-NUM-B. BSCVA6.5letters,2.63letters,108 each preserve units; actual power calculation belongs stat lane.
- N657:.6²=.36;8.4×sqrt(1−.36)=8.4×.8=6.72. Mean50 and scale0–100 are supplied as labels, not outcome count.2.57 power/MDE compatibility assigned stat lane.
- N658: discontinuation13%/4%tolerability and5%/5%safety apply separate causes; factor-two38/19=2.160µm SD and65/100µm differences all same unit. No cause sum asserted as observed data.
- N659: enrollment108×.9×.6=58.32(B/A),108×.9×.4=38.88(A/B); one decimal gives58.3/38.9. Completion×.95 gives55.404/36.936→55.4/36.9. Floor gives58/38. Printed formula n_j includes retentionr2 yet prose58/38 refers enrollment, explicitly separated by table captions. No standalone arithmetic candidate for enrollment/completion. Group identities compared to following table emit PT-NUM-C.
- N660–N661: all35power-table cells preserved. .42−.17=.25, not.17; .42−.15=.27; .40−.15=.25. Claimed17% versus25% detectable difference forwarded to stat lane rather than registered here as duplicate statistical observation. Count-header reversal against enrollment is PT-NUM-C. Other row sizes58/76,116/38,40/40 are explicitly sensitivity scenarios, not observed flow counts.
- N662: ten MI replications and ten hotdeck replications same count, not twenty distinct participants; no denominator inferred.
- N663: approximate accrual7–8/mo×30mo=210–240, encompassing216. At25%lower accrual,30/.75=40mo, while3years3mo=39mo; approximate7–8 rate gives completion36–41.14mo for216, including39. No precision-independent contradiction. About3/4 Indian recruitment is approximate and time-specific.
- N664: safety any dose, ITT randomized, PP excludes violations/<50%adherence are distinct declared populations. No realized denominator permits sum check.
- N665: data rows/columns/NA code and DSMC5–7member range are prospective; no workbook actual counts or source missingness supplied.

### Original/final SAP middle: N666–N684 (N-SAPL001–019)

- N666:216/3=72, two-thirds=144. Approximate six-month delay after72nd enrollment refers when outcomes mature, not accrual count error.
- N667:15 versus30American projected interim patients scale exactly twofold. They are explicitly approximate enrollment projections, not a fixed quarter of72 or144. Alpha fractions reviewed independently statistically;24hSAE notice agrees protocol.
- N668: four pooled any/serious ocular/systemic categories are overlapping, not mutually exclusive totals. Subject risk and multiple-events/person rate separated in printed methods.
- N669:100dpi, four-digit date, NA and figure/table parity are operational labels; no realized data table supplied.
- N670:≥8digit seed is not randomization block length. Generator algorithm versus cited bibliography is not independently a contradictory supplied output count.
- N671–N673: final2017 six/twelve-month and rescue rules retain dates. Two-step SUN examples2+→.5+,3+→1+,4+→2+ use ordered grades, not arithmetic subtraction on numeral labels. “4+ to 2+0.” is punctuation/endnote-looking debris without a supplied distinct grade2+0 definition; no numeric outcome inferred.
- N674–N675: nine named sites match nine encoded first digits and5character ID. Four-site retained administrative sentences occur alongside explicit superseding REDCap update; historical four-site list is not a reported nine-site enrollment sum. No candidate solely from those obsolete list clauses. Block probability statement repeated: PT-NUM-A.
- N676: final two5×5matrices reproduce9eligible/16ineligible and25outcome cells as original; no asymmetric eye eligibility.
- N677–N679: final measurement/missing-eye/baseline summary/outcome/−2/+4window definitions repeat matched original rules. Added vasculitis differs by explicit amendment. Units and patient/eye denominators distinguished; no realization supplied.
- N680: country/site<3pool rule is a prospective sparsity threshold, not an actual sample count. Dropout loss versus AE/intolerance0failure matches original.
- N681: same logMAR2.0 missing-eye and twelve-month both-time/both-eye definitions; four discontinuation labels count four. Starting-treatment steroid-free denominator explicit and distinct from ITT.
- N682:10%margin preserved, but inequality/CI orientation assigned statistical specialist; no numeric margin correction guessed.
- N683:216=2×108,.6−.4=.2,pbar=.5,10%loss→97.2perarm. Original/final inputs match; numeric arithmetic coherent.
- N684: all25sensitivity cells repeated and checked as N654; subgroup25%target is different endpoint/sample subgroup from20%overall target.

### Final SAP tail: N685–N718 (N-ST001–034)

- N685: additional5%twelve-month loss repeats N655, no fixed incompatible denominator.
- N686: exact historical/hazard label mismatch repeats PT-NUM-B; no independent power-based diagnosis here.
- N687: BSCVA SD6.5letters/MDE2.63letters/108 repeats N656; letters not logMAR or Snellen units.
- N688:.6²=.36 and8.4sqrt(.64)=6.72 repeat N657. Inferential MDE2.57 versus2.63 question handed to stat lane.
- N689:13%/4%tolerability and5%both safety preserve separate reasons;10%loss is planning assumption.
- N690:38%=2×19%; all proportions within[0,1].
- N691:160µmSD,65µmMDE,100µmhistorical difference share units;108beforeloss is explicit. Actual power stat lane.
- N692: rescue reason classes efficacy/safety/tolerability repeated; no source counts asserted, so no cause subtotal manufactured.
- N693–N697: exact enrollment/completion calculations repeat N659. n0/n1 initial code agrees table, but probability code is switched at the next formula; power table AthenB58/BthenA38 reverses enrollment A/B38.9/B/A58.3. PT-NUM-C. Seven row input vectors all read and checked; sensitivity rows explicitly change scenarios. Summary58DrugA/38DrugB ambiguous as rescue vs first-line label, retained in same candidate.
- N698:90day sensitivity versus >90day deviation is wording of intervention policy, no observed event at exactly90days supplied to yield concrete numeric contradiction.
- N699: approximate3/4India matches original planning value; no REPORT population aligned here.
- N700:7–8×30=210–240contains216;25%slower requires40ratherthan39months only under an exact30month baseline, whereas source rates/durations approximate. Four-site graph label is prospective retained operational text, without four-versus-nine plotted realized count.
- N701: PhaseI12mo/PhaseII6mo different time origins; no result matching without phase key.
- N702–N705: any-dose safety vs randomizedITT vs exclusionsPP;<50%adherence threshold, rowobservations/columnvariables/NA and subject disposition frequencies are prospective; no realized denominator conflict.
- N706:216/3=72; interim thirds coherent; DSMC5–7 separate count.
- N707: masked TreatmentA/B are presentation labels; no printed source drug mapping supplied for outcomes.
- N708:15/30American interim counts double, approximate enrollment projection. No actual numerator mismatch.
- N709–N710: randomized drug exposure assumption, AE counts and person risks versus recurrent-event rates expressly distinguish units. Four overlapping pooled categories are not summed into a total.
- N711: NA unique missing matches original/final and protocol; no actual cells supplied.
- N712: logMAR abbreviation identifies visual-acuity transform, not literal acuity letters count; no numeric conversion offered.
- N713:≥8digit seed is minimum length, no realized random seed to inspect.
- N714: threshold≥2+and two-step reduction versus≥1+to0 are separate endpoints/denominators; explicit revisions not contradiction.
- N715–N716: nine named sites and nine encoded digits reconcile exactly, and reproduce current site list.
- N717: injection sensitivity/deviation amendments repeat clauses, no event count at the boundary supplied.
- N718: revision says REDCap starting18Jan2017 and all lists electronic asof17Jan2017; body says18Jan2017forboth. This operational date could distinguish preparation from patient randomization; no concrete quantitative outcome/allocation inconsistency is supplied, so it is recorded as context rather than a candidate.

## Candidate PT-NUM-A: individual block-size probability wording

Relationships: N643,N675. Primary suggested category: Numeric or arithmetic inconsistency. Compared locations and roles: original SAP [PDF9 §2.4.3](../../../joi190092supp3_prod.pdf#page=9) PLAN and [PDF10 opening continuation](../../../joi190092supp3_prod.pdf#page=10) PLAN; final [PDF50 §2.4.3](../../../joi190092supp3_prod.pdf#page=50) PLAN. All are one bound plan bundle.

Printed inputs: block size4 chosen probability2/3; size6 chosen probability1/3. Prose: “Individuals have a higher probability of being in a block of size 6 because the blocks are larger.” Direct observation: probabilities and wording read from direct Poppler extraction. Calculation: participant weighting normalizes4×2/3 and6×1/3; P(participant in4)=8/14=4/7=57.1429%; P(participant in6)=6/14=3/7=42.8571%. Thus the long-run individual probability of size6 is lower than size4 by14.2857percentagepoints under the printed design.

Tolerance: exact fractions; rounding at even one percentagepoint cannot reverse the ordering. Inference is the size-weighted interpretation of “higher probability”; no realized allocation claim. Alternative: “higher” could mean higher than the block-selection probability1/3 rather than higher than size4. Indeed3/7>1/3 by2/21. A finite stopped list may also have a different realized fraction; no realized fraction is reported. Quality-control relevance: prose can misstate the quantitative randomization description used by later extractors; no claim about achieved balance or conclusions. Human question: Does “higher probability” compare size6 with size4, or compare the individual probability with the one-third block-selection probability, and should the intended comparator be stated explicitly?

## Candidate PT-NUM-B: hazard drug label attached to historical median

Relationships: N656,N686. Primary suggested category: Measure, label, or scale inconsistency. Compared locations and roles: original [SAP PDF24 secondary outcome2](../../../joi190092supp3_prod.pdf#page=24) PLAN; final [SAP PDF65 secondary outcome2](../../../joi190092supp3_prod.pdf#page=65) PLAN. Each location contains both sides of the comparison.

Printed inputs: lambdaC is hazard in methotrexate group; lambdaI is hazard in mycophenolate mofetil group; historical median3.5months is explicitly attributed to mycophenolate mofetil; parenthesis states lambdaC=log(2)/3.5mo for calculation. Direct observation: direct Poppler confirms these same label strings in original and final. Rule: under the supplied exponential hazard parameterization, median3.5mo corresponds to log(2)/3.5=0.1980420516 permonth. Applying the displayed historical MMF median to its named hazard points to lambdaI, whereas source assigns that value to lambdaC(MTX).

Tolerance: categorical drug identity has no rounding tolerance; hazard arithmetic rounded1e−9/month. Inference: the historical median is used as the intended MMF anchor, as opposed to an independently assumed MTX median. Alternative: calculation may intentionally anchor MTX at the same3.5mo as historical MMF or interchange C/I labels under a symmetric formula; neither is expressly stated. Power2.47months is not independently asserted wrong by this numeric observation. Quality-control relevance: named planning-arm input can be extracted under the wrong treatment label. Human question: Is log(2)/3.5 intended for the methotrexate or mycophenolate hazard, and does the calculation intentionally reuse the historical MMF median as a methotrexate assumption?

## Candidate PT-NUM-C: rescue sequence/count and probability-index reversal

Relationships: N659–N661,N693–N697. Primary suggested category: Measure, label, or scale inconsistency. Compared locations and roles: original [SAP PDF25–26 rescue planning](../../../joi190092supp3_prod.pdf#page=25) PLAN, [PDF26 formula and table headers](../../../joi190092supp3_prod.pdf#page=26) PLAN, [PDF27 table and summary](../../../joi190092supp3_prod.pdf#page=27) PLAN; final [PDF66 planning](../../../joi190092supp3_prod.pdf#page=66) PLAN, [PDF67 enrollment/formula/header](../../../joi190092supp3_prod.pdf#page=67) PLAN, [PDF68 table/summary](../../../joi190092supp3_prod.pdf#page=68) PLAN.

Printed inputs:108perinitialarm, retention.9, initialsuccessA.60/B.40. Enrollment table B/A58.3, A/B38.9; expected completion55.4/36.9. Index definesj0=Brescue afterAfailure,j1=Arescue afterBfailure; prose n1=58,n0=38. Following power-table first row labels AthenB58, BthenA38. Probability definitionsp0=MTXrescue afterMMFfailure,p1=MMFrescue afterMTXfailure; first table scenario .42forBafterA and.15forAafterB. Summary says58DrugA/38DrugB.

Direct observation: direct Poppler extraction confirms all labels and cells; direct imagePDF68 visually confirms row58,38,.42,.15,87% and summary. Calculations: afterAfailure108×.9×(1−.60)=38.88→38.9enrolling,36.936→36.9completing; afterBfailure108×.9×(1−.40)=58.32→58.3enrolling,55.404→55.4completing. Floors38forAthenB and58forBthenA follow the printed rule. Thus power-table first row reverses the two sequence counts relative to its own enrollment table. Also fixedj0/j1 sequencing and laterp0/p1 drug names swap associated identities when combined with those header probabilities: the labels and the numeric weights cannot all be retained simultaneously.

Tolerance: table rounding ±0.05person at one decimal; floor differences <1person permitted; reversal gap20persons exceeds either. This is identity/count comparison, not a reconstructed power adjudication. Alternatives: A/B may have been redefined between tables, or power-table counts are a new sensitivity scenario; however text names first row “main scenario” and provides no recoding. Summary58DrugA may mean rescueA, which matches enrollment table, rather than first-lineA, highlighting the unresolved drug-stage key. Quality-control relevance: rescue sample sizes can be transcribed under the opposite treatment sequence, affecting reuse of plan descriptions or power assumptions; no claim about observed rescue outcomes. Human question: Which table sequence labels and n0/p0 versus n1/p1 assignments are intended, and is the58/38power-table main scenario a recoded or changed scenario relative to the38.9/58.3enrollment calculation?

## Crosslane handoff and limitations

Statistical specialists must check power/MDE/CI relationships independently, including17%versus25%rescue difference, QoL/BSCVA MDEs, primary/subgroup power and noninferiority inequality. No old candidate/report data used. No candidate count limit or early stopping used. All119assigned groups inspected and all printed vectors retained. No extraction/scientific coverage gap. Exact randomization comparator and intended hazard/sequence definitions are unresolved human questions, not missing-page limitations. All original sources and reused assets unchanged. Every candidate compares PLAN with PLAN; the coordinator determines formal relationship classifications and stable IDs.
