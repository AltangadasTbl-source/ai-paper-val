# DOC-003 Support Quantitative Evidence Mapping

## Scope and method

- **Direct source:** `joi200126supp2_prod_1607962892.5372.pdf` (45 PDF pages), Statistical Analysis Plan (SAP), version 1.0, RATE-AF; trial registration printed as ISRCTN 95259705 (PDF p. 1).
- **Fresh extraction:** native text and layout text for PDF pp. 1-45 in `preprocessing/doc003/`; targeted CPU OCR for the cover (p. 1), otherwise blank/nonextractable p. 2, and visual trial schema (p. 26). No reusable scientific extraction existed for this source.
- **Result status:** This SAP contains planned analyses and blank reporting templates, not observed trial results. Blank cells, `N=`, `xx`, `x.xxx`, and dashes are templates/placeholders, not cached result values. No workbook formulas or cached workbook/displayed values apply.

## Complete page map

| PDF page(s) | Content and result-relevant extraction status |
|---|---|
| 1 | Administrative cover: SAP v1.0; planned RATE-AF digoxin-versus-beta-blocker trial; ISRCTN 95259705. No result values. |
| 2 | No extractable substantive content; no applicable quantitative evidence. |
| 3 | Abbreviations/definitions: ITT, SAP, QoL, PCS, MCS; SAP is pre-specified statistical methodology. No result values. |
| 4-5 | Contents/page map only. No result values. |
| 6-8 | Background, objectives, design, doses and planned outcomes/sample-size assumptions. Mapped below. |
| 9-12 | Statistical principles, ITT/per-protocol population, baseline summaries, covariates, missing-data plan. Mapped below. |
| 13-17 | SF-36 item coding, score formulas, EQ-5D, AFEQT, IPAQ, NT-pro-BNP, and diastolic-dysfunction definitions. Mapped below. |
| 18-23 | Primary/secondary outcome models, directions/scales, subgroups and sensitivity analyses. Mapped below. |
| 24 | References only; no result-relevant quantitative relationship. |
| 25 | Blank SAP-deviation reporting template with no filled deviations; no observed result. |
| 26 | Trial schema: two initial-rate-control arms; visits at baseline, 6 and 12 months; planned QoL/walk-distance/echocardiography/biomarker measures and eligibility thresholds. Mapped below. |
| 27 | Schedule-of-assessments template (X markers) for baseline, up-titration, month 6 and month 12; timing support only, no result values. |
| 28 | Blank CONSORT template: total randomised, arm N, completed/primary-outcome available N (%), dropouts, mean [SD], and min-max placeholders. |
| 29-30 | Blank baseline table template: planned counts/percentages and continuous summaries; variables/units and minimisation-variable footnote mapped below. |
| 31 | Blank adherence template: 6/12-month arm/total denominators, categories, non-mutually-exclusive medication types. |
| 32 | Blank ±4-week visit-window deviation-list template. |
| 33 | Blank primary-outcome results template; model and direction labels mapped below. |
| 34-40 | Blank secondary-outcome templates; models, measures, scales, directions, and footnotes mapped below. |
| 41-44 | Blank feasibility/safety templates, including event counts, proportions, rates, chi-square P-value placeholder, GP and pause summaries. |
| 45 | Blank primary-outcome subgroup forest-plot template and interaction-P-value column. |

## Trial, population, outcome, and timing definitions

- Design: prospective, randomised, open-label, blinded-endpoint (PROBE) trial of initial digoxin 62.5-250 micrograms once daily versus bisoprolol 1.25-15 mg once daily (pp. 6-8). Randomisation is 1:1 using minimisation on baseline EHRA (1/2a versus 2b/3/4) and sex (p. 8).
- Primary outcome: SF-36v2 Physical Component Summary (PCS) at 6 months (pp. 6-7, 18, 33). The stated superiority comparison is digoxin versus beta-blocker; the null is no PCS difference (p. 8).
- Secondary time points: patient-reported outcomes at baseline, 6 and 12 months; LVEF/diastolic function at baseline/12 months; heart rate at baseline, 6, 12 months except ambulatory heart rate only once; walking distance and EHRA baseline/6/12 months; NT-pro-BNP baseline/6/12 months (pp. 7, 18-22, 34-40).
- ITT includes all randomised participants in their allocated arm regardless of received intervention; those withdrawing consent for use of data are excluded from that definition (p. 10). Per-protocol primary sensitivity set is adherent to allocation at 6 months and still in AF at 6 months (p. 10).
- Baseline tables use n/count/percent for categorical data and n/mean/SD or n/median/IQR (and range as appropriate) for continuous data; no baseline hypothesis tests or CIs (p. 11; blank template pp. 29-30).
- Analysis adjustment: baseline score when applicable, five-category baseline EHRA, sex, age at randomisation, and baseline LVEF; Bisoprolol is the model reference category (pp. 11-12). LVEF models additionally adjust for baseline MI, PCI/stents, and CABG/CAPG history (p. 20; template p. 37).

## Quantitative definitions, units, and formulas

- Sample-size planning: 144 randomised participants assumed 85% power to detect 0.5 SD QoL effect with two-sided alpha 0.05; 160 would allow estimated 10% loss to follow-up/death before 12-month assessment (p. 8). Background comparator figures are RACE role-physical mean 47 with 17% improvement; another study 22% versus non-significant 8% change, SD 10 points in both arms; PIAF 17% improvement (p. 8). These are rationale, not RATE-AF results.
- All group-difference estimates: two-sided 95% CIs and two-sided P values unless stated otherwise; no multiplicity correction (p. 9). Interim Haybittle-Peto stopping guidance: probability below 0.001 that treatments differ (p. 9).
- Age is `(randomisation date - date of birth) / 365.25`, retaining the integer part (p. 12).
- SF-36 response coding is printed on pp. 12-16. Domains: PF=sum SFQ3a-j and score `((PF-10)/20)*100`; RP=sum SFQ4a-d and `((RP-4)/16)*100`; RE=sum SFQ5a-c and `((RE-3)/12)*100`; SF=sum SFQ6+SFQ10 and `((SF-2)/8)*100`; MH=sum SFQ9b,c,d,f,h and `((MH-5)/20)*100`; EV=sum SFQ9a,e,g,i and `((EV-4)/16)*100`; Pain=sum SFQ7+SFQ8 and `((Pain-2)/9)*100`; GHP=sum SFQ1+SFQ11a-d and `((GHP-5)/20)*100` (p. 16). Domain range is 0 worst to 100 best (p. 19).
- Printed SF-36 aggregate formulas: `AGPHYSCO=(PF*.456)+(RP*.362)+(Pa*.367)+(GHP*.199)+(EV*-.050)+(SF*-.028)+(RE*-.110)+(MH*-.256)`; `AGMENTCO=(PF*-.227)+(RP*-.102)+(P*-.130)+(GHP*.036)+(EV*.278)+(SF*.272)+(RE*.329)+(MH*.460)`; `PCS=(((AGPHYSCO-82.261)/20.867)*10)+50`; `MCS=(((AGMENTCO-63.7796)/19.582)*10)+50` (pp. 16-17). The source spells the pain term in AGPHYSCO as `Pa`, unlike the defined `P`; preserve this exact source label for checking.
- EQ-5D-5L is mapped to the EQ-5D-3L value set; index value 0 is imputed for death before questionnaire. Index range -0.285 worst to 1 best; VAS range 0 worst to 100 best (pp. 17, 19, 36).
- AFEQT scoring excludes the final two questions, which are separately tabulated; overall range 0 complete disability to 100 no disability (pp. 17, 19). IPAQ total MET-minutes/week is `MET level * minutes/day * days/week`; total is walking `3.3*minutes*days` + moderate `4.0*minutes*days` + vigorous `8.0*minutes*days` (p. 17).
- NT-pro-BNP is naturally log transformed before analysis. Exponentiated model effect is a geometric-mean ratio; below 1 favours Digoxin (pp. 17, 21, 40). Source alternates `BNP`, `NTpro-BNP`, and `NTproBNP`; p. 40 labels units ng/L whereas baseline template p. 30 labels NTproBNP pg/mL.
- Diastolic dysfunction: present if average E/e' >=15, or if at least two of IVRT <=65 ms, mitral E deceleration <=120 ms, average E/e' >=11, pulmonary-vein diastolic deceleration <=220; otherwise absent (p. 17). This is a binary yes/no outcome.
- EHRA ordinal classes are 1, 2a, 2b, 3, 4 (best to worst); binary improvement is a two-category worse-to-better change, separately baseline-to-6 and baseline-to-12 months. Participants with baseline 2a or below cannot achieve the threshold and are classed not improved (p. 18).
- Other printed units: LVEF percent of volume ejected and strata <40%, 40-49%, >=50% (pp. 19-20, 30, 37); E/e' ratio (p. 20); heart rate bpm (pp. 20, 30, 38); walk time min/s and distance metres (pp. 20, 39); baseline NTproBNP pg/mL (p. 30); digoxin level ug/L (p. 44); maximal pause duration seconds (p. 44).

## Planned result presentations and inferential definitions

- Primary PCS: arm n, mean [SD], min-max at baseline/6 months; linear regression of 6-month PCS on baseline PCS, arm, minimisation variables, age and baseline LVEF. Report adjusted mean difference, 95% CI and P value. Positive difference favours Digoxin because Bisoprolol is reference (pp. 18, 33).
- SF-36 global/domain scores, EQ-5D index/VAS, AFEQT, continuous LVEF, E/e', heart-rate measures, and walk distance use the primary linear-regression approach at their stated follow-up times (pp. 18-20, 34-39). LVEF higher is better; E/e' lower is better; positive mean difference is stated as favourable for Digoxin for most continuous templates, requiring direction matching for E/e' (pp. 20, 37).
- PCS repeated-measures secondary model: treatment, minimisation variables, age, baseline LVEF and time in days; initially constant treatment effect; add treatment-by-time interaction, use time-specific estimates if interaction P<0.05; unstructured covariance; adjusted mean differences and 95% CIs (p. 19).
- Diastolic-index composite: logistic regression of 12-month binary category on baseline category, treatment and standard covariates; adjusted odds ratio/95% CI (p. 20; template p. 37).
- EHRA: ordinal logistic model at 6/12 months, outcome class 1 reference, with baseline EHRA, treatment, sex, age and baseline LVEF; higher OR means worse Digoxin outcome. Binary two-class-improvement logistic model uses yes as outcome/reference, treatment, sex, age and LVEF; higher OR means better Digoxin outcome (pp. 21, 40).
- Feasibility outcomes receive summary statistics only, not formal model-based inference (p. 22); templates include recruitment target 3 participants/week, losses/dropouts, adherence, discontinuation, pacemaker, SDs/proportions, hospitalisation rates and cardiovascular events (pp. 21-22, 41-42).
- Safety template: arm and total number/percent of patients plus event counts, a chi-square test for patients with >=1 AE and P-value placeholder; SAE table includes 0/1/2/... SAE counts and total SAE count (p. 43). Safety/planned results are blank.
- Subgroups, primary PCS only: sex, modified EHRA, beta-blocker within one month, age <75/>=75, and LVEF <50/>=50, evaluated by treatment-by-subgroup interaction (pp. 22, 45). Sensitivities: per-protocol; additionally adjust baseline apical heart rate; exclude PCS questionnaires outside +/-4 weeks; multiple imputation with 50 imputations for missing 6-month PCS using treatment, sex, EHRA, baseline PCS and other relevant baseline data, combined with Stata `mi estimate` (p. 23).

## Candidate potential requiring later cross-source/numeric review (no C ID assigned)

1. **SUPP03-POT-01 — AFEQT template footnote label:** PDF p. 36 says the AFEQT £ footnote gives the range for the “visual analogue score” (0-100), whereas the planned outcome is AFEQT overall score (pp. 17, 19, 36). Numeric range matches AFEQT but the measure label may be copied from VAS; compare only after matching the main-paper AFEQT result.
2. **SUPP03-POT-02 — E/e' direction label:** PDF p. 20 states lower E/e' is better, but PDF p. 37 template says higher values/positive mean difference favour Digoxin in its E/e' section. The values are not populated; this is a pre-specified label-direction conflict requiring source/result matching.
3. **SUPP03-POT-03 — NT-pro-BNP time/label/unit consistency:** p. 40 heading says “at 6 months” but template has baseline, 6- and 12-month rows; pp. 7 and 21 specify 6 and 12 months. It also uses ng/L while p. 30 labels baseline NTproBNP pg/mL. No observed values are printed; preserve for cross-document/unit matching.
4. **SUPP03-POT-04 — EHRA illustrative category:** p. 18 defines categories 1, 2a, 2b, 3, 4, then illustrates baseline “3a” to 2a as two-category improvement. The example label is outside the printed category list; no result value is affected in this SAP template.
5. **SUPP03-POT-05 — 24-hour ambulatory heart-rate timing:** p. 20 says ambulatory rate is measured only once and has no baseline score to adjust; p. 38’s blank template places the ambulatory row under “Baseline.” The schedule and reported-results source are needed before concluding the intended time point.

## Limitations

- This assigned source ends at PDF p. 45 and contains no filled outcome table, forest plot, flow total, inferential estimate, or P value other than assumptions/placeholders. It therefore cannot by itself establish a reported-result inconsistency.
- The SAP does not give a single effective-date field beyond cover signatures; it is administrative context, not an observed result.
