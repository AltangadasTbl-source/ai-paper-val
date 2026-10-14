# Support core quantitative evidence map

Agent: /root/support_mapping. Scope: DOC-003 PDF pp.1-9, DOC-004 pp.1-18, DOC-005 pp.1-3, DOC-006 p.1. All 31 units mapped. No protocol or main-paper pages are mapped here. Matching main-paper keys below are semantic join keys for the separate main mapper; they are not independent main-paper transcriptions. No candidate diagnosis is performed.

Engine/provenance: reused native/layout text (historic pdftotext version unspecified) for DOC-004 pp.1-18 and DOC-005/006; manual image reading of all SAP pages and DOC-004 figures pp.10-18, with image confirmation of eTables pp.3-6. Reused raster engines/version unspecified. No new extraction/OCR script, rendering, or OCR used by this mapper. The source role is PLAN for DOC-003, REPORT for DOC-004/005/006. No Office/workbook/CSV source exists in this assignment; formulas/cached workbook values are not applicable. The SAP contains a printed mathematical formula, recorded literally below.

## DOC-003: statistical analysis plan

Source: joi250087supp2_prod_1766516490.96511.pdf. Image locators: review_1_5_1/preprocessing/DOC-003/page-001.png through page-006.png; evidence_recheck/doc003_p7.png; DOC-003/lowres-8.jpg and lowres-9.jpg. Empty native/OCR derivatives on pp.5-9 do not delimit coverage. Each image was opened and read anew.

### DOC-003 p.1 — cover and version

[Source](../../../joi250087supp2_prod_1766516490.96511.pdf#page=1). PLAN. Final version printed 11/04/2025; both statistical and methodology signature dates 11/04/2025. LEVOECMO, levosimendan to facilitate weaning from ECMO in severe cardiogenic shock. Sponsor, principal investigator, project manager, data manager, statistician and methodologist identified. No endpoint result, formula, population denominator, or decision rule on this administrative cover. Version date is relevant to plan identity; addresses and telephone numbers are administrative, not result quantities.

### DOC-003 p.2 — contents

[Source](../../../joi250087supp2_prod_1766516490.96511.pdf#page=2). PLAN. Contents: study summary and primary objective/endpoint p.3; secondary endpoints p.4; flow, sample size, analysis population, descriptive analysis, primary analysis p.5; secondary analyses p.7; significance, missing data, plan changes, software and references p.9. No independent result-relevant quantitative relationship on this contents page; all pointed sections opened below.

### DOC-003 p.3 — trial objective and primary endpoint

[Source](../../../joi250087supp2_prod_1766516490.96511.pdf#page=3). PLAN. Multicenter randomized double-blind phase III superiority trial; enrollment spans 24 months; each participant 60 days, including 24-hour treatment and 60-day follow-up. Early levosimendan intended to reduce ECMO duration. Primary objective: efficacy on time to successful ECMO weaning in patients receiving VA-ECMO for acute shock refractory to conventional therapy. Primary endpoint: time to successful ECMO weaning within 30 days following randomization. Success requires survival without ECMO, another mechanical circulatory support device, or heart transplant for 30 days after removal. All removals from randomization to day30 considered; adjudication can require follow-up until day60 for removal on day30. Unsuccessful removal within 30 days and death within 30 days without a weaning attempt are competing events. No event after day30 is considered in event-time follow-up; subjects with none of the three events censored at day30. Join keys: primary endpoint definition/window, success adjudication window, competing risks, intervention duration, follow-up.

### DOC-003 p.4 — secondary endpoint definitions and status

[Source](../../../joi250087supp2_prod_1766516490.96511.pdf#page=4). PLAN. Every following item is explicitly secondary: mortality D30/D60; total ECMO support inclusion-D30 and inclusion-D60 and ECMO-free days through both windows; ICU and total hospital length; MACE occurrence at D30/D60 (death, cardiac transplant, permanent LVAD escalation, stroke, rehospitalization for heart failure); time to hemodynamic improvement defined as mean blood pressure >60 mmHg; organ-failure days with SOFA >2 in at least one of six organ systems and organ-failure-free days inclusion-D30; catecholamine support duration/free days inclusion-D30; MV duration/free days inclusion-D30 and inclusion-D60; RRT duration/free days inclusion-D30; LV function by echocardiography at day30, left ventricular ejection fraction in percent. Safety includes incidence of drug-related atrial fibrillation, ventricular arrhythmias, ventricular fibrillation, torsades de pointes, hypokalemia, and any follow-up adverse events. Join keys: all secondary and safety endpoint statuses, windows and composite components; eTable3; eFigures2-8; main secondary outcomes and adverse-event table.

### DOC-003 p.5 — population, power and summaries

[Source](../../../joi250087supp2_prod_1766516490.96511.pdf#page=5). PLAN. Flow diagram planned to enumerate screened eligible, randomized totals, arm distribution, follow-up/losses and analyzed numbers. Sample size: control success cumulative incidence 50% from similar 30-day cohort accounting for death/weaning-failure competing risks; subdistribution HR 1.75; two-sided alpha 5%; power 80%; 101 successful-weaning events required under cited Latouche formula; total206,103 per group. No explicit numerical sample-size formula printed on this page. ITT primary analysis: every randomized participant in assigned arm regardless of treatment changes. Qualitative frequencies/percentages; normally distributed quantitative variables mean/SD; non-normal median/IQR and range; censored-data KM or CIF rates at15/30/60 days with95%CI where appropriate. Primary time-to-success within30 days accounts for competing risks; success definition repeats survival without ECMO/additional mechanical support/transplant for30 days after removal. Join keys: main sample-size assumptions, randomized/analyzed population, descriptive statistics and primary estimand.

### DOC-003 p.6 — primary event coding and inferential analysis

[Source](../../../joi250087supp2_prod_1766516490.96511.pdf#page=6). PLAN. Success event of interest; still on ECMO day30 censored; death before day30 without weaning competing; unsuccessful removal (death, repeat ECMO, additional mechanical support/transplant within30 days after removal) competing; lost before30 days censored. Time to success randomization-to-success date; unsuccessful time randomization-to-removal date; death without removal randomization-to-death date; loss randomization-to-last-news date; no event censor time30 days. CIF rates15/30 days with95%CI and group curves; Gray test of success CIF. Fine-Gray adjusted for primary shock etiology (acute MI, myocarditis, post-heart surgery, other) estimates treatment sHR and95%CI for each defined event. Proportional hazards assessed using Schoenfeld residuals. Sensitivity cause-specific Cox estimates treatment cause-specific HR and95%CI. Join keys: main primary model/covariate/Gray P/sHR; eTable2 cause-specific sensitivity; primary failure/death competitor results.

### DOC-003 p.7 — secondary analysis methods and disclosed revision

[Source](../../../joi250087supp2_prod_1766516490.96511.pdf#page=7). PLAN. Mortality: KM95%CI; only survival analysis through60 days, time from randomization to death irrespective of prior weaning, last news or follow-up end; logrank comparison; etiology-adjusted Cox. ECMO durations/free days D30/D60: Wilcoxon rank-sum; deaths assigned0 ECMO-free days; etiology-adjusted general linear model. ICU/hospital: RMST through60 days with95%CI because ongoing hospitalization leads to right censoring; logrank; etiology-adjusted Cox. MACE definition repeats all five components; KM95%CI through60 days; event time randomization-to-first-MACE, last update or end whichever first; logrank; etiology-adjusted Cox. Hemodynamic improvement is explicitly revised: originally >60mmHg time-to-improvement under competing risks, but descriptive inspection before inferential analysis found most patients stably >60 throughout follow-up; removed from inferential analysis as non-informative, replaced by descriptive MBP plot throughD30. Organ failure definition SOFA>2 in at least one of six systems; duration/free days throughD30 compared Wilcoxon; death assigned0 failure-free days; etiology-adjusted general linear model. Join keys: secondary methods, revision disclosure, eFigures2/4/5/7, eTable3.

### DOC-003 p.8 — secondary methods, hierarchical LV function and safety

[Source](../../../joi250087supp2_prod_1766516490.96511.pdf#page=8). PLAN. Catecholamine duration/free days inclusion-D30: Wilcoxon, deaths assigned0 catecholamine-free days; etiology-adjusted general linear model. MV duration/free days inclusion-D30/D60: Wilcoxon, death0 ventilator-free days; etiology-adjusted general linear model. RRT duration/free days inclusion-D30: Wilcoxon; the printed death rule says0 "ventilatory-free days"; etiology-adjusted general linear model. This literal wording is preserved for checker interpretation, without normalization.

LV function uses Global Net Benefit atD30 with hierarchical composite: (1)death,(2)heart transplantation,(3)LV improvement defined LVEF>30%. Every experimental patient pairwise compared with every control patient. Experimental survival versus control death is a win; if both survive, avoiding transplantation versus control transplant is a win; if neither transplanted, greater LV improvement atD30 wins; same outcome at every hierarchical level is tie. Printed formula wording: "Number of Wins–Number of Losses/Total number of comparisons". Intended grouping is not inferred here. Positive net benefit favors experimental treatment;95%CI bootstrap. Safety drug adverse-reaction incidence (AF, ventricular arrhythmia/VF/torsades/hypokalemia) uses Poisson regression allowing more than one event per patient, adjusted for prognostic factors. Join keys: main/eTable3 LVEF analysis, planned hierarchical endpoint, safety event model.

### DOC-003 p.9 — safety continuation, alpha, missingness and plan changes

[Source](../../../joi250087supp2_prod_1766516490.96511.pdf#page=9). PLAN. Any follow-up AE described overall/by arm by patient count/percentage; serious AEs separately. Numbers of AEs and SAEs compared by etiology-adjusted Poisson model. All analyses two-sided alpha5%. Primary loss-to-follow-up censored; no imputation because survival handles censoring; non-informative censoring assumed (loss independent of primary-event risk). Any modifications must precede database unblinding and receive systematic scientific-committee validation. R4.4.2. Latouche/Porcher/Chevret2004 sample-size reference; no additional numeric method or stopping/interim rule here. No subgroup-analysis prescription appears anywhere in this9-page SAP. No further multiplicity decision rule is printed beyond alpha5%. Join keys: main missing-data handling, significance/multiplicity, software, safety count model, prespecification/revision.

## DOC-004: results supplement

Native text is reproduced by page for completeness below. Table superscript1 is a footnote marker, not a denominator digit: p.3 headers mean146,69,77,59,32,27. All percentages are percent, differences for categorical endpoints are percentage points; continuous differences retain the row unit. Treatment contrast is levosimendan versus placebo except eTable4 explicitly prints placebo first. Tables retain every printed signed zero and dash. Page-specific join keys precede the transcription.

### DOC-004 p.1

[Source](../../../joi250087supp3_prod_1766516490.97011.pdf#page=1). REPORT.

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

[Source](../../../joi250087supp3_prod_1766516490.97011.pdf#page=2). REPORT.

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

[Source](../../../joi250087supp3_prod_1766516490.97011.pdf#page=3). REPORT.

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

[Source](../../../joi250087supp3_prod_1766516490.97011.pdf#page=4). REPORT.

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

[Source](../../../joi250087supp3_prod_1766516490.97011.pdf#page=5). REPORT.

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

[Source](../../../joi250087supp3_prod_1766516490.97011.pdf#page=6). REPORT.

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

[Source](../../../joi250087supp3_prod_1766516490.97011.pdf#page=7). REPORT.

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

[Source](../../../joi250087supp3_prod_1766516490.97011.pdf#page=8). REPORT.

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

[Source](../../../joi250087supp3_prod_1766516490.97011.pdf#page=9). REPORT.

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

[Source](../../../joi250087supp3_prod_1766516490.97011.pdf#page=10). REPORT. Stacked counts, axis count at0/30/60/90, treatment on horizontal axis. Join keys: main primary successful-weaning counts, failure and death competitor counts, total randomized/analyzed.

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

[Source](../../../joi250087supp3_prod_1766516490.97011.pdf#page=11). REPORT. Mortality cumulative incidence step curves, shaded intervals (confidence level not specified in this caption), placebo pink/red, levosimendan turquoise. D30 panel logrank P=.47; D60 panel logrank P=.56. Vertical scale0%,10%,20%,30%,40%,50%. Horizontal time days. Join keys: main mortality D30/D60 and SAP KM/logrank/Cox; risk sets and cumulative events are distinct quantities.

| Panel / printed array | Time points | Placebo | Levosimendan |
|---|---|---|---|
|D30 number at risk|0,5,10,15,20,25,30|104,101,99,93,84,83,81|101,97,88,83,78,77,75|
|D30 cumulative events|0,5,10,15,20,25,30|0,3,6,14,21,21,23|0,6,16,18,24,25,26|
|D60 number at risk|0,15,30,45,60|104,93,81,80,78|101,83,75,74,73|
|D60 cumulative events|0,15,30,45,60|0,14,23,25,26|0,18,26,27,28|

Curves end near22% placebo versus26% levosimendan atD30, and25% versus28% atD60; these are graphic positions, not additional printed numeric estimates. No HR/CI text is printed in these panels. Late step curves and censor marks retained as visual evidence; event totals above are exact labels.

### DOC-004 p.12 — eFigure3 SOFA subcomponent evolution

[Source](../../../joi250087supp3_prod_1766516490.97011.pdf#page=12). REPORT. Twelve panels: cardiovascular, respiratory, Glasgow, renal, liver, coagulation, each in levosimendan top row/placebo bottom row. Days1,7,14,21,28; axis SOFA score proportions0,.25,.50,.75,1. Categories0 (light green),1 (medium green),2 (dark green),3-4 (red). Each arm/component/day bar displays categorical proportions summing graphically to1. No participant denominators, individual bar numeric labels, P values, intervals, or contrasts printed. Graphic relationships: cardiovascular day1 entirely3-4 in both arms, lower severe fractions subsequently; respiratory severe fraction falls; renal severe fraction increases later; Glasgow/liver/coagulation mostly lower categories at later times. All60 bars inspected; plotted fractions are not silently converted to exact numbers. Join keys: main/SAP organ failure SOFA threshold, cardiovascular-failure-free days eTable3 (SOFA cardiovascular<2), secondary organ dysfunction.

### DOC-004 p.13 — eFigure4 MACE D30 and D60

[Source](../../../joi250087supp3_prod_1766516490.97011.pdf#page=13). REPORT. Caption composite death, cardiac transplant, permanent LVAD, stroke, rehospitalization for heart failure. D30 logrank P=.87; D60 logrank P=.94. Vertical0-50% by10%; horizontal days. Placebo pink/red, levosimendan turquoise; shaded intervals not separately quantified in caption. Join keys: main MACE; eTable3 rows; SAP MACE definition/method/window.

| Panel / printed array | Time points | Placebo | Levosimendan |
|---|---|---|---|
|D30 number at risk|0,5,10,15,20,25,30|104,98,91,83,72,70,68|101,96,83,75,69,68,66|
|D30 cumulative events|0,5,10,15,20,25,30|0,7,13,23,33,34,36|0,8,22,26,33,34,35|
|D60 number at risk|0,15,30,45,60|104,83,68,67,65|101,75,66,66,65|
|D60 cumulative events|0,15,30,45,60|0,23,36,38,39|0,26,35,35,36|

Curves end graphically near35% both atD30 and38% placebo/36% levosimendan atD60. Exact printed events are above; no HR or interval limits printed. Composite count is not the sum of separately tabulated component counts because participants may contribute multiple components.

### DOC-004 p.14 — eFigure5 mean blood pressure

[Source](../../../joi250087supp3_prod_1766516490.97011.pdf#page=14). REPORT. Mean Blood Pressure, mmHg versus day1,5,10,15,20,25,30. Printed total contributor n at those days203,191,139,102,61,44,38 respectively. Levosimendan pink/red; placebo turquoise. Y ticks20,40,60,80,100,120,140. Dashed horizontal threshold60mmHg. Individual translucent trajectories and bold arm centers/error bars; statistic/error-bar definition not supplied in caption. Bold positions roughly76/76 atD1,72/75 D5,68/75 D10,74/74 D15,77/76 D20,74/75 D25,79/77 D30 (levosimendan/placebo; visual approximations only, not printed data). Most bold summaries >60 throughout. No numeric arm estimates/intervals/tests printed. Join keys: SAP revised hemodynamic endpoint p.7, main secondary hemodynamic description.

### DOC-004 p.15 — eFigure6 vasoactive-dose distributions

[Source](../../../joi250087supp3_prod_1766516490.97011.pdf#page=15). REPORT. Three panels dobutamine, epinephrine, norepinephrine. Dose micrograms/kg/minute; days0-7. Caption median(IQR); placebo pink/red, levosimendan turquoise. Dobutamine y ticks2.5/5/7.5/10; epinephrine0/.5/1/1.5/2; norepinephrine.25/.50/.75/1.00. Median lines/shaded IQR matched to the exact eTable4 rows p.7, which are fully transcribed; no tests/estimates additionally printed. Epinephrine levosimendan line drawn between sparse observations day0/.02,day1/.02,day5/.10,day7/2.00, with no placebo numeric data. Norepinephrine and dobutamine every day0-7 represented. Join keys: eTable4 and main vasoactive-support secondary results. Distinguish interpolation from observed daily tabulated values.

### DOC-004 p.16 — eFigure7 hospital and ICU stays

[Source](../../../joi250087supp3_prod_1766516490.97011.pdf#page=16). REPORT. Caption distribution up toD60, RMST=Restricted Mean Survival Time. Top hospital stay duration in days, lower ICU duration; y axis number of patients. Placebo green, levosimendan orange. Printed dashed RMST hospital28 levosimendan/35 placebo; ICU17.5 levosimendan/19 placebo. Horizontal ticks0,20,40,60; histogram bars span the follow-up and include substantial hospital pileup at60. No exact numeric bar counts, confidence bounds, denominators, P values or effect differences printed. Histogram heights are graphic distributions, not complete downloadable bin counts. Join keys: main RMST hospitalization/ICU results, SAP p.7 right-censoring and RMST60-day specification. The four RMST labels are exact, their differences are not separately printed here.

### DOC-004 p.17 — eFigure8 serious adverse-event frequency

[Source](../../../joi250087supp3_prod_1766516490.97011.pdf#page=17). REPORT. Vertical Count; horizontal Serious adverse event number (count of events per patient). Panels levosimendan/placebo. Displayed horizontal categories0,1,2,3,4,5,6,8,9; no7 category is drawn. Levosimendan has no labelled bar at9. Join keys: main number/patients with SAEs, SAP Poisson model allowing recurrent events.

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

[Source](../../../joi250087supp3_prod_1766516490.97011.pdf#page=18). REPORT. Successful-weaning CIF by shock etiology, caption says predefined subgroups. Four panels, days0/5/10/15 and CIF proportion0-.7 by.1. Legend levosimendan pink/red, placebo turquoise. Printed estimates sHR(95%CI); no P or interaction P, population denominator or adjustment footnote printed on this figure.

| Panel / subgroup | Printed sHR | Printed95%CI |
|---|---:|---|
|A acute myocardial infarction|.73|.37-1.40|
|B myocarditis|2.16|.97-4.80|
|C post-heart surgery|.73|.46-1.15|
|D others|1.61|.78-3.33|

Graphical trajectories: acute MI turquoise rises earlier and ends around.63 versus pink.48 at15; myocarditis turquoise ends near.56 at13 while pink rises to near.58 at5 and then stops; post-heart surgery pink eventually rises to near.69 versus turquoise.55; others pink to near.67 versus turquoise.52. These are visual positions, not printed probabilities. Every panel's line/legend and printed sHR retained without reconciling direction at mapping stage. Join keys: main subgroup figure/treatment-by-etiology analysis, primary CIF, main baseline etiology strata, SAP primary adjustment; eTable6 defines other diagnoses. SAP absence of a subgroup paragraph is recorded at p.9 and is not a candidate conclusion here.

## Administrative support units

### DOC-005 p.1 — nonauthor collaborators, first roster page

[Source](../../../joi250087supp4_prod_1766516490.97511.pdf#page=1). REPORT. LEVOECMO Trial Group; columns names, suffix, degree, institution, location, role/contribution, group. Includes Paris and Bordeaux investigators and a clinical research assistant; header example labels steering committee and site investigator are form guidance. All rows reviewed. Nonempty NOT_APPLICABLE record: no endpoint, participant denominator, model, intervention rule, outcome definition, statistical plan or inferential value. Administrative form version02-22 and page1of3 are not result quantities. No statistical join key.

### DOC-005 p.2 — nonauthor collaborators, second roster page

[Source](../../../joi250087supp4_prod_1766516490.97511.pdf#page=2). REPORT. Paris/Lyon/Montpellier/Rennes/Nancy collaborator rows, including research nurse, site investigator and co-investigators. All rows reviewed. NOT_APPLICABLE: personnel/institution/role record only; no quantitative results, prospective statistical definitions or participant-count denominators. Version02-22, page2of3 administrative. No statistical join key.

### DOC-005 p.3 — nonauthor collaborators, last roster page

[Source](../../../joi250087supp4_prod_1766516490.97511.pdf#page=3). REPORT. Nancy/Nantes/Lille/Paris collaborator rows. All rows reviewed. NOT_APPLICABLE: personnel/institution/role record only; no result-relevant statistical quantity, endpoint status or plan. Version02-22,page3of3 administrative. No statistical join key.

### DOC-006 p.1 — data sharing statement

[Source](../../../joi250087supp5_prod_1766516490.97511.pdf#page=1). REPORT. Published December01,2025; DOI10.1001/jama.2025.19843; registry identity NCT04728932. Data available: No. Printed registry URL is an identity pointer only and was not opened. NOT_APPLICABLE for quantitative results/planning: no counts, endpoints, analyses, model, workbook formula/cache or statistical decision rule. Registry/DOI/date are bibliographic identifiers. The data-unavailability statement explains absence of accessible structured/raw participant data but is not a candidate or new review limitation on supplied-material coverage.

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


# DOC-002 protocol mapping: PDF pages 1–51

Runtime canonical ID: /root/protocol_mapping_001. Fresh support-mapping shard. Exact source: joi250087supp1_prod_1766516490.96011.pdf, PDF pages 1–51 only. Role: PLAN throughout. Complete original protocol version 1.1 occupies PDF pp.3–47 (printed pp.1–45). Version 2.0 cover/signature/contents occupy assigned pp.48–51. Scientific contents of later versions are assigned elsewhere.

Coverage: 51 of 51 pages mapped; 49 reusable-backed and 2 fresh-required. No scientific coverage gaps. Forty-seven relationship groups QP1-001–QP1-047 follow; each may contain explicitly enumerated related components. Matching main-paper keys are semantic keys for subsequent matching, not assertions that the report contains every planned endpoint. No candidates were diagnosed, and no old review conclusions were read. No Office, workbook or CSV source occurs in the assigned scope; formulas and cached workbook values are not applicable.

## Extraction provenance

Reusable locator: .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/layout_all_pages.txt (historical pdftotext version unspecified). All 51 assigned form-feed records were read in bounded page ranges 1–9, 10–13, 14–17, 18–28, 29–38 and 39–51; p45 was reread independently because a combined output was truncated. No unassigned source page was read. Normative scope, review contract, tooling record, source inventory, evidence-asset inventory, source coverage and coverage manifest were read.

Fresh native text, sorted reading-order text and rendered images were produced for exact PDF pp.4 and49. Text is empty because both are scanned signature pages, not blank pages. Both fresh 200-dpi images were visually inspected. PyMuPDF 1.26.4 rendered on the CPU; no OCR was necessary. Run-level GPU authorization did not change these derivative engines. The exact derivatives are native-004.txt, layout-004.txt, page-004.png, native-049.txt, layout-049.txt and page-049.png under .ai_paper_validation/review_1_6_2/preprocessing/protocol_001/. Engine for native text: PyMuPDF; for layout: PyMuPDF sorted reading order; for rendering: PyMuPDF CPU at200dpi. Sources and reused assets remain unchanged.

For each N=4 or49, these bundled helper commands were executed with the corresponding zero-padded output filename:

```bash
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py text joi250087supp1_prod_1766516490.96011.pdf --first N --last N .ai_paper_validation/review_1_6_2/preprocessing/protocol_001/native-NNN.txt
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py text joi250087supp1_prod_1766516490.96011.pdf --first N --last N .ai_paper_validation/review_1_6_2/preprocessing/protocol_001/layout-NNN.txt --layout
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py render joi250087supp1_prod_1766516490.96011.pdf --page N .ai_paper_validation/review_1_6_2/preprocessing/protocol_001/page-NNN.png
```

## Complete page ledger

Every row is COMPLETE. Not applicable means inspected and no result-relevant quantitative relationship was present. Historical numerical context is retained separately from prospective trial design.

| PDF page | Inspected content and quantitative applicability | Relationship groups |
|---:|---|---|
| 1 | Protocol cover, investigator/contact details; no trial quantity | Identity context |
| 2 | Bundle version index and changes pointer | QP1-001 |
| 3 | Original protocol cover, version1.1 and project identity | QP1-001 |
| 4 | Fresh scanned signed original protocol page, not blank | QP1-002 |
| 5 | Original contents, sections1–11; pointers only, not applicable | Contents inspected |
| 6 | Original contents, sections12–18; pointers only, not applicable | Contents inspected |
| 7 | Summary rationale and30-day primary objective | QP1-003,004 |
| 8 | Success/competing risks, secondary endpoints, subgroups, inclusion | QP1-004–021 |
| 9 | Exclusions, intervention and initial measurement schedule | QP1-021–025 |
| 10 | Follow-up status, sample size, administrative timeline | QP1-026,027 |
| 11 | Historical ECMO outcomes and pharmacokinetics | QP1-028,029 |
| 12 | Historical SURVIVE, LeoPARDS, LICORN, LEVO-CTS, CHEETAH | QP1-030–033 |
| 13 | Historical CHEETAH and observational ECMO series | QP1-033,034 |
| 14 | Primary and complete secondary objectives | QP1-004–020 |
| 15 | Detailed primary competing-risk definition and secondary outcomes | QP1-004–020 |
| 16 | Superiority design and stochastic minimization | QP1-035,036 |
| 17 | Blinding/unblinding and placebo appearance; no additional quantity | QP1-022 context |
| 18 | Consent table, treatment timing and baseline data definitions | QP1-023–025 |
| 19 | Daily collection and protocolized weaning decision thresholds | QP1-025,037 |
| 20 | D30/D60 status, participation duration and schedule table | QP1-026,027 |
| 21 | Standard-care table, withdrawal and drug stopping thresholds | QP1-038 |
| 22 | Retained data, SAE follow-up, trial cancellation | QP1-038,039 |
| 23 | Complete inclusion/exclusion list | QP1-021 |
| 24 | Consent, screening reasons, recruitment table | QP1-027,040 |
| 25 | Pharmacokinetics, vial concentration and packaging | QP1-029,041 |
| 26 | Drug dose, preparation table and ECMO management | QP1-022,041,042 |
| 27 | Common management, prohibited drug, efficacy window | QP1-042,043 |
| 28 | Safety event definitions | QP1-044 |
| 29 | AE severity/causality table and notification rules | QP1-044 |
| 30 | Notification exemptions and refractory hypotension threshold | QP1-038,044 |
| 31 | Monthly death monitoring, safety imbalance and AE thresholds | QP1-039,044 |
| 32 | SAE resolution and sponsor assessment; no efficacy quantity | QP1-044 |
| 33 | Administrative safety-reporting timelines | QP1-044 |
| 34 | DSMB safety remit; data-management administration | QP1-039 |
| 35 | Statistical overview, alpha, descriptive summaries and adjustment | QP1-045 |
| 36 | ITT exception, event/censor coding and time definitions | QP1-004,005,046 |
| 37 | Fine–Gray, secondary models, sample-size inputs and alpha | QP1-047 |
| 38 | Pre-unblinding amendment rule and principal ITT | QP1-046 |
| 39 | Missing CRF data coding and audit trail | QP1-046 |
| 40 | Consent/emergency enrollment; administrative, no additional quantity | QP1-021 context |
| 41 | Sponsor halt and amendment approval; administrative | QP1-039,046 context |
| 42 | Archives, funding, insurance and publication; no trial result | Not applicable |
| 43 | Publication/registration placeholder; no trial result | Not applicable |
| 44 | Bibliography1–16; no new trial relationship | Historical reference locators |
| 45 | Bibliography17–30; no new trial relationship | Historical reference locators |
| 46 | Bibliography31–38, including Latouche sample-size reference | QP1-047 reference |
| 47 | Addenda/scales/product pointers; no new quantitative relationship | Scale identities inspected |
| 48 | Version2.0 cover, date and project identity | QP1-001 |
| 49 | Fresh scanned second-version signature/approval page, not blank | QP1-002 |
| 50 | Version2.0 contents1–11; pointers only | Not applicable |
| 51 | Version2.0 contents12–18; pointers only | Not applicable |

## Complete relationship map

All entries have document role PLAN. Direct evidence links below resolve to the supplied PDF. Other page numbers in each entry are also exact PDF locators. Historical studies have no matching LEVOECMO trial-result key.

### QP1-001 — Version provenance

[PDFp2](../../../joi250087supp1_prod_1766516490.96011.pdf#page=2) lists original1.1,12/04/2020; second2.0,05/31/2023; final3.0,06/26/2024; summary of changes. [p3](../../../joi250087supp1_prod_1766516490.96011.pdf#page=3) prints version1.1 of04/12/2020, P170914J and EUDRACT2019-004319-29. [p48](../../../joi250087supp1_prod_1766516490.96011.pdf#page=48) prints version2.0 of31/05/2023. Preserve date strings: index and covers use different day/month conventions. Footer April2018 is template date. Matching key: protocol version/amendment provenance.

### QP1-002 — Fresh signature pages

[p4](../../../joi250087supp1_prod_1766516490.96011.pdf#page=4), printed2/45: research codeP170914J, version1.1 of04/12/2020; investigator date appears2/7/2021 (administrative handwriting uncertainty); sponsor stamp19JUL2021; CPP and ANSM date placeholders remain dotted. [p49](../../../joi250087supp1_prod_1766516490.96011.pdf#page=49), printed2/46: version2.0 of31/05/2023; investigator handwriting18/7/2023; sponsor signature/date unfilled; CPP OuestIII approval04/01/2021 and ANSM authorization30/11/2020. Matching key: administrative version identity, no efficacy result.

### QP1-003 — Pharmacologic summary

p7: action up to7–9days through active metabolite; single24h perfusion rationale. Pharmacologic context rather than outcome follow-up. Key: intervention-duration rationale.

### QP1-004 — Primary endpoint and windows

[pp7–8](../../../joi250087supp1_prod_1766516490.96011.pdf#page=8),[p14](../../../joi250087supp1_prod_1766516490.96011.pdf#page=14),[p15](../../../joi250087supp1_prod_1766516490.96011.pdf#page=15): time to successful ECMO weaning within30days after randomization. Success requires survival without ECMO, another mechanical circulatory device or heart transplantation for30days after removal. All removals up toD30 considered; removalD30 requires success ascertainment throughD60. No event after30days enters event-time analysis; those remaining on ECMO or without defined event censoredD30. p14 places unsuccessful weaning at attempted-weaning date. Key: primary outcome, status, window and event timing.

### QP1-005 — Competing risks, censoring and time definitions

pp8,15,[p36](../../../joi250087supp1_prod_1766516490.96011.pdf#page=36): successful weaning is event of interest. Competing events: death beforeD30 without weaning and unsuccessful weaning (death, repeat ECMO, another device or transplant within30days after removal). Time to successful weaning = weaning date minus randomization date. Unsuccessful time = removal date minus randomization date. Death time = death date minus randomization date. Lost-follow-up time = latest-news date minus randomization date, censored. Other patients censored at time30days. p15 rejects days alive without ECMO as primary because death on ECMO produces tied0days. Key: event coding, competing risks and time formulas.

### QP1-006 — Mortality

pp8,14,15: secondary mortalityD30 andD60. p20 records living/dead and death date/hour. p37 survival analysis restricted to60days. Key: mortality status and time points.

### QP1-007 — ECMO duration

pp8,14,15: total support duration inclusion–D30 and inclusion–D60. Key: ECMO duration and window.

### QP1-008 — ECMO-free days

pp8,14,15: number of ECMO-free days inclusion–D30/D60. No further zero-assignment algorithm printed here. Key: ECMO-free days, secondary status and window.

### QP1-009 — ICU duration

pp8,14,15: ICU stay duration. p20 records ICU discharge status/dateD30/D60. Key: ICU duration.

### QP1-010 — Hospital duration

pp8,14,15: hospitalization duration. p20 records hospital discharge status/dateD30/D60. Key: hospital duration.

### QP1-011 — Cardiovascular composite

pp8,14,15: major adverse cardiovascular eventsD30/D60 comprising death, cardiac transplant, escalation to permanentLVAD, stroke, dialysis and rehospitalization for heart failure. Key: composite components, status and time.

### QP1-012 — Organ failure

pp8,14,15: days with organ failure defined bySOFA and days alive without organ failure inclusion–D30. p14 says days without organ failure; pp8,15 expressly include alive condition. p47 listsSOFA addendum. No specific score threshold printed here. Key: SOFA/organ-failure duration and alive-free days.

### QP1-013 — Catecholamine support duration

pp8,14,15: duration of hemodynamic support with catecholamines. Key: secondary support duration.

### QP1-014 — Hemodynamic support-free days

pp8,14,15: days alive without hemodynamic support inclusion–D30. Key: alive support-free days and window.

### QP1-015 — Ventilation duration

pp8,14,15: duration of mechanical ventilation. Key: secondary ventilation duration.

### QP1-016 — Ventilator-free days

pp8,14,15: days alive without mechanical ventilation inclusion–D30 and inclusion–D60. Key: alive ventilation-free days and windows.

### QP1-017 — LV function

pp8,14,15: echocardiographic LV functionD30 after randomization. Key: LV function, secondary status and assessment time.

### QP1-018 — Hemodynamic time outcomes

pp8,14,15: time to improvement in systolic/diastolic/meanBP and heart rate; time to stabilization. No single numerical improvement threshold printed. Weaning readiness separatelyp19. Key: hemodynamic improvement/stabilization outcomes.

### QP1-019 — Drug reactions

pp8,14,15: incidence of atrial fibrillation, other supraventricular arrhythmias, ventricular arrhythmias including tachycardia/fibrillation/torsades, and hypokalemia. Key: adverse-reaction outcomes and secondary status.

### QP1-020 — Outcome subgroups

pp8,14,15: primary and secondary endpoints in prespecified acuteMI, myocarditis, post-cardiac-surgery and post-cardiac-arrest subgroups. No interaction-test specification printed. These groups are distinct from allocation factors below. Key: prespecified etiology subgroup analyses.

### QP1-021 — Eligibility/population

pp8–9,[p23](../../../joi250087supp1_prod_1766516490.96011.pdf#page=23): adults with refractory acute cardiogenic shock, VA-ECMO in preceding48h, recovery likely, relative/surrogate consent or emergency enrollment. Twenty exclusions: age<18; pregnancy/lactation; ECMO>48h; resuscitation>30min before ECMO; irreversible neurological pathology; end-stage cardiomyopathy without recovery hope; mechanicalMI complication; aortic regurgitation>II; ECMO for pulmonary embolism; cardiotoxic intoxication; afterLVAD; heart-transplant recipient; moribund/SAPSII>90; ChildB/C cirrhosis or other severe hepatic insufficiency; chronic dialysis; levosimendan hypersensitivity; torsades history; epilepsy; guardianship/permanent legal incompetence; another interventional study. pp24,40 permit emergency randomization then subsequent consent. Key: eligibility and randomized population.

### QP1-022 — Dose and comparator

[p9](../../../joi250087supp1_prod_1766516490.96011.pdf#page=9),[p26](../../../joi250087supp1_prod_1766516490.96011.pdf#page=26): continuousIV24h, no initial bolus; start0.15μg/kg/min, increase0.20μg/kg/min after2h if no rate-limiting effects. Riboflavin placebo reproduces yellow color, identical route/procedure/duration. p17 states double blinding and ICU nurse preparation. Key: randomized dose/duration/comparator.

### QP1-023 — Start window

p18: start as soon as possible, no later than24h after randomization; infusion24h. Key: intervention timing.

### QP1-024 — Baseline covariate definitions

p18: McCabe/Jackson, Charlson, SAPSII, SOFA; severe LV dysfunction byNYHA/EF; hepatic insufficiency bilirubin>100μmol/L or albumin<35g/L without another cause. Immunocompromised yes/no. Key: baseline prognostic definitions when matched to adjustment.

### QP1-025 — Repeated measurement schedule

pp9–10,18–19: baselineD1, thenD2–D30 or death/ICU discharge; p19 says days1,2,3…30. BP/HR, catecholamine doses, ventilation/RRT yes/no, urine output, potassium/ionogram, lactate, blood gases, WBC, platelets, renal/hepatic markers, SOFA, ECG. Echo: LVEF, LV outflowVTI and lateral mitral-annulus systolic TissueDoppler velocity. ECMO: FiO2, membrane ventilation, pump speed/flow, clots, blockage/change, hemolysis, cannulation hemorrhage/infection and leg ischemia. No repeated-measures model printed here. Key: measurement windows and physiological endpoints.

### QP1-026 — Status follow-up and schedule table

pp10,20: D30/D60 vital/ECMO status, repeat ECMO, other support, transplant, ventilation, ICU/hospital discharge and dates. Contact details at ICU discharge permitD60 collection. p20 table: D1 information/consent/randomization/history/dispensing; clinical exam, ECG/echoD1 andD2–D30 or death/discharge; AE/vital/ECMO statusD1, subsequent period andD60; continuation consent during follow-up andD60 if not obtained. Key: ascertainment schedule.

### QP1-027 — Enrollment and timeline

p10:206 subjects,103/arm;13sites;24months recruitment,2months participation,26months total,0.7subjects/site/month. p20:60days participation/follow-up,24h treatment. p24 recruitment table:206;13sites;24months;15.8subjects/site (printed15,8);0.66subjects/site/month. Key: planned sample size; site/calendar projections administrative.

### QP1-028 — Historical ECMO context

p11: long-term survival70–80% myocarditis/poisoning,40–50%MI,15–25% refractory cardiac arrest; hemorrhage10–20%, cannulation infection/bacteremia10–15%, limb ischemia5–10%, stroke5%. p30 historical mortality40–60%; p31 historical58%. No LEVOECMO-result counterpart.

### QP1-029 — Pharmacokinetics

pp11–12,25: half-life60min, clearance300mL/min, protein binding97%, equilibrium4–8h; active metabolite half-life about3days. p25 discusses effects through48h and historical24h levosimendan versus48h dobutamine. No trial-result counterpart.

### QP1-030 — Historical SURVIVE

p12: n1327; loading12μg/kg then0.1–0.2μg/kg/min for additional23h; BNP first5days; mortality180days26% versus28%, HR0.91,[0.74–1.13],P0.40. Levosimendan versus dobutamine, historical.

### QP1-031 — Historical LeoPARDS

p12:0.1μg/kg/min then0.2 for20–22h; mean±SD SOFA6.68±3.96 versus6.06±3.89,P0.053; D28 mortality34.5% versus30.9%,P0.43. Historical placebo comparison.

### QP1-032 — Historical LICORN/LEVO-CTS

p12: n336/n882, prophylactic0.1μg/kg/min24h from anesthesia. LICORN composite: prolonged catecholamines, LV assist, RRT. LEVO-CTS: death,RRT,perioperativeMI,mechanical assist. Low cardiac output22% in LEVO-CTS; approximately half needed catecholamines>24h in both. No group differences stated. Historical.

### QP1-033 — Historical CHEETAH

pp12–13: LVEF<25%, high-dose inotropes/IABP;0.025–0.2μg/kg/min without loading for up to48h or ICU discharge; futility stop after506. D30 deaths32(12.9%) versus33(12.8%), absoluteRD0.1percentage points,95%CI−5.7to5.9,P0.97; mean infusion0.07μg/kg/min. This is not LEVOECMO stopping.

### QP1-034 — Historical observational ECMO results

p13: Affronti successful weaning83.3% versus27.3%,P0.498. Tafer ECMO-free days22 versus9, D30 mortality24% versus56%,P<0.05; n80,37treated. Distelmaier n240,75%treated; weaningHR0.41,95%CI0.22–0.80,P0.008; printed lower30-day adjustedHR0.52,CI0.30–0.89,P0.016 and long-term survival adjustedHR0.64,CI0.42–0.98,P0.04. Baseline EuroSCORE P<0.001,SAPS3 P0.02,LVEF P0.04. Preserve historical label wording; no trial-result counterpart.

### QP1-035 — Design

pp15–16: multicenter phaseIII, randomized double-blind placebo-controlled superiority, two arms1:1. Consecutive eligible patients proposed for inclusion. Key: design/hypothesis and patient randomization.

### QP1-036 — Allocation

[p16](../../../joi250087supp1_prod_1766516490.96011.pdf#page=16): centralized24h CleanWeb service; minimization probability0.8 after first20 patients allocated by balanced randomization. Balance by center and primary etiology: acuteMI,myocarditis,post-heart-surgery,other causes. Key: allocation factors/minimization and corresponding analysis adjustment; post-arrest is not separately listed among allocation factors.

### QP1-037 — Weaning thresholds

[p19](../../../joi250087supp1_prod_1766516490.96011.pdf#page=19): daily trial when MBP>60mmHg on no/low vasopressors and pulsatile waveform≥24h. Reduce flow to66%,33%, then1–1.5L/min. Persistent MBP<60 stops trial and restores100%flow. Weanable: aorticVTI≥12cm,LVEF>20–25%,TDSa≥6cm/s at minimal flow. Same management in both groups. Key: primary endpoint decision rule.

### QP1-038 — Drug stopping and withdrawal

pp21–22: temporary suspension/permanent drug stop ordinarily retains enrollment; premature exit death,lost follow-up or consent withdrawal. Stop drug for anaphylaxis,VF,torsades,VT or MBP<45mmHg>60min despite two500mL crystalloid boluses AND norepinephrine≥4μg/kg/min OR epinephrine≥2μg/kg/min. Existing data usable unless objection/consent restriction; p22 permits pre-exit data. SAE monitoring30days after stop and until resolved. Key: population, intervention discontinuation and safety thresholds.

### QP1-039 — Monitoring/stopping

pp22,31,34: sponsor/ANSM may stop onDSMB recommendation for SUSARs or arm differences requiring benefit-risk reassessment, new product information or unmet enrollment. All deaths extracted monthly forDSMB/safety review; mortality imbalance or above expectation can trigger urgent measures. DSMB primarily monitors safety, may monitor efficacy especially when interim analyses exist; first meeting before enrollment. No numeric efficacy boundary, efficacy-interim schedule or alpha-spending rule specified here. Key: interim/stopping rules. Administrative notification15days after cancellation.

### QP1-040 — Flow denominator records

pp16,24: eligible non-enrolled registry/reasons; consent absence, physician refusal, team unavailable/missed, another trial. p36 records included/analysed numbers, exclusion reasons, deviations, inclusion curve andCONSORT flow. Key: flow and analysis denominators.

### QP1-041 — Dose-preparation table

[p25](../../../joi250087supp1_prod_1766516490.96011.pdf#page=25):2.5mg/mL (printed2,5),5mL vials,3vials/box,storage+2to+8°C. [p26](../../../joi250087supp1_prod_1766516490.96011.pdf#page=26) table: weight40–46kg,1flask,250mL glucose,8mL/h atH1–H2 and11mL/h atH3–H24;47–89kg,2flasks,500mL,16 and22mL/h;90–132kg,3flasks,1000mL,32 and44mL/h. No explicit dose-conversion formula printed. Key: delivered intervention dose/duration/units.

### QP1-042 — Common management targets

pp26–27: flow3.5–5L/min; PaO2 65–90mmHg or arterial saturation>90%; PaCO2 40–45mmHg; perfusionist at least every48h. aPTT55–70sec or antiXa0.4–0.6IU/mL; free hemoglobin every48h. Transfusion threshold9–10g/dL, possibly7–8 if stable without myocardial ischemia; platelet<20G/L or severe thrombopenia with bleeding. Key: common management/endpoint context, no observed trial estimates.

### QP1-043 — Concomitant treatment and efficacy period

pp26–27: other inotropes permitted, dobutamine preferred; open-label levosimendan prohibited throughout study; p27 also excludes digoxine among additional inotropes. Physician assures24h infusion compliance. Efficacy evaluation randomizationD1 throughD60. Key: intervention duration/contamination and follow-up.

### QP1-044 — Safety labels and thresholds

pp28–33: AE need not be causal, AR is causal; serious death/life-threat/hospitalization/prolongation/disability/congenital abnormality; unexpected against reference information. p29 severity mild/moderate/serious by daily-activity impact; WHO-UMC causality certain/probable/possible/unlikely. Table footnotes: all points reasonably complied with; drug intake or study procedures. p30 while onECMO only treatment-related deaths require immediate notification; VF/torsades/VT exempt from immediate notification onECMO, but notified immediately after weaning along with refractory hypotension(QP1-038). Natural-course deaths/ICU-relatedSAEs remain recorded. p31 drug effects include hypotension grades1/2,<30%MAP decrease; moderate tachycardiaHR<110bpm; hypokalemia3–3.5mmol/L; premature ventricular/atrial contractions,AF,nausea,vomiting,diarrhea,constipation,dizziness,headache,insomnia. Events monitored until resolution. Regulatory nonfatal SUSAR15days, additional reports8days, annualDSUR within60days of authorization anniversary. Key: safety ascertainment, with regulatory timing administrative.

### QP1-045 — Statistical overview

[p35](../../../joi250087supp1_prod_1766516490.96011.pdf#page=35): all comparisons two-sided typeI error5%. Descriptives overall/bygroup. Comparative analyses systematically unadjusted and adjusted for baseline prognostic factors potentially imbalanced, model appropriate to variable type/distribution. Qualitative n/%; quantitative n,mean,SD,95%CI mean,median,range,IQR. Censored KM/cumulative incidence and15/30/60day rates with95%CIs where appropriate. SAS/R latest version at analysis. Key: alpha/sidedness, adjustment and summary definitions; no named required prognostic covariate here.

### QP1-046 — Populations and missingness

[p36](../../../joi250087supp1_prod_1766516490.96011.pdf#page=36): ITT all randomized except consent withdrawal requesting no analysis. [p38](../../../joi250087supp1_prod_1766516490.96011.pdf#page=38): principal ITT original randomized group, all data regardless treatment changes. pp36,38 detailedSAP validated by scientific committee; modifications before database unblinding and committee validation. p39 codes missingCRF data and retains audit trail. No quantitative imputation algorithm or missingness assumption specified in assigned pages. Lost-follow-up censoring and retained early-exit data above; no replacementp37. Key: ITT denominator, consent exception, missing data andSAP timing.

### QP1-047 — Inferential models and sample-size inputs

[p37](../../../joi250087supp1_prod_1766516490.96011.pdf#page=37): primary cumulative incidence at15/30days with95%CIs. Fine–Gray group comparison/prognostic adjustment; subdistributionHR with95%CI. Schoenfeld residuals for proportional hazards; loglinearity of quantitative covariates studied. Cumulative incidence plotted nonparametrically or from model. Secondary qualitative χ², correctedχ² orFisher, logistic model for adjustment/exploratory; quantitative Student t-test (printed twice) or Mann–Whitney–Wilcoxon, linear regression adjustment. Mortality KM with95%CI only within60days, time from randomization to death regardless prior weaning, censor at latest news/end60days; logrank comparison andCox adjustment. Sample size: control successful-weaning cumulative incidence50% with competing death/weaning failure, based on30day cohort; target subdistributionHR1.75,alpha5%,power80%,101successful-weaning events,206subjects=103/arm. Latouche etal[38], p46 citation2004 StatMed23:3263–3274. No explicit formula or further censoring/competing-incidence inputs printed. No replacements; two-sided5% reiterated. No explicit multiplicity family/hierarchy, adjusted secondaryalpha, sensitivity specification or formal interim boundary in assigned original protocol. Outcomes listed as secondary, none explicitly key secondary. Keys: primary Fine–Gray/sHR, secondary model/test identity, power/sample size, alpha and multiplicity/interim rules.

## Closure and limitations

Every assigned protocol, administrative and bibliography page was opened. No LEVOECMO observed-result table/figure occurs here. Historical data remain historical. Applicable tables were summarypp7–10, consentp18, schedule/standard-carepp20–21, recruitmentp24, preparationp26 and causalityp29; all content relevant to result matching is mapped. No Office formulas/cached values, trial sensitivity result displays or result figures occur. The sole transcription uncertainty is administrative handwriting onp4, not a result-relevant quantity. Fresh native-text absence onpp4,49 was resolved by direct rendering and visual mapping; no scientific coverage gap remains.


# Support quantitative extraction: protocol shard 002

Agent: `/root/protocol_mapping_002`. Exact scope: DOC-002, `joi250087supp1_prod_1766516490.96011.pdf`, PDF pages 52–102 inclusive, 51 unique pages. Document role: PLAN throughout, including historical background quoted inside the protocol. Pages 52–93 are version 2.0 dated 31/05/2023, internal pages 5/46–46/46; pages 94–102 begin version 3.0 dated 26/06/2024, internal pages 1/46–9/46. All pages were opened and freshly mapped from the reusable, form-feed-delimited `.ai_paper_validation/review_1_5_1/preprocessing/DOC-002/layout_all_pages.txt`, using bounded `awk` page selection. Historical extraction engine: pdftotext/layout, exact legacy version unspecified. A later fresh coverage audit identified footer-only p.95 as a signed image page and directly rendered/visually mapped it; that page is fresh-required and now covered. Sources and reusable assets were not modified. Scope, contract, tooling, source and evidence inventories, source coverage, and coverage manifest informed the extraction; no earlier AI conclusions were read.

Links below are relative to this artifact. Direct PDF pages remain authority for later evidence confirmation. No workbook, CSV, or Office source belongs to this scope, so formulas versus cached workbook values are not applicable. Mathematical time definitions below are printed protocol specifications, not workbook formulas. No treatment-effect results of the LEVOECMO trial appear here; historic study values are explicitly separated. Relationship keys are local extraction keys for coordinator merging, not candidate IDs or global N/S IDs. Matching main-paper keys are semantic locators only; other agents own main-paper extraction.

## Complete page ledger

| PDF page | Internal page/version | Content inspected and quantitative applicability | Local relationships |
|---|---|---|---|
| [52](../../../joi250087supp1_prod_1766516490.96011.pdf#page=52) | 5/46, v2 | Summary: primary time to successful ECMO weaning within 30 days; pharmacologic action 7–9 days, single 24h infusion. | P2-01, P2-37 |
| [53](../../../joi250087supp1_prod_1766516490.96011.pdf#page=53) | 6/46, v2 | Success definition, 30-day post-removal confirmation, possible D60 confirmation; competing death/weaning failure; secondary endpoints and etiologic subgroups; adult refractory shock, VA-ECMO preceding 48h. | P2-02–P2-15 |
| [54](../../../joi250087supp1_prod_1766516490.96011.pdf#page=54) | 7/46, v2 | All 25 exclusions, consent continuation, infusion 24h/no bolus, 0.15→0.20 µg/kg/min after 2h; D1 measurements. | P2-16–P2-18 |
| [55](../../../joi250087supp1_prod_1766516490.96011.pdf#page=55) | 8/46, v2 | Daily D2–D30/death/ICU discharge; D30/D60 outcome status; 206/103 per arm, 14 centers, 24+12-month inclusion, 26+12 total, 2-month participation, 0.4/site/month; competing-risk model, DMC yes. | P2-19, P2-20, P2-30, P2-38 |
| [56](../../../joi250087supp1_prod_1766516490.96011.pdf#page=56) | 9/46, v2 | Historical survival/complication percentages; drug half-life, clearance, binding. Background, not prospective outcomes. | P2-37, P2-39 |
| [57](../../../joi250087supp1_prod_1766516490.96011.pdf#page=57) | 10/46, v2 | Historical SURVIVE, LeoPARDS, LICORN, LEVO-CTS, CHEETAH results/doses; equilibrium 4–8h, metabolite half-life about 3 days. | P2-37, P2-40–P2-44 |
| [58](../../../joi250087supp1_prod_1766516490.96011.pdf#page=58) | 11/46, v2 | Historical CHEETAH mortality; three retrospective cohorts; product names and section pointers. | P2-44–P2-47 |
| [59](../../../joi250087supp1_prod_1766516490.96011.pdf#page=59) | 12/46, v2 | Objectives: primary event/success/censoring/failure timing, full secondary endpoints/subgroups. Benefits/risks qualitative. | P2-01–P2-14 |
| [60](../../../joi250087supp1_prod_1766516490.96011.pdf#page=60) | 13/46, v2 | Detailed primary endpoint: event types/window/follow-up and protocolized weaning; secondary endpoints and four subgroups. | P2-01–P2-14 |
| [61](../../../joi250087supp1_prod_1766516490.96011.pdf#page=61) | 14/46, v2 | Phase III double-blind placebo superiority, two arms 1:1; minimization probability .8 after first20, center/etiology; 14 sites. IDs administrative. | P2-21, P2-22, P2-38 |
| [62](../../../joi250087supp1_prod_1766516490.96011.pdf#page=62) | 15/46, v2 | Blinding for participants, providers, outcome assessors; unblinding contacts. No additional numeric analysis rule. | P2-21; administrative contacts not applicable |
| [63](../../../joi250087supp1_prod_1766516490.96011.pdf#page=63) | 16/46, v2 | D1 consent/treatment within24h; 24h IV; CERNEVIT prohibited during infusion; baseline covariates, bilirubin >100 µmol/L or albumin <35 g/L defining hepatic insufficiency. | P2-17–P2-19, P2-23 |
| [64](../../../joi250087supp1_prod_1766516490.96011.pdf#page=64) | 17/46, v2 | Daily measurements and protocolized weaning thresholds/flow steps; ECMO binary parameters. | P2-19, P2-24 |
| [65](../../../joi250087supp1_prod_1766516490.96011.pdf#page=65) | 18/46, v2 | D30/D60 status/second ECMO; participation60d, infusion24h; chronology table D1/D2–30/D60 and D60 phone follow-up. | P2-19, P2-20, P2-38 |
| [66](../../../joi250087supp1_prod_1766516490.96011.pdf#page=66) | 19/46, v2 | Treatment suspension does not imply trial exit; exit reasons and data retention; discontinuation arrhythmia/hypotension threshold. | P2-25, P2-26 |
| [67](../../../joi250087supp1_prod_1766516490.96011.pdf#page=67) | 20/46, v2 | Retain prior data after withdrawal; SAE follow-up30d; sponsor/authority safety or recruitment cancellation, notice15d. | P2-25, P2-30 |
| [68](../../../joi250087supp1_prod_1766516490.96011.pdf#page=68) | 21/46, v2 | Inclusion48h/consent and exclusions1–21. | P2-15, P2-16 |
| [69](../../../joi250087supp1_prod_1766516490.96011.pdf#page=69) | 22/46, v2 | Exclusions22–25, emergency consent, recruitment table206/14/24+12/15,8/.4. | P2-16, P2-38 |
| [70](../../../joi250087supp1_prod_1766516490.96011.pdf#page=70) | 23/46, v2 | Pharmacokinetics; 2,5mg/mL×5mL vials,3 active/1 placebo per box; historic48h pharmacodynamics. | P2-27, P2-37 |
| [71](../../../joi250087supp1_prod_1766516490.96011.pdf#page=71) | 24/46, v2 | 24h no-bolus infusion .15→.20 after2h, complete weight/preparation/pump table; storage2–8°C. | P2-17, P2-27 |
| [72](../../../joi250087supp1_prod_1766516490.96011.pdf#page=72) | 25/46, v2 | No open-label levosimendan; common ECMO settings/anticoagulation/transfusion; CERNEVIT prohibited during infusion. | P2-18, P2-28 |
| [73](../../../joi250087supp1_prod_1766516490.96011.pdf#page=73) | 26/46, v2 | Compliance during24h; efficacy measurements D1–D60; steering committee roles. | P2-19; committee administrative context |
| [74](../../../joi250087supp1_prod_1766516490.96011.pdf#page=74) | 27/46, v2 | Safety outcome definitions (AE/reaction/SAE/unexpected/emerging); no numerical effect results. | P2-29 |
| [75](../../../joi250087supp1_prod_1766516490.96011.pdf#page=75) | 28/46, v2 | All serious/nonserious AEs eCRF; severity and WHO-UMC causality table dated17/04/2012. | P2-29 |
| [76](../../../joi250087supp1_prod_1766516490.96011.pdf#page=76) | 29/46, v2 | SAE notifications and post-weaning arrhythmia/hypotension thresholds; historical mortality40–60%; quarterly extraction. | P2-26, P2-29, P2-30, P2-48 |
| [77](../../../joi250087supp1_prod_1766516490.96011.pdf#page=77) | 30/46, v2 | Historical58% mortality; data extraction/imbalance monitoring; hypotension grades1–2 <30%, HR<110, potassium3–3.5mmol/L. | P2-29, P2-30, P2-48 |
| [78](../../../joi250087supp1_prod_1766516490.96011.pdf#page=78) | 31/46, v2 | SAE notification from treatment through60d, indefinite if related; follow until resolved. | P2-29 |
| [79](../../../joi250087supp1_prod_1766516490.96011.pdf#page=79) | 32/46, v2 | Sponsor safety classification; SUSAR notification15d and follow-up8d, safety-driven changes. No inferential efficacy rule. | P2-29, P2-30 |
| [80](../../../joi250087supp1_prod_1766516490.96011.pdf#page=80) | 33/46, v2 | Annual safety report within60d of anniversary; DSMB before first enrollment; source-data field none. | P2-30 |
| [81](../../../joi250087supp1_prod_1766516490.96011.pdf#page=81) | 34/46, v2 | Data management/storage; statistical two-sided5%; descriptions overall/by group; comparisons unadjusted. | P2-31, P2-32 |
| [82](../../../joi250087supp1_prod_1766516490.96011.pdf#page=82) | 35/46, v2 | Adjustments/prognostic factors; descriptions/CI; analysis plan before unblinding; ITT consent exception; primary follow-up classification. | P2-25, P2-31–P2-34 |
| [83](../../../joi250087supp1_prod_1766516490.96011.pdf#page=83) | 36/46, v2 | Primary time definitions, CIF15/30d, Fine–Gray/SHR95%CI, assumptions; secondary tests/regressions and mortality60d. | P2-02, P2-31–P2-35 |
| [84](../../../joi250087supp1_prod_1766516490.96011.pdf#page=84) | 37/46, v2 | Logrank/Cox; sample-size50%,HR1.75,alpha5%,power80%,101events,206/103; no replacement; ITT and plan changes. | P2-25, P2-31, P2-33, P2-35, P2-36 |
| [85](../../../joi250087supp1_prod_1766516490.96011.pdf#page=85) | 38/46, v2 | Monitoring high-level; missing data must be coded; eCRF validation/audit trail. No imputation specification. | P2-34 |
| [86](../../../joi250087supp1_prod_1766516490.96011.pdf#page=86) | 39/46, v2 | Audits, investigator commitments, emergency consent. No additional result-relevant quantitative relationship. | Administrative, not applicable |
| [87](../../../joi250087supp1_prod_1766516490.96011.pdf#page=87) | 40/46, v2 | Nonrandomization reasons, concomitant-trial exception IMPULMACS NCT04951999; sponsor halt discretion. | P2-16, P2-30 |
| [88](../../../joi250087supp1_prod_1766516490.96011.pdf#page=88) | 41/46, v2 | Substantial amendment approvals, final report1year, archive15years. No endpoint/model/sample-size amendment specified here. | Administrative, not applicable |
| [89](../../../joi250087supp1_prod_1766516490.96011.pdf#page=89) | 42/46, v2 | PHRC2017 funding, insurance/publication/registration placeholder. | Administrative, not applicable |
| [90](../../../joi250087supp1_prod_1766516490.96011.pdf#page=90) | 43/46, v2 | Bibliography1–16 only; numerical bibliographic metadata not LEVOECMO results. | Bibliography, not applicable |
| [91](../../../joi250087supp1_prod_1766516490.96011.pdf#page=91) | 44/46, v2 | Bibliography17–30 only. | Bibliography, not applicable |
| [92](../../../joi250087supp1_prod_1766516490.96011.pdf#page=92) | 45/46, v2 | Bibliography31–38; Latouche2004 sample-size citation, no formula printed. | P2-36 locator; bibliography otherwise not applicable |
| [93](../../../joi250087supp1_prod_1766516490.96011.pdf#page=93) | 46/46, v2 | Addenda listed SOFA/GLASGOW/SAPS2, product references; no attached numeric scales in this page. | P2-29 locator; list otherwise not applicable |
| [94](../../../joi250087supp1_prod_1766516490.96011.pdf#page=94) | 1/46, v3 | Version3.0 26/06/2024; project P170914J/EUDRACT2019-004319-29, administrative contacts. | P2-49 |
| [95](../../../joi250087supp1_prod_1766516490.96011.pdf#page=95) | 2/46, v3 | Scanned signed v3.0 protocol page: v3.0 26/06/2024; investigator 28/06/2024 (handwriting), sponsor02/07/2024, CPP OuestIII04/01/2021 and ANSM30/11/2020. Direct CPU render/visual audit completed. | Administrative; no statistical result relationship |
| [96](../../../joi250087supp1_prod_1766516490.96011.pdf#page=96) | 3/46, v3 | Contents section1–11 pointers, no underlying numeric evidence. | Not applicable |
| [97](../../../joi250087supp1_prod_1766516490.96011.pdf#page=97) | 4/46, v3 | Contents section11–18 pointers, no underlying numeric evidence. | Not applicable |
| [98](../../../joi250087supp1_prod_1766516490.96011.pdf#page=98) | 5/46, v3 | Summary primary30d, drug action7–9d/single24h. | P2-01, P2-37, P2-49 |
| [99](../../../joi250087supp1_prod_1766516490.96011.pdf#page=99) | 6/46, v3 | Success/competing risks and full secondary endpoints/subgroups; eligibility48h. | P2-02–P2-15, P2-49 |
| [100](../../../joi250087supp1_prod_1766516490.96011.pdf#page=100) | 7/46, v3 | All25 exclusions, dosing24h/no bolus/.15→.20 after2h; D1 collection. | P2-16–P2-19, P2-49 |
| [101](../../../joi250087supp1_prod_1766516490.96011.pdf#page=101) | 8/46, v3 | Daily data, D30/D60;206/103,14centers,36+3inclusion/38+3total months,2months participation,.4/site/month, DMC. | P2-19, P2-20, P2-30, P2-38, P2-49 |
| [102](../../../joi250087supp1_prod_1766516490.96011.pdf#page=102) | 9/46, v3 | Historical survival/complication and pharmacokinetic values repeated; not trial results. | P2-37, P2-39, P2-49 |

## Prospective result-relevant relationships and main-paper matching keys

Each relationship records exact printed content without diagnostic assessment. Page references in the ledger above locate every occurrence.

| Key | Pages | Planned relationship / definition | Matching main-paper key |
|---|---|---|---|
| P2-01 | 52,59,60,82;98 | Primary endpoint time to successful ECMO weaning within30 days after randomization; benefit direction faster/more successful weaning. | Primary outcome/Methods; time-to-successful-weaning result |
| P2-02 | 53,59,60,82–83;99 | Success requires alive without repeat ECMO, other mechanical circulatory support or heart transplant30 days after removal. Eligible removal D0–30; confirmation can run to D60 for removal D30. Death before removal and unsuccessful weaning are competing events. Failed attempt assigned its removal date, not later failure date. At D30 still on ECMO is censored; no post-D30 event considered. | Primary endpoint definition, cumulative incidence and competing-event classification |
| P2-03 | 53,59,60;99 | Secondary mortality D30 and D60. | Secondary mortality results |
| P2-04 | 53,59,60;99 | Secondary total ECMO duration inclusion–D30 and inclusion–D60; ECMO-free days in both windows. | ECMO duration/free-days outcomes |
| P2-05 | 53,59,60;99 | Secondary ICU stay duration and hospital stay duration. | Length-of-stay results |
| P2-06 | 53,59,60;99 | Secondary major adverse cardiovascular event composite at D30/D60: death, cardiac transplant, escalation to permanent LV assist device, stroke, dialysis, rehospitalization for heart failure. | MACE definition/status/results |
| P2-07 | 53,59,60;99 | Secondary time to hemodynamic improvement (systolic,diastolic,mean blood pressure,heart rate) and stabilization. | Hemodynamic outcomes/status |
| P2-08 | 53,59,60;99 | Secondary organ-failure days by SOFA and days alive without organ failure inclusion–D30; p59 says number of days without organ failure, whereas detailed endpoint and summaries include alive. | Organ failure/SOFA endpoint |
| P2-09 | 53,59,60;99 | Secondary catecholamine support duration and days alive without support inclusion–D30. | Catecholamine outcomes |
| P2-10 | 53,59,60;99 | Secondary ventilation duration and days alive without ventilation inclusion–D30 and D60. | Ventilation outcomes |
| P2-11 | 53,59,60;99 | Secondary LV function by echocardiography at D30 after randomization. | Echocardiographic outcome/status |
| P2-12 | 53,59,60;99 | Secondary incidence of drug adverse reactions: atrial fibrillation/other supraventricular arrhythmias, ventricular arrhythmias including tachycardia/fibrillation/torsades, hypokalemia. | Adverse events/Safety |
| P2-13 | 53,59,60;99 | Primary and secondary endpoints assessed in predefined subgroups acute MI, myocarditis, post-cardiac surgery, post-cardiac arrest. | Prespecified subgroup definitions and tests |
| P2-14 | 53,59,60;99 | Endpoint statuses are primary and secondary as above; no explicit key-secondary designation, tertiary hierarchy or multiplicity procedure printed in these pages. | Outcome hierarchy and reporting status |
| P2-15 | 53,68;99 | Target adults with refractory acute cardiogenic shock on VA-ECMO and likely LV recovery; ECMO initiated preceding48h. Surrogate consent or emergency enrollment then continuation consent. | Participants/Eligibility |
| P2-16 | 54,68–69;100 | Exclude age<18; pregnancy/lactation; ECMO>48h; cumulative resuscitation>30min in48h before ECMO (earlier low-flow requires consciousness recovered); irreversible neurology; irreversible end-stage cardiomyopathy; MI mechanical complication; aortic regurgitation>II; pulmonary embolism; cardiotoxic intoxication; prior LVAD or transplant; moribund/SAPSII>90; ChildB/C/severe hepatic insufficiency; chronic dialysis; levosimendan hypersensitivity; torsades previous30d; epilepsy; legal incompetence; other interventional trial; weight>180kg; CERNEVIT hypersensitivity; hypervitaminosis; severe hypercalcemia/hypercalciuria; vitaminA/retinoids. p87 exception for concomitant IMPULMACS NCT04951999. | Eligibility/analysis population description |
| P2-17 | 54,63,71;100 | Randomized IV levosimendan24h, no bolus;0.15µg/kg/min first2h,0.20µg/kg/min thereafter if no rate-limiting side effects. Start as soon as possible and ≤24h after randomization. Placebo same route/procedures/duration, yellow CERNEVIT. | Randomized intervention dose/timing |
| P2-18 | 63,72 | Open-label levosimendan prohibited entire trial; CERNEVIT prohibited only during experimental infusion. Additional inotropes permitted (p72 except digoxine), dobutamine preferred; standard heart-failure/ECMO management both arms. | Concomitant therapy/crossover |
| P2-19 | 54–55,63–65,73;100–101 | Baseline D1: comorbidities, potassium/lactate/blood gases/WBC/platelets/renal/hepatic markers, echocardiography (LV/LVEF, LVOT VTI, lateral-mitral tissue-Doppler systolic velocity), SOFA,catecholamines,AE/SAE. Daily D1–30/death/ICU discharge: hemodynamics,catecholamines,ventilation,RRT,urine,labs,SOFA,ECG,echo,weanability,ECMO parameters until removal. Efficacy assessment through D60. | Longitudinal collection/time windows |
| P2-20 | 55,65;101 | D30,D60: vital status/death date and hour,ECMO,repeat ECMO after removal,other mechanical support,transplant,ventilation,ICU/hospital status and discharge dates. Table on65: information/consent/randomization/history/dispensing D1 only; clinical/procedures D1 and daily period; AEs/vital/ECMO D1,daily,D60; pursuit consent daily/D60 if needed; telephone D60. | Follow-up and endpoint ascertainment |
| P2-21 | 61–62 | PhaseIII,multicenter,randomized,double-blind,placebo-controlled superiority,2 arms,1:1; concealed web allocation, patients/providers/assessors blinded; preparation off-protocol nurse. | Trial design/randomization/blinding |
| P2-22 | 61 | First20 assigned balanced random; thereafter stochastic minimization probability0.8; factors center and shock primary etiology acuteMI,myocarditis,post-heart surgery,other causes; continuous24h central service. | Randomization factors/model adjustment |
| P2-23 | 63 | Baseline hepatic insufficiency: bilirubin>100µmol/L or albumin<35g/L with no alternative cause; comorbidity indices McCabe/Jackson,Charlson,SAPSII,SOFA; recorded ejection fraction/NYHA etc. | Baseline/prognostic variables |
| P2-24 | 64 | Daily weaning once MBP>60mmHg,no/low-dose vasopressors,pulsatile waveform≥24h. Flow66%,33%,then1–1.5L/min; if persistent MBP<60 restore100% and stop. Weanable at minimal support if aorticVTI≥12cm,LVEF>20–25%,TDSa≥6cm/s. | Weaning algorithm underlying primary event |
| P2-25 | 66–67,82,84 | Temporary/permanent infusion cessation does not automatically end participation; exits death,loss,consent withdrawal; retain collected data unless objection. ITT all randomized except consent withdrawal plus requested nonanalysis (82); principal ITT original group regardless treatment changes/all data (84). No replacement for early exits. | Analysis population and withdrawal handling |
| P2-26 | 66,76 | Discontinue drug for anaphylactic shock,ventricular fibrillation,torsades,ventricular tachycardia,refractory hypotension. Hypotension MAP<45mmHg>60min despite2×500mL crystalloid AND norepinephrine≥4µg/kg/min OR epinephrine≥2µg/kg/min. | Treatment stopping/safety definition |
| P2-27 | 70–71 | Active concentration2,5mg/mL,vial5mL,boxes3vials; placebo5mL powder,boxes1vial. Preparation table below; products2–8°C/light protected. | Actual intervention preparation/delivery |
| P2-28 | 72 | Common care pump3.5–5L/min,PaO2 65–90mmHg and/or saturation>90%,PaCO2 40–45mmHg; perfusionist/plasma-freeHb every48h; heparin aPTT55–70s or antiXa.4–.6IU/mL; Hb transfusion9–10g/dL (7–8 stabilized/no ischemia),platelets<20G/L or bleeding. | Common care context, not efficacy test |
| P2-29 | 74–79,93 | All AEs recorded; serious means death/life-threatening/hospitalization/prolongation/disability/congenital outcome. Causal categories certain,probable/likely,possible,unlikely via WHO-UMC table; all criteria reasonably met; drug timing or study procedure timing. Serious postwean VT HR≥110bpm,grade3–4/refractory hypotension notified immediately; grades1–2/<30%MAP fall,HR<110bpm,K3–3.5mmol/L recorded without immediate notice. RelatedSAE surveillance treatment initiation–D60 and indefinitely if related,follow until resolved. | Safety endpoint ascertainment/classification |
| P2-30 | 55,67,76–80,87;101 | DSMB yes,independent ECMO/shock experts plus statistician,meeting before first enrollment; mission safety,possible efficacy especially if interim analyses. Quarterly all-death/SAE extracts and group imbalance surveillance; sponsor/authority can stop for SUSAR/imbalance,new information/futility of objectives,recruitment targets not met,or medical/administrative reasons. No numeric efficacy interim boundary,alpha spending,planned interim sample size,or multiplicity adjustment supplied in this shard. | Monitoring/interim/stopping rules |
| P2-31 | 81–84 | All comparisons two-sided typeI5%; unadjusted AND adjusted for baseline prognostic factors potentially unbalanced despite randomization; appropriate model chosen by variable type/distribution. | Significance/adjustment rules |
| P2-32 | 81–83 | Overall/by-group descriptions: qualitative n/%; quantitative n,mean,SD,95%CI of mean,median,range,IQR. Censored KM or CIF,rates15/30/60d if appropriate,95%CI. SAS or R latest version at analysis. | Descriptive measures and software |
| P2-33 | 82,84 | Detailed SAP scientific-committee approval; subsequent changes before database unblinding and committee approval. | Prespecification/amendment chronology |
| P2-34 | 82–83,85 | Five primary follow-up types: onECMO D30 censored; death without removal competing; success event; failed removal competing; lost follow-up censored at last news. All other subjects censored30d. Missing values must be coded(85); no imputation or explicit missing secondary-data strategy printed here. | Missing data/censoring/primary event coding |
| P2-35 | 83–84 | Primary CIF15/30d95%CI; Fine–Gray comparison and prognostic adjustment; SHR95%CI; Schoenfeld residual PH check and quantitative-covariate loglinearity; CIF nonparametric or modeled. Secondary qualitative χ²/correctedχ²/Fisher,logistic for prognosis/exploration; quantitative Studentt (printed twice) or Mann–Whitney–Wilcoxon,adjusted linear regression. Mortality only60d KM95%CI,logrank,Cox adjustment. Time definitions below. | Primary statistical analysis; secondary models/tests |
| P2-36 | 84,92 | Sample size: control30d successful-weaning CIF50% with death/failure competing; SHR1.75;alpha5%;power80%;101successful-weaning events;206total/103per group. Citation Latouche/Porcher/Chevret2004; explicit sample-size formula not printed. | Sample-size/power assumptions |
| P2-37 | 52,56–57,70;98,102 | Background pharmacology: action7–9d,single24h infusion; biological half-life60min,clearance300mL/min,binding97%,equilibrium4–8h,active metabolite half-life~3d. On70 historical prolonged infusion up to48h and 24h vs48h dobutamine comparison. | Historical rationale, not reported LEVOECMO result |
| P2-38 | 55,61,65,69;101 | v2 administrative recruitment206,103/arm,14centers,24+12months enrollment,26+12total,60d/2months follow-up,0.4/site/month; recruitment table also15,8subjects/site. v3 summary enrollment36+3,total38+3months,other figures unchanged. | Enrollment context;206 also sample-size key |

### Full preparation table (P2-27, PDF page71)

| Weight | Number of flasks | Glucose volume | Pump H1–H2 mL/h | Pump H3–H24 mL/h |
|---|---:|---:|---:|---:|
| 40–46kg | 1 | 250mL | 8 | 11 |
| 47–89kg | 2 | 500mL | 16 | 22 |
| 90–132kg | 3 | 1000mL | 32 | 44 |
| 133–180kg | 4 | 1000mL | 32 | 44 |

No arithmetic dose reconstruction was substituted for the printed regimen. Weight bands, vial quantities, infusion hours and pump units are retained as distinct supplied quantities.

### Printed time formulas (P2-34/P2-35, PDF page83)

- Successful-weaning time = difference between randomization date and weaning date.
- Unsuccessful-weaning time = difference between randomization date and ECMO removal date for patients dying, needing repeat ECMO, other mechanical support or transplant within30d after removal.
- Death without weaning time = difference between randomization date and death date.
- Loss-to-follow-up time = difference between randomization date and latest-news date.
- Other primary follow-up =30d, censored.
- Mortality survival time = difference between randomization date and death date regardless previous removal, or last-news date, or follow-up end60d.

## Historical numerical relationships explicitly distinguished from prospective trial data

| Key | Pages | Printed historical relationship; comparator/direction retained | Relevance |
|---|---|---|---|
| P2-39 | 56;102 | Long-term survival70–80% myocarditis/cardiotoxic poisoning,40–50%MI,15–25% refractory arrest. ECMO complications local hemorrhage10–20%,infection/bacteremia10–15%,limb ischemia5–10%,stroke5%. | Background; not LEVOECMO event counts or sample assumptions |
| P2-40 | 57 | SURVIVE n1327;12µg/kg loading then.1–.2µg/kg/min23h; BNP difference first5d;180d mortality26%levosimendan/28%dobutamine,HR.91[.74–1.13],P.40. | Cited historic RCT |
| P2-41 | 57 | LeoPARDS .1→.2µg/kg/min20–22h;mean±SD SOFA6.68±3.96vs6.06±3.89,P.053;28d mortality34.5%vs30.9%,P.43. | Cited historic RCT |
| P2-42 | 57 | LICORN n336;LEVO-CTS n882; .1µg/kg/min24h after anesthetic induction. LICORN composite prolonged catecholamines,LV mechanical device,RRT;LEVO-CTS death,RRT,perioperativeMI,mechanical cardiac assist. No group difference stated. LEVO-CTS22%developed low-output;about half in each trial needed catecholamines>24h. | Cited historical RCT definitions |
| P2-43 | 57 | CHEETAH selection preopLVEF<25% with IABP/high-dose inotrope;dose.025–.2µg/kg/min,no bolus,≤48h/ICU discharge;stopped for futility after506. | Historical stopping/dose, not LEVOECMO rule |
| P2-44 | 58 | CHEETAH30d deaths32[12.9%]vs33[12.8%];absoluteRD.1percentage points,95%CI−5.7to5.9,P.97;mean dose.07µg/kg/min. | Cited historical trial result |
| P2-45 | 58 | Affronti before/after VA-ECMO successful weaning83.3%levosimendan vs27.3%historical controls,P=.498 as printed. | Historical quotation, not planned comparison |
| P2-46 | 58 | Tafer cohort80,37treated;ECMO-free days22vs9;30d mortality24%vs56%,P<.05. | Historical cohort |
| P2-47 | 58 | Distelmaier240postcardiovascular-surgery patients,75%levosimendan;successful weaning HR.41,95%CI.22–.80,P.008;30d adjustedHR.52[.30–.89],P.016;long-term adjustedHR.64[.42–.98],P.04. Narrative prints lower30d and long-term survival. Baseline EuroSCORE P<.001,SAPS3P.02,LVEFP.04. | Historical cohort; labels retained verbatim in meaning |
| P2-48 | 76–77 | Historical VA-ECMO mortality40–60%(76),58%(77); used as context for safety notification policies, not LEVOECMO observed mortality. | Background to safety ascertainment |
| P2-49 | 94–102 | Version3.0 dated26/06/2024;projectP170914J/EUDRACT2019-004319-29. Summary duplicates planned primary/secondary definition,dosing,eligibility and sample206/103;administrative calendar36+3and38+3months. Version2.0 dated31/05/2023 on52–93. | Plan version/main Methods protocol-version matching |

## Coverage status and limitations

COMPLETE:51/51 assigned pages mapped;49 local relationship records (38 prospective/design/context keys,10 historical-only keys P2-39–P2-48,one version key P2-49), one complete dose-preparation table, all endpoint lists, chronology table, safety-causality table content, and printed time definitions mapped. All administrative and bibliography pages were opened; pages with no additional result-relevant numeric content include (86,88–91,93–97;92 is only a sample-size citation locator and93 only a scale-list locator). Historical and operational quantities remain available without being treated as reported trial outcomes.

Scientific coverage gaps:None within assigned scope. Derivative limitation:legacy engine/version provenance incomplete; native/layout text is a locator rather than final source authority. Page95 has only a footer in reusable text but substantive signed image content; the later coverage audit directly rendered and mapped it as a fresh-required unit; no assumption was made that an empty fresh-required page was blank. No primary-analysis fixed covariate list, explicit secondary missing-data imputation, subgroup interaction model, multiplicity correction, or numerical efficacy interim boundary was specified on the assigned pages; these are extraction limitations only and require matching against the separately assigned SAP and other protocol pages. No candidate diagnosis or finding count is supplied.

### Safety classification table and footnotes (P2-29, PDF page 75)

| WHO-UMC category | Printed criteria retained |
|---|---|
| Certain | Event/laboratory abnormality with plausible drug timing; cannot be explained by disease/other drugs; plausible pharmacologic/pathologic withdrawal response; definitive objective/specific disorder or recognized pharmacologic phenomenon; satisfactory rechallenge if necessary. |
| Probable / Likely | Reasonable drug timing; unlikely attributable to disease/other drugs; clinically reasonable withdrawal response; rechallenge not required. |
| Possible | Reasonable drug timing; may also be explained by disease/other drugs; withdrawal information may be lacking or unclear. |
| Unlikely | Drug timing makes relationship improbable but not impossible; disease/other drugs provide plausible explanation. |

Footnotes: all points should be reasonably complied with; timing can concern study procedures as well as drug intake. General AE severity categories: mild tolerated/no interference with daily activities, moderate sufficiently uncomfortable to affect daily activities, serious preventing daily activities; an attached severity scale is an alternative. A causal reaction requires a relationship with the trial or investigational product; an AE need not be causally related. Unexpected nature/severity/frequency/outcome is assessed against the reference safety information. Safety administrative notification intervals on pages 67 and 79–80 are 15 days for trial-cancellation notice, 15 days for nonfatal/non-life-threatening SUSAR initial notification, 8 calendar days for follow-up after receipt, 8 days for emerging-safety follow-up after awareness, annual DSUR within 60 days of authorization anniversary; these are operational deadlines rather than statistical stopping thresholds.


# DOC-002 protocol mapping part 003

Scope: only PDF pages 103–153 inclusive of `joi250087supp1_prod_1766516490.96011.pdf`; 51 unique PDF_PAGE units, all mapped. Runtime canonical ID: `/root/protocol_mapping_003`. Role: PLAN throughout, including the change-summary tables. These are prospective specifications and historical rationale, not current trial results. No candidates are diagnosed here. No other source units were read for scientific mapping.

Read controls: QUALITY_CONTROL_SCOPE.md; workflow_1_6_2/review_contract.md; tooling_record.md; source_inventory.md; evidence_asset_inventory.md; source_coverage.md; coverage_manifest.md. Reused transcription: `.ai_paper_validation/review_1_5_1/preprocessing/DOC-002/layout_all_pages.txt`, restricted with awk form-feed records 103–153. Historical native/layout engine version unspecified by reusable metadata. All assigned records contain substantive text; no fresh-required units in this shard. Fresh reasoning covered every page, including administration and bibliography.

Fresh derivatives for tracked-change interpretation: `preprocessing/protocol_003/page-149.png` and `preprocessing/protocol_003/page-153.png`, generated by the recorded fallback interpreter running `workflow_1_6_2/scripts/pdf_tools.py render`, PyMuPDF 1.26.4, 200 dpi, CPU. Both were visually inspected. No OCR was necessary. All sources and reused assets preserved. This shard contains no workbook, formula cells, cached workbook values, CSV, DOC, or DOCX.

Evidence links below resolve from this part file to the supplied PDF, always using physical PDF page numbers. Printed internal page numbers differ: PDF103–139 are protocol version3.0 internal pages10–46. The repeated footer identifies version3.0 dated26/06/2024; template footer date April2018 is distinct from protocol version identity. PDF140–151 compare versions1.1 and2.0; PDF152–153 compare versions2.0 and3.0.

## Complete page ledger

| PDF page | Content opened and mapped | Relationship keys or applicability |
|---:|---|---|
| 103 | Pharmacology and historical SURVIVE, LeoPARDS, LICORN, LEVO-CTS, CHEETAH trials | PR3-001, PR3-002; historical, not LEVOECMO results |
| 104 | CHEETAH continuation; ECMO cohort rationale; product pointers | PR3-003, PR3-004; historical, not LEVOECMO results |
| 105 | Primary and secondary objectives | PR3-005–017 |
| 106 | Primary and secondary endpoint definitions | PR3-005–017 |
| 107 | Superiority, allocation, minimization, site count | PR3-018, PR3-019 |
| 108 | Masking and unblinding | PR3-020; contacts not applicable to quantitative results |
| 109 | Baseline visit, treatment timing, covariate measurements | PR3-021, PR3-022 |
| 110 | Daily follow-up, protocolized ECMO weaning criteria | PR3-023, PR3-024 |
| 111 | D30/D60 ascertainment and chronology table | PR3-025, PR3-026 |
| 112 | Treatment termination and study exit definitions | PR3-027, PR3-028 |
| 113 | Consent withdrawal, safety follow-up, cancellation | PR3-028, PR3-029 |
| 114 | Inclusion and exclusion criteria | PR3-030 |
| 115 | Remaining exclusions, consent, recruitment table | PR3-030, PR3-031 |
| 116 | Product pharmacology and vial packaging | PR3-032 |
| 117 | Infusion and weight-based preparation table | PR3-033, PR3-034 |
| 118 | Other agents, ECMO targets and prohibited treatments | PR3-035, PR3-036 |
| 119 | Compliance, efficacy measurement window, steering committee | PR3-037; committee administration opened |
| 120 | Adverse-event and seriousness definitions | PR3-038 |
| 121 | Severity/causality classification table and reporting responsibilities | PR3-038; no numerical trial outcomes |
| 122 | Immediate safety reporting under/after ECMO and thresholds | PR3-039 |
| 123 | Non-immediate safety categories, mortality monitoring | PR3-039, PR3-040 |
| 124 | Safety reporting window and sponsor roles | PR3-041; administrative reporting details opened |
| 125 | SUSAR reporting and emerging safety issues | PR3-041; administrative deadlines opened |
| 126 | Annual safety reports, DSMB, data management | PR3-042; no numerical efficacy interim boundary |
| 127 | Data access/ownership and overall alpha | PR3-043, PR3-044 |
| 128 | Descriptions, ITT, outcome status list, software and SAP governance | PR3-044–047 |
| 129 | Event-time formulas, Fine–Gray model, assumptions and secondary methods | PR3-046–050 |
| 130 | Survival comparison, sample size, significance, ITT | PR3-050–052 |
| 131 | Monitoring and CRF missing-value coding | PR3-053; no statistical imputation specified here |
| 132 | Audit and ethics/consent | Administrative opened; no new quantitative statistical specification |
| 133 | Consent, co-enrolment exception, compensation, authorizations | PR3-030, PR3-054; remaining material administrative |
| 134 | Amendment approvals, final reporting, archives | Administrative opened; final summary within1year, archives15years; no efficacy-result relationship |
| 135 | Funding, insurance, publication and registration template | Administrative opened; PHRC2017, registration placeholder NCTXXXXX; no trial-result relationship |
| 136 | Bibliography1–16 | Opened; no new LEVOECMO outcome/statistical specification; citation12 title mentions historical1,866 adults |
| 137 | Bibliography17–30 | Opened; historical literature only; no new LEVOECMO relationship |
| 138 | Bibliography31–38 | PR3-051 provenance: Latouche2004; other citations do not supply current results |
| 139 | Addenda list and version policy | PR3-055; listed scales/product labels are pointers, not supplied numerical scale tables on this page |
| 140 | Change-summary cover versions1.1/2.0 | PR3-056 |
| 141 | Version headers, exclusions, placebo amendment | PR3-056–058 |
| 142 | Sites, duration, blinding, treatment timing amendment | PR3-058, PR3-059 |
| 143 | Participation chronology, full exclusions amendment | PR3-057, PR3-059 |
| 144 | Recruitment and product packaging amendment | PR3-058, PR3-059 |
| 145 | Infusion rate/packaging amendments | PR3-058, PR3-060 |
| 146 | Preparation-table new weight band, concomitant agents and safety reporting | PR3-060, PR3-061 |
| 147 | Immediate/non-immediate safety reporting amendments | PR3-061 |
| 148 | Safety reporting replacement text and thresholds | PR3-061 |
| 149 | Continued safety table including deleted paragraphs | PR3-061; fresh image separates retained from struck text |
| 150 | Safety-window and consent amendments | PR3-061; consent administration opened |
| 151 | Co-enrolment and Cernevit SmPC addendum | PR3-054, PR3-058 |
| 152 | Change-summary cover versions2.0/3.0 | PR3-062 |
| 153 | Version3.0 duration amendment table | PR3-062; fresh image confirms replacement values |

## Quantitative and statistical relationships

Main-paper match keys are semantic locators for the coordinator to pair with the main map; they do not assert that the report contains a matching result. IDs PR3-001–062 are shard-local inventory keys, not candidate or global N/S identifiers. Related occurrences are listed together without deciding consistency.

| Key | Exact evidence | Extracted relationship and printed quantities | Main-paper matching key |
|---|---|---|---|
| PR3-001 | PDF103 | Historical SURVIVE: n=1,327; loading 12 μg/kg, then 0.1 up to 0.2 μg/kg/min for 23 h. BNP first 5 days; 180-day mortality 26% vs 28%, HR 0.91 [0.74–1.13], p=.40. Historical LeoPARDS: 0.1 increased to 0.2 μg/kg/min for 20–22 h; ICU SOFA mean±SD 6.68±3.96 vs 6.06±3.89, P=.053; D28 mortality 34.5% vs 30.9%, P=.43. Metabolite OR-1986 half-life about 3 days. | Historical rationale only |
| PR3-002 | PDF103 | Historical LICORN n=336 and LEVO-CTS n=882: prophylactic 0.1 μg/kg/min for 24 h. LICORN composite: prolonged catecholamine infusion, LV mechanical assist device, RRT. LEVO-CTS composite: death, RRT, perioperative MI, mechanical cardiac assist device. LEVO-CTS 22% developed low cardiac output syndrome; approximately half needed catecholamines >24 h in both studies. CHEETAH: preoperative LVEF <25%, 0.025–0.2 μg/kg/min without bolus up to 48 h or ICU discharge, stopped for futility after 506 patients. | Historical rationale only |
| PR3-003 | PDF104 | Historical CHEETAH: D30 deaths 32 [12.9%] vs 33 [12.8%], absolute risk difference 0.1 percentage points, 95% CI −5.7 to 5.9, P=.97; mean dose 0.07 μg/kg/min. | Historical rationale only |
| PR3-004 | PDF104 | Historical Affronti weaning 83.3% vs 27.3%, p=.498. Tafer: cohort 80, 37 treated, ECMO-free days 22 vs 9, D30 mortality 24% vs 56%, p<.05. Distelmaier: 240 patients, 75% treated, successful weaning HR 0.41, 95% CI 0.22–0.80, P=.008; lower 30-day adjusted HR 0.52, 95% CI 0.30–0.89, P=.016, and long-term survival adjusted HR 0.64, 95% CI 0.42–0.98, P=.04, as printed. Baseline EuroSCORE P<.001, SAPS-3 P=.02, LVEF p=.04. | Historical rationale only |
| PR3-005 | PDF105–106 | Primary endpoint: time to successful ECMO weaning within 30 days after randomization. Successful requires survival without ECMO, other mechanical circulatory device, or heart transplant 30 days after ECMO removal. | Primary outcome definition/window |
| PR3-006 | PDF105–106 | Unsuccessful weaning is competing event at the weaning attempt; death within 30 days without an attempt also competes. Still on ECMO/no defined event: censor D30. Weaning D30 requires follow-up through D60 to qualify. No event after D30 enters event-time window. | Competing events/censoring |
| PR3-007 | PDF106 | Days alive without ECMO explicitly not primary: high proportion dying on ECMO creates ties at 0 days. Analysis models successful weaning with death/weaning failure competing. | Primary endpoint status |
| PR3-008 | PDF105–106 | Secondary mortality D30 and D60. | Mortality |
| PR3-009 | PDF105–106 | Secondary ECMO duration inclusion–D30 and inclusion–D60; ECMO-free days over both windows. | ECMO duration/free days |
| PR3-010 | PDF105–106 | Secondary ICU stay and hospitalization duration. | Stay duration |
| PR3-011 | PDF105–106 | Secondary MACE on D30/D60: death, cardiac transplant, escalation to permanent LVAD, stroke, dialysis, rehospitalization for heart failure. | MACE status/components |
| PR3-012 | PDF105–106 | Secondary time to improvement in systolic, diastolic and mean BP and heart rate; time to hemodynamic stabilization. No numerical improvement threshold here. | Hemodynamic outcomes |
| PR3-013 | PDF105–106 | Secondary days with organ failure defined by SOFA and days without organ failure in objectives / days alive without organ failure in endpoints, inclusion–D30. No SOFA cutoff in these passages. | Organ-failure days |
| PR3-014 | PDF105–106 | Secondary catecholamine support duration and days alive without support, inclusion–D30. | Catecholamine duration/free days |
| PR3-015 | PDF105–106 | Secondary ventilation duration and days alive without ventilation, inclusion–D30 and D60. | Ventilation duration/free days |
| PR3-016 | PDF105–106 | Secondary LV function by echocardiography D30; adverse drug effects incidence: AF/other supraventricular arrhythmias, ventricular arrhythmias including VT, VF and torsades, hypokalemia. | LV function; safety endpoint status |
| PR3-017 | PDF105–106 | Primary and secondary endpoints in predefined subgroups: acute MI, myocarditis, post-cardiac surgery, post-cardiac arrest. No interaction procedure or subgroup multiplicity rule in these passages. | Prespecified subgroup analyses |
| PR3-018 | PDF107 | Multicenter phase III, randomized, double-blind, placebo-controlled superiority trial; 2 arms, 1:1; all consecutive eligible patients. 14 French sites. | Trial design/allocation |
| PR3-019 | PDF107 | First 20 patients assigned by balanced randomization; thereafter stochastic minimization assignment probability 0.8 by center and primary etiology (acute MI, myocarditis, post-heart surgery, other causes). Central 24-hour Internet service conceals allocation. | Randomization/minimization |
| PR3-020 | PDF108 | Unmasked trained preparation nurse; participants, care providers and outcome assessors masked. Investigator can request unblinding when essential. | Blinding |
| PR3-021 | PDF109 | Baseline J1 inclusion/randomization; IV infusion 24 h, as soon as possible and no later than 24 h after randomization. CERNEVIT prohibited during experimental administration. | Intervention timing/duration |
| PR3-022 | PDF109–110 | Baseline admission/ECMO dates and times, etiology, age/sex, McCabe/Jackson, Charlson, SAPS II, SOFA, hemodynamics, catecholamines, laboratory/echo indices. Hepatic insufficiency: bilirubin >100 μmol/L or albumin <35 g/L without another cause. Echo LVEF, VTI, tissue Doppler systolic velocity at lateral mitral annulus. Measurement list does not mandate all as adjustment covariates. | Baseline covariates |
| PR3-023 | PDF110 | Daily D1,2,3…30 or death/ICU discharge: BP, heart rate, catecholamines, ventilation/RRT, urine, labs, SOFA, ECG, echo, weanability; ECMO parameters and complications until removal. | Measurement schedule |
| PR3-024 | PDF110 | Daily weaning trial once stable: MBP >60 mm Hg, no/low vasopressors, pulsatile waveform ≥24 h. Reduce flow to 66%, 33%, then minimum 1–1.5 L/min. Stop if MBP consistently <60 mm Hg, restore 100% flow. Weanable at aortic VTI ≥12 cm, LVEF >20–25%, TDSa ≥6 cm/s at minimum flow; both arms. | Weaning decision rule |
| PR3-025 | PDF111 | D30/D60: vital status/date/hour, ECMO or repeat ECMO, other support, transplant, ventilation, ICU/hospital discharge. Collect contact at ICU discharge for D60. Chronology table: D1 randomization/drug; clinical/procedural follow-up D2–D30 or death/ICU discharge; AE/vital/ECMO status also D60; pursuit consent at D60 if absent earlier. | Outcome ascertainment |
| PR3-026 | PDF111 | Enrollment 36+3 months; subject participation/follow-up 60 days; treatment 24 h; total duration 38+3 months. Randomize/blind immediately once eligible. Added procedures: D1 study drug, D60 phone follow-up. | Study duration |
| PR3-027 | PDF112 | Stop drug for anaphylactic shock, VF, torsades, VT, refractory hypotension: mean arterial BP <45 mm Hg for >60 min despite two successive 500 mL crystalloid boluses AND norepinephrine ≥4 μg/kg/min OR epinephrine ≥2 μg/kg/min. Drug suspension/termination alone does not remove participant from study. | Drug discontinuation/safety |
| PR3-028 | PDF112–113 | Stated premature-exit reasons: death, lost follow-up, consent withdrawal; adverse reaction/drug termination not automatic exit. Participant can leave anytime; investigator safety withdrawal allowed. Prior data usable unless objection; collect endpoints at exit as agreed, attempt vital status in lost patients. Severe AE follow-up 30 days after drug termination or until resolved. | Population/missing follow-up |
| PR3-029 | PDF113 | Sponsor/authority may cancel on DMC recommendation for SUSARs or between-arm serious-reaction discrepancy, new information limiting objectives, or unmet enrollment targets. No numerical stopping boundary. Authority/IRB notification within 15 days. | Stopping rules |
| PR3-030 | PDF114–115,133 | Eligibility: refractory acute cardiogenic shock with VA-ECMO in preceding 48 h; relative or emergency consent. Exclusions: age <18; pregnant/lactating; ECMO >48 h; resuscitation cumulative low-flow >30 min in preceding 48 h (older low-flow requires full consciousness recovery); irreversible neurology; end-stage cardiomyopathy without recovery; MI mechanical complication; aortic regurgitation >II; PE/toxicity ECMO; post-LVAD; heart transplant; moribund/SAPS II >90; Child B/C or severe hepatic insufficiency; chronic dialysis; levosimendan hypersensitivity; torsades in preceding 30 days; epilepsy; guardianship/legal incapacity; another interventional study; weight >180 kg; Cernevit hypersensitivity; hypervitaminosis; severe hypercalcemia/hypercalciuria or predisposing conditions; vitamin A/retinoids. §14.2 co-enrollment exception separately mapped. | Eligibility/population |
| PR3-031 | PDF115 | Recruitment table: 206 subjects, 14 sites, 36+3 months, 15.8 subjects/site (printed 15,8), 0.4/site/month. Administrative recruitment quantities distinct from power assumptions. | Planned total 206 |
| PR3-032 | PDF116 | Historical pharmacology: half-life 60 min, clearance 300 mL/min, protein binding 97%, equilibrium 4–8 h, metabolite about 3 days. Levosimendan 2.5 mg/mL, 5 mL vials, 3/box; Cernevit placebo 5 mL powder vial, 1/box. | Formulation |
| PR3-033 | PDF117 | Infusion 24 h without initial bolus; start 0.15 μg/kg/min, increase to 0.20 after 2 h if no rate-limiting side effects. Storage +2 to +8 °C. | Dose/rate/duration |
| PR3-034 | PDF117 | Preparation table columns: weight / flasks / glucose / H1–H2 mL/h / H3–H24 mL/h. Rows: 40–46 kg /1/250 mL/8/11; 47–89 kg /2/500 mL/16/22; 90–132 kg /3/1000 mL/32/44; 133–180 kg /4/1000 mL/32/44. Pump flow units distinct from dose text. | Dose preparation/weight bands |
| PR3-035 | PDF118 | Additional inotropes allowed in both arms, dobutamine preferred; open-label levosimendan prohibited entire study, Cernevit only during experimental administration; additional inotropes except digoxin. | Concomitant interventions |
| PR3-036 | PDF118 | Common ECMO management: flow 3.5–5 L/min; PaO2 65–90 mm Hg and/or saturation >90%; PaCO2 40–45 mm Hg; perfusionist at least every 48 h; aPTT 55–70 sec or anti-Xa 0.4–0.6 IU/mL; free Hb every 48 h/as indicated; transfusion Hb 9–10 g/dL, possibly 7–8 if stable/no residual ischemia; platelets <20 G/L or bleeding with severe thrombopenia. Operational targets, not outcome definitions. | Common ECMO management |
| PR3-037 | PDF119 | Physician supervises compliance during 24-hour infusion; efficacy measurements Day1/randomization through 60 days. | Exposure/follow-up |
| PR3-038 | PDF120–122 | AE is untoward occurrence without required causality; reaction has causal relationship. Serious: death, life-threatening, hospitalization/prolongation, disability, congenital abnormality. Unexpected differs from reference safety information. All serious/nonserious AEs recorded eCRF; severity mild/moderate/serious. WHO-UMC table: certain, probable/likely, possible, unlikely; all points reasonably complied with. These are source categories, not review dispositions. | Safety definitions/ascertainment |
| PR3-039 | PDF122–123 | Under ECMO only deaths directly related to treatment immediately notified; historical mortality 40–60%; all-cause death extraction every 3 months. After weaning, only listed life-threatening/fatal SAEs immediately notified: VF, torsades, VT (HR ≥110 bpm), PVC/PAC/AF, hypotension grades3/4 and refractory rule PR3-027. Other SAEs recorded CRF with extraction every 3 months. | Safety notification versus incidence |
| PR3-040 | PDF123 | Historical mortality 58%, not observed trial rate. Arm imbalance/higher than expected mortality prompts safety response, no numeric boundary. Non-immediate events include natural-course events, hypotension grades1/2 (<30% mean BP decrease), HR <110 bpm, PVC/PAC/AF without life-threatening/fatal outcome, potassium 3–3.5 mmol/L. | Safety thresholds/monitoring |
| PR3-041 | PDF124–125 | Safety reporting begins treatment/first specific intervention, continues 60 days after randomization, indefinitely if likely study-related. Monitor until resolved despite withdrawal. SUSAR initial notification immediate if fatal/life-threatening, otherwise ≤15 days; follow-up 8 calendar days; emerging issue follow-up ≤8 days. Administrative deadlines, not efficacy interim rules. | Safety window |
| PR3-042 | PDF126 | Annual DSUR includes cumulative AEs, submitted ≤60 days after authorization anniversary. DSMB primary mission safety, may monitor efficacy especially if interim analysis; first meeting before enrollment. No actual efficacy look schedule, alpha spending or futility boundary here. | DSMB/interim monitoring |
| PR3-043 | PDF127,130 | All comparisons two-sided type I error 5%. No separate hierarchy or multiplicity procedure in these paragraphs. | Alpha/sidedness/multiplicity |
| PR3-044 | PDF127–128 | Descriptive overall/by arm; comparative analysis systematically unadjusted and adjusted for possibly unbalanced baseline prognostic factors; model according to distribution/type. No fixed adjustment list here. | Adjustment plan |
| PR3-045 | PDF128,130 | ITT all randomized, initial arm, all data regardless treatment changes; §12.1.5 excludes patients withdrawing consent who request no analysis. No replacement of premature exits. | ITT/population |
| PR3-046 | PDF128–129 | Five termination states: not weaned D30 censored; death before D30 without weaning competing; successful weaning event; unsuccessful weaning (death/repeat ECMO/other device/transplant within 30 days of removal) competing; lost follow-up before D30 censored. Successful time = weaning date minus randomization date; unsuccessful time = removal date minus randomization date despite later failure component; death time = death minus randomization; lost time = latest news minus randomization; others censored at 30 days. | Event-time formulas/encoding |
| PR3-047 | PDF128,130 | SAS or R latest at analysis. Detailed SAP validated by scientific committee; later modifications before unblinding and committee validated. CONSORT flow: included, analyzed/exclusion reasons, deviations, inclusion curve. | SAP governance/prespecification |
| PR3-048 | PDF128–129 | Qualitative n/%; quantitative n, mean, SD, 95% CI mean, median, range, IQR. Censored KM or CIF with 15/30/60-day rates as appropriate and 95% CI; primary CIF at 15/30 days with 95% CIs. | Descriptions/CIF displays |
| PR3-049 | PDF129 | Primary Fine–Gray between-arm comparison and prognostic adjustment; proportional hazards evaluated by Schoenfeld residuals, quantitative covariate log-linearity studied. Report subdistribution HR with 95% CI. CIF nonparametric or model-based. | Primary model/HR/assumptions |
| PR3-050 | PDF129–130 | Secondary qualitative χ², corrected χ² or Fisher; logistic adjustment/exploration. Quantitative Student t-test (duplicated in source list) or Mann–Whitney–Wilcoxon, linear adjustment. Mortality through60 days: KM with95% CI, logrank, Cox adjustment. Time from randomization to death regardless weaning; censor latest news/end60days. | Secondary tests/models; mortality HR |
| PR3-051 | PDF130,138 | Power: control 30-day successful-weaning CIF50% with death/weaning failure competing; target subdistribution HR1.75, alpha5%, power80%, 101 successful-weaning events, 206 subjects, 103/arm. Latouche et al2004 reference38. No printed equation here. | Sample size/power |
| PR3-052 | PDF130 | No replacement of premature exits; two-sided5% alpha; initial-arm ITT all data regardless treatment change. | Missingness/replacement/population |
| PR3-053 | PDF131 | Missing data must be coded in CRF; electronic consistency checks and audit trail. No statistical imputation procedure here. | Missing data |
| PR3-054 | PDF133,151 | Other interventional trials prohibited except IMPULMACS,NCT04951999; observational participation requires consultation. Change summary introduces exception in v2.0. | Co-enrollment eligibility |
| PR3-055 | PDF139 | Addenda may change without protocol version change. Lists investigators, SAE/pregnancy forms, SOFA/Glasgow/SAPS2, levosimendan/Cernevit SmPC. External URLs not read; numerical scale tables not supplied on this page. | Version governance |
| PR3-056 | PDF140–141 | Cover prints v1.1 date12/04/2020 and v2.0 date05/31/2023. Table heading v1.1 dated14/12/2020, row v1.1 of04/12/2020; v2.0 dated31/05/2023. Preserve printed identity strings without diagnosis. | Version/date provenance |
| PR3-057 | PDF141,143 | v1.1 resuscitation >30 min before ECMO becomes v2.0 cumulative low-flow >30 min in preceding48h; older episode requires recovered consciousness. Torsades history becomes preceding30days; adds weight>180kg and Cernevit exclusions21–25. Other thresholds repeat age<18,ECMO>48h,SAPSII>90,aortic regurgitation>II,ChildB/C. | Eligibility amendment |
| PR3-058 | PDF141–142,144–145,151 | v1.1 riboflavin placebo becomes v2.0 polyvitamin Cernevit; trained unmasked preparation nurse; drug3×5mL vials at2.5mg/mL, placebo1×5mL Cernevit vial; adds Cernevit SmPC and prohibition during experimental administration. Native tracked-change text contains old deleted words; active final prose PR3-032–035 anchors retained definitions. | Placebo amendment |
| PR3-059 | PDF142–144 | v1.1 13sites,24month enrollment,26total; v2.0 14sites,24+12enrollment,26+12total; participation2months/60days and24h treatment unchanged. Summary enrollment/site/month0.7→0.4; recruitment table0.66→0.4. Planned206 and15.8/site unchanged. | Enrollment/duration amendment |
| PR3-060 | PDF145–146 | Infusion24h without bolus,0.15→0.20μg/kg/min after2h if tolerated unchanged. v2.0 preparation adds133–180kg/4flasks/1000mL/32mL/h H1–2/44mL/h H3–24; lower3bands unchanged. Open-label drug prohibited; Cernevit during study infusion newly explicit. | Dose amendment |
| PR3-061 | PDF146–150 | v2.0 reorganizes safety: under-ECMO all-cause death extraction every3months; immediate post-weaning reporting limited to life-threatening/fatal listed SAEs, VT≥110bpm, PVC/PAC/AF, grade3/4 hypotension and refractory rule. Retains <30% BP drop, HR<110, potassium3–3.5 thresholds. Makes60-day window explicit. The old monthly death-extraction paragraph appears in right-column native text but is struck through on fresh PDF149 image; it is deleted, not retained v2.0 specification. Deleted prior AE list includes nausea/vomiting/diarrhea/constipation/dizziness/headache/insomnia, continuing PDF150. Active final prose PR3-038–042 anchors definitions. | Safety amendment |
| PR3-062 | PDF152–153 | v2.0 cover05/31/2023→v3.0 cover06/26/2024; table31/05/2023→26/06/2024. Inclusion24+12months→36+3; total26+12→38+3; participation2months unchanged;206,14sites,15.8/site,0.4/site/month unchanged. Fresh PDF153 image confirms old values struck and new retained; do not combine deleted and inserted quantities. | Final version/duration amendment |

## Exact source page links

Each PDF-page token in the relationship table above refers only to the supplied DOC-002 source. Multi-page locators mean the individually listed pages below, not a different document. These links preserve physical PDF page identity for mechanical recheck.

[PDF103](../../../joi250087supp1_prod_1766516490.96011.pdf#page=103)

[PDF104](../../../joi250087supp1_prod_1766516490.96011.pdf#page=104)

[PDF105](../../../joi250087supp1_prod_1766516490.96011.pdf#page=105)

[PDF106](../../../joi250087supp1_prod_1766516490.96011.pdf#page=106)

[PDF107](../../../joi250087supp1_prod_1766516490.96011.pdf#page=107)

[PDF108](../../../joi250087supp1_prod_1766516490.96011.pdf#page=108)

[PDF109](../../../joi250087supp1_prod_1766516490.96011.pdf#page=109)

[PDF110](../../../joi250087supp1_prod_1766516490.96011.pdf#page=110)

[PDF111](../../../joi250087supp1_prod_1766516490.96011.pdf#page=111)

[PDF112](../../../joi250087supp1_prod_1766516490.96011.pdf#page=112)

[PDF113](../../../joi250087supp1_prod_1766516490.96011.pdf#page=113)

[PDF114](../../../joi250087supp1_prod_1766516490.96011.pdf#page=114)

[PDF115](../../../joi250087supp1_prod_1766516490.96011.pdf#page=115)

[PDF116](../../../joi250087supp1_prod_1766516490.96011.pdf#page=116)

[PDF117](../../../joi250087supp1_prod_1766516490.96011.pdf#page=117)

[PDF118](../../../joi250087supp1_prod_1766516490.96011.pdf#page=118)

[PDF119](../../../joi250087supp1_prod_1766516490.96011.pdf#page=119)

[PDF120](../../../joi250087supp1_prod_1766516490.96011.pdf#page=120)

[PDF121](../../../joi250087supp1_prod_1766516490.96011.pdf#page=121)

[PDF122](../../../joi250087supp1_prod_1766516490.96011.pdf#page=122)

[PDF123](../../../joi250087supp1_prod_1766516490.96011.pdf#page=123)

[PDF124](../../../joi250087supp1_prod_1766516490.96011.pdf#page=124)

[PDF125](../../../joi250087supp1_prod_1766516490.96011.pdf#page=125)

[PDF126](../../../joi250087supp1_prod_1766516490.96011.pdf#page=126)

[PDF127](../../../joi250087supp1_prod_1766516490.96011.pdf#page=127)

[PDF128](../../../joi250087supp1_prod_1766516490.96011.pdf#page=128)

[PDF129](../../../joi250087supp1_prod_1766516490.96011.pdf#page=129)

[PDF130](../../../joi250087supp1_prod_1766516490.96011.pdf#page=130)

[PDF131](../../../joi250087supp1_prod_1766516490.96011.pdf#page=131)

[PDF132](../../../joi250087supp1_prod_1766516490.96011.pdf#page=132)

[PDF133](../../../joi250087supp1_prod_1766516490.96011.pdf#page=133)

[PDF134](../../../joi250087supp1_prod_1766516490.96011.pdf#page=134)

[PDF135](../../../joi250087supp1_prod_1766516490.96011.pdf#page=135)

[PDF136](../../../joi250087supp1_prod_1766516490.96011.pdf#page=136)

[PDF137](../../../joi250087supp1_prod_1766516490.96011.pdf#page=137)

[PDF138](../../../joi250087supp1_prod_1766516490.96011.pdf#page=138)

[PDF139](../../../joi250087supp1_prod_1766516490.96011.pdf#page=139)

[PDF140](../../../joi250087supp1_prod_1766516490.96011.pdf#page=140)

[PDF141](../../../joi250087supp1_prod_1766516490.96011.pdf#page=141)

[PDF142](../../../joi250087supp1_prod_1766516490.96011.pdf#page=142)

[PDF143](../../../joi250087supp1_prod_1766516490.96011.pdf#page=143)

[PDF144](../../../joi250087supp1_prod_1766516490.96011.pdf#page=144)

[PDF145](../../../joi250087supp1_prod_1766516490.96011.pdf#page=145)

[PDF146](../../../joi250087supp1_prod_1766516490.96011.pdf#page=146)

[PDF147](../../../joi250087supp1_prod_1766516490.96011.pdf#page=147)

[PDF148](../../../joi250087supp1_prod_1766516490.96011.pdf#page=148)

[PDF149](../../../joi250087supp1_prod_1766516490.96011.pdf#page=149)

[PDF150](../../../joi250087supp1_prod_1766516490.96011.pdf#page=150)

[PDF151](../../../joi250087supp1_prod_1766516490.96011.pdf#page=151)

[PDF152](../../../joi250087supp1_prod_1766516490.96011.pdf#page=152)

[PDF153](../../../joi250087supp1_prod_1766516490.96011.pdf#page=153)

## Scope closure and limitations

Mapped 51/51 assigned pages: 51 reusable-backed, 0 fresh-required. Inventory: 62 shard-local relationship records including historical quantities, administrative provenance, and prospective statistical elements; no displayed current trial results in this shard. All result-relevant table groups are mapped: endpoints, allocation, chronology, recruitment, four-row preparation, causality, statistical definitions, sample size and amendment comparisons. Bibliography and administration explicitly opened and accounted.

No scientific coverage gaps. Native extraction does not preserve deletion styles in amendment tables. Fresh visual inspection of PDF149 and153 resolved monthly versus three-monthly reporting and duration replacement values. Other amendment records retain old/new column provenance and are anchored to final active prose. No sensitivity procedure beyond adjusted/unadjusted analyses and predefined subgroups is printed in this assigned scope. No fixed prognostic covariate list, statistical imputation rule, numerical interim efficacy boundary or multiplicity procedure is printed in these assigned passages; other assigned sources may contain them. These are extraction boundaries, not findings. Global N/S numbering and main-paper pairing belong to the coordinator/checkers.
