# Support mapping shard 006

Runtime agent: /root/support_mapper_6. Role: support quantitative mapper. Scope: DOC-004 all 26 PDF pages, DOC-005 all 6 PDF pages, DOC-006 PDF page 1; 33/33 mapped, no scientific coverage gaps. All three documents are REPORT by content. No candidate diagnosis or prior scientific output is incorporated.

## Engines, reusable assets, and source-location control

Read QUALITY_CONTROL_SCOPE.md, workflow_1_6_2/review_contract.md, source_inventory.md, source_coverage.md, assigned evidence-asset inventory rows, and tooling_record.md. Reused DOC-004 normalized/native text and all 12 canonical rendered companions pp.14–25; DOC-005 six-page native text; DOC-006 one-page native text. All 26 DOC-004 native-page filenames and normalized SOURCE PDF PAGE markers correctly correspond to the supplied PDF. The printed page labels differ from PDF page numbers (for example eTable1 printed13 is PDF14); these are preserved but PDF numbers control links. Direct fresh sorted layout extraction of all26PDFpages corroborates every source location; native source plus rendered companions agree.

New derivative: preprocessing/support-006/doc004_direct_layout.txt. Command: `/home/juliz/venvs/stt/bin/python workflow_1_6_2/scripts/pdf_tools.py text joi240158supp3_prod_1742927563.7911.pdf --first 1 --last 26 .ai_paper_validation/review_1_6_2/preprocessing/support-006/doc004_direct_layout.txt --layout`. Engine: PyMuPDF 1.28.0, sorted reading order, CPU native/layout extraction. No fresh rendering or OCR required. GPU request retained; no CPU OCR performed. Legacy image engines UNKNOWN_LEGACY. All image tables/plots visually read, with every printed cell preserved below. Source PDF page numbers, not printed page labels, control citations.

## Complete page coverage and relationship groups

Each record group includes every printed quantity and definition in its page-specific source transcript below. A table row's stable member key is its group ID followed by the exact printed row and, where needed, treatment column. Numeric and statistical groups cross-reference rather than duplicate cells.

| Source/page | Group IDs | Exact unit and matching main-paper key | Coverage |
|---|---|---|---|
| DOC-004 p.1 | SP6-N001 | Contents; citation; authors' supplemental-report status. No result cells; lists eMethods, eTables1–5, eFigure. | COMPLETE |
| DOC-004 p.2 | SP6-N002 | Trial design:54 NEALS centers, July2020–March2022, RGC. Administrative oversight has no inferential relationship. | COMPLETE |
| DOC-004 p.3 | SP6-N003, SP6-S001 | Eligibility≤36months; VC≥50%; riluzole>30days/edaravone1cycle;4 randomization strata. Main eligibility/randomization key. | COMPLETE |
| DOC-004 p.4 | SP6-N004, SP6-S002 | Block size8:3/3/2;60/30mg daily;24weeks;two60mL bottles,30/15mg per bottle; dosing/visits; pooled primary contrast. | COMPLETE |
| DOC-004 p.5 | SP6-N005, SP6-S003 | Primary function+survival24weeks; three hierarchical secondary endpoints CAFS,SVC,death/PAV;PAV>22h/day>7days; TEAE definitions; exploratory biomarker status. | COMPLETE |
| DOC-004 p.6 | SP6-N006, SP6-S004 | Exploratory measure counts4/6/11; speech9features; time-to-event3+8; plasmaNfL posthoc; combined dose main vs dose-specific exploratory; FAS sharedplaceboA/B/D. | COMPLETE |
| DOC-004 p.7 | SP6-N007, SP6-S005 | Regimen-only/safety populations; safety gold-allergy exclusion; ALSFRS-R scheduled weeks0,4,8,12,16,20,24;DRR meaning. | COMPLETE |
| DOC-004 p.8 | SP6-N008, SP6-S006 | DRR0.50 illustrative6points/6months vs12months and9months survival vs18; functional repeated measures; exponential survival; shared-control hierarchical model. | COMPLETE |
| DOC-004 p.9 | SP6-N009, SP6-S007 | MCMC≥500000,thinning10;convergence;CAFS sensitivity;futility40participants30active/10placebo,every12weeks,posterior<5% for≥10%ALSFRS-Rslowing;no success stop. | COMPLETE |
| DOC-004 p.10 | SP6-N010, SP6-S008 | SVC linear mixed/random slopes covariates/interactions/random regimen intercepts; Cox death/PAV/hospitalization; supportive baselineNfL+visit interaction;two assay replicates. | COMPLETE |
| DOC-004 p.11 | SP6-N011, SP6-S009 | CV>25% repetition;LOQ usesLOD;no exclusions primary;FASserumNfLprespecified vs regimen-onlyposthoc;plasma4plex posthoc;30min,-80C,96well. | COMPLETE |
| DOC-004 p.12 | SP6-N012, SP6-S010 | NfLMMRM regimen-only,covariates+visit interactions;outliers<4pg/mL or<2%individualmax;oneplacebo baseline omitted sensitivity;urinaryp75ecd;KingStage4intervalcensoring,otherTTEventrightcensoring. | COMPLETE |
| DOC-004 p.13 | SP6-N013, SP6-S011 | Complete prespecified subgroup definitions;random-slope model interaction terms;FASprimary/secondary endpoints. | COMPLETE |
| DOC-004 p.14 | SP6-N014 | eTable1:7visits×3groups, each n/mean/SD. ALSFRS-R distributions; observed contributor counts. | COMPLETE |
| DOC-004 p.15 | SP6-N015, SP6-S012 | eTable2:9parameterrows; median,mean(SD),95%CrI;DRRPr<1/Pr<0.9;monthly slopes/hazards/covariates. Main primary analysis key. | COMPLETE |
| DOC-004 p.16 | SP6-N016, SP6-S013 | eTable3A:6rows FAS24-week ALSFRS-R/SVC pooled/30/60mg vs sharedplacebo,n120/59/61 vs164; estimates(SE),difference(SE),95%CI,P. | COMPLETE |
| DOC-004 p.17 | SP6-N017, SP6-S014 | eTable3B:12rows ERO24-week ALSFRS-R/SVC/plasma/serumNfL pooled/30/60mg vs regimenplacebo41;estimates(SE where given),difference(SE where given),95%CI,P;log/exponentiation footnote. | COMPLETE |
| DOC-004 p.18 | SP6-N018, SP6-S015 | eTable4:11rows allparticipants,riluzole,edaravone,combinedmedication,age;3estimatesandCIs/row;subgroupPvalues;plotreference/direction. | COMPLETE |
| DOC-004 p.19 | SP6-N019, SP6-S016 | eTable4:16rows sex,race,ethnicity,weight,BMI,CKD,onset;3estimatesandCIs/row;subgroupPvalues. | COMPLETE |
| DOC-004 p.20 | SP6-N020, SP6-S017 | eTable4:8rowsElEscorial×onset,severity,NfL,dFRS;3estimatesandCIs/row;4subgroupPvalues;axis−2,0,2. | COMPLETE |
| DOC-004 p.21 | SP6-N021 | eTable5:9safetycategoryrows×5arms,eachparticipantcount(%),eventcount;denominators120/59/61/163/41. | COMPLETE |
| DOC-004 p.22 | SP6-N022 | eTable5:14rows×5arms,eachparticipantcount(%),eventcount;same denominator/control definitions. | COMPLETE |
| DOC-004 p.23 | SP6-N023 | eTable5:14rows×5arms,eachparticipantcount(%),eventcount;same denominator/control definitions. | COMPLETE |
| DOC-004 p.24 | SP6-N024 | eTable5:13rows×5arms,eachparticipantcount(%),eventcount;same denominator/control definitions. | COMPLETE |
| DOC-004 p.25 | SP6-N025, SP6-S018 | eFigure serumNfL sensitivity caption;all thresholds/times,exclusioncount,groupchanges,geometricmeancontrast95%CI/P. | COMPLETE |
| DOC-004 p.26 | SP6-N026 | Printed28;rights-only endpage. Explicit no-applicable numeric/statistical result content. | COMPLETE |
| DOC-005 p.1 | SP6-N027 | Nonauthorcollaborator table,biostatistician/advisory/subinvestigator roles;formv02-22,p1of6. No applicable quantitative result/design. | COMPLETE |
| DOC-005 p.2 | SP6-N028 | Collaborator roster/institutions/location/subinvestigatorroles;formv02-22,p2of6. No applicable quantitative result/design. | COMPLETE |
| DOC-005 p.3 | SP6-N029 | Collaborator roster/institutions/location/investigatorroles;formv02-22,p3of6. No applicable quantitative result/design. | COMPLETE |
| DOC-005 p.4 | SP6-N030 | Collaborator roster/data/system/projectmanagement/IRBroles;formv02-22,p4of6. No applicable quantitative result/design. | COMPLETE |
| DOC-005 p.5 | SP6-N031 | Collaborator roster/sitemonitoring/centralpharmacyroles;formv02-22,p5of6. No applicable quantitative result/design. | COMPLETE |
| DOC-005 p.6 | SP6-N032 | Collaborator roster/pharmacy/DSMB/medicalmonitorroles;formv02-22,p6of6. No applicable quantitative result/design. | COMPLETE |
| DOC-006 p.1 | SP6-N033, SP6-S019 | DataavailableNo;design/analysissoftwareSAS≥9.4,R≥4.0,JAGS≥4.3;codeunavailable;trialongoing. No result cells. | COMPLETE |

## Matching and interpretation keys supplied to downstream checkers

All numeric transcripts below preserve the printed readings; no arithmetic diagnosis is made here. Groups SP6-S001–S019 are the complete statistical relationship groups for this scope.

Primary key: pooled30+60mg CNM-Au8 versus concurrent shared controls, FAS,24weeks, function+survival Bayesian DRR; eTable2 function/mortality row median0.96,mean0.97(SD0.099),95%CrI(0.783,1.175),Pr(DRR<1)=0.6450,Pr(DRR<0.9)=0.2505. Covariates baselineedaravone,baselineriluzole,monthssinceonset,prebaselineALSFRS-Rslope. Component slopes monthly: placebo−1.03 and active−1.00;monthly mortalityrates0.010 and0.009. Do not treat posterior probabilities as frequentistPvalues.

Secondary key: hierarchical CAFS, SVCdecline, survivalfreePAV. SVC repeatedmeasure/randomslopes and covariates as pp.10; time-event Cox covariates age plus baseline drugs,dFRS,onset; King'sStage4 intervalcensoring. eTable3A is FAS with sharedplacebo164;3B ERO with regimenplacebo41. Each has dose-specific59/61,pooled120. Change estimates are24weeks; forest eTable4 slopes are monthlyALSFRS-R model estimates, not24weekmeanchanges. eTable3B NfL log-transformed/exponentiated, difference heading, GMR abbreviation preserved; SE not printed for NfL cells. Every plasma/serum CI endpoint andPvalue is separately preserved. Plasma pooled−9.5(−18.0,0),P0.04;30mg−8.5(−18,2),P0.10;60mg−10.5(−20,0),P0.04. Serum pooled−26.4(−50.3,−2.6),P0.03;30mg−25.5(−52.2,1.3),P0.06;60mg−27.4(−45.1,−0.7),P0.05.

Subgroup key: pooledactive vs sharedplacebo FAS linear mixed/randomslopes, age65,onset18months,baseline severityitem2,NfL/dFRSmedians. pvalue printed once beside each applicable subgroup block; not assigned separately to every within-subgroup treatmentcontrast. Caption says everyCIcrossesnodifference and no subgroup significantbenefit; graphical right favorsTreatment,leftPlacebo,verticalnull0,axis−2,0,2. All35data rows and plotted direction positions are read; printed numeric row values in transcript are authority, graphical marks provide visual direction/interval companions.

Safety key: eTable5 TEAEincidence≥5%ineithergroup. Pooled120,30mg59,60mg61,sharedplacebo163,regimenplacebo41. Eachcell is distinct participantcount(%),numberofevents; repeated events are not participants. All50rows×5arms=250cells (750 participant/percentage/event quantities), all retained. Severity rows mild/moderate/severe are preserved separately from seriousrows. Main safety comparison should match safety denominator163 rather than efficacy164. TEAE diseaseprogressionsymptoms included except separatelyrecorded/analysedALSFRS-RorSVCworsening. No interval orPvalues printed in safetytable.

NfL sensitivity key: serum regimen-only, posthoc omission1baselineplacebomeasure, cutoff<4pg/mL OR<2%individualmax, Ln thenbacktransform. Caption times baseline,week4(plasmaonly),week8(serumonly),week16,week24. Printedplacebochange+11.6 (percent sign absent),active+0.8%,placebovsactive geometricmeanchange+9.7%,95%CI−0.1%to+18.5%,P0.051. This page contains caption text only in its supplied PDF/renderedimage; no hidden numerical plot inferred.

No XLS/XLSX/CSV/DOC/DOCX in this disjoint scope; workbook formulas/cached values do not apply. Administrative and rights content explicitly covered above. Legacy engine provenance is the only limitation; no extraction or visual-inspection gap remains.

## Source-level full quantitative transcriptions by actual PDF page

The page sections below are source-linked direct sorted-layout transcription, preserving all numeric cells, endpoint names, scales, models, timepoints and footnotes. OCR is not used. Text/image reading is a transcription aid; later candidate recheck must return to exact supplied PDF.

### DOC-004 PDF page 1

Source: [DOC-004 p.1](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=1). Relationship group SP6-N001; applicable statistical group as coverage table.

```text
                   Supplemental Online Content



 Writing Committee for the HEALEY ALS Platform Trial. CNM-Au8 in amyotrophic lateral
 sclerosis: the HEALEY ALS platform trial. JAMA. Published online February 17, 2025.
 doi:10.1001/jama.2024.27643



 eMethods
 eTable 1. Distribution of ALSFRS-R by visit and treatment group
 eTable 2. Primary Efficacy Analysis of Function and Mortality with Bayesian Shared
 Parameter Model
 eTable 3A. Results for secondary and exploratory outcomes using repeated-measures
 analysis using shared placebo participants (Full Analysis Set)
 eTable 3B. Results for secondary and exploratory outcomes using repeated-measures
 analysis using only Regimen C (CNM-Au8) placebo participants (Efficacy Regimen Only
 dataset)
 eTable 4. Subgroup Forest Plot for ALSFRS-R
 eTable 5. Treatment-Emergent Adverse Events (TEAE) with ≥5% incidence in either group
 eFigure. Serum Neurofilament Sensitivity Analysis



 This supplemental material has been provided by the authors to give readers additional
 information about their work.





© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 2

Source: [DOC-004 p.2](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=2). Relationship group SP6-N002; applicable statistical group as coverage table.

```text
                                                                                                                   1


eMethods



Trial Design and Oversight

The HEALEY ALS Platform Trial is a novel, efficient, perpetual design, platform trial designed to test multiple investigational

products against placebo in parallel. In this platform trial, each new investigational product is tested as a regimen specific appendix,

or “Regimen” to the master protocol. CNM-Au8 was evaluated in Regimen C (RGC) of the HEALEY ALS Platform Trial, a

randomized, double-blind, placebo-controlled trial enrolled and followed participants at 54 Northeast ALS Consortium (NEALS)

centers in the United States between July 2020 and March 2022. The trial was conducted in accordance with Good Clinical Practice

guidelines of the International Conference on Harmonization and ethical principles of the Declaration of Helsinki. Protocol approval

was provided for all trial sites by a central Institutional Review Board, the Massachusetts General Brigham Human Research

Committee. All participants provided written informed consent prior to screening.



The trial was designed by and conducted through the NEALS network, a global collaborative trial network (www.neals.org), in

collaboration with Clene Nanomedicine, Inc. (Clene). Participant-level data were obtained at each trial site and stored in the electronic

data capture system for the trial at Massachusetts General Hospital. An independent Data and Safety Monitoring Board reviewed

unblinded safety data at pre-defined intervals throughout the trial. Statistical analyses were performed by biostatisticians at Berry





                                                                                                                   1

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 3

Source: [DOC-004 p.3](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=3). Relationship group SP6-N003; applicable statistical group as coverage table.

```text
                                                                                                                   2


Consultants, Massachusetts General Hospital, and Pentara Corporation. Clene provided the active drug and placebo and was involved

in the trial design, data analysis, and manuscript review.



Trial Participants

Those who were eligible for the platform trial were adults with a diagnosis of clinically possible, probable, lab-supported probable, or

definite ALS defined by revised El Escorial criteria, disease duration ≤ 36 months, a vital capacity ≥ 50% predicted for age, height,

and sex, the ability to swallow pills and liquids, and either no use of riluzole and/or edaravone or stable dosing of riluzole and/or

edaravone for more than 30 days or one cycle, respectively. Those eligible for the CNM-Au8 regimen could not be allergic to gold.

Full inclusion and exclusion criteria can be viewed in the trial protocol available as a Supplement.



Randomization techniques

Both the randomization to regimen, which was not blinded, and the randomization to active drug or placebo within a regimen, which

was blinded to both participant and investigator, were done using as pre-determined randomization schedule. In order to ensure

balance in regimens and treatment groups by current medication use, both randomization schedules were stratified by baseline use of

riluzole and edaravone (4 strata total).


Random assignment to a regimen was done. Random assignment to a regimen within a stratum uses a block urn design (Zhao and

Wang; Block urn design - a new randomization algorithm for sequential trials with two or more treatments and balanced or

                                                                                                                   2

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 4

Source: [DOC-004 p.4](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=4). Relationship group SP6-N004; applicable statistical group as coverage table.

```text
                                                                                                                   3


unbalanced allocation. Contemp Clin Trials. 2011 Nov;32(6):953-61) with one instance of each regimen in a given block and modified

to remove from consideration any regimens to which the participant cannot be assigned (termed "unavailable regimens").


Within each strata a blocking schema was used to create the randomization schedule. Blocks were of size 8 (3 for 30mg, 3 for 60mg, 2

for Placebo). Randomization schedules were created using SAS software and validated to ensure no discernable patterns were seen

before implementation.



Trial Interventions and Procedures

Eligible participants were randomized 3:3:2 ratio to receive CNM-Au8 60mg daily, CNM-Au8 30mg daily, or matching placebo, with

stratification for edaravone and/or riluzole use. Trial duration was 24 weeks. Active drug and placebo were provided as liquid in

individual containers. Participants were instructed to take two 60mL bottles of study drug or placebo daily in the morning at least 30

minutes prior to food intake. For the 60mg dose, each bottle contained 30mg of CNM-Au8. For the 30mg dose, each bottle contained

15mg CNM-Au8. The primary analysis compared those receiving active CNM-Au8, at either the 60mg or 30mg daily dosage, to

placebo. Clinic visits were conducted at baseline, Weeks 4, 8, 16 and 24, and telephone visits at Weeks 2, 12, and 20, with a final

telephone follow-up at week 28. Participants who completed the randomized, double-blind trial were eligible for enrollment in an

open-label extension (OLE) evaluating the long-term effects of CNM-Au8 (NCT04414345).



Outcomes

                                                                                                                   3

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 5

Source: [DOC-004 p.5](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=5). Relationship group SP6-N005; applicable statistical group as coverage table.

```text
                                                                                                                   4


The primary endpoint was change in disease severity from baseline through 24 weeks as measured by the ALS Functional Rating

Scale revised (ALSFRS-R) total score and survival and analyzed using a Bayesian shared-parameter model (see Primary Analysis

Methods below).  Survival and PAV status were recorded during planned 24-week double-blind follow-up and censored at the last

date known alive if prior to the end of the week 24 visit window.



The three secondary clinical efficacy outcomes (in hierarchical order) included 1) the Combined Assessment of Function and Survival

(CAFS) model, a joint-rank test combining ALSFRS-R decline and survival free of permanent assisted ventilation (PAV), defined as

more than 22 hours daily for more than 7 days; 2) rate of decline in percent predicted of normal (PPN) slow vital capacity (SVC) and;

3) survival that is free of PAV.



Safety was assessed via documentation of treatment-emergent adverse events (TEAEs) at each trial visit. Symptoms of ALS

progression, including those consistent with disease progression, were recorded as TEAEs. Any worsening of a disease progression

measure that was being recorded and analyzed separately (i.e., ALSFRS-R or SVC) was not recorded as a TEAE. Safety was

additionally assessed based on laboratory assays, vital signs, electrocardiograms, and the Columbia Suicide Severity Rating Scale (C-

SSRS).



Pre-specified exploratory measures included: 4 biofluid biomarkers (serum and CSF neurofilament light (NfL), serum creatinine,


                                                                                                                   4

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 6

Source: [DOC-004 p.6](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=6). Relationship group SP6-N006; applicable statistical group as coverage table.

```text
                                                                                                                   5


urinary p75 extracellular domain (p75ecd), ; 6 clinical outcome measures (HHD), quantitative motor speech (9 features), home vital

capacity, ALSFRS-R domain scores, the ALS Assessment Questionnaire (ALSAQ-40) and its domain scores, and the Center for

Neurologic Study – Bulbar Function Scale (CNS-BFS); and 11 time-to-event analyses (3 events related to cutoffs in trial endpoints,

such as time to decline of at least 6 points on the ALSFRS-R, and 8 exploring clinical events such as time to first serious adverse

event). Plasma NfL was added later as a post-hoc analysis. Only relevant exploratory analyses are presented in this manuscript.

Details about all exploratory measures and their analyses can be found in the statistical analysis plan (available as a Supplement).



Analysis of Dosages

The main analysis for primary, secondary, safety and exploratory measures was on the combined 30mg and 60mg daily dosages

compared to placebo. Prespecified exploratory analyses compared each dose to placebo directly for all primary, secondary, and

exploratory endpoints.



Analysis Populations

The primary analysis population for both the primary and secondary endpoints, referred to as the Full Analysis Set (FAS), included all

participants randomized to the Regimen C active treatment arm, all participants randomized to the placebo arm within Regimen C, and

all placebo participants from Regimens A, B, and D. Participants were analyzed according to the treatment group to which they were

randomized within their respective regimen to estimate a treatment policy estimand. Additional prespecified efficacy analyses were


                                                                                                                   5

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 7

Source: [DOC-004 p.7](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=7). Relationship group SP6-N007; applicable statistical group as coverage table.

```text
                                                                                                                   6


performed using only Regimen C participants (CNM-Au8 and placebo), called the regimen-only analyses. Safety analyses were

performed in an equivalent full analysis set for safety that included all Regimen C participants who initiated treatment and all placebo

participants from Regimens A, B, and D except those who were known to be ineligible for the CNM-Au8 regimen (i.e., those with

gold allergy).



The primary analysis on the FAS used longitudinal ALSFRS-R scores from all scheduled visits (Weeks 0, 4, 8, 12, 16, 20 and 24) or

from any early termination or ad hoc visits substituting for a planned visit.



Primary analysis methods

The primary analysis is a Bayesian shared parameter model of function and survival that provides an integrated estimate of the

increase or decrease in the rate of disease progression on treatment relative to control. The analysis model has components for each

endpoint that are linked through an integrated estimate of disease slowing in treatment relative to control across the two endpoints

(denoted as the disease rate ratio, or DRR). This composite variable strategy fully incorporates effects of treatment on the intercurrent

event of death. The DRR measures the ratio of ALSFRS-R slopes within the functional component or the hazard ratio within the

survival component with values less than 1 indicating slowing in disease progression  This parameter can be interpreted as the

slowing in the rate of disease progression measured across both endpoints. A DRR of 0.50 corresponds to a 50% slowing in the rate

of disease progression. If a participant in the control group would be expected to decrease 6 points over 6 months, then under a DRR


                                                                                                                   6

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 8

Source: [DOC-004 p.8](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=8). Relationship group SP6-N008; applicable statistical group as coverage table.

```text
                                                                                                                   7


of 0.50, they would be expected to reach the same milestone (ALSFRS-R decrease of 6 points) over 12 months on treatment.

Similarly for survival, if they were expected to survive for a median time of 9 months on control, under the treatment they would be

expected to survive for 18 months.  In the functional component, ALSFRS-R is measured for those who have survived using a linear

repeated measure model that adjusts for baseline covariates and accommodates potential differences in the shared control across

regimens. The survival component is measured through an exponential proportional hazards model. The shared treatment effect

between the ALSFRS-R and mortality components allows the participants who were lost to follow-up due to mortality to inform

treatment effect estimates beyond their censored ALSFRS-R longitudinal data. The degree to which treatment effects on mortality

inform the shared-treatment effect parameter depends on the mortality rate within the study.

The primary analysis includes concurrent shared controls across regimens.  It is expected that there will not be systematic differences

in rates of progression in controls across regimens. The platform enrols participants under the same master protocol, across the same

sites, during the same time period, and with only very minor differences in regimen-specific inclusion/exclusion. However, minor

differences across the shared controls may be present due to these minor differences in inclusion/exclusion and due to differences in

the modes of administration. To account for these potential differences, the primary analysis is conducted within a Bayesian

hierarchical meta-analytic framework. As such, the regimen-specific random effects on the rate of progression for controls are

assumed to come from an underlying hierarchical distribution with unknown population mean and variability. The population mean

and variability (hyper-parameters) within the hierarchical distribution are given a prior distribution, and posterior estimates are

obtained from the data. If the variability in the rate of progression is estimated to be small, the model will borrow more information


                                                                                                                   7

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 9

Source: [DOC-004 p.9](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=9). Relationship group SP6-N009; applicable statistical group as coverage table.

```text
                                                                                                                   8


across regimens and the analysis will be similar to a pooled analysis across regimens.  If the variability in the rate of progression is

estimated to be large across regimens, the model will borrow less across regimens and the analysis will be similar to an independent

analysis across regimens.

The Bayesian posterior distribution of all model parameters is calculated using Markov chain Monte Carlo (MCMC). We drew at least

500,000 samples from the posterior distribution with a thinning of 10. The exact number of samples from the MCMC was determined

based on convergence diagnostics to ensure an adequate effective sample size of the posterior distribution.

Prespecified sensitivity analyses, including CAFS, which was employed as a sensitivity analysis, in addition to a secondary endpoint,

were performed to assess the sensitivity of the results to the primary analysis population, modeling assumptions, and missing data

assumptions as described in Statistical Analysis Plan (available as a Supplement).



Interim Analyses

A regimen could be stopped early should prespecified interim analyses indicate futility. Interim analyses occurred simultaneously for

all actively enrolling regimens and included any regimen within the master protocol that had 40 active randomized participants (30

study drug and 10 placebo). Subsequent interim analyses occurred every 12 weeks. As described in the master protocol, early futility

would be declared if the regimen had a posterior probability of <5% that CNM-Au8 would slow ALSFRS-R decline by at least 10%.

There was no stopping rule for early success.





                                                                                                                   8

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 10

Source: [DOC-004 p.10](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=10). Relationship group SP6-N010; applicable statistical group as coverage table.

```text
                                                                                                                   9


Secondary efficacy analysis methods

SVC was assessed using both a repeated measures linear mixed model and random slopes model with the following covariates,

centered to the analysis population: months since symptom onset, pre-baseline change in ALSFRS-R slope (delta-FRS), baseline

riluzole and edaravone use, and their interaction with time. Models run on the full analysis set, which includes shared placebos from

other regimens, random regimen-specific intercepts are included.



Each participant’s vital status was verified at the time of the last patient last visit in the RCT. Rates of death, death-equivalent events

(permanent assisted ventilation (PAV) defined as use of ventilation for >22 hours per day for more than 7 days in a row), and

hospitalization were analyzed using a Cox proportional hazards model, with covariates of pre-baseline ALSFRS-R slope, months since

symptom onset, riluzole and edaravone use at baseline, and age at baseline. A separate supportive analysis was run which included

centered baseline serum NfL level and the interaction of centered baseline serum NfL level and visit as additional covariates.





Exploratory Analyses

As a part of the Healey Platform Trial Master Protocol, serum was analyzed using single molecule array (Simoa) testing, a digital

immunoassay (Quanterix) as a single-plex assay. Two replicates from each aliquot were performed. If the sample NfL was below the


                                                                                                                   9

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 11

Source: [DOC-004 p.11](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=11). Relationship group SP6-N011; applicable statistical group as coverage table.

```text
                                                                                                                 10


limit of detection or only one replicate yielded an NfL concentration, the replicates were repeated.  If the coefficient of variation (CV)

for these two replicates was >25%, the replicates were repeated; the repeat replicates were used unless their CV was higher than the

original.  If a serum sample value was <LOQ, the value was imputed by using the assay LOD. For the primary analysis, no outliers

were omitted.



Serum NfL in the Full Analysis set was the prespecified exploratory endpoint for NfL. However, for this regimen, serum samples

were tested with all longitudinal samples from a single participant tested on the same plate (different than other regimens). Only

regimen samples were tested in this way, thus a post-hoc exploratory analysis of only regimen samples is presented. In addition,

plasma samples were tested using a multiplex assay (Neurology 4 Plex-A, Quanterix) that included NfL, glial fibrillary acidic protein

(GFAP), tau, and ubiquitin carboxy-terminal hydrolase L1 (UCH-L1) with two replicates from each aliquot performed. The plasma

analysis was pre-specified in Clene Nanomedicine’s Pharmacodynamic SAP originally as UCH-L1 alone, but due to non-availability

of the UCH-L1 assay the Neurology 4 Plex-A (including NfL) was analyzed, thus it is considered post-hoc for the purposes of this

manuscript.



Sites were instructed to process serum and plasma samples within 30 minutes of collection and stored at -80C for batch shipment to

the lab using standard operating procedures as described in prior studies. Samples were tested on a 96-well plate with high and low-

level quality control standards to allow for correction of plate-to-plate variability. NfL values were log-transformed prior to analysis.


                                                                                                                 10

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 12

Source: [DOC-004 p.12](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=12). Relationship group SP6-N012; applicable statistical group as coverage table.

```text
                                                                                                                 11


Data was analyzed by mixed model repeat measures (MMRM) with prespecified covariates including pre-treatment ALSFRS-R slope

(delta-FRS), months from symptom onset, use of riluzole, use of edaravone; covariate by visit interaction, and treatment by visit

interaction. NfL was analyzed in the regimen only dataset. For the primary analyses of neurofilament, all values obtained were

included in the analysis (i.e., no outliers were excluded). To assess whether the serum NfL result was sensitive to outliers, a post hoc

analysis was performed that excluded outliers (observations with very low NfL values, namely those <4 pg/mL or <2% of the

maximum for a given participant. This excluded one baseline NfL for one participant in the placebo group.



Urinary p75 extracellular domain (p75ecd) was analyzed at Flinders University in the Rogers Lab. Urinary p75 extracellular domain

was quantified using a sandwich enzyme-linked immunosorbent assay (ELISA) in 96-well plates, as previously described. Only

samples from the CNM-Au8 regimen were analyzed for urinary p75ecd.



Prespecified exploratory outcomes for time to event analyses included time to hospitalization, placement of a feeding tube, use of

assisted ventilation, King’s Stage 4, death alone, and death or PAV. Analysis used an adjusted Cox regression using the same

covariates described for the primary endpoint as well as participant age. King’s stage analysis was interval censored; other variables

were right censored. Death or PAV was censored at the time the participant was last known to be alive.



Subgroup Analyses


                                                                                                                 11

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 13

Source: [DOC-004 p.13](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=13). Relationship group SP6-N013; applicable statistical group as coverage table.

```text
                                                                                                                 12


Differences in treatment efficacy were explored in several prespecified subgroups: baseline riluzole use (yes vs. no), and baseline

edaravone use (yes vs. no), age (<65 years vs 65 or older), sex, race, ethnicity, weight categories, BMI categories, chronic kidney

disease stage, time since onset of weakness (<18 months vs 18 months or more), El Escorial criteria with time since onset of

weakness, baseline symptom severity (all ALSFRS-R questions scored 2 or greater vs any scored 0 or 1), early disease state, baseline

serum urate concentration (<5.5mg/dL vs 5.5mg/dL or greater), baseline serum NfL concentration (median split), site of onset (any

bulbar vs none), pre-baseline rate of progression by delta-FRS (fast vs. slow with median split), and clinic site (sites with <5

participants were pooled). Subgroup specific estimates will be obtained by including subgroup, subgroup × time, and subgroup ×

treatment × time terms to a random-slope model for primary and secondary efficacy endpoints using the FAS population.





                                                                                                                 12

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 14

Source: [DOC-004 p.14](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=14). Relationship group SP6-N014; applicable statistical group as coverage table.

```text
                                                                                                                 13

eTable 1. Distribution of ALSFRS-R by visit and treatment group



                    CNM-Au8 pooled             Shared Placebo           Regimen Placebo

          Visit            n       mean (SD)       n       mean (SD)       n      mean (SD)
        Baseline           120          34.3 (6.6)        164         35.1 (6.7)        41         36.1 (5.9)
      Week 4           120          33.0 (7.0)        160         34.5 (7.0)        40         35.4 (6.7)
      Week 8           115          32.3 (7.3)        155         33.4 (7.4)        38         34.3 (7.1)
     Week 12           115          31.4 (7.7)        152         32.7 (7.9)        39         33.7 (7.9)
     Week 16           110          30.5 (7.7)        148         31.8 (8.3)        36         32.5 (7.5)
     Week 20           111          29.7 (7.8)        143         31.2 (8.6)        36         32.6 (7.9)
     Week 24           111          29.1 (7.9)        143         30.2 (8.7)        35         31.4 (8.2)





                                                                                                                 13

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 15

Source: [DOC-004 p.15](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=15). Relationship group SP6-N015; applicable statistical group as coverage table.

```text
                                                                                                                 14

eTable 2. Primary Efficacy Analysis of Function and Mortality with Bayesian Shared Parameter Model

                                                       95%
  Parameter                         Median      Mean (SD)                      Pr(DRR < 1.0)    Pr(DRR < 0.9)
                                                                          Credible Interval
  DRR
       Function and Mortality                  0.96         0.97 (0.099)          (0.783, 1.175)           0.6450            0.2505
  ALSFRS-R Slopes (points per month)
      Regimen C placebo w/ sharing         −1.03       −1.03 (0.073)       (−1.181, −0.894)
       Pooled CNM-Au8                   −1.00       −1.00 (0.075)       (−1.143, −0.847)
   Mortality Event Rate (events per month)
       Shared placebo                        0.010       0.010 (0.0026)        (0.0054, 0.0154)
       Pooled CNM-Au8                     0.009       0.009 (0.0025)        (0.0052, 0.0150)
   Covariates
      Months since onset                     1.03         1.03 (0.046)          (0.938, 1.120)
        Pre-baseline Slope                      1.39         1.40 (0.079)          (1.255, 1.565)
       Edaravone Use                         1.13         1.13 (0.101)          (0.949, 1.344)
        Riluzole Use                           1.03         1.03 (0.093)          (0.854, 1.220)

    Abbreviations: DRR = Disease Rate Ratio
    Note: The Bayesian shared parameter model includes covariates for baseline use of Edaravone, baseline use of Riluzole, months since onset
    of symptoms, and pre-baseline slope of ALSFRS-R.





                                                                                                                 14

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 16

Source: [DOC-004 p.16](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=16). Relationship group SP6-N016; applicable statistical group as coverage table.

```text
                                                                                                                 15

eTable 3A. Results for secondary and exploratory outcomes using repeated-measures analysis using shared placebo
participants (Full Analysis Set)

    FAS Population            24-week Change Estimate                   Difference from Shared Placebo


        Endpoint                                                     Difference (SE)      95% CI       Pvalue                   CNM-Au8 Pooled       Shared
                               (n=120)        Placebo (n=164)

 ALSFRS-R total Score          -5.47 (0.43)           -5.51 (0.36)             0.0 (0.55)           -1.03, 1.11        0.94

 SVC (% predicted)             -9.32 (1.36)           -8.53 (1.15)            -0.78 (1.77)          -4.25, 2.68        0.66



      Dose Specific                                                                       Difference (SE)      95% CI     P value                   CNM-Au8 30 mg        Shared
                               (n=59)         Placebo (n=164)

 ALSFRS-R total Score         -5.70 (0.59)           -5.51 (0.36)            -0.19 (0.69)          -1.53, 1.16        0.79

 SVC (% predicted)             -7.84 (1.84)           -8.53 (1.15)            0.69 (2.19)           -3.55, 4.92        0.75



                   CNM-Au8 60 mg        Shared           Difference (SE)      95% CI      P value
                               (n=61)         Placebo (n=164)

 ALSFRS-R total Score         -5.24 (0.59)           -5.51 (0.36)            0.27 (0.68)           -1.07, 1.60        0.69

 SVC (% predicted)           -10.79 (1.99)          -8.53 (1.15)            -2.26 (2.29)          -6.75, 2.24        0.33





                                                                                                                 15

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 17

Source: [DOC-004 p.17](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=17). Relationship group SP6-N017; applicable statistical group as coverage table.

```text
                                                                                                                 17

eTable 3B. Results for secondary and exploratory outcomes using repeated-measures analysis using only Regimen C (CNM-Au8)
placebo participants (Efficacy Regimen Only dataset)

  ERO Population       24-week Change Estimate           Difference from Regimen Placebo


     Endpoint                                           Difference (SE)    95% CI    P value
               CNM-Au8 Pooled    Regimen
                         (n=120)      Placebo (n=41)
 ALSFRS-R total
                          -5.45 (0.44)        -5.39 (0.71)        -0.07 (0.83)       -1.71, 1.57      0.94
  Score
 SVC (% predicted)      -9.57 (1.38)        -6.74 (2.29)        -2.83 (2.67)       -8.10, 2.44      0.29

  Plasma NfL (% change)       -2.3              7.9                 -9.5             -18.0, 0        0.04
 Serum NfL (% change)        0.4              26.8               -26.4          -50.3, -2.6       0.03


    Dose Specific                                                           Difference (SE)    95% CI    P value
               CNM-Au8 30 mg    Regimen
                          (n=59)       Placebo (n=41)
 ALSFRS-R total
                          -5.56 (0.60)        -5.39 (0.71)        -0.17 (0.93)       -2.00, 1.66      0.85
  Score
 SVC (% predicted)      -7.61 (1.86)        -6.74 (2.29)        -0.87 (2.94)       -6.69, 4.95      0.77

  Plasma NfL (% change)       -1.3              7.9                 -8.5             -18, 2         0.10
 Serum NfL (% change)        1.4              26.8               -25.5           -52.2, 1.3       0.06
               CNM-Au8 60 mg    Regimen
                                                           Difference (SE)    95% CI     P value
                          (n=61)       Placebo (n=41)
 ALSFRS-R total
                         -5.35 (0.61)        -5.39 (0.71)        0.04 (0.93)       -1.79, 1.87      0.97
  Score
 SVC (% predicted)     -11.53 (1.98)       -6.74 (2.29)        -4.79 (3.03)      -10.76, 1.19      0.12

  Plasma NfL (% change)       -3.4              7.9               -10.5             -20, 0         0.04
 Serum NfL (% change)        -0.5             26.8               -27.4          -45.1, -0.7       0.05
FAS = Full Analysis Set (includes shared placebos), ERO = Efficacy Regimen Only (includes only regimen-specific placebos),
ALSFRS-R = Amyotrophic Lateral Sclerosis Functional Rating Scale – Revised; SVC = Slow Vital Capacity; CI = confidence interval; SE = standard error; NfL = Neurofilament
Light; GMR – geometric mean ratio
*Serum and plasma NfL was modeled as log-transformed and exponentiated back to the original scale to present results.
Models adjusted for time since symptom onset, pre-baseline ALSFRS-R slope, edaravone use at baseline, riluzole use at baseline and their interactions with visit.


                                                                                                                 17

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 18

Source: [DOC-004 p.18](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=18). Relationship group SP6-N018; applicable statistical group as coverage table.

```text
                                                                                                                       19

     eTable 4. Subgroup Forest Plot for ALSFRS-R

     This forest plot shows the behavior of the Amyotrophic Lateral Sclerosis Functional Rating Scale – Revised (ALSFRS-R) in multiple
      subgroups, comparing the combined (pooled) CNM-Au8 arm to the shared placebo arm using a linear mixed model approach as
      described in the methods section. For each subgroup, the difference between the estimated slopes for the CNM-Au8 arm and the
     placebo arm is shown as a point estimate on the plot with 95% confidence intervals (95%CI) represented as the horizontal solid line.
     The vertical dashed line represents “no difference.” In every subgroup analyzed, the 95% CI crosses the “no difference” line,
      indicating that no subgroups showed a statistically significant benefit from CNM-Au8 on the slope of ALSFRS-R decline.



                                                                                              Plot                DifferenceSubgroup                CNM AU8 Pooled  Placebo Slope                                                            p-value


All Participants                       -0.98 (-1.13,-0.82)    -1.01 (-1.13,-0.88)                                      0.03 (-0.16,0.23)
Riluzole Use
    N                               -1.07 (-1.39,-0.75)    -0.88 (-1.15,-0.61)                                       -0.19 (-0.60,0.22)     0.22
    Y                               -0.95 (-1.12,-0.78)    -1.05 (-1.19,-0.90)                                      0.10 (-0.12,0.32)
Edaravone Use
    N                               -1.00 (-1.17,-0.83)    -0.96 (-1.10,-0.81)                                       -0.04 (-0.27,0.18)     0.19
    Y                               -0.91 (-1.22,-0.60)    -1.17 (-1.43,-0.90)                                      0.26 (-0.14,0.66)
Riluzole & Edaravone Use
      Neither                          -1.15 (-1.49,-0.81)    -0.82 (-1.10,-0.54)                                       -0.33 (-0.77,0.10)
      Riluzole Only                   -0.94 (-1.14,-0.75)    -1.01 (-1.18,-0.83)                                      0.06 (-0.20,0.32)
      Edaravone Only                 -0.49 (-1.45,0.47)     -1.38 (-2.27,-0.49)                                      0.89 (-0.42,2.20)
     Both                            -0.96 (-1.28,-0.64)    -1.15 (-1.43,-0.88)                                      0.19 (-0.23,0.61)
Age Group
     < 65                            -0.97 (-1.15,-0.80)    -1.03 (-1.18,-0.88)                                      0.05 (-0.18,0.28)      0.81
     >= 65                           -0.95 (-1.23,-0.68)    -0.95 (-1.19,-0.71)                                      0.00 (-0.36,0.36)



                                                                                                                       19

                   © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 19

Source: [DOC-004 p.19](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=19). Relationship group SP6-N019; applicable statistical group as coverage table.

```text
                                                                                                                       20


                                                                                              Plot                DifferenceSubgroup                CNM AU8 Pooled  Placebo Slope                                                            p-value


Sex
     F                               -0.98 (-1.22,-0.74)    -1.10 (-1.33,-0.87)                                      0.12 (-0.21,0.45)      0.50
   M                               -0.99 (-1.18,-0.80)    -0.97 (-1.12,-0.81)                                       -0.02 (-0.27,0.22)
Race
     White                           -0.95 (-1.10,-0.80)    -1.01 (-1.14,-0.88)                                      0.06 (-0.14,0.25)
Ethnicity
     Not Hispanic or Latino           -0.97 (-1.13,-0.82)    -1.01 (-1.14,-0.88)                                      0.04 (-0.16,0.24)
Weight Group
     < 56 kg                         -1.39 (-2.02,-0.76)    -1.14 (-1.73,-0.55)                                       -0.25 (-1.11,0.60)
     56 to <77 kg                     -0.93 (-1.18,-0.68)    -1.04 (-1.25,-0.83)                                      0.11 (-0.21,0.43)
     77 to <150 kg                   -0.95 (-1.14,-0.75)    -0.97 (-1.14,-0.80)                                      0.03 (-0.23,0.28)
BMI Group
     < 18.5 kg/m2                    -0.43 (-1.50,0.63)     -1.40 (-2.30,-0.49)                                      0.96 (-0.43,2.35)
      18.5 to < 25 kg/m2               -1.03 (-1.29,-0.78)    -1.07 (-1.28,-0.85)                                      0.03 (-0.30,0.36)
     25 to < 30 kg/m2                -0.95 (-1.18,-0.72)    -0.93 (-1.13,-0.73)                                       -0.02 (-0.33,0.28)
     30 to < 40 kg/m2                -1.00 (-1.32,-0.68)    -1.09 (-1.36,-0.82)                                      0.09 (-0.33,0.50)
     >= 40 kg/m2                    -0.35 (-1.26,0.56)     -0.15 (-1.05,0.76)                                        -0.21 (-1.49,1.07)
Chronic Kidney Disease
      Stage 1 or better                 -0.99 (-1.16,-0.81)    -1.04 (-1.20,-0.88)                                      0.05 (-0.18,0.29)
      Stage 2                          -0.92 (-1.22,-0.63)    -0.92 (-1.15,-0.69)                                      0.00 (-0.38,0.37)
Time Since Symptom Onset
     < 18 monthss                    -0.99 (-1.28,-0.69)    -0.95 (-1.22,-0.68)                                       -0.04 (-0.37,0.30)     0.59
     >= 18 months                    -0.96 (-1.18,-0.75)    -1.04 (-1.23,-0.85)                                      0.08 (-0.16,0.32)


                                                                                                                       20

                   © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 20

Source: [DOC-004 p.20](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=20). Relationship group SP6-N020; applicable statistical group as coverage table.

```text
                                                                                                                       21


                                                                                              Plot                DifferenceSubgroup                CNM AU8 Pooled  Placebo Slope                                                            p-value


El Escorial Definite & Time Since
Symptom Onset

      Definite and < 18 months        -1.05 (-1.40,-0.71)    -1.25 (-1.65,-0.86)                                      0.20 (-0.29,0.69)      0.53
     Not Definite and < 18 months    -0.95 (-1.12,-0.77)    -0.97 (-1.11,-0.84)                                      0.03 (-0.19,0.24)
Baseline Symptom Severity Group
      All ALSFRS-R Items >= 2       -0.99 (-1.31,-0.67)    -0.88 (-1.11,-0.65)                                       -0.11 (-0.50,0.27)     0.38
     >= 1 ALSFRS-R Items < 2       -0.99 (-1.17,-0.81)    -1.08 (-1.25,-0.91)                                      0.09 (-0.13,0.32)
Baseline NFL Group
     NfL < Median                   -0.85 (-1.07,-0.64)    -0.95 (-1.12,-0.78)                                      0.10 (-0.17,0.36)      0.74
     NfL >= Median                  -1.04 (-1.25,-0.83)    -1.07 (-1.26,-0.88)                                      0.03 (-0.25,0.31)
Fast vs. Slow Progressors
     dFRS < Median                  -0.84 (-1.07,-0.62)    -0.91 (-1.09,-0.72)                                      0.06 (-0.21,0.34)      0.70
     dFRS >= Median                -1.16 (-1.41,-0.90)    -1.14 (-1.36,-0.93)                                       -0.01 (-0.29,0.27)





                                                                                                                       21

                   © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 21

Source: [DOC-004 p.21](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=21). Relationship group SP6-N021; applicable statistical group as coverage table.

```text
                                                                                                                 22

eTable 5. Treatment-Emergent Adverse Events (TEAE) with ≥5% incidence in either group

Treatment
                                                                            Regimen-
Emergent        Pooled CNM-    CNM-Au8     CNM-Au8       Shared
                                                                                               Specific
Adverse Events  Au8             30mg         60mg          Placebo
                                                                                   Placebo
(TEAE)

                   (N=120)         (N=59)         (N=61)         (N=163)         (N=41)

               Number of        Number of      Number of      Number of      Number of
MedDRA SOC    Participants         Participants       Participants       Participants       Participants
Preferred Term    (%), Number of   (%), Number of   (%), Number of   (%), Number of   (%), Number of
                   events                events            events            events            events
                 111 (92.5%),                                  146 (89.6%),
Any TEAE                      54 (91.5%), 293  57 (93.4%), 430                 38 (92.7%), 228
                     723                                          889
Mild            41 (34.2%), 500
                               21 (35.6%), 205  20 (32.8%), 295  68 (41.7%), 673  13 (31.7%), 151

Moderate        44 (36.7%), 165  22 (37.3%), 66   24 (39.3%), 99   53 (32.5%), 164   15 (36.6%), 61
Severe            24 (20%), 58    11 (18.6%), 22   13 (21.3%), 36   25 (15.3%), 47   10 (24.4%), 16
Serious TEAEs    16 (13.3%), 20    6 (10.2%), 9    10 (16.4%), 11    15 (9.2%), 21    7 (17.1%), 12
Treatment-
Related Serious     0 (0.0%), 0      0 (0.0%), 0      0 (0.0%), 0      2 (1.2%), 3      1 (2.4%), 2
TEAE
Deaths            4 (3.3%), 4      1 (1.7%), 1      3 (4.9%), 3      4 (2.5%), 4      2 (4.9%), 2
TEAEs Leading
to Study Drug      8 (6.7%), 8      4 (6.8%), 4      4 (6.6%), 4     11 (6.7%), 17     3 (7.3%), 4
Withdrawal
TEAEs Leading
to Study Drug      9 (7.5%), 15    6 (10.2%), 11     3 (4.9%), 4     12 (7.4%), 24     4 (9.8%), 6
Interruption




                                                                                                                 22

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 22

Source: [DOC-004 p.22](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=22). Relationship group SP6-N022; applicable statistical group as coverage table.

```text
                                                                                                                 23


Treatment
                                                                            Regimen-
Emergent        Pooled CNM-    CNM-Au8     CNM-Au8       Shared
                                                                                               Specific
Adverse Events  Au8             30mg         60mg          Placebo
                                                                                   Placebo
(TEAE)

                   (N=120)         (N=59)         (N=61)         (N=163)         (N=41)

              Number of        Number of      Number of      Number of      Number of
MedDRA SOC    Participants         Participants       Participants       Participants       Participants
Preferred Term    (%), Number of   (%), Number of   (%), Number of   (%), Number of   (%), Number of
                   events                events            events            events            events
TEAEs Leading
to Study Drug      3 (2.5%), 5      0 (0.0%), 0      3 (4.9%), 5      5 (3.1%), 12      1 (2.4%), 1
Reduction
Fall             26 (21.7%), 44   13 (22.0%), 22   13 (21.3%), 22   43 ( 26.4%), 79   13 ( 31.7%), 17
Muscular
                24 (20.0%), 39   10 (16.9%), 18   14 (23.0%), 21   45 ( 27.6%), 67   12 ( 29.3%), 17
weakness
Diarrhoea        23 (19.2%), 33   9 (15.3%), 12    14 (23.0%), 21   12 ( 7.4%), 14     4 ( 9.8%), 5
Nausea          17 (14.2%), 21   9 (15.3%), 10    8 (13.1%), 11    14 ( 8.6%), 16    6 ( 14.6%), 8
Fatigue          13 (10.8%), 17    6 (10.2%), 8     7 (11.5%), 9    30 ( 18.4%), 33    9 ( 22.0%), 9
Headache        17 (14.2%), 26   9 (15.3%), 17     8 (13.1%), 9    19 ( 11.7%), 23    4 ( 9.8%), 6
Neuromyopathy   14 (11.7%), 21    6 (10.2%), 8     8 (13.1%), 13   22 ( 13.5%), 33    6 ( 14.6%), 7
Constipation      17 (14.2%), 19    4 (6.8%), 4     13 (21.3%), 15   20 ( 12.3%), 24    3 ( 7.3%), 4
Dyspnoea        13 (10.8%), 14    7 (11.9%), 8      6 (9.8%), 6     10 ( 6.1%), 11     4 ( 9.8%), 5
Dysarthria        15 (12.5%), 16   9 (15.3%), 10     6 (9.8%), 6     11 ( 6.7%), 13     2 ( 4.9%), 2
Dysphagia        10 (8.3%), 10    6 (10.2%), 6      4 (6.6%), 4    18 ( 11.0%), 22    5 ( 12.2%), 6
Oedema
                 7 (5.8%), 13     2 (3.4%), 3      5 (8.2%), 10    12 ( 7.4%), 15     4 ( 9.8%), 4
peripheral
Tension
                 7 (5.8%), 10     1 (1.7%), 1      6 (9.8%), 9     10 ( 6.1%), 15     4 ( 9.8%), 4
headache





                                                                                                                 23

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 23

Source: [DOC-004 p.23](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=23). Relationship group SP6-N023; applicable statistical group as coverage table.

```text
                                                                                                                 24


Treatment
                                                                            Regimen-
Emergent        Pooled CNM-    CNM-Au8     CNM-Au8       Shared
                                                                                               Specific
Adverse Events  Au8             30mg         60mg          Placebo
                                                                                   Placebo
(TEAE)

                   (N=120)         (N=59)         (N=61)         (N=163)         (N=41)

              Number of        Number of      Number of      Number of      Number of
MedDRA SOC    Participants         Participants       Participants       Participants       Participants
Preferred Term    (%), Number of   (%), Number of   (%), Number of   (%), Number of   (%), Number of
                   events                events            events            events            events
Urinary tract
                 10 (8.3%), 13     4 (6.8%), 6      6 (9.8%), 7     10 ( 6.1%), 10     1 (2.4%), 1
infection
Arthralgia         6 (5.0%), 12     3 (5.1%), 8      3 (4.9%), 4      6 (3.7%), 6      3 (7.3%), 3
Vomiting          6 (5.0%), 9      4 (6.8%), 5      2 (3.3%), 4      6 (3.7%), 6      2 (4.9%), 2
Amyotrophic
                 8 (6.7%), 10     2 (3.4%), 2      6 (9.8%), 8      1 (0.6%), 1      0 (0.0%), 0
lateral sclerosis
Skin laceration      6 (5.0%), 7      2 (3.4%), 2      4 (6.6%), 5      4 (2.5%), 8      2 (4.9%), 2
Cough            7 (5.8%), 7      1 (1.7%), 1      6 (9.8%), 6      4 (2.5%), 4      1 (2.4%), 1
Decreased
                  5 (4.2%), 5      2 (3.4%), 2      3 (4.9%), 3     12 (7.4%), 13     3 (7.3%), 3
appetite
Insomnia          5 (4.2%), 6      0 (0.0%), 0      5 (8.2%), 6      2 (1.2%), 2      2 (4.9%), 2
Salivary
                  5 (4.2%), 6      1 (1.7%), 1      4 (6.6%), 5      9 (5.5%), 9      2 (4.9%), 2
hypersecretion
Depression         3 (2.5%), 3      1 (1.7%), 1      2 (3.3%), 2      8 (4.9%), 8      4 (9.8%), 4
Faeces
                  7 (5.8%), 7      1 (1.7%), 1      6 (9.8%), 6      0 (0.0%), 0      0 (0.0%), 0
discoloured
Post-traumatic
                  4 (3.3%), 4      2 (3.4%), 2      2 (3.3%), 2      6 (3.7%), 6      3 (7.3%), 3
pain
Weight
                  2 (1.7%), 2      0 (0.0%), 0      2 (3.3%), 2       5( 3.1%), 5      5 (12.2%), 5
decreased
Pain in extremity    5 (4.2%), 7      1 (1.7%), 1      4 (6.6%), 6      9 (5.5%), 10      1 (2.4%), 1



                                                                                                                 24

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 24

Source: [DOC-004 p.24](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=24). Relationship group SP6-N024; applicable statistical group as coverage table.

```text
                                                                                                                 25


Treatment
                                                                            Regimen-
Emergent        Pooled CNM-    CNM-Au8     CNM-Au8       Shared
                                                                                               Specific
Adverse Events  Au8             30mg         60mg          Placebo
                                                                                   Placebo
(TEAE)

                   (N=120)         (N=59)         (N=61)         (N=163)         (N=41)

              Number of        Number of      Number of      Number of      Number of
MedDRA SOC    Participants         Participants       Participants       Participants       Participants
Preferred Term    (%), Number of   (%), Number of   (%), Number of   (%), Number of   (%), Number of
                   events                events            events            events            events
Pruritus           6 (5.0%), 8      0 (0.0%), 0      6 (9.8%), 8      4 (2.5%), 6      0 (0.0%), 0
Dizziness          4 (3.3%), 4      3 (5.1%), 3      1 (1.6%), 1     10 (6.1%), 13     2 (4.9%), 3
Increased upper
                  5 (4.2%), 6      3 (5.1%), 4      2 (3.3%), 2      4 (2.5%), 4      1 (2.4%), 1
airway secretion
Anxiety           4 (3.3%), 4      0 (0.0%), 0      4 (6.6%), 4      8 (4.9%), 8      2 (4.9%), 2
COVID-19         3 (2.5%), 3      2 (3.4%), 2      1 (1.6%), 1     11 ( 6.7%), 11     3 (7.3%), 3
Pulmonary
                  5 (4.2%), 5      1 (1.7%), 1      4 (6.6%), 4      2 (1.2%), 2      1 (2.4%), 1
embolism
Sinusitis           6 (5.0%), 6      4 (6.8%), 4      2 (3.3%), 2      0 (0.0%), 0      0 (0.0%), 0
Asthenia             4.(3.3%), 5      0 (0.0%), 0      4 (6.6%), 5      2 (1.2%), 2      1 (2.4%), 1
Back pain          5 (4.2%), 6      3 (5.1%), 4      2 (3.3%), 2      4 (2.5%), 10      0 (0.0%), 0
Flatulence         5 (4.2%), 5      0 (0.0%), 0      5 (8.2%), 5      0 (0.0%), 0      0 (0.0%), 0
Complication
associated with      3 (2.5%), 4      3 (5.1%), 4      0 (0.0%), 0      3 (1.8%), 3      0 (0.0%), 0
device
Alanine
aminotransferase    3 (2.5%), 3      3 (5.1%), 3      0 (0.0%), 0      2 (1.2%), 2      0 (0.0%), 0
increased
Aspartate
aminotransferase    3 (2.5%), 3      3 (5.1%), 3      0 (0.0%), 0      1 (0.6%), 1      0 (0.0%), 0
increased



                                                                                                                 25

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 25

Source: [DOC-004 p.25](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=25). Relationship group SP6-N025; applicable statistical group as coverage table.

```text
                                                                                                                 27

eFigure. Serum Neurofilament Sensitivity Analysis


Sensitivity analysis of NfL tested in serum samples longitudinally at Baseline, Week 4 (plasma only), Week 8 (serum only), Week 16,

and Week 24. NfL values <4pg/mL or <2% of the maximum for a given individual were excluded. This removed one baseline

measure for one participant. Values were converted to natural log (Ln) scale prior to analysis and difference of least square means is

shown at each timepoint. After back-transformation to compare values in the placebo and combined dosage CNM-Au8 treatment

groups in this sensitivity analysis, the NfL levels were increased in the regimen placebo group (+11.6) and in the CNM-Au8 treatment

group (+0.8%). The difference in change of the geometric mean comparing placebo to CNM-Au8 treatment groups was +9.7% (95%

CI: -0.1% to +18.5%, p=0.051).





                                                                                                                 27

              © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 PDF page 26

Source: [DOC-004 p.26](../../../../joi240158supp3_prod_1742927563.7911.pdf#page=26). Relationship group SP6-N026; applicable statistical group as coverage table.

```text
                                                                                                  28





                                                                                                  28

© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-005 PDF page 1

Source: [DOC-005 p.1](../../../../joi240158supp4_prod_1742927563.8061.pdf#page=1). SP6-N027: administrative roster, no applicable quantitative result/design; every unit opened.


### DOC-005 PDF page 2

Source: [DOC-005 p.2](../../../../joi240158supp4_prod_1742927563.8061.pdf#page=2). SP6-N028: administrative roster, no applicable quantitative result/design; every unit opened.


### DOC-005 PDF page 3

Source: [DOC-005 p.3](../../../../joi240158supp4_prod_1742927563.8061.pdf#page=3). SP6-N029: administrative roster, no applicable quantitative result/design; every unit opened.


### DOC-005 PDF page 4

Source: [DOC-005 p.4](../../../../joi240158supp4_prod_1742927563.8061.pdf#page=4). SP6-N030: administrative roster, no applicable quantitative result/design; every unit opened.


### DOC-005 PDF page 5

Source: [DOC-005 p.5](../../../../joi240158supp4_prod_1742927563.8061.pdf#page=5). SP6-N031: administrative roster, no applicable quantitative result/design; every unit opened.


### DOC-005 PDF page 6

Source: [DOC-005 p.6](../../../../joi240158supp4_prod_1742927563.8061.pdf#page=6). SP6-N032: administrative roster, no applicable quantitative result/design; every unit opened.


### DOC-006 PDF page 1

Source: [DOC-006 p.1](../../../../joi240158supp5_prod_1742927563.8111.pdf#page=1). SP6-N033 / SP6-S019; no numerical result cells. Complete software/data availability transcript:

```text
Data Sharing Statement
Berry. CNM-Au8 in Amyotrophic Lateral Sclerosis. JAMA. Published February 17, 2025.
doi:10.1001/jama.2024.27643
Data
Additional Information: Clinicaltrials.gov Clinical Trial Identifier NCT04297683,
NCT04414345
Data available: No
Additional Information
Explanation for why data not available: All data and report requests should be submitted to
the HEALEY ALS Platform Trial Data and Report Sharing Review Committee at
HealeyAMGCenterforALS@mgh.harvard.edu There will be a period of time where the Healey
Placebo Data will not be shared outside of the Sponsor, Regimen Partners, Writing Group
Leadership, and regulators as outlined in the HEALEY ALS Platform Trial Data and Report
Sharing Policy (add link) to protect the scientific integrity of the active regimens in the HEALEY
ALS Platform Trial. Statistical analyses and design simulations were programmed in SAS v9.4
or later, R v4.0 or later, or JAGS v4.3 or later; code is not publicly available at the present time
as the trial is still ongoing.


```

## Final reuse-fitness accounting

DOC-004:26total,26usableunique reusable,0fresh-required,26mapped. DOC-005:6total,6usableunique reusable,0fresh-required,6mapped. DOC-006:1total,1usableunique reusable,0fresh-required,1mapped. Fresh-required unit list: empty. Additional26page direct layout is corroborative extraction, not evidence that reusable units are absent. No legacy locator path requires fitness correction. Exact native-page filenames01–26 and normalized markers1–25 match source page locations. Printed folio numbers diverge from PDF numbering and are not locators. Canonical images14–25 match source pages and were all visually inspected. No omission arises from absent graphical coordinates: forest numeric cells are printed; serum sensitivity page25 has caption only.
