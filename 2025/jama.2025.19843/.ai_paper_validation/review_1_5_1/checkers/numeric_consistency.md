# Numeric Consistency Check

## Scope, evidence standard, and method

Independent numeric/reporting review of the complete canonical numeric inventory, `N001` through `N052`, using `relationships/numeric_relationship_inventory.md`, both numeric mapping parts, both quantitative evidence maps, and direct supplied-PDF confirmation. Direct PDFs are authoritative; extracted text and rendered pages were used as locators or transcription aids. No legacy candidate, checker, queue, verifier, critic, endetail, or final-report content was consulted.

Checks applied when applicable were exact count and subgroup summation; numerator/denominator/percentage recomputation; reported difference direction and one-decimal rounding (tolerance 0.05 percentage point for a displayed one-decimal percentage or percentage-point difference, and 0.5 day for a displayed whole-day rounded restricted mean); population and missing-denominator compatibility; matched figure/table/narrative occurrence; measure, unit, reference-group, and rate-versus-count labels. A matched planned-versus-observed value was not treated as a contradiction where the source identifies one as planned and the other as realized.

## Complete relationship outcomes

| Stable ID | Checked inputs and direct-source locations | Result / calculation / tolerance | Outcome |
|---|---|---|---|
| N001 | Main PDF p4 Fig 1; p1 abstract | 209 assessed - 4 excluded = 205; 101 + 104 = 205, matching abstract. | CHECKED_NO_CANDIDATE |
| N002 | Main PDF p4 Fig 1 | Four one-person exclusion lines sum to 4. | CHECKED_NO_CANDIDATE |
| N003 | Main PDF p3 analysis population; p4 Fig 1 | ITT statement and primary-analysis boxes retain randomized 101 and 104. | CHECKED_NO_CANDIDATE |
| N004 | Main PDF p4 Fig 1 | 101/101 received levosimendan; 102/104 received placebo and 2/104 did not; 102 + 2 = 104. | CHECKED_NO_CANDIDATE |
| N005 | Main PDF p4 Fig 1 and intervention narrative | Definitive interruption 11 + 3 = 14, matching narrative. | CHECKED_NO_CANDIDATE |
| N006 | Main PDF p4 Fig 1 and narrative | Two lost follow-up are explicitly partitioned 1 before plus 1 after primary-end-point collection; no asserted missing primary denominator. | CHECKED_NO_CANDIDATE |
| N007 | Main PDF p1, p4, p5 Table 1 | Women 26 + 30 = 56 and men 75 + 74 = 149; 56/205 = 27.317% and 149/205 = 72.683%, each rounds as printed. | CHECKED_NO_CANDIDATE |
| N008 | Main PDF p1, p4, p5 Table 1 | Postcardiotomy 39 + 40 = 79 (38.5%); MI 29 + 27 = 56 (27.3%); myocarditis 12 + 16 = 28 (13.7%). | CHECKED_NO_CANDIDATE |
| N009 | Main PDF p5 Table 1 | Sex rows: 26 + 75 = 101 and 30 + 74 = 104; each printed percentage agrees within 0.05 percentage point. | CHECKED_NO_CANDIDATE |
| N010 | Main PDF p5 Table 1 | Etiology rows: 39 + 29 + 12 + 21 = 101; 40 + 27 + 16 + 21 = 104; percentages reconcile to arm denominators within rounding tolerance. | CHECKED_NO_CANDIDATE |
| N011 | Main PDF p5 Table 1 | Age, BMI, and ECMO-time medians/IQRs are correctly labelled with units; ECMO-time available n=99 is explicitly printed and is not a percentage denominator conflict. | CHECKED_NO_CANDIDATE |
| N012 | Main PDF p5 Table 1 and footnotes | SOFA 12 (10-15), n=98 versus 12 (9-14), n=100, range 0-24; SAPS II labels and 0-163 scale are coherent. | CHECKED_NO_CANDIDATE |
| N013 | Main PDF p5 Table 1 | Ventilation: 87/101 = 86.14% -> 86.1 and 80/104 = 76.92% -> 76.9. KRT: 9/101 = 8.91% -> 8.9 and 15/104 = 14.42% -> 14.4. | CHECKED_NO_CANDIDATE |
| N014 | Main PDF p5 Table 1 | Placebo history rows expressly use available denominator 103: 40/103=38.8%, 33/103=32.0%, 21/103=20.4%; no conflation with randomized n=104. | CHECKED_NO_CANDIDATE |
| N015 | Main PDF p5 Table 1 | LVEF n=82/94, VTI n=76/91, and MAP n=100/103 are printed as available observations; units (%/cm/mm Hg) agree with labels. | CHECKED_NO_CANDIDATE |
| N016 | Main PDF p5 Table 1 | pH: 8/101=7.9%, 11/104=10.6%; lactate: 53/101=52.5%, 47/104=45.2%; creatinine: 47/101=46.5%, 43/104=41.3%. | CHECKED_NO_CANDIDATE |
| N017 | Main PDF p5 Table 1 | ALT: 52/99=52.525% -> 52.5%; 49/103=47.573% -> 47.6%. Denominators match explicitly printed available ALT n. | CHECKED_NO_CANDIDATE |
| N018 | Main PDF p5 Table 1 | AST: 81/99=81.818% -> 81.8%; 80/104=76.923% -> 76.9. The unbracketed placebo denominator is 104, consistent with percentage. | CHECKED_NO_CANDIDATE |
| N019 | Main PDF p5 Table 1 and footnote e | Medication counts/percentages agree with n=101/104 to one decimal; dose and inotropic-score units/formula are labelled, not rates or event counts. | CHECKED_NO_CANDIDATE |
| N020 | Main PDF p1 abstract; p4 intervention narrative | 0.20 +/- 0.01 escalation is consistently labelled micrograms/kg/min; 93% versus 96% is an arm-specific descriptive percentage, while 97% initial-dose statement is overall. No incompatible denominator is claimed. | CHECKED_NO_CANDIDATE |
| N021 | Main PDF p1, p4, p6 Table 2, p7 Fig 3 | 69/101=68.3168% and 71/104=68.2692%, both 68.3%; unrounded difference 0.0475 percentage point -> 0.0 within 0.05-point rounding tolerance. | CHECKED_NO_CANDIDATE |
| N022 | Main PDF p6 Table 2 footnote d; Supplement 3 p10 eFigure 1 | Levosimendan 69 success + 15 failure + 15 death + 2 censored=101; placebo 71+21+12=104. eFigure 1 separately partitions failures (11+4=15; 12+5+4=21), matching the Table 2 definition. | CHECKED_NO_CANDIDATE |
| N023 | Main PDF p6 Table 2 | Success, failure, and death percentage-point differences recompute to +0.0475 -> 0.0, -5.260 -> -5.3, and +3.346 -> 3.3; bootstrap CIs are not independently recomputable from printed aggregates but labels and endpoints are coherent. | CHECKED_NO_CANDIDATE |
| N024 | Main PDF p6 Table 2 | D30 mortality: 26/101=25.743% ->25.7; 23/104=22.115% ->22.1; difference 3.628 ->3.6. | CHECKED_NO_CANDIDATE |
| N025 | Main PDF p1, p4, p6 Table 2; Supplement 3 p11 eFigure 2 | D60 mortality: 28/101=27.723% ->27.7; 26/104=25.000%; difference 2.723 ->2.7. Figure terminal counts 28/26 and narrative/table match. | CHECKED_NO_CANDIDATE |
| N026 | Main PDF p1, p4, p6 Table 2 | ECMO-free and ECMO-duration values have matching median/IQR and day labels; displayed median differences 24-23=1 and 5-6=-1 agree. | CHECKED_NO_CANDIDATE |
| N027 | Main PDF p6 Table 2; Supplement 3 p16 eFigure 7 | Hospital 28 versus 35 and difference -7 match supplement RMST labels. ICU 18 versus 19 in whole-day Table 2 corresponds to Supplement eFigure 7 labels 17.5 and 19; differing displayed precision permits whole-day rounding (tolerance 0.5 day), not a contradiction. | CHECKED_NO_CANDIDATE |
| N028 | Main PDF p1, p6 Table 2, p7 Table 3 and narrative | 18/101=17.822% ->17.8; 9/104=8.654% ->8.7; difference 9.168 ->9.2. Same ventricular-arrhythmia definition is stated in Table 2 footnote and repeated consistently. | CHECKED_NO_CANDIDATE |
| N029 | Main PDF p7 Table 3 | Serious AE: 59/101=58.416% ->58.4, 61/104=58.654% ->58.7, difference -0.238 ->-0.2. Any arrhythmia: 63/101=62.376% ->62.4, 55/104=52.885% ->52.9, difference 9.491 ->9.5. | CHECKED_NO_CANDIDATE |
| N030 | Main PDF p7 Table 3 | AF, supraventricular tachyarrhythmia, and bradycardia counts reproduce printed percentages and ARDs within one-decimal rounding. Categories are not presented as mutually exclusive. | CHECKED_NO_CANDIDATE |
| N031 | Main PDF p7 Table 3 | Zero torsades values are counts, not a displayed P value. VF/VT-shock, hypokalemia, and cessation-event percentages/ARDs recompute within tolerance. Categories are not claimed to partition all events. | CHECKED_NO_CANDIDATE |
| N032 | Main PDF p6 Fig 2 | Risk-set counts and cumulative event counts are separately labelled; no rule requires their subtraction or equality because Figure 2 shows competing events and is truncated at day 15. Counts remain within allocated totals. | CHECKED_NO_CANDIDATE |
| N033 | Main PDF p6 Fig 2 caption | 11 (IQR 9-20) versus 16 (12-19) days are explicitly reverse-Kaplan-Meier median observation times, correctly distinguished from event counts or median ECMO duration. | CHECKED_NO_CANDIDATE |
| N034 | Main PDF p7 Fig 3; p5 Table 1; p6 Table 2 | Each subgroup numerator/total recomputes to printed percentage; totals across four etiologies equal 104 placebo and 101 levosimendan, and all-patient 71/104 and 69/101 match Table 2. | CHECKED_NO_CANDIDATE |
| N035 | Main PDF p8 discussion/limitations; p1/p6 Table 2 | “>95%,” 68%, and 26% are deliberately coarse discussion repeats of arm-specific values. Planned 50% versus observed 32% refers to weaning-failure design assumption versus observed aggregate failure and is explicitly contextualized; not a same-population numeric conflict. | CHECKED_NO_CANDIDATE |
| N036 | Supplement 1 pp14,37; Supplement 2 pp3,6 | Endpoint definition consistently distinguishes successful-weaning event, competing outcomes, and day-30 censoring; no count/proportion contradiction. | CHECKED_NO_CANDIDATE |
| N037 | Supplement 1 p10,37; Supplement 2 p5 | Planned 206=103+103 and 101-event, 50%-control-CIF inputs agree across protocol/SAP. Actual randomized n=205 is clearly an observed enrollment result, not printed as the planned target. | CHECKED_NO_CANDIDATE |
| N038 | Supplement 1 p16; Supplement 2 p5 | 1:1 allocation, ITT population, and minimization factors match main-report labels; no numeric population mismatch. | CHECKED_NO_CANDIDATE |
| N039 | Supplement 1 pp141-153 | 13-to-14-site and recruitment-rate changes occur in explicit amendment history; retained planned n=206 is not falsely asserted as actual enrollment. | CHECKED_NO_CANDIDATE |
| N040 | Supplement 3 p3 eTable 1 | Emergency 69+77=146; surrogate 32+27=59; 146+59=205. Each consent-status row sums to its shown denominator and row percentages recompute within tolerance. | CHECKED_NO_CANDIDATE |
| N041 | Supplement 3 pp5-6 eTable 3 | Table labels medians/IQRs versus n(%) and percentage-point differences versus RR; stated zero-cell no-RR rule is applied to displayed zero-event rows. No rate/count or measure-label contradiction. | CHECKED_NO_CANDIDATE |
| N042 | Supplement 3 pp5-6 eTable 3; main PDF p6 Table 2 | D30 MACE 35/101=34.7%, 36/104=34.6%; D60 36/101=35.6%, 39/104=37.5%. Difference directions and main/supplement population labels agree. | CHECKED_NO_CANDIDATE |
| N043 | Supplement 3 p7 eTable 4 | Daily drug-dose entries distinguish available n from median/IQR dose; sparse epinephrine cells shown as dash are not denominators or zeros. No printed arithmetic total is asserted. | CHECKED_NO_CANDIDATE |
| N044 | Supplement 3 p8 eTable 5 | Exposure percentages reproduce 93/101=92.1, 96/104=92.3, 8/101=7.9, 5/104=4.8, 98/104=94.2, 14/101=13.9, and 12/104=11.5. Durations are medians/IQRs, not event rates. | CHECKED_NO_CANDIDATE |
| N045 | Supplement 3 p9 eTable 6 | Each six-category arm total is 21. Every n/21 percentage agrees within 0.05 percentage point; categories form the stated “other” etiology subset. | CHECKED_NO_CANDIDATE |
| N046 | Supplement 3 p10 eFigure 1; main PDF p6 Table 2 | Trajectory stacks total 101 and 104. Their success/failure/death/censoring groupings reconcile to Table 2 as documented for N022. | CHECKED_NO_CANDIDATE |
| N047 | Supplement 3 p11 eFigure 2; main PDF p6 Table 2 | D30 terminal deaths 26 versus 23 and D60 28 versus 26 match Table 2. Risk sets and cumulative events are correctly separately labelled. | CHECKED_NO_CANDIDATE |
| N048 | Supplement 3 p13 eFigure 4; pp5-6 eTable 3 | D30 terminal MACE 35 levosimendan/36 placebo and D60 36/39 match eTable 3; figure’s cumulative-event label is not confused with a proportion. | CHECKED_NO_CANDIDATE |
| N049 | Supplement 3 p14 eFigure 5 | Figure labels mean blood pressure in mm Hg, seven time points, total plotted n, and a 60-mm-Hg reference. No exact plotted mean is claimed as a table value, so no unsupported visual-coordinate arithmetic was applied. | CHECKED_NO_CANDIDATE |
| N050 | Supplement 3 pp15-16 eFigures 6-7; pp7 eTable 4; main PDF p6 Table 2 | eFigure 6 is an appropriately labelled graphical rendering of eTable 4 trajectories. eFigure 7 hospital/ICU RMST labels agree with main results at their respective displayed precisions (see N027). | CHECKED_NO_CANDIDATE |
| N051 | Supplement 3 p17 eFigure 8 | Levosimendan frequencies 42+22+19+8+2+4+2+2=101; placebo 43+31+13+4+6+3+1+2+1=104. Zero-serious-AE frequencies also imply 59 and 61 with any serious AE, matching main Table 3. | CHECKED_NO_CANDIDATE |
| N052 | Supplement 4 pp1-3; Supplement 5 p1 | Collaborator roster and data-sharing statement contain no quantitative study-result relationship; administrative NCT identifier is not a result count. | CHECKED_NO_CANDIDATE |

## Candidate proposals

No distinct document-grounded numeric-consistency candidate was identified in `N001`-`N052`.

The principal apparent precision difference was independently checked: main Table 2 displays ICU restricted-mean stay as 18 days while Supplement 3 eFigure 7 displays 17.5 days. The values use different stated display precision and do not exceed the applicable whole-day rounding tolerance; therefore this is recorded under N027/N050 as `CHECKED_NO_CANDIDATE`, not a candidate proposal.

## Limitations

Bootstrap confidence intervals, hazard ratios, and other model-derived quantities cannot be regenerated from printed aggregate data alone and were checked here only for printed measure labels, matched population/timepoint, direction, and arithmetic inputs. Graphical curves were not reverse-engineered from coordinates when exact values were not printed. These limitations do not leave an unreviewed N relationship.

## Coverage summary

- Canonical numeric relationships checked: 52 of 52 (`N001`-`N052`).
- Qualifying candidate proposals: 0.
- Direct-source pages visually confirmed for figure-dependent arithmetic: main PDF pp4, 6-7 and Supplement 3 pp10-11; remaining cited direct-source PDF locations were confirmed with direct layout text and source-matched evidence maps.
