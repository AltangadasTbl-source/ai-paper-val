# Support Quantitative Evidence Map — DOC-002 pp. 97-109 and DOC-003 pp. 1-16

## Scope and evidence method

This is a source-grounded extraction map, not a candidate diagnosis or adjudication. `D-N` and `D-S` are local relationship identifiers for this part only. Direct PDF pages are the authority. DOC-002 pp. 97-109 were individually visually inspected from the current-run 180-dpi JPEGs because its native/layout extraction is font-encoding garble. DOC-003 pp. 1-2 were checked using fresh layout text and direct PDF; pp. 3-16 used the page-addressable reused normalized text and page images, visually confirmed against the direct PDF/rendered-page representation.

## Per-page coverage

| Source/page | Content and result relevance | Coverage outcome |
|---|---|---|
| DOC-002 PDF p. 97 | Blank CRF fields for prior quit attempt, smoking duration, age starting, and SUTS; site IDs 3000-3007. | No completed participant/result values; template labels retained in D-N001. |
| DOC-002 PDF p. 98 | Blank primary-abstinence, mixed-model, and verified-abstinence subgroup templates; site IDs 3008-3015. | No displayed estimates; template definitions retained in D-N002. |
| DOC-002 PDF p. 99 | Continuation of blank subgroup template; site IDs 3016-3017. | No result values. |
| DOC-002 PDF p. 100 | Glossary. | Definitions retained in D-N003. |
| DOC-002 PDF pp. 101-109 | mTB-Tobacco intervention SMS log with numbered messages, schedule markers, times, and character counts. | Protocol intervention content; timing/quantity definitions retained in D-N004; no analysis results. |
| DOC-003 PDF p. 1 | Supplement contents. | No result values. |
| DOC-003 PDF p. 2 | Trial Steering Committee member list. | No result values. |
| DOC-003 PDF p. 3 | eTable 1, screening and ineligibility counts. | D-N005. |
| DOC-003 PDF p. 4 | eTable 2, prior quit attempts by cluster and arm. | D-N006. |
| DOC-003 PDF p. 5 | eTable 3, TB-treatment-adherence summaries and z/P pairs. | D-N007, D-S001. |
| DOC-003 PDF p. 6 | eTable 4, causes of death. | D-N008. |
| DOC-003 PDF p. 7 | Kaplan-Meier survival plot. | D-N009. |
| DOC-003 PDF p. 8 | eTable 5, cluster recruitment and abstinence rates. | D-N010. |
| DOC-003 PDF p. 9 | eTable 6, cluster death counts/rates. | D-N011. |
| DOC-003 PDF pp. 10-11 | eTable 7, cluster characteristics and unadjusted RRs. | D-N012, D-S002. |
| DOC-003 PDF p. 12 | eTable 8, subgroup RRs for verified abstinence. | D-N013, D-S003. |
| DOC-003 PDF pp. 13-14 | eTable 9, post-hoc ITT sensitivity analysis after exclusion of deaths and footnotes. | D-N014, D-S004. |
| DOC-003 PDF pp. 15-16 | eTable 10, adverse-event categories, counts/percentages, test statistics, and P values. | D-N015, D-S005. |

## DOC-002 protocol and administrative evidence

### D-N001 — CRF baseline/template variables

- **Location:** DOC-002 PDF p. 97.
- **Direct observation:** The uncompleted form includes `Attempted to quit in the past`, `Smoking duration`, `Age starting`, and `Strength of Urges To Smoke (SUTS)`. The visible site identifiers are 3000 through 3007. The SUTS columns specify group, n, median (IQR), mean (SD), z value, and P value, but contain no filled values.
- **Matching/main-paper key:** baseline smoking history and SUTS variables; this page supplies only a planned data-collection/display schema.
- **Rule/interpretation boundary:** blank fields are not zero observations and are not inferential results.

### D-N002 — Primary-outcome and subgroup template definitions

- **Location:** DOC-002 PDF pp. 98-99.
- **Direct observation:** The blank mixed-model template labels self-reported abstinence at 9 weeks, self-reported last-7-days abstinence, CO and cotinine test, and CO/cotinine ITT, with columns `n/N(%)`, proportion (95% CI), RR (95% CI), adjusted RR (95% CI), and ICC. The continuation lists subgroup categories: age <40/>40, education, occupation, gender, and smoking duration <24/>24 years. No cell is completed.
- **Matching/main-paper key:** abstinence outcomes, RR/adjusted RR/ICC and subgroup analysis.
- **Rule/interpretation boundary:** these are planned labels only; no numerical estimate may be inferred from a blank template.

### D-N003 — Definitions relevant to matching

- **Location:** DOC-002 PDF p. 100.
- **Direct observation:** Glossary defines cRCT as cluster randomized controlled trial; CI as confidence interval; CO as carbon monoxide; ICC as intraclass correlation coefficient; IQR as interquartile range; ITT as intention to treat; RR as relative risk; SAP as statistical analysis plan; SMS as short message service; SUTS as strength of urges to smoke; TB as tuberculosis; and ppm as parts per million.
- **Matching/main-paper key:** defines the scale/measure labels used in DOC-003 eTables 3, 8, and 9.

### D-N004 — Intervention-message schedule and displayed quantity

- **Location:** DOC-002 PDF pp. 101-109.
- **Direct observation:** The log numbers messages 1-134 and prints a character count and scheduled timing for each. It states participants receive up to 5 text messages every day (message 3), begins the intervention at `Q(-8), Tx(+1)`, marks the quit date as `Q` / Tx(+8), and includes follow-up messages at Q(+52)/Tx(+61), Q(+112)/Tx(+121), and Q(+180)/Tx(+189). Selected explicit numeric claims include `6 months` regular treatment (message 18), `30%` lung-capacity increase after a few weeks without smoking (message 98), 10 deep breaths (message 118), 1.5 months (message 123), and two/four/six-month TB-treatment milestones (messages 132-134). Character counts range from 54 (message 74) to 163 (messages 4, 18, and 27) among visible entries.
- **Matching/main-paper key:** intervention dose/schedule and TB-treatment timepoints; not an outcome dataset.
- **Rule/interpretation boundary:** the message claims are protocol content. They do not report trial estimates, denominators, or tested effects.

## DOC-003 quantitative evidence

### D-N005 — Screening and ineligibility accounting

- **Location:** DOC-003 PDF p. 3, eTable 1.
- **Direct observation:** Total screenings 9,232; eligible 1,086; ineligible 8,146; consent not given 6 (3 not willing to follow procedures and 3 not willing to participate). Listed ineligibility reasons: age <15 years 385; not diagnosed with pulmonary TB 2,783; diagnosis not within last 4 weeks 1,820; not current smoker (defined as not smoking at least 25 days in the past month) 7,069; not willing to quit 273; no mobile phone 1,290; cannot read SMS/no household reader 236.
- **Rule available for later checking:** 1,086 + 8,146 = 9,232. The printed reason categories are not explicitly stated to be mutually exclusive; do not sum them as though they are.

### D-N006 — Prior quit attempts by cluster

- **Location:** DOC-003 PDF p. 4, eTable 2.
- **Direct observation:** Each of the 27 cluster rows has Yes plus No = 40 and percentages summing to 100.0. mHealth Yes counts (site: count [%]): 1002 13 [32.5], 1003 0 [0.0], 1005 7 [17.5], 1006 0 [0.0], 1007 23 [57.5], 1008 9 [22.5], 1011 16 [40.0], 1012 11 [27.5], 1013 1 [2.5], 1015 4 [10.0], 2001 9 [22.5], 2003 11 [27.5], 2005 19 [47.5], 2006 18 [45.0], 2007 5 [12.5], 2009 6 [15.0], 2010 16 [40.0]. Usual-care Yes counts: 1001 10 [25.0], 1004 1 [2.5], 1009 0 [0.0], 1010 0 [0.0], 1014 5 [12.5], 2002 3 [7.5], 2004 0 [0.0], 2008 4 [10.0], 2011 10 [25.0]. The paired No counts are the printed complement to 40 in each row.
- **Matching/main-paper key:** baseline quit-attempt distribution by randomized cluster.

### D-N007 / D-S001 — TB-treatment adherence by month

- **Location:** DOC-003 PDF p. 5, eTable 3.
- **Direct observation:** For months 1-6, respectively, mHealth median(IQR) is 30(30-30) each month; mean(SD) is 29.87(1.345), 29.59(2.757), 29.39(3.894), 29(5.092), 28.56(6.049), 27.88(7.397). Control median(IQR) is 30(30-30) each month; mean(SD) is 29.9(0.2), 29.8(0.6), 29.7(2.3), 29.5(3.3), 29.5(3.3), 29.3(3.9). Total: mHealth 180(180-180), 174.3(21.501); control 180(180-180), 178.0(12.1).
- **Statistical observation (D-S001):** Printed z/P pairs for month 1 through total are -0.86/0.388, 0.44/0.656, 1.64/0.101, 0.44/0.657, 0.95/0.34, 1.85/0.064, and 1.19/0.232. Test name, sidedness, and population denominators are not printed on this page.
- **Matching/main-paper key:** secondary outcome, TB-treatment adherence over months 1-6.

### D-N008 — Death causes by arm

- **Location:** DOC-003 PDF p. 6, eTable 4.
- **Direct observation:** Total deaths: overall 52, mHealth 25, usual care 27. Causes overall/mHealth/usual care: TB 32 (61.5%)/16 (64.0%)/16 (59.2%); cancer 3 (5.7%)/0/3 (11.1%); heart attack 8 (15.2%)/5 (20.0%)/3 (11.1%); fall/fever 2 (3.8%)/1 (4.0%)/1 (3.7%); stroke 2 (3.8%)/0/2 (7.4%); liver failure 2 (3.8%)/2 (8.0%)/0; drug user 1 (1.9%)/0/1 (7.4%); HIV/AIDS comorbidity 1 (1.9%)/1 (4.0%)/0; severe pneumonia 1 (1.9%)/0/1 (7.4%).
- **Rule available for later checking:** arm counts add to the overall count by cause and death totals 25 + 27 = 52.

### D-N009 — Kaplan-Meier survival display

- **Location:** DOC-003 PDF p. 7, eFigure/Figure S1.
- **Direct observation:** The figure labels time as number of days (0-200 shown) and survival probability (0.80-1.00 labelled). It displays Control and Intervention curves with shaded confidence bands; at approximately day 180, the plotted Control curve is about 0.93 and Intervention about 0.96. No exact event counts, model statistic, CI values, or P value are printed.
- **Matching/main-paper key:** survival/death outcome by trial group. Approximate axis reading is descriptive only, not an exact numeric comparator.

### D-N010 — Cluster recruitment and abstinence rates

- **Location:** DOC-003 PDF p. 8, eTable 5.
- **Direct observation:** Twenty-seven site rows each report recruitment `40/N (%)`, self-reported quitter at 6-month follow-up, verified quitter at 6-month follow-up, and 6-month ITT quitter. Every ITT denominator is 40. The table contains all cluster-level values, including: control 1001 4/40 (10) ITT; mHealth 1002 17/40 (42.5), 1003 35/40 (87.5), 1005 25/40 (62.5), 1011 29/40 (72.5), 2009 26/40 (65), and 2012 20/40 (50); controls 1004 7/40 (17.5), 1009 5/40 (12.5), 1010 9/40 (22.5), 1014 7/40 (17.5), 2002 6/40 (15), 2004 0/40 (0), 2008 12/40 (30), 2011 5/40 (12.5). Other printed mHealth ITT counts are: 1006 5, 1007 7, 1008 10, 1012 23, 1013 16, 1015 22, 2001 5, 2003 16, 2005 6, 2006 11, 2007 12, 2010 15 (all /40; printed percentages 12.5, 17.5, 25, 57.5, 40, 55, 12.5, 40, 15, 27.5, 30, 37.5 respectively).
- **Rule available for later checking:** each printed n/N percentage may be checked against its printed numerator and denominator, allowing stated display precision; self-reported and verified outcomes are distinct measures with denominators that may be below 40.

### D-N011 — Cluster-wise deaths

- **Location:** DOC-003 PDF p. 9, eTable 6.
- **Direct observation:** Death n(%) by cluster: 1001 1(2.5), 1002 0, 1003 0, 1004 0, 1005 2(5.0), 1006 0, 1007 0, 1008 0, 1009 4(10.0), 1010 2(5.0), 1011 1(2.5), 1012 1(2.5), 1013 4(10.0), 1014 2(5.0), 1015 0, 2001 0, 2002 3(7.5), 2003 2(5.0), 2004 4(10.0), 2005 3(7.5), 2006 1(2.5), 2007 3(7.5), 2008 5(7.5), 2009 0, 2010 3(7.5), 2011 6(15.0), 2012 5(12.5). Arm labels are printed with each row.
- **Matching/main-paper key:** death outcome by cluster; the denominator is not explicitly repeated on this page, though eTable 5 records 40 recruited for each cluster.
- **Rule available for later checking:** only after confirming a common denominator and population across tables, a printed percentage can be compared with its count.

### D-N012 / D-S002 — Cluster characteristics and unadjusted relative risks

- **Location:** DOC-003 PDF pp. 10-11, eTable 7.
- **Direct observation:** The 27 site rows provide age mean(SD), male n(%), smoking-duration mean(SD) in years, education categories (no formal, primary, middle, higher) and occupation (employed, dependent, retired). Each row is a cluster, usually n=40; exceptions visibly include site 1015 male 39(97.5), 2003 male 38(95), 2004 male 34(85), 2005 male 39(97.5), 2006 male 38(95), 2007 male 33(82.5), 2008 male 32(80), 2009 male 35(87.5), 2010 male 36(90), and 2011 male 39(97.5). Exact row values are on the cited two pages.
- **Statistical observation (D-S002):** Printed unadjusted relative risks (95% CI), in the order of displayed characteristics, are age 1.03 (1.01-1.04), male 0.83 (0.34-2.02), smoking duration 0.97 (0.95-0.99), education no-formal 1 [reference], primary 1.32 (0.88-1.97), middle 1.91 (1.16-3.15), higher 1.86 (1.16-2.99), occupation employed 1 [reference], dependent 2.01 (1.30-3.09), retired 1.00 (0.43-2.31).
- **Matching/main-paper key:** cluster-level characteristics, reference categories, and unadjusted relative-risk analysis.

### D-N013 / D-S003 — Subgroup analysis of verified 6-month abstinence

- **Location:** DOC-003 PDF p. 12, eTable 8.
- **Direct observation / statistical observation:** Unadjusted RR (95% CI) for verified abstinence at month 6: all 2.890 (1.983-4.709); age <40 2.672 (1.472-4.857), >=40 2.953 (2.048-5.092); no formal education 2.880 (1.566-5.542), primary years 1-5 2.638 (1.849-4.07), secondary or above >=6 years 2.719 (1.348-4.83); active job/business 2.989 (1.933-4.885), dependent/retired 2.587 (1.329-3.986); smoking duration <24 years 3.511 (1.884-7.127), >=24 years 2.446 (1.550-3.911); reading SMS yes 2.769 (1.743-4.318), no 2.198 (1.288-3.299).
- **Matching/main-paper key:** verified abstinence at 6 months; effect measure explicitly labelled RR and 95% CI.

### D-N014 / D-S004 — Post-hoc ITT sensitivity analysis excluding deaths

- **Location:** DOC-003 PDF pp. 13-14, eTable 9.
- **Direct observation:** Population denominators after exclusion of deaths are mHealth 695 and usual care 333. For biochemically verified abstinence at month 6, <10 ppm: 300/695, 43.2% (39.4-46.9) vs 55/333, 16.5% (12.7-20.9); absolute difference 26.7 (21.2-32.1); crude RR 2.9 (1.8-6.4), crude ICC 0.18; adjusted RR 3.1 (1.9-6.5), adjusted ICC 0.18. For <6 ppm: 264/695, 38.0% (34.4-41.7) vs 38/333, 11.4% (8.2-15.3); difference 26.6 (21.6-31.5); crude RR 3.6 (2.4-5.4), ICC 0.17; adjusted RR 3.8 (2.4-6.2), ICC 0.18.
- **Direct observation, continued:** Week-9 point abstinence: 353/695, 50.8% (47.0-54.6) vs 75/333, 22.5% (18.1-27.4); difference 28.3 (22.4-34.1); crude RR 2.5 (1.7-3.6), ICC 0.20; adjusted RR 2.6 (1.7-3.8), ICC 0.20. Month-6 point abstinence: 400/695, 57.5% (53.8-61.2) vs 82/333, 24.6% (20.1-29.6); difference 32.9 (27.0-38.8); crude RR 2.58 (1.8-3.6), ICC 0.20; adjusted RR 2.7 (1.8-4.0), ICC 0.20. Successful TB treatment: 643/695, 92.5% (90.3-94.4) vs 308/333, 92.5% (89.1-95.1); difference 0 (-3.4-3.5); crude RR 1.1 (0.7-1.6), ICC 0.25; adjusted RR 1.1 (0.7-1.5), ICC 0.23. Defaulted: 22/695, 3.2% (2.0-4.8) vs 7/333, 2.1% (0.8-4.3); difference 1.1 (-1.0-3.1); RRs/ICCs not printed. Treatment failures: 1/695, 0.1% (0.01-0.8) vs 2/333, 0.6% (0.1-2.2); difference 0.5 (-0.4-1.3); RRs/ICCs not printed.
- **Definitions (p. 14):** a=numerator/total group number; b=absolute difference; c=relative risk; d=intraclass correlation coefficient; e=adjusted for age, sex, education, occupation, smoking duration, accounting for clustering and mixed-effects models for RR; f=carbon-monoxide breath-test cutoff values.
- **Matching/main-paper key:** post-hoc sensitivity analysis, ITT population after deaths excluded; distinctions between crude/adjusted RR and ICC are explicit.

### D-N015 / D-S005 — Adverse events

- **Location:** DOC-003 PDF pp. 15-16, eTable 10.
- **Direct observation:** Each event has none/mild/moderate/severe categories reported as mHealth n(%) and control n(%). Group category counts sum to 699 mHealth and 334 control for nausea, diarrhoea, dry mouth, epigastric pain, headache, insomnia, abnormal dreams, irritability, anxiety, palpitations, and musculoskeletal pain.
- **Statistical observation (D-S005):** Printed X2/P pairs: nausea 6.5 with 0.084 (exact-test superscript); diarrhoea 1.0 with 0.825 (exact); dry mouth 31.2 with <.001; epigastric pain 18.2 with <.001 (exact); headache 2.7 with 0.426; insomnia 6.9 with 0.072; abnormal dreams 3.8 with 0.255 (exact); irritability 18.5 with <.001; anxiety 17.1 with <.001; palpitations 5.2 with 0.154 (exact); musculoskeletal pain 8.8 with 0.031. Page 16 defines superscript a as based on Exact test.
- **Matching/main-paper key:** adverse-event outcomes by study arm. The `<.001` presentations are threshold displays, not literal-zero P values.

## Source-linked observations reserved for downstream checking

These statements do not diagnose or adjudicate any candidate.

1. **D-N011:** eTable 6 prints site 2008 as 5 deaths (7.5%). eTable 5 prints 40 recruited at every cluster, including 2008. Any comparison must first confirm that both figures use the same analysis population and denominator; if they do, `5/40` is a relevant arithmetic relationship for a later independent checker.
2. **D-N010/D-N011/D-N014/D-N015:** Denominators vary by outcome and timepoint (cluster recruited n=40; some observed follow-up denominators <40; sensitivity denominators 695/333; adverse-event denominators 699/334). They must not be substituted for one another without a printed population/time match.
3. **D-S001/D-S005:** Test names and detailed test conventions are incompletely provided for some z/P and X2/P pairs. Later statistical review should use only the stated definitions, including the exact-test footnote, and should not infer a test model from the printed summaries alone.

## Limitations

DOC-002 pp. 97-109 contain blank CRF/template material and an intervention SMS log rather than completed trial results; no numerical outcome can be extracted from a blank field. DOC-003 eFigure p. 7 has no printed exact survival estimates or test output, so its values are only qualitative/axis-based. All DOC-003 table values above were confirmed visually against the direct page image; the normalized text was used only to assist exhaustive transcription.
