# Support core quantitative evidence map

Agent: /root/support_mapping. Scope: DOC-003 PDF pp.1-9, DOC-004 pp.1-18, DOC-005 pp.1-3, DOC-006 p.1. All 31 units mapped. No protocol or main-paper pages are mapped here. Matching main-paper keys below are semantic join keys for the separate main mapper; they are not independent main-paper transcriptions. No candidate diagnosis is performed.

Engine/provenance: reused native/layout text (historic pdftotext version unspecified) for DOC-004 pp.1-18 and DOC-005/006; manual image reading of all SAP pages and DOC-004 figures pp.10-18, with image confirmation of eTables pp.3-6. Reused raster engines/version unspecified. No new extraction/OCR script, rendering, or OCR used by this mapper. The source role is PLAN for DOC-003, REPORT for DOC-004/005/006. No Office/workbook/CSV source exists in this assignment; formulas/cached workbook values are not applicable. The SAP contains a printed mathematical formula, recorded literally below.

## DOC-003: statistical analysis plan

Source: joi250087supp2_prod_1766516490.96511.pdf. Image locators: review_1_5_1/preprocessing/DOC-003/page-001.png through page-006.png; evidence_recheck/doc003_p7.png; DOC-003/lowres-8.jpg and lowres-9.jpg. Empty native/OCR derivatives on pp.5-9 do not delimit coverage. Each image was opened and read anew.

### DOC-003 p.1 — cover and version

[Source](../../../../joi250087supp2_prod_1766516490.96511.pdf#page=1). PLAN. Final version printed 11/04/2025; both statistical and methodology signature dates 11/04/2025. LEVOECMO, levosimendan to facilitate weaning from ECMO in severe cardiogenic shock. Sponsor, principal investigator, project manager, data manager, statistician and methodologist identified. No endpoint result, formula, population denominator, or decision rule on this administrative cover. Version date is relevant to plan identity; addresses and telephone numbers are administrative, not result quantities.

### DOC-003 p.2 — contents

[Source](../../../../joi250087supp2_prod_1766516490.96511.pdf#page=2). PLAN. Contents: study summary and primary objective/endpoint p.3; secondary endpoints p.4; flow, sample size, analysis population, descriptive analysis, primary analysis p.5; secondary analyses p.7; significance, missing data, plan changes, software and references p.9. No independent result-relevant quantitative relationship on this contents page; all pointed sections opened below.

### DOC-003 p.3 — trial objective and primary endpoint

[Source](../../../../joi250087supp2_prod_1766516490.96511.pdf#page=3). PLAN. Multicenter randomized double-blind phase III superiority trial; enrollment spans 24 months; each participant 60 days, including 24-hour treatment and 60-day follow-up. Early levosimendan intended to reduce ECMO duration. Primary objective: efficacy on time to successful ECMO weaning in patients receiving VA-ECMO for acute shock refractory to conventional therapy. Primary endpoint: time to successful ECMO weaning within 30 days following randomization. Success requires survival without ECMO, another mechanical circulatory support device, or heart transplant for 30 days after removal. All removals from randomization to day30 considered; adjudication can require follow-up until day60 for removal on day30. Unsuccessful removal within 30 days and death within 30 days without a weaning attempt are competing events. No event after day30 is considered in event-time follow-up; subjects with none of the three events censored at day30. Join keys: primary endpoint definition/window, success adjudication window, competing risks, intervention duration, follow-up.

### DOC-003 p.4 — secondary endpoint definitions and status

[Source](../../../../joi250087supp2_prod_1766516490.96511.pdf#page=4). PLAN. Every following item is explicitly secondary: mortality D30/D60; total ECMO support inclusion-D30 and inclusion-D60 and ECMO-free days through both windows; ICU and total hospital length; MACE occurrence at D30/D60 (death, cardiac transplant, permanent LVAD escalation, stroke, rehospitalization for heart failure); time to hemodynamic improvement defined as mean blood pressure >60 mmHg; organ-failure days with SOFA >2 in at least one of six organ systems and organ-failure-free days inclusion-D30; catecholamine support duration/free days inclusion-D30; MV duration/free days inclusion-D30 and inclusion-D60; RRT duration/free days inclusion-D30; LV function by echocardiography at day30, left ventricular ejection fraction in percent. Safety includes incidence of drug-related atrial fibrillation, ventricular arrhythmias, ventricular fibrillation, torsades de pointes, hypokalemia, and any follow-up adverse events. Join keys: all secondary and safety endpoint statuses, windows and composite components; eTable3; eFigures2-8; main secondary outcomes and adverse-event table.

### DOC-003 p.5 — population, power and summaries

[Source](../../../../joi250087supp2_prod_1766516490.96511.pdf#page=5). PLAN. Flow diagram planned to enumerate screened eligible, randomized totals, arm distribution, follow-up/losses and analyzed numbers. Sample size: control success cumulative incidence 50% from similar 30-day cohort accounting for death/weaning-failure competing risks; subdistribution HR 1.75; two-sided alpha 5%; power 80%; 101 successful-weaning events required under cited Latouche formula; total206,103 per group. No explicit numerical sample-size formula printed on this page. ITT primary analysis: every randomized participant in assigned arm regardless of treatment changes. Qualitative frequencies/percentages; normally distributed quantitative variables mean/SD; non-normal median/IQR and range; censored-data KM or CIF rates at15/30/60 days with95%CI where appropriate. Primary time-to-success within30 days accounts for competing risks; success definition repeats survival without ECMO/additional mechanical support/transplant for30 days after removal. Join keys: main sample-size assumptions, randomized/analyzed population, descriptive statistics and primary estimand.

### DOC-003 p.6 — primary event coding and inferential analysis

[Source](../../../../joi250087supp2_prod_1766516490.96511.pdf#page=6). PLAN. Success event of interest; still on ECMO day30 censored; death before day30 without weaning competing; unsuccessful removal (death, repeat ECMO, additional mechanical support/transplant within30 days after removal) competing; lost before30 days censored. Time to success randomization-to-success date; unsuccessful time randomization-to-removal date; death without removal randomization-to-death date; loss randomization-to-last-news date; no event censor time30 days. CIF rates15/30 days with95%CI and group curves; Gray test of success CIF. Fine-Gray adjusted for primary shock etiology (acute MI, myocarditis, post-heart surgery, other) estimates treatment sHR and95%CI for each defined event. Proportional hazards assessed using Schoenfeld residuals. Sensitivity cause-specific Cox estimates treatment cause-specific HR and95%CI. Join keys: main primary model/covariate/Gray P/sHR; eTable2 cause-specific sensitivity; primary failure/death competitor results.

### DOC-003 p.7 — secondary analysis methods and disclosed revision

[Source](../../../../joi250087supp2_prod_1766516490.96511.pdf#page=7). PLAN. Mortality: KM95%CI; only survival analysis through60 days, time from randomization to death irrespective of prior weaning, last news or follow-up end; logrank comparison; etiology-adjusted Cox. ECMO durations/free days D30/D60: Wilcoxon rank-sum; deaths assigned0 ECMO-free days; etiology-adjusted general linear model. ICU/hospital: RMST through60 days with95%CI because ongoing hospitalization leads to right censoring; logrank; etiology-adjusted Cox. MACE definition repeats all five components; KM95%CI through60 days; event time randomization-to-first-MACE, last update or end whichever first; logrank; etiology-adjusted Cox. Hemodynamic improvement is explicitly revised: originally >60mmHg time-to-improvement under competing risks, but descriptive inspection before inferential analysis found most patients stably >60 throughout follow-up; removed from inferential analysis as non-informative, replaced by descriptive MBP plot throughD30. Organ failure definition SOFA>2 in at least one of six systems; duration/free days throughD30 compared Wilcoxon; death assigned0 failure-free days; etiology-adjusted general linear model. Join keys: secondary methods, revision disclosure, eFigures2/4/5/7, eTable3.

### DOC-003 p.8 — secondary methods, hierarchical LV function and safety

[Source](../../../../joi250087supp2_prod_1766516490.96511.pdf#page=8). PLAN. Catecholamine duration/free days inclusion-D30: Wilcoxon, deaths assigned0 catecholamine-free days; etiology-adjusted general linear model. MV duration/free days inclusion-D30/D60: Wilcoxon, death0 ventilator-free days; etiology-adjusted general linear model. RRT duration/free days inclusion-D30: Wilcoxon; the printed death rule says0 "ventilatory-free days"; etiology-adjusted general linear model. This literal wording is preserved for checker interpretation, without normalization.

LV function uses Global Net Benefit atD30 with hierarchical composite: (1)death,(2)heart transplantation,(3)LV improvement defined LVEF>30%. Every experimental patient pairwise compared with every control patient. Experimental survival versus control death is a win; if both survive, avoiding transplantation versus control transplant is a win; if neither transplanted, greater LV improvement atD30 wins; same outcome at every hierarchical level is tie. Printed formula wording: "Number of Wins–Number of Losses/Total number of comparisons". Intended grouping is not inferred here. Positive net benefit favors experimental treatment;95%CI bootstrap. Safety drug adverse-reaction incidence (AF, ventricular arrhythmia/VF/torsades/hypokalemia) uses Poisson regression allowing more than one event per patient, adjusted for prognostic factors. Join keys: main/eTable3 LVEF analysis, planned hierarchical endpoint, safety event model.

### DOC-003 p.9 — safety continuation, alpha, missingness and plan changes

[Source](../../../../joi250087supp2_prod_1766516490.96511.pdf#page=9). PLAN. Any follow-up AE described overall/by arm by patient count/percentage; serious AEs separately. Numbers of AEs and SAEs compared by etiology-adjusted Poisson model. All analyses two-sided alpha5%. Primary loss-to-follow-up censored; no imputation because survival handles censoring; non-informative censoring assumed (loss independent of primary-event risk). Any modifications must precede database unblinding and receive systematic scientific-committee validation. R4.4.2. Latouche/Porcher/Chevret2004 sample-size reference; no additional numeric method or stopping/interim rule here. No subgroup-analysis prescription appears anywhere in this9-page SAP. No further multiplicity decision rule is printed beyond alpha5%. Join keys: main missing-data handling, significance/multiplicity, software, safety count model, prespecification/revision.

## DOC-004: results supplement

Native text is reproduced by page for completeness below. Table superscript1 is a footnote marker, not a denominator digit: p.3 headers mean146,69,77,59,32,27. All percentages are percent, differences for categorical endpoints are percentage points; continuous differences retain the row unit. Treatment contrast is levosimendan versus placebo except eTable4 explicitly prints placebo first. Tables retain every printed signed zero and dash. Page-specific join keys precede the transcription.

### DOC-004 p.1

[Source](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=1). REPORT.

Contents and identity only; no independent quantitative result. All listed tables and figures mapped below.


```text
                            Supplemental Online Content


Combes A, Saura O, Nesseler N, et al; LEVOECMO Trial Group; International ECMO
Network (ECMONet). Levosimendan to facilitate weaning from ECMO in patients with severe
cardiogenic shock: the LEVOECMO randomized clinical trial. JAMA. Published online
December 1, 2025. doi:10.1001/jama.2025.19843



eAppendix. Supplementary Data
eTable 1. Type of Consent
eTable 2. Cause-Specific Analysis
eTable 3. Secondary End Points
eTable 4. Daily Doses of Dobutamine, Epinephrine and Norepinephrine From Randomization
to Day 7
eTable 5. Vasopressor or Inotrope Exposure and Treatment Duration From Randomization
to Day 30
eTable 6. Other Causes of Cardiogenic Shock at Randomization
eFigure 1. Patients’ Trajectory
eFigure 2. Cumulative Incidence of D30 and D60 Mortality
eFigure 3. SOFA Score Subcomponents Evolution From D1 to D28
eFigure 4. D30 and D60 Cumulative Incidence of Major Cardiac Adverse Events (MACE)
Defined as Death, Cardiac Transplant, Escalation to Permanent Left Ventricular Assist
Device, Stroke, or Re-Hospitalization for Heart Failure
eFigure 5. Mean Blood Pressure Evolution From D1 to D30
eFigure 6. Median (IQR) Doses of Vasoactive Drugs From Randomization (Day 0) to Day 7
eFigure 7. Distribution of ICU and Hospital Stay Up to D60
eFigure 8. Number of Serious Adverse Events
eFigure 9. Cumulative Incidence of Successful ECMO Weaning in Predefined Subgroups of
Patients



This supplemental material has been provided by the authors to give readers additional
information about their work.




© 2025 American Medical Association. All rights reserved, including those for text and data mining,
AI training, and similar technologies.

```

### DOC-004 p.2

[Source](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=2). REPORT.

Join keys: eligibility thresholds, consent categories and analysis-population inclusion. All exclusions transcribed below.


```text
eAppendix. Supplementary Data

Patients

Exclusion criteria were: age <18 years; pregnant or lactating women; initiation of VA-ECMO

>48 h; resuscitation >30 minutes (cumulative low-flow time) in the 48 hours before ECMO;

irreversible neurological pathology; end-stage cardiomyopathy with no hope of LV function

recovery; mechanical complication of myocardial infarction; aortic regurgitation > grade II;

VA-ECMO for pulmonary embolism; VA-ECMO for cardiotoxic drug intoxication; ECMO

after left-ventricle assist device implantation; VA-ECMO in heart transplant patients; patient

moribund on the day of randomization; SAPS II >90; liver cirrhosis (Child B or C) and other

severe hepatic insufficiency; chronic renal failure requiring hemodialysis; known

hypersensitivity to levosimendan; history of torsades de pointes in the 30 days prior to

inclusion; history of epilepsy; individuals under guardianship; or permanently legally

incompetent adults; participation to another interventional study; patient with a weight over

180 kg; known hypersensitivity to polyvitamin CERNEVIT®. As patients couldn’t provide

written consent at inclusion, it was obtained from a close relative or surrogate. If unavailable,

emergency consent allowed randomization without it. The patient and relative/legal

representative were informed as soon as possible and gave written consent for continuation.




© 2025 American Medical Association. All rights reserved, including those for text and data mining,
AI training, and similar technologies.

```

### DOC-004 p.3

[Source](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=3). REPORT.

Join keys: randomized101/104 population, total205, emergency/surrogate consent, continued consent. Table superscripts distinguished visually.


```text
           eTable 1. Type of Consent


                                                                  Overall           Levosimendan            Placebo
                                                                  N = 1461             N = 691              N = 771
Emergency consent, no. (%)
     Patient’s signed continued informed consent             113/146 (77.4%)         53/69 (76.8%)       60/77 (77.9%)
     Patient unable to consent at the end of follow-up         4/146 (2.7%)           1/69 (1.4%)         3/77 (3.9%)
     Death before ability to consent                          29/146 (19.9%)         15/69 (21.7%)       14/77 (18.2%)
     Declined consent                                          0/146 (0.0%)           0/69 (0.0%)         0/77 (0.0%)
                                                                 Overall         Levosimendan             Placebo
                                                                 N = 591            N = 321               N = 271
Consent from a close relative or surrogate, no. (%)
     Patient’s signed continued informed consent             35/59 (59.3%)        20/32 (62.5%)       15/27 (55.6%)
     Patient unable to consent at the end of follow-up         3/59 (5.1%)         1/32 (3.1%)          2/27 (7.4%)
     Death before ability to consent                         21/59 (35.6%)        11/32 (34.4%)       10/27 (37.0%)
     Declined consent                                          0/59 (0.0%)         0/32 (0.0%)          0/27 (0.0%)
1
    n/N (%)




           © 2025 American Medical Association. All rights reserved, including those for text and data mining,
           AI training, and similar technologies.

```

### DOC-004 p.4

[Source](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=4). REPORT.

Join keys: cause-specific Cox sensitivity for primary success/failure/death, adjusted etiology, SAP p.6, main primary sensitivity. Three complete inferential triples.


```text
eTable 2. Cause-Specific Analysis



 Event                                       csHR (95% CI) a           P value

 Successful ECMO weaning                     1.15 (0.82 – 1.62)           0.42

 ECMO weaning failure                        0.91 (0.46 – 1.82)           0.79

 Death before ECMO weaning                   1.57 (0.72 – 3.44)           0.26


a:
     Cause-specific hazard ratio (csHR) for the primary endpoint, estimated using the cause-specific Cox
proportional hazards model and adjusted for cardiogenic shock etiology.




© 2025 American Medical Association. All rights reserved, including those for text and data mining,
AI training, and similar technologies.

```

### DOC-004 p.5

[Source](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=5). REPORT.

Join keys: secondary organ/catecholamine/MV/KRT/LVEF outcomes, MACE D30/D60 and components, SAP pp.4/7/8, main secondary table. Footnotes define bootstrap differences, RR, missing observations, LVEF handling and omission of P values.


```text
        eTable 3. Secondary End Points


                                                                              Levosimendan            Placebo               Median or                 Relative difference
Outcomes/eventsa
                                                                                 N = 101              N = 104       Risk Difference, (95% CI) b           (95% CI) c

Number of organ-failure-free days at Day 30, median (IQR)                    12 (0, 21)         14 (0, 23)             -2 (-10 to 4)

Number of days with organ failure, median (IQR)                               9 (6, 17)         12 (6, 18)             -3 (-5 to 2)

Number of catecholamine-free days at Day 30, median (IQR)                    18 (0, 23)         18 (5, 25)              0 (-4 to 6)

Catecholamine duration, days, median (IQR)                                    9 (5, 13)         10 (5, 16)             -1 (-4 to 2)

No of days alive and free from cardiovascular failure within 7 days d,
                                                                              0 (0, 2)           0 (0, 2)               0 (0 to 0)
median (IQR)

No of days alive and free from MV by day 30, median (IQR)                     6 (3, 11)         6 (3, 13)              -0 (-3 to 2)

Mechanical ventilation duration by day 30, days, median (IQR)                21 (0, 27)         22 (2, 27)             -0 (-7 to 4)

Kidney replacement therapy duration by day 30, days, median (IQR)            30 (0, 30)         30 (8, 30)              0 (-5 to 1)

No of days alive and free from KRT by day 30, median (IQR)                    0 (0, 2)           0 (0, 5)               0 (0 to 0)

                                                                             45 (30, 50)       40 (25, 50)
Left ventricular ejection fraction, median (IQR), by day 30                                                            5 (-0 to 10)
                                                                              (n = 100)

Major adverse cardiovascular events during first 30 days, no. (%)            35 (34.7%)        36 (34.6%)           0.0 (-12.6 to 13.6)         RR, 1.00 (0.69 to 1.46)

 Cardiac transplant by day 30, no. (%)                                        0 (0.0%)          5 (4.8%)            -4.8 (-9.6 to -1.0)                    -

 Escalation to permanent left ventricular assist device by day 30, no. (%)    4 (4.0%)          4 (3.8%)             0.1 (-4.8 to 5.1)          RR, 1.03 (0.26 to 4.01)

 Stroke by day 30, no. (%)                                                    7 (6.9%)          6 (5.8%)             1.2 (-5.7 to 8.0)          RR, 1.20 (0.42 to 3.45)

 Dialysis by day 30, no. (%)                                                 29 (28.7%)        38 (36.5%)           -7.8 (-21.4 to 4.7)         RR, 0.79 (0.53 to 1.17)




       © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.

```

### DOC-004 p.6

[Source](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=6). REPORT.

Join keys: secondary organ/catecholamine/MV/KRT/LVEF outcomes, MACE D30/D60 and components, SAP pp.4/7/8, main secondary table. Footnotes define bootstrap differences, RR, missing observations, LVEF handling and omission of P values.


```text
 Rehospitalization for heart failure by day 30, no. (%)                         0 (0.0%)           1 (1.0%)             -1.0 (-2.9 to 0.0)                      -

Major adverse cardiovascular events during first 60 days, no. (%)              36 (35.6%)        39 (37.5%)           -1.9 (-15.4 to 11.7)          RR, 0.95 (0.66 to 1.36)

 Cardiac transplant by day 60, no. (%)                                          0 (0.0%)           5 (4.8%)            -4.8 (-9.6 to -1.0)                      -

 Escalation to permanent left ventricular assist device by day 60, no. (%)      4 (4.0%)           5 (4.8%)             -0.8 (-6.7 to 5.0)          RR, 0.82 (0.23 to 2.98)

 Stroke by day 60, no. (%)                                                      7 (6.9%)           6 (5.8%)             1.2 (-5.7 to 8.0)           RR, 1.20 (0.42 to 3.45)

 Dialysis by day 60, no. (%)                                                        -                  -

 Rehospitalization for heart failure by day 60, no. (%)                         0 (0.0%)           1 (1.0%)             -1.0 (-2.9 to 0.0)                      -


       Abbreviations: IQR, Interquartile range; Q1, first quartile (25th percentile); Q3, third quartile (75th percentile); RR, Relative Risk; CI, Confidence Interval;
       ECMO, extracorporeal membrane oxygenation, ECMO, extracorporeal membrane oxygenation; MV, mechanical ventilation, KRT, kidney replacement
       therapy.
       a
        : Summary measure within each group: median (interquartile range) for continuous variables, number and percentage (n (%)) for categorical variables. For
       patients alive at day 30, left ventricular ejection fraction (LVEF) was assessed at day 30 and for those who died before day 30, the last available LVEF
       measurement prior to death was used. In the presence of missing data, the number of observations is reported as (n = …) for continuous variables and as n/N
       (%) for categorical variables. Being free from cardiovascular failure was defined as a cardiovascular component of the SOFA score < 2.
       b
        : Absolute difference between groups (difference in medians for continuous variables or in percentages for categorical variables), with a 95% confidence
       interval estimated by non-parametric bootstrap resampling.
       c
       : Relative measure of effect: expressed as relative risk (95% CI) for binary endpoints. The relative risk and its 95% confidence interval are not estimated
       when one of the groups has zero events.

       p-values were not reported for secondary outcomes because of multiple testing concerns.




       © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.

```

### DOC-004 p.7

[Source](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=7). REPORT.

Join keys: daily vasoactive doses day0-7; eFigure6; SAP catecholamine support. Unit supplied by eFigure6 is micrograms/kg/minute.


```text
eTable 4. Daily Doses of Dobutamine, Epinephrine and Norepinephrine From
Randomization to Day 7



                                               Placebo,                    Levosimendan,
   Drug                     Day
                                           n; Median (IQR)                n; Median (IQR)

                              0         88 ; 9.44 (5.00 - 11.85)       81 ; 8.43 (5.00 - 10.10)

                              1         89 ; 9.70 (5.00 - 12.00)       83 ; 8.41 (5.00 - 11.25)

                              2         88 ; 8.56 (5.00 - 10.33)       80 ; 7.33 (4.98 - 10.00)

                              3         89 ; 5.02 (4.22 - 9.84)        69 ; 6.67 (4.97 - 10.00)
   Dobutamine
                              4         82 ; 5.00 (3.00 - 8.08)        61 ; 5.00 (4.46 - 8.00)

                              5         74 ; 5.00 (2.70 - 8.70)        58 ; 4.98 (3.55 - 7.35)

                              6         55 ; 5.00 (3.41 - 8.13)        48 ; 5.00 (3.98 - 7.04)

                              7         55 ; 5.20 (4.25 - 9.13)        43 ; 5.00 (4.00 - 7.83)

                              0                     -                   2 ; 0.02 (0.01 - 0.02)

                              1                     -                   2 ; 0.02 (0.01 - 0.02)
   Epinephrine
                              5                     -                   1 ; 0.10 (0.10 - 0.10)

                              7                     -                   1 ; 2.00 (2.00 - 2.00)

                              0         76 ; 0.32 (0.10 - 0.76)        72 ; 0.40 (0.18 - 0.71)
                              1         80 ; 0.40 (0.17 - 0.94)        80 ; 0.63 (0.30 - 1.02)
                              2         70 ; 0.30 (0.10 - 0.59)        80 ; 0.52 (0.21 - 0.98)
                              3         58 ; 0.26 (0.11 - 0.73)        61 ; 0.40 (0.20 - 0.83)
   Norepinephrine
                              4         50 ; 0.26 (0.10 - 0.90)        48 ; 0.38 (0.18 - 0.66)
                              5         46 ; 0.30 (0.10 - 0.78)        51 ; 0.25 (0.15 - 0.48)
                              6         38 ; 0.32 (0.20 - 0.69)        46 ; 0.26 (0.16 - 0.49)
                              7         38 ; 0.20 (0.10 - 0.56)        42 ; 0.35 (0.14 - 0.58)




© 2025 American Medical Association. All rights reserved, including those for text and data mining,
AI training, and similar technologies.

```

### DOC-004 p.8

[Source](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=8). REPORT.

Join keys: vasoactive exposure denominators101/104 and treatment duration throughD30, secondary catecholamine outcomes. Duration displays median[IQR] in days.


```text
eTable 5. Vasopressor or Inotrope Exposure and Treatment Duration From
Randomization to Day 30



     Drug                         Outcome            Levosimendan                 Placebo

                                  Exposure          (93/101) (92.1%)         (96/104) (92.3%)
     Dobutamine
                                  Duration               6 [4-10]               7 [4.75-13]

                                  Exposure            (8/101) (7.9%)          (5/104) (4.8%)
     Epinephrine
                                  Duration                1 [1-1]                 1 [1-2]

                                  Exposure          (93/101) (92.1%)         (98/104) (94.2%)
     Norepinephrine
                                  Duration               7 [4-11]                 5 [3-12]

                                  Exposure          (14/101) (13.9%)         (12/104) (11.5%)
     Other vasoactive drugsa
                                  Duration             2.5 [1.25-3]              2 [1-3.25]


a
    Other drugs included vasopressin, isoprenaline and milrinone.




© 2025 American Medical Association. All rights reserved, including those for text and data mining,
AI training, and similar technologies.

```

### DOC-004 p.9

[Source](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=9). REPORT.

Join keys: shock-etiology other subgroup21 per arm, main baseline/etiology strata and eFigure9 other group.


```text
eTable 6. Other Causes of Cardiogenic Shock at Randomization



                                                   Levosimendan            Placebo
                                                      N = 21a              N = 21a
 Other causes of cardiogenic shock, no. (%)
     Decompensated dilated cardiomyopathy           3/21 (14.3%)        9/21 (42.9%)
     Acute cardiac arrhythmia                       6/21 (28.6%)        6/21 (28.6%)
     Cardiac arrest prior to ECMO                   5/21 (23.8%)         1/21 (4.8%)
     Takotsubo cardiomyopathy                       3/21 (14.3%)         1/21 (4.8%)
     Acute valvular disease                          1/21 (4.8%)        3/21 (14.3%)
     Miscellaneous conditions b                     3/21 (14.3%)         1/21 (4.8%)
 a
     n/N (%)
 b
  Miscellaneous conditions such as sepsis, late complications of congenital heart
 disease, and thyrotoxic cardiomyopathy.




© 2025 American Medical Association. All rights reserved, including those for text and data mining,
AI training, and similar technologies.

```

### DOC-004 p.10 — eFigure1 patient trajectories

[Source](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=10). REPORT. Stacked counts, axis count at0/30/60/90, treatment on horizontal axis. Join keys: main primary successful-weaning counts, failure and death competitor counts, total randomized/analyzed.

| Trajectory | Levosimendan N101 | Placebo N104 |
|---|---:|---:|
| Successful weaning |69(68.3%)|71(68.3%)|
| Unsuccessful weaning: death |11(10.9%)|12(11.5%)|
| Unsuccessful weaning: heart transplantation |No segment/numeric label|5(4.8%)|
| Unsuccessful weaning: LVAD |4(4.0%)|4(3.8%)|
| Death before weaning |15(14.9%)|12(11.5%)|
| Censored |2(2.0%)|No segment/numeric label|

Legend six categories as above; absent numeric labels are not invented zeros. Color order bottom-to-top: censored, death before weaning, unsuccessful LVAD, unsuccessful heart transplantation, unsuccessful death, success. Matching failure counts can be joined as death/transplant/LVAD components; this map does not substitute their sum for a directly printed aggregate.

### DOC-004 p.11 — eFigure2 mortality D30 and D60

[Source](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=11). REPORT. Mortality cumulative incidence step curves, shaded intervals (confidence level not specified in this caption), placebo pink/red, levosimendan turquoise. D30 panel logrank P=.47; D60 panel logrank P=.56. Vertical scale0%,10%,20%,30%,40%,50%. Horizontal time days. Join keys: main mortality D30/D60 and SAP KM/logrank/Cox; risk sets and cumulative events are distinct quantities.

| Panel / printed array | Time points | Placebo | Levosimendan |
|---|---|---|---|
|D30 number at risk|0,5,10,15,20,25,30|104,101,99,93,84,83,81|101,97,88,83,78,77,75|
|D30 cumulative events|0,5,10,15,20,25,30|0,3,6,14,21,21,23|0,6,16,18,24,25,26|
|D60 number at risk|0,15,30,45,60|104,93,81,80,78|101,83,75,74,73|
|D60 cumulative events|0,15,30,45,60|0,14,23,25,26|0,18,26,27,28|

Curves end near22% placebo versus26% levosimendan atD30, and25% versus28% atD60; these are graphic positions, not additional printed numeric estimates. No HR/CI text is printed in these panels. Late step curves and censor marks retained as visual evidence; event totals above are exact labels.

### DOC-004 p.12 — eFigure3 SOFA subcomponent evolution

[Source](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=12). REPORT. Twelve panels: cardiovascular, respiratory, Glasgow, renal, liver, coagulation, each in levosimendan top row/placebo bottom row. Days1,7,14,21,28; axis SOFA score proportions0,.25,.50,.75,1. Categories0 (light green),1 (medium green),2 (dark green),3-4 (red). Each arm/component/day bar displays categorical proportions summing graphically to1. No participant denominators, individual bar numeric labels, P values, intervals, or contrasts printed. Graphic relationships: cardiovascular day1 entirely3-4 in both arms, lower severe fractions subsequently; respiratory severe fraction falls; renal severe fraction increases later; Glasgow/liver/coagulation mostly lower categories at later times. All60 bars inspected; plotted fractions are not silently converted to exact numbers. Join keys: main/SAP organ failure SOFA threshold, cardiovascular-failure-free days eTable3 (SOFA cardiovascular<2), secondary organ dysfunction.

### DOC-004 p.13 — eFigure4 MACE D30 and D60

[Source](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=13). REPORT. Caption composite death, cardiac transplant, permanent LVAD, stroke, rehospitalization for heart failure. D30 logrank P=.87; D60 logrank P=.94. Vertical0-50% by10%; horizontal days. Placebo pink/red, levosimendan turquoise; shaded intervals not separately quantified in caption. Join keys: main MACE; eTable3 rows; SAP MACE definition/method/window.

| Panel / printed array | Time points | Placebo | Levosimendan |
|---|---|---|---|
|D30 number at risk|0,5,10,15,20,25,30|104,98,91,83,72,70,68|101,96,83,75,69,68,66|
|D30 cumulative events|0,5,10,15,20,25,30|0,7,13,23,33,34,36|0,8,22,26,33,34,35|
|D60 number at risk|0,15,30,45,60|104,83,68,67,65|101,75,66,66,65|
|D60 cumulative events|0,15,30,45,60|0,23,36,38,39|0,26,35,35,36|

Curves end graphically near35% both atD30 and38% placebo/36% levosimendan atD60. Exact printed events are above; no HR or interval limits printed. Composite count is not the sum of separately tabulated component counts because participants may contribute multiple components.

### DOC-004 p.14 — eFigure5 mean blood pressure

[Source](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=14). REPORT. Mean Blood Pressure, mmHg versus day1,5,10,15,20,25,30. Printed total contributor n at those days203,191,139,102,61,44,38 respectively. Levosimendan pink/red; placebo turquoise. Y ticks20,40,60,80,100,120,140. Dashed horizontal threshold60mmHg. Individual translucent trajectories and bold arm centers/error bars; statistic/error-bar definition not supplied in caption. Bold positions roughly76/76 atD1,72/75 D5,68/75 D10,74/74 D15,77/76 D20,74/75 D25,79/77 D30 (levosimendan/placebo; visual approximations only, not printed data). Most bold summaries >60 throughout. No numeric arm estimates/intervals/tests printed. Join keys: SAP revised hemodynamic endpoint p.7, main secondary hemodynamic description.

### DOC-004 p.15 — eFigure6 vasoactive-dose distributions

[Source](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=15). REPORT. Three panels dobutamine, epinephrine, norepinephrine. Dose micrograms/kg/minute; days0-7. Caption median(IQR); placebo pink/red, levosimendan turquoise. Dobutamine y ticks2.5/5/7.5/10; epinephrine0/.5/1/1.5/2; norepinephrine.25/.50/.75/1.00. Median lines/shaded IQR matched to the exact eTable4 rows p.7, which are fully transcribed; no tests/estimates additionally printed. Epinephrine levosimendan line drawn between sparse observations day0/.02,day1/.02,day5/.10,day7/2.00, with no placebo numeric data. Norepinephrine and dobutamine every day0-7 represented. Join keys: eTable4 and main vasoactive-support secondary results. Distinguish interpolation from observed daily tabulated values.

### DOC-004 p.16 — eFigure7 hospital and ICU stays

[Source](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=16). REPORT. Caption distribution up toD60, RMST=Restricted Mean Survival Time. Top hospital stay duration in days, lower ICU duration; y axis number of patients. Placebo green, levosimendan orange. Printed dashed RMST hospital28 levosimendan/35 placebo; ICU17.5 levosimendan/19 placebo. Horizontal ticks0,20,40,60; histogram bars span the follow-up and include substantial hospital pileup at60. No exact numeric bar counts, confidence bounds, denominators, P values or effect differences printed. Histogram heights are graphic distributions, not complete downloadable bin counts. Join keys: main RMST hospitalization/ICU results, SAP p.7 right-censoring and RMST60-day specification. The four RMST labels are exact, their differences are not separately printed here.

### DOC-004 p.17 — eFigure8 serious adverse-event frequency

[Source](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=17). REPORT. Vertical Count; horizontal Serious adverse event number (count of events per patient). Panels levosimendan/placebo. Displayed horizontal categories0,1,2,3,4,5,6,8,9; no7 category is drawn. Levosimendan has no labelled bar at9. Join keys: main number/patients with SAEs, SAP Poisson model allowing recurrent events.

| SAE number per patient | Levosimendan patient count | Placebo patient count |
|---:|---:|---:|
|0|42|43|
|1|22|31|
|2|19|13|
|3|8|4|
|4|2|6|
|5|4|3|
|6|2|1|
|8|2|2|
|9|No labelled bar|1|

These are patient counts stratified by event multiplicity, not event totals. Reconstruct event totals by weighting multiplicity only in checker calculations; source does not print that sum. All labels read visually.

### DOC-004 p.18 — eFigure9 predefined successful-weaning subgroups

[Source](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=18). REPORT. Successful-weaning CIF by shock etiology, caption says predefined subgroups. Four panels, days0/5/10/15 and CIF proportion0-.7 by.1. Legend levosimendan pink/red, placebo turquoise. Printed estimates sHR(95%CI); no P or interaction P, population denominator or adjustment footnote printed on this figure.

| Panel / subgroup | Printed sHR | Printed95%CI |
|---|---:|---|
|A acute myocardial infarction|.73|.37-1.40|
|B myocarditis|2.16|.97-4.80|
|C post-heart surgery|.73|.46-1.15|
|D others|1.61|.78-3.33|

Graphical trajectories: acute MI turquoise rises earlier and ends around.63 versus pink.48 at15; myocarditis turquoise ends near.56 at13 while pink rises to near.58 at5 and then stops; post-heart surgery pink eventually rises to near.69 versus turquoise.55; others pink to near.67 versus turquoise.52. These are visual positions, not printed probabilities. Every panel's line/legend and printed sHR retained without reconciling direction at mapping stage. Join keys: main subgroup figure/treatment-by-etiology analysis, primary CIF, main baseline etiology strata, SAP primary adjustment; eTable6 defines other diagnoses. SAP absence of a subgroup paragraph is recorded at p.9 and is not a candidate conclusion here.

## Administrative support units

### DOC-005 p.1 — nonauthor collaborators, first roster page

[Source](../../../../joi250087supp4_prod_1766516490.97511.pdf#page=1). REPORT. LEVOECMO Trial Group; columns names, suffix, degree, institution, location, role/contribution, group. Includes Paris and Bordeaux investigators and a clinical research assistant; header example labels steering committee and site investigator are form guidance. All rows reviewed. Nonempty NOT_APPLICABLE record: no endpoint, participant denominator, model, intervention rule, outcome definition, statistical plan or inferential value. Administrative form version02-22 and page1of3 are not result quantities. No statistical join key.

### DOC-005 p.2 — nonauthor collaborators, second roster page

[Source](../../../../joi250087supp4_prod_1766516490.97511.pdf#page=2). REPORT. Paris/Lyon/Montpellier/Rennes/Nancy collaborator rows, including research nurse, site investigator and co-investigators. All rows reviewed. NOT_APPLICABLE: personnel/institution/role record only; no quantitative results, prospective statistical definitions or participant-count denominators. Version02-22, page2of3 administrative. No statistical join key.

### DOC-005 p.3 — nonauthor collaborators, last roster page

[Source](../../../../joi250087supp4_prod_1766516490.97511.pdf#page=3). REPORT. Nancy/Nantes/Lille/Paris collaborator rows. All rows reviewed. NOT_APPLICABLE: personnel/institution/role record only; no result-relevant statistical quantity, endpoint status or plan. Version02-22,page3of3 administrative. No statistical join key.

### DOC-006 p.1 — data sharing statement

[Source](../../../../joi250087supp5_prod_1766516490.97511.pdf#page=1). REPORT. Published December01,2025; DOI10.1001/jama.2025.19843; registry identity NCT04728932. Data available: No. Printed registry URL is an identity pointer only and was not opened. NOT_APPLICABLE for quantitative results/planning: no counts, endpoints, analyses, model, workbook formula/cache or statistical decision rule. Registry/DOI/date are bibliographic identifiers. The data-unavailability statement explains absence of accessible structured/raw participant data but is not a candidate or new review limitation on supplied-material coverage.

## Coverage and limits

| Source | Units mapped | Reusable backed | Fresh required | Scientific gap |
|---|---:|---:|---:|---|
|DOC-003|9/9|9|0|None|
|DOC-004|18/18|18|0|None|
|DOC-005|3/3|3|0|None|
|DOC-006|1/1|1|0|None|

Counts:31 page records;6 eTables (eTable3 across2 pages),9 eFigures,3 cause-specific estimate/CI/P triples,4 figure logrank P values,4 subgroup sHR/CI pairs,4 exact figure RMST labels. All printed table rows/numbers/units/footnotes and all figure numeric labels/risk/event arrays transcribed;22 eTable3 rows include one unestimated D60 dialysis row. SAP entire9-page plan mapped, including power, event rules, secondary statuses, methods, missingness, revision and printed formula.

Derivative limitations: legacy engine versions unspecified; SAP empty native text/OCR does not affect visual coverage; image-only plots have no exact numeric coordinate data or histogram bar-count labels, so visual approximations are explicitly marked and never substituted for printed table values. Secondary table bootstrap replication count and CI algorithm not printed here; eFigure5 error-bar statistic not printed; eFigure9 adjustment/model reference direction not separately printed. These are source-description boundaries for checkers, not findings. No Office/cache applicable. No supplied or reused artifact modified. No old conclusions, findings, candidates, screening or classification records read.

### Additional locator provenance — coordinator-supplied targeted OCR

After visual mapping was complete, the coordinator supplied fresh locator text for SAP pp.5/6 under review_1_6_2/preprocessing/gpu_ocr/sap-page-005-text.txt and sap-page-006-text.txt, with engine_record.md. Engine rapidocr-onnxruntime1.4.4/onnxruntime-gpu1.28.0, existing stt Python3.12.3, user-requested RTX5070 via PowerShell5.1/WSL CUDA flags. Engine provider behavior supporting GPU execution is detailed in the coordinator's record; the earlier CPU fallback attempt is preserved and is not described as GPU output. This mapper inspected the new texts only as locator aids after independently reading the unchanged images. OCR omits p.5's full treatment-change sentence and p.6's Gray-test comparison clause, and truncates the unsuccessful-weaning definition; image reading supplies those clauses in the page records above. OCR's spacing, case and partial clauses are not silently treated as source statements. No scientific mapping changes or candidate conclusions follow from OCR omissions. No new derivative was generated by this mapper.
