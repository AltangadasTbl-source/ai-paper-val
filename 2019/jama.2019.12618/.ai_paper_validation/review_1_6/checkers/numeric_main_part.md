# Main numeric consistency checker

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

