# Numeric supporting relationship inventory

Runtime: /root/numeric_support; model gpt-6.1-sol; reasoning medium; fresh optional numeric shard. Status: COMPLETE. Exact scope: DOC-003 REPORT eFigure source p.13 and eTables1–11 source pp.14–25, including every row, column, denominator, percentage, sample size, interval and model label. Main article numeric, cross-document comparisons and inferential test logic belong to separately assigned reviewers.

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely. Evidence: source-linked support map lines1–689, direct Poppler26.01.0 layout extraction of source pp.14–25, and reusable full-page source renders pp.14,15,20,24 visually inspected for all qualifying printed pair discrepancies. Direct eMethods pp.9–12 inspected for definitions and missing-data model. No old conclusions or web consulted. Direct extraction command: `pdftotext -layout -f 14 -l 25 joi240147supp2_prod_1738701765.29201.pdf /tmp/numeric-support-direct.txt`; direct native definitions command `pdftotext -f 9 -l 12 joi240147supp2_prod_1738701765.29201.pdf -`. All reusable/source files preserved. CPU; this new transcription is not a reused asset. The temporary output was relocated without changing its content to `preprocessing/numeric-support-direct.txt` under the permitted review directory; the historical extraction command above records the original execution.

Stable groups N201–N242 cover all200 printed numerator/denominator/percentage cells: eTable1 50; eTable2 52; eTable3 12; eTable4 6; eTable5 18; eTable7 26; eTable8 6; eTable9 14; eTable10 4; eTable11 12. There are92 estimate/interval sets,66 with P values; their complete printed arrays are preserved below for identity checks, with statistical compatibility assigned to the statistical lanes. All continuous group medians, IQRs and n and all three eFigure panels are retained through the linked complete evidence transcription.

Percentage rule: each integer numerator/denominator gets half-unit intervals, nonnegative numerator bound at zero; printed one-decimal percentage gets±.05 and integer percentage±.5. Recomputed percent interval is100×[max(0,n−.5)/(d+.5),(n+.5)/(d−.5)]. Interval gap divided by absolute printed percentage above.05 qualifies. Counts and totals use analogous interval sums. No group sum is imposed on overlapping event or procedure categories.

| Relationship ID | Exact REPORT source | All assigned arithmetic/identity cells | Check result |
|---|---|---|---|
| N201 | DOC-003 p.13 | eFigure A: SpO2 medians/IQR, Pre and H1–H8 | All restrictive/liberal curves and aggregate97(96–99)/100(99–100); no count arithmetic or measure-identity discrepancy. Graphical endpoints remain approximate. |
| N202 | DOC-003 p.13 | eFigure B: oxygen flow H1–H8 | All restrictive/liberal curves, L/min, aggregate0(0–1)/12(12–15); median-of-record summaries need not equal individual hourly medians. |
| N203 | DOC-003 p.13 | eFigure C: FiO2 H1–H8 | All curves and aggregate.28(.21–.36)/.60(.60–.80); fraction scale retained. |
| N204 | DOC-003 p.14 | eTable1 prehospital enrollment: all15 rows | Restrictive numerators308 and liberal307, each denominator750/758; all30 percentage cells reconcile. |
| N205 | DOC-003 p.14 | eTable1 in-hospital enrollment: all5 rows | Restrictive442 and liberal451; enrollment totals308+442=750,307+451=758; all10 percentage cells reconcile. |
| N206 | DOC-003 p.14 | eTable1 receiving center: all5 rows | Counts sum750/758, combined1508. All10 percentage cells checked; Bern pair F-NUM-101, four small Rigshospitalet/Odense gaps excluded. |
| N207 | DOC-003 p.15 | eTable2 BMI | 25.0(22.5–28.1),n628 versus25.0(22.8–27.8),n615; samples within headers750/758, quartile order preserved. |
| N208 | DOC-003 p.15 | eTable2 mechanism: all13 rows | Counts sum742/756;26 percentage cells reconcile. Restrictive firearm denominator724 differs from742 but screen precision. |
| N209 | DOC-003 p.15 | eTable2 transport: all6 rows | Counts sum747/743; all12 percentage cells checked; liberal walk-in F-NUM-102. |
| N210 | DOC-003 p.15 | eTable2 previous oxygen/highest SpO2 | 333/713(46.7),351/718(48.9);100(97–100),n265 and99(97–100),n285; reconcile. |
| N211 | DOC-003 p.15 | eTable2 admission temperature | 36.5(35.9–37.0),n479 versus36.5(35.9–36.9),n484; no count/scale conflict. |
| N212 | DOC-003 p.15 | eTable2 resuscitation surgery: all6 rows | All12 percentage cells checked; categories not stated mutually exclusive. Liberal vascular F-NUM-103; others reconcile. |
| N213 | DOC-003 p.16 | eTable3 trauma-to-randomization | 54(35–79),n633 versus52(33–78),n635;633+635=1268 printed total. |
| N214 | DOC-003 p.16 | eTable3 oxygen category: all4 rows | Restrictive200+171+18+350=739; liberal13+45+340+337=735. All8 percentage cells reconcile and sum100% within rounding; majority/tie/category priority retained. |
| N215 | DOC-003 p.16 | eTable3 hemoglobin/lactate: all4 rows | Hemoglobin n602/603 and482/487; lactate n585/590 and472/479; all medians/IQR within intervals and counts within allocation totals. |
| N216 | DOC-003 p.16 | eTable3 major violations/deviations | 50/742(6.7),102/744(13.7);40/741(5.4),17/738(2.3). Reconcile;750−50=700,758−102=656 match eTable8 PP headers. |
| N217 | DOC-003 p.17 | eTable4 primary/key secondary counts: all3 rows | All6 percentages reconcile. Restrictive composite118,death63,respiratory65 imply overlap10; liberal121,53,78 imply10; unions valid. Available733/724 imply missing17/34. |
| N218 | DOC-003 p.17 | eTable4 first model: all3 rows | OR/CI/P retained; label OR with modeled/IPW context, not crude RR. No evidenced measure substitution. |
| N219 | DOC-003 p.17 | eTable4 adjusted model: all3 rows | All three OR/CI/P sets retained; adjusted values not required to equal crude count OR. |
| N220 | DOC-003 p.17 | eTable4 adjusted plus smoking: all3 rows | All three OR/CI/P sets retained; active-smoking definition retained. |
| N221 | DOC-003 p.18 | eTable5 all9 outcome count rows | All18 percentage cells reconcile, including0/738(0.0) and1/730(0.1). Counts/n differ by endpoint/eligibility; no forced column sum. |
| N222 | DOC-003 p.18 | eTable5 all3 model columns, all9 rows | 24 OR/CI/P sets and three MI dash sets retained; modeled context explains crude-ratio differences. ICU admission count linked to N227/F-NUM-106. |
| N223 | DOC-003 p.19 | eTable6 all6 group descriptive rows | All12 median/IQR/n sets retained; n165/161,735/725,735/723,368/357,736/724,736/728. Quartile order and counts coherent. |
| N224 | DOC-003 p.19 | eTable6 all3 mean-difference columns, all6 rows | 18 MD/CI/P sets retained. Median summaries cannot reproduce means; no evidenced OR/RR/rate identity conflict. |
| N225 | DOC-003 p.20 | eTable7 all-patient row | 118/733(16.1),121/724(16.7); both OR columns retained. Same counts as eTable4. |
| N226 | DOC-003 p.20 | eTable7 intubation No/Yes | 56+62=118,558+175=733;50+71=121,543+181=724. All4 percentages reconcile; four OR/CI sets retained. |
| N227 | DOC-003 p.20 | eTable7 ICU No/Yes | 42+74=116,458+271=729;50+68=118,481+238=719. All4 percentages reconcile; subgroup Yes count inconsistent with eTable5 ICU admission under feasible overlap, F-NUM-106. |
| N228 | DOC-003 p.20 | eTable7 AIS<3/≥3 | 45+73=118,500+233=733;48+73=121,473+202=675. Liberal AIS<3 percentage F-NUM-104. Denominator subtotal deficit49 alone does not establish exhaustive ascertainment. |
| N229 | DOC-003 p.20 | eTable7 lung disease No/Yes | 97+19=116,667+59=726;105+14=119,643+69=712. All4 percentages reconcile within precision, including14/69(20.2). Missing subgroup values may reduce totals. |
| N230 | DOC-003 p.20 | eTable7 site prehospital/in-hospital | 48+70=118,303+430=733;54+67=121,296+428=724. All4 percentages reconcile. |
| N231 | DOC-003 p.21 | eTable7 ISS≤15/>15 | 22+95=117,380+352=732;19+100=119,389+329=718. All4 percentages reconcile; reduced totals compatible with unavailable ISS. |
| N232 | DOC-003 p.22 | eTable8 PP counts: all3 rows | Header700/656. All6 percentages reconcile. Composite104,death54,respiratory58 imply overlap8; liberal105,44,69 imply8. Respiratory n685/629 versus683/627 can reflect outcome availability. |
| N233 | DOC-003 p.22 | eTable8 all3 model columns, all3 rows | Nine OR/CI/P sets retained with same modeled measure caveat; not relabeled as crude. |
| N234 | DOC-003 p.23 | eTable9 both AE rows | 207/750(27.6),263/758(34.7),16/750(2.1),20/758(2.6); all4 percentage cells reconcile. |
| N235 | DOC-003 p.23 | eTable9 all5 SAE rows | All10 percentage cells reconcile. Different SAE categories not stated disjoint. Death63/53 agrees eTable4 numerator; headers differ by footnote follow-up rule, not contradiction. No SAR/SUSAR registered. |
| N236 | DOC-003 p.24 | eTable10 exclusion-after-randomization pairs | 55/750(45),67/758(55): both denominator/percentage pairs F-NUM-105.45/55 percentages approximate55/122 and67/122. |
| N237 | DOC-003 p.24 | eTable10 secondary-exclusion pairs | 174/750(51),165/758(49): both pairs F-NUM-105.174+165+2 missing allocation=341 footnote; percentages approximate174/339 and165/339. |
| N238 | DOC-003 p.24 | eTable10 exclusion-after-randomization stated total | Printed130 versus55+67=122; half-unit sum interval121–123 and total129.5–130.5 yield relative gap6.5/130=.05, excluded. |
| N239 | DOC-003 p.25 | eTable11 primary missing-as-none/all rows | 118/750(15.7),121/758(16.0);135//750(18.0),155/758(20.4). Percentages reconcile; differences17/34 equal eTable4 missingness. |
| N240 | DOC-003 p.25 | eTable11 death missing-as-none/all rows | 63/750(8.4),53/758(7.0);80/750(10.7),87/758(11.4). Percentages reconcile within precision; differences17/34. |
| N241 | DOC-003 p.25 | eTable11 respiratory missing-as-none/all rows | 65/750(8.7),78/758(10.3);82/750(10.9),112/758(14.8). All percentages reconcile; differences17/34. |
| N242 | DOC-003 p.25 | eTable11 all6 OR/CI/P sets | Model-based OR retained; no crude OR/RR identity inference. Double slash135//750 is notation only, without numeric change. |

## eFigure quantitative visual transcription: DOC-003 p13

PanelA SpO2(%): x=Pre,1,2,3,4,5,6,7,8hours; yaxis break to0,then93–100 in1-unit ticks. Restrictive median Pre97,H1 97,H2 98,H3–H8 97;IQR approximately Pre93–99,H1 95–100,H2 96–100,H3 96–99,H4 96–99,H5 96–99,H6 96–99,H7 95–99,H8 96–99. Liberal Pre97,H1–H8 100;IQR approximately Pre93–99,H1 100–100,H2 100–100,H3 99.75–100,H4 100–100,H5 99.5–100,H6–H8 99–100. Noninteger endpoints are graphical approximations, not printed numeric labels.

PanelB oxygenflow(L/min),H1–H8;axis0,3,6,9,12,15. Restrictivemedian0allhours,IQRH1 0–2,H2–H8 0–1. Liberalmedian15,13,12,12,12,12,12,12;IQRgraphapproximatelyH1 15–15,H2 12–15,H3–H4 10–15,H5–H6 10–13.25,H7–H8 5–12. Printedaggregate medians/IQR are liberal12(12–15),restrictive0(0–1).

PanelC FiO2,H1–H8;axis.21,.30,.40,.50,.60,.70,.80,.90,1.00. Restrictivemedianapproximately.32,.30,.29,.27,.25,.25,.25,.25;IQRapproximately.25–.45,.24–.40,.22–.39,.21–.36,.21–.35,.21–.35,.21–.35,.21–.34. Liberalmedianapproximately.98,.65,.60,.60,.60,.60,.60,.60;IQRapproximately.63–1.00,.60–.99,.60–.80,.60–.70,.60–.65,.60–.65,.60–.62,.60–.60. Printedaggregates liberal.60(.60–.80),restrictive.28(.21–.36). Caption definitions and numeric aggregate annotations are source printed; graphical endpoint approximations are clearly distinguished and do not pretend exact data recovery.

## Complete structured result tables for bounded checker reads

The following direct layout transcriptions preserve every row and column of eTables1–11, including all counts, denominators, percentages, medians/IQR/n, estimates, confidence intervals, P values, labels and footnotes. Source pages appear in order14,15,16,17,18,19,20,21,22,23,24,25; each printed page number is the exact PDF page. Restrictive precedes liberal. Inferential columns appear in source order: odds ratio or mean difference, P; adjusted measure, P; adjusted plus smoking, P. eTable7 has two OR/CI columns and no P column; eTable11 has one OR/CI/P column. These columns are labels in the supplied display; no inference that the first model is crude is introduced. The values were visually checked against all12 reusable full-page renders and freshly extracted using direct Poppler pdftotext26.01.0 CPU `-layout -f 14 -l 25`, output preprocessing/support-current/DOC-003-tables14-25-layout.txt. This section is the authoritative compact row/column map for SUP031–SUP040. Read this section together with SUP025–SUP030 and the plan register; the complete native appendix is retained for provenance and exhaustive page coverage.

```text
                                                                                                                  14


4.2 eTables

 eTable 1. Additional Characteristics of Patient Enrollment Location and
 Receiving Trauma Center
                                                                                 Restrictive        Liberal
 Characteristics                                                                oxygen group     oxygen group
                                                                                   (N=750)          (N=758)
 Enrollment location – no./total no. (%)
  Prehospital
    Physician staffed Critical Care Unit 1 and 2 – City:
                                                                                 62/750 (8.3)     68/758 (9.0)
    Copenhagen, Denmark
    Physician staffed Critical Care Unit 3 – South:
                                                                                 25/750 (3.3)     21/758 (2.8)
    Hvidovre, Denmark
    Physician staffed Critical Care Unit 4 – North:
                                                                                 25/750 (3.3)     26/758 (3.4)
    Hilleroed, Denmark
    Physician staffed Critical Care Unit 5 – Center: Herlev,
                                                                                 34/750 (4.5)     36/758 (4.7)
    Denmark
    Danish Air Ambulance Ringsted, Denmark                                       40/750 (5.3)     37/758 (4.9)
    Danish Air Ambulance Billund, Denmark                                        21/750 (2.8)     23/758 (3.0)
    Danish Air Ambulance Skive, Denmark                                          17/750 (2.3)     18/758 (2.4)
    Danish Air Ambulance Saltum, Denmark                                          2/750 (0.3)      2/758 (0.3)
    Physician staffed Critical Care Unit: Odense, Denmark                        38/750 (5.1)     39/758 (5.1)
    Physician staffed Critical Care Unit: Aarhus, Denmark                        13/750 (1.7)     13/758 (1.7)
    Physician staffed Critical Care Unit: Randers, Denmark                        1/750 (0.1)      0/758 (0.0)
    Lifeliner 2 Helicopter Emergency Medical Services
    (including a physician-staffed ambulance vehicle),                           5/750 (0.7)      3/758 (0.4)
    Rotterdam, The Netherlands
    REGA 3, Swiss-Air Ambulance, Bern, Switzerland                               19/750 (2.5)     16/758 (2.1)
    REGA 10, Swiss-Air Ambulance, Wilderswil,
                                                                                 3/750 (0.4)      3/758 (0.4)
    Switzerland
    REGA 14, Swiss-Air Ambulance, Zweisimmen,
                                                                                 3/750 (0.4)      2/758 (0.3)
    Switzerland
  In-hospital
    Rigshospitalet, Copenhagen University Hospital,
                                                                                150/750 (20.0)   160/758 (21.1)
    Denmark
    Odense University Hospital, Odense, Denmark                                 118/750 (15.7)   117/758 (15.4)
    Aarhus University Hospital, Aarhus, Denmark                                  62/750 (8.3)     58/758 (7.7)
    Erasmus MC, University Medical Center Rotterdam,
                                                                                87/750 (11.6)    90/758 (11.9)
    Rotterdam, The Netherlands
    University Hospital Bern, Switzerland                                        25/750 (3.3)     26/758 (3.4)
 Receiving trauma center – no./total no. (%) (N=1508)
  Rigshospitalet, Copenhagen University Hospital,
                                                                                335/750 (44.4)   348/758 (45.7)
  Denmark
  Odense University Hospital, Odense, Denmark                                   173/750 (22.9)   177/758 (23.2)
  Aarhus University Hospital, Aarhus, Denmark                                   100/750 (13.3)    93/758 (12.2)
  Erasmus MC, University Medical Center Rotterdam,
                                                                                92/750 (12.2)    93/758 (12.2)
  Rotterdam, The Netherlands
  University Hospital Bern, Switzerland                                          50/750 (7.2)     47/758 (6.7)

Trauma patients allocated to either a restrictive or liberal oxygen strategy.




© 2024 American Medical Association. All rights reserved.
                                                                                                                              15



 eTable 2. Additional Characteristics of Patients
                                                                                  Restrictive                  Liberal
 Characteristics                                                                oxygen group              oxygen group
                                                                                    (N=750)                   (N=758)
                                                                                25.0 (22.5-28.1)          25.0 (22.8-27.8)
 Body Mass Index – kg/m2
                                                                                    [n=628]                   [n=615]
 Mechanism of injury – no./total no. (%)
   Traffic: Motor vehicle accident                                               147/742 (19.8)            151/756 (20.0)
   Traffic: Motorcycle accident                                                   74/742 (10.0)             70/756 (9.3)
   Traffic: Bicycle accident                                                     109/742 (14.7)            108/756 (14.3)
   Traffic: Pedestrian                                                            53/742 (7.1)              50/756 (6.6)
   Traffic: Other (eg, ship, airplane, or railway train)                          14/742 (1.9)              19/756 (2.5)
   Shot by handgun, shotgun, rifle or other firearm of any
                                                                                   8/724 (1.1)               6/756 (0.8)
   caliber
   Stabbed by knife, sword, dagger, other pointed or sharp
                                                                                   69/742 (9.3)              68/756 (9.0)
   object
   Struck or hit by blunt object                                                  51/742 (6.9)               58/756 (7.7)
   Fall: 0-2 meters                                                               82/742 (11.1)              69/756 (9.1)
   Fall: 2-4 meters                                                               66/742 (8.9)               68/756 (9.0)
   Fall: >4 meters                                                                58/742 (7.8)               57/756 (7.5)
   Blast/explosion                                                                 3/742 (0.4)               4/756 (0.5)
   Other                                                                           8/742 (1.1)               28/756 (3.7)
 Type of transport to the trauma center – no./total no. (%)
   Ground ambulance                                                              583/747 (78.0)            585/743 (78.7)
   Helicopter ambulance                                                          140/747 (18.7)            141/743 (19.0)
   A combination of ground ambulance and helicopter
                                                                                   14/747 (1.9)              9/743 (1.2)
   ambulance
   Private vehicle                                                                 1/747 (0.1)               3/743 (0.4)
   Walk-in                                                                         9/747 (1.2)               4/743 (5.3)
   Other                                                                           0/747 (0.0)               1/743 (0.1)
 Use of prehospital or in-hospital supplemental oxygen
                                                                                 333/713 (46.7)            351/718 (48.9)
 prior to randomization – no./total no. (%)
                                                                                 100 (97-100)               99 (97-100)
    Highest SpO2 measured prior to randomization – %
                                                                                    [n=265]                   [n=285]
                                                                                36.5 (35.9-37.0)          36.5 (35.9-36.9)
 Body temperature measured on admission – o C
                                                                                    [n=479]                   [n=484]
 Surgery performed in the trauma resuscitation room
  Neurosurgery – no./total no. (%)                                                  3/744 (0.4)              1/747 (0.1)
  Cardiothoracic surgery – no./total no. (%)                                       10/744 (1.3)              9/747 (1.2)
  Abdominal surgery – no./total no. (%)                                             0/744 (0.0)              4/747 (0.5)
  Orthopedic surgery – no./total no. (%)                                            2/744 (0.3)              1/747 (0.1)
  Vascular surgery – no./total no. (%)                                              1/744 (0.1)              0/747 (1.1)
  Other(s) – no./total no. (%)                                                      1/744 (0.1)              1/747 (0.1)

Trauma patients allocated to either a restrictive or liberal oxygen strategy. Continuous variables are presented as median with
interquartile range.




© 2024 American Medical Association. All rights reserved.
                                                                                                                                16



 eTable 3. Oxygen Intervention Characteristics
                                                                                   Restrictive                  Liberal
 Characteristic                                                                   oxygen group               oxygen group
                                                                                      (N=750)                   (N=758)
                                                                                    54 (35-79)                 52 (33-78)
 Time from trauma to randomization – min (N=1268)
                                                                                     [n = 633]                  [n=635]
 Type of supplemental oxygen* – no./total no. (%)
   No supplemental oxygen                                                          200/739 (27.1)             13/735 (1.8)
   Nasal cannula                                                                   171/739 (23.1)             45/735 (6.1)
   Non-rebreather mask                                                              18/739 (2.4)             340/735 (46.2)
   Intubated (at any point during the intervention period)                         350/739 (47.4)            337/735 (45.9)
                                                                                  12.9 (11.4-14.0)          12.7 (11.3-14.0)
 Hemoglobin hour 1 ± 30 min § – g/dL
                                                                                      [n=602]                   [n=603]
                                                                                  12.5 (10.8-13.7)          12.4 (10.6-13.9)
 Hemoglobin hour 6 ± 2 hours § – g/dL
                                                                                      [n=482]                   [n=487]
                                                                                    1.5 (0.9-2.5)             1.4 (0.9-2.4)
 Lactate hour 1 ± 30 min § – mmol/L
                                                                                      [n=585]                   [n=590]
                                                                                    1.4 (0.9-2.2)             1.4 (0.9-2.1)
 Lactate hour 6 ± 2 hours § – mmol/L
                                                                                      [n=472]                   [n=479]
 Major protocol violation ¶ – no./total no. (%)                                     50/742 (6.7)             102/744 (13.7)
 Protocol deviation † – no./total no. (%)                                           40/741 (5.4)              17/738 (2.3)

Trauma patients allocated to either a restrictive or liberal oxygen strategy. The time from trauma to randomization is presen ted
with a median and interquartile range.
* The data collection sheet consisted of eight hourly data points (H1-H8). The sum of no supplemental oxygen, nasal cannula,
non-rebreather mask or intubated is 100%. Patients are in the no supplemental oxygen category if none of the eight data points
were nasal cannula, non-rebreather mask or intubated. If just one of the eight data points was intubated, the patient was
categorized as intubated. Patients could receive both supplemental oxygen via a nasal cannula and non -rebreather mask
during the 8-hour intervention period at different time points and were registered in the appropriate category based on the
majority of the data points from the sheet. In case they were evenly distributed, the patient was registered in the non -rebreather
mask category.
§ The 1st and 2nd arterial blood gases during the oxygen intervention were obtained at hour 1 ± 30 min after randomization and
hour 6 ± 2 hours after randomization, respectively.
¶ See page 10 for definitions of major protocol violations.
† See page 10 for definition of protocol deviations.




© 2024 American Medical Association. All rights reserved.
                                                                                                                                                                                                      17



 eTable 4. Primary and Key Secondary Outcomes

                                         Restrictive            Liberal                                                                                           Adjusted odds
                                                                                     Odds ratio                           Adjusted odds
                                          oxygen                oxygen                                     P value                                 P value       ratio + smoking          P value
                                                                                      (95% CI)                            ratio (95% CI)
                                           group                group                                                                                                (95% CI)
 Primary outcome
 Death and/or major
                                           118/733             121/724                  1.01                                   0.98                                    1.05
 respiratory complications –                                                                                 0.94                                    0.92                                   0.80
                                            (16.1)              (16.7)              (0.75 to 1.37)                         (0.68 to 1.41)                          (0.73 to 1.49)
 no./total no. (%)
 Key secondary outcomes
                                                                                        1.28                                   1.37                                    1.37
 Death – no./total no. (%)              63/733 (8.6)         53/724 (7.3)                                    0.23                                    0.25                                   0.26
                                                                                    (0.85 to 1.92)                         (0.80 to 2.38)                          (0.80 to 2.33)
 Major respiratory
                                                                                        0.84                                   0.84                                    0.90
 complications – no./total              65/733 (8.9)        78/724 (10.8)                                    0.33                                    0.38                                   0.58
                                                                                    (0.59 to 1.19)                         (0.57 to 1.23)                          (0.61 to 1.32)
 no. (%)

Trial outcomes for trauma patients allocated to either a restrictive or liberal oxygen strategy. Death and major respiratory complications were both evaluated within 30 days. The smoking variable
reflects only active smokers, identified from medical records and, in some cases, confirmed directly with patients.




© 2024 American Medical Association. All rights reserved.
                                                                                                                                                                                                          18



 eTable 5. Categorical Exploratory Outcomes

                                          Restrictive            Liberal                                                                                              Adjusted odds
                                                                                       Odds ratio                            Adjusted odds
                                           oxygen                oxygen                                       P value                                  P value       ratio + smoking           P value
                                                                                        (95% CI)                             ratio (95% CI)
                                            group                group                                                                                                   (95% CI)
 Presence of any
                                                                                          1.67                                     1.72                                    1.69
 hypoxemic episodes (SpO2                44/737 (6.0)         28/737 (3.8)                                      0.04                                     0.03                                    0.04
                                                                                      (1.02 to 2.70)                           (1.04 to 2.78)                          (1.04 to 2.78)
 <90%) * – no./total no. (%)
 ICU re-admission(s) –                                                                    0.59                                     0.60                                    0.57
                                         17/368 (4.6)         18/352 (5.1)                                      0.22                                     0.25                                    0.19
 no./total no. (%) †                                                                  (0.26 to 1.37)                           (0.25 to 1.43)                          (0.25 to 1.32)
 Sepsis during hospital
                                                                                          0.55                                     0.53                                    0.52
 admission – no./total no.               19/736 (2.6)         31/727 (4.3)                                      0.06                                     0.05                                    0.05
                                                                                      (0.30 to 1.02)                           (0.29 to 1.00)                          (0.27 to 1.00)
 (%)
 Surgical site infection(s)
                                                                                          0.50                                     0.49                                    0.51
 within 30 days – no./total              23/736 (3.1)         32/724 (4.4)                                      0.05                                     0.03                                    0.04
                                                                                      (0.25 to 0.99)                           (0.26 to 0.93)                          (0.27 to 0.96)
 no. (%)
 Pneumonia post-discharge
 within 30 days after                                                                     1.06                                     1.04                                    1.03
                                         27/640 (4.2)         24/620 (3.9)                                      0.86                                     0.89                                    0.93
 enrollment ¶ – no./total no.                                                         (0.60 to 1.85)                           (0.59 to 1.85)                          (0.57 to 1.85)
 (%)
 Brain injury within 7 days of
                                            290/738              275/732                  1.11                                     1.05                                    1.04
 admission – no./total no.                                                                                      0.35                                     0.68                                    0.74
                                             (39.3)               (37.6)              (0.88 to 1.41)                           (0.82 to 1.35)                          (0.81 to 1.33)
 (%)
 Myocardial infarction within
                                          0/738 (0.0)          1/730 (0.1)                    -                    -                   -                    -                   -                   -
 7 days – no./total no. (%)
 Cerebral ischemia within 7                                                               1.56                                     1.45                                    1.47
                                         16/738 (2.2)         10/730 (1.4)                                      0.30                                     0.38                                    0.36
 days – no./total no. (%)                                                             (0.68 to 3.57)                           (0.63 to 3.45)                          (0.64 to 3.45)
 ICU admission – no./total                  374/738              359/736                  1.16                                     1.01                                    1.01
                                                                                                                0.24                                     0.95                                    0.95
 no. (%)                                     (50.7)               (48.8)              (0.90 to 1.49)                           (0.76 to 1.33)                          (0.76 to 1.33)

Trial outcomes for trauma patients allocated to either a restrictive or liberal oxygen strategy. No exploratory outcomes were statistically significant between the groups after adjusting for multiple
testing. The smoking variable reflects only active smokers, identified from medical records and, in some cases, confirmed directly with patients.
* Defined as any hypoxemic episodes (SpO2 <90%) during the eight-hour intervention from the hourly collected SpO2 values.
† ICU: Intensive care unit.
¶ Only patients discharged within 30 days were eligible for evaluation of pneumonia post-discharge.




© 2024 American Medical Association. All rights reserved.
                                                                                                                                                                                                       19



 eTable 6. Continuous Exploratory Outcomes
                                                                                                                                                                   Adjusted mean
                                         Restrictive            Liberal                                                    Adjusted mean
                                                                                  Mean difference                                                                   difference +
                                          oxygen                oxygen                                      P value          difference              P value                                P value
                                                                                     (95% CI)                                                                         smoking
                                           group                group                                                         (95% CI)
                                                                                                                                                                      (95% CI)
 Initial surgery duration after
                                        114 (64-166)         113 (68-149)                 10.3                                    12.6                                    15.4
 trauma resuscitation room                                                                                     0.29                                    0.22                                   0.13
                                          [n=165]              [n=161]               (-8.8 to 29.3)                          (-7.4 to 32.6)                          (-4.3 to 35.0)
 treatment – min
 Time on mechanical                        0 (0-14)             0 (0-12)                  4.8                                     3.3                                     3.7
                                                                                                               0.45                                    0.59                                   0.54
 ventilation – hours                       [n=735]              [n=725]              (-7.6 to 17.2)                          (-8.7 to 15.2)                          (-8.1 to 15.6)
 Days alive without
                                          30 (29-30)           30 (29-30)                 -0.6                                    -0.4                                    -0.5
 mechanical ventilation –                                                                                      0.16                                    0.27                                   0.20
                                           [n=735]              [n=723]               (-1.4 to 0.2)                           (-1.1 to 0.3)                           (-1.2 to 0.2)
 days
 Intensive Care Unit Length                  2 (1-9)             2 (1-7)                   1.1                                     1.0                                     1.0
                                                                                                               0.10                                    0.17                                   0.16
 of Stay – days                             [n=368]             [n=357]               (-0.2 to 2.5)                           (-0.4 to 2.3)                           (-0.4 to 2.5)
 Days alive outside the
                                          29 (26-30)           30 (27-30)                 -0.8                                    -0.5                                    -0.6
 Intensive Care Unit within                                                                                    0.09                                    0.17                                   0.12
                                           [n=736]              [n=724]               (-1.7 to 0.1)                           (-1.3 to 0.2)                           (-1.3 to 0.2)
 30 days – days
 Hospital Length of Stay –                 7 (3-15)             7 (3-15)                  -0.7                                    -1.0                                    -1.0
                                                                                                               0.41                                    0.23                                   0.23
 days                                      [n=736]              [n=728]               (-2.3 to 0.9)                           (-2.3 to 0.6)                           (-2.5 to 0.6)

Trial outcomes for trauma patients allocated to either a restrictive or liberal oxygen strategy. All continuous variables are presented as medians with interquartile ranges in the group allocation
columns. No exploratory outcomes were statistically significant between the groups after adjusting for multiple testing. The smoking variable reflects only active smokers, identified from medical
records and, in some cases, confirmed directly with patients.
* Patients still admitted at day 30 were not eligible for evaluation of pneumonia post-discharge.




© 2024 American Medical Association. All rights reserved.
                                                                                                                                                   20



 eTable 7. Adjusted Subgroup Analyses
                                                   Restrictive                  Liberal
                                                                                              Odds ratio (95% CI)   Adjusted odds ratio (95% CI)
                                                  oxygen group              oxygen group
                                                    no. of events/total no. of patients (%)
                                                                                                     1.01                      0.98
 All patients                                     118/733 (16.1)           121/724 (16.7)
                                                                                                 (0.75 to 1.37)            (0.68 to 1.39)
 Intubated at randomization
                                                                                                     1.12                      1.16
   No                                             56/558 (10.0)              50/543 (9.2)
                                                                                                 (0.75 to 1.67)            (0.73 to 1.85)
                                                                                                     0.90                      0.76
   Yes                                            62/175 (35.4)             71/181 (39.2)
                                                                                                 (0.57 to 1.41)            (0.45 to 1.30)
 ICU admission
                                                                                                     0.98                      0.89
   No                                              42/458 (9.2)             50/481 (10.4)
                                                                                                 (0.64 to 1.49)            (0.56 to 1.43)
                                                                                                     0.96                      0.98
   Yes                                            74/271 (27.3)             68/238 (28.6)
                                                                                                 (0.63 to 1.49)            (0.58 to 1.67)
 Moderate or severe traumatic brain
 injury *
                                                                                                     1.06                      1.11
   AIS < 3                                         45/500 (9.0)              48/473 (9.2)
                                                                                                 (0.68 to 1.64)            (0.68 to 1.85)
                                                                                                     0.81                      0.83
   AIS ≥ 3                                        73/233 (31.3)             73/202 (36.1)
                                                                                                 (0.53 to 1.25)            (0.51 to 1.37)
 Known lung disease
                                                                                                     0.88                      0.95
   No                                             97/667 (14.5)            105/643 (16.3)
                                                                                                 (0.65 to 1.22)            (0.65 to 1.39)
                                                                                                     1.85                      1.06
   Yes                                             19/59 (32.2)              14/69 (20.2)
                                                                                                 (0.73 to 4.55)            (0.40 to 2.86)
 Site of inclusion
                                                                                                     0.81                      0.95
   Prehospital                                    48/303 (15.8)             54/296 (18.2)
                                                                                                 (0.51 to 1.28)            (0.55 to 1.64)
                                                                                                     1.19                      0.98
   In-hospital                                    70/430 (16.3)             67/428 (15.7)
                                                                                                 (0.81 to 1.79)            (0.63 to 1.52)
 Injury severity score †




© 2024 American Medical Association. All rights reserved.
                                                                                                                                                                                         21


                                                           Restrictive                  Liberal
                                                                                                                        Odds ratio (95% CI)               Adjusted odds ratio (95% CI)
                                                          oxygen group              oxygen group
                                                            no. of events/total no. of patients (%)
                                                                                                                                 1.33                                   1.14
   ISS ≤ 15                                                 22/380 (5.8)                  19/389 (4.9)
                                                                                                                             (0.69 to 2.56)                         (0.56 to 2.33)
                                                                                                                                 0.86                                   0.93
   ISS > 15                                                95/352 (27.0)                 100/329 (30.4)
                                                                                                                             (0.60 to 1.23)                         (0.62 to 1.40)

Adjusted subgroup analyses for trauma patients allocated to either a restrictive or liberal oxygen strategy.
* Moderate or severe traumatic brain injury was evaluated by a score of 3 or higher on the AIS (Abbreviated Injury Scale) from the head/neck codes, but only head codes were selected.
† Injury Severity Score: ISS.




© 2024 American Medical Association. All rights reserved.
                                                                                                                                                                                                    22



 eTable 8. Per-Protocol Analyses of Primary and Key Secondary Outcomes ¶
                                        Restrictive            Liberal
                                                                                                                                                                  Adjusted odds
                                         oxygen                oxygen                Odds ratio                           Adjusted odds                                                       P
                                                                                                           P value                                 P value       ratio + smoking
                                          group                 group                 (95% CI)                            ratio (95% CI)                                                    value
                                                                                                                                                                     (95% CI)
                                         (N=700)               (N=656)
 Primary outcome
 Death and/or major
                                           104/683             105/627                 0.98                                    0.97                                    1.04
 respiratory complications –                                                                                 0.91                                    0.87                                   0.83
                                            (15.2)              (16.7)             (0.71 to 1.35)                          (0.67 to 1.41)                          (0.71 to 1.52)
 no./total no. (%)
 Key secondary outcomes
                                                                                       1.27                                    1.25                                    1.22
 Death – no./total no. (%)              54/683 (7.9)        44/627 (7.0)                                     0.29                                    0.45                                   0.49
                                                                                   (0.82 to 2.00)                          (0.70 to 2.22)                          (0.69 to 2.17)
 Major respiratory
                                                                                       0.78                                    0.82                                    0.89
 complications – no./total              58/685 (8.5)        69/629 (11.0)                                    0.20                                    0.34                                   0.58
                                                                                   (0.54 to 1.14)                          (0.54 to 1.23)                          (0.59 to 1.33)
 no. (%)

Per-protocol analyses of trauma patients allocated to either a restrictive or liberal oxygen strategy. Death and major respiratory complications were both evaluated within 30 days. The smoking
variable reflects only active smokers, identified from medical records and, in some cases, confirmed directly with patients.
¶ See page 10 for definitions of major protocol violations.




© 2024 American Medical Association. All rights reserved.
                                                                                                                                 23



 eTable 9. Adverse Events (AE) and Serious Adverse Events (SAE) ¶
                                                                                   Restrictive                 Liberal
                                                                                  oxygen group             oxygen group
                                                                                     (N=750)                  (N=758)
 Adverse event (AE) – no./total no. (%)
  Atelectasis                                                                     207/750 (27.6)           263/758 (34.7)
  Irritability of airway mucosa                                                    16/750 (2.1)             20/758 (2.6)
 Serious adverse event (SAE) – no./total no. (%)
  Death                                                                             63/750 (8.4)             53/758 (7.0)
  Was life-threatening                                                              8/750 (1.1)              13/758 (1.7)
  Involved or prolonged hospital length of stay                                     29/750 (3.9)             37/758 (4.9)
  Involved persistence of significant disability or incapacity                      0/750 (0.0)              0/758 (0.0)
  Resulted in a congenital anomaly or birth defect                                  0/750 (0.0)              1/758 (0.1)

¶ See page 9 for the definitions of AE and SAE registration. There is a difference in the denominator of the patients for both
groups compared to the outcome tables because patients were observed for AEs and SAEs up until a potential consent
withdrawal. In case consent was withdrawn and no event was registered, the patient was registered as having no events and
included in this table. No Serious Adverse Reactions (SAR) or Suspected Unexpected Serious Adverse Reactions (SUSAR)
were registered.




© 2024 American Medical Association. All rights reserved.
                                                                                                                         24



 eTable 10. Distribution of Oxygen Interventions Among the Post-
 Randomization Excluded Patients ¶
                                                                                Restrictive                Liberal
                                                                               oxygen group            oxygen group
                                                                                  (N=750)                 (N=758)
 Exclusion after randomization – no./total no. (%) (N=130)                       55/750 (45)             67/758 (55)
 Secondary exclusion – no./total no. (%) (N=341) *                              174/750 (51)            165/758 (49)

¶ Detailed numbers on the post-randomization excluded patients from Figure 1 in the main manuscript.
* Two patients had missing data on the randomized oxygen intervention, which is the reason for the discrepancy between
N=341 and the numbers in the table.




© 2024 American Medical Association. All rights reserved.
                                                                                               25



 eTable 11. Best/Worst Case Scenario: Primary and Key Secondary Outcomes
                                   Restrictive          Liberal        Odds ratio
                                                                                       P value
                                  oxygen group       oxygen group       (95% CI)
 Primary outcome
 Missing not counted as
 event: Death and/or major                                                0.99
                                  118/750 (15.7)     121/758 (16.0)                     0.96
 respiratory complications –                                          (0.74 to 1.33)
 no./total no. (%)
 Missing counted as event:
 Death and/or major                                                       0.85
                                  135//750 (18.0)    155/758 (20.4)                     0.24
 respiratory complications –                                          (0.65 to 1.11)
 no./total no. (%)
 Key secondary outcomes
 Missing not counted as
                                                                          1.28
 event: Death – no./total no.      63/750 (8.4)        53/758 (7.0)                     0.22
                                                                      (0.86 to 1.92)
 (%)
 Missing counted as event:                                                0.93
                                   80/750 (10.7)      87/758 (11.4)                     0.70
 Death – no./total no. (%)                                            (0.68 to 1.30)
 Missing not counted as
 event: Major respiratory                                                 0.82
                                   65/750 (8.7)       78/758 (10.3)                     0.26
 complications – no./total                                            (0.57 to 1.16)
 no. (%)
 Missing counted as event:
 Major respiratory                                                        0.70
                                   82/750 (10.9)     112/758 (14.8)                     0.02
 complications – no./total                                            (0.52 to 0.95)
 no. (%)




© 2024 American Medical Association. All rights reserved.
```
