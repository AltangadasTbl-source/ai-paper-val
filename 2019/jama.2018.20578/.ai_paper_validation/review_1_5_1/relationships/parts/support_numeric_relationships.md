# Support Numeric Relationship Inventory Part

All records are source mappings, not candidate determinations. PDF pages below are direct-source locations.

## SN001 — Protocol population, outcome, extraction, and sensitivity definitions

- **Source:** DOC-002 `joi180151supp1_prod.pdf` pp. 2-7.
- **Relationship:** Aspirin any dose versus placebo/no aspirin in persons without cardiovascular disease. The primary composite is cardiovascular mortality + non-fatal MI + non-fatal stroke. Extract raw events, RR/HR, 95% CI, and P values; sensitivity exclusions are open-label, >100 mg/day, and pre-2000 studies, plus later protocol changes for asymptomatic-PVD/ABPI and ASCEND primary composite.
- **Rule/labels:** ARD = placebo risk - (RR x placebo risk), per the printed prose; negative favors aspirin and positive favors no aspirin. Follow-up criterion >=12 months; sample-size criterion >1,000; BMI obesity label >=30.

## SN002 — DIC, I2, and selected Bayesian model matrix

- **Source:** DOC-003 pp. 5-6; `I2` is fixed-effect I2.
- **Rule:** lowest DIC selected; if DIC difference <=3, random selected if I2 >25%.
- **All patients:** composite 19.38/21.24/I2 0/fixed; ACM 14.28/16.27/0/fixed; CVM 24.56/26.53/0/fixed; MI 48.96/38.72/42/random; total stroke 30.13/31.30/1/fixed; ischaemic stroke 25.81/25.72/18/fixed; major bleeding 27.17/28.48/0/fixed; intracranial 25.40/27.24/0/fixed; major GI 28.46/29.74/0/fixed; incident cancer 27.06/27.93/25/random; cancer mortality 29.66/29.25/17/fixed.
- **Low risk:** composite 8.04/9.81/0/fixed; ACM 7.47/8.93/0/fixed; CVM 9.15/10.55/0/fixed; MI 15.68/14.81/32/random; total stroke 17.22/16.97/26/random; ischaemic 14.45/13.75/33/random; major bleeding 11.88/13.46/11/fixed; intracranial 11.45/13.00/0/fixed; major GI 13.81/15.15/9/fixed; incident cancer 11.45/11.03/41/random; cancer mortality 13.30/11.53/42/random.
- **High risk:** composite 12.71/14.05/0/fixed; ACM 8.79/10.02/0/fixed; CVM 16.69/18.68/14/fixed; MI 26.93/26.03/26/random; total stroke 18.33/19.38/11/fixed; ischaemic 16.93/18.25/8/fixed; major bleeding 17.14/17.39/10/fixed; intracranial 15.05/16.28/0/fixed; major GI 16.61/16.80/15/fixed; incident cancer 14.23/15.52/3/fixed; cancer mortality 14.74/16.33/0/fixed.
- **Diabetes:** composite 12.47/14.06/0/fixed; ACM 7.50/8.74/0/fixed; CVM 10.15/10.34/51/random; MI 26.40/27.29/13/fixed; total stroke 20.79/21.49/13/fixed; ischaemic 8.65/6.41/77/random; major bleeding 6.06/7.02/0/fixed; intracranial 6.03/6.20/1/fixed; major GI 6.06/6.25/1/fixed; incident cancer 6.55/6.98/34/random; cancer mortality 8.57/8.90/39/random. Entries are fixed DIC/random DIC/I2/model.

## SN003 — eTable 3 ARD and NNT/NNH

- **Source:** DOC-003 p. 15. ARD values and intervals are percentage-point presentation; NNT/NNH printed only for statistically significant ARD.
- **Efficacy, all/low/high/diabetes:** composite -0.41 (-0.59,-0.23),242 / -0.34 (-0.52,-0.14),297 / -0.63 (-1.04,-0.18),160 / -0.65 (-1.17,-0.09),153; ACM -0.13 (-0.32,0.07) / -0.01 (-0.27,0.27) / -0.43 (-0.84,0.02) / -0.24 (-0.91,0.49); CVM -0.07 (-0.17,0.04) / -0.07 (-0.16,0.03) / -0.04 (-0.32,0.27) / -0.05 (-0.94,1.27); MI -0.28 (-0.47,-0.05),361 / -0.27 (-0.49,0.00),366 / -0.32 (-0.74,0.16) / -0.26 (-0.88,0.47); all stroke -0.09 (-0.20,0.04) / -0.04 (-0.21,0.14) / -0.19 (-0.49,0.16) / -0.77 (-1.48,0.16); ischaemic -0.19 (-0.30,-0.06),540 / -0.16 (-0.29,-0.02),623 / -0.28 (-0.63,0.12) / -0.83 (-1.70,0.50); incident cancer 0.03 (-0.37,0.46) / 0.41 (-0.13,1.01) / -0.30 (-0.76,0.19) / -0.68 (-2.09,0.95); cancer mortality 0.05 (-0.11,0.23) / 0.16 (-0.06,0.42) / -0.13 (-0.41,0.17) / 0.16 (-0.56,1.02).
- **Safety, all/low/high/diabetes:** major bleeding 0.47 (0.34,0.62),210 / 0.40 (0.25,0.57),249 / 0.64 (0.35,0.97),152 / 0.80 (0.29,1.39),121; intracranial 0.11 (0.04,0.18),927 / 0.13 (0.05,0.22),796 / 0.07 (-0.04,0.21) / 0.12 (-0.09,0.43); major GI 0.30 (0.20,0.41),334 / 0.27 (0.15,0.40),376 / 0.39 (0.16,0.69),255 / 0.41 (0.06,0.86),243.

## SN004 — eTable 4 total-stroke counts, totals, and subgroup estimates

- **Source:** DOC-003 p. 16. All: 12 studies; aspirin 1,116/73,883, no aspirin 1,136/72,317; ARR 0.10 (-0.03,0.22); HR 0.93 (0.86,1.02); I2=1. Low: 6; 752/56,212 vs 788/56,354; ARR 0.04 (-0.15,0.20); HR 0.95 (0.79,1.16); I2=6. High: 7; 381/17,671 vs 380/15,963; ARR 0.22 (-0.07,0.49); HR 0.89 (0.77,1.03); I2=11. Diabetes: 7; 128/4,048 vs 156/3,960; ARR 0.50 (-0.05,0.97); HR 0.78 (0.61,1.00); I2=13; displayed upper bound is 1.004.

## SN005 — eTable 5 event-rate matrix

- **Source:** DOC-003 p. 17. Unit: events per 10,000 participant-years. Entries are aspirin/no aspirin for all, low risk, high risk, diabetes respectively.
- Composite 60.2/65.2, 41.3/46.4, 109.2/117.9, 103.6/114.1; ACM 69.4/70.0, 50.5/50.4, 118.5/124.9, 134.2/137.6; CVM 19.1/19.5, 10.7/11.9, 40.7/40.7, 38.3/40.4; MI 28.1/31.2, 17.2/21.0, 56.5/59.8, 59.8/62.6; total stroke 24.0/25.0, 19.9/20.9, 41.5/44.9, 59.0/74.2; ischaemic stroke 18.4/21.4, 14.7/17.1, 30.8/36.9, 40.3/46.7; cancer incidence 105.4/105.5, 97.7/93.8, 121.8/132.4, 162.7/166.2; cancer mortality 31.2/30.1, 23.8/21.6, 48.8/51.9, 61.9/60.9; major bleeding 23.1/16.4, 19.2/13.4, 37.7/28.3, 54.7/42.4; intracranial 6.7/5.1, 6.5/4.6, 7.4/6.3, 10.0/8.3; major GI 12.9/8.2, 10.5/6.7, 19.5/12.6, 22.6/16.7.

## SN006 — Sensitivity-analysis size and displayed estimates

- **Source:** DOC-003 p. 18. Columns: <=100 mg/day (11 studies, N=134,470); double-blind/placebo (9, N=135,043); since 2000 (9, N=113,140); excluding asymptomatic PAD (11, N=156,874). All entries HR (95% CrI): composite 0.89 (0.83,0.95) / 0.88 (0.83,0.94) / 0.91 (0.84,0.98) / 0.88 (0.83,0.93); ACM 0.95 (0.87,1.03) / 0.96 (0.88,1.03) / 0.94 (0.85,1.04) / 0.94 (0.88,1.01); CVM 0.91 (0.80,1.05) / 0.96 (0.84,1.09) / 0.88 (0.73,1.06) / 0.92 (0.82,1.04); MI 0.87 (0.76,1.00; upper 0.9989) / 0.84 (0.70,1.03) / 0.94 (0.81,1.08) / 0.80 (0.68,0.95); total stroke 0.90 (0.82,0.98) / 0.93 (0.84,1.02) / 0.89 (0.80,0.98) / 0.95 (0.87,1.03); ischaemic stroke 0.79 (0.74,0.85) / 0.85 (0.69,1.06) / 0.80 (0.74,0.86) / 0.81 (0.76,0.87); major bleeding 1.43 (1.30,1.57) / 1.41 (1.28,1.55) / 1.39 (1.26,1.53) / 1.42 (1.30,1.56); intracranial 1.31 (1.11,1.56) / 1.33 (1.11,1.60) / 1.34 (1.13,1.60) / 1.33 (1.13,1.57); major GI 1.55 (1.36,1.77) / 1.54 (1.35,1.76) / 1.48 (1.28,1.71) / 1.57 (1.38,1.79); incident cancer 1.01 (0.92,1.08) / 0.99 (0.89,1.06) / 1.01 (0.91,1.10) / 1.02 (0.98,1.07); cancer mortality 1.04 (0.96,1.12) / 1.03 (0.95,1.12) / 1.04 (0.96,1.12) / 1.05 (0.97,1.13).

## SN007 — Study-flow and risk-of-bias summary figures

- **Source:** DOC-003 pp. 19-20. Study flow: 1,385 identified = 668 Embase + 717 Medline; 235 duplicates; 1,150 screened; exclusions 1,131 = 605+244+147+60+45+13+10+7; 2 meta-analysis articles; 21 publications / 13 trials. Risk-of-bias figure: 13 assessments per domain; overall 9 low and 4 high; reporting/attrition/sequence each 13 low; detection 9 low/4 unclear; blinding 9 low/4 high; allocation 10 low/3 unclear.

## SN008 — Forest-plot source unit and comparison note

- **Source:** DOC-003 pp. 22-26. Complete individual trial event/total/RR/CI/weight rows are displayed in eFigure 4; outcome-level summaries are in SS006. Experimental=aspirin; control=no aspirin; RR and 95% CI.
- **Neutral mapper comparison:** eTable 4 p.16 total-stroke totals are 73,883/72,317 from 12 studies; eFigure 4 p.24 total-stroke totals are 81,623/80,057 from 13 displayed rows. The difference is ASCEND’s 7,740 participants in each arm; eTable 1 p.9 labels ASCEND all stroke not included because only ischaemic stroke is reported. No candidate determination is made in this mapping part.
