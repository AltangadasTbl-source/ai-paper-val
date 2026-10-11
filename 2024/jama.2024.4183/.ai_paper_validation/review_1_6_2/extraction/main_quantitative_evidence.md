# Main quantitative evidence map — Workflow 1.6.2

Status: COMPLETE. Scope: DOC-001, REPORT, all physical PDF pages 1–10 (printed pages 1722–1731). Source: jama_cinciripini_2024_oi_240036_1716416465.98349.pdf. This is a fresh relationship reconstruction, with no candidate selection, diagnosis, classification, or adjudication. No earlier scientific output was used.

Every N record is a numeric relationship and every S record is an inferential or statistical-method relationship. IDs are main-document local: DOC-001:N001–DOC-001:N055 and DOC-001:S001–DOC-001:S028; compact table labels omit the DOC-001 prefix. There are 83 relationship records. Multi-value rows preserve all displayed components of one relationship; matching occurrences are cross-referenced rather than silently combined. Percentages in Bayesian results are posterior estimates, not assumed to be crude proportions. All intervals in outcome results are 95% credible intervals (CrIs). Risk differences use percentage points; the paper calls them absolute RDs, including signed values. No frequentist P value, test statistic, standard error, hazard ratio, odds ratio, person-time, or incidence rate is displayed in this main paper. The logistic model is described on p.4, without displayed regression coefficients.

## Source and derivative provenance

Source SHA-256 from the current inventory: f51fd5b8f20a10df81121eb8aa19f1c4defb98d04ad476ce1e60dd95c68a18d1. Reused text locators: .ai_paper_validation/review_1_5_3/preprocessing/main/page-001.txt through page-010.txt and doc001_layout.txt. The curator independently matched each to current direct text after whitespace removal; old identity metadata is not adopted. Engine for these reusable layout/native assets: legacy Poppler pdftotext, version unrecorded. Current source graphic confirmation used Poppler pdftoppm 26.01.0, CPU, no OCR or fallback environment.

Command: `pdftoppm -f 3 -l 7 -r 110 -png jama_cinciripini_2024_oi_240036_1716416465.98349.pdf .ai_paper_validation/review_1_6_2/preprocessing/main_mapper/page`.

Outputs: .ai_paper_validation/review_1_6_2/preprocessing/main_mapper/page-03.png, page-04.png, page-05.png, page-06.png, page-07.png. Pages 3,5,6,7 were viewed directly to confirm Figure 1, Table, Figure 2, and Figure 3 respectively. Page 4 was an incidental range render; its usable text was inspected. Source graphics and their annotations were not modified. Figure 3 continuous density curves carry no additional labelled numeric quantiles beyond the printed counts, estimates and intervals below; their horizontal scale is 0–100%, ticks 0,20,40,60,80,100, and density heights are intentionally scaled without numeric ordinates.

## Complete page coverage

| Physical page | Printed page | Content and exact unit coverage | Record coverage | Status |
|---|---:|---|---|---|
| 1 | 1722 | Complete abstract: design, interventions, primary and secondary outcomes, populations, all estimates/CrIs/RDs/probabilities and narrative directions | N001–N010; S001–S012 | COMPLETE |
| 2 | 1723 | Introduction, Key Points, design, inclusion/exclusion, titration, phase definitions and hypothesis | N051; S013–S016; matching S006–S012 | COMPLETE |
| 3 | 1724 | Figure 1 entire SMART tree, doses, placeholders and caption | S014–S016 | COMPLETE; direct visual inspection |
| 4 | 1725 | Methods continuation: dosing, visits, follow-ups, endpoint, randomization/blinding, sample-size decision, priors, model/IPW, full flow narrative | N001–N010,N052; S001,S002,S013–S021 | COMPLETE |
| 5 | 1726 | Entire Table including every row and footnote; phase-1 and phase-2 results and start of abstainer results | N022–N047; S002–S010 | COMPLETE; direct visual inspection |
| 6 | 1727 | Figure 2 entire eligibility/decline/ineligibility/flow tree, all branches, losses, analysis totals and footnotes | N011–N021,N048–N050 | COMPLETE; direct visual inspection |
| 7 | 1728 | Figure 3 entire 8-row plot/count table and caption; remaining abstainer contrast; adverse events, adherence, secondary results | S003–S011,S022–S026; N053–N055 | COMPLETE; direct visual inspection |
| 8 | 1729 | Remaining secondary results, post hoc pathway definition, discussion, limitations and conclusions including numerical repeats | S002,S004–S012,S027,S028 | COMPLETE |
| 9 | 1730 | Article information, author roles, disclosures, funding, references 1–24; no study-result numeric relationship | No applicable additional relationship; bibliography/funding identifiers excluded from scientific mapping | COMPLETE |
| 10 | 1731 | References 25–40; no study-result numeric relationship | No applicable additional relationship; bibliographic dates/pages/identifiers excluded | COMPLETE |

Direct source links below use physical pages. Units 1–10 are all mapped; reusable units 10, fresh-required units 0, scientific coverage gaps 0. No uncovered unit was omitted.

## Numeric relationships: abstract and participant population

Location for N001–N010: [p.1 abstract](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1), with matching [p.4 Results](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4) and Figure 2 p.6 where identified.

| ID | Quantity and population | Printed value(s) and denominator/location context | Matching occurrence |
|---|---|---|---|
| N001 | Randomized/analysis population | Abstract design/results: 490 randomized; p.4 Results: 491 randomized, 1 CNRT person eliminated after randomization, leaving 490 due to protocol violation/data unusable | Figure 2 central node 491; arm headers 245 CNRT and 245 varenicline; Table 245 per arm |
| N002 | Sex, total sample | 210 female/women (43%), total 490 | Abstract p.1; Results p.4; Table female 105 (42.9) each arm |
| N003 | Race, total sample | 287 non-Hispanic White (58%), total 490 | Abstract p.1; Results p.4; Table 143/144 |
| N004 | Age, total sample | Mean 48.1 years | Abstract p.1; Results p.4; Table arm means 48.9 and 47.37 |
| N005 | Smoking and employment narrative | Average 20 cigarettes/day p.1 and p.4; p.4 >79% employed | Table cigarettes/day medians 20/20; employment 181/179 with percentages recorded separately |
| N006 | CNRT first-phase disposition | 54 abstinent; 191 nonabstinent; 151 rerandomized; 40 did not return and assigned continuation | Abstract p.1, Results p.4, Figure 2 p.6 |
| N007 | Varenicline first-phase disposition | 88 abstinent; 157 nonabstinent; 122 rerandomized; 35 did not return and assigned continuation | Abstract p.1, Results p.4, Figure 2 p.6 |
| N008 | CNRT phase-2 group percentages in abstract | Of 191 phase-1 nonabstainers: continuation 90 (47%); dose increase 50 (33%); switch varenicline 51 (34%). 151 rerandomized also printed immediately before these | Figure 2 shows 50 randomized continuation plus 40 assigned; dose increase50; switch51 |
| N009 | Varenicline phase-2 group percentages in abstract | Of 157 phase-1 nonabstainers: dose increase39 (32%); switch CNRT41 (34%); continuation77 (49%). 122 rerandomized also printed immediately before these | Figure 2 shows42 randomized continuation plus35 assigned; dose increase39; switch41 |
| N010 | Analysis and missing outcome assignment | p.4: all participants analyzed at week12; lost to follow-up analyzed nonabstinent, intent to treat; 40/35 assigned continue. Body printed phrase is “who did attend rerandomization” for these40/35; abstract says “did not return” | Figure 2 footnote c: participants imputed into continuation in phase2; p.8 limitation: did not return |

## Numeric relationships: entire Figure 2 flow diagram

Source: [p.6 Figure 2](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6). N011–N021 preserve every screening category. Categories are counts, not percentages.

| ID | Node/relationship | Printed counts |
|---|---|---|
| N011 | Eligibility, exclusion and allocation overview | 2232 assessed;1740 excluded;1052 declined;688 ineligible;491 randomized |
| N012 | Declined, not interested |459 of1052 |
| N013 | Declined, time/distance/transportation |377 of1052 |
| N014 | Declined, study drug/procedure |198 of1052 |
| N015 | Declined, other |18 of1052 |
| N016 | Ineligible, medical/psychiatric/behavioral conditions |134 unstable or exclusionary medical;103 unstable or exclusionary psychiatric;88 poor reporter/behavioral instability, each of688 |
| N017 | Ineligible, smoking/treatment/substance use |84 smoking <5 cigarettes/day;61 concurrent cessation treatment;47 illicit drug use, each of688 |
| N018 | Ineligible, drug-event/residence |32 reported adverse event to study drug;31 no stable residence or phone, each of688 |
| N019 | Ineligible, medications/other |21 exclusionary psychiatric medications;20 exclusionary nonpsychiatric medications;67 other, each of688 |
| N020 | CNRT initial treatment/analysis identity |245 randomized to CNRT;245 received treatment as randomized;1 did not receive treatment as randomized marked b |
| N021 | Varenicline initial allocation |245 randomized to receive2-mg varenicline |

Figure2 footnotes: (a) phase1 minimization balanced gender and race; (b) participant assigned to a different phase2 condition and excluded from all analyses; (c) intent-to-treat approach imputed participants into continuation; (d) abstinence7-day point prevalence biochemically confirmed; continuous abstinence30 days after treatment and6 months after target quit date. The footnote's supplied wording is preserved by location, without adopting any judgment.

| ID | Phase1 group/disposition | Phase2 condition | Rerandomized | Assigned continuation outside rerandomization | Included primary analyses | Lost follow-up |
|---|---|---|---:|---:|---:|---:|
| N048 | CNRT, abstinent |Continue CNRT|Not rerandomized|Not applicable|54|0|
| N048 | CNRT, nonabstinent |Switch varenicline|51|0|51|1|
| N048 | CNRT, nonabstinent |Increase CNRT|50|0|50|2|
| N048 | CNRT, nonabstinent |Continue CNRT|50|40|90|37|
| N049 | Varenicline, abstinent |Continue varenicline|Not rerandomized|Not applicable|88|4|
| N049 | Varenicline, nonabstinent |Switch CNRT|41|0|41|6|
| N049 | Varenicline, nonabstinent |Increase varenicline|39|0|39|5|
| N049 | Varenicline, nonabstinent |Continue varenicline|42|35|77|32|
| N050 | Cross-branch totals | CNRT191 nonabstinent/151 rerandomized/40 assigned; varenicline157 nonabstinent/122 rerandomized/35 assigned;142 phase1 abstainers |All tree counts above|All tree counts above|All8 terminal primary-analysis groups above|All8 terminal losses above|

N050 is a grouping relationship for tree-total reconstruction, not an additional printed total. The derived count142 is explicitly54+88; no unprinted person is inferred.

## Numeric relationships: entire baseline Table

Source: [p.5 Table, “Baseline Measures and Demographics”](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5). Every column denominator is n=245. CNRT and varenicline columns follow that order. Counts and percentages are transcribed exactly as printed, without substitution.

| ID | Row and scale | CNRT (n=245) | Varenicline (n=245) |
|---|---|---|---|
| N022 | Age, mean(SD), years |48.9(11.4)|47.37(11.2)|
| N023 | Sex: female, n(%) |105(42.9)|105(42.9)|
| N024 | Sex: male, n(%) |145(57.1)|145(57.1)|
| N025 | African American, non-Hispanic,n(%) |64(26.1)|65(26.5)|
| N026 | Asian, non-Hispanic,n(%) |9(3.7)|3(1.2)|
| N027 | Hispanic, any race,n(%) |19(7.8)|22(9)|
| N028 | >1 race,n(%) |5(2.0)|6(2.4)|
| N029 | White, non-Hispanic,n(%) |143(58.3)|144(58.8)|
| N030 | Other race/ethnicity,n(%) |5(2.0)|5(2.0)|
| N031 | Employment yes,n(%) |181(73.9)|179(73.1)|
| N032 | Employment no,n(%) |64(26.1)|66(26.9)|
| N033 | Education, median(IQR),years |13(12–14)|13(12–14)|
| N034 | Household income <$50000,n(%) |115(46.9)|107(43.7)|
| N035 | Household income $50000–79999,n(%) |51(20.8)|68(27.8)|
| N036 | Household income ≥$80000,n(%) |73(29.8)|63(25.7)|
| N037 | Household income not reported,n(%) |6(2.4)|7(2.9)|
| N038 | CO,median(IQR),ppm |19(13–26)|21(15–28)|
| N039 | Cigarettes/day,median(IQR) |20(12–20)|20(11.8–20)|
| N040 | FTCD total score,median(IQR) |5(3–6)|5(3.8–6)|
| N041 | Years of smoking,mean(SD) |28.6(12.5)|28.0(11.8)|
| N042 | Age of smoking initiation,median(IQR),years |17(14–20)|17(14–19)|
| N043 | Sex category total relationship |Female105 + male145, displayed percentages42.9+57.1, header245 |Same printed values and header245 |
| N044 | Race category total relationship |64+9+19+5+143+5; percentages26.1+3.7+7.8+2.0+58.3+2.0 |65+3+22+6+144+5; percentages26.5+1.2+9+2.4+58.8+2.0 |
| N045 | Employment category total relationship |181+64; percentages73.9+26.1 |179+66; percentages73.1+26.9 |
| N046 | Income category total relationship |115+51+73+6; percentages46.9+20.8+29.8+2.4 |107+68+63+7; percentages43.7+27.8+25.7+2.9 |
| N047 | Table definitions/footnotes |a: phase2 demographics eTable3; b:CNRT21-mg patch plus2-mg lozenges; c:self-reported NIH race/ethnicity categories; d:eligibility CO≥6ppm; e:FTCD6-item instrument,range0–10,higher scores greater dependence;score≥5 moderate to severe |Same definitions |

## Other numeric and exposure relationships

| ID | Source location | Complete relationship |
|---|---|---|
| N051 |p.2 Participants and Introduction|Eligibility age18–75 years,≥5 cigarettes/day,expired CO≥6ppm; historical background nearly70% want to quit,55% attempted ≥24h,7.5% succeed,4.7% recommended counseling/pharmacotherapy,approximately6 attempts; these are cited external-background quantities only, not current trial results. Prior3-mg dose studies are discussed without current-trial estimates. Recruitment June2015–October2019, Houston Texas; p.1 repeats dates |
| N052 |p.4 Behavioral Counseling/Follow-up|Brief counseling15 minutes: phase1 two in-clinic and three telephone visits;phase2 two in-clinic and one telephone visit. Follow-ups30 days after end of treatment and6 months after initial quit day. Abstract says weekly brief counseling |
| N053 |p.7 Adverse Events|Estimated frequencies and95%CrIs referenced to eTables5/6, no individual frequencies displayed. No medication-attributable group differences exceeded2% with nonoverlapping CrIs except nausea, higher phase1 varenicline than CNRT. Three serious adverse events unrelated to treatment |
| N054 |p.7 Visit and Medication Adherence|Mean prescribed dose taken averaged≥82% for active varenicline and≥77% for active CNRT patch; no individual group denominators or dispersion displayed. Visit attendance higher phase1 than phase2 and higher phase2 abstainers than nonabstainers. eTables7/8 pointers |
| N055 |p.7 Visit and Medication Adherence|Active CNRT lozenges ranged across phases from median40(IQR0–118) to76(IQR9.75–140) lozenges. Specific phase/condition assignment of extrema not displayed. No mean or percentage inferred |

## Inferential relationships: endpoint, phase1 and all Figure3 rows

| ID | Population/contrast/time | Numerator/denominator; estimate;95%CrI; probability/direction | Exact locations and matching occurrences |
|---|---|---|---|
| S001 |Prespecified primary outcome|Self-reported no smoking in previous7 days plus expired CO<6ppm at end of treatment week12; biochemically verified7-day point prevalence. All participants evaluated week12, missing outcome nonabstinent|p.1 Main Outcomes; p.2 Trial Design; p.4 Outcomes/Results; p.6 footnote d |
| S002 |Phase1 CNRT vs varenicline,week6|CNRT54/245,22%(17–27);varenicline88/245,36%(30–42);absolute RD−14%(−22 to−6),posterior probability≥99% of nonzero difference; narrative contrary to assumed similarity|p.4 last lines+p.5 first paragraph;p.8 Discussion repeats22/36 and phase1 absolute42/63 at week12 |
| S003 |CNRT phase1 abstainers continuing CNRT,week12|42/54;78%(69–85)|p.5 last paragraph+p.7 Figure3 row1 and continuation paragraph;p.8 Discussion42 and higher CNRT conditional probability |
| S004 |Varenicline phase1 abstainers continuing varenicline,week12|63/88;72%(65–78)|p.7 Figure3 row2 and continuation paragraph;p.8 Discussion63 |
| S005 |CNRT phase1 nonabstainers switching varenicline,week12|7/51;14%(10–18)|p.1 abstract51(34%);p.5 Smoking Cessation End of Phase2;p.7 Figure3 row3;p.8 Discussion14% |
| S006 |CNRT phase1 nonabstainers increasing CNRT,week12|7/50;14%(10–18)|p.1 abstract50(33%);p.5 phase2;p.7 Figure3 row4;p.8 Discussion14% |
| S007 |CNRT phase1 nonabstainers continuing CNRT,week12|7/90;8%(6–10)|p.1 abstract90(47%);p.5 phase2;p.7 Figure3 row5;p.8 Discussion8% |
| S008 |Varenicline phase1 nonabstainers switching CNRT,week12|0/41;0%(0–0)|p.1 abstract41(34%),printed0 without%;p.5 phase2;p.7 Figure3 row6;p.8 Discussion0% |
| S009 |Varenicline phase1 nonabstainers increasing varenicline,week12|8/39;20%(16–26)|p.1 abstract39(32%);p.5 phase2;p.7 Figure3 row7;p.8 Discussion20% |
| S010 |Varenicline phase1 nonabstainers continuing varenicline,week12|2/77;3%(1–4)|p.1 abstract77(49%);p.5 phase2;p.7 Figure3 row8;p.8 Discussion3% |
| S011 |Phase1 abstainers CNRT vs varenicline,week12|Absolute RD6%(−5 to16);posterior probability88% of difference;CNRT78% somewhat higher than varenicline72%; unexpected |p.5+p.7 abstainers paragraph;p.8 Discussion conditional CNRT higher,absolute numbers63 varenicline vs42 CNRT |
| S012 |Phase2 benefit conclusions across locations|CNRT increase or switch enhances abstinence vs continuation;varenicline increase greatest benefit. Key Points p.2: CNRT similar benefit but dosage increase may give longer-term benefit. Abstract p.1 and Conclusion p.8 favor varenicline increase and CNRT increase/switch;continuous abstinence favors dosage increase |p.1 conclusions,p.2 Key Points,p.8 Discussion/Conclusion; numerical contrasts separately preserved below |

Figure3 caption: each distribution is probability density,area under curve1;heights scaled for full depiction. Phase1 CNRT21-mg patch+2-mg lozenges;varenicline2mg/day. Phase2 increased CNRT two patches,lozenges stay2mg;varenicline increases3mg/day. Brown=phase1 abstainers;lighter blue=switch;orange=increase;darker blue=continue. Axes: probability density (vertical,no numeric ticks);probability of abstinence % (horizontal0,20,40,60,80,100). All eight row labels and row-order correspondence are preserved by S003–S010. Plot shapes are directly viewed; no unlabelled curve values are digitized or inferred.

## Inferential relationships: intervention, design and analysis methods

| ID | Exact location | Complete statement and quantitative components |
|---|---|---|
| S013 |p.2 hypotheses; p.4 statistical rationale|Relative to continuing same medication,nonabstainers hypothesized greatest benefit from increasing varenicline after initial varenicline or switching CNRT to varenicline;anticipated similar CNRT and varenicline abstinence at6 weeks. Bayesian model intended sequential clinician decisions,comparisons within initial treatment arms rather than identifying single best pathway |
| S014 |p.1 interventions;p.2 Pharmacotherapy;p.3 Figure1;p.4 first paragraph|Phase1 weeks1–6;phase2 weeks7–12. Start day after randomization,7 days before target quit. Varenicline0.5mg/day days1–3,0.5mg twice/day days4–7,1mg twice/day thereafter=2mg/day. CNRT21-mg patch+2-mg lozenges as needed,recommended≥6/day. All corresponding alternate-medication placebos |
| S015 |p.1,p.2,p.3 Figure1,p.4 dose continuation;p.8 limitations|Phase2 three nonabstainer choices:continue initial dose;switch to alternate phase1 regimen;increase. Varenicline extra1-mg evening tablet,total3mg/day;CNRT extra21-mg patch,total42mg/day in morning,lozenges continue2mg. Abstract says “3-mg or more” varenicline. Dose adjustments permitted by blinded physician for adverse events. Limitation discusses2mg vs4mg lozenges and two21-mg patches or3-mg varenicline |
| S016 |p.2 Trial Design,p.3 Figure1 and caption|Phase1 abstainers atweek6,7-day point prevalence with expiredCO<6ppm,continue same medication throughweek12. Figure1 CNRT starting regimen21mg/2mg/placebo varenicline and varenicline2mg/placeboCNRT;nonabstainers rerandomizedweek6 to switch,continue,increase;varenicline increase3mg/day and CNRT increase two21-mg patches;week12 abstinence assessment under both initial arms |
| S017 |p.4 Randomization/Blinding;Figure2 footnote a|Phase1 adaptive randomization,minimization,to stratify gender and race,computer program by data team. All staff blinded except coordinator preparing distribution kits. University of Pennsylvania service prepackaged coded blinded daily blister packs/bottles;active/placebo treatments described |
| S018 |p.4 Sample Size Determination and Statistical Analysis Plan|For each comparison,estimated probability of detecting benefit at0.80 or greater,K=1000 Monte Carlo simulations. All comparisons≥80% chance of detecting >80% probability of benefit with total500 participants;posterior probability prespecified sufficient to confirm hypotheses. eAppendix2/eFigure1/eTables1–2 pointers;no further main-paper simulation inputs |
| S019 |p.4 statistical analysis|Primary outcome analyses did not adjust multiplicity given a priori precise unbiased probability-estimate goal. Secondary outcomes p.7 descriptive and “collaborative” of primary outcomes,without multiplicity correction. No frequentist significance level given |
| S020 |p.4 statistical analysis|Logistic regression evaluated abstinence among treatments. Priors normal distribution N(μ=0,σ=1000) on log(odds) scale. Inverse probability weighting for probability of assignment to specific sequence by design permits unbiased effect-size estimates under rerandomization. No other covariates,posterior sampling algorithm,weights or coefficient table displayed |
| S021 |p.4 statistical analysis|All analyses R version4.0.3. eAppendix2/eFigure1 supplementary analysis pointers. Sample-size information and point-estimate details delegated there; this main map does not invent those details |

## Inferential relationships: all contrasts and secondary/post hoc occurrences

| ID | Exact location/population/time | Printed estimate,interval,probability and direction |
|---|---|---|
| S022 |p.1 abstract and p.5 phase2 CNRT nonabstainers,week12;same p.8 discussion|Both switch to varenicline and increase CNRT vs continue CNRT:RD6%. Abstract95%CrI6–11%;body95%CrI2–11%;both posterior probability>99%,either strategy benefit over continuing initial dosage. Discussion says6% increase comparing8% vs14%/14%. No distinction in abstract interval between two strategies |
| S023 |p.1 abstract and p.5 phase2 varenicline nonabstainers,week12;same p.8 discussion|Switch CNRT vs continue varenicline:RD−3%(−4 to−1),posterior probability>99%. Body states “continuing was worse than switching”. Abstract states “continuing varenicline at the initial dosage was worse than switching to a higher dosage” adjacent to RD−3%. Discussion prints “a 3% decrement of 3%” between3% continuation and0% switch. Printed directions retained separately from signed RD |
| S024 |p.1 abstract,p.5 phase2 varenicline nonabstainers,week12;p.8 discussion|Increase varenicline vs continue:RD18%(13–24),posterior probability>99% of benefit/superiority. Discussion says17% increase comparing3% with20%. Both numerical occurrences preserved,model-based RD not replaced by crude subtraction |
| S025 |p.7 Secondary Outcomes:continuous abstinence EOT+30days among phase1 nonabstainers|CNRT n191:increase8%,n50;switch varenicline10%,n51;continue3%,n90;posterior probability>99% for benefit of either alternative. Varenicline n157:only increasing dose8%,n39 benefited relative to continuation0%,n42 as printed. No switch rate,individual credible intervals or RDs displayed;see eFigure2/eTable9 |
| S026 |p.1 abstract,p.7 Secondary Outcomes,p.8 Discussion:continuous abstinence6months after target quit,phase1 nonabstainers|Only CNRT patch increase3% and varenicline increase2% benefit over respective continuation0%;posterior probabilities96% and99% respectively of nonzero difference. Abstract and Discussion agree only increased doses benefit at6months. No numerator,n group,CrI or RD printed in main passage; eFigure3/eTable9 pointers |
| S027 |p.8 first paragraph:phase1 abstainers continuous abstinence|At EOT+30days,CNRT higher than varenicline,posterior probability>97%;at6months no differences. eFigures2/3/eTable11 pointers. p.8 Discussion says early quitters may benefit equally long-term. No rates/counts/CrIs/RDs supplied in main text |
| S028 |p.8 Post Hoc Analyses and p.7 eTable10 pointer|Primary outcome only:average week12 probability for each treatment pathway combines phase1 abstainers continuing treatment and nonabstainers rerandomized among3 alternatives. Highest varenicline pathway rate=abstainers+increased-dose nonabstainers;CNRT similar rates for abstainers+increased dose or switch. eAppendix5/eTable12 pointers;no main-paper numerical pathway estimate or denominator displayed. p.7 eTable10 points to absoluteRDs/probabilities increase vs switch for both initial treatments at each time;no main printed estimates for those contrasts |

## Matching-location index for checker handoff

| Result/relationship group | All main-paper occurrences to match |
|---|---|
| Initial phase1 populations and randomization |p.1 abstract;p.4 Results;p.5 Table headers/phase1 results;p.6 Figure2;p.8 Discussion |
| Week6 abstainers/nonabstainers |p.1 abstract;p.4 Results;p.5 end-phase2 descriptions;p.6 Figure2;p.7 secondary-results population descriptors;p.8 Discussion |
| Every week12 posterior probability/count/CrI |p.1 abstract for six nonabstainer groups;p.5 body;p.7 Figure3 all8 rows and abstainer continuation;p.8 Discussion rates/absolute42,63 |
| CNRT alternative vs continuation RDs |p.1 abstract;p.5 phase2 narrative;p.8 Discussion |
| Varenicline alternatives vs continuation RDs/directions |p.1 abstract;p.5 phase2 narrative;p.8 Discussion |
| Longer-term continuous abstinence conclusions |p.1 abstract;p.2 Key Points;p.7 secondary-results paragraphs;p.8 secondary paragraph/Discussion/Conclusions |
| Intervention dosage/duration |p.1 abstract;p.2 Methods;p.3 Figure1;p.4 methods continuation;p.7 Figure3 caption;p.8 limitations |
| Analysis model,decision rule,population,missingness |p.2 Design;p.4 Methods/Results;p.6 Figure2 footnotes;p.7 secondary multiplicity statement;p.8 limitations/posthoc |

## Limitations and completion

All assigned study-result evidence is mapped, including nonsignificant, zero-event, secondary, safety, adherence, post hoc, baseline, and narrative-only results. Source graphs were inspected directly; graph density heights are deliberately scaled and are not independent numeric data. No scientific coverage gap remains. Main-paper unreported supplementary detail is identified explicitly by pointer and delegated source ownership; it is not treated as a missing source unit. No raw participant data, unlabelled density quantiles, or unstated model details are inferred. Historical reference/background quantities are distinguished from current results; references and grant/publication numbers are not result relationships. No candidate/report conclusions were read or produced.
