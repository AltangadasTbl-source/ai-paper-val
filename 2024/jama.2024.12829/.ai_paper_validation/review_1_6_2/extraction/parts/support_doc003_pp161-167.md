# DOC-003 support evidence map, PDF pages 161–167

Source `joi240088supp2_prod_1746815064.36071.pdf`; role PLAN, final SAP tail and version-revision table. Exactly seven pages opened and mapped. Reused pagewise native/layout extraction supplies all text; no image-only quantitative unit in this shard and no OCR needed. Engine: legacy PDF native/layout; exact version unavailable. No source or reused derivative is modified. The source remains final authority. Source-specific keys are retained for subsequent global N/S assignment.

| PDF page | Key | Mapped scope and no-applicable records | Main-paper matching key |
|---|---|---|---|
|161|D003-P161|Secondary outcome analysis definitions; full numerical windows and measures below|Secondary stroke, mRS, restenosis, EQ-5D|
|162|D003-P162|Completion of EQ-5D method, safety and medication analysis|Safety S11, concomitant medication|
|163|D003-P163|Medication test methods continued; bibliographic references otherwise no applicable trial result|Medication comparisons|
|164|D003-P164|Reference continuation, line numbers/whitespace; no applicable trial quantitative relationship|None|
|165|D003-P165|SAP v1→v2 revision table: interim rules, original/final sample-size assumptions|Sample size, power, interim analysis|
|166|D003-P166|Revision table continuation completing sample-size derivations|Sample size, power, alpha/dropout|
|167|D003-P167|Printed line numbers2872–2913 only; no applicable quantitative relationship|None|

## Complete planned quantitative relationships

D003-P161, lines2775–2797: page starts with continuation of prior-page endpoint: after enrollment or after BA procedure of qualifying lesion during follow-up; Cox proportional hazards, HR95%CI. The prior page supplies the beginning of the endpoint and is mapped in the adjacent part; no standalone endpoint is invented here. Any ischemic/hemorrhagic stroke inside target-artery territory or all-cause deaths at90d/12m/24m/36m: Cox, HR95%CI. Stroke outside target territory at90d/12m/24m/36m: Cox, HR95%CI. Composite stroke/MI/vascular death at12m/24m/36m: Cox, HR95%CI. mRS at90d/12m/24m/36m: ordinal logistic, common OR. Target-artery restenosis within12m: logistic regression between groups, OR95%CI; stenosis>70% or increased by30% on follow-up neurovascular imaging. Quality of life EQ-5D within12m: Student t test or Wilcoxon rank sum as appropriate, continued on162.

D003-P162, lines2798–2819: EQ-5D Wilcoxon rank sum completes161. Safety AEs coded MedDRA version26 or later, grouped by system organ class and preferred term; group numbers and percentages of subjects, Fisher exact comparison of number of each grouped AE event. Deaths/SAEs summary listings plus case narratives; number of deaths during treatment summarized and compared by Fisher exact. Vital signs at different timepoints statistically described and compared with no named test here. Concomitant medication list antiplatelet aspirin/clopidogrel/ticagrelor/cilostazol, anticoagulation, lipid-lowering statins; continuation163.

D003-P163, lines2820–2823: antihypertensive list diuretic, ACE inhibitor, ARB, beta blocker, calcium antagonist, central α agonist, vasodilator; chi-square or Fisher exact to compare numbers between groups. Lines2825 onward references only; no historical publication numeric statement is converted into a BASIS trial result. D003-P164 finishes reference4 and blank numbered lines.

### D003-P165/P166 revision table, lines2871 onward

| Element | SAP version1.0 printed column | SAP version2.0 printed column |
|---|---|---|
| Interim analysis | When half of patients completed12-month visit; midterm α1=.0015 and final α2=.024 | No interim analyses; independent statistician summarizes enrollment/status/baseline/safety including coded SAEs for DSMB at regular intervals; DSMB can recommend modification/stopping for safety; steering/sponsor decide |
| Planning source | 1-year SAMMPRIS results, target-vessel stroke or death12.2% within12m | VISSIT and prior China randomized trial; medical primary composite anticipated15%; angioplasty7% based on angioplasty-without-stent studies and clinical experience |
| Effect assumption | 50% relative reduction, 6.1% | Absolute difference8% |
| Initial N/power/alpha | 686 cases;80% power; two-sided α=.05 | Total512,256/group;80% power; one-sided α2.5%;10% dropout |
| Interim inflation | O'Brien-Fleming spending stated to lead to6% expansion of total type I error; SAS increases N to728 | No interim analysis inflation specified |
| Dropout/final N |10% lost follow-up, final802|10% dropout incorporated in512|

Version changes are explicitly disclosed by this table; values are transcribed, not reconciled or diagnosed by this mapper. Final primary outcome definition is elsewhere in final SAP and should be matched to the primary composite reported in main article and DOC-002 S6/S8/S9.

## Complete pagewise source-linked layout appendix

### DOC-003 PDF page 161

[Source page](../../../../joi240088supp2_prod_1746815064.36071.pdf#page=161)

```text
       BASIS                                                                Number:2017YFC1307900



2775           after enrollment or after balloon angioplasty procedure of the qualifying lesion

2776           during follow-up will be analyzed using a Cox proportional hazard model and

2777           report the hazard ratios with 95% CIs;

2778          Any stroke (ischemic or hemorrhage stroke) inside of the territory of the target

2779           artery or all-cause deaths (within 90 days, 12 months, 24 months and 36 months

2780           after enrollment) will be analyzed using a Cox proportional hazard model. The

2781           hazard ratios with 95% CIs will be reported;

2782          Any stroke (ischemic or hemorrhage stroke) outside of the territory of the target

2783           artery (within 90 days, 12 months, 24 months and 36 months after enrollment)

2784           will be analyzed using a Cox proportional hazard model. The hazard ratios with

2785           95% CIs will be reported;

2786          Combined events such as stroke, myocardial infarction, and vascular death

2787           (within 12 months, 24 months and 36 months after enrollment) will be analyzed

2788           using a Cox proportional hazard model. The hazard ratios with 95% CIs will be

2789           reported.

2790          Common odds ratios of mRS (at 90 days, 12 months, 24 months and 36 months)

2791           will be estimated using ordinal logistic regression.

2792          Logistic regression analysis will be performed to compare the restenosis rate of

2793           the target artery within 12 months (defined as rate of stenosis >70% or increased

2794           by 30% based on following-up neurovascular imaging) between the two treatment

2795           groups and the odds ratio with 95% CI will be reported.

2796          Life quality assessment (EuroQol-5-Dimensions Scale [EQ-5D] questionnaire)

2797           within 12 months after enrollment will be tested using student t-test or Wilcoxon



                                                    161

```

### DOC-003 PDF page 162

[Source page](../../../../joi240088supp2_prod_1746815064.36071.pdf#page=162)

```text
       BASIS                                                                Number:2017YFC1307900



2798             rank sum test as appropriate.

2799   12.4 Safety Analyses

2800   Adverse Events

2801   Adverse events (AEs) will be coded using the MedDRA coding dictionary (Version 26 or

2802   a later release) and grouped by system organ class. Separate data display listings and

2803   summaries will be presented for adverse events. Within each treatment group, the number

2804   and percentage of subjects experiencing an AE will be summarized by system organ class

2805   and preferred term and Fisher’s Exact test will be used to compare the number of each

2806   grouped AE event between treatment groups.

2807   Deaths and Serious Adverse Events

2808   Summary tables and data displays will be provided for serious adverse events (as detailed

2809   in the study protocol). In addition, all deaths and serious AE's will be documented in a

2810   case narrative format in the clinical study report.

2811   The number of deaths occurring over the treatment period will be summarized and

2812   Fisher’s Exact test will be used to compare the number of deaths between treatment

2813   groups.

2814   Vital Signs

2815   The results of vital signs at different time points will be statistically described and

2816   compared.

2817   12.5 Concomitant Medication

2818   Describe the list of concomitant medication including antiplatelet drug (sspirin,

2819   clopidogrel, ticagrelor, cilostazol), anticoagulation drug, lipid-lowering drug (statin),


                                                    162

```

### DOC-003 PDF page 163

[Source page](../../../../joi240088supp2_prod_1746815064.36071.pdf#page=163)

```text
       BASIS                                                                  Number:2017YFC1307900



2820   antihypertensive drugs (diuretic, angiotensin-converting enzyme inhibitor, angiotensin

2821   receptor blocker, beta-blocker, calcium channel antagonist, central α agonist, vasodilator)

2822   and so on. The Chi-squared tests or Fisher exact test will be used to compare the number

2823   between treatment groups.

2824

2825   13. Reference

2826   1. Zaidat OO, Fitzsimmons BF, Woodward BK, Wang Z, Killer-Oberpfalzer M, Wakhloo

2827     A, Gupta R, Kirshner H, Megerian JT, Lesko J, et al. Effect of a balloon-expandable

2828     intracranial stent vs medical therapy on risk of stroke in patients with symptomatic

2829     intracranial stenosis: the VISSIT randomized clinical trial. Jama. 2015;313:1240-1248.

2830     doi: 10.1001/jama.2015.1693

2831   2. Stapleton CJ, Chen YF, Shallwani H, Vakharia K, Turan TN, Woo HH, Derdeyn CP,

2832     Charbel FT, Siddiqui AH, Amin-Hanjani S. Submaximal Angioplasty for

2833     Symptomatic      Intracranial   Atherosclerotic      Disease:   A    Meta-Analysis     of

2834     Peri-Procedural and       Long-Term Risk. Neurosurgery. 2020;86:755-762. doi:

2835     10.1093/neuros/nyz337

2836   3. Miao Z, Jiang L, Wu H, Bao Y, Jiao L, Li S, Wu J, Hua Y, Li Y, Zhu J, et al.

2837     Randomized controlled trial of symptomatic middle cerebral artery stenosis:

2838     endovascular     versus   medical    therapy    in   a   Chinese    population.   Stroke.

2839     2012;43:3284-3290. doi: 10.1161/strokeaha.112.662270

2840   4. Dumont TM, Kan P, Snyder KV, Hopkins LN, Siddiqui AH, Levy EI. Revisiting

2841     angioplasty without stenting for symptomatic intracranial atherosclerotic stenosis after

2842     the stenting and aggressive medical management for preventing recurrent stroke in


                                                   163

```

### DOC-003 PDF page 164

[Source page](../../../../joi240088supp2_prod_1746815064.36071.pdf#page=164)

```text
       BASIS                                                        Number:2017YFC1307900



2843     intracranial stenosis (SAMMPRIS) study. Neurosurgery. 2012;71:1103-1110. doi:

2844     10.1227/NEU.0b013e318271bcb8

2845

2846

2847

2848

2849

2850

2851

2852
2853
2854
2855
2856
2857
2858
2859
2860
2861
2862
2863
2864
2865
2866
2867
2868
2869
2870


                                            164

```

### DOC-003 PDF page 165

[Source page](../../../../joi240088supp2_prod_1746815064.36071.pdf#page=165)

```text
       BASIS                                                                     Number:2017YFC1307900



2871   Revisions to previous SAP version
       SAP version 1.0                                       Changes in SAP version 2.0
       5.3 Interim Analyses                                  5.3 Interim Analyses
       Interim analysis is performed when half of            Interim analyses will not be performed in this
       patients finished 12-months visit. The mid-term trial. However, a Data and Safety Monitoring
       analysis α1 is estimated to be 0.0015, and the        Board (DSMB) is in place to ensure the safety

       final analysis α2 is 0.024.                           of subjects in the study. An independent
                                                             statistician will prepare summary statistics on
                                                             enrollment, subject status in the study, baseline
                                                             characteristics, and safety data, including
                                                             summary tables of coded SAEs and these will
                                                             be examined by the DSMB. These tables will be
                                                             provided to the DSMB at regular intervals. If
                                                             the tables give rise to safety concerns for any
                                                             treatment, the DSMB may recommend that the
                                                             trial should be modified or stopped prematurely.
                                                             The Steering Committee will, in conjunction
                                                             with the Sponsor, decide whether to act on this
                                                             recommendation.
       6. Sample Size Estimates                              6. Sample Size Estimates
       The estimation of the sample size is calculated According to VISSIT trial and a previous
       according to      the   1-year   results   of    the randomized trial in China, the composite event
       SAMMPRIS trial, the incidence of target vessel rate of the primary outcome in the medical
       stroke or death rate was 12.2% within 12 group is anticipated to be 15%. As to the
       months after enrollment in the experimental balloon angioplasty group, we assume a 7% of
       group. The sample size was 686 cases, with a the primary outcome based on studies of
       80% power, two-sided α = 0.05, to detect a angioplasty without stenting and investigators’s
       50 % relative reduction (6.1%) after balloon clinical practice experience in China. As a
       angioplasty for intracranial atherosclerosis. It is result, the sample size required to detect an
       assumed that the O'Brien-Fleming spending absolute difference of 8%. A total of 512
       function will lead to 6% expansion of the total patients (256 per group) will be enrollled

                                                       165

```

### DOC-003 PDF page 166

[Source page](../../../../joi240088supp2_prod_1746815064.36071.pdf#page=166)

```text
BASIS                                                          Number:2017YFC1307900



type I error. The SAS software is used to considering an 80% statistical power at
calculate the sample size required for the one-sided α of 2.5% and a 10% dropout rate.
mid-term analysis, which increases the sample
size to the required 728 cases. Considering the
10% lost to follow-up rate, the final sample size
of this study is 802 cases.




                                            166

```

### DOC-003 PDF page 167

[Source page](../../../../joi240088supp2_prod_1746815064.36071.pdf#page=167)

```text
2872

2873
2874
2875
2876
2877
2878
2879
2880
2881
2882
2883
2884
2885
2886
2887
2888
2889
2890
2891
2892
2893
2894
2895
2896
2897
2898
2899
2900
2901
2902
2903
2904
2905
2906
2907
2908
2909
2910
2911
2912
2913

```
