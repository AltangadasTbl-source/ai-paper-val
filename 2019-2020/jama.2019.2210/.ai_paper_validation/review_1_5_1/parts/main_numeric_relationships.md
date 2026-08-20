# Main Numeric Relationship Part — DOC-001

This part inventories local numeric relationships `MN01`-`MN33` from `extraction/main_quantitative_evidence.md`. They are complete for main-article PDF pp. 1-9 and are provisional local keys only.

| Key | Relationship type | Exact direct PDF locations | Compact relationship record | Cross-document match key |
|---|---|---|---|---|
| MN01 | trial population/time | pp. 1-2 | Digestive-tract stage I-III, age 30-90, 2010-2018 trial context. | XMAIN-TRIAL-POPULATION |
| MN02 | total/assignment | pp. 1-2,4 | 251 vitamin D + 166 placebo = 417 randomized; 3:2 allocation. | XMAIN-ASSIGNMENT-251-166 |
| MN03 | outcome definitions | pp. 1-2 | RFS and OS are randomization-origin time-to-event outcomes; safety distinct. | XMAIN-OUTCOME-DEFINITIONS |
| MN04 | analysis populations | pp. 1,3 | ITT randomized population for efficacy; per-protocol for adverse events. | XMAIN-ITT-417 / XMAIN-SAFETY-PER-PROTOCOL |
| MN05 | planning quantities | p. 3 | 75% vs 62%, alpha .05, 80% power, 1% loss, N=400, 3:2, 5+2 years. | XMAIN-SAMPLE-SIZE |
| MN06 | subgroup definitions | p. 3 | <20, 20-40, >40 ng/mL; interaction low vs middle only. | XMAIN-25OHD-LOW-MIDDLE |
| MN07 | analysis settings | p. 3 | Interim after 200; P<.001; 50 imputations; specified post hoc methods. | XMAIN-ANALYSIS-SETTINGS |
| MN08 | flow reconciliation | pp. 1,4 | 439-22=417; 22=15+5+2; abstract 15+7=22. | XMAIN-FLOW-439-22-417 |
| MN09 | allocation totals | p. 4 | 251 + 166 = 417; 60%/40%. | XMAIN-ITT-417 |
| MN10 | discontinuation totals | p. 4 | Figure: 23=14+9 and 19=10+9, plus 1 separately lost. Narrative includes that loss among 15 vitamin-D nonmedical stops: 15+10+9+9=43; 43/417=10.31% -> 10.3%. | XMAIN-MEDICATION-STOPPING |
| MN11 | follow-up | pp. 1,4 | 1 lost; 416/417=99.76% -> 99.8%; arm median/IQR/max values mapped. | XMAIN-FOLLOWUP-99.8 |
| MN12 | sex/age/BMI | pp. 1,4-5 | Men 276/417=66.19%, women 141/417=33.81%; mean versus median age distinguished. | XMAIN-SEX-276-417 |
| MN13 | site distribution | pp. 4-5 | Sites total 40+174+2+201=417; shares 9.6/41.7/0.5/48.2%. | XMAIN-SITE-DISTRIBUTION |
| MN14 | stage distribution | pp. 4-5 | Stage totals 182+111+124=417; rounded 44/26/30%. | XMAIN-STAGE-DISTRIBUTION |
| MN15 | age/BMI categories | p. 5 | Age categories total 251/166; BMI categories total 249/165 without a missingness note (C007). | XMAIN-AGE-BMI-QUARTILES |
| MN16 | baseline comorbidity | p. 5 | Nonexclusive counts at n=251/166; no summation identity expected. | XMAIN-BASELINE-COMORBIDITIES |
| MN17 | pathology | p. 5 | 226+22+3=251; 147+16+3=166; other=4+1+1. | XMAIN-PATHOLOGY |
| MN18 | baseline 25(OH)D denominators | pp. 4-6 | 173+232+5=410; 417-410=7 missing; arm totals 248/162. | XMAIN-25OHD-DENOMINATOR-410 |
| MN19 | SNP denominators | p. 5 | All genotype triplets total below arm n with variable totals: 245/157, 231/150, 230/150, 231/150, 231/150, 231/148, and 231/150; no available-case/missingness footnote (C001). | XMAIN-SNP-GENOTYPE-DENOMINATORS |
| MN20 | composite/death counts | pp. 1,4 | RFS composite 50/251=20%, 43/166=26%; death 37/251=15%,25/166=15%. | XMAIN-PRIMARY-EVENTS-50-43; XMAIN-DEATHS-37-25 |
| MN21 | event components | p. 4 | Death components 27+10=37, 16+9=25; composite not additive with relapse/death components. | XMAIN-EVENT-COMPONENTS |
| MN22 | 5-y RFS and risks sets | pp. 1-2,4,6 | 77% vs 69%, with Figure 2A at-risk sequence mapped. | XMAIN-RFS5-77-69 |
| MN23 | 5-y OS and risk sets | pp. 1,4,6 | 82% vs 81%, with Figure 2B at-risk sequence mapped. | XMAIN-OS5-82-81 |
| MN24 | subgroup biochemical values | p. 4 | Middle 26.5->45; low 16->36 ng/mL, including IQRs. | XMAIN-25OHD-SUBGROUP-CHANGE |
| MN25 | post hoc biochemical values | p. 6 | 25(OH)D and calcium medians/IQRs/change ratios, with distinct units. | XMAIN-25OHD-CHANGE-21-41; XMAIN-CALCIUM-CHANGE-9.3 |
| MN26 | safety, per-protocol censoring | pp. 6,8 | n=227/147 and four safety outcome count/percentage pairs. | XMAIN-SAFETY-CENSORING-227-147 |
| MN27 | safety, 1-y adherence | p. 8 | n=243/160 and four safety outcome pairs. | XMAIN-SAFETY-1YEAR-243-160 |
| MN28 | safety, randomization group | p. 8 | n=251/166 and four safety outcome pairs/definitions. | XMAIN-SAFETY-RANDOMIZED-251-166 |
| MN29 | abstract safety repetition | pp. 1,8 | Abstract uses the per-protocol-until-censoring 3/5 fracture and 2/0 stone values. | XMAIN-ABSTRACT-SAFETY-PER-PROTOCOL |
| MN30 | assay/interims | pp. 3-4 | 19 blinded duplicate samples, correlation 0.92; 3 actual interim analyses. | XMAIN-ASSAY-CORRELATION-0.92; XMAIN-THREE-INTERIMS |
| MN31 | Figure 2 observation time | p. 6 | Outcome/model-specific median observation-time IQRs for placebo and vitamin D. | XMAIN-FIG2-OBSERVATION-TIMES |
| MN32 | Figure 3 risk sets | p. 7 | All four panel at-risk sequences; panel C visibly has a row although its footnote says no panel-C numbers are given because of weighting. | XMAIN-FIG3-RISK-SETS |
| MN33 | Figure 3 observation time | p. 7 | Subgroup/outcome-specific median observation-time IQRs. | XMAIN-FIG3-OBSERVATION-TIMES |

**No-applicable record:** DOC-001 PDF p. 9 contains no result-relevant numeric relationship.
