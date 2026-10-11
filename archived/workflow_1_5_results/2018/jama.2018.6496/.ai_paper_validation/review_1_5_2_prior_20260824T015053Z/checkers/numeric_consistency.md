# Numeric Consistency Check — N001 to N055

## Scope, method, and outcome

Complete check of all 55 canonical numeric/reporting relationships in `relationships/numeric_relationship_inventory.md`. I used the fresh main and support mapper artifacts and the matching fresh OCR and rendered pages. Arithmetic was recomputed from printed integers; integer percentages were tested against ordinary nearest-whole-percent rounding (accepted interval for displayed `p%`: `[p-0.5%, p+0.5%)`). I did not treat non-additive categories, overlapping difficult-airway characteristics, multi-response complications, or explicitly outcome-specific denominators as totals.

`NO_CANDIDATE_SIGNAL` means that the printed relationship reconciles under its stated definition, has no applicable arithmetic comparison, or has a documented non-additive/precision explanation. `PROPOSED_CANDIDATE_SIGNAL` is a document-grounded quality-control signal only, pending human adjudication; no candidate ID or disposition is assigned here.

The reverse-ordered duration confidence interval in Table 3 is not duplicated here: it is an inferential interval/estimate issue assigned to the statistical checker (the related numeric relationship is N019 only as supporting evidence).

## Complete relationship records

| ID | Exact fresh evidence location | Applied check and calculation | Outcome |
|---|---|---|---|
| N001 | [DOC001 PDF p. 1](../../../jama_driver_2018_oi_180054.pdf#page=1), p. 4 Figure 1, p. 5 Table 1 | Allocation: 381 + 376 = 757. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N002 | DOC001 pp. 1, 4, 5 | Difficult-airway groups: 198 + 182 = 380; complements 183 + 194 = 377 and 380 + 377 = 757. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N003 | DOC001 p. 1 abstract; p. 5 Table 1 | 230/757 = 30.38%, rounds to 30%; sex complement from Table 1 is (381−272)+(376−255)=230. Completion 757/757=100%. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N004 | DOC001 pp. 1–2 | Eligibility threshold, dates, and annual visit volume are context quantities with no supplied same-population total comparator. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N005 | DOC001 p. 3; DOC002 p. 11 | Printed 1:1 rule, five stated block sizes, and two strata are definitions; no allocation-block sequence is supplied to test. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N006 | DOC001 p. 3; DOC003 p. 5 | Device dimensions/angles are consistently expressed in cm, French/mm, and degrees; no incompatible same-measure comparator. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N007 | DOC001 p. 3; DOC003 p. 3 | Definitions distinguish saturation percentage, absolute percentage-point fall, and seconds; no within-display scale confusion. Cross-document endpoint wording is reserved for cross-source checking. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N008 | [DOC001 PDF p. 4](../../../jama_driver_2018_oi_180054.pdf#page=4), Figure 1 | 3768−3011=757; 2785+61+28+27+22+15=2938; 30+20+16+6+1=73; 2938+73=3011. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N009 | DOC001 p. 4 Figure 1 | 372+4+5=381; difficult-airway branch 191+2+5=198. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N010 | DOC001 p. 4 Figure 1 | 345+25+6=376; difficult-airway branch 161+18+3=182; 14/15=93.33%→93%, 23/25=92%. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N011 | DOC001 p. 4 narrative/Figure 1 | Adherence: 372/381=97.64%→98%; 345/376=91.76%→92%. Physicians may appear in both arms, so 44+40 is not a unique-physician total. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N012 | DOC001 p. 5 Table 1 | All printed sex percentages round: 272/381=71.39%→71%; 255/376=67.82%→68%. Means/SDs are descriptive, not additive. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N013 | DOC001 p. 5 Table 1 and footnote b | The oxygenation rows use 352 and 344 denominators, implying missing counts 29 and 32. Footnote b instead states oxygen saturation unavailable for 43 patients, split 19 and 24. The fractions themselves round correctly, but the stated missingness does not reconcile. See Signal 4. | COMPLETE — PROPOSED_CANDIDATE_SIGNAL |
| N014 | DOC001 p. 5 Table 1 | Medical components: 185+32+21+20+16+44=318; 173+23+27+28+23+41=315. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N015 | DOC001 p. 5 Table 1 | Trauma: 29+34=63; 23+38=61. Medical+trauma: 318+63=381; 315+61=376. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N016 | DOC001 p. 5 Table 1 | Any-difficult-airway totals match N002. Individual characteristics explicitly can overlap, so their sum is not tested as a denominator total. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N017 | DOC001 p. 5 Table 1 footnotes | Missingness splits: 29+32=61; 94+91=185; 19+24=43. BMI context: 64+68=132. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N018 | [DOC001 PDF p. 6](../../../jama_driver_2018_oi_180054.pdf#page=6), Table 2 | Tested printed fractions: 204/267=76.40%→76%; 210/276=76.09%→76%. Preoxygenation modalities can overlap; no sum rule applies. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N019 | DOC001 p. 6 Table 2 footnote a | 338/381=88.71%→89%; 341/376=90.69%→91%. Etomidate/ketamine are expressly non-exhaustive medication rows; 31+22=53 and 53/78=67.95%→68%. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N020 | DOC001 p. 6 Table 2 footnote b | 366/381=96.06%→96%; 367/376=97.61%→98%. Listed drugs are expressly non-exhaustive; no subtype sum rule applies. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N021 | DOC001 p. 6 Table 2, patient-position rows | The three printed position counts are 222+117+39=378 versus n=381 and 244+96+32=372 versus n=376. Rows are presented as the position categories without a printed “other”/missing category. See Signal 2. | COMPLETE — PROPOSED_CANDIDATE_SIGNAL |
| N022 | DOC001 p. 6 Table 2 footnote d | Start-saturation denominators: 381−21=360 and 376−33=343. All four printed fractions round correctly (22/360=6.11%, 27/343=7.87%, 13/360=3.61%, 8/343=2.33%). | COMPLETE — NO_CANDIDATE_SIGNAL |
| N023 | DOC001 p. 6 Table 2 | 221/381=58.01%→58%; 227/376=60.37%→60%. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N024 | DOC001 p. 6 Table 2 and footnote f | Final-intubator rows: bougie 318+57+8=383, exceeding n=381 by 2; ETT+stylet 334+37+5=376. Footnote calls this the final intubating physician. See Signal 1. | COMPLETE — PROPOSED_CANDIDATE_SIGNAL |
| N025 | DOC001 p. 6 Table 2 | Laryngoscope rows reconcile: 362+12+7=381 and 366+8+2=376; all percentages round. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N026 | DOC001 p. 6 Table 2 and footnote g | With printed denominators after four missing each arm: 218+78+75=371, not 377; 182+90+98=370, not 372. Each fraction rounds correctly, but categories do not exhaust their displayed denominator. See Signal 3. | COMPLETE — PROPOSED_CANDIDATE_SIGNAL |
| N027 | DOC001 p. 6 Table 2 and footnote h | Grades sum to denominators: 269+74+27+3=373; 269+62+23+5=359. Missingness: 381−8=373; 376−17=359. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N028 | DOC001 p. 6 Table 2; p. 4 Figure 1 | First-device categories: 372+4+5=381 and 25+345+6=376; match Figure 1. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N029 | DOC001 p. 7 narrative; p. 8 Table 4 | Failures 8+48=56; 56/757=7.40%→7%. The rescue detail is explicitly process detail/non-independent, and Table 4 branches each reconcile within its arm. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N030 | DOC001 p. 8 Table 4 footnotes | Bougie failure pathways: 0+0+6+0+0+2=8; ETT+stylet pathways: 34+1+6+3+2+2=48. Percentages round (34/48=70.83%→71%; 1/48=2.08%→2%; etc.). | COMPLETE — NO_CANDIDATE_SIGNAL |
| N031 | DOC001 p. 5 narrative | Actual-use denominator is 444, distinct from randomization. 404/444=90.99%→91%; 283/444=63.74%→64%; 31/444=6.98%→7%. Signs can co-occur, so no sum test applies. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N032 | [DOC001 PDF p. 9](../../../jama_driver_2018_oi_180054.pdf#page=9), Table 5 | Fractions round: 47/371=12.67%→13%; 50/364=13.74%→14%. Composite is explicitly one count per patient despite >1 complication, so component sum is inapplicable. Outcome-specific waveform denominators are printed. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N033 | DOC001 p. 9 Table 5 | Counts and <1% displays are compatible with arm denominators (1/381=.26%, 1/376=.27%). Individual complications may co-occur; no total sum rule. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N034 | DOC001 pp. 8–9 discussion | Study-side rounded values match their defined trial displays; other numbers are explicitly external contextual reports and have no supplied raw comparator. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N035 | DOC001 pp. 9–10 | 25/376=6.65%→7% supports the protocol-violation repeat; 31/444=6.98%→7% supports resistance repeat; 362+366=728/757=96.17% (>96%). | COMPLETE — NO_CANDIDATE_SIGNAL |
| N036 | [DOC002 PDF pp. 8–9](../../../joi180054supp1_prod.pdf#page=8) | Protocol attempt/switch boundary is a definition, not an arithmetic display. Exact comparator is deferred to cross-source review. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N037 | DOC002 p. 9 | Hypoxemia definition uses percentage/percentage-point thresholds consistently; no reported numerator/denominator to reconcile. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N038 | DOC002 p. 9 | Protocol duration endpoint is a definition; no numeric result or duplicate same-label value in this relationship. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N039 | DOC002 p. 9 | Esophageal-intubation/hypoxemia definitions distinguish event and threshold; no arithmetic comparator. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N040 | DOC002 p. 10 | Sampling every 20 seconds and a 1-minute endpoint are consistent measurement units; lowest saturation can be outside fixed intervals by explicit rule. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N041 | DOC002 p. 11 | 1:1 allocation, blocks 2/4/6/8/10, and two strata match the stated protocol definition; no block sequence to test. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N042 | DOC002 p. 12 | One-minute observation endpoint is a definition, not a count/rate. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N043 | DOC002 p. 13 | Nine listed difficult-airway characteristics are an “any” subgroup definition, so overlap is expected and no sum test applies. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N044 | DOC002 p. 14 | “Approximately 98%” is a contextual approximation without supplied numerator/denominator. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N045 | DOC002 pp. 17–18 | Second-attempt and five-working-day quantities are timing/collection rules; no result count to reconcile. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N046 | DOC002 p. 20 | ITT/primary-analysis population is defined by eligibility and device conditions; no inconsistent displayed total in this relationship. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N047 | DOC002 pp. 20–21 | Missing-data/video rule is explicit; no printed missingness count to test. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N048 | [DOC003 PDF p. 3](../../../joi180054supp2_prod.pdf#page=3) | eTable footnote consistently labels percentage-point/median differences, seconds, and waveform availability. Numerical result comparisons belong to S relationships/cross-source lane. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N049 | DOC003 p. 5 | 1–2 cm and 90° maneuver is a procedural instruction; units are unambiguous. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N050 | DOC003 p. 7 | Form categories are labels/response fields, not reported counts; medical/trauma best-choice rule avoids an inappropriate overlap sum. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N051 | DOC003 p. 8 | Ordered 0–9 scale, <=15 LPM/flush rate, and >=30° threshold have distinct units/scales and no conflicting same-field display. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N052 | DOC003 p. 9 | Form labels define medication, position, and difficult-airway fields; no reported count or inconsistent scale. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N053 | DOC003 p. 10 | First-attempt blade-in/blade-out and switch fields are definitions; exact cross-document boundary comparison is reserved for cross-source checking. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N054 | DOC003 pp. 11–12 | Second-attempt/rescue/confirmation fields are non-exclusive capture fields, not a numeric total. | COMPLETE — NO_CANDIDATE_SIGNAL |
| N055 | DOC003 p. 13 | Complication labels and 5-minute time boundary are definitions; selectable complications may co-occur and no count is displayed. | COMPLETE — NO_CANDIDATE_SIGNAL |

## Proposed candidate signals requiring human adjudication

### Signal 1 — final-intubator category counts exceed the Bougie arm total (N024)

- **Exact source location:** [DOC001 PDF p. 6, Table 2](../../../jama_driver_2018_oi_180054.pdf#page=6), “Operator” rows and footnote f; corroborated by fresh OCR `preprocessing/ocr_text/DOC001-page-006.txt` lines 36–39 and fresh rendered page `preprocessing/rendered_pages/DOC001-page-006.png`.
- **Printed inputs:** Bougie arm `n=381`; emergency-medicine senior resident/fellow `318 (83%)`, junior resident `57 (15%)`, faculty `8 (2%)`. Footnote f: “This lists the final intubating physician.”
- **Rule and calculation:** Final-intubator categories should assign one final physician per patient within the `n=381` arm. `318 + 57 + 8 = 383`; `383 − 381 = 2` excess assignments. Each count individually rounds to its printed percentage (83.46%, 14.96%, 2.10%), so rounding cannot remove a two-count excess.
- **Direct observation versus inference:** Direct observation is the three printed counts, arm denominator, and final-physician footnote. The inference is that the categories are intended to be mutually exclusive/exhaustive final-intubator categories; that follows from the singular final-physician wording, but the source does not explicitly state whether a patient could be counted in more than one displayed training category.
- **Alternative source-grounded interpretation:** A training-category overlap, a change of intubating physician (the same footnote states eight changes total), or a denominator/row transcription issue could explain the excess; the table does not say which applies.
- **Quality-control relevance:** If confirmed, the operator-composition denominators or row labels cannot all describe one final-intubator distribution and could be copied incorrectly in descriptive extraction.
- **Exact human question:** “For the Bougie arm, are the three final-intubator rows intended to be mutually exclusive per patient, and if so, which printed numerator or denominator should reconcile 318+57+8 with 381?”

### Signal 2 — patient-position category counts do not exhaust either randomized-arm denominator (N021)

- **Exact source location:** [DOC001 PDF p. 6, Table 2](../../../jama_driver_2018_oi_180054.pdf#page=6), “Patient position for intubation” rows; fresh OCR `preprocessing/ocr_text/DOC001-page-006.txt` lines 28–34 and rendered page `preprocessing/rendered_pages/DOC001-page-006.png`.
- **Printed inputs:** Bougie `n=381`: sniffing `222 (58%)`, neutral cervical spine `117 (31%)`, cervical spine extension without sniffing `39 (10%)`. ETT+stylet `n=376`: `244 (65%)`, `96 (26%)`, `32 (9%)`.
- **Rule and calculation:** If these are the complete position categories in the displayed section, each arm’s category counts should equal its arm total. Bougie: `222+117+39=378`, deficit `381−378=3`. ETT+stylet: `244+96+32=372`, deficit `376−372=4`. Printed percentages individually round correctly; the deficits are counts, not rounding artifacts.
- **Direct observation versus inference:** Direct observation is the displayed section heading, three category rows, and arm denominators. The inference is exhaustiveness: the table contains no printed other-position or missing-position row, but does not explicitly say these are all possible positions.
- **Alternative source-grounded interpretation:** Unshown/missing position values or a category not displayed in Table 2 could account for the deficits; footnote c defines only the sniffing position and does not provide a missingness count.
- **Quality-control relevance:** A confirmed mismatch would affect interpretation of descriptive process-category frequencies and their denominators.
- **Exact human question:** “Do the three printed patient-position rows exhaust Table 2’s randomized arm denominators? If yes, please reconcile the deficits of 3 Bougie and 4 ETT+stylet patients; if no, identify the omitted/missing category and its counts.”

### Signal 3 — video-screen-use category sums are below their stated available-data denominators (N026)

- **Exact source location:** [DOC001 PDF p. 6, Table 2](../../../jama_driver_2018_oi_180054.pdf#page=6), “Video screen use for video laryngoscopy” rows and footnote g; fresh OCR `preprocessing/ocr_text/DOC001-page-006.txt` lines 44–47 and rendered page `preprocessing/rendered_pages/DOC001-page-006.png`.
- **Printed inputs:** Bougie: screen never `218/377 (58%)`, entire attempt `78/377 (21%)`, during passage `75/377 (20%)`. ETT+stylet: `182/372 (49%)`, `90/372 (24%)`, `98/372 (26%)`. Footnote g says four values were missing in each group.
- **Rule and calculation:** The shared denominators equal the randomized group sizes less four (`381−4=377`; `376−4=372`). If the three displayed use categories are exhaustive for available data: Bougie `218+78+75=371`, leaving `6`; ETT+stylet `182+90+98=370`, leaving `2`. Individual percentages round correctly.
- **Direct observation versus inference:** Direct observation is the three count/denominator rows and explicit four-missing-per-arm footnote. The inference is that “never,” “entire attempt,” and “during passage” are exhaustive screen-use categories; they appear as the only rows under that heading, but the source does not explicitly define every possible viewing pattern.
- **Alternative source-grounded interpretation:** There may be an unprinted intermediate viewing category, additional unknown screen-use data beyond footnote g, or a table transcription/denominator issue.
- **Quality-control relevance:** If confirmed, the stated screen-use denominator or category distribution is internally incomplete, affecting a process-measure comparison that may be extracted as a proportion.
- **Exact human question:** “Are the three video-screen-use rows intended to partition all nonmissing observations? If so, what accounts for the six Bougie and two ETT+stylet observations not represented by their stated denominators?”

### Signal 4 — Table 1 oxygenation denominators conflict with its stated oxygen-saturation missingness (N013)

- **Exact source location:** [DOC001 PDF p. 5, Table 1 and footnote b](../../../jama_driver_2018_oi_180054.pdf#page=5); fresh OCR `preprocessing/ocr_text/DOC001-page-005.txt` and rendered page `preprocessing/rendered_pages/DOC001-page-005.png`.
- **Printed inputs:** Table 1 oxygenation rows are `44/352 (13%)` and `21/352 (6%)` for Bougie (`n=381`) and `40/344 (12%)` and `11/344 (3%)` for ETT+stylet (`n=376`). Footnote b states that `43` patients lacked oxygen saturation before intubation, split `19` Bougie and `24` ETT+stylet.
- **Rule and calculation:** For the displayed oxygenation denominators, missing values are `381−352=29` in Bougie and `376−344=32` in ETT+stylet, total `61`. This conflicts with the footnote’s printed oxygen-saturation missingness `19+24=43`. All four proportions themselves round correctly, so the inconsistency is the denominator/missingness identity rather than percentage rounding.
- **Direct observation versus inference:** Direct observation is the two group totals, two available-data denominators, and the footnote’s three oxygen-saturation missingness values. The inference is that the footnote’s phrase “oxygen saturation ... respectively” refers to the same baseline oxygen-saturation availability summarized by Table 1; both appear in the same table and describe availability before intubation.
- **Alternative source-grounded interpretation:** The footnote may have transposed the vital-sign labels or their group splits, or the oxygenation rows may use a different availability time point not stated in the table. The source supplies no distinct definition that reconciles 352/344 with 19/24 missing.
- **Quality-control relevance:** If confirmed, the available-data denominator for baseline oxygenation or the associated missingness description is misstated, which can affect extraction of baseline prevalence and missing-data handling.
- **Exact human question:** “Which Table 1 values are correct for baseline oxygen-saturation availability: denominators 352 and 344 (implying 29 and 32 missing), or footnote b’s 19 and 24 missing; and, if both are intended, what distinct data fields/time points do they represent?”

## Limitations

- This lane evaluated numeric/reporting relationships only. Statistical compatibility, including the Table 3 duration interval ordering, is assigned to the dedicated statistical checker.
- Protocol/form definitions were checked for internal numeric unit/label coherence. Whether differently worded protocol, form, supplement, and article endpoints describe the same endpoint is assigned to cross-source checking.
- Fresh OCR was used as a locator and fresh rendered pages were visually consulted for Table 2; direct PDFs remain the source evidence.

## Completion counts

- Relationships assigned and completed: 55/55 (`N001`–`N055`).
- `NO_CANDIDATE_SIGNAL`: 51.
- `PROPOSED_CANDIDATE_SIGNAL`: 4 (Signals 1–4).
