# DOC-003 complete support quantitative map

Assigned scope: joi180136supp2_prod.pdf PDF pages 1–17, document role REPORT. This supplement reports individual baseline and interim results, safety, trial design and implemented Bayesian methods and simulation results; reproduction of material from a published protocol does not turn this results supplement into a prospective plan. No other direct source was inspected for this shard. Matching main-paper keys below are semantic join keys, not assertions about another document.

Tooling: reused native and layout text `.ai_paper_validation/review_1_5_2/preprocessing/{native_text,layout_text}/DOC-003.txt` and all 17 source-linked rendered page PNGs `rendered_pages/DOC-003-01.png` through `DOC-003-17.png`. The asset inventory establishes exact native/layout agreement with current pdftotext and full page-image coverage. Historical derivative engine/version is unrecorded. Visual inspection of pp.2–17 confirms graphical material and row/column alignment; p.1 is a contents page read in native/layout text. CPU device; no new OCR or derivative rendering required. No source or reused asset modified.

## Page coverage

| Source page | Content mapped | Status |
|---|---|---|
| 1 | Contents; no independent quantitative result | COMPLETE; NO_APPLICABLE_RESULT |
| 2 | eTable1 inclusion/exclusion; graphical table manually transcribed below | COMPLETE |
| 3 | eTable2 patient rows 1–19, all columns and IVR baseline values | COMPLETE |
| 4 | eTable2 patient rows 20–30 and family/gene footnotes | COMPLETE |
| 5 | eTable3 all 27 analyzed patients; means, intervals, probabilities, post-trial status, all footnotes | COMPLETE |
| 6 | eTable4 all 12 safety rows, both treatment columns | COMPLETE |
| 7 | eFigure1 design graphic and caption, all intervals, treatment/visit sequences, stopping flow | COMPLETE |
| 8 | eFigure2 density graphic and caption; N=27, four symptoms, threshold and all four probabilities | COMPLETE |
| 9 | eFigure3 patient7 event at 11 days and histology 40x; no comparative efficacy result | COMPLETE |
| 10 | eMethods1 individual interim WinBUGS code and definitions | COMPLETE |
| 11 | eMethods2 total-group hierarchical code and first parameter definitions | COMPLETE |
| 12 | eMethods2 remaining definitions and shared within-patient SD | COMPLETE |
| 13 | eMethods3 genotype hierarchical code, priors, data and effect formulas | COMPLETE |
| 14 | eMethods3 genotype coding, shared variances and probability definitions | COMPLETE |
| 15 | eMethods4 simulation assumptions and all six steps | COMPLETE |
| 16 | eMethods4 null simulation Tables1–2 and power-simulation methods | COMPLETE |
| 17 | eMethods4 effect simulation Tables3–4, power and bias results | COMPLETE |

All 17 units were reusable-backed and freshly mapped. Fresh-required extraction units: 0. Scientific gaps: 0. No workbook, formula cache, CSV or Office table is present in the assigned scope. No sensitivity-result display is present; genotype model and individual results are fully mapped, not assumed absent. The supplement contains no frequentist P-value column; printed posterior probabilities are retained as such.

## Relationship inventory

Every table cell, code line and parameter definition appears in the page-linked transcription below. Each relationship bundles the logically connected rows of one display; all rows are covered.

| ID | Exact location | Quantities / relationship / extraction key | Matching main-paper key |
|---|---|---|---|
| N301 | [p.2 eTable1](../../../../joi180136supp2_prod.pdf#page=2) | Eligibility: adult >=18; genotype-confirmed NDM; exclusion timing 5/3/2 days, cardiac QT >500ms or QRS >150msec; all eight exclusion items transcribed below | eligibility/NDM population |
| N302 | [p.3 eTable2 rows1–19](../../../../joi180136supp2_prod.pdf#page=3) | Patient-level age years, sex, genotype, mutation, prior treatment, comorbidity and baseline mean IVR stiffness/pain/weakness/tiredness. Every value and allele retained in transcription | baseline Table1; CLCN1/SCN4A; family clustering |
| N303 | [p.4 eTable2 rows20–30](../../../../joi180136supp2_prod.pdf#page=4) | Remaining baseline rows; families *=8,9,19; **=14,15,16; ***=24,25,26,27; IVR interactive voice response; chloride vs sodium gene definitions | baseline Table1; related patients |
| N304 | [p.5 eTable3](../../../../joi180136supp2_prod.pdf#page=5) | N=27: patient IDs1,2,4,5,8–30; 3,6,7 dropped out; four patients with two sets, 23 with one. All 27 effect/95%CrI/posterior-probability/interim-index/post-trial rows retained | individual responder results; Figure individual effects |
| N305 | [p.6 eTable4](../../../../joi180136supp2_prod.pdf#page=6) | Mexiletine/placebo No.(%): GI21(70)/1(3); tremor2(7)/0(0); palpitations2(7)/0(0); headache1(3)/1(3); insomnia1(3)/0(0); any27(90)/2(6); >1 reactions2(7)/0(0); >2 reactions0(0)/0(0); withdrawal1(3)/0(0); dose reduction3(10)/0(0); extra therapy2(7)/0(0); serious allergic skin reaction1(3)/0(0). Table itself does not state denominator | safety/adverse-event results |
| N306 | [p.7 eFigure1](../../../../joi180136supp2_prod.pdf#page=7) | Individual design1–4 sets, 11weeks each; period4weeks; total11–44weeks; visits1–16. Actual four two-set patients1,2,4,5; other23 one set | design; flow; treatment sets |
| N307 | [p.8 eFigure2](../../../../joi180136supp2_prod.pdf#page=8) | Total NDM N=27; AUC to right of0.75: stiffness100%, pain45%, weakness87%, tiredness74%; x-axis placebo-minus-mexiletine mean IVR effect | Bayesian total-group symptom probabilities |
| N308 | [p.9 eFigure3](../../../../joi180136supp2_prod.pdf#page=9) | Patient7 generalized erythematous papules after11 days mexiletine; skin histology hematoxylin-eosin40x; photographic panels A/B, no efficacy estimate/interval | serious adverse reaction; withdrawal |
| N309 | [p.16 Tables1–2](../../../../joi180136supp2_prod.pdf#page=16) | Null simulations1000; all six variables each have1000 valid,0 missing; mean_sets mean3.41; diff mean0.07; type I positive count0/1000,0.00. Full mean/median/SD/min/max/25th/50th/75th rows retained | sample size simulation; type I rate |
| N310 | [p.17 Tables3–4](../../../../joi180136supp2_prod.pdf#page=17) | Fixed1.75 effect simulations1000; mean_sets2.59; mean effect1.29; bias1.29−1.75=−0.46; positive685/1000,68.5%, negative315/1000,31.5%; all descriptive cells retained | sample size/power assumptions |
| S301 | [p.5 eTable3 and footnote](../../../../joi180136supp2_prod.pdf#page=5) | Primary IVR-stiffness mean effect, 95%credible interval, posterior Pr(effect>0.75). Predefined responder Pr>0.80, nonresponder Pr<0.20; printed patient11 exception: posterior38%, mean0.00, CrI−12.24;12.16, data distribution0(CI0;0), absent stiffness both periods, prior influence and stopped after1 set; all other row evidence retained | interim stopping/individual response |
| S302 | [p.7 design](../../../../joi180136supp2_prod.pdf#page=7) | End-of-set interim1–4; enough evidence=yes stops, no continues through next set; fourth set always stops. Figure order M/P, P/M, M/P, P/M, with washout between arms | flexible N-of-1 stopping design |
| S303 | [p.8 posterior density](../../../../joi180136supp2_prod.pdf#page=8) | Probability density not a P-value; improvement positive placebo−mexiletine. Dotted vertical0.75; AUC beyond threshold gives symptom-specific percentages | primary/secondary Bayesian symptoms |
| S304 | [p.10 eMethods1](../../../../joi180136supp2_prod.pdf#page=10) | Individual observations separately normal by treatment; loops1:30 both arms. Mean priors dnorm(0,0.001); arm-specific sigma~dunif(0.01,10), tau=1/sigma². diff=mu_plac−mu_mex; p1=step(diff),p2=step(diff−0.75),p3=step(diff−2). Printed maximum30 measurements/treatment period | individual interim model/priors/thresholds |
| S305 | [pp.11–12 eMethods2](../../../../joi180136supp2_prod.pdf#page=11) | Hierarchical group model, patient means normal around arm population means with arm-specific tau; observation loops to actual N_plac[i],N_mex[i] with common tau.within. Group mean priors dnorm(4,0.001); within/mex/plac sigma each dunif(0.01,10). Group diff=mu.plac−mu.mex; p1/p2/p3 thresholds0/.75/2. Shared SD across arms. Exact code and printed descriptions retained separately below | total-group hierarchical model and priors |
| S306 | [pp.13–14 eMethods3](../../../../joi180136supp2_prod.pdf#page=13) | Gen_Pat1=CLCN1,0=SCN4A. mu_gen.mex=a+b*G; mu_gen.plac=c+d*G; a,b,c,d each dnorm(0,0.01). arm-specific between-patient SD common across genotypes; within SD same arms/genotypes; all sigma dunif(.01,10). SCN4A means a,c and effect c−a; CLCN1 means a+b,c+d and effect(c+d)−(a+b). Genotype posterior step thresholds.75,2. Printed parameter explanations separately retained | genotype subgroup hierarchical model |
| S307 | [pp.15–17 eMethods4](../../../../joi180136supp2_prod.pdf#page=15) | Two simulation regimes0 or1.75 IVR effect;14 observations/arm/pair; patient-specific random baseline/variability;30 virtual patients/aggregate;1000 replicates. Interim stop posterior<20% or>80% on effect>.75, otherwise next pair20–80%; recorded mean and95%CrI; group positive posterior>.80. SAS9.4,WinBUGS1.4,R3.1.3. Printed pointer individual=eMethods2/group=eMethods3 retained. All simulation results below | sample size; power; interim/group decision thresholds |

## Graphical material not present in native text

### PDF p.2 — eTable1 complete graphical eligibility transcription

Inclusion: (1) At least18 years of age; (2) Genetically confirmed diagnosis of NDMs.

Exclusion: (1) Inability or willingness to approved to provide informed consent (wording as displayed); (2) Other neurological conditions that might affect assessment of study measurement; (3) Genetically confirmed DM1 (CTG > repeats), or DM2 — no numeric CTG cutoff is legible/printed in the supplied table; (4) Existing cardiac conduction abnormalities evidenced on ECG, including malignant arrhythmia or cardiac conduction disturbance such as second-degree AV block, third-degree AV block, prolonged QT interval >500ms or QRS duration >150msec; (5) Current use of antiarrhythmic medication for cardiac disorder: flecainide acetate, encainide, disopyramide, procainamide, quinidine, propafenone or mexiletine; (6) Women pregnant or lactating; (7) Currently on medication for myotonia such as phenytoin and flecainide acetate within5 days enrollment; carbamazepine and mexiletine within3 days; propafenone, procainamide, disopyramide, quinidine and encainide within2 days; (8) Renal or hepatic disease, heart failure, history of myocardial infarction, or seizure disorders.

Footnote abbreviations printed: NDMs=non-dystrophic myotonic syndromes; DM=myotonic dystrophy; CTG=cysteine-threonine-glycine (amino acids); AV=atrioventricular. Published-protocol reproduction attribution is retained in page transcription.

### PDF p.7 — eFigure1 complete design graphic

Graphic heading Figure1 Study Design. Study duration minimum11weeks maximum44weeks. Treatment-set11weeks; treatment-period4weeks. Set1: mexiletine, washout, placebo, interim analysis1; visit labels1,2,3,4. Set2: placebo, washout, mexiletine, interim analysis2; visit labels5,6,7,8. Set3: mexiletine, washout, placebo, interim analysis3; visit labels9,10,11,12. Set4: placebo, washout, mexiletine, interim analysis4; visit labels13,14,15,16. Following each of first3 interims, enough evidence for (in)effectiveness? yes→stop individual N-of-1 trial; no→next set. Following interim4→stop. Caption actual set counts retained below.

### PDF p.8 — eFigure2 complete graphical numeric/label map

Panel NDM population, N=27. Y-axis Probability Density Function ticks0.0,0.2,0.4,0.6,0.8. X-axis Mean Effect (IVR score Placebo − IVR score Mexiletine) ticks−1,0,1,2,3,4,5. Vertical dotted threshold0.75. Legend black solid Stiffness; red dashed Pain; blue dotted Weakness; green dash-dot Tiredness. Curve annotations100%,45%,87%,74% respectively; caption independently gives same probabilities and AUC definition. Curves display distributions around mean effects; exact numeric means or interval limits are not printed in this graphic and are not digitized or inferred here.

### PDF p.9 — eFigure3 graphic

Clinical photograph A and skin-biopsy B, patient7. Caption after11 days mexiletine; hematoxylin-eosin40x. No additional comparative statistical quantity. Histology image scale is not an efficacy-result unit; the caption and adverse-event linkage are fully mapped.

## Complete page-linked source transcription

All text-based numeric rows, full model code, explanatory definitions, footnotes and simulation tables follow. Graphical supplement above closes native extraction omissions. Row/column alignment in all tables was checked visually; no values have been normalized to an expected analysis.

### DOC-003 PDF p.1

[Supplied source p.1](../../../../joi180136supp2_prod.pdf#page=1)

```text
                           Supplementary Online Content


Stunnenberg BC, Raaphorst J, Groenewoud HM, et al. Effect of mexiletine
on muscle stiffness in patients with nondystrophic myotonia evaluated
using aggregated N-of-1 trials. JAMA. doi:10.1001/jama.2018.18020

eTable 1. Inclusion and Exclusion Criteria
eTable 2. Individual Demographic, Genotype, and IVR Baseline
Information per Study Patient
eTable 3. Results of Individual Bayesian Interim Analyses on the Primary
Outcome Measure
eTable 4. Adverse Reactions
eFigure 1. Study Design
eFigure 2. Posterior Probability Distributions on Reaching a Clinically
Meaningful Treatment Effect on NDM Disease Group Level (N=27)
eFigure 3. Serious Adverse Event in Patient No. 7
eMethods 1. Winbugs Bayesian Model to Estimate the Effect for an
Individual Patient During Interim Analyses
eMethods 2. Winbugs Bayesian Hierarchical Model to Estimate the Mean
Effect of Mexiletine in Total NDM Disease Group
eMethods 3. Winbugs Bayesian Hierarchical Model to Estimate the Mean
Effect of Mexiletine in Genotype Subgroups
eMethods 4. Details on the Simulation-Based Sample Size Calculation

This supplementary material was provided by the authors to give readers
additonal information about their work.




© 2018 American Medical Association. All rights reserved.

```

### DOC-003 PDF p.2

[Supplied source p.2](../../../../joi180136supp2_prod.pdf#page=2)

```text
eTable 1. Inclusion and Exclusion Criteria




Abbreviations: NDMs= non-dystrophic myotonic syndromes; DM= myotonic dystrophy; CTG=
cysteine-threonine- glycine (amino acids); AV= atrioventricular. This table was reproducted with
permission of BioMed Central as the original publisher from the published study protocol
(Stunnenberg BC, Woertman W, Raaphorst J, et al. Combined N-of-1 trials to investigate mexiletine in
non-dystrophic myotonia using a Bayesian approach; study rationale and protocol. BMC neurology
2015;15:43).




© 2018 American Medical Association. All rights reserved.

```

### DOC-003 PDF p.3

[Supplied source p.3](../../../../joi180136supp2_prod.pdf#page=3)

```text
eTable 2. Individual Demographic, Genotype and IVR-Baseline Information per Study Patient

Patient   Age       Gender   Affected   Mutation(s)     Previous         Relevant              IVR –       IVR –    IVR –      IVR –
nr.       (years)            gene       (allele 1/      anti-myotonic    comorbidity           stiffness   pain     weakness   tiredness
                                        allele 2)       treatment                              (mean)      (mean)   (mean)     (mean)

1.        24        Male     CLCN1      Gly233Ser /     Mexiletine,      -                     7.87        1.20     9.00       8.80
                                        Gly233Ser       acetazolamide
2.        33        Male     CLCN1      Gly285Glu /     Phenytoin        Asthma                6.93        0.00     6.00       2.93
                                        Arg894X
3.        27        Male     CLCN1      c.302-1G>A      -                -                     2.85        2.31     0.00       0.00

4.        25        Female   SCN4A      Gly1306Ala      -                -                     4.93        2.93     2.36       2.57

5.        25        Male     CLCN1      Arg894X /       Phenytoin        -                     7.07        0.00     0.00       2.36
                                        Arg894X
6.        26        Male     CLCN1      Gly233Ser /     Acetazolamide,   Cluster headache      7.78        6.11     7.89       7.44
                                        Gly233Ser       carbamazepine
7.        39        Female   SCN4A      Gly305Glu /     -                Depression            5.20        0.00     0.00       4.47
                                        Ser264fsX6
8. *      21        Female   SCN4A      Gly1306Val      Acetazolamide    -                     5.14        3.68     0.00       5.41

9. *      51        Male     SCN4A      Gly1306Val      Acetazolamide,   -                     5.09        5.55     0.00       6.14
                                                        gabapentin
10.       32        Male     SCN4A      Gly1306Ala      -                Panic disorder        4.71        2.29     0.00       7.29

11.       53        Male     SCN4A      Gly1306Val      Amitriptyline    Stable angina         0.00        5.12     0.00       4.47
                                                                         pectoris
12.       53        Female   SCN4A      Val1485Phe      -                Migraine, artrosis,   3.56        3.37     3.75       4.88
                                                                         asthma
13.       51        Male     SCN4A      Arg1148Cys      -                Lumbago               4.23        5.46     4.38       5.46

14. **    54        Female   CLCN1      c.302-2 A>C     -                -                     5.50        0.00     3.00       5.08

15. **    58        Male     CLCN1      c.302-2 A>C     -                Hypertension          7.07        0.47     3.67       2.60

16. **    60        Male     CLCN1      c.302-2 A>C /   Quinidine        -                     6.62        0.00     4.00       6.31
                                        Met646Ile
17.       55        Male     CLCN1      Gly285Glu /     -                Hernia                5.87        3.67     5.13       1.07
                                        Met646Ile                        lumbosacralis
18.       48        Female   ClCN1      c.302-2 A>C /   Tocainide        -                     5.71        0.59     4.18       0.88
                                        Met646Ile
19. *     21        Male     SCN4A      Gly1306Val      -                -                     3.31        2.00     0.23       3.85



© 2018 American Medical Association. All rights reserved.

```

### DOC-003 PDF p.4

[Supplied source p.4](../../../../joi180136supp2_prod.pdf#page=4)

```text
20.       32      Female    SCN4A     Gly1306Val    -               -                     6.08   5.85   0.46    5.08

21.       64      Male      SCN4A     Gly1306Val    Acetazolamide   COPD                  2.77   3.00   2.62    2.62

22.       19      Male      SCN4A     Leu703Pro     Acetazolamide   -                     8.00   0.00   5.00    7.00

23.       50      Male      CLCN1     Gly285Glu /   Acetazolamide   -                     7.71   0.00   7.71    0.00
                                      Met646Ile
24. ***   53      Male      CLCN1     Phe413Cys     -               -                     6.80   3.73   4.60    7.47

25. ***   58      Male      CLCN1     Phe413Cys     -               Hypothyreoidism       6.57   0.00   2.79    3.07

26. ***   62      Male      CLCN1     Phe413Cys     -               -                     6.80   0.00   3.93    3.67

27. ***   60      Male      CLCN1     Phe413Cys     -               Cerebral infarction   6.22   0.00   0.00    6.89

28.       65      Male      CLCN1     Lys195fsX     Quinidine       Subdural hematoma     6.71   0.00   3.37    0.79

29.       44      Female    CLCN1     Phe413Cys     -               -                     6.71   0.00   0.57    4.86

30.       49      Male      CLCN1     Gly285Glu     -               Panic disorder        4.62   3.69   0.00    4.00



*/**/*** Study patients belonging to the same family. Abbreviations: IVR= interactive voice response system; CLCN1=skeletal muscle chloride channel
gene; SCN4A= skeletal muscle sodium channel gene.




© 2018 American Medical Association. All rights reserved.

```

### DOC-003 PDF p.5

[Supplied source p.5](../../../../joi180136supp2_prod.pdf#page=5)

```text
eTable 3. Results of Individual Bayesian Interim Analyses on the Primary Outcome Measure
Patient   Affected   Interim        Mean        95% Credible       Posterior probability       Mexiletine
nr.       gene       analysis nr.   treatment   Interval           (of clinically meaningful   treatment
                                    effect                         difference)                 post-trial

1         CLCN1      2              4.4         (4.03 ; 4.85)      100%                        Continued
2         CLCN1      2              3.1         (2.63 ; 3.49)      100%                        Continued
4         SCN4A      2              1.1         (0.27 ; 1.90)      81%                         Continued
5         CLCN1      2              4.7         (4.50 ; 4.87)      100%                        Continued
8         SCN4A      1              1.2         (-0.03 ; 2.41)     80%                         Continued
9         SCN4A      1              3.2         (2.78 ; 3.56)      100%                        Continued
10        SCN4A      1              3.7         (2.28 ; 5.04)      100%                        Continued
11        SCN4A      1              0.00        (-12.24 ; 12.16)   38%*                        Stopped
12        SCN4A      1              2.66        (1.76 ; 3.56)      100%                        Continued
13        SCN4A      1              -0.05       (-0.56 ; 0.45)     2%                          Stopped
14        CLCN1      1              3.5         (2.81 ; 4.19)      100%                        Continued
15        CLCN1      1              2.7         (2.16 ; 3.24)      100%                        Continued
16        CLCN1      1              4.49        (3.96 ; 5.03)      100%                        Continued
17        CLCN1      1              3.22        (2.94 ; 3.50)      100%                        Continued
18        CLCN1      1              2.55        (1.77 ; 3.32)      100%                        Continued
19        SCN4A      1              2.63        (1.18 ; 4.01)      99%                         Continued
20        SCN4A      1              1.13        (0.14 ; 2.13)      80%                         Continued
21        SCN4A      1              4.41        (3.80 ; 5.0)       100%                        Continued
22        SCN4A      1              0.01        (-0.56 ; 0.57)     1%                          Stopped
23        CLCN1      1              5.49        (4.98 ; 6.04)      100%                        Continued
24        CLCN1      1              2.64        (2.16 ; 3.12)      100%                        Continued
25        CLCN1      1              1.65        (1.27 ; 2.03)      100%                        Continued
26        CLCN1      1              4.65        (4.07 ; 5.21)      100%                        Continued
27        CLCN1      1              3.14        (2.46 ; 3.83)      100%                        Continued
28        CLCN1      1              4.50        (4.0 ; 4.99)       100%                        Continued
29        CLCN1      1              6.99        (6.59 ; 7.41)      100%                        Continued
30        CLCN1      1              3.57        (2.91 ; 4.23)      100%                        Continued

Primary outcome measure (IVR-stiffness) mean treatment effects are reported (N=27). Mexiletine
non-responders (pre-defined posterior probability effect of reaching 0.75 point difference on the
IVR-scale <0.20, i.e. 20%) are marked in bold (patient nr. 11, 13 and 22). Mexiletine-responders were
pre-defined as posterior probability effect 0.75 point difference on the IVR-scale >0.80, i.e. 80%.
Patient no. 1, 2, 4 and 5 represent patients that had two instead of one treatment-set as part of their
individual N-of-1 trial. Patient no. 3, 6 and 7 dropped out. * Posterior probability in patient no. 11 is
strongly influenced by the flat (wide) non-informative prior since the distribution of the treatment
effect was 0 (95% CI 0;0) (absence of muscle stiffness during both placebo en mexiletine treatment
periods). Therefore the individual N-of-1 trial was stopped after 1 treatment-set and mexiletine
treatment was discontinued.



© 2018 American Medical Association. All rights reserved.

```

### DOC-003 PDF p.6

[Supplied source p.6](../../../../joi180136supp2_prod.pdf#page=6)

```text
eTable 4. Adverse Reactions

                                                       Mexiletine   Placebo
Adverse reactions                                      No. (%)      No. (%)
Gastro-intestinal discomfort                           21 (70%)     1 (3%)
(Reflux, dyspepsia, nausea, diarrhea and
flatulence)
Tremor                                                 2 (7%)       0 (0%)
Palpitations                                           2 (7%)       0 (0%)
Headache                                               1 (3%)       1 (3%)
Insomnia                                               1 (3%)       0 (0%)
Any                                                    27 (90%)     2 (6%)
   >1 adverse reactions                                2 (7%)       0 (0%)
   >2 adverse reactions                                0 (0%)       0 (0%)
   Causing study withdrawal                            1 (3%)       0 (0%)
   Leading to dosage reduction                         3 (10%)      0 (0%)
   Leading to additional therapy                       2 (7%)       0 (0%)
                                                       Mexiletine   Placebo
Serious adverse reactions                              No. (%)      No. (%)
Allergic skin reaction (toxicodermia)                  1 (3%)       0 (0%)




© 2018 American Medical Association. All rights reserved.

```

### DOC-003 PDF p.7

[Supplied source p.7](../../../../joi180136supp2_prod.pdf#page=7)

```text
eFigure 1. Study Design




Each individual N-of-1 trial had a flexible design of a mimimum of one and a maximum of four
treatment-sets, depending of the level of evidence that was reached after each individual interim
analysis at the end of each treatment-set. Note that in the trial, only four patients (no. 1, 2, 4 and 5)
needed two treatment-sets to reach the predefined evidence for (in)effectiveness, while all other 23
patients needed only one treatment-set. This figure was reproducted with permission of BioMed
Central as the original publisher from the published study protocol (Stunnenberg BC, Woertman W,
Raaphorst J, et al. Combined N-of-1 trials to investigate mexiletine in non-dystrophic myotonia using
a Bayesian approach; study rationale and protocol. BMC neurology 2015;15:43).




© 2018 American Medical Association. All rights reserved.

```

### DOC-003 PDF p.8

[Supplied source p.8](../../../../joi180136supp2_prod.pdf#page=8)

```text
eFigure 2. Posterior Probability Distributions on Reaching a Clinically Meaningful Treatment

Effect on NDM Disease Group Level (N=27)




The probability density functions (PDF) of the treatment effects of the four IVR-scores show the

distributions around each mean treatment effect. The dotted line (0.75) represent the threshold

for a clinically meaningful treatment effect. Posterior probabilities of a clinically meaningful

treatment effect represent the area under the curve (AUC) of the treatment effect distributions right

from the dotted line; p (meaningful effect) = 100% for IVR-stiffness, 45% for IVR-pain, 87% for IVR-

weakness and 74% for IVR-tiredness.




© 2018 American Medical Association. All rights reserved.

```

### DOC-003 PDF p.9

[Supplied source p.9](../../../../joi180136supp2_prod.pdf#page=9)

```text
eFigure 3. Serious Adverse Event in Patient No. 7




(A) Generalised erythematous papules that developed in patient no. 7 after eleven days of mexiletine
treatment. (B) Histological section of skin biopsy shows a superficial dermatitis with eosinophilic
infiltration and leucostasis as can be seen in toxicodermia (hematoxylin-eosin 40x).




© 2018 American Medical Association. All rights reserved.

```

### DOC-003 PDF p.10

[Supplied source p.10](../../../../joi180136supp2_prod.pdf#page=10)

```text
eMethods 1. Winbugs Bayesian Model to Estimate the Effect for an Individual Patient During
Interim Analyses

model
{
for (i in 1:30) {
Stiffness_plac[i]~dnorm(mu_plac,tau_plac)}
for (j in 1:30) {
Stiffness_mex[j]~dnorm(mu_mex,tau_mex)}
mu_plac~dnorm(0, 0.001)
mu_mex~dnorm(0,0.001)
tau_plac<-1/(sigma_plac*sigma_plac)
sigma_plac~dunif(0.01, 10)
tau_mex<-1/(sigma_mex*sigma_mex)
sigma_mex~dunif(0.01, 10)
diff<-mu_plac-mu_mex
p1<-step(diff)
p2<-step(diff-0.75)
p3<-step(diff-2)
}

In which:Real data:

Stiffness_plac[i] - IVR score of measurement i during placebo treatment
Stiffness_mex[i] - IVR score of measurement i during mexiletine treatment

Estimated model parameters:
mu_plac       Mean IVR score over the days with placebo treatment
sigma_plac    Standard deviation of IVR scores over the days with placebo treatment
tau_plac      1/(sigma_plac*sigma_plac)
mu_mex        Mean IVR score over the days with mexiletine treatment
sigma_mex     Standard deviation of IVR scores over the days with mexiletine treatment
tau_mex       1/(sigma_mex*sigma_mex)
diff           mu_plac – mu_mex
               Difference between mean IVR score during placebo treatment en mean IVR score
               during mexiletine treatment
p1            Probability that the difference will be greater than 0.
p2            Probability that the difference will be greater than 0.75
p3            Probability that the difference will be greater than 2


In the model it is assumed there is a maximum number of 30 measurements during a treatment
period.




© 2018 American Medical Association. All rights reserved.

```

### DOC-003 PDF p.11

[Supplied source p.11](../../../../joi180136supp2_prod.pdf#page=11)

```text
eMethods 2. Winbugs Bayesian Hierarchical Model to Estimate the Mean Effect of Mexiletine in
Total NDM Disease Group


model
{
  for( i in 1 : n ) {
    mu_mex[i] ~ dnorm(mu.mex, tau.mex)
    mu_plac[i] ~ dnorm(mu.plac, tau.plac)
    diff_patient[i] <- mu_plac[i] - mu_mex[i]
    for ( t in 1 : N_plac[i] ) {
        Stiff_Plac[i, t] ~ dnorm(mu_plac[i], tau.within)
    }
    for ( t in 1 : N_mex[i] ) {
        Stiff_Mex[i, t] ~ dnorm(mu_mex[i], tau.within)
    }
  }
p1 <- step(mu.plac - mu.mex)
p2 <- step(mu.plac - mu.mex - 0.75)
p3 <- step(mu.plac - mu.mex - 2)
tau.within<-1/(sigma.within*sigma.within)
sigma.within~dunif(0.01, 10)
 mu.mex ~ dnorm(4, 0.001)
tau.mex<-1/(sigma.mex*sigma.mex)
sigma.mex~dunif(0.01, 10)
   mu.plac ~ dnorm(4, 0.001)
tau.plac<-1/(sigma.plac*sigma.plac)
sigma.plac~dunif(0.01, 10)
diff <- mu.plac - mu.mex
}

In which:

Real data:
Stiff_Plac[i, t]   IVR stiffness score for patient i at time t during placebo treatment
Stiff_Mex[i, t]    IVR stiffness score for patient i at time t during mexiletine treatment
N_plac[i]          Number of observations for patient i during placebo treatment
N_mex[i]           Number of observations for patient i during mexiletine treatment
n                  Number of patients

Estimated model parameters
mu_mex[i]     mean IVR score of patient i during the placebo treatment
mu_plac[i]    mean IVR score of patient i during the mexiletine treatment
mu.plac       Mean IVR score of NDM population (so the mean of the individual means)
              during placebo treatment (=population mean)
sigma.plac    Standard deviation of the individual mean IVR scores in the NDM population
              during placebo treatment
tau.plac      1/(sigma.plac*sigma.plac)
mu.mex        Mean IVR score of NDM population (so the mean of the individual means)
              during mexiletine treatment (=population mean)
sigma.mex     Standard deviation of the individual mean IVR scores in the NDM population


© 2018 American Medical Association. All rights reserved.

```

### DOC-003 PDF p.12

[Supplied source p.12](../../../../joi180136supp2_prod.pdf#page=12)

```text
               during placebo treatment
tau.mex        1/(sigma.mex*sigma.mex)
sigma.within Standard deviation for IVR score measurements for an individual patient. It is
assumed that the
               standard deviation is the same during placebo and mexiletine treatment.
tau.within     1/(sigma.within*sigma.within)

diff            mu.plac – mu.mex
                Difference between population mean IVR score during placebo treatment en
population
               mean IVR score during mexiletine treatment (=population effect)
p1             Probability that the population effect will be greater than 0
P2             Probability that the population effect will be greater than 0.75
P3             Probability that the population effect will be greater than 2




© 2018 American Medical Association. All rights reserved.

```

### DOC-003 PDF p.13

[Supplied source p.13](../../../../joi180136supp2_prod.pdf#page=13)

```text
eMethods 3. Winbugs Bayesian Hierarchical Model to Estimate the Mean Effect of Mexiletine in
Genotype Subgroups


model
{
  for( i in 1 : n ) {
    mu_gen.mex[i] <- a + b*Gen_Pat[i]
    mu_gen.plac[i] <- c + d*Gen_Pat[i]
    mu_mex[i] ~ dnorm(mu_gen.mex[i], tau.mex)
    mu_plac[i] ~ dnorm(mu_gen.plac[i], tau.plac)
    diff_patient[i] <- mu_plac[i] - mu_mex[i]
    for ( t in 1 : N_plac[i] ) {
        Stiff_Plac[i, t] ~ dnorm(mu_plac[i], tau.within)
    }
    for ( t in 1 : N_mex[i] ) {
        Stiff_Mex[i, t] ~ dnorm(mu_mex[i], tau.within)
    }
  }

p2_SCN4A<-step(diff_SCN4A - 0.75)
p2_CLCN1<-step(diff_CLCN1 - 0.75)
p3_SCN4A<-step(diff_SCN4A - 2)
p3_CLCN1<-step(diff_CLCN1 - 2)

tau.within<-1/(sigma.within*sigma.within)
sigma.within~dunif(0.01, 10)
  a ~ dnorm(0, 0.01)
  b ~ dnorm(0, 0.01)
  c ~ dnorm(0, 0.01)
  d ~ dnorm(0, 0.01)

tau.mex<-1/(sigma.mex*sigma.mex)
sigma.mex~dunif(0.01, 10)
tau.plac<-1/(sigma.plac*sigma.plac)
sigma.plac~dunif(0.01, 10)
mu.mex_SCN4A <- a
mu.mex_CLCN1 <- a + b
mu.plac_SCN4A <- c
mu.plac_CLCN1 <- c + d
diff_SCN4A <- mu.plac_SCN4A - mu.mex_SCN4A
diff_CLCN1 <- mu.plac_CLCN1 - mu.mex_CLCN1
 }

In which:

Real data:
Stiff_Plac[i, t]   IVR stiffness score for patient i at time t during placebo treatment
Stiff_Mex[i, t]    IVR stiffness score for patient i at time t during mexiletine treatment
N_plac[i]          Number of observations for patient i during placebo treatment
N_mex[i]           Number of observations for patient i during mexiletine treatment
n                  Number of patients

© 2018 American Medical Association. All rights reserved.

```

### DOC-003 PDF p.14

[Supplied source p.14](../../../../joi180136supp2_prod.pdf#page=14)

```text
Gen_Pat[i]     Genotype for patient i (1=CLCN1, 0=SCN4A)

Estimated model parameters
mu_mex[i]     mean IVR score of patient i during the placebo treatment
mu_plac[i]    mean IVR score of patient i during the mexiletine treatment
mu.plac_SCN4AMean IVR score of SCN4A population (so the mean of the individual means)
              during placebo treatment (=population mean)
mu.plac_CLCN1 Mean IVR score of CLCN1 population (so the mean of the individual means)
              during placebo treatment (=population mean)
sigma.plac    Standard deviation of the individual mean IVR scores in the NDM population
              during placebo treatment (assumed to be the same for both genotypes)
tau.plac      1/(sigma.plac*sigma.plac)
mu.mex_SCN4A Mean IVR score of SCN4A population (so the mean of the individual means)
              during mexiletine treatment (=population mean)
mu.mex_CLCN1 Mean IVR score of CLCN1 population (so the mean of the individual means)
              during mexiletine treatment (=population mean)
sigma.mex     Standard deviation of the individual mean IVR scores in the NDM population
              during placebo treatment (assumed to be the same for both genotypes)
tau.mex       1/(sigma.mex*sigma.mex)
sigma.within Standard deviation for IVR score measurements for an individual patient.
              It is assumed that the standard deviation is the same during placebo and mexiletine
              treatment and the same for both genotypes.
tau.within    1/(sigma.within*sigma.within)

diff_SCN4A     mu.plac – mu.mex for SCN4A patients
               Difference between population mean IVR score during placebo treatment and
               mean IVR score during mexiletine treatment (=population effect) for SCN4A patients
diff_CLCN1     mu.plac – mu.mex for SCN4A patients

P2_SCN4A       Probability that the population effect for SCN4A population will be greater than 0.75
P2_CLCN1       Probability that the population effect for CLCN1 population will be greater than 0.75
P3_SCN4A       Probability that the population effect for SCN4A population will be greater than 2
P3_CLCN1       Probability that the population effect for CLCN1 population will be greater than 2




© 2018 American Medical Association. All rights reserved.

```

### DOC-003 PDF p.15

[Supplied source p.15](../../../../joi180136supp2_prod.pdf#page=15)

```text
eMethods 4. Details on the Simulation-Based Sample Size Calculation

We performed two sets of simulations to determine the operating characteristics of the overall
strategy (combined N-of-1 trials using the Bayesian hierarchical model meta-analysis) - one set under
the assumption of no treatment effect (for the determination of the type 1 error), and one set under
the assumption of a particular fixed treatment effect (for the determination of the power). As fixed
treatment effect we used 1.75 point difference on the IVR-stiffness scale, that was based on
preliminary results of the previous RCT by Statland et al. (2012), provided by the study team.

1.1 Calculation of type 1 error rate - simulations under the assumption of a treatment effect of
    zero

    1. For each virtual patient, using SAS 9.4 software, we simulated data (14 observations per arm
        per treatment pair) that allowed the patient to have their own randomly chosen baseline
        value and expected variability, both for the placebo and mexiletine treatment periods (with
        the overall treatment effect being zero);

    2. Per individual patient, the Bayesian interim analysis defined in eMethods 2 (using Winbugs
        version 1.4 software, run from R Statistics version 3.1.3) was performed to determine
        whether a conclusion of no meaningful effect (<20% posterior probability on 0.75 point
        difference) or meaningful effect (>80% posterior probability on 0.75 point difference) would
        be drawn, or the patient would be evaluated with another treatment pair (between 20-80%
        posterior probability on 0.75 point difference);

    3. Step 1 and 2 were continued until no further testing on that patient would have been
        conducted, and the final results for that patient was recorded (mean treatment effect with
        95% credible interval and posterior probability on a meaningful treatment effect);

    4. Step 1-3 were repeated until 30 virtual patient data-sets were simulated (with variation in
        the number of treatment-sets). All data from these 30 virtual individual N-of-1 trials was
        used to perform the Bayesian meta-analysis on a group level according to eMethods 3;

    5. We recorded the overall result (i.e., posterior probability on a meaningful treatment effect
        on a group level) of the Bayesian meta-analysis and the final estimate of the treatment effect
        (mean effect, 95% credible interval);

    6. Step 1-5 were repeated 1000 times (corresponding with data from 1000 aggregated N-of-1
        trials) and we determined: (a) the fraction of meta-analyses that return a positive conclusion
        (i.e. a >80% posterior probability on a meaningful treatment effect): as measure for the type

© 2018 American Medical Association. All rights reserved.

```

### DOC-003 PDF p.16

[Supplied source p.16](../../../../joi180136supp2_prod.pdf#page=16)

```text
          I error rate. The type 1 error rate (number of times that p2.mean.tot > 80%: (p2_effect=1))
          was found to be 0.00 (see Table 2 below); (b) the mean treatment effect from these 1000
          simulated data-sets, as measure for the bias since the true value is exactly zero, was found to
          be 0.07 (see Table 1 below).


                               mean_sets   diff.mean.tot      mu.mex.tot    mu.plac.tot    p1.mean.tot    p2.mean.tot
N                   Valid            1000           1000            1000           1000           1000           1000
                    Missing              0              0               0              0              0              0
Mean                                  3.41            .07            4.58           4.65            .55            .12
Median                                3.43            .06            4.57           4.66            .55            .09
Std. Deviation                         .21            .27             .38            .31            .19            .10
Minimum                               2.73           -.85            3.46           3.74            .04            .00
Maximum                               3.97            .95            5.82           5.57            .97            .66
Percentiles    25                     3.27           -.12            4.32           4.43            .41            .04
               50                     3.43            .06            4.57           4.66            .55            .09
               75                     3.57            .25            4.83           4.86            .69            .17

Table 1. Results from simulations under the assumption of a treatment effect of zero
Mean_sets = mean number of pairs per patient
Diff.mean.tot = mean treatment effect (mu.plac.tot – mu.mex.tot)
Mu.mex.tot = mean effect during mexiletine period
Mu.plac.tot = mean effect during placebo period
P1.mean.tot = probability of an effect > .00
P2.mean.tot = probability of an effect > .75


                       Frequency   Percent    Valid Percent    Cumulative Percent
  Valid      .00          1000       100           100               100
            1.00           .00       .00           .00               100
            Total         1000       100           100               100

Table 2. Results from calculation of type 1 error rate
Type 1 error rate = number of times that p2.mean.tot > 80%: (p2_effect=1)



1.2 Calculation of the power - simulations under the assumption of a treatment effect of 1.75

          (Step 1 – 5) Calculation the power was analogous to the above described steps 1-6 for
          calculation of the type 1 error with the exemption that the overall treatment effect for each
          virtual patient within each virtual treatment-set was kept at a fixed treatment effect of 1.75
          (instead of zero).

    6. Step 1-5 were repeated 1000 times (corresponding with data from 1000 aggregated N-of-1
          trials) to determine: (a) the fraction of meta-analyses that return a positive conclusion (i.e. a
          >80% posterior probability on a meaningful treatment effect): as measure for the power. The
          power (number of times that p2.mean.tot > 80%: (p2_effect=1)) was found to be 68.5% (see

© 2018 American Medical Association. All rights reserved.

```

### DOC-003 PDF p.17

[Supplied source p.17](../../../../joi180136supp2_prod.pdf#page=17)

```text
        Table 4 below); (b) the mean treatment effect from these 1000 simulated data-sets (1.29 –
        see Table 3 below) minus the assumed, fixed treatment effect of 1.75 (as measure for the
        bias) was found to be -0.46 [1.29 – 1.75].



                               mean_sets   diff.mean.tot      mu.mex.tot     mu.plac.tot    p1.mean.tot    p2.mean.tot
N                 Valid              1000           1000            1000            1000           1000           1000
                  Missing                0              0               0               0              0              0
Mean                                  2.59          1.29             3.38            4.67            .99            .83
Median                                2.60           1.29            3.37            4.67           1.00            .86
Std. Deviation                         .25            .26             .35             .31            .02            .12
Minimum                               1.73            .43            2.44            3.79            .81            .26
Maximum                               3.47           2.13            4.60            5.59           1.00           1.00
Percentiles    25                     2.43           1.12            3.13            4.46            .99            .77
               50                     2.60           1.29            3.37            4.67           1.00            .86
               75                     2.73           1.46            3.62            4.88           1.00            .93

Table 3. Results from simulations under the assumption of a treatment effect of 1.75
Mean_sets = mean number of pairs per patient.
Diff.mean.tot = mean treatment effect (mu.plac.tot – mu.mex.tot)
Mu.mex.tot = mean effect during mexiletine period
Mu.plac.tot = mean effect during placebo period
P1.mean.tot = probability of an effect > .00
P2.mean.tot = probability of an effect > .75



                     Frequency     Percent    Valid Percent    Cumulative Percent
Valid      .00          315         31,5          31.5                31.5
           1.00         685         68.5          68.5               100.0
          Total         1000        100.0        100.0

Table 4. Results from power calculation
Power = number of times that p2.mean.tot > 80%: (p2_effect=1)




© 2018 American Medical Association. All rights reserved.

```
