# Complete support quantitative evidence — Workflow 1.6.2

Status: COMPLETE. All192 support PDF pages mapped: DOC-002 REPORT pp1–25 and DOC-003 PLAN pp1–167. This canonical artifact is a lossless source/page-order merge of seven independently owned evidence parts. Relative source links are relocated one level because the canonical artifact is in `extraction/`, rather than `extraction/parts/`. Every clinical-result row, inferential relationship, plan-design definition, operational unit and explicit no-applicable record in the parts remains present. Local evidence keys are source-specific and are not candidate IDs. Global N/S relationship assignment occurs after mapping.

The mapped unique-page totals are25+167=192. Reusable-backed support units190; fresh-required units2, DOC-003 pp46 and48, mapped directly by assigned shard; no scientific coverage gaps. Reusable text/OCR supplies locators and transcriptions, and source/page images are the authority for image-only quantitative content. New PDF rendering runs on CPU; user-approved GPU OCR is not required for these mapped units. Derivative limitations and exact tool engines are recorded in each part.

## Disjoint source/page scope index

| Source/role | PDF pages | Page count | Original part artifact |
|---|---|---:|---|
| DOC-002 REPORT |1–25|25|parts/support_doc002_pp001-025.md|
| DOC-003 PLAN |1–32|32|parts/support_doc003_pp001-032.md|
| DOC-003 PLAN |33–64|32|parts/support_doc003_pp033-064.md|
| DOC-003 PLAN |65–96|32|parts/support_doc003_pp065-096.md|
| DOC-003 PLAN |97–128|32|parts/support_doc003_pp097-128.md|
| DOC-003 PLAN |129–160|32|parts/support_doc003_pp129-160.md|
| DOC-003 PLAN |161–167|7|parts/support_doc003_pp161-167.md|

Shared matching definitions: DOC-002 S6/S7/S8/S9 full primary composite and S10 composite without revascularization should be matched to main-paper primary/post hoc analyses and the original/final protocol/SAP definitions in DOC-003. DOC-002 S4/S5 mRS score distributions and S11 disabling stroke link to DOC-003 ordinal-logistic mRS and safety definitions. DOC-002 S11 row-specific tests link to DOC-003 final-SAP Fisher safety plan on p162. Version identities remain explicit: original protocol and SAP, final protocol and SAP, and disclosed amendment/revision tables; older and newer assumptions are never merged into one assumed plan.

Each complete part follows below without shortening.

---


<!-- BEGIN support_doc002_pp001-025.md -->

# DOC-002 complete support evidence map, PDF pages 1–25

Source: `joi240088supp1_prod_1746815064.21247.pdf`; role REPORT. All 25 pages mapped. This new mapping uses the retained per-page native/layout text and visually inspected page images, without legacy scientific conclusions. Figure images on pp6–13 and Table S2 p15 were read visually. No OCR was required. Original source is authoritative; retained transcription is an aid. Native table rows and all footnotes are reproduced in the pagewise appendix below; no row selection is made. Local evidence keys are source-specific; the coordinator assigns global N/S relationships.

Engine record: retained native/layout text from legacy pdftotext extraction; exact version unavailable. Retained PNG rendering engine/version unavailable. Fresh source text confirmation pp14–25 used the supplied workflow helper with pinned PyMuPDF 1.26.4, sorted reading order. Its geometry is less readable than the retained layout, so the retained layout plus visual p15 authority supplies the tabular alignment. Compute for PDF text/rendering is CPU; no new render or OCR derivative was produced.

## Per-page coverage and matching keys

| PDF page | Local key | Complete mapped scope | Main-paper matching key |
|---|---|---|---|
| 1 | D002-C01 | Identity, online publication September 5 2024; corrected November 27 2024; no outcome relationship | Source version |
| 2 | D002-C02 | Complete contents; references Figures S1–S6 and tables S1–S12; page pointers retained below; no independent result | Support table/figure keys |
| 3 | D002-C03 | Site/investigator list; administrative, no applicable result relationship | Participating centers |
| 4 | D002-C04 | Continued site/investigator list; administrative, no applicable result relationship | Participating centers |
| 5 | D002-C05 | Committees, sponsor, CRO, statistical-analysis unit, imaging lab, CEC, DSMB, AE committee, steering committee; no applicable quantitative result | Blinded adjudication/oversight |
| 6 | D002-E06 | Design/allocation diagram, eligibility, total planned 512, 31 centers, allocation 1:1, visits/windows | Methods population/design/follow-up |
| 7 | D002-E07 | Distribution of 31 centers in 14 provinces; administrative map, no numerical clinical result | Centers |
| 8 | D002-E08 | Training photos/map with value legend 0,2,4,6; no definition tying this scale to a clinical result; no applicable result relationship | Training |
| 9 | D002-E09 | Complete operational timeline, enrollment start/end, 1-year endpoint completion, independent interpretation | Recruitment/follow-up |
| 10 | D002-E10 | S1 CEC flow, reported cases and endpoint/additional-material/nonendpoint counts at four meetings | Adjudication/endpoint events |
| 11 | D002-E11 | S2 monthly and cumulative enrollment, dates Nov2018–Apr2022, final 512 | Enrollment population |
| 12 | D002-E12 | S3 all 31 center enrollment bars and exact printed counts | Enrollment and center analysis |
| 13 | D002-E13a/b | S4/S5 complete mRS distributions at 90 days/1 year, each score count/percent and group header | Secondary mRS, disabling stroke |
| 14 | D002-E14 | Every S1 baseline count/percentage, median/IQR, unit, nested denominator and footnote | Baseline Table 1 |
| 15 | D002-E15 | Every S2 risk-factor value and evaluated denominator at baseline, 3 months, 1 year | Risk-factor management |
| 16 | D002-E16 | Every S3 medication count/percentage in 6 group/time columns, NA at year1 dual agent | Antiplatelet/statin management |
| 17 | D002-E17 | Every S4 procedural count/percentage, duration, pressure, imaging denominator, restenosis definition | BA treatment/procedure/restenosis |
| 18 | D002-E18 | Every S5 revascularization indication/count, group totals, eligibility definition | Primary composite/revascularization |
| 19 | D002-E19 | S6 post hoc center-adjusted primary count/percentage, HR, CI, P and 2-category center adjustment | Primary outcome/sensitivity |
| 20 | D002-E20 | S7 center subgroup sample/count/percentage, HR/CI, interaction P, population headers | Center interaction |
| 21 | D002-E21 | S8 PPS primary/component count/percentage, HR/CI, P, printed headers/footnotes | Per-protocol primary sensitivity |
| 22 | D002-E22 | S9 ATS primary/component count/percentage, HR/CI, P, printed headers/footnotes | As-treated primary sensitivity |
| 23 | D002-E23 | S10 post hoc composite without revascularization: all ITT/PPS/ATS N, counts, percentages, HR/CI/P | Composite without revascularization |
| 24 | D002-E24 | Every S11 safety count/percentage/P, each test footnote, hemorrhage/disabling-stroke definitions | Serious AEs/disabling stroke |
| 25 | D002-E25 | Every S12 target definition, evaluated denominator, count and percentage | Year1 vascular target attainment |

## Visually mapped diagram and figure content

### D002-E06, PDF page 6: study design and allocation

Age 35–80 years; symptomatic ICAS ≥70% by DSA; ischemic stroke 14–90 days or TIA <90 days; arteries ICA C4–C7, MCA M1, BA, dominant VA V4; pre-mRS 0–2. Diagram states 512 patients from 31 centers in China, randomized R 1:1. Experimental group intracranial balloon angioplasty plus AMM; control AMM only. Visits: 1d, 30±3d, 90±7d, 180±14d, 1y±30d, 3y±30d with 6-month intervals after 1y. Clinical follow-up and neurovascular imaging marked. ICAS, DSA, TIA, ICA, MCA, VA, mRS and AMM expanded in source caption. No outcome counts appear.

### D002-E09, PDF page 9: operational timeline

2017/11/24 first investigators meeting DSMB; 2018/6/19 leading-center ethical approval; 2018/10/17 leading-center kickoff; 2018/11/08 first patient enrolled; 2019/8/21 first clinical technique review; 2020/06/15 first DSMB review; 2020/10/15 regular quality-control meeting; 2021/02/02 Co lab meeting; 2021/05/30 first CEC review; 2021/11/20 second CEC; 2022/04/02 last patient enrolled; 2022/09/07 third CEC; 2023/04/10 fourth CEC; 2023/05/02 all patients completed 1-year primary endpoint follow-up; 2023/06 complete data cleaning, core-lab analysis, independent CEC interpretation. Dates are administrative contextual evidence.

### D002-E10, PDF page 10: Figure S1

Investigators/CRC → endpoint events occur → independent CEC collects clinical information and confirms all endpoint events at each review meeting. Four boxes, transcribed as printed (later boxes all say “2nd meeting”):

| Meeting/date | Reported cases | Endpoint events | Additional materials needed | Nonendpoint events |
|---|---:|---:|---:|---:|
| 1st, 2021/05/30 | 19 | 10 | 6 | 3 |
| 2nd, 2021/11/20 | 27 | 24 | 1 | 2 |
| 2nd, 2022/09/07 | 26 | 23 | 2 | 1 |
| 2nd, 2023/04/10 | 15 | 13 | 1 | 1 |

Source does not state these are unique participants; do not turn cumulative adjudication meetings into a participant count.

### D002-E11, PDF page 11: Figure S2

X axis every month Nov18–Apr22; y axis 0–600 with 100-unit ticks. Blue enrollment this month and orange cumulative enrollment. Orange printed cumulative labels in month order: Nov18 1, Dec18 2, Jan19 3, Feb19 5, Mar19 6, Apr19 7, May19 11, Jun19 15, Jul19 19, Aug19 27, Sep19 35, Oct19 45, Nov19 55, Dec19 67, Jan20 78, Feb20 83, Mar20 85, Apr20 88, May20 94, Jun20 104, Jul20 126, Aug20 133, Sep20 160, Oct20 189, Nov20 196, Dec20 207, Jan21 223, Feb21 231, Mar21 235, Apr21 245, May21 259, Jun21 269, Jul21 280, Aug21 307, Sep21 342, Oct21 369, Nov21 395, Dec21 427, Jan22 435, Feb22 466, Mar22 478, Apr22 512. Late overlapping text near the final plotted point includes 511 adjacent to 512; monthly series has no exact numeric labels, so no exact monthly counts are inferred from plotted heights. Early small labels and final overlaps remain image-based locators for direct recheck.

### D002-E12, PDF page 12: Figure S3, all enrollment bars

Image authority is used; empty legacy OCR is not treated as evidence of absent content. Axis 0–300 in steps 50. Counts in printed top-to-bottom order:

| Center | Enrolled |
|---|---:|
| Beijing Tian Tan Hospital | 258 |
| Affiliated Hospital of Qingdao University | 84 |
| Nanjing Drum Tower Hospital | 23 |
| First Affiliated Hospital of Anhui Medical University | 18 |
| Beijing Luhe Hospital | 16 |
| Beijing Chao-Yang Hospital | 15 |
| Henan Provincial People's Hospital | 13 |
| First Affiliated Hospital of Sun Yat-sen University | 10 |
| Qilu Hospital of Shandong University | 9 |
| Second Affiliated Hospital of Guangzhou Medical University | 9 |
| Affiliated Hospital of Guizhou Medical University | 8 |
| Hunan Provincial People's Hospital | 7 |
| First Hospital of Jilin University | 7 |
| First Affiliated Hospital of Anhui University of CM | 5 |
| Beijing Fengtai You Anmen Hospital | 4 |
| Shandong Provincial Hospital | 4 |
| Beijing ShunYi Hospital | 3 |
| General Hospital of Northern Theater of Chinese People's Liberation Army | 3 |
| Dongfang Hospital Beijing University of Chinese Medicine | 2 |
| Liaocheng People's Hospital | 2 |
| Guangdong Sanjiu Brain Hospital | 2 |
| Affiliated Hospital of Northwest University | 1 |
| Guangdong Provincial Hospital of Traditional Chinese Medicine | 1 |
| Second Affiliated Hospital of Nanjing Medical University | 1 |
| Chinese PLA General Hospital | 1 |
| First People's Hospital of Changzhou | 1 |
| First Affiliated Hospital of Xi'an Jiaotong University | 1 |
| Jiangxi Provincial People's Hospital | 1 |
| Wuhan NO.1 Hospital | 1 |
| West China Hospital Sichuan University | 1 |
| Shenzhen Hospital of Southern Medical University | 1 |

### D002-E13a/b, PDF page 13: mRS Figures S4/S5

Both legends scores 0,1,2,3,4,5,6; horizontal axis percentage of patients 0–100 in increments 10. BA and AMM names expanded in captions. All printed count/percentage pairs are retained literally; no arithmetic correction is applied. The narrow segments use leader lines. Table lists increasing-score order from left to right.

| Time/group, printed group header | mRS0 | mRS1 | mRS2 | mRS3 | mRS4 | mRS5 | mRS6 |
|---|---|---|---|---|---|---|---|
| 90d BA N=249 | 82.3 (N=205) | 14.5 (N=36) | 2.0 (N=50) | 0.8 (N=2) | 0.0 (N=0) | 0.0 (N=0) | 0.4 (N=1) |
| 90d AMM N=252 | 73.4 (N=185) | 19.1 (N=48) | 4.8 (N=12) | 0.8 (N=2) | 1.6 (N=4) | 0.4 (N=1) | 0.0 (N=0) |
| 1y BA N=249 | 78.3 (N=195) | 18.5 (N=46) | 1.6 (N=4) | 0.8 (N=2) | 0.4 (N=1) | 0.0 (N=0) | 0.4 (N=1) |
| 1y AMM N=252 | 67.9 (N=169) | 23.3 (N=58) | 5.2 (N=13) | 1.2 (N=3) | 1.2 (N=3) | 0.4 (N=1) | 0.8 (N=2) |

The BA 90d mRS2 leader explicitly reads N=50 in the retained image. The group headers and counts are kept separately from the plotted percentages; denominators are not reconstructed or silently substituted. No inferential estimate or P appears in these figures.

## Statistical relationship detail and table alignment keys

D002-E14: S1 BA249/AMM252. Ethnicity exhaustive categories Han/Korean/Manchus/Mongol/Yi; medical history; ASITN/SIR overall median-like printed 1(1,1) under n(%) label and categories0–2/3–4; lesion length/reference vessel/minimal lumen mm; ischemic stroke215/208 and nested infarct categories; preprocedure eTICI0/1/2a/2b50/2b67/2c/3; all medication counts. Appendix preserves every row and the non-zone BA131(61.9) printed pair without alteration. IQR definition and eTICI expanded.

D002-E15: S2 six columns BA baseline/3m/1y then AMM baseline/3m/1y. Evaluated counts precede each variable. One unlabeled evaluated row249/249/NA versus252/252/NA is printed between current smoking and next evaluated row; visually confirmed as a distinct row with no following variable before the next evaluated count. BMI kg/m²; activity h/week; systolic/diastolic mmHg; cholesterol/HDL/LDL mg/dl; glycosylated hemoglobin%. All values median(IQR), counts n(%), with NA retained. Appendix retains all six-column arrays.

D002-E16: S3 columns same order; aspirin; ticagrelor or clopidogrel; statin, each n(%), BA249/AMM252 printed headers. Year1 dual-agent cells NA.

D002-E17: S4 BA header249; footnote241 underwent BA, 7 crossover to AMM and1 direct balloon-expanding stenting. Procedural categories use printed denominator context241; restenosis24(15.7) and related TIA/stroke3/153(2.0); imaging153. Restenosis >70% or increased by30%; 1-year window. Duration seconds, pressure atm, median IQR and n(%). All complications may overlap; source does not define categories as exclusive.

D002-E18: S5 “primary population” title; acute revascularization BA1/AMM1/total2; elective hard-TIA BA2/AMM10/total12; elective ischemic stroke BA0/AMM10/total10; overall3/21/24. Hard TIA means recurrent transient ischemic attack >10min or new disabling neurologic symptoms. Window beyond30d through1y.

| Local statistical key | Display/analysis | BA and AMM printed data | Printed inferential evidence | Population/model/definition |
|---|---|---|---|---|
| D002-S19 | S6 primary center adjustment | 9(3.9),34(13.5); headers249,252 | HR0.32 (0.16–0.62), P.001 | Post hoc; adjusting groups and centers; centers Beijing Tiantan vs other |
| D002-S20a | S7 Beijing Tiantan | site total256; 4(2.9),19(16.1) | HR0.17 (0.06–0.51) | Headers BA233 AMM238; post hoc primary interaction |
| D002-S20b | S7 other centers | site total245; 7(6.3),15(11.2) | HR0.56 (0.23–1.36); shared interaction P.10 | Same primary outcome/interaction |
| D002-S21a | S8 PPS primary | 9(3.9),33(13.9) | HR0.27 (0.13–0.56), P<.001 | Printed headers249,252; title per-protocol |
| D002-S21b | S8 early stroke/death | 6(2.6),4(1.7) | HR1.55 (0.44–5.49), P not printed | Within30d after enrollment |
| D002-S21c | S8 late qualifying ischemic stroke | 1(0.4),18(7.6) | HR0.06 (0.01–0.41), P not printed | Beyond30d through1y |
| D002-S21d | S8 late revascularization | 3(1.3),20(8.4) | HR0.15 (0.04–0.50), P not printed | Beyond30d through1y |
| D002-S22a | S9 ATS primary | 11(4.5),34(13.4) | HR0.32 (0.16–0.64), P.001 | Printed headers249,252; title as-treated |
| D002-S22b | S9 early stroke/death | 8(3.3),4(1.6) | HR2.09 (0.63–6.92), P not printed | Within30d after enrollment |
| D002-S22c | S9 late qualifying ischemic stroke | 1(0.4),19(7.5) | HR0.05 (0.01–0.39), P not printed | Beyond30d through1y |
| D002-S22d | S9 late revascularization | 3(1.2),21(8.3) | HR0.14 (0.04–0.47), P not printed | Beyond30d through1y |
| D002-S23a | S10 ITT post hoc no revascularization | N249/252; 9(3.6),23(9.1) | HR0.39 (0.18–0.85), P.01 | Early stroke/death plus late qualifying ischemic stroke |
| D002-S23b | S10 PPS same endpoint | N233/238; 7(3.0),22(9.2) | HR0.32 (0.14–0.75), P.01 | Same composite without revascularization |
| D002-S23c | S10 ATS same endpoint | N247/254; 9(3.6),23(9.1) | HR0.40 (0.19–0.86), P.02 | Same composite without revascularization |

S6/S8/S9 full primary definition: any stroke or all-cause death within30d after enrollment or after BA of qualifying lesion, or any ischemic stroke or revascularization of qualifying artery beyond30d through1y after enrollment. S8/S9 revascularization footnote: acute qualifying-artery occlusion with neurologic deficit requiring IV/intraarterial thrombolysis, thrombectomy, balloon/stent angioplasty, or intracranial-extracranial bypass; elective symptom-driven revascularization includes BA/stent/bypass. No absent component P value is inferred.

D002-E24/S24: S11 all safety rows/tests in appendix, BA249/AMM252. Overall12(4.8)/14(5.6), P.84 chi-square; nervous7(2.8)/12(4.8), P.35 chi-square; symptomatic hemorrhage3(1.2)/1(.4), P.37 Fisher; asymptomatic3(1.2)/0, P.12 Fisher; any hemorrhage6(2.4)/1(.4), P.07 Fisher; disabling stroke6(2.4)/18(7.1), P.02 chi-square. Remaining nine system rows and P values preserved below. Symptomatic hemorrhage MRI/CT-confirmed subarachnoid/parenchymal/intraventricular causing new symptoms >24h or seizure; disabling stroke mRS>2 at1y. Each row is a separate inferential relationship under the shared S24 display family.

D002-E25: S12 target attainment denominators differ per row. LDL<1.8mmol/L N139/120 with66(47.5)/61(50.8); triglycerides<200mg/dL N141/122 with127(90.1)/104(85.3); HbA1c<7% N65/66 with46(70.8)/48(72.7); BP≤140/90 without DM N166/160 with119(71.7)/119(74.4); BP≤130/80 with DM N81/83 with17(21.0)/24(28.9). Group header249/252 remains contextual, not substituted for evaluated N.

## Complete pagewise native/layout transcription appendix

Each page below is explicitly source-linked. Image-only evidence is mapped above. No source or reused asset is modified. No diagnosis or candidate selection is made.

### DOC-002 PDF page 1

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=1)

```text
                                 Supplementary Online Content

Sun X, Deng Y, Zhang Y, et al; for the BASIS Investigators. Balloon angioplasty vs aggressive medical
management for symptomatic intracranial artery stenosis: the BASIS randomized clinical trial. JAMA.
Published online September 5, 2024. doi:10.1001/jama.2024.12829
Corrected online November 27, 2024.




This supplemental material has been provided by the authors to give readers additional information about
their work.




                                                    1

```

### DOC-002 PDF page 2

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=2)

```text
                                                  Supplementary Appendix


Contents
 List of participating sites and investigators in the BASIS trial                                             Page 2

 Study Committee Members of the BASIS trial                                                                   Page 4

 Study design and treatment allocation                                                                        Page 5

 Distribution of 31 participating centers in 14 provinces                                                     Page 6

 On-site and online training arrangement of the BASIS trial                                                   Page 7

 Research Progress of BASIS                                                                                   Page 8

 Supplementary Figures S1-S6                                                                                  Page 9-12
     Figure S1. Flow chart of clinical-event adjudication committee (CEC) assessing and confirming            Page 9
 endpoint events
     Figure S2. Enrollment progress of the BASIS trial by month                                               Page 10
     Figure S3. Number of patients enrolled by center                                                         Page 11
     Figure S4. Distribution of 90-day mRS                                                                    Page 12
     Figure S5. Distribution of 1-year mRS                                                                    Page 12

 Supplementary Tables S1-S8
     Table S1. Demographic and baseline clinical characteristics                                              Page 13-26
     Table S2. Measures of risk factors at baseline, 3-months and 1-year follow-up                            Page 13
     Table S3. The proportion of patients receiving antiplatelet and statin medicine at baseline, 3-months    Page 15
 and 1-year follow-up                                                                                         Page 16
     Table S4. Details of balloon angioplasty
     Table S5. The number of patients and reason for revascularisation beyond 30 days through 1 year in the   Page 17
 ITT population of the BASIS trial                                                                            Page 18
     Table S6 Post-hoc analysis of center-effect adjustment
     Table S7. Post-hoc analysis of treatment interaction on the primary outcome regarding different sites    Page 19
     Table S8. Study outcomes in the per-protocol population                                                  Page 20
     Table S9. Study outcomes in the as-treated population                                                    Page 21
     Table S10. Post-hoc analysis of the comparison of any stroke or all-cause death within 30 days after     Page 22
 enrollment or after BA of the qualifying lesion or any ischemic stroke from the qualifying artery beyond     Page 23
 30 days through 1 year after enrollment between BA and AMM groups
   Table S11. Number of patients with other serious adverse events (by system organ class) up to 1-year       Page 24
 visit
   Table S12. The proportion of patients meeting the proposed target of vascular risk factor management at    Page 25
 1-year follow-up




                                                                    2

```

### DOC-002 PDF page 3

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=3)

```text
      List of participating sites and investigators in the BASIS trial
    BASIS site                                                                                  Investigator

    Beijing Tiantan Hospital, Capital Medical University                                        Zhongrong Miao

    Beijing Tiantan Hospital, Capital Medical University                                        Yilong Wang

    The Affiliated Hospital of Qingdao University                                               Yong Zhang

    Nanjing Drum Tower Hospital, The Affiliated Hospital of Nanjing University Medical School   Yun Xu

    Zhengzhou University People's Hospital                                                      Tianxiao Li

    The Second Affiliated Hospital of Guangzhou Medical University                              Yunxiang Ji

    Beijing Luhe Hospital,Capital Medical University                                            Xiaokun Geng

    The First Hospital of Jilin University                                                      Shouchun Wang

    Qilu Hospital of Shandong University                                                        Wei Wu

    Hunan Provincial People's Hospital                                                          Xiaoping Gao

    The First Affiliated Hospital,Sun Yat-sen University                                        Shihui Xing

    The Affiliated Hospital of Guizhou Medical University                                       Hua Yang

    Shandong Provincial Hospital                                                                Yifeng Du

    General Hospital of The Northern Theater of The Chinese People's Liberation Army            Huisheng Chen

    Guangdong Sanjiu Brain Hospital                                                             Peiming Wang

    Shenzhen Hospital of Southern Medical University                                            Yajie liu

    West China Hospital Sichuan University                                                      Hongbo Zheng

    Wuhan First Hospital                                                                        Wenhua Liu

    The First Affiliated Hospital of Anhui Medical University                                   Weimin Yang

    Jiangxi Provincial People's Hospital                                                        Wenfeng Cao

    Liaocheng People's Hospital                                                                 Guisheng Jiang

    The First Affiliated Hospital of Xi'an Jiaotong University                                  Jianfeng Han

    The First People's Hospital of Changzhou                                                    Ya Peng

    Chinese PLA General Hospital                                                                Jun Wang

    Beijing Chao-Yang Hospital, Capital Medical University                                      Yang Wang

    Beijing Fengtai You Anmen Hospital                                                          Shiyong Zhang

    Dongfang Hospital Beijing University of Chinese Medicine                                    Gesheng Wang




                                                                 3

```

### DOC-002 PDF page 4

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=4)

```text
BASIS site                                                         Investigator

Beijing ShunYi Hospital                                            Liyu Wang

The Second Affiliated Hospital Of NanJing Medical University       Jin Wu

Guangdong Provincial Hospital of Traditional Chinese Medicine      Guifu Li

The Affiliated Hospital of Northwest University                    Mingze Chang




                                                               4

```

### DOC-002 PDF page 5

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=5)

```text
       Study Committee Members of the BASIS trial
Cooperation team                                  Unit or Hospital name                                Investigator Name

Sponsor                Beijing Tiantan Hospital, Capital Medical University                            NA

CRO                    Beijing Jingchengtong Medicine Technology Co., Ltd.                             NA

Statistical analysis   Department of Biostatistics, Peking University Clinical Research Institute      NA

Imaging core lab       China National Clinical Research Center for Neurological Diseases, Tiantan      Jing Jing
                       Neuroimaging Center of Excellence

                       China National Clinical Research Center for Neurological Diseases, Tiantan      Nan Qi
                       Neuroimaging Center of Excellence

CEC team               Tangdu Hospital of Air Force Medical University                                 Zhenwei Zhao

                       Beijing Tiantan Hospital, Capital Medical University                            Kehui Dong

                       The First Affiliated Hospital of Harbin Medical University                      Huaizhang Shi

DSMB                   People's Liberation Army Air Force General Hospital                             Jin Shi

                       Strategic Support Force Specialty Medical Center                                Yiling Cai

                       China National Clinical Research Center for Neurological Diseases               Yuesong Pan

AE Committee           Beijing Tiantan Hospital, Capital Medical University                            Xuan Sun

                       Beijing Tiantan Hospital, Capital Medical University                            Yiming Deng

                       Beijing Tiantan Hospital, Capital Medical University                            Ning Ma

Steering               Beijing Tiantan Hospital, Capital Medical University                            Zhongrong Miao
Committee
                       Beijing Tiantan Hospital, Capital Medical University                            Yilong Wang

                       Beijing Tiantan Hospital, Capital Medical University                            Yongjun Wang

                       Department of Neurology, University of california irvine, Irvine, California,   Wengui Yu
                       USA

                       Beijing Tiantan Hospital, Capital Medical University                            Xingquan Zhao

                       Neurovascular Imaging Research Core and Department of Neurology,                David S Liebeskind
                       University of California, USA

                       Department of Neurosurgery, University Hospitals Cleveland Medical Center/      Sepideh Amin-Hanjani
                       Case Western Reserve Univeristy School of Medicine, Ohio, USA




                                                                    5

```

### DOC-002 PDF page 6

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=6)

```text
   Study design and treatment allocation




ICAS denotes intracranial atherosclerosis stenosis. DSA denotes digital subtraction angiography. TIA
denotes transient ischemic attack. ICA denotes internal carotid artery. MCA denotes middle cerebral
artery. VA denotes vertebral artery. mRS denotes modified Rankin Scale. AMM denotes aggressive
medical management.




                                                 6

```

### DOC-002 PDF page 7

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=7)

```text
   Distribution of 31 participating centers in 14 provinces




                                                  7

```

### DOC-002 PDF page 8

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=8)

```text
   On-site and online training arrangement of the BASIS trial




                                                8

```

### DOC-002 PDF page 9

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=9)

```text
   Research Progress of BASIS




                                 9

```

### DOC-002 PDF page 10

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=10)

```text
Supplementary Results
   Figure S1. Flow chart of clinical-event adjudication committee (CEC) assessing and confirming
    endpoint events




                                              10

```

### DOC-002 PDF page 11

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=11)

```text
   Figure S2. Enrollment Progress of the BASIS trial by month




                                              11

```

### DOC-002 PDF page 12

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=12)

```text
   Figure S3. Number of patients enrolled by each participating center




                                                12

```

### DOC-002 PDF page 13

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=13)

```text
Figure S4. Distribution of the modified Rankin Scale at 90 days
BA denotes balloon angioplasty. AMM denotes aggressive medical management.




Figure S5. Distribution of modified Rankin Scale at 1 year
BA denotes balloon angioplasty. AMM denotes aggressive medical management




                                                 13

```

### DOC-002 PDF page 14

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=14)

```text
    Table S1. Demographic and baseline clinical characteristics of patients
      Characteristics                                      Balloon angioplasty group   Aggressive medical management
                                                                      (n=249)          group   (n=252)

      Ethnicity, n (%)

        Han                                                          245 (98.4)                   249 (98.8)

        Korean                                                          0 (0)                       1 (0.4)

        Manchus                                                        2 (0.8)                      1 (0.4)

        Mongol                                                         2 (0.8)                       0 (0)

        Yi                                                             0 (0.0)                      1 (0.4)

      Medical History, n (%)

        Coronary heart disease                                       29 (11.7)                     28 (11.1)

        ischemic stroke                                              50 (20.1)                     55 (21.8)

      ASITN/SIR, n (%)                                                 1(1,1)                       1 (1,1)

        0-2                                                          222 (89.2)                   219 (86.9)

        3-4                                                          27 (10.8)                     33 (13.1)

      Lesion length, mm, median (IQR)                               6.1 (5.0,8.0)                6.0 (4.7,7.8)

      Reference-vessel diameter, mm                                 2.3 (2.0,2.8)                2.4 (2.1,2.9)

      Minimal luminal diameter, mm                                  0.5 (0ꞏ3,0ꞏ6)                0ꞏ5 (0ꞏ4,0ꞏ7)

      ischemic stroke, n (%)                                         215 (86.4)                   208 (82.5)

        Border zone infarct                                          84 (39.1)                     85(40.9)

        Non-zone infarct                                             131(61.9)                    123(59.1)

      eTICI before the procedure, n (%)

        0                                                               0 (0)                        0 (0)

        1                                                              3 (1.2)                      3 (1.2)

        2a                                                            12 (4.8)                     17 (6.8)

        2b50                                                         80 (32.1)                     78 (31.0)

        2b67                                                         112 (45.0)                   121 (48.0)

        2c                                                           39 (15.7)                     31 (12.3)

        3                                                              3 (1.2)                      2 (0.8)

      Received medical therapy at qualifying event n (%)

        Statin                                                       123 (49.4)                   126 (50.0)

        ACE inhibitor or angiotensin II receptor                     29 (11.7)                     19 (7.5)

        Beta-Blocker                                                   4 (1.6)                      4 (1.6)

        Calcium antagonist                                           78 (31.3)                     43 (17.1)

        Diuretic                                                       1 (0.4)                      1 (0.4)

        Sulfonylureas                                                  5 (2.0)                      8 (3.2)

        Biguanides                                                    10 (4.0)                     17 (6.8)

        Glycoside inhibitor                                           16 (6.4)                     23 (9.1)

        Insulin                                                      47 (19.0)                     25 (10.0)

Data are n (%), or median (IQR). IQR denotes interquartile range. eTICI denotes expanded Thrombolysis in Cerebral
Infarction. BA denotes balloon angioplasty. AMM denotes aggressive medical management.

                                                               14

```

### DOC-002 PDF page 15

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=15)

```text
            Table S2. Measures of risk factors at baseline, 3-months and 1-year follow-up
Characteristics                                                      Balloon angioplasty group (n=249)                                 Aggressive medical management group (n=252)

                                                      Baseline                  3 months                     1 year              Baseline                3 months               1 year

No. Patients evaluated                                  249                        245                         248                  252                    245                    246

BMI, kg/m2, median (IQR)                          25.4 (23.7,27.5)           25.4 (23.7,27.5)            25.2 (23.7,27.3)     25.4 (23.5,27.7)       25.4 (23.6,27.7)       25.6 (23.5,27.7)

No. Patients evaluated                                  249                        248                         248                  252                    252                    246

Current smoking, n (%)                                60 (24.1)                  11 (4.4)                    22 (8.9)            66 (26.2)               15 (6.0)               16 (6.5)

No. Patients evaluated                                  249                        249                         NA                   252                    252                    NA

No. Patients evaluated                                  248                        243                         247                  249                    251                    246

Activity level per week, h, median (IQR)            3.5 (2.5,7.0)             4.0 (3.0,7.0)               4.0 (2.5,7.0)        7.0 (3.5,7.0)           5.0 (3.5,7.0)         5.0 (3.0,7.0)

No. Patients evaluated                                  249                        239                         247                  252                    233                    243

Blood pressure, mm Hg, median (IQR)

 Systolic                                        140.0 (130.0,154.0)       135.0 (130.0,138.0)        130.0 (125.0,139.0)   140.0 (130.0, 151.0)    135.0 (130.0,140.0)   130.0 (125.0,139.0)

 Diastolic                                        83.0 (77.0,91.0)           80.0 (75.0,85.0)            80.0 (70.0,82.0)    84.0 (77.0, 92.0)       80.0 (75.0,85.0)       80.0 (75.0,85.0)

No. Patients evaluated                                  233                        128                         140                  230                    143                    121

Cholesterol, mg/dl, median (IQR)                 136.1 (115.2,163.2)       137.3(121.0,155.3)         134.8(115.6,150.4)    139.2 (119.9,161.3)     141.9 (119.5,157.4)   134.2(115.6,158.9)

No. Patients evaluated                                  232                        119                         140                  226                    137                    120

High-density lipoprotein, mg/dl                    41.8(35.2,49.1)           44.5 (38.3,51.4)            45.2 (38.3,53.9)     39.8 (34.8,48.0)       43.7 (37.9,50.7)       42.0 (34.4,48.5)

No. Patients evaluated                                  233                        121                         139                  226                    141                    120

Low-density lipoprotein, mg/dl                    72.7 (57.6,93.6)           73.1 (59.2,89.7)            70.8 (55.7,86.6)     76.0 (61.5,94.7)       75.4 (61.1,89.3)       69.0 (56.3,88.8)

No. Patients evaluated                                  150                         88                         65                   132                    107                    66

Glycosylated hemoglobin, %                          6.1 (5.6,7.0)              6.0 (5.7,6.7)              6.2 (5.8,7.4)         6.5 (5.8,7.8)          6.1 (5.6,6.9)         6.1 (5.6,7.1)

    Data are n (%), or median (IQR). BMI denotes body-mass index. BA denotes balloon angioplasty. AMM denotes aggressive medical management. IQR denotes
    interquartile range.




                                                                                                 15

```

### DOC-002 PDF page 16

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=16)

```text
    Table S3. The proportion of patients receiving antiplatelet and statin medicine at baseline, 3-months and 1-year follow up
    Characteristics                                                      Balloon angioplasty group (n=249)        Aggressive medical management group (n=252)

                                                                    Baseline         3 months           1 year    Baseline        3 months           1 year

    Receiving aspirin, n (%)                                        249(100)         234(93.9)        197(79.1)   252(100)        236(93.7)        185(73.4)

    Receiving ticagrelor or clopidogrel, n (%)                      249(100)         238(95.6)           NA       252(100)        238(94.4)           NA

    Receiving statin, n (%)                                         249(100)         237(95.2)        199(79.9)   252(100)        237(94.0)        191(75.8)

Data are n (%). BA denotes balloon angioplasty. AMM denotes aggressive medical management.




                                                                               16

```

### DOC-002 PDF page 17

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=17)

```text
       Table S4. Details of balloon angioplasty
            Characteristics                                                        Balloon angioplasty groupa
                                                                                            (n=249)

            Balloon angioplasty duration, s                                             30.0 (20.0,60.0)

            Balloon angioplasty time, no. (%)

              1                                                                            182 (75.5)

              2                                                                            48 (19.9)

              3                                                                             11 (4.6)

            Balloon pressure, atm, no. (%)                                                6.0 (4.5,7.0)

            Residual stenosis degree after the procedure, no. (%)

              0-50%                                                                        214 (88.8)

              50%-70%                                                                       19 (7.9)

              70%-100%                                                                      8 (3.3)

            eTICI after the procedure, no. (%)

              0                                                                             0 (0.0)

              1                                                                             2 (0.8)

              2a                                                                            1 (0.4)

              2b50                                                                          9 (3.7)

              2b67                                                                          20 (8.3)

              2c                                                                           93 (38.6)

              3                                                                            116 (48.1)

            Rescue stenting, no. (%)                                                       39 (16.2)

            Intra-procedural complications, no. (%)                                        42 (17.4)

              Vasospasm                                                                     3 (1.2)

              Arterial dissection                                                          35 (14.5)

              Pseudoaneurysm                                                                0 (0.0)

              Arterial occlusion                                                            1 (0.4)

              Arterial perforation                                                           0 (0.0)

              Arterial rupture                                                              0 (0.0)

              hemorrhage                                                                    1 (0.4)

              Thrombosis                                                                    4 (1.7)
                                                                b.c
            Restenosis of the qualifying artery within 1 y , no. (%)                       24 (15.7)
                                                            c
              TIA or stroke clearly related to restenosis                                 3/153 (2.0)

Data are n (%), or median (IQR). IQR denotes interquartile range. eTICI denotes expanded Thrombolysis in the
Cerebral Infarction. BA denotes balloon angioplasty.
a
    241 of 249 patients underwent BA. 8 patients didn't undergo BA due to crossover to the AMM group (7 patients) and
direct balloon-expanding stenting (1 patient).
b
    Restenosis of the qualifying artery within 1 year was based on subsequent neurovascular                     imaging,
stenosis degree >70% or increased by 30%.
c
    153 patients had intact follow-up cerebrovascular imaging within 1 year to assess the restenosis of the qualifying
artery.


                                                                       17

```

### DOC-002 PDF page 18

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=18)

```text
                      Table S5 The number of patients and reason for revascularization beyond 30 days through 1 year in the
                       primary population of the BASIS trial


Reasons for revascularization                                        Balloon angioplasty group   Aggressive       medical   Number
                                                                                                 management group

Acute revascularization                                                          1                            1               2
(acute qualifying artery occlusion accompanied by neurological
deficit)

Elective revascularization                                                       2                        10                  12
(Hard TIA: culprit artery stenosis that causes recurrent transient
ischemic attack lasting longer than 10 minutes or new disabling
neurological symptoms)

Elective revascularization                                                       0                        10                  10
(ischemic stroke caused by the culprit artery stenosis)

Total                                                                            3                        21                  24


                TIA denotes transient ischemic attack.




                                                                                       18

```

### DOC-002 PDF page 19

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=19)

```text
         Table S6 Post hoc analysis of center-effect adjustment
Outcome                                                                        Balloon angioplasty        Aggressive medical         Measure of Effect   Treatment Effect      P value
                                                                               group (n=249)              management group (n=252)                          (95% CI) *

Primary outcome, no. (%)

Any stroke or all-cause death within 30 days after enrollment or after BA of           9 (3.9)                     34 (13.5)            Hazard ratio     0.32 (0.16 to 0.62)    .001
the qualifying lesion, or any ischemic stroke or revascularization of the
qualifying artery beyond 30 days through 1 year after enrollment

  Data are n (%). CI denotes confidence interval. IQR denotes interquartile range.
  a
      Treatment effects are reported as hazard ratio with the 95% CI by adjusting for groups and centers.
  We divided the participating centers into Beijing Tiantan Hospital and other centers when adjusting the center effect.




                                                                                                     19

```

### DOC-002 PDF page 20

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=20)

```text
     Table S7 Post-hoc analysis of treatment interaction on the primary outcome regarding different sites
        Site                       No. of patients   Balloon angioplasty       Aggressive medical      Measure of Effect   Treatment Effect     P for interaction
                                                       group (N=233)       management group (N =238)                          (95% CI)


        Beijing Tiantan Hospital        256                4(2.9)                   19(16.1)             Hazard ratio      0.17(0.06 to 0.51)         .10

        Other centers                   245                7(6.3)                   15(11.2)             Hazard ratio      0.56(0.23 to 1.36)

    Data are n (%). CI denotes confidence interval. IQR denotes interquartile range.




                                                                                           20

```

### DOC-002 PDF page 21

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=21)

```text
              Table S8. Study outcomes in the per-protocol population (PPS)
Outcome                                                                                       Balloon angioplasty      Aggressive medical      Measure of Effect   Treatment Effect      p value
                                                                                                group (n=249)       management group (n=252)                           (95% CI)

Primary outcome, no. (%)

Any stroke or all-cause death within 30 days after enrollment or after BA of the qualifying         9 (3.9)                 33 (13.9)             Hazard ratio     0.27 (0.13 to 0.56)   <.001
lesion, or any ischemic stroke or revascularization of the qualifying artery beyond 30 days
through 1 year after enrollment a

  Any stroke or all-cause death within 30 days after enrollment                                     6 (2.6)                  4 (1.7)              Hazard ratio     1.55 (0.44 to 5.49)

  Any ischemic stroke from the qualifying artery beyond 30 days through 1 year after                1 (0.4)                 18 (7.6)              Hazard ratio     0.06 (0.01 to 0.41)
  enrollment

  Revascularization of the qualifying artery beyond 30 days through 1 year after                    3 (1.3)                 20 (8.4)              Hazard ratio     0.15 (0.04 to 0.50)
               a
  enrollment

       Data are n (%). CI denotes confidence interval.
       a
           Fulfills one of the following requirements to be considered for revascularization of the qualifying artery: (1) Acute revascularization: acute qualifying
           artery occlusion accompanied by neurological deficit, requiring intravenous thrombolysis, intraarterial thrombolysis, mechanical thrombectomy, balloon/stent
           angioplasty, or intracranial-extracranial bypass; (2) Elective revascularization: neurologic symptom-driven revascularization, including BA, stent implantation, or
           intracranial-extracranial bypass.




                                                                                                          21

```

### DOC-002 PDF page 22

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=22)

```text
                 Table S9. Study outcomes in the as-treated population (ATS)
Outcome                                                                            Balloon angioplasty           Aggressive medical      Measure of Effect    Treatment Effect      p value
                                                                                     group (n=249)            management group (n=252)                            (95% CI)

Primary outcome, no. (%)

Any stroke or all-cause death within 30 days after enrollment or after BA of the        11 (4.5)                      34 (13.4)                Hazard ratio   0.32 (0.16 to 0.64)    .001
qualifying lesion, or any ischemic stroke or revascularization of the qualifying
artery beyond 30 days through 1 year after enrollment a

   Any stroke or all-cause death within 30 days after enrollment                         8 (3.3)                       4 (1.6)                 Hazard ratio   2.09 (0.63 to 6.92)

   Any ischemic stroke from the qualifying artery beyond 30 days through 1 year          1 (0.4)                      19 (7.5)                 Hazard ratio   0.05 (0.01 to 0.39)
   after enrollment

   Revascularization from the qualifying artery beyond 30 days through 1 year            3 (1.2)                      21 (8.3)                 Hazard ratio   0.14 (0.04 to 0.47)
                      a
   after enrollment

          Data are n (%). CI denotes confidence interval.
          a
              Fulfills one of the following requirements to be considered for revascularization of the qualifying artery: (1) Acute revascularization: acute qualifying
              artery occlusion accompanied by neurological deficit, requiring intravenous thrombolysis, intraarterial thrombolysis, mechanical thrombectomy, balloon/stent
              angioplasty, or intracranial-extracranial bypass; (2) Elective revascularization: neurologic symptom-driven revascularization, including BA, stent implantation, or
              intracranial-extracranial bypass.




                                                                                                         22

```

### DOC-002 PDF page 23

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=23)

```text
     Table S10. Post-hoc analysis of the comparison of any stroke or all-cause death within 30 days after enrollment or after BA of the qualifying lesion or any
      ischemic stroke from the qualifying artery beyond 30 days through 1 year after enrollment between BA and AMM groups
Outcome                                                                               Balloon angioplasty   Aggressive medical   Measure of Effect   Treatment Effect   p value
                                                                                            group           management group                            (95% CI)


Intention-to-treat population, no. (%)                                                      N=249                N=252

Any stroke or all-cause death within 30 days after enrollment or after BA of the            9 (3.6)           23 (9.1)             Hazard ratio      0.39 (0.18-0.85)     .01
qualifying lesion, or any ischemic stroke from the qualifying artery beyond 30 days
through 1 year after enrollment

Per-protocol population, no. (%)                                                            N=233                N=238

Any stroke or all-cause death within 30 days after enrollment or after BA of the            7 (3.0)              22 (9.2)          Hazard ratio      0.32 (0.14-0.75)     .01
qualifying lesion, or any ischemic stroke from the qualifying artery beyond 30 days
through 1 year after enrollment

As-treated population, no. (%)                                                              N=247                N=254

Any stroke or all-cause death within 30 days after enrollment or after BA of the            9 (3.6)              23 (9.1)          Hazard ratio      0.40 (0.19-0.86)     .02
qualifying lesion, or any ischemic stroke from the qualifying artery beyond 30 days
through 1 year after enrollment

Data are n (%). CI denotes confidence interval.




                                                                                                23

```

### DOC-002 PDF page 24

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=24)

```text
        Table S11. Number of patients with other serious adverse events (by system organ class) up to 1-year visit
    System organ class, n (%)                                        Balloon angioplasty group (n=249)   Aggressive medical management group (n=252)   P value

    Overall                                                                      12 (4.8)                                  14 (5.6)                     0.84c
       Nervous system disorders
                                                                                  7 (2.8)                                  12 (4.8)                     0.35c
                                                                                  3 (1.2)                                  1 (0.4)
       Symptomatic intracranial hemorrhage a                                                                                                            0.37d
                                                                                  3 (1.2)                                  0 (0.0)
       Asymptomatic intracranial hemorrhage                                                                                                             0.12d
                                                                                  6 (2.4)                                  1 (0. 4)
       Any intracranial hemorrhage                                                                                                                      0.07d
       Disabling stroke b                                                         6 (2.4)                                  18 (7.1)
                                                                                                                                                        0.02c

    Vascular and lymphatic system disorder                                        2 (0.8)                                  1 (0.4)                      0.62d

    Metabolic and nutritional disease                                             1 (0.4)                                  1 (0.4)                      1.00d

    Infection                                                                     0 (0.0)                                  2 (0.8)                      0.50d

    Various surgical and medical operations                                       2 (0.8)                                  0 (0.0)                      0.25d

    Respiratory, thoracic and mediastinal disorder                                1 (0.4)                                  1 (0.4)                      1.00d

    Gastrointestinal disorder                                                     1 (0.4)                                  1 (0.4)                      1.00d

    Injury and poisoning                                                          0 (0.0)                                  1 (0.4)                      1.00d
    Benign, malignant, and unexplained tumor (including cystic and
                                                                                  1 (0.4)                                  0 (0.0)                      0.50d
    polypoid)
    Reproductive system and breast disease                                        1 (0.4)                                  0 (0.0)                      0.50d


a
    Symptomatic intracranial hemorrhage was defined as subarachnoid, parenchymal, or intraventricular hemorrhage identified on brain MRI or CT, which led to new
neurologic symptoms (consciousness level change, headache, or focal neurologic symptoms), lasting over 24 hours or a seizure.
b
    Disabling stroke was defined as modified Rankin Scale > 2 at 1 year.
c
    Tested by Chi-square test.
d
    Tested by Fisher's exact test.



                                                                                        24

```

### DOC-002 PDF page 25

[Source page](../../../joi240088supp1_prod_1746815064.21247.pdf#page=25)

```text
   Table S12. The proportion of patients meeting the proposed target of vascular risk factor management at 1-year follow-up


                             Risk Factors                               Balloon angioplasty group      Aggressive medical
                                                                                (n=249)             management group (n=252)

                             No. Patients evaluated                               139                         120

                             LDL-c level is < 1.8mmol/L, no. (%)                66(47.5)                    61(50.8)

                             No. Patients evaluated                               141                         122

                             Triglycerides < 200mg/dL, no. (%)                  127(90.1)                   104(85.3)

                             No. Patients evaluated                                65                          66

                             HbA1c < 7.0%, no. (%)                              46(70.8)                    48(72.7)

                             No. Patients evaluated                               166                         160

                             ≤140/90 mmHg (without DM), no. (%)                 119(71.7)                   119(74.4)

                             No. Patients evaluated                                81                          83

                             ≤130/80 mmHg (DM), no. (%)                         17(21.0)                    24(28.9)




                                                                           25

```


<!-- END support_doc002_pp001-025.md -->

---


<!-- BEGIN support_doc003_pp001-032.md -->

# DOC-003 support evidence: PDF pages 1-32

Scope: all 32 assigned PDF pages, individually opened; document role PLAN throughout. Pages 1-2 identify bundle versions; pages 3-32 belong to original protocol V2.0 dated June 25, 2018. Source: [protocol bundle](../../../joi240088supp2_prod_1746815064.36071.pdf#page=1). Mapping is descriptive, without candidate diagnosis. Reused eligible individual page layout files from `.ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/`; legacy native/layout engine version unavailable. Scientific coverage COMPLETE, 32/32; derivative gaps none in this shard. No fresh extraction, rendering or OCR was required. Inventory and reused-asset hashes existed before scientific mapping. No source/reused asset was modified. No Office source, formula or cached workbook value applies.

## Per-page coverage and matching keys

| PDF page | Status | Complete content map and result-matching key |
|---|---|---|
| 1 | COMPLETE | Version list: original V2.0-20180625; amendments V2.1-20200414, V2.2-20211222; final V2.3-20220328. No quantitative result; preserves version identity. |
| 2 | COMPLETE | Bundle ranges: original protocol pp3-59, final pp60-123; original SAP pp124-139, final pp140-158. Administrative locator only. |
| 3 | COMPLETE | Original protocol V2.0, June 25, 2018; title and investigator metadata. No applicable quantitative result. |
| 4 | COMPLETE | Contents, original protocol endpoint/inclusion/randomization/intervention/follow-up sections. No additional numeric design relationship. |
| 5 | COMPLETE | Contents continuing statistics/sample size/interim/subgroups and appendices. No additional numeric design relationship. |
| 6 | COMPLETE | Signature/ethics page. No applicable quantitative relationship. |
| 7 | COMPLETE | PLAN-A-design/population/intervention: multicenter prospective randomized open-label blinded endpoint PROBE; superiority of BA+AMM vs AMM. Age35-80; recent TIA<90d or stroke21-90d; stenosis70-99%. Aspirin100mg daily entire follow-up, clopidogrel75mg daily first90d; resistant patients may use ticagrelor/cilostazol. |
| 8 | COMPLETE | PLAN-A-primary/secondary: atorvastatin20-80mg/d for1year, LDL<1.8mmol/L or<70mg/dL; BP130-140/90-100mmHg. Primary stroke/death within30d, or any ischemic stroke/revascularization qualifying artery after30d through12mo. All10 secondary outcomes transcribed below and indexed in hierarchy record. |
| 9 | COMPLETE | PLAN-A-eligibility: inclusion1-4 and exclusion1-8 opening. DSA WASID70-99%, lesion≤10mm, diameter≥1.5mm, normal distal artery; antithrombotic/risk management. Exclusion thresholds: surgery30d/planned90d, lysis24h, worsening24h, stroke<21d, other70-99% stenosis, parent>50% or opposite extracranial>70%, mRS≥3. |
| 10 | COMPLETE | Exclusion8-18 continued, all preserved below: nonatherosclerosis, calcification, embolic mechanisms/MI6wk, intracranial lesion, hemorrhage3mo, prior/planned target intervention, DAPT impossible, access, allergies; Hb<100g/L, platelets<100×10^9/L, irreversible INR>1.5, ALT/AST>3×ULN, creatinine>2×ULN. |
| 11 | COMPLETE | Exclusion19-24: pregnancy/lactation, concurrent renal/radial/coronary intervention, survival<1yr, follow-up impossible, other unfinished trial, investigator unsuitability. PLAN-A-synopsis-power: exponential event time; medical risk12.2%, BA6.25%; hazards6.45%,13.01%;5% crossover after3mo; λmcb=.25λm+.75λb=8.09%; adjusted control λm*=.05λmcb+.95λm=12.76%; two-sided logrank; SAS9.3/EAST6.0;686 patients/91events;90% confidence; α=.05;50% relative risk reduction; Lan-DeMets6% expansion. |
| 12 | COMPLETE | Power sequence728 after interim expansion;10% attrition;final802. PLAN-A-follow-up: baseline, DSA, discharge,30±7d,90±7d,6mo±14d,1yr±30d, then6monthly to3yr. Training3-5 procedures per center; first100 patients30d safety feasibility discussion. |
| 13 | COMPLETE | Abbreviations: FAS full analysis set, CI confidence interval, DSMB, endpoint instruments. No numeric result. |
| 14 | COMPLETE | Abbreviations continuing mRS, MoCA, SAP, TIA, WASID. No additional numeric result. |
| 15 | COMPLETE | Complete visit-assessment matrix preserved below: visits1-7 and8-11; baseline15d-0d; angiogram0d; discharge;30±7d;90±7d;6mo±14d telephone;1yr±30d;6monthly1-3yr. mRS baseline,30d,90d,6mo,1yr,later; NIHSS baseline,discharge,90d,1yr; EQ-5D/MoCA baseline,1yr,later. Optional HbA1c/platelet/genotype/MoCA/HR-VWI/TCD and CTP footnotes; events at all visits. |
| 16 | COMPLETE | Matrix abbreviation continuation only; no additional quantitative relationship. |
| 17 | COMPLETE | Background: Asian stroke share up to50%, historical1yr recurrence23%, short-term≤3mo context. Historical figures are not BASIS outcome estimates or power inputs here. |
| 18 | COMPLETE | PLAN-A-hypothesis: superiority;50% primary-risk decrease in12mo. Objective includes stroke/all-cause death within30d of enrollment OR BA during follow-up; later qualifying-artery ischemic stroke/revascularization. PROBE,1:1. Training3-5 videos;operator annual BA>50. Population here stroke21-90d, TIA<90d,70-99%. |
| 19 | COMPLETE | Identical-arm AMM doses/durations; BP130-140/90-100, LDL targets;first100 safety review. Primary definition repeated stroke/death30d;ischemic stroke/revascularization after30d through12mo. Ischemic stroke sudden focal deficit CT/MRI confirmed; hemorrhage CT/MRI plus symptoms continuing p20. |
| 20 | COMPLETE | PLAN-A-primary-components: symptomatic hemorrhage symptoms>24h or seizure;counts primary within30d enrollment or within30d follow-up BA. Revascularization30d-12mo acute occlusion with deficit and listed rescue procedures; elective symptom-driven BA/stent/bypass for CT/MRI recurrent target stroke or recurrent TIA>10min/new disabling symptoms. Secondary1-3: target stroke/all-cause death90d, other-territory stroke90d,mRS90d. |
| 21 | COMPLETE | Secondary4-10: target stroke/all-cause death12mo,other-territory stroke12mo,revascularization12mo,mRS12mo,restenosis>70% or increase30%,stroke/MI/vascular-death12mo,EQ-5D12mo. Inclusion1-3: age35-80, here stroke14-90d/TIA<90d, prior therapy; DSA ICA C4-C7,MCA M1,VA V4,BA,stenosis70-99%,lesion≤10mm,diameter≥1.5mm. |
| 22 | COMPLETE | Inclusion3 continuation/4 consent. Full exclusion1-10 repeated: surgery30d or≥3-grade within90d,lysis/worsening24h,stroke<21d,other70-99%,parent>50%,contralateral extracranial>70%,mRS≥3;nonatherosclerosis,calcification,embolism/MI6wk. |
| 23 | COMPLETE | Exclusion11-24 repeated; all laboratory/organ thresholds as p10;survival<1yr. Consent heading. |
| 24 | COMPLETE | Consent and center-stratified IWRS central randomization,1:1 individual eligible patients. Allocation list storage; DSA evaluation heading. |
| 25 | COMPLETE | PLAN-A-intervention-technique: central imaging review; technical success residual≤50%; DAPT aspirin100mg/clopidogrel75mg≥3d pre-BA; heparin during; aspirin throughout; clopidogrel75mg or ticagrelor90mg twice daily90d; replacement if CYP2C19 loss-of-function or ADP aggregation>40%;atorvastatin20-80mg/d1yr. |
| 26 | COMPLETE | General anesthesia; femoral/radial access. ASITN/SIR poor collateral<3;wire.014inch;balloon covers lesion+≥2mm each end;submaximal diameter≤70% proximal artery;nominal-pressure inflation10-30s repeated2-3times if necessary;smaller pre-dilation permitted. |
| 27 | COMPLETE | Success residual≤50%,mTICI3,no flow-impairing dissection. Rescue for residual≥70%/unstable flow mTICI<2b,dissection with mTICI<2b,or thrombosis/embolization. Final DSA10-15min. Both arms identical AMM aspirin100mg entire/clopidogrel75mg90d, replacement resistance ADP>40% or CYP2C19;training6monthly. |
| 28 | COMPLETE | PLAN-A-risk-targets: LDL<1.8mmol/L or70mg/dL; BP checks screening,randomization,discharge,30,90,180d,1yr,end;target≤140/90 without DM or≤130/80 with DM. Non-HDL<100mg/dL;add drugs if non-HDL≥100 or TG≥200mg/dL despite statin. |
| 29 | COMPLETE | HbA1c<7%;FPG/HbA1c baseline,30d,90d,1yr. Moderate activity30min/day3times/week. Clopidogrel supply3-5d screening and wording after90d;atorvastatin to1yr;tablet counting adherence;LDL threshold>1.8/>70;drug options. |
| 30 | COMPLETE | Drug-option doses lisinopril10/40mg,candesartan16/32,atenolol50/100,felodipine5/10,clonidine.1,hydralazine50;chlorthione25mg starts p29. Benefit/supply descriptions;follow-up to primary endpoint or study end,continue outcome collection following treatment discontinuation/other intervention if consent. |
| 31 | COMPLETE | Follow-up30±7d,90±7d,6mo±14d,1yr±30d,6monthly to3yr;telephone6mo/post1yr,other in person;all require neurovascular imaging DSA/CTA/MRA1yr. Baseline data/lab list. |
| 32 | COMPLETE | Baseline smoking cigarettes/day,BMI,exercise/week and duration;mRS/NIHSS/MoCA/EQ-5D; optional HRMRI/genotype/platelet/TCD/MoCA. Visit2 randomized treatment,adverse events,medications,vitals;30d drug supply for successful randomization. |

## Relationship register for canonical merger

| Local relationship key | Statistical relationship | Exact PLAN source locations | Matching report key / scope |
|---|---|---|---|
| PLAN-A-design | PROBE superiority BA+AMM vs AMM; center-stratified IWRS1:1 | pp7,18,24 | Main trial design/randomization/analysis unit |
| PLAN-A-primary | Stroke/death0-30d then qualifying-artery ischemic stroke/revascularization>30d-12mo; objective and hemorrhage text also specify30d after BA during follow-up | pp8,18-20 | Main primary composite definition and12mo result |
| PLAN-A-secondary | Ten listed secondary outcomes with90d/12mo and component/status distinctions | pp8,20-21 | Main/supplement endpoint hierarchy, status and matching result |
| PLAN-A-synopsis-power | Exponential/hazard/crossover calculation and686/91events/90%confidence/.05/50% inputs;728 then802 | pp11-12 | Main power calculation; original detailed statistics in next shard |
| PLAN-A-population |35-80,70-99%;21-90d stroke in synopsis/design vs14-90d printed inclusion;exclusion<21d;all24 exclusions | pp7,9-11,18,21-23 | Main enrollment/analysis population and plan-version matching |
| PLAN-A-intervention | Aspirin100mg entire,clopidogrel75mg90d,atorvastatin20-80mg1yr;submaximal≤70%;success≤50% plusmTICI3;rescue thresholds | pp7-8,19,25-29 | Main/supplement BA and AMM intervention definition |
| PLAN-A-follow-up | Endpoint follow-up continuation,visit windows and modality,one-year imaging | pp12,15-16,30-32 | Main outcome ascertainment/missingness/time-point matching |
| PLAN-A-risk-targets | BP synopsis130-140/90-100;detailed≤140/90(noDM) or≤130/80(DM);LDL,HbA1c/non-HDL thresholds | pp8,19,28-29 | Main/supplement AMM targets |

All supplied text assertions are retained separately, without treating original and final protocol versions as interchangeable. Missing statistical details are explicitly deferred to supplied SAP units owned by other shards, rather than inferred. No inferential result, CI or P-value from BASIS participants appears in this shard.

## Complete reusable page transcription appendix

Every assigned page follows, including criterion items and all schedule footnotes. This is native/layout transcription, a locator aid; exact PDF remains final authority. Page links target source PDF pages, not printed section numbers.

### DOC-003 PDF page 1

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=1)

```text
     BASIS                                                                      Number:2017YFC1307900


 1                                            Protocol
 2
 3   This trial protocol has been provided by the authors to give readers additional information
 4   about their work.
 5
 6   Balloon Angioplasty vs. Aggressive Medical Management for Symptomatic Intracranial
 7   Artery Stenosis: The BASIS Randomized Clinical Trial
 8
 9   Versions of BASIS Protocols

10   BASIS Protocol V2.0-20180625 (original version)

11   BASIS Protocol V2.1-20200414 (amended version)

12   BASIS Protocol V2.2-20211222 (amended version)

13   BASIS Protocol V2.3-20220328 (final version)


14


15


16


17


18


19


20


21


22


23

                                                    1

```

### DOC-003 PDF page 2

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=2)

```text
     BASIS                                                                         Number:2017YFC1307900


24   This supplement contains the following items:
25   1. Original protocol in English (page 3 to 59), final protocol in English (page 60 to 123)
26   2. Original statistical analysis plan in English (page 124 to 139), final statistical analysis plan
27   in English (page 140 to 158)

28


29


30


31


32


33


34


35


36


37


38



39


40




                                                      2

```

### DOC-003 PDF page 3

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=3)

```text
     BASIS                                                                       Number:2017YFC1307900


41           Balloon Angioplasty vs. Aggressive Medical Management for

42    Symptomatic Intracranial Artery Stenosis: The BASIS Randomized

43                                          Clinical Trial

44                                             (BASIS)

45




46

47



48                                         Protocol
49

50   Research team: Beijing Tiantan Hospital, Capital Medical University, Beijing, China

51   Principal Investigator: Zhongrong Miao, MD, Professor of Neurology

52   Co-Principal Investigator: Yilong Wang, MD, Professor of Neurology

53   Protocol Version 2.0

54   Date: June 25, 2018

55




                                                    3

```

### DOC-003 PDF page 4

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=4)

```text
     BASIS                                                                                                                                   Number:2017YFC1307900


56                                                                             Contents
57   Protocol Signature Page .............................................................................................................................................6

58   1.BASIS Protocol Synopsis ........................................................................................................................................7

59   2.Abbreviations ........................................................................................................................................................13

60   3.Schedule of assessments ........................................................................................................................................15

61   4.Background............................................................................................................................................................17

62   5.Objectives and Hypothesis ....................................................................................................................................18

63      5.1 Objectives .......................................................................................................................................................18

64   5.2 Hypothesis ..........................................................................................................................................................18

65   6.Study Design .........................................................................................................................................................18

66   7.Study Endpoint ......................................................................................................................................................19

67      7.1 Primary endpoint ............................................................................................................................................19
68      7.2 Secondary endpoints.......................................................................................................................................20

69   8. Inclusion and Exclusion Criteria ..........................................................................................................................21

70      8.1 Inclusion criteria .............................................................................................................................................21
71      8.2 Exclusion criteria............................................................................................................................................22

72   9. Informed Consent .................................................................................................................................................23

73   10. Randomization ....................................................................................................................................................24

74   11. DSA evaulation and lesion evaualtion ................................................................................................................24

75   12. Balloon Angioplasty ...........................................................................................................................................25

76   13. Aggressive medical management .......................................................................................................................27

77      13.1 Antiplatelet treatment ...................................................................................................................................27
78      13.2 Vascular risk factor management .................................................................................................................27

79   14. Patient and Researcher Benefit ...........................................................................................................................30

80   15. Follow-up ...........................................................................................................................................................30

81   16. Management of (transient) ischemic events during follow-up ...........................................................................35

82   17. Assessment of endpoint and adverse events (AEs) ............................................................................................36

83      17.1 Endpoint events assessment .........................................................................................................................36

                                                                                         4

```

### DOC-003 PDF page 5

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=5)

```text
      BASIS                                                                                                                                     Number:2017YFC1307900

 84      17.2 AEs assessment ............................................................................................................................................36
 85      17.3 SAE record and report ..................................................................................................................................37
 86      17.4 Prediction of AEs and countermeasures .......................................................................................................37

 87   18. Core Laboratory..................................................................................................................................................39

 88   19. Quality control ....................................................................................................................................................40

 89   20. Statistical Analysis .............................................................................................................................................40

 90      20.1 Sample size ...................................................................................................................................................40
 91      20.2 Interim analysis ............................................................................................................................................41
 92      20.3 Subgroup analysis.........................................................................................................................................41

 93   21. Data Safety and Monitoring Board .....................................................................................................................42

 94   22. Study organization ..............................................................................................................................................42

 95   23. Research drug supply and responsibilities division ............................................................................................44

 96   24. Research Device Processing Mechanism, Characteristics, and Responsibilities Division .................................45

 97   25. Control requirements ..........................................................................................................................................48

 98   26. Institutional Review Board (IRB)/Ethics Committee (IEC) ...............................................................................49

 99   Reference ..................................................................................................................................................................50

100   Appendix ..................................................................................................................................................................51

101      Appendix Table 1. ASITN/SIR collateral circulation scale .................................................................................51
102      Appendix Table 2. modified Rankin Scale...........................................................................................................52
103      Appendix Table 3. National Institute of Health Stroke Scale (NIHSS) ...............................................................53
104      Appendix Table 4. EuroQoL 5D-5L ....................................................................................................................57
105      Appendix Table 5. mTICI grade ..........................................................................................................................59
106
107

108

109

110

111

112


                                                                                            5

```

### DOC-003 PDF page 6

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=6)

```text
      BASIS                                                                             Number:2017YFC1307900


113

114

115                                     Protocol Signature Page
116

117

118

119   I have read this protocol and agree to adhere to the requirements.
120
121   By signing this document we confirm that the clinical study will be conducted in accordance with
122   the protocol and all applicable laws and regulations including, but not limited to, the International
123   Conference on Harmonisation Guideline for Good Clinical Practice (GCP) and the ethical principles
124   that have their origins in the Declaration of Helsinki.
125
126
127
128   ——————————————————————————————————
129   Clinical Site
130
131
132
133   ———————————————                                           ————————————
134   Site Principal Investigator Signature                     Date
135

136

137
138
139
140
141
142
143
                                                         6

```

### DOC-003 PDF page 7

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=7)

```text
      BASIS                                                                        Number:2017YFC1307900

144
145
146   1. BASIS Protocol Synopsis
147

         Official Title       Balloon Angioplasty for Symptomatic Intracranial Artery Stenosis: A
                              Multicenter,     Prospective,     Open-Label,       Blinded-Endpoint,
                              Randomized, Controlled Trial
         National   Subject   Prediction model and intervention strategy for recurrence and
         and Number
                              progression of symptomatic intracranial and extracranial major artery
                              stenosis（2017YFC1307900）
         Acronym              BASIS

         PI                   Prof. Zhongrong Miao and Prof. Yilong Wang
         Study Objectives     To evaluate whether combined balloon angioplasty and aggressive
                              medical management (AMM) is superior to AMM for patients with
                              high-risk intracranial atherosclerotic stenosis (ICAS)
         Study Design         The BASIS trial is an investigator-initiated, multicenter, prospective,
                              randomized, open-label, blinded end-point (PROBE) trial
                              Patients eligible in BASIS were 35 to 80 years old, with a recent
                              transient ischemic attack (<90 days) or ischemic stroke (21 to 90
                              days) before enrollment attributed to 70-99% atherosclerotic
                              stenosis   of a major intracranial        artery (anterior/posterior
                              circulation). Patients were randomly assigned to the experimental
                              group and control group
                              Experimental group: patients will receive balloon angioplasty plus
                              AMM
                              Control group: patients will receive the AMM alone
                                  AMM： aspirin 100 mg daily for the entire follow-up and
                                   clopidogrel 75mg daily for the first 90 days after enrollment.
                                   Whether to continue taking clopidogrel after 90 days will be
                                   assessed according to the patient’s condition. Clopidogrel can be
                                   replaced with ticagrelor or cilostazol with appropriate dosage for
                                   patients with clopidogrel resistance. Atorvastatin will be taken
                                                     7

```

### DOC-003 PDF page 8

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=8)

```text
BASIS                                                                         Number:2017YFC1307900

                             at 20mg-80mg/day for one year after enrollment; the dose will
                             be adjusted to target LDL <1.8mmol/L or <70mg/dl. The
                             decision of whether to continue taking atorvastatin after one
                             year will be assessed according to the patient's condition.
                            Vascular risk factor management— blood pressure target
                             130-140/90-100 mmHg
   Primary Endpoint    The primary outcome is stroke or death within 30 days after
                       enrollment, or any ischemic stroke or revascularization of the
                       qualifying artery after 30 days through 12 months after enrollment.
   Secondary Endpoints 1.   Any stroke (ischemic or haemorrhagic stroke) in the territory of
                            the target artery or all-cause death within 90 days after enrollment
                       2.   Any stroke (ischemic or haemorrhagic stroke) outside the
                            territory of the target artery within 90 days after enrollment
                       3.   mRS (modified Rankin Scale) at 90 days
                       4.   Any stroke (ischemic or haemorrhagic stroke) in the territory of
                            the target artery or all-cause death within 12 months after
                            enrollment
                       5.   Any stroke (ischemic or haemorrhagic stroke) outside the
                            territory of the target artery within 12 months after enrollment
                       6.   Revascularization of the qualifying artery within 12 months after
                            enrollment
                       7.   mRS at 12 months
                       8.   Restenosis rate of the target artery within 12 months (defined as
                            rate of stenosis >70% or increased by 30% based on follow-up
                            neurovascular imaging)
                       9.   Combined events such as stroke, myocardial infarction, and
                            vascular death within 12 months after enrollment
                       10. Quality of life assessment (EuroQol-5-Dimensions Scale
                            [EQ-5D] questionnaire) within 12 months after enrollment.




                                              8

```

### DOC-003 PDF page 9

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=9)

```text
BASIS                                                                         Number:2017YFC1307900

   Inclusion Criteria   1.   Age 35-80 years
                        2.   Participants with primary or recurrent sICAS (a recent TIA[<90
                             days] or ischemic stroke [21-90 days] before enrollment
                             attributed to 70-99% atherosclerotic stenosis of a major
                             intracranial artery receiving treatment with at least one
                             antithrombotic drug and/or standard medical management of
                             vascular risk factors
                        3.   Diagnosed      by       DSA:   a    major    intracranial   artery
                             (anterior/posterior circulation) severe atherosclerotic stenosis
                             (70-99% according to WASID method) with lesion length ≤
                             10mm, diameter ≥1.5mm, and normal distal artery. (Regarding
                             the curvature and angle of the lesion, whether the patient is
                             enrollled in BASIS is per the investigator's determination based
                             on the patient’s anatomy);
                        4.   Informed consent signed.


   Exclusion Criteria   1.   Surgery within the past 30 days or plan to receive major surgery
                             within 90 days
                        2.   Thrombolytic therapy within 24 hours before enrollment
                        3.   Neurological deficit worsening within 24 hours before
                             enrollment
                        4.   Acute ischemic stroke onset within 21 days before enrollment
                        5.   Other intracranial arteries with severe stenosis (70-99%) besides
                             the target artery and its supplying artery
                        6.   Target artery’s parent artery stenosis > 50%. For example,
                             patient with MCA severe stenosis (target artery) and ipsilateral
                             ICA stenosis > 50% should be excluded; patient with BA severe
                             stenosis (target artery) and dominant VA stenosis > 50% should
                             be excluded; the patient with extracranial artery (non-lesion
                             side) stenosis > 70% should be excluded
                        7.   Baseline mRS ≥ 3
                        8.   Non-atherosclerotic disease (e.g., arterial dissection, moyamoya

                                                 9

```

### DOC-003 PDF page 10

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=10)

```text
BASIS                                                          Number:2017YFC1307900

             disease, vascular inflammatory lesions caused by infection,
             autoimmune        disease,   post-radiation,   postpartum   status;
             developmental or genetic abnormalities such as fibromuscular
             dysplasia, sickle cell anemia, suspected vasospasm)
        9.   Target artery with severely calcified stenosis
        10. Suspected ischemic event caused by embolism or the arterial
             embolism originates from an extracranial segment (ipsilateral
             chest or neck vascular steno-occlusive disease) or potential
             cardioembolism (e.g., atrial fibrillation, mitral stenosis, patent
             foramen ovale, left ventricular thrombus, myocardial infarction
             within 6 weeks, etc.)
        11. Coexistent intracranial tumor, aneurysm or arteriovenous
             malformation
        12. Intracranial hemorrhage within the past 3 months, including
             parenchymal        hemorrhage,     intraventricular    hemorrhage,
             subarachnoid hemorrhage, epidural hemorrhage or subdural
             hemorrhage, etc.
        13. Angioplasty procedure (including balloon dilatation, stenting, or
             endarterectomy) already performed at the original target vessel
             or its primary supplying artery, or a planned stenting procedure;
        14. Unable to receive dual antiplatelet therapy due to other disease
        15. Tortuous vascular approach that cannot be stabilized to obtain
             vascular access
        16. Allergy to heparin, aspirin, clopidogrel, contrast agents,
             anesthetics, and balloon components
        17. Haemoglobin < 100g/L, platelet count < 100×109/ L,
             international normalized ratio (INR) >1.5 (irreversible),
             coagulation dysfunction or uncorrectable bleeding factors
        18. Severe liver or kidney dysfunction. ALT > three-fold higher
             than the upper limit of normal value or AST > three-fold higher
             than the upper limit of normal value, or serum creatinine >
             two-fold higher than the upper limit of normal value

                                 10

```

### DOC-003 PDF page 11

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=11)

```text
BASIS                                                                  Number:2017YFC1307900

                 19. Pregnant and lactating women
                 20. Participants with renal artery, radial artery, or coronary artery
                     requiring concurrent intervention
                 21. Expected survival is less than 1 year
                 22. Unable to complete follow-up due to mental illness, cognitive or
                     emotional disorders
                 23. Participant in another drug/medical device clinical trial who had
                     not yet completed the study requirements
                 24. Participant not suitable for the BASIS trial per investigator’s
                     opinion.
   Sample Size        The estimation of the sample size is based on the assumption that
                 the time when an event (stroke or death) occurs follows an
                 exponential distribution. According to the 1-year results of the
                 SAMMPRIS trial, the incidence of target vessel stroke or death was
                 12.2% within 12 months after enrollment in the medical management
                 group. According to the SAMMPRIS study, the incidence of the
                 primary endpoint events was assumed to be 6.25% within 12 months
                 after balloon angioplasty for intracranial atherosclerosis. In this way,
                 the sample risk rates of the experimental group and the control group
                 were estimated to be 6.45% and 13.01%, respectively. It was assumed
                 that 5% of patients in the control group needed balloon dilatation after
                 3 months of follow-up. The risk of balloon dilation in the
                 experimental group was: λmcb = 0.25λm + 0.75λb = 8.09 %.
                 Therefore, the adjusted risk rate of the control group was determined
                 as: λm * = 0.05λmcb + 0.95λm = 12.76%.
                      The test of the null hypothesis applies a two-sided log-rank test.
                 SAS 9.3 or EAST 6.0 software was used to estimate sample size. The
                 sample size was 686 cases, and a total of 91 endpoint events were
                 estimated in the two groups, with 90% confidence, bilateral α = 0.05,
                 to detect 50 % relative risk reduction. It is assumed that the
                 Lan-DeMets loss function will lead to 6% expansion of the total type I
                 error. The SAS software is used to calculate the sample size required

                                       11

```

### DOC-003 PDF page 12

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=12)

```text
      BASIS                                                                                Number:2017YFC1307900

                                for the mid-term analysis, which increases the sample size to the
                                required 728 cases. Considering the 10% attrition rate and random
                                ratio, the final sample size of this study is 802 cases.
         Follow-up               All participants will be followed up by the on-site neurologist at
                                 baseline, the day of DSA, discharge, 30±7 days, 90±7 days, 6
                                 months±14 days, 1year ±30 days and up to 3years (at 6 months
                                 intervals after 1 year).
         Study    introduction After the study was initiated at a site, the participating study centers
         period
                                copied the video (including the DSA and endovascular process) of
                                3-5 cases of balloon angioplasty in their centers and transferred the
                                video to the core laboratory. After a review was passed, the group
                                continued enrollment, to ensure consistency of the balloon
                                angioplasty process.
                                     The first 100 participants completed the peri-operative (30 days)
                                observation,    mainly        collecting   adverse   events    during   the
                                peri-operative period. The PI met with other investigators from the
                                participating centers for interim discussion to evaluate the feasibility
                                of this treatment plan and the continuation of later research.
148


149


150


151


152


153


154


155



                                                         12

```

### DOC-003 PDF page 13

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=13)

```text
      BASIS                                                                  Number:2017YFC1307900


156   2. Abbreviations

      ACA           Anterior Cerebral Artery
      ACE           Angiotensin Converting Enzyme
      ADA           American Diabetes Association
      AE            Adverse Event
      ARB           Angiotensin Receptor Blocker
      BMI           Body Mass Index
      BP            Blood Pressure
      CEC           Clinical Events Adjudication Committee
      CFDA          China Food and Drug Administration
                    Clopidogrel in High-risk patients        with    Acute     Nondisabling
      CHANCE        Cerebrovascular Events
      CI            Confidence Interval
      CRF           Case Report Form
      CT            Computer Tomography
      CTP           Computed Tomography Perfusion Imaging
      DAPT          Dual Antiplatelet Therapy

      DICOM         Digital Imaging and Communications in Medicine

      DSA           Digital Subtraction Angiography
      DSMB          Data Safety Monitoring Board
      EoT           End of Trial
      EQ-5D         EuroQOL five Dimensions questionnaire
      FAS           Full Analysis Set
      FFR           Fractional Flow Reserve
      HDL           High Density Lipoprotein
      ICAD          Intracranial Atherosclerotic Disease
      ICAS          Intracranial Atherosclerotic Stenosis
      IDL           Intermediate Density Lipoproteins
      IEC           Independent Ethics Committee

                                                13

```

### DOC-003 PDF page 14

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=14)

```text
BASIS                                                            Number:2017YFC1307900


IRB        Institutional Review Board
IVRS       Inter-voice Response System Inter-voice
LDL        Low Density Lipoprotein
LFT        Liver Function Test
MCA        Middle Cerebral Artery
MI         Myocardial Infarction
MoCA       Cognitive Functional Outcome by the Montreal Cognitive Assessment

mRS        Modified Rankin Scale
NMPA       National Medical Products Administration

PTAS       Percutaneous Transluminal Angioplasty and Stenting

SAE        Serious Adverse Event
           Stenting and Aggressive Medical Management for Preventing Recurrent
SAMMPRIS   stroke in Intracranial Stenosis
SAP        Statistical Analysis Plan
SAS        Statistical Analysis Software SAS
SNPs       Single Nucleotide Polymorphisms
TIA        Transient Ischemic Attacks
UADE       Unanticipated Adverse Device Effect
VLDL       Very Low Density Lipoprotein
WASID      Warfarin-Aspirin Symptomatic Intracranial Disease

TCD        Transcranial Doppler




                                        14

```

### DOC-003 PDF page 15

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=15)

```text
              BASIS                                                                                                                      Number:2017YFC1307900


157           3. Schedule of assessments
158
                                                                                                                     Visit 6                       Follow up 1y to 3y
                Visit                           Visit 1    Visit 2     Visit 3         Visit 4   Visit 5                                 Visit 7
                                                                                                               Telephone interview                 (Visit 8,9,10,11)

                                                Baseline   Angiogram                                                                                    6       months
  Assessment                                                           Discharge   30d±7d            90d±7 d    6 mo±14 d            1y±30 d
                                                15d～0 d    0d                                                                                           intervals
      Informed consent                      X
      Inclusion/exclusion criteria check X
      History and physical examination X
      Vital signs1                          X              X           X           X             X                                   X
                              2
      Blood laboratory test       and
                                            X                          X           X             X                                   X
      urine routine test

      Coagulation function3                 X
      FBG, HbA1c4                           X                                      X             X                                   X

      Platelet aggregation test and/or
                                       X
      CYPC219 genotype test5

      ECG                                   X
      MRI/CT                                X                                                                                        X
          6
      CTP                                       X9                                               X                                         X
      DSA/CTA/MRA                           X9                                                                                             X
                                        7
      Life-style modification review        X                          X           X             X             X                     X             X

      mRS                                   X                                      X             X             X                     X             X
      NIHSS (neurological examination) X                               X                         X                                   X
      EQ-5D
      examination)                          X                                                                                        X             X
      MoCA5                                 X                                                                                        X             X
                      5
      HR-VWI,TCD                            X                                                                                        X

      Medication review and patient
                                                           X           X           X             X                                   X
      compliance survey

      AE、SAE and endpoints8                 X              X           X           X             X             X                     X             X8
159           1. Vital signs: blood pressure, heart rate, respiration rate, body temperature;
160           2. Blood laboratory test includes blood routine and biochemistry examinations, hepatic and renal function tests.
161           3. Coagulation function: PT, APTT, TT, FIB, INR;
162           4. HbA1c is an optional test, but is recommended for patients with Diabetes Mellitus.
163           5. Platelet aggregation test, CYPC219 genotype test, MoCA, HR-VWI and TCD test are optional according
164           to the center;
165           6. CTP is optional, but is recommended for patients with hemodynamic compromise, poor collateral or
166           perforator stroke.
167           7. Life-style modification review: including whether to smoke and the number of cigarettes per day; Weight:
168           reflect the patient's weight control through the patient's weight and BMI; Exercise: number of exercises per
169           week and duration of each exercise.
170           8. After one year of follow-up, follow-up will focus on AE, SAE and endpoint events;
171
172           Abbreviations: FBG, fasting blood glucose; HbA1c, Glycosylated Hemoglobin; ECG, electrocardiograph;
173           MRI, magnetic resonance imaging; CT, computerized tomography; CTP, CT perfusion; DSA, digital
174           subtraction angiography; CTA, computerized tomography angiography; MRA, magnetic resonance
175           angiography; digital subtraction angiography (DSA), computerized tomography angiography (CTA), or
176           magnetic resonance angiography (MRA); mRS, modified Rankin scale; EQ-5D, quality-of-life EuroQol-5

                                                                                        15

```

### DOC-003 PDF page 16

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=16)

```text
      BASIS                                                                        Number:2017YFC1307900

177   Dimensions; MoCA, Montreal cognitive assessment; HR-VWI, High-resolution vessel wall imaging; TCD,
178   transcranial Doppler; AE, adverse event; SAE, serious adverse event.




                                                      16

```

### DOC-003 PDF page 17

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=17)

```text
      BASIS                                                                            Number:2017YFC1307900



179   4. Background

180   Intracranial atherosclerotic stenosis (ICAS) is a major etiology of stroke worldwide, which is

181   associated with a high rate of stroke recurrence, substantial morbidity, and mortality, accounting for

182   up to 50% of ischemic stroke in south and east Asia.1 Despite receiving treatment with aspirin and

183   standard medical management of vascular risk factors, patients with symptomatic ICAS (sICAS)

184   still had as high as 23% stroke recurrence rate at 1 year.2,3 Therefore, optimal secondary stroke

185   prevention and reducing mortality risk in patients with sICAS is a major global health problem.

186   Currently, treatment options for sICAS include aggressive medical management (AMM), balloon

187   angioplasty, and stenting (balloon angioplasty combined with stenting); however, the optimal

188   treatment for sICAS remains unclear.

189      The SAMMPRIS and VISSIT trials showed high perioperative complication rates and no

190   significant advantage of intracranial stenting compared to aggressive medical therapy (AMM) in the

191   long term. 4, 5 The CASSISS trial reported that stenting by experienced operators didn’t add

192   additional risks of stroke or death within 30 days compared to AMM for sICAS, although it failed

193   to demonstrate a benefit of stenting.6 As lower rates of short-term stroke or mortality

194   (peri-procedural or mean follow-up ≤ 3 months) were found in balloon angioplasty compared to

195   intracranial stenting,7 balloon angioplasty alone may be a feasible alternative to stenting for sICAS

196   treatment. Moreover, several meta-analyses also proved the safety and efficacy of balloon

197   angioplasty for sICAS, which suggested that balloon angioplasty alone may be a potentially

198   promising treatment for sICAS.8-10

199      To date, limited evidence is available from RCTs to determine the efficacy and safety of balloon

200   angioplasty for sICAS patients. Hence, we designed the BASIS (Balloon Angioplasty for

201   Symptomatic Intracranial Artery Stenosis) randomized controlled trial to explore whether balloon

202   angioplasty plus AMM is superior to AMM alone in patients with sICAS.
                                                        17

```

### DOC-003 PDF page 18

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=18)

```text
      BASIS                                                                           Number:2017YFC1307900



203   5. Objectives and Hypothesis

204   5.1 Objectives

205   To investigate whether balloon angioplasty combined with AMM is superior to AMM alone for

206   patients with high-risk sICAS in the primary endpoint (ischemic/hemorrhage stroke or all-cause

207   death within 30 days after enrollment or after balloon angioplasty procedure of the qualifying lesion

208   during follow-up, or any ischemic stroke or revascularization from the qualifying artery beyond 30

209   days through 12 months after enrollment).

210   5.2 Hypothesis

211   Compared to AMM alone, balloon angioplasty combined with AMM could decrease by 50% the

212   risk of the primary endpoint in patients with high-risk sICAS over a 12-month follow-up period.

213

214   6. Study Design

215   Study introduction period

216   After the study is formally initiated at a site, the participating study center will copy the video
217   (including the DSA and endovascular process) of 3 to 5 cases of balloon angioplasty in their center
218   and transfer the video to the core laboratory (Beijing Tiantan Hospital). After the review is passed,
219   the group can continue enrollment, so as to ensure the consistency of the process of balloon
220   angioplasty. The annual volume of BA by the neurointerventionalists in the BASIS trial was more
221   than 50 cases. The neurointerventionalists from the participating centers received standard training
222   in technique from the leading center at regular intervals.
223      The BASIS trial is an investigator-initiated, multicenter, prospective, randomized, open-label,

224   blinded end-point (PROBE) trial that plans to enrolll patients with sICAS (defined as a recent TIA

225   (<90 days) or ischemic stroke (21-90 days) attributed to a 70-99% atherosclerotic stenosis of a

226   major intracranial artery (anterior/posterior circulation). The patients are randomly assigned to

227   either the experimental group or the control group at a 1:1 ratio.

                                                        18

```

### DOC-003 PDF page 19

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=19)

```text
      BASIS                                                                            Number:2017YFC1307900


228   Experimental group: patients will receive balloon angioplasty (details in procedure part) plus

229   AMM (same as the control group);

230   Control group: patients will receive AMM alone.

231          Drug administration plan of AMM: aspirin 100 mg daily for the entire follow-up and
232           clopidogrel 75mg daily for the first 90 days after enrollment. Whether to continue taking
233           clopidogrel after 90 days will be assessed according to the condition of the patient.
234           Clopidogrel can be replaced with ticagrelor or cilostazol with appropriate dosage for patients
235           with clopidogrel resistance. Atorvastatin tablets will be used 20mg-80mg/day for one year
236           after enrollment; the dose will be adjusted to control LDL <1.8mmol/L or <70mg/dl. Whether
237           to continue taking atorvastatin after one year will be assessed according to the patient’s
238           condition.
239          Risk factor management—Control blood pressure 130-140/90-100 mmHg and LDL
240           <1.8mmol/L or <70mg/dl
241   The first 100 participants will complete the peri-operative (30 days) observation, mainly to collect

242   adverse events during the peri-operative period. The PI will meet with other investigators from the

243   participating centers for interim discussion to evaluate the feasibility of this treatment plan and the

244   continuation of later research, and follow-up research can be conducted later.

245


246   7. Study Endpoint

247   7.1 Primary endpoint

248   The primary endpoint is stroke or death within 30 days after enrollment, or any ischemic stroke or

249   revascularization of the qualifying artery beyond 30 days through 12 months after enrollment.

250        Ischemic stroke is defined as a new focal neurologic deficit of sudden onset, which is confirmed

251   on brain CT or MRI. Symptomatic brain hemorrhage is defined as parenchymal, subarachnoid, or

252   intraventricular hemorrhage detected on CT or MRI, which is associated with new neurologic

253   symptoms (headache, change in the level of consciousness, or focal neurologic symptoms), lasting
                                                         19

```

### DOC-003 PDF page 20

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=20)

```text
      BASIS                                                                              Number:2017YFC1307900


254   over 24 hours or a seizure. Symptomatic brain hemorrhage will be considered a primary endpoint

255   only when it occurs within 30 days after enrollment or within 30 days after the balloon angioplasty

256   during follow-up. Revascularization of the culprit artery will be considered a primary endpoint if it

257   occurs from 30 days through 12 months after enrollment and fulfills one of the following

258   requirements:

259   a. Acute revascularization: acute qualifying artery occlusion accompanied by neurological deficit,

260        requiring intravenous thrombolysis, intraarterial thrombolysis, mechanical thrombectomy,

261        balloon/stent angioplasty, or intracranial-extracranial bypass.

262   b. Elective revascularization: neurologic symptom-driven revascularization, including BA, stent

263        implantation, or intracranial-extracranial bypass, if the participant fulfills one of the following

264        conditions:

265        1) Ischemic stroke caused by the culprit artery stenosis: a new focal neurological deficit of

266           sudden onset attributed to the territory of the culprit artery, which is confirmed as a recurrent

267           stroke on brain CT or MRI (follow-up imaging will be compared to baseline imaging for the

268           detection of new lesions);

269        2) Culprit artery stenosis that causes recurrent transient ischemic attack lasting longer than 10

270           minutes or new disabling neurological symptoms (paroxysmal limb weakness/numbness,

271           inarticulateness, diplopia, or ataxia) compared to the baseline qualifying symptoms.

272   7.2 Secondary endpoints

273   1.   Any stroke (ischemic or hemorrhage stroke) in the territory of the target artery or all-cause

274   death within 90 days after enrollment

275   2.   Any stroke (ischemic or hemorrhage stroke) outside of the territory of the target artery within

276   90 days after enrollment

277   3.   mRS at 90 days

                                                         20

```

### DOC-003 PDF page 21

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=21)

```text
      BASIS                                                                            Number:2017YFC1307900


278   4. Any stroke (ischemic or hemorrhage stroke) in the territory of the target artery or all-cause death

279        within 12 months after enrollment

280   5. Any stroke (ischemic or hemorrhage stroke) outside the territory of the target artery within 12

281         months after enrollment

282   6. Revascularization of the qualifying artery within 12 months after enrollment

283   7.    mRS at 12 months

284   8. Restenosis of the target artery within 12 months (defined as stenosis >70% or increased by 30%

285        based on following-up neurovascular imaging)

286   9. Combined events such as stroke, myocardial infarction, and vascular death within 12 months

287        after enrollment

288   10. Quality of life assessment (EuroQol-5-Dimensions Scale [EQ-5D] questionnaire) within 12

289         months after enrollment.

290   8. Inclusion and Exclusion Criteria

291   8.1 Inclusion criteria

292   1. Age 35-80 years

293   2. Participants with primary or recurrent sICAS (a recent TIA [<90 days] or ischemic stroke [14-90

294        days] before enrollment attributed to 70-99% atherosclerotic stenosis of a major intracranial

295        artery) receiving treatment with at least one antithrombotic drug and/or standard medical

296        management of vascular risk factors

297   3. Diagnosed by DSA: a major intracranial artery (terminal internal carotid artery [ICA] [C4-C7

298        segments], middle cerebral artery [MCA] M1 segment, vertebral artery [VA] V4 segment, and

299        basilar artery [BA]) severe atherosclerotic stenosis (70-99% according to WASID method11)

300        with lesion length ≤ 10mm, diameter ≥1.5mm, and normal distal artery. (Regarding the curvature


                                                        21

```

### DOC-003 PDF page 22

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=22)

```text
      BASIS                                                                          Number:2017YFC1307900


301     and angle of the lesion, whether the patient is enrollled in BASIS will be according tor the

302     investigator's determination based on the patient’s anatomy

303   4. Informed consent signed

304   8.2 Exclusion criteria
305   1. Surgery within the past 30 days or plan to receive ≥ 3-grade surgery within 90 days

306   2. Thrombolytic therapy within 24 hours before enrollment

307   3. Neurological deficit worsening within 24 hours before enrollment

308   4. Acute ischemic stroke onset within 21 days before enrollment

309   5. Other intracranial arteries with severe stenosis (70-99%) beside the target artery and its

310      supplying artery

311   6. Target artery parent artery stenosis > 50%. For example, patient with MCA severe stenosis

312      (target artery) and ipsilateral ICA stenosis > 50% should be excluded; patient with BA severe

313      stenosis (target artery) and dominant VA stenosis > 50% should be excluded; the patient with

314      extracranial artery (non-lesion side) stenosis > 70% should be excluded

315   7. Baseline modified Rankin Scale ≥ 3

316   8. Non-atherosclerotic diseases (e.g., arterial dissection, moyamoya disease, vascular inflammatory

317      lesions caused by infection, autoimmune diseases, post-radiation, postpartum status;

318      developmental or genetic abnormalities such as fibromuscular dysplasia, sickle cell anemia,

319      suspected vasospasm

320   9. Target artery with severely calcified stenosis

321   10. Suspected ischemic event caused by embolism or the arterial embolism from extracranial

322      segment (ipsilateral chest or neck vascular occlusive disease) or potential cardioembolism (e.g.,

323      atrial fibrillation, mitral stenosis, patent foramen ovale, left ventricular thrombus, myocardial

324      infarction within 6 weeks, etc.)

                                                          22

```

### DOC-003 PDF page 23

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=23)

```text
      BASIS                                                                               Number:2017YFC1307900


325   11. Coexistent intracranial tumor, aneurysm or arteriovenous malformation

326   12. Intracranial hemorrhage within the past 3 months, including parenchymal hemorrhage,

327      intraventricular hemorrhage, subarachnoid hemorrhage, epidural hemorrhage or subdural

328      hemorrhage, etc.

329   13. Angioplasty procedure (including balloon dilatation, stenting, or endarterectomy) already

330      performed at the original target vessel or its primary supplying artery, or a planned stenting

331      procedure

332   14. Unable to receive dual antiplatelet therapy due to other diseases

333   15. Tortuous vascular approach not amenable to vascular access

334   16. Allergy to heparin, aspirin, clopidogrel, contrast agents, anesthetics, and balloon components

335   17. Hemoglobin < 100g/L, platelet count < 100×109/ L, international normalized ratio (INR) >1.5

336      (irreversible), coagulation dysfunction or uncorrectable bleeding factors

337   18. Severe liver or kidney dysfunction. ALT > three-fold higher than the upper limit of normal

338      value or AST > three-fold higher than the upper limit of normal value, or serum creatinine >

339      two-fold higher than the upper limit of normal value

340   19. Pregnant and lactating women

341   20. Participants with renal artery, radial artery, or coronary artery requiring concurrent intervention

342   21. Expected survival is less than 1 year

343   22. Unable to complete follow-up due to mental illness, cognitive or emotional disorder

344   23. Participants participating in other drug/medical device clinical trials who have not yet

345      completed the study requirement

346   24. Participants are not suitable for the BASIS trial per investigator’s opinion.

347

348   9. Informed Consent
                                                         23

```

### DOC-003 PDF page 24

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=24)

```text
      BASIS                                                                            Number:2017YFC1307900


349   The clinical trial must follow the Helsinki Declaration and the relevant clinical trial norms and

350   regulations in China. Informed consent was designed based on the NMPA regulations and ICH

351   guidelines. Each patient who agrees to participate in the study will be invited to sign an informed

352   consent form. Before signing the informed consent form, a specially trained researcher

353   (understanding the key points of the study and the related risks of the study, the confidentiality of

354   the management of records and the source of funds, etc.) will introduce the research purpose, study

355   plan, study cycle, potential risks and expected benefits, cost and compensation, voluntary

356   participation principle, treatment principle of study related risks, etc.

357

358   10. Randomisation

359   The BASIS trial will use an interactive web response system (IWRS) for central randomization

360   stratified by study centers. Patients who sign the informed consent and meet all inclusion criteria

361   and do not meet any exclusion criteria will be enrollled in the study. After inputting the eligible

362   patient’s necessary information into the web-based system, the researcher in each center will obtain

363   a random code as well as the corresponding group allocation information from the IWRS. Eligible

364   patients will be randomized into either the experimental group or the control group at a 1:1 ratio

365   (Figure 1). Finally, researchers and research assistants need to print randomization application

366   forms and center randomization lists.

367       The researcher team should archive the randomized list and related files (randomized

368   application form) together in the central researcher folder (archived by the clinical study department

369   of the center).

370

371   11. DSA and lesion evaluation

                                                          24

```

### DOC-003 PDF page 25

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=25)

```text
      BASIS                                                                             Number:2017YFC1307900


372   In order to ensure the quality of DSA images in the study, we will choose a clinical research center

373   with DSA facilities. Before the start of the study, researchers from all centers will participate in the

374   training of image generation, collection and evaluation, and obtain corresponding qualifications.

375      When the patient is enrollled, the central laboratory will obtain the CD disc of the patient's MRI

376   / HRMRI imaging, CT perfusion imaging, and DSA before balloon angioplasty for central review.

377   DSA imaging needs to show the residual vessel diameter at the maximum stenosis and the

378   maximum length of the stenosis. If the patient underwent balloon angioplasty, arterial imaging after

379   angioplasty should also be sent to the imaging core laboratory for central review. The standard of

380   technical success is the residual stenosis of the target vessel ≤ 50 %.

381

382   12. Balloon Angioplasty

383   Antithrombotic protocol

384   Pre-procedure: All patients who are scheduled to undergo balloon angioplasty should receive dual

385   antiplatelet therapy (aspirin 100 mg per day and clopidogrel 75 mg per day) for at least three days

386   before the procedure.

387   Intra-procedure: Intravenous anticoagulant such as heparin during the procedure.

388   Post-procedure: Aspirin 100 mg per day must be used for the entire duration of follow-up, and

389   clopidogrel 75 mg per day or ticagrelor 90mg twice a day must be used for 90 days after

390   randomization. If clopidogrel resistance testing is obtained and the results shows loss-of-function of

391   the CYP2C19 allele or platelet aggregation rate of ADP > 40%, then ticagrelor or cilostazole may

392   be used as replacement. After 90 days, whether to continue to take clopidogrel will be decided

393   according to the patient's condition and the researcher's opinion. Atorvastatin will be taken

394   20mg-80mg/day for one year after enrollment after which its continuation will be according the

395   patient's condition.
                                                         25

```

### DOC-003 PDF page 26

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=26)

```text
      BASIS                                                                             Number:2017YFC1307900


396   Anesthesia strategy and arterial access

397   The procedure should be performed under general anesthesia. Femoral artery access is

398   recommended (radial artery access is allowed for patients with tortuosity of the aortic arch or aorta).

399   Procedure steps

400   1.   A stable vascular access with a long sheath or guide catheter (an intermediate catheter is

401        recommended for participants with tortuous access), which should be placed as distal as

402        possible, is suggested to provide adequate support for performing the balloon angioplasty.

403        Collateral status assessment based on a whole brain DSA is recommended before balloon

404        angioplasty according to the ASITN/SIR collateral flow grading system (poor collateral:

405        ASITN/SIR < 3).12

406   2.   An 0.014-inch microwire with a microcatheter (or not) passes through the lesion to reach the

407        distal branch of the target artery.

408   3.   A balloon (recommending the Neuro RX and Neuro LPS Intracranial Balloon Dilation Catheter

409        [Sinomed Inc., Tianjin, China]) is navigated over the microwire to the target artery lesion.

410        Balloon size selection: the balloon length should cover the lesion completely and cover at least

411        2 mm beyond each end of the lesion. The balloon diameter is determined according to the

412        treating physician’s opinion (submaximal angioplasty is suggested: balloon with a diameter no

413        more than 70% of the proximal artery diameter).

414   4.   The balloon should be slowly inflated to nominal pressure, and maintained at this pressure for

415        10 to 30 seconds before deflating slowly. This step can be repeated 2 to 3 times if the dilation

416        effect of the balloon angioplasty is not satisfactory. For patients with extremely severe stenosis,

417        a relatively smaller balloon can be used for pre-dilation.




                                                         26

```

### DOC-003 PDF page 27

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=27)

```text
      BASIS                                                                            Number:2017YFC1307900


418   5.   Technical success: residual stenosis ≤ 50% of the proximal artery diameter with modified

419        Thrombolysis in Cerebral Infarction (mTICI)13 3 grade without arterial dissection that impairs

420        the distal blood flow.

421   6.   Rescue stent implantation is allowed when: (1) residual stenosis ≥ 70% after balloon dilation or

422        the antegrade flow is unstable (mTICI < 2b); (2) arterial dissection impairs distal blood flow

423        (mTICI < 2b); (3) development of thrombosis or embolization that jeopardizes distal perfusion.

424        Other measures such as intravenous/intra-arterial thrombolysis, infusion of GP IIb/IIIa

425        inhibitors, are based on the physician's experience, which can be used alone or in combination

426        with rescue stenting.

427   7.   A final DSA should be performed after 10 to 15 minutes of observation.

428   13. Aggressive medical management

429   13.1 Antiplatelet treatment

430   AMM will be identical in both arms. All the necessary blood and imaging tests are collected in the

431   screening period before randomization for the management of risk factors. Both arms are prescribed

432   with an AMM regime (includes aspirin 100 mg per day for the entire follow-up and clopidogrel

433   75mg per day for the first 90 days after enrollment). Clopidogrel can be replaced with ticagrelor or

434   cilostazol with appropriate dosage for patients with clopidogrel resistance (Platelet aggregation rate

435   of adenosine diphosphate >40% or Loss-of-function allele of CYP2C19 is detected).

436   13.2 Risk factor management

437   Neurologists and study investigators at each site will be responsible for the management of the

438   patients’ risk factors. They will receive training on risk factor management according to the Chinese

439   Stroke Association guidelines for the clinical management of cerebrovascular disorders.14 All study

440   investigators will be regularly trained according to the BASIS protocol every 6 months. If a patient


                                                        27

```

### DOC-003 PDF page 28

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=28)

```text
      BASIS                                                                         Number:2017YFC1307900


441   fails to reach the target goal of risk factor management, a face-to-face follow-up with the local

442   neurologist to modify their medical regime will be necessary.

443   13.2.1 Primary risk factors

444   Achieving target LDL cholesterol

445   The baseline serum low-density lipoprotein cholesterol (LDL-c) level is recorded before enrollment.

446   The target LDL-c level is < 1.8mmol/L or 70 mg/dl. If the patient’s LDL level is higher than the

447   target level, he/she should modify the lipid-lowering drugs. Liver enzyme (AST / ALT) levels will

448   be measured at the beginning of the study and at each visit point.

449   Blood pressure management

450   Blood pressure will be checked at screening, randomization, discharge, 30 days, 90 days, 180 days,

451   1 year, and at the end of the trial. Patients may need to visit local sites for blood pressure

452   measurement and modify their medical regime if necessary. The target blood pressure is no more

453   than 140mmHg/90mmHg for patients without DM and no more than 130mmHg/80mmHg for

454   patients with DM. Antihypertensive drugs include Angiotensin-converting enzyme inhibitor (ACEI),

455   Angiotensin Receptor Blocker (ARB), beta-blocker, calcium channel antagonist (CCB), diuretic,

456   vasodilator, etc.

457   13.2.2 Secondary risk factors

458   Non-HDL cholesterol

459   The target level of non-HDL cholesterol is < 100 mg/dL. Non-HDL cholesterol includes

460   low-density lipoproteins (LDL), very-low-density lipoproteins (VLDL), and intermediate-density

461   lipoproteins (IDL). When a larger statin dosage fails to lower the LDL level, if non-HDL

462   cholesterol ≥ 100 mg/dL or triglycerides are ≥ 200mg/dL, other lipid-lowering drugs in addition to

463   statin are recommended, such as ezetimibe or PCSK9 inhibitors.

464   Diabetes management

                                                        28

```

### DOC-003 PDF page 29

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=29)

```text
      BASIS                                                                             Number:2017YFC1307900


465   The target of DM management is to achieve HbA1c < 7.0%. Fasting plasma glucose (FPG) and

466   HbA1c levels will be measured at baseline, 30 days, 90 days, and 1 year.

467   Lifestyle modification

468   Smoking cessation: investigators at each site will evaluate smoking status at each follow-up and

469   encourage all subjects to quit smoking as soon as possible.

470   Weight management: investigators at each site will evaluate the patient’s weight according to

471   body mass index (BMI).

472   Activity level: activity level for each patient is also assessed at each follow-up by trained

473   investigators or coordinators. Moderate exercise of 30 minutes a day, three times per week is

474   strongly recommended to all patients with athletic ability.

475   13.2.3 Research drugs

476   During the screening period of BASIS, clopidogrel will be provided free of charge for 3 to 5 days.

477   After 90 days of enrollment, clopidogrel will also be provided free of charge. From enrollment to 1

478   year, atorvastatin if required by patients will be provided free of charge, and other drugs will be

479   purchased by the patients.

480   At each visit point, the patient's compliance with treatment will be evaluated by counting the

481   number of clopidogrel and atorvastatin tablets.

482   Patients with LDL > 1.8 mmol / L or > 70 mg / dL will be treated with atorvastatin. Whether to

483   continue taking atorvastatin after 1 year will be assessed based on the patient's condition. If patients

484   are taking other lipid-lowering drugs, patients are encouraged to switch to atorvastatin (not

485   mandatory). For patients whose blood pressure does not reach the treatment goal, antihypertensive

486   drugs will be given. Patients can choose to use but are not limited to the following antihypertensive

487   drugs:

488      Diuretic (Chlorthione 25mg)

                                                         29

```

### DOC-003 PDF page 30

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=30)

```text
      BASIS                                                                            Number:2017YFC1307900


489      Angiotensin-converting enzyme inhibitor (ACEI) (Lisinopril 10mg or 40 mg)

490      Angiotensin Receptor Blocker (ARB) (Candesartan 16mg or 32 mg),

491      Beta-blocker (Atenolol 50mg or 100mg)

492      Calcium channel antagonist (CCB) (Felodipine 5mg or 10 mg)

493      Central α agonist (clonidine 0.1mg)

494      Vasodilator (hydralazine 50mg)

495

496   14. Patient and Researcher Benefit

497   Patient benefit: Patients participating in this study will receive systematic treatment and follow-up.

498   Clopidogrel is provided free of charge during the screening period and 90 days of enrollment, and

499   atorvastatin tablets are provided free of charge from enrollment to 1 year. DSA is free at 1-year

500   follow-up. However, other related examinations and medications are not free, and the balloons used

501   when they are randomly assigned to the experimental group are not free.

502   Researcher benefit: Researchers participating in this study have the right to the use of scientific

503   data to publish scientific research.

504

505   15. Follow-up

506   All patients will be followed up to the primary endpoint of the study or to the end of the study.

507   Unless the patient does not agree to continue participating in the study, efforts will be made to

508   obtain complete endpoint information (whether the patient is cured or dead). If the patient

509   discontinues from this study and receives other treatments such as stenting, but agreed to provide

510   endpoint information, follow-up will continue.




                                                        30

```

### DOC-003 PDF page 31

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=31)

```text
      BASIS                                                                           Number:2017YFC1307900


511       All participants will be followed up by the on-site neurologists at baseline, the day of DSA,

512   discharge, 30±7 days, 90±7 days, 6 months±14 days, 1 year ±30 days, and up to 3 years (at 6

513   months intervals after 1 year). Follow-up visits will be conducted by telephone at 6-month and

514   post-1-year periods and will be evaluated in person at other visits. At each follow-up visit, the

515   participants’ medications, laboratory tests, risk factor management (as described above), and

516   possible adverse events/endpoints are reviewed by an experienced neurologist and/or

517   neurointerventionalist. All patients are required to undergo a neurovascular imaging examination

518   including DSA, CTA or MRA at 1-year follow-up.

519   Visit 1: Screening

520      Signed informed consent

521      Review inclusion/exclusion criteria

522      Randomization-experimental group: balloon angioplasty+AMM; control group: AMM

523      Medical history, concomitant medication, demographic data collection

524      Ischemic stroke history record

525      Vital signs, blood routine, urine routine, blood biochemistry, coagulation function examination

526       Vital signs: Blood pressure, heart rate, respiration, body temperature；

527       blood biochemistry: Renal function: creatinine, urea (or urea nitrogen), glucose, uric acid, total

528       bilirubin, direct bilirubin, indirect bilirubin, lactate dehydrogenase, creatine kinase isoenzyme;

529       liver function: alkaline phosphatase, glutamyl transpeptidase, aspartate aminotransferase,

530       alanine aminotransferase; blood lipids: total cholesterol, low-density lipoprotein, high-density

531       lipoprotein, triglyceride;

532       Coagulation function: PT, APTT, TT, FIB, INR

533      Fasting blood glucose, HbA1c (optional)

534      Pregnancy test
                                                       31

```

### DOC-003 PDF page 32

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=32)

```text
      BASIS                                                                           Number:2017YFC1307900


535      Electrocardiogram

536      DSA

537      MRI/HRMRI (HRMRI is unnecessary; if MRI is not available, CT can replace MRI)

538      CTP (anterior circulation sICAS)

539      Patient smoking cessation information, weight, and exercise will be collected. Smoking

540       cessation documentation will include whether the patient plans to smoke and the number of

541       daily cigarettes; weight: the patient's weight and BMI will reflect the patient's weight control;

542       exercise: weekly exercise frequency will be recorded, as well as each exercise duration

543      mRS, NIHSS, MoCA, EQ-5D (MoCA is unnecessary)

544      Platelet function test and/or CYPC219 genotype test will be obtained according to the

545       availability at the center, this item is unnecessary

546      TCD (recommend but not necessary)

547      Research drug distribution: Clopidogrel (only for patients who are enrollled in BASIS)

548      Aspirin and clopidogrel medication orders

549      Concomitant medication collection

550      AE, SAE and endpoint observation

551   Visit 2: Treatment

552      Treatment according to the randomization assignment

553      Concomitant medication collection

554      Vital signs

555      Research drug distribution and recovery (Randomly successful patients are provided 30 days

556       follow-up research drug; Randomly failed patients recover research drugs issued during the

557       screening period; randomly successful patients are given clopidogrel and atorvastatin tablets)

558      Aspirin, clopidogrel and atorvastatin medication orders

                                                         32

```


<!-- END support_doc003_pp001-032.md -->

---


<!-- BEGIN support_doc003_pp033-064.md -->

# DOC-003 support evidence: PDF pages 33-64

Scope: all32 assigned pages individually opened, PLAN throughout. Original protocol V2.0 continues pp33-59; final V2.3 dated March28,2022 begins p60. Source: [protocol bundle](../../../joi240088supp2_prod_1746815064.36071.pdf#page=33). Scientific coverage COMPLETE32/32; reusable-backed30 pages and fresh-required2 pages (46,48) closed by fresh CPU PyMuPDF1.26.4 source renders, visually inspected. Render paths: `.ai_paper_validation/review_1_6_2/preprocessing/plan-page-46.png` and `plan-page-48.png`. Existing individual layouts `.ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-N.layout.txt` were reused (legacy engine version unavailable); retained images pp45/47/58 also visually inspected. No OCR was needed. Two raster tables absent from reusable text are completely transcribed below. Inventory and hashes existed before mapping. Sources/reused assets preserved. No Office/formula/cache source applies. No candidate diagnosis.

## Per-page complete coverage

| PDF page | Status | Complete quantitative/design map and matching report key |
|---|---|---|
|33|COMPLETE|PLAN-A-visits: treatment compliance/events;discharge NIHSS,labs optional,life-style/cost;30±7d mRS,labs/drugs/adherence/AE/SAE/endpoints;90±7d starts.|
|34|COMPLETE|90d mRS/NIHSS,CTP optional,labs/atorvastatin/adherence/events;6mo±14d telephone mRS/events;1yr±30d MRI(orCT),DSA necessary/CTP optional,mRS/NIHSS/MoCA(optional)/EQ-5D,TCD optional.|
|35|COMPLETE|1yr aspirin/labs/adherence/events;after1yr every6mo±30d visits8-11;9/11 face-to-face with mRS/MoCA/EQ-5D;telephone other visits;events all;management of neurological follow-up events.|
|36|COMPLETE|PLAN-A-revascularization: symptomatic experimental-arm restenosis≥70% DSA leads expert advice about revascularization;not recommended<70%. Endpoint strokes/death/revascularization;report48h,adjudicate7d by2of3 blinded committee. SAE definition death/life-threatening/hospitalization/disability/intervention.|
|37|COMPLETE|All expected device complications retained below;UADE definition;AE/SAE from consent through study end including discontinued-treatment patients;reportSAE24h. No BASIS result count.|
|38|COMPLETE|Complication mechanisms and management;acute occlusion typically within30min BA. No applicable inferential quantitative relationship.|
|39|COMPLETE|Rupture/hyperperfusion management;independent imaging core review blinded to clinical/treatment data by>10yr experts. No result estimate.|
|40|COMPLETE|PLAN-A-analysis: primary event rate/95%CI Kaplan-Meier,logrank comparison,HR/95%CI Cox;secondary time-to-event KM/Cox;mRS common OR ordinal-logistic;secondary CIs no multiplicity adjustment;main ITT with PP and as-treated sensitivity;SAS9.4;missing imputation/subgroups referred SAP. Power paragraph starts12.2% target-vessel stroke/death12mo.|
|41|COMPLETE|PLAN-A-detail-power:686,80%power,two-sidedα=.05,50%reduction to6.1%;O’Brien-Fleming spending6% expansion;728;10%loss;802. Interim at half participants12mo;α1=.0015,α2=.024. All11 primary subgroups age<65/≥65,sex,hypertension,diabetes,smoking,eGFR<60/≥60ml/min/1.73m²,stenosis<80/≥80%,BMI<25/25-30/≥30kg/m²,hypoperfusion,anterior/posterior,stroke/TIA.|
|42|COMPLETE|DSMB annual review,steering twice/year,weekly operational monitoring;blinded CEC uniform outcomes;committee table no applicable statistical result.|
|43|COMPLETE|Committee/organization table continuation;no applicable result/design input.|
|44|COMPLETE|Committee closing;clopidogrel supply3-5d screening/90d enrollment then patient-purchased conditional continuation;atorvastatin free1yr,conditional thereafter.|
|45|COMPLETE|Device definition NeuroRX:working length145cm,guidewire<.014inch,catheter inner≥5F(.056inch),two markers,exit24cm from tip. Retained image inspected:2F proximal shaft,3F distal shaft,semicompliant hydrophilic balloon.|
|46|COMPLETE_FRESH|RX raster size table individually rendered/visually mapped below;9diameters1.50-4.00mm,6lengths6-25mm,48available combinations. NeuroLPS registration/materials below;administrative identifier/date not result.|
|47|COMPLETE|LPS component schematic individually inspected from retained image:L=1550±100mm,D1 expanded diameter,L2 effective balloon length;9components;two markers90%Pt/10%Ir;two-layer sheath;size table heading.|
|48|COMPLETE_FRESH|LPS raster size table individually rendered/visually mapped below:9diameters1.50-4.00mm×5lengths8,10,12,15,20mm,all45combinations. Device not free;inventory responsibilities/regulatory text no result.|
|49|COMPLETE|Ethics/protocol amendments and annual reports;no applicable quantitative relationship.|
|50|COMPLETE|References only;no additional BASIS quantitative input. External works not retrieved.|
|51|COMPLETE|PLAN-A-collateral-scale ASITN/SIR0none,1slow peripheral residual,2rapid peripheral partial territory,3slow complete bylate venous,4complete rapid retrograde;matches proceduralpoor<3.|
|52|COMPLETE|PLAN-A-mRS:ordinal0-5 disability,6death;0none,1symptoms/no disability,2slight independent,3moderate notfullyindependent,4moderately severe dependent without constantcare,5severe constantcare,6death. Main ordinal outcome/baseline threshold.|
|53|COMPLETE|PLAN-A-NIHSS:0-42 higher severity;LOC1a0-3,questions1b0-2,commands1c0-2;scoring rules fully retained.|
|54|COMPLETE|NIHSS gaze0-2,visual0-3,facial0-3,eacharm0-4/UN;arms90°sitting/45°supine10s.|
|55|COMPLETE|NIHSS eachleg0-4/UN,30°5s;ataxia0-2/UN,sensory0-2,coma(LOC3)automatic sensory2;language starts.|
|56|COMPLETE|NIHSS language0-3 (coma automatically3),dysarthria0-2/UN,neglect0-2 neverUN;fullcategory instructions retained.|
|57|COMPLETE|PLAN-A-EQ5D five domains mobility,self-care,usual activities,pain/discomfort,anxiety/depression;fiveorderedlevels each no/slight/moderate/severe/unable-or-extreme;today,self-report.|
|58|COMPLETE|EQ VAS0-100,0worstimaginable/100bestimaginable today;retained image inspected for scale.|
|59|COMPLETE|PLAN-A-mTICI grade0no perfusion,1limited slow distal,2a<half territory,2b>half,3complete withno distal occlusion;matches success/rescue criteria.|
|60|COMPLETE|Final protocol V2.3 March28,2022 title page;no result. Preserve version separation.|
|61|COMPLETE|Final contents endpoint/eligibility/intervention/follow-up references;no additional numeric relationship.|
|62|COMPLETE|Final contents stats/sample/subgroups but nointerim subsection listed;index only,substantive later pages owned other shard.|
|63|COMPLETE|Final signature/ethics page;no applicable quantitative relationship.|
|64|COMPLETE|PLAN-A-final-synopsis:PROBE superiority BA+AMM vsAMM,age35-80,TIA<90d/stroke14-90d,70-99%;terminalICA,MCAM1,VAV4,BA. Aspirin100mgdailyentire,clopidogrel75mg90d withresistance replacements;atorvastatin sentence continues p65(other shard).|

## Reconstructed original-protocol statistical relationships

| Local relationship key | Printed specification | Exact locations / report matching key |
|---|---|---|
|PLAN-A-analysis|Primary Kaplan-Meier risk and95%CI/logrank;CoxHR95%CI;secondaryKM/Cox;mRS ordinal commonOR;secondary CI widths unadjusted multiplicity;ITT primary,PP/as-treated sensitivity;SAS9.4;missingness deferred SAP.|p40;main methods and outcome measures|
|PLAN-A-detail-power|12.2% event probability at12mo;printed p41 assigns preceding rate to “experimental group”;686/80%power/two-sided.05/50%relative reduction(6.1%);O’Brien-Fleming6%→728;10%loss→802.|pp40-41;main/synopsis power assumptions. Preserve printed role/inputs, no inference.|
|PLAN-A-interim|At half participants complete12mo;interimα1=.0015;finalα2=.024.|p41;main stopping/multiplicity/finaltest level|
|PLAN-A-subgroups|All11primary subgroups with all thresholds/categories listed above;no interaction model specified here.|p41;main/supplement subgroup analysis;SAP crossmatching|
|PLAN-A-visits|30±7d/90±7d/6mo±14d/1yr±30d/later6mo±30d; instruments and event ascertainment per page table.|pp33-35;main outcome timepoints and missingness|
|PLAN-A-revascularization|Symptomatic restenosis≥70%;expert recommendation;not<70%;endpoint adjudication and SAE collection beyond discontinuation.|pp36-37;main primary components/safety population|
|PLAN-A-scales|mRS0-6 (higher worse),NIHSS0-42(higher worse),EQ-5D-5L/VAS0-100(higherVASbetter),collateral0-4,mTICI0/1/2a/2b/3.|pp51-59;main/supplement outcomes and technical success|
|PLAN-A-final-synopsis|Final14-90d stroke and primary superiority;AMM doses/durations here.|p64;final version counterpart to original pp7/9/18/21-22|

No BASIS participant result/CI/P-value is reported on these pages. Plan-derived secondary status, primary components, power, alpha and populations are kept as supplied, without harmonizing between plan locations or versions. Covariates/imputation details are not printed in these assigned statistical paragraphs; matching SAP units have other owners.

## Fresh visual transcription of device tables

[RX source p46](../../../joi240088supp2_prod_1746815064.36071.pdf#page=46), CPU render PyMuPDF1.26.4. Column lengths6,10,12,15,20,25mm. Row diameter1.50: available10,15,20mm;2.00and2.25:10,15,20,25mm;2.50,2.75,3.00,3.25,3.50,4.00:all6lengths. Absence of checkmark means no displayed available combination;units mm. Derived available-count48=3+4+4+6×6, purely inventory of device configurations, not sample size.

[LPS source p48](../../../joi240088supp2_prod_1746815064.36071.pdf#page=48), CPU render PyMuPDF1.26.4. Column lengths8,10,12,15,20mm;diameters1.50,2.00,2.25,2.50,2.75,3.00,3.25,3.50,4.00mm. Every intersection has a dot (45combinations). Raster headings and units visually read, no OCR approximation used.

## Complete eligible page transcription appendix

All32native/layout pages follow, including everyinstrument item,administrative page and reference. Raster additions above take precedence over their native-text absence;PDF remains final authority.

### DOC-003 PDF page 33

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=33)

```text
      BASIS                                                                     Number:2017YFC1307900


559      Patient compliance survey

560      AE, SAE and endpoint observation

561   Visit 3: Discharge

562      Concomitant medication collection

563      Vital signs

564      Blood routine, urine routine, blood biochemistry(optional)

565      NIHSS

566      Patients’ smoking cessation, weight, and exercise will be collected

567      Patient compliance survey

568      The disease treatment-related cost information collection

569      AE, SAE and endpoint observation

570   Visit 4: 30±7 days after enrollment

571      Concomitant medication collection

572      Vital signs, blood routine, urine routine, blood biochemistry

573      Fasting blood glucose, HbA1c (optional)

574      Patient smoking cessation, weight, and exercise data are collected

575      mRS

576      Research drug distribution: clopidogrel and atorvastatin

577      Aspirin, clopidogrel and atorvastatin calcium medication orders

578      Patient compliance survey

579      The disease treatment-related cost information collection

580      AE, SAE and endpoint observation

581   Visit 5: 90±7 days after enrollment

582      Concomitant medication collection

                                                       33

```

### DOC-003 PDF page 34

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=34)

```text
      BASIS                                                                    Number:2017YFC1307900


583      Vital signs, blood routine, urine routine, blood biochemistry

584      Fasting blood glucose, HbA1c (optional)

585      CTP (optional)

586      Patient smoking cessation, weight, and exercise data are collected

587      mRS and NIHSS

588      Research drug distribution: atorvastatin

589      Aspirin and atorvastatin medication orders

590      Patient compliance survey

591      The disease treatment-related cost information collection

592      AE, SAE and endpoint observation

593   Visit 6: 6 months±14 days after enrollment (interview by telephone)

594      Concomitant medication collection

595      Patient smoking cessation, weight, and exercise data are collected

596      mRS

597      AE, SAE and endpoint observation

598   Visit 7: 1 year±30 days after enrollment

599      Concomitant medication collection

600      Vital signs, blood routine, urine routine, blood biochemistry

601      Fasting blood glucose, HbA1c(optional)

602      MRI/HRMRI (HRMRI is unnecessary; if MRI is not available, CT can replace MRI)

603      CTP, DSA (DSA is necessary and CTP is unnecessary)

604      Patient smoking cessation, weight, and exercise data are collected

605      mRS, NIHSS, MoCA, EQ-5D (MoCA is unnecessary)

606      TCD (recommend but not necessary)

                                                       34

```

### DOC-003 PDF page 35

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=35)

```text
      BASIS                                                                              Number:2017YFC1307900


607      Research drug recovery: atorvastatin tablets

608      Patient compliance survey

609      Follow-up aspirin medication orders

610      The disease treatment-related cost information collection

611      AE, SAE and endpoint observation

612   Follow-up after 1 year: every 6 months ± 30 days after 1-year enrollment

613   Follow-up every 6 months (visit 8, visit 9, visit 10, visit 11, visit 9, and visit 11 require patients to

614   undergo face-to-face follow-up).

615   Visit by telephone:

616      Patient smoking cessation, weight, and exercise data are collected

617      Follow-up aspirin medication

618      AE, SAE and endpoint observation

619   Face-to-face visit:

620      Patient smoking cessation, weight, and exercise data are collected

621      mRS, MoCA, EQ-5D (MoCA is unnecessary)

622      Follow-up aspirin and atorvastatin tablet medication orders

623      AE, SAE and endpoint observation.

624

625   16. Management of (transient) ischemic events during follow-up

626   If any patient in each group has a potential clinical neurological event (transient cerebral ischemia,

627   ischemic stroke), the neurologist will determine whether to perform a vessel imaging examination,

628   including DSA. The most effective treatment for ICAS patients with transient cerebral ischemia or

629   ischemic stroke is unknown. The researchers will determine the best treatment according to the

630   patient's condition and actively control the risk factors.
                                                          35

```

### DOC-003 PDF page 36

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=36)

```text
      BASIS                                                                            Number:2017YFC1307900


631      If patients in the experimental group experience transient cerebral ischemia or ischemic stroke,

632   accompanied by restenosis ≥ 70 % diagnosed by DSA, investigators composed of neurologists and

633   neurointerventional experts will provide advice on whether the patient should undergo

634   revascularization or medical management alone. Revascularization is not recommended for patients

635   with restenosis < 70 %.

636

637   17. Assessment of endpoint and adverse events (AEs)

638   17.1 Endpoint event assessment

639   The endpoint events include target vessel haemorrhagic stroke, ischemic stroke, death, and target

640   vessel revascularization. If a patient has a potential primary endpoint event, the researcher must

641   report to a third-party monitoring company project team within 48 hours, including the patient's

642   complete medical records. The project team will submit the patient's data to the event arbitration

643   committee, and the event arbitration committee will complete the arbitration within 7 days. The

644   endpoint event arbitration committee is composed of three members. First, two members use

645   back-to-back arbitration. If the evaluation opinions are inconsistent, a third evaluation expert will

646   cast a decisive vote.

647   17.2 AEs assessment

648   An AE is the presence of any unexpected medical condition during or after being treated with

649   medical devices. It includes symptoms, signs, or abnormal laboratory parameters that can be

650   unrelated to treatment. An AE that fulfills at least one of the following criteria is classified as a

651   severe AE(SAE): AE that results in death; is life-threatening; requires/prolongs inpatient

652   hospitalization; results in serious disability; or requires medical intervention to prevent one of the

653   above-mentioned outcomes. If a potential endpoint occurs, the committee board meeting will be

654   convened to evaluate whether such an event can be categorized as the primary endpoint.
                                                        36

```

### DOC-003 PDF page 37

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=37)

```text
      BASIS                                                                               Number:2017YFC1307900


655   Unanticipated adverse device effect (UADE): Any serious adverse reaction affecting health or

656   safety, or any life-threatening event or death related to (caused by) the device. The nature, severity,

657   or degree of such serious adverse reactions, life-threatening events or deaths, or other unexpected

658   device-related serious events involving patient rights, safety, or welfare, were not previously

659   identified in the study plan.

660   The following events are considered as possible (expected) complications of balloon angioplasty:

      Vasospasm                       Neurological symptoms                Coagulation disorders

      Dissection                      Pseudoaneurysm                       Death

      Vessel occlusion                Renal insufficiency/failure           Embolism (air, tissue, thrombus or
                                                                            foreign body )
      Vessel perforation              Respiratory          distress/failure Pain, and/or puncture site infection
                                      hematoma
      Vessel rupture                   Seizure                             Hemorrhage

      Vessel embolism                 Infection                            Hypertension

      Stroke                          Drug reaction of antiplatelets       Hypotension


      Transient ischemic attack       Syncope

661   17.3 SAE record and report

662   The collection time of adverse events and serious adverse events in the study begins with signing

663   the informed consent, across the study period, until the end of the study. SAEs of patients who

664   discontinue treatment in advance will be recorded.

665   When any SAE occurs during the study, the researcher should immediately treat the patient, and

666   report in writing within 24 hours to the clinical trial institution, ethics committee, and sponsor

667   (Beijing Tiantan Hospital, Capital Medical University). For death events, clinical trial institutions

668   and researchers should provide the ethics committee and sponsors (Beijing Tiantan Hospital,

669   Capital Medical University) with all the required information.

670   17.4 Prediction of AEs and countermeasures
                                                           37

```

### DOC-003 PDF page 38

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=38)

```text
      BASIS                                                                              Number:2017YFC1307900


671   AEs that may occur during the procedures include, but are not limited to:

672   Thromboembolic events

673   The possible causes include no anticoagulation or insufficient anticoagulation, insufficient

674   antiplatelet aggregation treatment before and after the procedure or aspirin resistance.

675   Anticoagulation and antiplatelet aggregation should be reasonably standardized. If embolization

676   occurs in the important vessels, it should be handled by a professional doctor and assessed

677   according to the patient's condition.

678   Cerebral vasospasm

679   Cerebral vasospasm can be caused by subarachnoid hemorrhage (SAH), or by instrumentation with

680   endovascular catheters and guidewires. If vasospasm occurs, the professional doctor will give

681   symptomatic treatment per the patient's condition.

682   Acute vessel occlusion

683   Possible causes include intimal injury, platelet aggregation, thrombosis, etc., usually occurring

684   within 30 minutes after balloon angioplasty or may be related to intimal avulsion. Preventive

685   measures: including aspirin, ticlid or clopidogrel antiplatelet drugs can effectively reduce acute

686   thrombotic    events.   Under    strict   pre-procedure   antiplatelet   therapy   and   intraprocedure

687   anticoagulation, acute vessel occlusion events can be avoided.

688   Treatment measures: Once acute vessel occlusion occurs, reasonable treatment should be performed

689   immediately. Thrombolysis can be performed in patients with acute thrombosis.

690   Thrombosis

691   Thrombosis occurs mainly due to plaque fragmentation caused by squeezing the plaque during

692   balloon dilatation. Sometimes, thrombosis is caused by the catheter and guide wire. The use of brain

693   protection devices and intraprocedure anticoagulation are the basic measures to prevent this event.

694   Vessel rupture

                                                         38

```

### DOC-003 PDF page 39

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=39)

```text
      BASIS                                                                            Number:2017YFC1307900


695   A vessel rupture complication can directly lead to death. When balloon angioplasty is performed,

696   the selected balloon is preferably slightly smaller than the diameter of the target vessel. Once vessel

697   rupture occurs, symptomatic treatment should be performed immediately by a professional

698   physician.

699   Cerebral hyperperfusion syndrome

700   For severe stenotic lesions, the autoregulation ability of distal vessels decreases due to long-term

701   ischemia. The sudden expansion of the lesion site diameter may significantly increase the blood

702   flow. The distal vessels, especially the cortical arteries, cannot immediately adapt to this sudden

703   increase in blood flow and passively expand, resulting in cerebral hyperperfusion syndrome. The

704   clinical presentation includes headache, nausea, vomiting, seizure, and disturbance of consciousness.

705   Some patients can suffer intracranial hemorrhage. The possibility of this occurrence should be fully

706   recognized before the procedure, and blood pressure should be appropriately reduced during and

707   after the procedure to prevent this event. If postoperative cerebral hyperperfusion syndrome occurs,

708   symptomatic treatment should be performed according to the patient's condition (such as

709   antihypertensive medications, analgesics, antiepileptic drugs), agents to reduce intracranial pressure,

710   surgical treatment of cerebral hemorrhage, etc.

711

712   18. Core Laboratory

713   Imaging will be adjudicated by an independent imaging core lab (China National Clinical Research

714   Center for Neurological Diseases, Tiantan Neuroimaging Center of Excellence). All of the blood

715   samples and imaging data will be collected, transported, and preserved according to the study

716   protocol. Imaging will be blinded (clinical features and treatment options for patients), reviewed by

717   experienced MRI experts and DSA experts (over a 10-year working experience).

718
                                                        39

```

### DOC-003 PDF page 40

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=40)

```text
      BASIS                                                                            Number:2017YFC1307900



719   19. Quality control

720   To ensure that the collected data is concordant with the protocol, each sub-center of the BASIS trial

721   will be regularly scrutinized, and by comparing data in the Electronic Data Capture System (EDC)

722   and data in the original documents (case report form [CRF] vs. source documents) to confirm data

723   consistency. If a patient develops an AE/severe AE or completed a 1-year observation after

724   receiving treatment from non-study sites, duplicate copies of the medical documents will be

725   collected for future review.

726

727   20. Statistical Analysis

728   The composite event rates and corresponding 95% CIs of the primary outcome in the two treatment

729   groups will be estimated by Kaplan-Meier survival analysis and compared by log-rank test. A

730   hazard ratio between the two groups and its 95% CI will be calculated using a Cox proportional

731   hazards regression model. Time-to-event endpoints of the secondary outcomes will also be analyzed

732   using Kaplan-Meier survival analysis and Cox regression, and common odds ratios of mRS will be

733   estimated using ordinal logistic regression. The widths of the intervals will not be adjusted for

734   multiplicity for secondary outcomes. The main analysis of this study will be conducted based on the

735   intention-to-treat principle, and per protocol analysis and as treated analysis will also be conducted

736   as sensitivity analyses. All analyses will be performed using SAS software, Version 9.4 (SAS

737   Institute). Detailed statistical methods, missing data imputation and subgroup analyses are described

738   in the statistical analysis plan.

739   20.1 Sample size

740   The estimation of the sample size is calculated according to the 1-year results of the SAMMPRIS

741   trial, the incidence of target vessel stroke or death rate was 12.2% within 12 months after

                                                        40

```

### DOC-003 PDF page 41

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=41)

```text
      BASIS                                                                               Number:2017YFC1307900


742   enrollment in the experimental group.1 The sample size was 686 cases, with a 80% power,

743   two-sided α = 0.05, to detect a 50 % relative reduction (6.1%) after balloon angioplasty for

744   intracranial atherosclerosis. It is assumed that the O'Brien-Fleming spending function will lead to 6%

745   expansion of the total type I error. The SAS software is used to calculate the sample size required

746   for the mid-term analysis, which increases the sample size to the required 728 cases. Considering

747   the 10% lost to follow-up rate, the final sample size of this study is 802 cases.


748   20.2 Interim analysis


749   Interim analysis is performed when half of patients finished 12-months visit. The mid-term analysis

750   α1 is estimated to be 0.0015, and the final analysis α2 is 0.024.

751   20.3 Subgroup analysis

752   Subgroup analyses on the primary outcome will be performed in the following subgroups:

753      Age, <65 years old vs. ≥ 65 years old

754      Sex, men vs. women

755      Hypertension, yes vs. no

756      Diabetes, yes vs. no

757      Smoking, yes vs. no

758      Baseline renal function, eGFR <60 ml/min/1.73m2 vs. eGFR≥60 ml/min/1.73m2

759      Target vessel stenosis degree, <80%vs. ≥80%

760      BMI, <25 Kg/m2 vs. 25-30 Kg/m2vs. ≥30 Kg/m2

761      Hypoperfusion, yes vs. no

762      Lesion location, anterior circulation vs. posterior circulation

763      The mechanism, ischemic stroke vs. TIA

764

                                                         41

```

### DOC-003 PDF page 42

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=42)

```text
      BASIS                                                                               Number:2017YFC1307900



765   21. Data Safety and Monitoring Board

766   The data safety and monitoring board (DSMB) is comprised of academic members and an

767   independent statistician. The DSMB is scheduled to have meetings annually to review the study

768   progress to guarantee the trial is in accordance with the standards of ethics and ensure the safety of

769   all enrollled patients. After each DSMB meeting, the DSMB members will generate a report

770   including all recommendations, and hand it to the steering committee immediately after the

771   meeting.

772

773   22. Study organization

774   Twice a year, the steering committee will meet to oversee the trial and provide strategic guidance.

775   Periodically, the clinical research team of the leading center will meet online with the project team

776   of the clinical research organization to review the trial progress and data monitoring each week. An

777   independent clinical events adjudication committee (CEC) will ensure that defined outcomes are

778   reported and judged uniformly using the same definition by experts who are blinded to the

779   treatment status. (Table 1)

780

781   Table 1. Collaboration team of trial and Study Committee

          Collaboration                   Unit or Hospital name                     Investigator Name
          team
          Sponsor         Beijing Tian Tan Hospital, Capital Medical University     NA
          CRO             Beijing Jingchengtong Medicine Technology Co., Ltd.       NA
          Statistical     Department of Biostatistics, Peking University Clinical   NA
          analysis        Research Institute
          Imaging core    China National Clinical Research Center for               Jing Jing
          lab             Neurological Diseases, Tiantan Neuroimaging Center of
                          Excellence
                          China National Clinical Research Center for               Nan Qi
                          Neurological Diseases, Tiantan Neuroimaging Center of
                          Excellence

                                                         42

```

### DOC-003 PDF page 43

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=43)

```text
BASIS                                                                             Number:2017YFC1307900


    Collaboration                 Unit or Hospital name                     Investigator Name
    team
    CEC team      Tangdu Hospital of Air Force Medical University           Zhenwei Zhao
                   Beijing Tian Tan Hospital, Capital Medical University    Kehui Dong
                   The First Affiliated Hospital of Harbin Medical          Huaizhang Shi
                   University
    DSMB           People's Liberation Army Air Force General Hospital      Jin Shi
                   Strategic Support Force Specialty Medical Center         Yiling Cai
                   China National Clinical Research Center for              Yuesong Pan
                   Neurological Diseases
    AE             Beijing Tian Tan Hospital, Capital Medical University    Xuan Sun
    Committee      Beijing Tian Tan Hospital, Capital Medical University    Yiming Deng
                   Beijing Tian Tan Hospital, Capital Medical University    Ning Ma
    Steering       Beijing Tian Tan Hospital, Capital Medical University    Zhongrong Miao
    Committee
                   Beijing Tian Tan Hospital, Capital Medical University    Yilong Wang
                   Beijing Tian Tan Hospital, Capital Medical University    Yongjun Wang
                   Comprehensive Stroke Center, University of California,   Wengui Yu
                   Irvine, USA
                   Beijing Tian Tan Hospital, Capital Medical University    Xingquan Zhao
                   Neurovascular Imaging Research Core and Department       David S Liebeskind
                   of Neurology, University of California, USA
                   Department of Neurosurgery, University Hospitals         Sepideh Amin-Hanjani
                   Cleveland Medical Center/ Case Western Reserve
                   Univeristy School of Medicine, Ohio, USA
    Cooperation    Unit or Hospital name                                    Investigator Name
    team
    Sponsor        Beijing Tian Tan Hospital, Capital Medical University    NA
    CRO            Beijing Jingchengtong Medicine Technology Co., Ltd.      NA
    Statistical    Medical Statistics Office, Peking University First       NA
    analysis       Hospital, Beijing, China
    Imaging core   China National Clinical Research Center for              Jing Jing
    lab            Neurological Diseases, Tiantan Neuroimaging Center of    Nan Qi
                   Excellence
    CEC team       Tangdu Hospital of Air Force Medical University          Zhenwei Zhao
                   Beijing Tian Tan Hospital, Capital Medical University    Kehui Dong
                   The First Affiliated Hospital of Harbin Medical          Huaizhang Shi
                   University
    DSMB           People's Liberation Army Air Force General Hospital      Jin Shi
                   Strategic Support Force Specialty Medical Center         Yiling Cai
                   Beijing Tian Tan Hospital, Capital Medical University    Yuesong Pan
    AE             Beijing Tian Tan Hospital, Capital Medical University    Xuan Sun
    Committee      Beijing Tian Tan Hospital, Capital Medical University    Yiming Deng
                   Beijing Tian Tan Hospital, Capital Medical University    Ning Ma
    Technology     Strategic Support Force Specialty Medical Center         Yiling Cai
    Steering       Xuanwu Hospital Capital Medical University               Yabing Wang
    Committee      Aerospace Central Hospital                               Peifu Wang
                   Beijing Chaoyang Emergency Rescue Hospital of            Qiang Zhang
                                                  43

```

### DOC-003 PDF page 44

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=44)

```text
      BASIS                                                                             Number:2017YFC1307900


           Collaboration                  Unit or Hospital name                   Investigator Name
           team
                        Integrated Traditional Chinese and Western Medicine
                        The Sixth Medical Center of the General Hospital of the   Feng Qiu
                        People's Liberation Army
           Chairs    of Beijing Tian Tan Hospital, Capital Medical University     Zhongrong Miao
           Steering     Beijing Tian Tan Hospital, Capital Medical University     Yilong Wang
           Committee    Comprehensive Stroke Center, University of California,    Wengui Yu
                        Irvine, USA
782
783   23. Research drug supply and responsibilities division
784
785   Clopidogrel will be provided to the patients for free during the screening period of 3-5 days and the

786   enrollment period of 90 days. Whether to continue taking clopidogrel after 90 days will be assessed

787   according to the patient's condition. The patient will need to purchase clopidogrel after 90 days.

788       Atorvastatin tablets are also free for 1 year. Whether to continue taking atorvastatin tablets after

789   1 year will be assessed according to the patient's condition. Patients will need to buy atorvastatin

790   after 1 year.

791       Drugs used in BASIS will be stored in a safe place by researchers or other authorized personnel

792   and stored in accordance with the conditions required (the drug instructions).

793        Researchers, hospital pharmacists or other persons are permitted to store and distribute the

794   research drugs, and are responsible for ensuring that the drugs used in clinical trials are safely

795   maintained in accordance with the requirements of the (research) organizers and meet the

796   corresponding regulatory requirements.

797       All drugs used in clinical studies should be distributed according to the researcher's prescription,

798   and the researcher should ensure that the drugs used for research distribution and recovery are

799   accurately recorded.

800       Any quality problems related to research drugs (labels, failure dates, etc.) encountered in the

801   reception or use should be reported to the organizer in time, and the organizer should initiate a

802   complaint procedure.
                                                         44

```

### DOC-003 PDF page 45

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=45)

```text
      BASIS                                                                            Number:2017YFC1307900


803          Under no circumstances will researchers provide research results to third parties, allow the

804   research results to be used under non-clinical research protocols, or transfer the research results in

805   any other way.

806

807   24. Research Device Processing Mechanism, Characteristics, and

808   Responsibilities Division

809   Balloon devices provided by SINOMED will be used in accordance with high-quality clinical

810   practice guidelines and medical device tracking guidelines. An introduction to the balloon device

811   contains the following information:

812          Device name: Neuro RX intracranial balloon catheter

813          Research and development unit: Sino Medical Science and Technology Co., Ltd.

814          Registration number: CFDA, 20163772491 (China, Equipment, Registration, Approval,

815   2016-12-19)

816          Composition: Neuro RX intracranial balloon catheter is an expandable balloon with a rapid

817   exchange system that can be used to treat ICAS. Its working length is 145 cm, with a guide wire of

818   less than 0.014’ and a catheter with an inner diameter of ≥ 5F ( 0.056’). Two opaque markers on the

819   catheter shaft indicate the working length of the balloon. The guide wire exit is 24 cm from the far

820   tip.

821          Device parameters (length and diameter)




822



                                                        45

```

### DOC-003 PDF page 46

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=46)

```text
      BASIS                                                                          Number:2017YFC1307900




823

824   Recommend: The Neuro RX intracranial balloon catheter is suitable for ICAS lesion, and balloon

825   dilatation for improving intracranial perfusion.

826      Device name: Neuro LPS intracranial balloon dilatation catheter

827      Research and development unit: Sino Medical Science and Technology Co., Ltd.

828      Registration number: NMPA, 20203030576 (China, Equipment, Registration,

829   Approval, 2020-06-19)

830     Composition:

831     Neuro LPS intracranial balloon dilatation catheter is composed of medical polypropylene,

832   polytetrafluoroethylene, polyether amide block copolymer, polycarbonate, polyolefin, stainless steel,

833   and platinum alloy.

834




                                                         46

```

### DOC-003 PDF page 47

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=47)

```text
      BASIS                                                                                       Number:2017YFC1307900




835

836   1) TIP head (polyether amide block copolymer)

837   2) Balloon protective sheath (polytetrafluoroethylene)

838   3) Balloon (polyetheramide block copolymer)

839   4) Balloon inner tube (polyetheramide block copolymer)

840   5) Marker (two Markers are respectively set on the balloon's inner tube (4), the outer edge of the

841   two Markers is flush with the neck of the balloon, and the material is 90% platinum and 10%

842   iridium alloy)

843   6) Balloon outer tube (polyetheramide block copolymer)

844   7) Metal conduit (304 stainless steel)

845   8) Sheath (two layers, inner layer of 304 stainless steel, outer layer of polyolefin)

846   9) Joint (polycarbonate)

847   Note 1: D1 represents the diameter of the balloon after expansion.

848   Note 2: L2 represents the effective length of the balloon on the balloon catheter.

849   Note 3: L represents the effective length of the balloon catheter.

850   Note 4: A complete balloon dilatation catheter is inserted into a high-density polyethylene ring protective sleeve.

851   Device parameters (length and diameter)




                                                                47

```

### DOC-003 PDF page 48

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=48)

```text
      BASIS                                                                            Number:2017YFC1307900




852

853   Description: The Neuro RX or Neuro LPS intracranial balloon dilatation catheter is provided by

854   SINOMED. Intracranial balloon catheter equipment is not provided free of charge.

855   Responsibilities Division

856   Investigators and/or other designated persons/institutions should archive and save the delivery

857   records of the products to the research center, including the inventory of the research center, the use

858   of each item, and the unused products that will be returned to the sponsor. In the event of damage,

859   loss, or additional (unscheduled) material, the organizer or relevant party shall be notified. These

860   records should include the date, quantity, product serial number, shelf life (if any), and a unique

861   code number assigned to the device and the research object.

862

863   25. Control requirements

864   BASIS will be carried out in accordance with the relevant provisions of the China Food and Drug

865   Administration (NMPA): 'medical device clinical trial quality management norms' and 'drug clinical

866   trial quality management norms'.
                                                        48

```

### DOC-003 PDF page 49

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=49)

```text
      BASIS                                                                            Number:2017YFC1307900



867   26. Institutional Review Board (IRB)/Ethics Committee (IEC)

868   Researchers or organizers must submit a clinical research protocol to the Ethics Committee of

869   Beijing Tiantan Hospital and obtain a written certificate signed by the Ethics Committee with clear

870   approval time and approval opinions.

871      The following information should be clearly marked on the written certificate of approval:

872   clinical trial information (study number, name, and version number of clinical study protocol),

873   review documents (study protocol, informed consent, etc.).

874     The clinical research will be initiated only after the research sponsor has received written

875   evidence of a clear approval time and approval opinion.

876     During the clinical research, any revision or modification of the clinical study protocol, any event

877   that may affect patient safety or the continuation of clinical research, especially any safety changes,

878   and any updates to the Investigator's Manual should be reported to the Ethics Committee.

879      If necessary, a progress report is provided to the ethics committee each year, and the clinical

880   research results are summarized at the end of the clinical study.

881

882


883


884


885


886


887



                                                        49

```

### DOC-003 PDF page 50

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=50)

```text
      BASIS                                                                                           Number:2017YFC1307900



888   Reference
889   1.      Gutierrez J, Turan TN, Hoh BL, Chimowitz MI. Intracranial atherosclerotic stenosis: risk factors, diagnosis,
890           and treatment. Lancet Neurol. 2022;21:355-368. doi: 10.1016/s1474-4422(21)00376-8
891   2.      Kasner SE, Chimowitz MI, Lynn MJ, Howlett-Smith H, Stern BJ, Hertzberg VS, Frankel MR, Levine SR,
892           Chaturvedi S, Benesch CG, et al. Predictors of ischemic stroke in the territory of a symptomatic intracranial
893           arterial stenosis. Circulation. 2006;113:555-563. doi: 10.1161/circulationaha.105.578229
894   3.      Zaidat OO, Klucznik R, Alexander MJ, Chaloupka J, Lutsep H, Barnwell S, Mawad M, Lane B, Lynn MJ,
895           Chimowitz M. The NIH registry on use of the Wingspan stent for symptomatic 70-99% intracranial arterial
896           stenosis. Neurology. 2008;70:1518-1524. doi: 10.1212/01.wnl.0000306308.08229.a3
897   4.      Zaidat OO, Fitzsimmons BF, Woodward BK, Wang Z, Killer-Oberpfalzer M, Wakhloo A, Gupta R, Kirshner
898           H, Megerian JT, Lesko J, et al. Effect of a balloon-expandable intracranial stent vs medical therapy on risk of
899           stroke in patients with symptomatic intracranial stenosis: the VISSIT randomized clinical trial. Jama.
900           2015;313:1240-1248. doi: 10.1001/jama.2015.1693
901   5.      Chimowitz MI, Lynn MJ, Derdeyn CP, Turan TN, Fiorella D, Lane BF, Janis LS, Lutsep HL, Barnwell SL,
902           Waters MF, et al. Stenting versus aggressive medical therapy for intracranial arterial stenosis. N Engl J Med.
903           2011;365:993-1003. doi: 10.1056/NEJMoa1105335
904   6.      Gao P, Wang T, Wang D, Liebeskind DS, Shi H, Li T, Zhao Z, Cai Y, Wu W, He W, et al. Effect of Stenting
905           Plus Medical Therapy vs Medical Therapy Alone on Risk of Stroke and Death in Patients With Symptomatic
906           Intracranial Stenosis: The CASSISS Randomized Clinical Trial. Jama. 2022;328:534-542. doi:
907           10.1001/jama.2022.12000
908   7.      Wang T, Yang K, Zhang X, Luo J, Xu R, Wang X, Yang Y, Bai X, Ma Y, Yan Y, et al. Endovascular Therapy
909           for Symptomatic Intracranial Artery Stenosis: a Systematic Review and Network Meta-analysis. Transl Stroke
910           Res. 2022;13:676-685. doi: 10.1007/s12975-022-00996-8
911   8.      Seyedsaadat SM, Yolcu YU, Neuhaus A, Rizvi A, Alzuabi M, Murad MH, Brinjikji W, Bydon M, Kallmes DF.
912           Submaximal angioplasty in the treatment of patients with symptomatic ICAD: a systematic review and
913           meta-analysis. J Neurointerv Surg. 2020;12:380-385. doi: 10.1136/neurintsurg-2019-015451
914   9.      Stapleton CJ, Chen YF, Shallwani H, Vakharia K, Turan TN, Woo HH, Derdeyn CP, Charbel FT, Siddiqui AH,
915           Amin-Hanjani S. Submaximal Angioplasty for Symptomatic Intracranial Atherosclerotic Disease: A
916           Meta-Analysis of Peri-Procedural and Long-Term Risk. Neurosurgery. 2020;86:755-762. doi:
917           10.1093/neuros/nyz337
918   10.     Peng G, Li K, Wang A, Tian X, Qi Z, Li S, Tong X, Deng Y, Sun X, Miao Z. Medical and Endovascular
919           Treatments for Intracranial Atherosclerotic Stenosis: A Network Meta-Analysis. Transl Stroke Res. 2021. doi:
920           10.1007/s12975-021-00957-7
921   11.     Chimowitz MI, Lynn MJ, Howlett-Smith H, Stern BJ, Hertzberg VS, Frankel MR, Levine SR, Chaturvedi S,
922           Kasner SE, Benesch CG, et al. Comparison of warfarin and aspirin for symptomatic intracranial arterial
923           stenosis. N Engl J Med. 2005;352:1305-1316. doi: 10.1056/NEJMoa043033
924   12.     Higashida RT, Furlan AJ, Roberts H, Tomsick T, Connors B, Barr J, Dillon W, Warach S, Broderick J, Tilley
925           B, et al. Trial design and reporting standards for intra-arterial cerebral thrombolysis for acute ischemic stroke.
926           Stroke. 2003;34:e109-137. doi: 10.1161/01.Str.0000082721.62796.09
927   13.     Zaidat OO, Yoo AJ, Khatri P, Tomsick TA, von Kummer R, Saver JL, Marks MP, Prabhakaran S, Kallmes DF,
928           Fitzsimmons BF, et al. Recommendations on angiographic revascularization grading standards for acute
929           ischemic stroke: a consensus statement. Stroke. 2013;44:2650-2663. doi: 10.1161/strokeaha.113.001972
930   14.     Wang Y, Han S, Qin H, Zheng H, Jiang B, Cao Y, Gao Y, Guan L, Jia Q, Jiang Y, et al. Chinese Stroke
931           Association guidelines for clinical management of cerebrovascular disorders: executive summary and 2019
932           update of the management of high-risk population. Stroke Vasc Neurol. 2020;5:270-278. doi:
933           10.1136/svn-2020-000385
934
935
936
937
938
939

                                                                 50

```

### DOC-003 PDF page 51

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=51)

```text
      BASIS                                                                           Number:2017YFC1307900



940
941   Appendix
942   Appendix Table 1. ASITN/SIR collateral circulation scale

943

              Grade 0                   No collaterals visible to the ischemic site


              Grade 1                   Slow collaterals to the periphery of the ischemic site with
                                        persistence of some of the defect
              Grade 2                   Rapid collaterals to the periphery of ischemic site with
                                        persistence of some of the defect and to only a portion of
                                        the ischemic territory
              Grade 3                   Collaterals with slow but complete angiographic blood
                                        flow of the ischemic bed by the late venous phase
              Grade 4                   Complete and rapid collateral blood flow to the vascular
                                        bed in the entire ischemic territory by retrograde
                                        perfusion

944

945
946
947
948
949
950
951
952
953
954
955
956
957
958
959
960
961

962
                                                       51

```

### DOC-003 PDF page 52

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=52)

```text
      BASIS                                                                                      Number:2017YFC1307900


963   Appendix Table 2. modified Rankin Scale

964   The modified Rankin Scale (mRS) is an ordinal hierarchical scale ranging from 0 to 5, with higher scores
965   indicating more severe disability. A score of 6 has been added to signify death.
              Category Short description           Long description
              0           No symptoms              No symptoms
                          Symptoms,           no
              1                                    Minor symptoms that do not interfere with lifestyle
                          disability
                                                   Slight disability, symptoms that lead to some restriction in
              2           Slight disability        lifestyle, but do not interfere with the patient's capacity to
                                                   look after himself.
                                                   Moderate disability, symptoms that significantly restrict
              3           Moderate disability
                                                   lifestyle and prevent totally independent existence
                                                   Moderately severe disability, symptoms that clearly
                          Moderately severe
              4                                    prevent independent existence though not needing constant
                          disability
                                                   attention
                                                   Severe disability, totally dependent patient requiring
              5           Severe disability
                                                   constant attention day and night.
              6           Death                    Death
966


967


968


969


970

971
972

973


974




                                                               52

```

### DOC-003 PDF page 53

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=53)

```text
      BASIS                                                                           Number:2017YFC1307900


975   Appendix Table 3. National Institute of Health Stroke Scale (NIHSS)

976       The NIHSS is an ordinal hierarchical scale to evaluate the severity of stroke by assessing a
977   patient’s performance. Scores range from 0 to 42, with higher scores indicating a more severe
978   deficit. Administer stroke scale items in the order listed. Record performance in each category after
979   each subscale exam. Do not go back and change scores. Follow directions provided for each exam
980   technique. Scores should reflect what the patient does, not what the clinician thinks the patient can
981   do. The clinician should record answers while administering the exam and work quickly. Except
982   where indicated, the patient should not be coached (i.e. repeated requests to patient to make a
983   special effort).

           Instructions                                                Scale definition
                                                                       0 = Alert; keenly responsive.
                                                                       1 = Not alert; but arousable by minor
           1a. Level of consciousness. The investigator must           stimulation to obey, answer, or respond.
           choose a response if a full evaluation is prevented by      2 = Not alert; required repeated
           such obstacles as an endotracheal tube, language barrier,   stimulation to attend, or is obtunded and
           orotracheal trauma/bandages. A 3 is scored only if the      requires strong or painful stimulation to
           patient makes no movement (other than reflexive             make movements (not stereotyped).
           posturing) in response to noxious stimulation.              3 = Responds only with reflex motor or
                                                                       autonomic        effects     or    totally
                                                                       unresponsive, flaccid and areflexic.
           1b. LOC Questions: The patient is asked the month and
           his/her age. The answer must be correct – there is not
           partial credit for being close. Phasic and stuporous
           patients who do not comprehend the questions will score
                                                                       0 = Answers both questions correctly.
           2. Patients unable to speak because of endotracheal
                                                                       1 = Answers one question correctly.
           intubation, orotracheal trauma, severe dysarthria from
                                                                       2 = Answers neither question correctly.
           any cause, language barrier, or any other problem not
           secondary to aphasia are given a 1. It is important that
           only the initial answer be graded and that the examiners
           not “help” the patient with verbal or non-verbal clues.
           1c. LOC Commands: The patient is asked to open and
           close the eyes and then to grip and release the
           non-paretic hand. Substitute another one step command
           if the hand cannot be used. Credit is given if an
           unequivocal attempt is made but not completed due to        0 = Performs both tasks correctly.
           weakness. If the patient does not respond to command,       1 = Performs one task correctly.
           the task should be demonstrated to him or her               2 = Performs neither task correctly.
           (pantomime), and the result scored (i.e. follows none,
           one or two commands). Patients with trauma,
           amputation, or other physical impediments should be
           given suitable one-step commands. Only the first
                                                       53

```

### DOC-003 PDF page 54

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=54)

```text
BASIS                                                                           Number:2017YFC1307900


    attempt is scored.
    2. Best Gaze: Only horizontal eye movements will be
    tested. Voluntary or reflexive (oculocephalic) eye
    movements will be scored, but caloric testing is not
    done. If the patient has a conjugate deviation of the eyes
                                                                 0= Normal.
    that can be overcome by voluntary or reflexive activity,
                                                                 1= Partial gaze palsy; gaze is abnormal
    the score will be a 1. If a patient has an isolated
                                                                 in one or both eyes, but forced deviation
    peripheral nerve paresis (CN III, IV or VI), score a 1.
                                                                 or total gaze paresis is not present.
    Gaze is testable in all aphasic patients. Patients with
                                                                 2= Forced deviation; or total gaze paresis
    ocular trauma, bandages, preexisting blindness, or other
                                                                 not overcome by the oculocephalic
    disorder of visual acuity or fields should be tested with
                                                                 maneuver.
    reflexive movements, and a choice made by the
    investigator. Establishing eye contact and then moving
    about the patient from side to side will occasionally
    clarify the presence of a partial gaze palsy.
    3. Visual: Visual fields (upper and lower quadrants) are
    tested by confrontation, using finger counting or visual
    threat, as appropriate. Patients may be encouraged, but
    if they look at the side of the moving finger
    appropriately, this can be scored as normal. If there is     0= No visual loss.
    unilateral blindness or enucleation, visual fields in the    1= Partial hemianopia.
    remaining eye are scored. Score 1 only if a clear-cut        2= Complete hemianopia.
    asymmetry, including quadrantanopia, is found. If            3= Bilateral hemianopia (blind including
    patient is blind from any cause, score 3.                    cortical blindness)
    Double simultaneous stimulation is performed in this
    case.
    If there is extinction, the patient receives a 1, and the
    results are used to respond to item 11.
                                                                 0 = Normal symmetrical movements.
    4. Facial palsy: Ask or use pantomime to encourage the
                                                                 1= Minor paralysis (flattened nasolabial
    patient to show teeth or raise eyebrows and close eyes.
                                                                 fold, asymmetry on smiling)
    Score symmetry of grimace in response to noxious
                                                                 2= Partial paralysis (total or near-total
    stimuli in the poorly response or non-comprehending
                                                                 paralysis of lower face)
    patient. If facial trauma/bandages, orotracheal tube, tape
                                                                 3= Complete paralysis of one or both
    or other physical barriers obscure the face, these should
                                                                 sides (absence of facial movement in the
    be removed to the extent possible.
                                                                 upper and lower face).
                                                                 0= No drift; limb holds 90 (or 45)
    5. Motor arm: The limb is placed in the appropriate
                                                                 degrees for full 10 seconds.
    position: extend the arms (palms down) 90 degrees (if
                                                                 1= Drift; limb holds 90 (or 45) degrees,
    sitting) or 45 degrees (if supine). Drift is scored if the
                                                                 but drifts down before full 10 seconds;
    arm falls before 10 seconds. The aphasic patient is
                                                                 does not hit bed or other support.
    encouraged using urgency in the voice and pantomime,
                                                                 2= Some effort against gravity; limb
    but not noxious stimulation. Each limb is tested in turn,
                                                                 cannot get to or maintain (if cued) 90 (or
    beginning with the non-paretic arm. Only in the case of
                                                                 45) degrees, drifts down to bed, but has
    amputation or joint fusion at the shoulder, the examiner
                                                                 some effort against gravity.
    should record the score as untestable (UN), and clearly
                                                                 3= No effort against gravity; limb falls.
    write the explanation for this choice.
                                                                 4= No movement.
                                                 54

```

### DOC-003 PDF page 55

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=55)

```text
BASIS                                                                            Number:2017YFC1307900


                                                                 UN = Amputation or joint fusion:
                                                                 explain:
                                                                 5a = Left Arm.
                                                                 5b = Right arm.
                                                                 0= No drift; leg holds 30-degree position
                                                                 for full 5 seconds.
    6. Motor leg: The limb is placed in the appropriate          1= Drift; leg falls by the end of the
    position:                                                    5-second period but does not hit bed.
    hold the leg at 30 degrees (always tested supine). Drift     2= Some effort against gravity; leg falls
    is scored if the leg falls before 5 seconds. The aphasic     to bed by 5 seconds, but has some effort
    patient is encouraged using urgency in the voice and         against gravity.
    pantomime, but not noxious stimulation. Each limb is         3= No effort against gravity; leg falls to
    tested in turn, beginning with the non-paretic leg. Only     bed immediately.
    in the case of amputation or joint fusion at the hip, the    4= No movement.
    examiner should record the score as untestable (UN),         UN = Amputation or joint fusion:
    and clearly write the explanation for this choice.           explain:
                                                                 6a. Left Leg
                                                                 6b. Right Leg.
    7. Limb ataxia: This item is aimed at finding evidence
    of a unilateral cerebellar lesion. Test with eyes open. In
    case of visual defect, ensure testing is done in intact
    visual field. The finger-nose-finger and heel-shin tests
                                                                 0= Absent.
    are performed on both sides, and ataxia is scored only if
                                                                 1= Present in one limb.
    present out of proportion to weakness. Ataxia is absent
                                                                 2= Present in two limbs.
    in the patient who cannot understand or is paralyzed.
                                                                 UN = Amputation or joint fusion:
    Only in the case of amputation or joint fusion, the
                                                                 explain:
    examiner should record the score as untestable (UN),
    and clearly write the explanation for this choice. In case
    of blindness, test by having the patient touch nose from
    extended arm position.
    8. Sensory: Sensation or grimace to pinprick when
    tested, or withdrawal from noxious stimulus in the
    obtunded or aphasic patient. Only sensory loss attributed
    to stroke is scored as abnormal and the examiner should      0= Normal; no sensory loss.
    test as many body areas (arms [not hands], legs, trunk,      1= Mild-to-moderate sensory loss;
    face) as needed to accurately check for hemisensory          patients feels pinprick is less sharp or is
    loss. A score of 2, 'severe or total sensory loss', should   dull on the affected side; or there is a
    only be given when a severe or total loss of sensation       loss of superficial pain with pinprick, but
    can be clearly demonstrated. Stuporous and aphasic           patient is aware of being touched.
    patients will, therefore, probably score 1 or 0. The         2= Severe to total sensory loss; patient is
    patient with brainstem stroke who has bilateral loss of      not aware of being touched in the face,
    sensation is scored 2. If the patient does not respond and   arm and leg.
    is quadriplegic, score 2.
    Patients in a coma (item 1a=3) are automatically given a
    2 on this item.
    9. Best language: A great deal of information about          0= No aphasia; normal
    comprehension will be obtained during the preceding          1= Mild-to-moderate       aphasia;   some
                                                 55

```

### DOC-003 PDF page 56

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=56)

```text
      BASIS                                                                             Number:2017YFC1307900


984       sections of the examination. For this scale item, the          obvious loss of fluency or facility of
          patient is asked to describe what is happening in the          comprehension, without significant
          attached picture, to name the items on the attached            limitation on ideas expressed or form of
          naming sheet and to read from the attached list of             expression. Reduction of speech and/or
          sentences. Comprehension is judged from responses              comprehension, however, makes
          here, as well as to all of the commands in the preceding       conservation about provided materials
          general neurological exam. If visual loss interferes with      difficult or impossible. For example, in
          the tests, ask the patient to identify objects placed in the   conversation about provided materials,
          hand, repeat, and produce speech. The intubated patient        examiner can identify picture or naming
          should be asked to write. The patient in a coma (item          card content from patient's response.
          1a=3) will automatically score 3 on this item. The             2= Severe aphasia; all communication is
          examiner must choose a score for the patient with stupor       through fragmentary expression; great
          or limited cooperation, but a score of 3 should be used        need for inference, questioning, and
          only if the patient is mute and follows no one-step            guessing by the listener. Range of
          commands.                                                      information that can be exchanged is
                                                                         limited; listener carries burden of
                                                                         communication.       Examiner      cannot
                                                                         identify materials provided from patient
                                                                         response.
                                                                         3 = Mute, global aphasia: no usable
                                                                         speech or auditory comprehension.
          10. Dysarthria: If patient is thought to be normal, an
                                                                         0= Normal.
          adequate sample of speech must be obtained by asking
                                                                         1= Mild-to-moderate dysarthria; patient
          patient to read or repeat words from the attached list. If
                                                                         slurs at least some words and, at worst,
          the patient has severe aphasia, the clarity of articulation
                                                                         can be understood by some difficulty.
          of spontaneous speech can be rated. Only if patient is
                                                                         2= Severe dysarthria: patient's speech is
          intubated or has other physical barriers to producing
                                                                         so slurred as to be unintelligible in the
          speech, the examiner should record the score as
                                                                         absence of or out of proportion to any
          untestable (UN), and clearly write an explanation for
                                                                         dysphasia, or is mute/anarthric.
          this choice. Do not tell the patient why he or she is
                                                                         UN = Intubated or other physical barrier.
          being tested.
          11. Extinction and Inattention (formerly Neglect):
                                                                         0= No abnormality.
          Sufficient information to identify neglect may be
                                                                         1= Visual, tactile, auditory, spatial, or
          obtained during the prior testing. If the patient has a
                                                                         personal inattention or extinction to
          severe visual loss preventing visual double simultaneous
                                                                         bilateral
          stimulation, and the cutaneous stimuli are normal, the
                                                                         simultaneous stimulation in one of the
          score is normal. If the patient has aphasia but does
                                                                         sensory modalities.
          appear to attend to both sides, the score is normal. The
                                                                         2= Profound hemi-inattention or
          presence of visual spatial neglect or anosagnosia may
                                                                         extinction to more than one modality;
          also be taken as evidence of abnormality. Since the
                                                                         does not recognize own hand or orients
          abnormality is scored only if present, the item is never
                                                                         to only one side of space.
          untestable.




                                                        56

```

### DOC-003 PDF page 57

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=57)

```text
      BASIS                                                                          Number:2017YFC1307900


985   Appendix Table 4. EuroQoL 5D-5L
986   Under each heading, please tick the ONE box that best describes your health TODAY.
987   Mobility
      I have no problems in walking about
      I have slight problems in walking about
      I have moderate problems in walking about
      I have severe problems in walking about
      I am unable to walk about
      Self-care
      I have no problems washing or dressing myself
      I have slight problems washing or dressing myself
      I have moderate problems washing or dressing myself
      I have severe problems washing or dressing myself
      I am unable to wash or dress myself
      Usual activities (e.g. work, study, housework, family or leisure activities)
      I have no problems doing my usual activities
      I have slight problems doing my usual activities
      I have moderate problems doing my usual activities
      I have severe problems doing my usual activities
      I am unable to do my usual activities
      Pain/discomfort
      I have no pain or discomfort
      I have slight pain or discomfort
      I have moderate pain or discomfort
      I have severe pain or discomfort
      I have extreme pain or discomfort
      Anxiety/depression
      I am not anxious or depressed
      I am slightly anxious or depressed
      I am moderately anxious or depressed
      I am severely anxious or depressed
      I am extremely anxious or depressed
988




                                                         57

```

### DOC-003 PDF page 58

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=58)

```text
      BASIS                                                    Number:2017YFC1307900


         We would like to know how good or bad your
          health is TOADY.
         This scale is numbered from 0 to 100.
         100 means the best health you can imagine.
          0 means the worst health you can imagine.
         Mark an X on the scale to indicate how your health
          is TODAY.
         Now, please write the number you marked on the
          scale in the box below.




      YOUR HEALEH TOADY =
989




                                                     58

```

### DOC-003 PDF page 59

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=59)

```text
       BASIS                                                                         Number:2017YFC1307900


 990   Appendix Table 5. mTICI grade
 991
        mTICI grade     Definitions

        0 grade         No perfusion

        1 grade         Antegrade reperfusion past the initial occlusion, but limited distal branch

                        filling with little or slow distal reperfusion

        2a grade        Antegrade reperfusion of less than half of the occluded target artery previously

                        ischemic territory (eg, in 1 major division of the MCA and its territory)

        2b grade        Antegrade reperfusion of more than half of the previously occluded target

                        artery ischemic territory (eg, in 2 major divisions of the MCA and their

                        territories)

        3 grade         Complete antegrade reperfusion of the previously occluded target artery

                        ischemic territory, with absence of visualized occlusion in all distal branches

 992
 993
 994
 995
 996
 997
 998
 999
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
                                                       59

```

### DOC-003 PDF page 60

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=60)

```text
       BASIS                                                                       Number:2017YFC1307900



1015           Balloon Angioplasty vs. Aggressive Medical Management for

1016    Symptomatic Intracranial Artery Stenosis: The BASIS Randomized

1017                                          Clinical Trial

1018                                             (BASIS)

1019




1020

1021



1022                                         Protocol
1023

1024   Research team: Beijing Tiantan Hospital, Capital Medical University, Beijing, China

1025   Principal Investigator: Zhongrong Miao, MD, Professor of Neurology

1026   Co-Principal Investigator: Yilong Wang, MD, Professor of Neurology

1027   Protocol Version 2.3

1028   Date: March 28, 2022

1029

1030



                                                      60

```

### DOC-003 PDF page 61

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=61)

```text
       BASIS                                                                                                                                   Number:2017YFC1307900



1031                                                                             Contents
1032   Protocol Signature Page ...........................................................................................................................................63

1033   1.BASIS Protocol Synopsis ......................................................................................................................................64

1034   2.Abbreviations ........................................................................................................................................................70

1035   3.Schedule of assessments ........................................................................................................................................73

1036   4.Background............................................................................................................................................................75

1037   5.Objectives and Hypothesis ....................................................................................................................................76

1038      5.1 Objectvices .....................................................................................................................................................76

1039      5.2 Hypothesis ......................................................................................................................................................76

1040   6.Study Design .........................................................................................................................................................76

1041   7.Study Endpoint ......................................................................................................................................................78

1042      7.1 Primary endpoint ............................................................................................................................................78
1043      7.2 Secondary endpoints.......................................................................................................................................79

1044   8. Inclusion and Exclusion Criteria ..........................................................................................................................80

1045      8.1 Inclusion criteria .............................................................................................................................................81
1046      8.2 Exclusion criteria............................................................................................................................................81

1047   9. Informed Consent .................................................................................................................................................84

1048   10. Randomization ....................................................................................................................................................84

1049   11. DSA evaulation and lesion evaualtion ................................................................................................................85

1050   12. Balloon Angioplasty ...........................................................................................................................................85

1051   13. Aggressive medical management .......................................................................................................................87

1052      13.1 Antiplatelet treatment ...................................................................................................................................87
1053      13.2 Risk factor management ...............................................................................................................................88

1054   14. Patient and Researcher Benefit ...........................................................................................................................91

1055   15. Follow-up ...........................................................................................................................................................91

1056   16. Management of (transient) ischemic events during follow-up ...........................................................................97

1057   17. Assessment of endpoint and adverse events (AEs) ............................................................................................97

1058      17.1 Endpoint events assessment .........................................................................................................................97
                                                                                          61

```

### DOC-003 PDF page 62

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=62)

```text
       BASIS                                                                                                                                    Number:2017YFC1307900


1059      17.2 AEs assessment ............................................................................................................................................98
1060      17.3 SAE record and report ..................................................................................................................................99
1061      17.4 Prediction of AEs and countermeasures .......................................................................................................99

1062   18. Core Laboratory................................................................................................................................................101

1063   19. Quality control ..................................................................................................................................................102

1064   20. Statistical Analysis ...........................................................................................................................................102

1065      20.1 Sample size .................................................................................................................................................102
1066      20.2 Subgroup analysis.......................................................................................................................................103

1067   21. Data Safety and Monitoring Board ...................................................................................................................103

1068   22. Study organization ............................................................................................................................................104

1069   23. Research drug supply and responsibilities division ..........................................................................................106

1070   24. Research Device Processing Mechanism, Characteristics, and Responsibilities Division ...............................107

1071   25. Control requirements ........................................................................................................................................110

1072   26. Institutional Review Board (IRB)/Ethics Committee (IEC) .............................................................................111

1073   Reference ................................................................................................................................................................112

1074   Appendix ................................................................................................................................................................113

1075      Appendix Table 1. ASITN/SIR collateral circulation scale ...............................................................................113
1076      Appendix Table 2. modified Rankin Scale.........................................................................................................115
1077      Appendix Table 3. National Institute of Health Stroke Scale (NIHSS) .............................................................116
1078      Appendix Table 4. EuroQoL 5D-5L ..................................................................................................................121
1079      Appendix Table 5. mTICI grade ........................................................................................................................123
1080

1081

1082

1083

1084

1085

1086

1087
                                                                                           62

```

### DOC-003 PDF page 63

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=63)

```text
       BASIS                                                                             Number:2017YFC1307900



1088

1089                                     Protocol Signature Page
1090
1091   I have read this protocol and agree to adhere to the requirements.
1092
1093   By signing this document we confirm that the clinical study will be conducted in accordance with
1094   the protocol and all applicable laws and regulations including, but not limited to, the International
1095   Conference on Harmonisation Guideline for Good Clinical Practice (GCP) and the ethical principles
1096   that have their origins in the Declaration of Helsinki.
1097
1098
1099
1100   ——————————————————————————————————
1101   Clinical Site
1102
1103
1104
1105   ———————————————                                           ————————————
1106   Site Principal Investigator Signature                     Date
1107

1108

1109
1110
1111
1112
1113
1114
1115
1116
1117
1118
1119
1120
                                                          63

```

### DOC-003 PDF page 64

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=64)

```text
       BASIS                                                                        Number:2017YFC1307900



1121   1. BASIS Protocol Synopsis
1122

          Official Title       Balloon Angioplasty for Symptomatic Intracranial Artery Stenosis: A
                               Multicenter,     Prospective,     Open-Label,       Blinded-Endpoint,
                               Randomized, Controlled Trial
          National   Subject   Prediction model and intervention strategy for recurrence and
          and Number
                               progression of symptomatic intracranial and extracranial major artery
                               stenosis（2017YFC1307900）
          Acronym              BASIS

          PI                   Prof. Zhongrong Miao and Prof. Yilong Wang
          Study Objectives     To evaluate whether combined balloon angioplasty and aggressive
                               medical management (AMM) is superior to AMM for patients with
                               high-risk intracranial atherosclerotic stenosis (ICAS)
          Study Design         The BASIS trial is an investigator-initiated, multicenter, prospective,
                               randomized, open-label, blinded end-point (PROBE) trial
                               Patients eligible in BASIS are 35-80 years old, with a recent
                               transient ischemic attack (<90 days) or ischemic stroke (14-90
                               days) before enrollment attributed to 70-99% atherosclerotic
                               stenosis of a major intracranial artery (terminal internal carotid
                               artery, middle cerebral artery M1 segment, vertebral artery V4
                               segment, and basilar artery) and are randomly assigned to an
                               experimental group and a control group
                               Experimental group: patients will receive balloon angioplasty plus
                               AMM;
                               Control group: patients will receive the AMM alone；
                                   AMM： aspirin 100 mg daily for the entire follow-up and
                                    clopidogrel 75mg daily for the first 90 days after enrollment.
                                    Whether to continue taking clopidogrel after 90 days will be
                                    assessed according to the condition of the patient，clopidogrel
                                    can be replaced with ticagrelor or cilostazol with appropriate
                                    dosage for patients with clopidogrel resistance; atorvastatin will
                                                     64

```


<!-- END support_doc003_pp033-064.md -->

---


<!-- BEGIN support_doc003_pp065-096.md -->

# DOC-003 support quantitative evidence: PDF pages 65–96

Status: COMPLETE. Exact disjoint scope: 32 PDF pages, 65 through 96 inclusive. Document role: PLAN. Content is final protocol, with the version lineage detailed within assigned pages 124–126 in the next part. All 32 pages have usable source-linked native/layout text; fresh-required units: 0; mapped units: 32. No scientific gap. No OCR performed. Reused engine: legacy native/layout extraction, version unavailable; artifacts retained unchanged and hashed in the run inventory. Each page's complete native transcription aid appears below the analytical map. Sources remain final authority.

Reusable assets: `.ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-NNN-native.txt` and corresponding layout files for every assigned page. Page 73 schedule read in layout as well as native text. No earlier scientific conclusions were used.

## Page coverage and result matching keys

| PDF page | Coverage | Quantitative/statistical evidence and matching key |
|---|---|---|
| 65 | COMPLETE | Protocol synopsis: atorvastatin 20–80 mg/day for 1 year; LDL <1.8 mmol/L or <70 mg/dL; blood pressure 130–140/90–100 mmHg; primary composite and secondary outcomes 1–11. Keys: intervention, primary composite, secondary hierarchy. |
| 66 | COMPLETE | Secondary outcomes 12–19 at 24/36 months; all four inclusion criteria. Keys: endpoint status/time, eligibility population. |
| 67 | COMPLETE | Exclusions 1–11, with thresholds and perforator-stroke exception. Key: eligible analysis population. |
| 68 | COMPLETE | Exclusions 11–23 continued; numeric laboratory and survival thresholds. Key: eligible population. |
| 69 | COMPLETE | Exclusions 23–25, sample size 512/256 per arm, rates 7%/15%, power 80%, one-sided alpha 2.5%, dropout 10%, allocation 1:1; complete visit windows; first-100 30-day safety discussion. Keys: power, interim decision, follow-up. |
| 70 | COMPLETE | Abbreviations ACA, ACE, ADA, AE, ARB. No numerical results or additional analysis specification. |
| 71 | COMPLETE | Abbreviations including CI, CEC, DSMB, EQ-5D, FAS, MoCA. Definitions relevant to endpoints/analysis sets retained. |
| 72 | COMPLETE | Abbreviations including mRS, SAE, SAP, SAS, TIA, WASID, TCD. No additional analysis specification. |
| 73 | COMPLETE | Schedule table: screening 15 days to day 0; angiogram day 0; discharge; 30±7 days; 90±7 days; 6 months±14 days; 1 year±30 days; telephone visits every 6 months thereafter through 3 years. mRS/NIHSS/EQ-5D/MoCA measurements, AE/SAE/endpoints and imaging; footnotes establish optional tests. |
| 74 | COMPLETE | Schedule glossary continuation only; no additional numerical/statistical relationship. |
| 75 | COMPLETE | Background historical values 50%, 23% 1-year recurrence, short-term ≤3 months; retained as context, not BASIS outcomes. |
| 76 | COMPLETE | Superiority objective; primary composite detailed with postprocedure 30-day window; hypothesis 50% lower primary risk over 12 months; operator >50 angioplasties/year and training 3–5 cases. |
| 77 | COMPLETE | PROBE design; sICAS TIA <90 days or ischemic stroke 14–90 days, stenosis 70–99%; DSA vessel definitions; 1:1 randomization; aspirin/clopidogrel/atorvastatin doses/durations; first-100 interim discussion. |
| 78 | COMPLETE | Primary endpoint section: any stroke/death within 30 days; qualifying-artery ischemic stroke/revascularization days >30–12 months. Stroke and symptomatic hemorrhage definitions; acute/elective revascularization definitions. |
| 79 | COMPLETE | Elective revascularization criteria: recurrent culprit-territory imaging-confirmed stroke, recurrent TIA >10 minutes or new disabling neurological symptoms. Secondary endpoints 1–8. |
| 80 | COMPLETE | Secondary endpoints 9–19: restenosis, vascular composite, EQ-5D, 24/36-month outcomes. |
| 81 | COMPLETE | Inclusion four conditions and exclusion 1–6; full eligibility definitions. |
| 82 | COMPLETE | Exclusion 6 continued and 7–12; dominant/balanced vertebral definitions, mRS ≥3 exclusion, severe calcification and cardioembolic conditions. |
| 83 | COMPLETE | Exclusions 13–25; complete laboratory, prior-procedure, follow-up and survival conditions. |
| 84 | COMPLETE | Consent plus individual central IWRS randomization stratified by center, 1:1. Key: stratification/randomization. |
| 85 | COMPLETE | DSA core review technical success residual stenosis ≤50%; preprocedure aspirin 100 mg/day and clopidogrel 75 mg/day ≥3 days, intraprocedure anticoagulation. |
| 86 | COMPLETE | Postprocedure aspirin entire follow-up; clopidogrel 75 mg/day or ticagrelor 90 mg twice/day for 90 days after randomization; atorvastatin 20–80 mg/day for 1 year; poor collateral ASITN/SIR <3; wire 0.014 inch. |
| 87 | COMPLETE | Balloon length lesion+≥2 mm each end; submaximal diameter ≤70% proximal artery; inflation 10–30 seconds repeated 2–3 times; technical success ≤50% stenosis, mTICI 3, no flow-impairing dissection; rescue-stent thresholds; final DSA after 10–15 min. |
| 88 | COMPLETE | Identical AMM in both arms; aspirin100/clopidogrel75 doses/durations; resistance ADP aggregation >40% or CYP2C19 loss of function; LDL <1.8 mmol/L or70 mg/dL. |
| 89 | COMPLETE | BP targets ≤140/90 without DM and ≤130/80 with DM; non-HDL <100 mg/dL; added lipid therapy non-HDL ≥100 and triglycerides ≥200; HbA1c <7.0%; timing of laboratory checks. |
| 90 | COMPLETE | Exercise 30 min/day 3 times/week; lipid management and drug compliance counts; permitted antihypertensive doses. |
| 91 | COMPLETE | Remaining antihypertensive doses; follow-up continues after alternative treatment with consent; visit windows begin. |
| 92 | COMPLETE | Follow-up telephone at6 months and after1 year, otherwise in person; 1-year DSA/CTA/MRA; screening laboratory/medical data. |
| 93 | COMPLETE | Screening mRS/NIHSS/MoCA/EQ-5D, optional imaging/genotype tests; treatment visit. |
| 94 | COMPLETE | Drug allocation/recovery, discharge NIHSS and 30±7-day mRS/AE/endpoints. |
| 95 | COMPLETE | 90±7-day mRS/NIHSS; 6 months±14-day telephone mRS; AE/SAE/endpoints. |
| 96 | COMPLETE | 1 year±30-day mRS/NIHSS/MoCA/EQ-5D and DSA; after1 year every6 months±30 days with in-person visits9/11 and telephone visits8/10. |

## Reconstructed relationships

### DOC003-FP-ENDPOINT: primary definition and endpoint hierarchy

At p65 synopsis and p78 section7.1 the primary composite is stroke or death within30 days after enrollment, or qualifying-artery ischemic stroke or revascularization beyond30 days through12 months. Objective p76 explicitly includes ischemic/hemorrhagic stroke or all-cause death within30 days after enrollment or balloon angioplasty of the qualifying lesion during follow-up. Section7.1 p78 explicitly considers symptomatic brain hemorrhage primary only within30 days after enrollment or within30 days after balloon angioplasty during follow-up. These definitions are preserved separately for matching to main-paper primary outcome, not diagnosed here.

Ischemic stroke: sudden new focal neurologic deficit confirmed on brain CT/MRI (p78). Symptomatic brain hemorrhage: parenchymal, subarachnoid or intraventricular hemorrhage on CT/MRI associated with new symptoms (headache, consciousness change or focal symptoms), lasting >24 hours or a seizure (p78). Revascularization primary window is30 days–12 months and requires acute qualifying-artery occlusion with deficit requiring IV/intraarterial thrombolysis, thrombectomy, balloon/stent angioplasty or intracranial-extracranial bypass; or elective neurological symptom-driven revascularization for recurrent imaging-confirmed culprit-territory ischemic stroke or recurrent TIA >10 minutes/new disabling symptoms (pp78–79). Baseline/follow-up imaging is compared for new lesions.

All19 secondary endpoints, in order (pp65–66,79–80): (1) any ischemic/hemorrhagic stroke or all-cause death within30 days after enrollment or qualifying-lesion angioplasty during follow-up; (2) target-territory ischemic/hemorrhagic stroke or all-cause death within90 days; (3) outside-target-territory stroke within90 days; (4) mRS90 days; (5) target-territory stroke or all-cause death within12 months; (6) target-artery revascularization within12 months; (7) outside-target-territory stroke within12 months; (8) mRS12 months; (9) target-artery restenosis within12 months, stenosis >70% or increase by30% on follow-up neurovascular imaging; (10) composite stroke, MI or vascular death within12 months; (11) EQ-5D within12 months; (12) target-territory stroke or all-cause death24 months; (13) outside-target-territory stroke24 months; (14) mRS24 months; (15) stroke/MI/vascular death24 months; (16) target-territory stroke or all-cause death36 months; (17) outside-target-territory stroke36 months; (18) neurological improvement by mRS36 months; (19) stroke/MI/vascular death36 months. All are secondary in this protocol; no separate key-secondary ranking is stated in these pages. Synopsis says composite stroke, MI **and** vascular death while detailed section says **or**; both text occurrences retained for interpretation by checkers.

### DOC003-FP-POPULATION: full eligibility criteria

Inclusion: age35–80; primary/recurrent sICAS with TIA <90 days or ischemic stroke14–90 days attributable to70–99% major-intracranial stenosis while receiving≥1 antithrombotic and/or standard risk-factor management; DSA confirms ICA C4–C7, MCA M1, VA V4 or BA stenosis70–99% by WASID, lesion≤10 mm, diameter≥1.5 mm, normal distal artery, anatomy judged by investigator; signed consent (pp66,81).

Exclusions all25 (pp67–69,81–83): (1) surgery past30 days/planned major or≥3-grade surgery90 days; (2) thrombolysis previous24 hours; (3) worsening deficits previous24 hours; (4) acute ischemic stroke previous14 days; (5) other severe70–99% intracranial stenosis apart from target/supplying artery; (6) supplying-artery stenosis >50%, with ipsilateral ICA/dominant VA examples, nonlesion extracranial >70%, balanced bilateral VA >70%, and dominant-lesion VA exceptions for slender/dysplastic/non-dominant PICA-terminating contralateral VA; (7) perforator stroke except severe supplying stenosis with hemodynamic compromise/poor collaterals; (8) baseline mRS≥3; (9) nonatherosclerotic diseases including dissection, moyamoya, inflammatory/infectious/autoimmune/postradiation/postpartum disease, fibromuscular dysplasia, sickle cell anemia, suspected vasospasm; (10) severely calcified target; (11) embolism from extracranial/cardioembolic source including AF, mitral stenosis, PFO, LV thrombus, MI within6 weeks; (12) intracranial tumor/aneurysm/AVM; (13) intracranial hemorrhage within3 months; (14) previous target/supplying-vessel angioplasty/stenting/endarterectomy or planned stenting; (15) inability to receive DAPT; (16) inaccessible tortuous approach; (17) allergy to heparin/aspirin/clopidogrel/contrast/anesthetics/balloon components; (18) hemoglobin<100 g/L, platelets<100×10^9/L, irreversible INR>1.5, coagulation dysfunction/uncorrectable bleeding; (19) ALT/AST>3×upper normal or creatinine>2×upper normal; (20) pregnancy/lactation; (21) concurrent renal/radial/coronary intervention; (22) expected survival<1 year; (23) mental/cognitive/emotional barriers to follow-up; (24) other incomplete drug/device trial participation; (25) investigator judgment unsuitable.

### DOC003-FP-DESIGN: intervention, randomization, dose and procedure

Individual multicenter PROBE superiority trial (pp76–77); central IWRS, center-stratified, 1:1 (p84). Experimental balloon angioplasty plus AMM, control AMM. Both arms aspirin100 mg/day throughout follow-up and clopidogrel75 mg/day first90 days; clopidogrel continuation discretionary thereafter; replacement ticagrelor/cilostazol if resistant (p77,p88). Procedure p86 specifies alternative ticagrelor90 mg twice/day. Resistance ADP aggregation>40% or CYP2C19 loss-of-function alleles (p88). Atorvastatin20–80 mg/day1 year, LDL<1.8 mmol/L or70 mg/dL (pp77,86,88). Summary/overview BP130–140/90–100 (pp65,77); detailed management ≤140/90 without DM, ≤130/80 with DM (p89); preserve occurrences separately.

Preprocedure DAPT≥3 days; heparin during procedure (p85). Balloon length extends≥2 mm beyond each lesion end; submaximal diameter≤70% proximal artery; inflation10–30 seconds, repeat2–3 times if needed (p87). Technical success residual stenosis≤50%, mTICI3, no dissection impairing flow. Rescue stenting if residual stenosis≥70% or unstable antegrade flow mTICI<2b, flow-impairing dissection mTICI<2b, or thrombosis/embolism jeopardizing distal perfusion. Thrombolysis/GP IIb/IIIa inhibitors allowed with/without rescue stenting by physician judgment. Poor collateral ASITN/SIR<3 (p86). Main-paper keys: procedural success, rescue stents, randomized treatment components, per-protocol/as-treated populations.

### DOC003-FP-POWER-INTERIM: sample size and safety decision

Synopsis p69: experimental7%, control15%, absolute difference8 percentage points,80% power, one-sided alpha2.5%,10% attrition,1:1, total512=256 each. Objective p76 states hypothesis50% lower primary-event risk over12 months. No sample-size equation in this shard. First100 participants complete30-day perioperative observation, then investigators discuss feasibility/continuation (pp69,77–78); no numerical efficacy stopping boundary in those passages.

### DOC003-FP-FOLLOWUP: visit schedule, outcomes and missingness-related follow-up

Baseline; DSA day; discharge;30±7 days;90±7 days;6 months±14 days;1 year±30 days; subsequent6-month intervals through3 years (pp69,73,91–96). In-person except6-month/post1-year telephone, with visits9/11 in-person (pp92,96). Follow-up remains sought after alternative treatments such as stenting when participant consents (p91). Neurovascular imaging at1 year DSA/CTA/MRA (p92); visit7 list calls DSA necessary, CTP optional (p96). mRS/NIHSS/EQ-5D/MoCA gathered as listed per page; MoCA optional. No missing-value statistical imputation rule or named analysis-population definition in this shard.

## Complete per-page native transcription aids

The following source-linked retained transcriptions supply every detailed row, scale name, numerical background quantity, dose and footnote. They are aids, not adjudications.

### PDF page 65

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=65)

```text
BASIS

Number:2017YFC1307900

be taken 20mg-80mg/day for one year after enrollment; the dose
was adjusted to control LDL <1.8mmol/L or <70mg/dl. Whether
to continue taking atorvastatin after one year will be assessed
according to the patient's condition.


Risk

factor

management—Control

blood

pressure

130-140/90-100 mmHg
Primary Endpoint

The primary outcome is stroke or death within 30 days after
enrollment, or any ischemic stroke or revascularization of the
qualifying artery beyond 30 days through 12 months after enrollment.

Secondary Endpoints 1.

Any stroke (ischemic or hemorrhage stroke) or all-cause death
within 30 days after enrollment or after balloon angioplasty
procedure of the qualifying lesion during follow-up

2.

Any stroke (ischemic or hemorrhage stroke) in the territory of the
target artery or all-cause death within 90 days after enrollment

3.

Any stroke (ischemic or hemorrhage stroke) outside of the
territory of the target artery within 90 days after enrollment

4.

mRS (modified Rankin Scale) at 90 days

5.

Any stroke (ischemic or hemorrhage stroke) in the territory of the
target artery or all-cause death within 12 months after enrollment

6.

Revascularization of the qualifying artery within 12 months after
enrollment

7.

Any stroke (ischemic or hemorrhage stroke) outside of the
territory of the target artery within 12 months after enrollment

8.

mRS at 12 months

9.

Restenosis rate of the target artery within 12 months (defined as
rate of stenosis >70% or increased by 30% based on following-up
neurovascular imaging)

10. Combined events such as stroke, myocardial infarction, and
vascular death within 12 months after enrollment
11. Quality of life assessment (EuroQol-5-Dimensions Scale
[EQ-5D] questionnaire) within 12 months after enrollment
65


```

### PDF page 66

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=66)

```text
BASIS

Number:2017YFC1307900

12. Any stroke (ischemic or hemorrhage stroke) in the territory of the
target artery or all-cause death within 24 months after enrollment
13. Any stroke (ischemic or hemorrhage stroke) outside of the
territory of the target artery within 24 months after enrollment
14. mRS at 24 months
15. Combined events such as stroke, myocardial infarction, and
vascular death within 24 months after enrollment
16. Any stroke (ischemic or hemorrhage stroke) in the territory of the
target artery or all-cause death within 36 months after enrollment
17. Any stroke (ischemic or hemorrhage stroke) outside of the
territory of the target artery within 36 months after enrollment
18. Neurological improvement assessed by mRS at 36 months
19. Combined events such as stroke, myocardial infarction, and
vascular death within 36 months after enrollment.
Inclusion Criteria

1.

Age 35-80 years

2.

Participants with primary or recurrent sICAS (a recent TIA[<90
days] or ischemic stroke [14-90 days] before enrollment
attributed to 70-99% atherosclerotic stenosis of a major
intracranial artery) receiving treatment with at least one
antithrombotic drug and/or standard medical management of
vascular risk factors

3.

Diagnosed by DSA: a major intracranial artery (terminal internal
carotid artery [ICA] [C4-C7 segments], middle cerebral artery
[MCA] M1 segment, vertebral artery [VA] V4 segment, and
basilar artery [BA]) severe atherosclerotic stenosis (70-99%
according to WASID method) with lesion length ≤ 10mm,
diameter ≥1.5mm, and normal distal artery. (Regarding the
curvature and angle of the lesion, whether the patient is enrollled
in BASIS will be assessed according to the investigator's
determination based on the patient’s anatomy)

4.

Informed consent signed.
66


```

### PDF page 67

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=67)

```text
BASIS

Exclusion Criteria

Number:2017YFC1307900

1.

Surgery within the past 30 days or plan to receive major surgery
within 90 days

2.

Thrombolytic therapy within 24 hours before enrollment

3.

Neurological deficits worsen within 24 hours before enrollment

4.

Acute ischemic stroke onset within 14 days before enrollment

5.

Other intracranial arteries with severe stenosis (70-99%) besides
the target artery and its supplying artery

6.

Target artery’s supplying artery stenosis > 50%. For example,
patient with MCA severe stenosis (target artery) and the
ipsilateral ICA stenosis > 50% should be excluded; patient with
BA severe stenosis (target artery) and the dominant VA
stenosis > 50% should be excluded; the patient with extracranial
artery (non-lesion side) stenosis > 70% should be excluded; For
patients with balanced VA, if bilateral VA stenosis > 70% at the
same time, should be excluded (unable to determine which VA
is the lesion artery). However, if patient’s dominant VA is the
lesion artery with a dysplasia or slender contralateral VA or a
non-dominant contralateral VA terminating at posteroinferior
cerebellar artery, should not be excluded.

7.

Participant with perforator stroke (except for severe stenosis of
supplying artery combined with hemodynamic compromise or
poor collaterals)

8.

Baseline mRS ≥ 3

9.

Non-atherosclerotic

diseases

(e.g.,

arterial

dissection,

moyamoya disease, vascular inflammatory lesions caused by
infection, autoimmune diseases, post-radiation, postpartum
status; developmental or genetic abnormalities such as
fibromuscular

dysplasia,

sickle

cell

anemia,

suspected

vasospasm)
10. Target artery with severely calcified and adjacent to stenosis
11. Suspected ischemic event caused by embolism or the arterial
67


```

### PDF page 68

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=68)

```text
BASIS

Number:2017YFC1307900

embolism from extracranial segment (ipsilateral chest or neck
vascular occlusive disease) or potential cardioembolism (e.g.,
atrial fibrillation, mitral stenosis, patent foramen ovale, left
ventricular thrombus, myocardial infarction within 6 weeks,
etc.)
12. Coexistent intracranial tumor, aneurysm or arteriovenous
malformation
13. Intracranial hemorrhage within the past 3 months, including
parenchymal

hemorrhage,

intraventricular

hemorrhage,

subarachnoid hemorrhage, epidural hemorrhage or subdural
hemorrhage, etc.
14. Angioplasty procedure (including balloon dilatation, stenting, or
endarterectomy) performed at the original target vessel or its
primary supplying artery, or a planned stenting procedure
15. Unable to receive dual antiplatelet therapy due to other diseases
16. Tortuous vascular approach that cannot be stabilized to obtain
vascular access
17. Allergy to heparin, aspirin, clopidogrel, contrast agents,
anesthetics, and balloon components
18. Hemoglobin

< 100g/L, platelet

count

<

100×109/

L,

international normalized ratio (INR) >1.5 (irreversible),
Coagulation dysfunction or uncorrectable bleeding factors
19. Severe liver or kidney dysfunction. ALT > three-fold higher
than the upper limit of normal value or AST > three-fold higher
than the upper limit of normal value, or serum creatinine >
two-fold higher than the upper limit of normal value
20. Pregnant and lactating women
21. Participants with renal artery, radial artery, and coronary artery
requiring concurrent intervention
22. Expected survival is less than< 1 year
23. Unable to complete follow-up due to mental illness, cognitive or
68


```

### PDF page 69

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=69)

```text
BASIS

Number:2017YFC1307900

emotional disorders
24. Participants participating in other drug/medical device clinical
trials who have not yet completed the program requirements
25. Participants are not suitable for the BASIS trial per investigator’s
opinion.
Sample Size

According to previous literature：①we assume a 7% event rate
of the primary endpoint in the experimental group；②a 15% event
rate of the primary endpoint in the control group；③an 80% statistical
power at a one-sided α of 2.5% and a 10% attrition rate；④the
experimental group and the control group are allocated according to a
1:1 ratio.
Finally, a total of 512 patients (256 per group) are planned to be
enrollled.

Follow-up

All participants will be followed up by the on-site neurologist at
baseline, the day of DSA, discharge, 30±7 days, 90±7 days, 6
months±14 days, 1year ±30 days and up to 3years (at 6-month
intervals after 1 year).

Study
period

introduction After the study is formally started, the participating study centers
copy the video (including the DSA and endovascular process) of 3-5
cases of balloon angioplasty in their centers and transfer the video to
the core laboratory. After consistency is passed, the group continues
to enrollment. This process is to ensure the consistency of the balloon
angioplasty procedure with the protocol.
The first 100 participants completed the peri-operative (30 days)
observation, mainly collecting the adverse events during the
peri-operative period. The PI will need to meet with other
investigators from the participating centers for interim discussion to
evaluate the feasibility of this treatment plan and the continuation of
later research, and follow-up research can be conducted later.

1123
1124
69


```

### PDF page 70

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=70)

```text
BASIS

Number:2017YFC1307900

1125
1126
1127
1128
1129
1130
1131
1132
1133
1134
1135
1136
1137
1138

1139

2. Abbreviations
ACA

Anterior Cerebral Artery

ACE

Angiotensin Converting Enzyme

ADA

American Diabetes Association

AE

Adverse Event

ARB

Angiotensin Receptor Blocker
70


```

### PDF page 71

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=71)

```text
BASIS

Number:2017YFC1307900

BMI

Body Mass Index

BP

Blood Pressure

CEC

Clinical Events Adjudication Committee

CFDA
CHANCE

China Food and Drug Administration
Clopidogrel in High-risk patients
Cerebrovascular Events

CI

Confidence Interval

CRF

Case Report Form

CT

Computer Tomography

CTP

Computed Tomography Perfusion Imaging

DAPT

Dual Antiplatelet Therapy

DICOM

Digital Imaging and Communications in Medicine

DSA

Digital Subtraction Angiography

DSMB

Data Safety Monitoring Board

EoT

End of Trial

EQ-5D

EuroQOL five Dimensions questionnaire

FAS

Full Analysis Set

FFR

Fractional Flow Reserve

HDL

High Density Lipoprotein

ICAD

Intracranial Atherosclerotic Disease

ICAS

Intracranial Atherosclerotic Stenosis

IDL

Intermediate Density Lipoproteins

IEC

Independent Ethics Committee

IRB

Institutional Review Board

IVRS

Inter-voice Response System Inter-voice

LDL

Low Density Lipoprotein

LFT

Liver Function Test

MCA

Middle Cerebral Artery

MI

Myocardial Infarction

MoCA

Cognitive Functional Outcome by the Montreal Cognitive Assessment
71

with

Acute

Nondisabling


```

### PDF page 72

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=72)

```text
BASIS

Number:2017YFC1307900

mRS

Modified Rankin Scale

NMPA

National Medical Products Administration

PTAS

Percutaneous Transluminal Angioplasty and Stenting

SAE
SAMMPRIS

Serious Adverse Event
Stenting and Aggressive Medical Management for Preventing Recurrent
stroke in Intracranial Stenosis

SAP

Statistical Analysis Plan

SAS

Statistical Analysis Software SAS

SNPs

Single Nucleotide Polymorphisms

TIA

Transient Ischemic Attacks

UADE

Unanticipated Adverse Device Effect

VLDL

Very Low Density Lipoproteins

WASID

Warfarin-Aspirin Symptomatic Intracranial Disease

TCD

Transcranial Doppler

72


```

### PDF page 73

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=73)

```text
BASIS

Number:2017YFC1307900

3. Schedule of assessments

1140
1141

Visit

Assessment
Informed consent

Follow up 1y to 3y

Visit 2

Visit 3

Visit 4

Baseline

Angiogram
0d

Discharge

30d±7d

X

X

X

X

X

X

X

X

X

X

X

X

15d～0 d

Visit 5

Visit 6

Visit 1

90d±7 d

Visit 7

Telephone interview
6 mo±14 d

(Visit 8,9,10,11)
6

1y±30 d

months

intervals

X

Inclusion/exclusion criteria check X
History and physical examination X
Vital signs1
Blood laboratory test
urine routine test

X
2

and

X

Coagulation function3

X

FBG, HbA1c4

X

Platelet aggregation test and/or
X
CYPC219 genotype test5
ECG

X

MRI/CT

X

6

X
X9

CTP

DSA/CTA/MRA
Life-style modification review

X

7

mRS

X

X

X

X

NIHSS (neurological examination) X

X

X

X

X

X

X

X

X

X

X

X

X

X

EQ-5D
examination)

X

X

X

5

MoCA

X

X

X

HR-VWI,TCD5

X

X

Medication review and patient
compliance survey
AE、SAE and endpoints8

1142
1143
1144
1145
1146
1147
1148
1149
1150
1151
1152
1153
1154
1155
1156
1157
1158
1159

X

X9

X

X

X

X

X

X

X

X

X

X
X

X

X8

1. Vital signs: blood pressure, heart rate, respiration rate, body temperature;
2. Blood laboratory test includes blood routine and biochemistry examinations, hepatic and renal function tests.
3. Coagulation function: PT, APTT, TT, FIB, INR;
4. HbA1c is an optional test, but is recommended for patients with Diabetes Mellitus.
5. Platelet aggregation test, CYPC219 genotype test, MoCA, HR-VWI and TCD test are optional according
to the availability of the test at the center;
6. CTP is an optional test, but is recommended for patients with hemodynamic compromise, poor collateral
or perforator stroke.
7. Life-style modification review: including whether to smoke and the number of cigarettes per day; Weight:
reflect the patient's weight control through the patient's weight and BMI; Exercise: number of exercises per
week and duration of each exercise.
8. After one year of follow-up, follow-up will focus on AE, SAE and endpoint events;
Abbreviations: FBG, fasting blood glucose; HbA1c, Glycosylated Hemoglobin; ECG, electrocardiograph;
MRI, magnetic resonance imaging; CT, computerized tomography; CTP, CT perfusion; DSA, digital
subtraction angiography; CTA, computerized tomography angiography; MRA, magnetic resonance
angiography; digital subtraction angiography (DSA), computerized tomography angiography (CTA), or
magnetic resonance angiography (MRA); mRS, modified Rankin scale; EQ-5D, quality-of-life EuroQol-5
73


```

### PDF page 74

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=74)

```text
BASIS

1160
1161

Number:2017YFC1307900

Dimensions; MoCA, montreal cognitive assessment; HR-VWI, High-resolution vessel wall imaging; TCD,
transcranial Doppler; AE, adverse event; SAE, serious adverse event.

74


```

### PDF page 75

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=75)

```text
BASIS

Number:2017YFC1307900

1162

4. Background

1163

Intracranial atherosclerotic stenosis (ICAS) is a major etiology of stroke worldwide, which is

1164

associated with stroke recurrence, substantial morbidity, and mortality, accounting for up to 50%

1165

of ischemic strokes in south and east Asia.1 Despite receiving treatment with aspirin and

1166

standard medical management of vascular risk factors, patients with symptomatic ICAS (sICAS)

1167

still have as high as 23% 1-year stroke recurrence rate. 2,3 Therefore, secondary prevention of

1168

stroke and reducing mortality in patients with sICAS is a global major issue. Currently,

1169

treatment options for sICAS include aggressive medical management (AMM), balloon

1170

angioplasty, and stenting (balloon angioplasty combined with stenting); however, the optimal

1171

treatment for sICAS remains unclear.

1172

The SAMMPRIS and VISSIT trials have shown high perioperative complication rates and

1173

no significant advantage of endovascular stents compared to aggressive medical therapy (AMM)

1174

in the long term. 4, 5 However, the CASSISS trial reported that stenting by experienced operators

1175

didn’t add additional risk of stroke or death within 30 days compared to AMM for sICAS,

1176

although it failed to demonstrate a benefit of stenting.6 As lower rates of short-term stroke or

1177

mortality (peri-procedural or mean follow-up ≤ 3 months) were found in balloon angioplasty

1178

than stenting,7 balloon angioplasty alone may be a feasible alternative treatment to stenting for

1179

sICAS treatment. Moreover, several previous meta-analyses also proved the safety and efficacy

1180

of balloon angioplasty for sICAS, which suggested that balloon angioplasty alone may be a

1181

potentially promising treatment for sICAS.8-10

1182

To date, limited evidence is available from RCTs to determine the efficacy and safety of

1183

balloon angioplasty for sICAS patients. Hence, we designed the BASIS (Balloon Angioplasty
75


```

### PDF page 76

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=76)

```text
BASIS

Number:2017YFC1307900

1184

for Symptomatic Intracranial Artery Stenosis) randomized controlled trial to explore whether

1185

balloon angioplasty plus AMM is superior to AMM alone in patients with sICAS.

1186
1187

5. Objectives and Hypothesis

1188

5.1 Objectives

1189

To investigate whether balloon angioplasty combined with AMM is superior to AMM alone for

1190

patients with high-risk sICAS in the primary endpoint (ischemic/haemorrhagic stroke or

1191

all-cause death within 30 days after enrollment or after balloon angioplasty procedure of the

1192

qualifying lesion during follow-up, or any ischemic stroke or revascularization from the

1193

qualifying artery beyond 30 days through 12 months after enrollment).

1194

5.2 Hypothesis

1195

Compared to AMM alone, balloon angioplasty combined with AMM could decrease the risk of

1196

the primary endpoint by 50% in patients with high-risk sICAS over the 12-month follow-up

1197

period.

1198
1199

6. Study Design

1200

Study introduction period

1201

After the study is formally started, the participating study centers copied the video (including the

1202

DSA and surgical process) of 3-5 cases of balloon angioplasty in their centers and transfer the

1203

video to the core laboratory (Beijing Tiantan Hospital). After the consistency is passed, the

1204

group continued to enrolll, so as to ensure the consistency of the balloon angioplasty procedure.

1205

The annual volume of BA by the neurointerventionalists in the BASIS trial was more than 50

1206

cases. The neurointerventionalists from the participating centers received standard training in

1207

technique from the leading center at regular intervals.
76


```

### PDF page 77

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=77)

```text
BASIS

Number:2017YFC1307900

1208

The BASIS trial is an investigator-initiated, multicenter, prospective, randomized,

1209

open-label, blinded end-point (PROBE) trial that plans to enrolll patients with sICAS (defined as

1210

a recent TIA (<90 days) or ischemic stroke (14-90 days) attributed to a 70-99% atherosclerotic

1211

stenosis of a major intracranial artery including terminal internal carotid artery [ICA] C4-C7

1212

segment, middle cerebral artery [MCA] M1 segment, vertebral artery [VA] V4 segment and

1213

basilar artery [BA]) determined by DSA. The patients are randomly assigned to either the

1214

experimental group or the control group at a 1:1 ratio.

1215

Experimental group: patients will receive balloon angioplasty (details in procedure part) plus

1216

AMM (same as the control group);

1217

Control group: patients will receive the AMM alone.

1218



Drug administration plan of AMM: aspirin 100 mg daily for the entire follow-up and

1219

clopidogrel 75mg daily for the first 90 days after enrollment. Whether to continue taking

1220

clopidogrel after 90 days will be assessed according to the condition of the patient，

1221

clopidogrel can be replaced with ticagrelor or cilostazol with appropriate dosage for

1222

patients with clopidogrel resistance; atorvastatin were used 20mg-80mg/day for one year

1223

after enrollment; the dose was adjusted to control LDL <1.8mmol/L or <70mg/dl. Whether

1224

to continue taking atorvastatin after one year will be assessed according to the patient's

1225

condition.

1226
1227



Risk factor management—Control blood pressure 130-140/90-100 mmHg and LDL
<1.8mmol/L or <70mg/dl

1228

The first 100 participants completed the peri-operative (30 days) observation, mainly collecting

1229

the adverse events during the peri-operative period. The PI needs to meet with other

1230

investigators from the participating centers for interim discussion to evaluate the feasibility of

77


```

### PDF page 78

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=78)

```text
BASIS

Number:2017YFC1307900

1231

this treatment plan and the continuation of later research, and follow-up research can be

1232

conducted later.

1233

7. Study Endpoint

1234

7.1 Primary endpoint

1235

The primary endpoint is stroke or death within 30 days after enrollment, or any ischemic stroke

1236

or revascularization of the qualifying artery beyond 30 days through 12 months after enrollment.

1237

Ischemic stroke is defined as a new focal neurologic deficit of sudden onset, which is

1238

confirmed on brain CT or MRI. Symptomatic brain hemorrhage is defined as parenchymal,

1239

subarachnoid, or intraventricular hemorrhage detected on CT or MRI, which is associated with

1240

new neurologic symptoms (headache, change in the level of consciousness, or focal neurologic

1241

symptoms), lasting over 24 hours or a seizure. Symptomatic brain hemorrhage will be

1242

considered a primary endpoint only when it occurs within 30 days after enrollment or within 30

1243

days after the balloon angioplasty procedure during follow-up. Revascularization of the culprit

1244

artery will be considered a primary endpoint if it occurs from 30 days through 12 months after

1245

enrollment and fulfills one of the following requirements:

1246

c. Acute revascularization: acute qualifying artery occlusion accompanied by neurological

1247

deficit, requiring intravenous

1248

thrombectomy, balloon/stent angioplasty, or intracranial-extracranial bypass.

thrombolysis,

intraarterial

thrombolysis, mechanical

1249

d. Elective revascularization: neurologic symptom-driven revascularization, including BA,

1250

stent implantation, or intracranial-extracranial bypass, if the participant fulfills one of the

1251

following conditions:

78


```

### PDF page 79

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=79)

```text
BASIS

Number:2017YFC1307900

1252

3) Ischemic stroke caused by the culprit artery stenosis: a new focal neurological deficit of

1253

sudden onset attributed to the territory of the culprit artery, which is confirmed as a

1254

recurrent stroke on brain CT or MRI (follow-up imaging will be compared to baseline

1255

imaging for the detection of new lesions)

1256

4) Culprit artery stenosis that causes recurrent transient ischemic attack lasting longer than

1257

10

1258

weakness/numbness, inarticulateness, diplopia, or ataxia) compared to the baseline

1259

qualifying symptoms.

minutes

or

new

disabling

neurological

symptoms

(paroxysmal

limb

1260

7.2 Secondary endpoints

1261

1.

1262

enrollment or after balloon angioplasty procedure of the qualifying lesion during follow-up

1263

2.

1264

death within 90 days after enrollment

1265

3.

1266

within 90 days after enrollment

1267

4.

1268

5. Any stroke (ischemic or hemorrhage stroke) in the territory of the target artery or all-cause

1269

Any stroke (ischemic or hemorrhage stroke) or all-cause death within 30 days after

Any stroke (ischemic or hemorrhage stroke) in the territory of the target artery or all-cause

Any stroke (ischemic or hemorrhage stroke) outside of the territory of the target artery

mRS at 90 days

death within 12 months after enrollment

1270

6.

1271

7. Any stroke (ischemic or hemorrhage stroke) outside of the territory of the target artery

1272
1273

Revascularization of the target artery within 12 months after enrollment

within 12 months after enrollment
8.

mRS at 12 months
79


```

### PDF page 80

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=80)

```text
BASIS

1274
1275
1276
1277
1278
1279
1280
1281
1282
1283

Number:2017YFC1307900

9. Restenosis of the target artery within 12 months (defined as stenosis >70% or increased by
30% based on following-up neurovascular imaging)
10. Combined events such as stroke, myocardial infarction, or vascular death within 12 months
after enrollment
11. Quality of life assessment (EuroQol-5-Dimensions Scale [EQ-5D] questionnaire) within 12
months after enrollment
12. Any stroke (ischemic or hemorrhage stroke) in the territory of the target artery or all-cause
death within 24 months after enrollment
13. Any stroke (ischemic or hemorrhage stroke) outside of the territory of the target artery
within 24 months after enrollment

1284

14. mRS at 24 months

1285

15. Combined events such as stroke, myocardial infarction, or vascular death within 24 months

1286
1287
1288
1289
1290

after enrollment
16. Any stroke (ischemic or hemorrhage stroke) in the territory of the target artery or all-cause
death within 36 months after enrollment
17. Any stroke (ischemic or hemorrhage stroke) outside of the territory of the target artery
within 36 months after enrollment

1291

18. Neurological improvement assessed by mRS at 36 months

1292

19. Combined events such as stroke, myocardial infarction, or vascular death within 36 months

1293

after enrollment.

1294
1295

8. Inclusion and Exclusion Criteria
80


```

### PDF page 81

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=81)

```text
BASIS

Number:2017YFC1307900

1296

8.1 Inclusion criteria

1297

1. Age 35-80 years

1298

5. Participants with primary or recurrent sICAS (a recent TIA [<90 days] or ischemic stroke

1299

[14-90 days] before enrollment attributed to 70-99% atherosclerotic stenosis of a major

1300

intracranial artery) receiving treatment with at least one antithrombotic drug and/or standard

1301

medical management of vascular risk factors

1302

6. Diagnosed by DSA: a major intracranial artery (terminal internal carotid artery [ICA] [C4-C7

1303

segments], middle cerebral artery [MCA] M1 segment, vertebral artery [VA] V4 segment,

1304

and basilar artery [BA]) severe atherosclerotic stenosis (70-99% according to WASID

1305

method11) with lesion length ≤ 10mm, diameter ≥1.5mm, and normal distal artery.

1306

(Regarding the curvature and angle of the lesion, whether the patient is enrollled in BASIS

1307

will be assessed according to the investigator's determination based on the patient’s anatomy)

1308

7. Informed consent signed.

1309

8.2 Exclusion criteria

1310

1. Surgery within the past 30 days or plan to receive ≥ 3-grade surgery within 90 days

1311

2. Thrombolytic therapy within 24 hours before enrollment

1312

3. Neurological deficits worsen within 24 hours before enrollment

1313

4. Acute ischemic stroke onset within 14 days before enrollment

1314

5. Other intracranial arteries with severe stenosis (70-99%) besides the target artery and its

1315

supplying artery

1316

6. Target artery’s supplying artery stenosis > 50%. For example, patient with MCA severe

1317

stenosis (target artery) and the ipsilateral ICA stenosis > 50% should be excluded; patient
81


```

### PDF page 82

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=82)

```text
BASIS

Number:2017YFC1307900

1318

with BA severe stenosis (target artery) and the dominant VA stenosis > 50% should be

1319

excluded; the patient with extracranial artery (non-lesion side) stenosis > 70% should be

1320

excluded; For patients with balanced VA, if bilateral VA stenosis > 70% is present at the

1321

same time, the patient should be excluded (unable to determine which VA is the lesion

1322

artery). However, if the patient’s dominant VA is the lesion artery with a dysplasia or

1323

slender contralateral VA or a non-dominant contralateral VA terminating at the

1324

posteroinferior cerebellar artery, the patient should not be excluded.

1325
1326

7. Participant with perforator stroke (except for severe stenosis of supplying artery combined
with hemodynamic compromise or poor collaterals)12

1327

8. Baseline modified Rankin Scale ≥ 3

1328

9. Non-atherosclerotic diseases (e.g., arterial dissection, moyamoya disease, vascular

1329

inflammatory lesions caused by infection, autoimmune diseases, post-radiation, postpartum

1330

status; developmental or genetic abnormalities such as fibromuscular dysplasia, sickle cell

1331

anemia, suspected vasospasm)

1332

10. Target artery with severe calcification

1333

11. Suspected ischemic event caused by embolism or arterial embolism from an extracranial

1334

segment (ipsilateral chest or neck vascular occlusive disease) or potential cardioembolism

1335

(e.g., atrial fibrillation, mitral stenosis, patent foramen ovale, left ventricular thrombus,

1336

myocardial infarction within 6 weeks, etc.)

1337

12. Coexistent intracranial tumor, aneurysm or arteriovenous malformation

82


```

### PDF page 83

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=83)

```text
BASIS

Number:2017YFC1307900

1338

13. Intracranial hemorrhage within the past 3 months, including parenchymal hemorrhage,

1339

intraventricular hemorrhage, subarachnoid hemorrhage, epidural hemorrhage or subdural

1340

hemorrhage, etc.

1341

14. Angioplasty procedure (including balloon dilatation, stenting, or endarterectomy) already

1342

performed at the original target vessel or its primary supplying artery, or a planned stenting

1343

procedure

1344

15. Unable to receive dual antiplatelet therapy due to other diseases

1345

16. Tortuous vascular approach not amenable to vascular access

1346

17. Allergy to heparin, aspirin, clopidogrel, contrast agents, anesthetics, and balloon components

1347

18. Hemoglobin < 100g/L, platelet count < 100×109/ L, international normalized ratio

1348

(INR) >1.5 (irreversible), Coagulation dysfunction or uncorrectable bleeding factors

1349

19. Severe liver or kidney dysfunction. ALT > three-fold higher than the upper limit of normal

1350

value or AST > three-fold higher than the upper limit of normal value, or serum creatinine >

1351

two-fold higher than the upper limit of normal value

1352

20. Pregnant and lactating women

1353

21. Participants with renal artery, radial artery, and coronary artery requiring concurrent

1354

intervention

1355

22. Expected survival is less than< 1 year

1356

23. Unable to complete follow-up due to mental illness, cognitive or emotional disorders

1357

24. Participants participating in other drug/medical device clinical trials who have not yet

1358
1359

completed the program requirements
25. Participants are not suitable for BASIS trial per investigator’s opinion.
83


```

### PDF page 84

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=84)

```text
BASIS

Number:2017YFC1307900

1360
1361

9. Informed Consent

1362

The clinical trial must follow the Helsinki Declaration and the relevant clinical trial norms and

1363

regulations in China. Informed consent was designed based on NMPA regulations and ICH

1364

guidelines. Each patient who agreed to participate the study will be invited to sign an informed

1365

consent form. Before signing the informed consent form, a specially trained researcher

1366

(understanding the key points of the study and the related risks of the study, the confidentiality

1367

of the management records and the source of funds, etc.) will introduce the research purpose,

1368

study plan, study cycle, potential risks and expected benefits, cost and compensation, voluntary

1369

participation principle, treatment principle of study related risks, etc.

1370
1371

10. Randomization

1372

The BASIS trial used an interactive web response system (IWRS) for central randomization

1373

stratified by study centers. Patients who sign the informed consent and meet all inclusion criteria

1374

and do not meet any exclusion criteria will be enrollled in the study. After entering the eligible

1375

patient’s necessary information into the web-based system, the researcher in each center will

1376

obtain a random code as well as the corresponding group allocation information from the IWRS.

1377

Eligible patients will be randomized into either the experimental group or the control group at a

1378

1:1 ratio (Figure 1). Finally, researchers and research assistants need to print randomization

1379

application forms and center randomization lists.

84


```

### PDF page 85

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=85)

```text
BASIS

Number:2017YFC1307900

1380

The researcher team should archive the randomized list and related files (randomized

1381

application form) together in the central researcher folder (archived by the clinical study

1382

department of the center).

1383
1384

11. DSA evaluation and lesion evaluation

1385

In order to ensure the quality of DSA images in the study, we will choose a clinical research

1386

center with DSA facilities. Before the start of the study, researchers from all centers will

1387

participate in the training of image generation, collection and evaluation, and obtain

1388

corresponding qualifications.

1389

When the patient is enrollled, the central laboratory will obtain the CD disc of the patient's

1390

MRI / HRMRI imaging, CT perfusion imaging, and DSA before balloon angioplasty for central

1391

review. DSA imaging needs to show the residual vessel diameter at the maximum stenosis and

1392

the maximum length of the stenosis. If the patient underwent balloon angioplasty, arterial

1393

imaging after angioplasty should also be sent to the central laboratory for central review. The

1394

standard of technical success is the residual stenosis of the target vessel ≤ 50 %.

1395
1396

12. Balloon Angioplasty

1397

Antithrombotic protocol

1398

Pre-procedure: All patients who are scheduled to undergo balloon angioplasty should receive

1399

dual antiplatelet therapy (aspirin 100 mg per day and clopidogrel 75 mg per day) for at least

1400

three days before the procedure.

1401

Intra-procedure: Intravenous anticoagulant such as heparin during the procedure.
85


```

### PDF page 86

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=86)

```text
BASIS

Number:2017YFC1307900

1402

Post-procedure: Aspirin 100 mg per day must be used for the entire duration of follow-up, and

1403

clopidogrel 75 mg per day or ticagrelor 90mg twice a day must be used for 90 days after

1404

randomization. After 90 days, whether to continue to take it will be assessed according to the

1405

patient's condition and the researcher's opinion. Atorvastatin will be taken 20mg-80mg/day for

1406

one year after enrollment; Whether to continue taking atorvastatin after one year will be

1407

assessed according to the patient's condition.

1408

Anesthesia strategy and arterial access

1409

The procedure should be performed under general anesthesia. Femoral artery access is

1410

recommended (radial artery access is allowed for patients with tortuosity of the aortic arch, or

1411

aorta).

1412

Procedure steps

1413

8.

A stable vascular access with a long sheath or guiding catheter (an intermediate catheter is

1414

recommended for participants with tortuous access), which should be placed as distal as

1415

possible, is suggested to provide adequate support for performing the balloon angioplasty.

1416

Collateral status assessment based on a whole brain DSA is recommended before balloon

1417

angioplasty according to the ASITN/SIR collateral flow grading system (poor collateral:

1418

ASITN/SIR < 3). 13

1419
1420

9.

An 0.014-inch microwire with a microcatheter (or not) passes through the lesion to reach
the distal branch of the target artery.

1421

10. A balloon (recommending the Neuro RX and Neuro LPS Intracranial Balloon Dilation

1422

Catheter [Sinomed Inc., Tianjin, China]) is navigated over the microwire to the lesion of the

1423

target artery.
86


```

### PDF page 87

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=87)

```text
BASIS

Number:2017YFC1307900

1424

Balloon size selection: the balloon length should cover the lesion completely and cover at

1425

least 2 mm beyond each end of the lesion. The balloon diameter is determined according to

1426

the physician’s opinion (submaximal angioplasty is suggested: balloon with a diameter no

1427

more than 70% of the proximal artery diameter).

1428

11. The balloon should be slowly inflated to the nominal pressure, and maintained for 10-30

1429

seconds before deflating slowly. This step can be repeated 2-3 times if the dilation effect of

1430

balloon angioplasty is not satisfactory. For patients with extremely severe stenosis, a

1431

relatively smaller balloon can be used for pre-dilation.

1432

12. Technical success: residual stenosis ≤ 50% of the proximal artery diameter with modified

1433

Thrombolysis in Cerebral Infarction (mTICI)14 of 3 grade without arterial dissection that

1434

impairs the distal blood flow.

1435

13. Rescue stent implantation is allowed when: (1) residual stenosis ≥ 70% after balloon

1436

dilation or the antegrade flow is unstable (mTICI < 2b); (2) arterial dissection impairing the

1437

distal blood flow (mTICI < 2b); (3) development of thrombosis or embolization that

1438

jeopardizes distal perfusion. Other measures such as intravenous/intra-arterial thrombolysis,

1439

infusion of GP IIb/IIIa inhibitors, are based on the physician's experience, which can be

1440

used alone or in combination with rescue stenting.

1441

14. A final DSA should be performed after 10–15 minutes of observation.

1442
1443

13. Aggressive medical management

1444

13.1 Antiplatelet treatment

87


```

### PDF page 88

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=88)

```text
BASIS

Number:2017YFC1307900

1445

AMM will be identical in both arms. All the necessary blood and imaging tests are collected in

1446

the screening period before randomization for the following management of risk factors. Both

1447

arms are prescribed with an AMM regime (includes aspirin 100 mg per day for the entire

1448

follow-up and clopidogrel 75mg per day for the first 90 days after enrollment). For the record:

1449

clopidogrel can be replaced with ticagrelor or cilostazol with appropriate dosage for patients

1450

with clopidogrel resistance (Platelet aggregation rate of adenosine diphosphate >40% or

1451

Loss-of-function alleles of CYP2C19 is detected).

1452

13.2 Risk factor management

1453

Neurologists and study investigators at each site will be responsible for the management of

1454

patient’s risk factors. They will receive training on risk factor management according to the

1455

Chinese Stroke Association guidelines for the clinical management of cerebrovascular

1456

disorders.15 All study investigators are regularly trained according to the BASIS protocol every

1457

6 months. If a patient fails to reach the target, a face-to-face follow-up with the local neurologist

1458

to modify their medical regime will be necessary.

1459

13.2.1 Primary risk factors

1460

Achieving target LDL cholesterol

1461

The baseline serum low-density lipoprotein cholesterol (LDL-c) level is recorded before

1462

enrollment. The target LDL-c level is < 1.8mmol/L or 70 mg/dl. If the patient’s LDL level is

1463

higher than the target level, he/she should modify the lipid-lowering drugs. Liver enzyme (AST /

1464

ALT) levels will be measured at the beginning of the study and at each visit point.

1465

Blood pressure management

88


```

### PDF page 89

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=89)

```text
BASIS

Number:2017YFC1307900

1466

The blood pressure will be checked at screening, randomization, discharge, 30 days, 90 days,

1467

180 days, 1 year, and the end of the trial. Patients may need to visit local sites for blood pressure

1468

measurement and modify their medical regime if necessary. The target blood pressure is no

1469

more than 140mmHg/90mmHg for patients without DM and no more than 130mmHg/80mmHg

1470

for patients with DM. Antihypertensive drugs include Angiotensin-converting enzyme inhibitor

1471

(ACEI), Angiotensin Receptor Blocker (ARB), beta-blocker, calcium channel antagonist (CCB),

1472

diuretic, vasodilator, etc.

1473

13.2.2 Secondary risk factors

1474

Non-HDL cholesterol

1475

The target level of non-HDL cholesterol is < 100 mg/dL. Non-HDL cholesterol includes

1476

low-density

1477

intermediate-density lipoproteins (IDL). When a larger statin dosage fails to lower the LDL

1478

level, or if the non-HDL cholesterol ≥ 100 mg/dL and triglycerides ≥ 200mg/dL, then other

1479

lipid-lowering drugs in addition to statin are recommended, such as ezetimibe or PCSK9

1480

inhibitors.

1481

Diabetes management

1482

The target of DM management is to achieve HbA1c < 7.0%. Fasting plasma glucose (FPG) and

1483

HbA1c levels will be measured at baseline, 30 days, 90 days, and 1 year.

1484

Lifestyle modification

1485

Smoking cessation: investigators at each site will evaluate the patient’s smoking status at each

1486

follow-up and encourage all subjects to quit smoking as soon as possible.

lipoproteins

(LDL),

very-low-density

89

lipoproteins

(VLDL),

and


```

### PDF page 90

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=90)

```text
BASIS

Number:2017YFC1307900

1487

Weight management: investigators at each site will evaluate the weight according to body

1488

mass index (BMI).

1489

Activity level: activity level for each patient is also assessed at each follow-up by trained

1490

investigators or coordinators, and moderate exercise of 30 minutes a day, three times per week is

1491

strongly recommended to all patients with athletic ability.

1492

13.2.3 Research drugs

1493

During the screening period of BASIS, clopidogrel will be provided free of charge for 3-5 days.

1494

After 90 days of enrollment, clopidogrel will also be provided free of charge. From enrollment

1495

to 1 year, atorvastatin required by patients will be provided free of charge, and other drugs will

1496

be purchased by the patients.

1497

At each visit point, the patient's compliance with treatment will be evaluated by counting the

1498

number of clopidogrel and atorvastatin.

1499

Patients with LDL > 1.8 mmol / L or > 70 mg / dL will be treated with atorvastatin. Whether to

1500

continue taking atorvastatin after 1 year will be assessed accordin to the patient's condition. If

1501

patients are taking other lipid-lowering drugs, patients are encouraged to switch to atorvastatin

1502

(not mandatory). For patients whose blood pressure does not reach the treatment goal,

1503

antihypertensive drugs will be given. Patients can choose to use but are not limited to the

1504

following antihypertensive drugs:

1505



Diuretic (Chlorthione 25mg)

1506



Angiotensin-converting enzyme inhibitor (ACEI) (Lisinopril 10mg or 40 mg)

1507



Angiotensin Receptor Blocker (ARB) (Candesartan 16mg or 32 mg),

1508



Beta-blocker (Atenolol 50mg or 100mg)
90


```

### PDF page 91

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=91)

```text
BASIS

Number:2017YFC1307900

1509



Calcium channel antagonist (CCB) (Felodipine 5mg or 10 mg)

1510



Central α agonist (clonidine 0.1mg)

1511



Vasodilator (hydralazine 50mg)

1512
1513

14. Patient and Researcher Benefit

1514

Patient benefit: Patients participating in this study will receive more systematic treatment and

1515

follow-up. Clopidogrel is provided free of charge during the screening period and 90 days of

1516

enrollment, and atorvastatin is provided free of charge from enrollment to 1 year. DSA is free at

1517

1-year follow-up. However, other related examinations and medications that need to be

1518

explained are not free, and the balloons used when they are randomly assigned to the

1519

experimental group are not free.

1520

Researchers benefit: Researchers participating in this study have the right to give priority to the

1521

use of scientific data to publish and sign scientific research work.

1522
1523

15. Follow-up

1524

All patients will be followed up to the primary endpoint of the study or the end of the study.

1525

Unless the patient does not agree to continue participating in the study, efforts will be made to

1526

obtain complete endpoint information (whether the patient is cured or dead). If the patient

1527

discontinued this study and received other treatments, such as stenting, but agreed to provide

1528

endpoint information, follow-up will continue.

1529

All participants will be followed up by the on-site neurologists at baseline, the day of DSA,

1530

discharge, 30±7 days, 90±7 days, 6 months±14 days, 1 year ±30 days, and up to 3 years (at 6
91


```

### PDF page 92

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=92)

```text
BASIS

Number:2017YFC1307900

1531

months intervals after 1 year). Follow-up visits will be conducted by telephone at 6-month and

1532

post-1-year periods and will be evaluated in person at other visits. At each follow-up visit, the

1533

participants’ medications, laboratory tests, risk factor management (as described above), and

1534

possible adverse events/endpoints are reviewed by an experienced neurologist and/or

1535

neurointerventionalist. All patients are required to undergo a neurovascular imaging

1536

examination including DSA, CTA or MRA at 1-year follow-up.

1537

Visit 1: Screening

1538



Signed informed consent

1539



Review inclusion/exclusion criteria

1540



Randomization-experimental group: balloon angioplasty+AMM; control group: AMM

1541



Medical history, concomitant medication, demographic data collection

1542



Ischemic stroke history record

1543



Vital signs, blood routine, urine routine, blood biochemistry, coagulation function

1544

examination

1545

Vital signs: Blood pressure, heart rate, respiration, body temperature；

1546

blood biochemistry: Renal function: creatinine, urea (or urea nitrogen), glucose, uric acid,

1547

total bilirubin, direct bilirubin, indirect bilirubin, lactate dehydrogenase, creatine kinase

1548

isoenzyme; liver function: alkaline phosphatase, glutamyl transpeptidase, aspartate

1549

aminotransferase, alanine aminotransferase; blood lipids: total cholesterol, low-density

1550

lipoprotein, high-density lipoprotein, triglyceride;

1551

Coagulation function: PT, APTT, TT, FIB, INR

1552



Fasting blood glucose, HbA1c (optional)
92


```

### PDF page 93

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=93)

```text
BASIS

Number:2017YFC1307900

1553



Pregnancy test

1554



Electrocardiogram

1555



DSA

1556



MRI/HRMRI (HRMRI is unnecessary; if MRI is not available, CT can replace MRI)

1557



CTP (anterior circulation sICAS)

1558



Patients’ smoking cessation, weight, and exercise data are collected. Smoking cessation:

1559

including whether to smoke and the number of daily cigarettes; weight: use the patient's

1560

weight and BMI to reflect the patient's weight control; exercise: weekly exercise frequency,

1561

each exercise duration

1562



mRS, NIHSS, MoCA, EQ-5D (MoCA is unnecessary)

1563



Platelet function test and/or CYPC219 genotype test according to the availability of the

1564

center, this item is unnecessary

1565



TCD (recommend but not necessary)

1566



Research drug distribution: Clopidogrel (only for patients who are enrollled in BASIS)

1567



Aspirin and clopidogrel medication orders

1568



Concomitant medication collection

1569



AE, SAE and endpoint observation

1570

Visit 2: Treatment

1571



Treatment according to the randomization scheme

1572



Concomitant medication collection

1573



Vital signs

93


```

### PDF page 94

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=94)

```text
BASIS

1574



Number:2017YFC1307900

Research drug distribution and recovery (Randomly successful patients are distributed 30

1575

days follow-up research drug; Randomly failed patients recovered research drugs issued

1576

during the screening period; randomly successful patients are given clopidogrel and

1577

atorvastatin)

1578



Aspirin, clopidogrel and atorvastatin medication orders

1579



Patient compliance survey

1580



AE, SAE and endpoint observation

1581

Visit 3: Discharge

1582



Concomitant medication collection

1583



Vital signs

1584



Blood routine, urine routine, blood biochemistry (optional)

1585



NIHSS

1586



Patients’ smoking cessation, weight, and exercise data are collected

1587



Patient compliance survey

1588



The disease treatment-related cost information collection

1589



AE, SAE and endpoint observation

1590

Visit 4: 30±7 days after enrollment

1591



Concomitant medication collection

1592



Vital signs, blood routine, urine routine, blood biochemistry

1593



Fasting blood glucose, HbA1c (optional)

1594



Patients’ smoking cessation, weight, and exercise are collected

1595



mRS
94


```

### PDF page 95

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=95)

```text
BASIS

Number:2017YFC1307900

1596



Research drug distribution: clopidogrel and atorvastatin

1597



Aspirin, clopidogrel and atorvastatin calcium orders

1598



Patient compliance survey

1599



The disease treatment-related cost information collection

1600



AE, SAE and endpoint observation

1601

Visit 5: 90±7 days after enrollment

1602



Concomitant medication collection

1603



Vital signs, blood routine, urine routine, blood biochemistry

1604



Fasting blood glucose, HbA1c (optional)

1605



CTP (optional)

1606



Patients’ smoking cessation, weight, and exercise data are collected

1607



mRS and NIHSS

1608



Research drug distribution: atorvastatin

1609



Aspirin and atorvastatin medication orders

1610



Patient compliance survey

1611



The disease treatment-related cost information collection

1612



AE, SAE and endpoint observation

1613

Visit 6: 6 months±14 days after enrollment (interview by telephone)

1614



Concomitant medication collection

1615



Patients’ smoking cessation, weight, and exercise data are collected

1616



mRS

1617



AE, SAE and endpoint observation
95


```

### PDF page 96

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=96)

```text
BASIS

Number:2017YFC1307900

1618

Visit 7: 1 year±30 days after enrollment

1619



Concomitant medication collection

1620



Vital signs, blood routine, urine routine, blood biochemistry

1621



Fasting blood glucose, HbA1c (optional)

1622



MRI/HRMRI (HRMRI is unnecessary; if MRI is not available, CT can replace MRI)

1623



CTP, DSA (DSA is necessary and CTP is unnecessary)

1624



Patients’ smoking cessation, weight, and exercise data are collected

1625



mRS, NIHSS, MoCA, EQ-5D (MoCA is unnecessary)

1626



TCD (recommend but not necessary)

1627



Research drug recovery: atorvastatin

1628



Patient compliance survey

1629



Follow-up aspirin medication orders

1630



The disease treatment-related cost information collection

1631



AE, SAE and endpoint observation

1632

Follow-up after 1 year: every 6 months ± 30 days after 1-year enrollment

1633

Follow-up every 6 months (visit 8, visit 9, visit 10, visit 11, visit 9, and visit 11 require patients

1634

to undergo face-to-face follow-up).

1635

Visit by telephone:

1636



Patients’ smoking cessation, weight, and exercise are collected

1637



Follow-up aspirin medication

1638



AE, SAE and endpoint observation

1639

Face-to-face visit:
96


```

## Layout supplement: complete visit-by-assessment schedule PDF page73

```text
               BASIS                                                                                                                      Number:2017YFC1307900



1140           3. Schedule of assessments
1141
                                                                                                                      Visit 6                       Follow up 1y to 3y
                   Visit                         Visit 1    Visit 2     Visit 3         Visit 4   Visit 5                                 Visit 7
                                                                                                                Telephone interview                 (Visit 8,9,10,11)

                                                 Baseline   Angiogram                                                                                    6       months
   Assessment                                                           Discharge   30d±7d            90d±7 d    6 mo±14 d            1y±30 d
                                                 15d～0 d    0d                                                                                           intervals
       Informed consent                      X
       Inclusion/exclusion criteria check X
       History and physical examination X
       Vital signs1                          X              X           X           X             X                                   X
                               2
       Blood laboratory test       and
                                             X                          X           X             X                                   X
       urine routine test

       Coagulation function3                 X
       FBG, HbA1c4                           X                                      X             X                                   X

       Platelet aggregation test and/or
                                        X
       CYPC219 genotype test5

       ECG                                   X
       MRI/CT                                X                                                                                        X
           6
       CTP                                       X9                                               X                                         X
       DSA/CTA/MRA                           X9                                                                                             X
                                         7
       Life-style modification review        X                          X           X             X             X                     X             X

       mRS                                   X                                      X             X             X                     X             X
       NIHSS (neurological examination) X                               X                         X                                   X
       EQ-5D
       examination)                          X                                                                                        X             X
               5
       MoCA                                  X                                                                                        X             X
       HR-VWI,TCD5                           X                                                                                        X

       Medication review and patient
                                                            X           X           X             X                                   X
       compliance survey

       AE、SAE and endpoints8                 X              X           X           X             X             X                     X             X8
1142           1. Vital signs: blood pressure, heart rate, respiration rate, body temperature;
1143           2. Blood laboratory test includes blood routine and biochemistry examinations, hepatic and renal function tests.
1144           3. Coagulation function: PT, APTT, TT, FIB, INR;
1145           4. HbA1c is an optional test, but is recommended for patients with Diabetes Mellitus.
1146           5. Platelet aggregation test, CYPC219 genotype test, MoCA, HR-VWI and TCD test are optional according
1147           to the availability of the test at the center;
1148           6. CTP is an optional test, but is recommended for patients with hemodynamic compromise, poor collateral
1149           or perforator stroke.
1150           7. Life-style modification review: including whether to smoke and the number of cigarettes per day; Weight:
1151           reflect the patient's weight control through the patient's weight and BMI; Exercise: number of exercises per
1152           week and duration of each exercise.
1153           8. After one year of follow-up, follow-up will focus on AE, SAE and endpoint events;
1154
1155           Abbreviations: FBG, fasting blood glucose; HbA1c, Glycosylated Hemoglobin; ECG, electrocardiograph;
1156           MRI, magnetic resonance imaging; CT, computerized tomography; CTP, CT perfusion; DSA, digital
1157           subtraction angiography; CTA, computerized tomography angiography; MRA, magnetic resonance
1158           angiography; digital subtraction angiography (DSA), computerized tomography angiography (CTA), or
1159           magnetic resonance angiography (MRA); mRS, modified Rankin scale; EQ-5D, quality-of-life EuroQol-5
                                                                                         73

```


<!-- END support_doc003_pp065-096.md -->

---


<!-- BEGIN support_doc003_pp097-128.md -->

# DOC-003 support quantitative evidence: PDF pages 97–128

Status: COMPLETE. Exact disjoint scope: 32 PDF pages, 97 through128 inclusive. Document role: PLAN. Pages97–123 continue final protocol; pages124–126 give protocol amendment history; pages127–128 begin original SAP Version1.0 dated December27,2018. The source table of contents' approximate component ranges are not used to relabel actual page content. All32 pages reusable-backed; fresh-required units0; mapped units32; scientific gaps0. No OCR performed. Reused engine: legacy native/layout extraction and retained PNG renders, version unavailable. Sources and assets unchanged.

Reusable native/layout assets: `.ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-N.native.txt` and `page-N.layout.txt` for all assigned pages. Retained images `rendered-108.png`, `rendered-109.png`, `rendered-110.png` were inspected visually to map the embedded device diagrams/tables absent from native text. Every page's full native transcription aid follows the authored map. No legacy candidate or scientific conclusion was used.

## Complete page coverage

| PDF page | Coverage | Quantitative/statistical evidence and matching key |
|---|---|---|
| 97 | COMPLETE | Follow-up face-to-face mRS/MoCA/EQ-5D; restenosis≥70% with transient ischemia/stroke triggers revascularization discussion, <70% not recommended; endpoints reported48h, adjudication7days. |
| 98 | COMPLETE | Three-member endpoint committee: two independent assessments, third deciding vote; AE/SAE/UADE definitions; complication inventory begins. |
| 99 | COMPLETE | Complication list continues; adverse-event collection consent–study end including treatment discontinuations, SAE report24h; no additional inferential rule. |
| 100 | COMPLETE | Safety-event management including acute occlusion usually within30min of angioplasty; no trial-result estimate. |
| 101 | COMPLETE | Hyperperfusion management; independent blinded core imaging review, experts >10 years experience. No additional statistical result. |
| 102 | COMPLETE | Full primary and secondary statistical models,95% CIs, ITT and sensitivity populations, multiplicity statement, software; detailed below. |
| 103 | COMPLETE | Sample size and all11 subgroup variables/cutoffs; below. |
| 104 | COMPLETE | Annual DSMB meetings, steering twice yearly, weekly progress monitoring, blinded CEC; study collaboration table. No formal numerical stopping boundary in passage. |
| 105 | COMPLETE | Collaboration/DSMB/AE/steering personnel tables. No result-relevant numeric relationship or analysis method. |
| 106 | COMPLETE | Committee continuation; clopidogrel free screening3–5 days and enrollment90 days, discretionary thereafter; atorvastatin1 year. |
| 107 | COMPLETE | Drug distribution responsibilities; Neuro RX device:145cm working length, wire<0.014inch, catheter inner diameter≥5F(0.056inch), registration metadata. |
| 108 | COMPLETE | Neuro RX device schematic and complete diameter×length availability table visually inspected; guidewire exit24cm from tip,2F proximal/3F distal shaft. Neuro LPS materials/approval metadata. |
| 109 | COMPLETE | Neuro LPS diagram visually inspected: catheter length1550±100mm; D1 expanded diameter, L2 balloon effective length, L catheter effective length; nine parts, markers90%platinum/10%iridium. |
| 110 | COMPLETE | Neuro LPS complete diameter×length table visually inspected; device administration. |
| 111 | COMPLETE | Regulatory/ethics protocol/version approval, amendments submitted, annual progress report. No result-relevant quantitative/statistical element. |
| 112 | COMPLETE | References1–13, contextual study citations only; no newly stated BASIS result or statistical method. |
| 113 | COMPLETE | References14–17; appendix collateral scale begins grade0. |
| 114 | COMPLETE | ASITN/SIR scale grades1–4; complete scale defined below. |
| 115 | COMPLETE | mRS full ordinal definition,0–5 plus6death, higher worse; below. |
| 116 | COMPLETE | NIHSS range0–42 higher worse; LOC1a scores0–3, LOC questions1b0–2. |
| 117 | COMPLETE | NIHSS LOC commands1c0–2; gaze0–2; visual0–3; facial palsy0–3 starts. |
| 118 | COMPLETE | NIHSS facial continuation, arm left/right0–4, leg left/right0–4, ataxia0–2; arm90°/45°10sec, leg30°5sec. |
| 119 | COMPLETE | NIHSS sensory0–2, language0–3, dysarthria0–2 begins; coma coding rules. |
| 120 | COMPLETE | NIHSS dysarthria continuation/untestable flag, extinction/inattention0–2. |
| 121 | COMPLETE | EQ-5D-5L five domains×five response levels; present-day measurement. |
| 122 | COMPLETE | EQ visual health scale0–100,100best imaginable health,0worst. |
| 123 | COMPLETE | mTICI grades0,1,2a,2b,3 and reperfusion definitions, below. |
| 124 | COMPLETE | Protocol versions2.0/2.1/2.2/2.3 dates; V2.1 stroke interval/artery clarification; V2.2 exclusion criteria starts. |
| 125 | COMPLETE | V2.2 exclusion continuation and newly added24-/36-month outcomes. |
| 126 | COMPLETE | V2.2 sample-size amendment802→512, control15%/balloon7%, forgoing interim analysis rationale; V2.3 adds30-day stroke/death and1-year revascularization secondary outcomes. |
| 127 | COMPLETE | Original SAP coverVersion1.0 December27,2018. No scientific-method text on cover. |
| 128 | COMPLETE | Original SAP contents: primary/secondary/safety, planned/interim, sample size, ITT/PPS/ATS/SS, subgroups/multiplicity, withdrawal/missingness/event rates/time-to-event. No actual method specification on this contents page. |

## Reconstructed relationships

### DOC003-FP-STATISTICS: primary and secondary estimands, models, populations and multiplicity

[Final protocol statistical section](../../../joi240088supp2_prod_1746815064.36071.pdf#page=102), printed lines1751–1761: composite primary-event rates with95% CIs by Kaplan–Meier; log-rank treatment comparison; treatment hazard ratio and95% CI via Cox proportional hazards regression. Secondary time-to-event outcomes also Kaplan–Meier/Cox; common odds ratios of mRS via ordinal logistic regression. Secondary confidence-interval widths unadjusted for multiplicity. Main analysis intention-to-treat; per-protocol and as-treated sensitivity analyses. SAS9.4. Detailed missing-data imputation and subgroup analyses delegated to SAP. No covariate list, imputation algorithm or numerical population definition is supplied on this page; no method is assumed. Main-paper matching keys: primary KM event risk, Cox HR/CI, log-rank P, secondary time-to-event HR, mRS common OR, ITT/PP/as-treated analyses, secondary multiplicity disclosure.

### DOC003-FP-SIZE: power inputs

[P103 lines1763–1769](../../../joi240088supp2_prod_1746815064.36071.pdf#page=103): control primary-event rate15%, balloon7%, absolute difference8%, total512=256/arm,80% power, one-sided alpha2.5%,10% dropout. Rate assumptions attributed to supplied historical studies and investigator experience. No formula on this page. Match to p69 synopsis and main-paper sample-size section. Protocol amendment p126 separately documents802→512 and dropping interim analysis, so the revised design is explicitly disclosed in PLAN content.

### DOC003-FP-SUBGROUPS: complete prespecified primary-outcome subgroup list

[P103 lines1770–1782](../../../joi240088supp2_prod_1746815064.36071.pdf#page=103): age<65 vs≥65; sex men/women; hypertension yes/no; diabetes yes/no; smoking yes/no; baseline eGFR<60 vs≥60 mL/min/1.73m²; target stenosis<80% vs≥80%; BMI<25 vs25–30 vs≥30 kg/m²; hypoperfusion yes/no; lesion anterior/posterior circulation; mechanism ischemic stroke/TIA. These11 variables are all retained. No interaction model/P-value rule or adjusted subgroup covariates in this passage. Match to main-paper subgroup plot and supplement subgroup estimates after defining categories from supplied report, without assuming exact matching where labels differ.

### DOC003-FP-ADJUDICATION-SAFETY: endpoint processing and collection

P97 endpoint types: target-vessel hemorrhagic/ischemic stroke, death, target-vessel revascularization; possible primary event reported48h, adjudication7days. P98 committee3members, two independent assessments and decisive third vote. SAE definition includes death, life threat, hospitalization/prolongation, serious disability or intervention to prevent those outcomes. P99 AE/SAE collection begins consent and continues to study end, including early treatment discontinuation; reportSAE24h. P101 blinded core review; p104 blinded CEC, annual DSMB. These determine safety/endpoint ascertainment and matching windows, not event counts. P97 restenosis≥70% after recurrent ischemia prompts revascularization review, <70% does not; this is distinct from restenosis outcome definition >70% or30%increase elsewhere in final protocol.

### DOC003-FP-VERSIONS: documented amendments and prospective-status context

[P124](../../../joi240088supp2_prod_1746815064.36071.pdf#page=124) explicitly names original protocolV2.0-20180625, amendmentV2.1-20200414, amendmentV2.2-20211222, finalV2.3-20220328.

V2.1 April14,2020: changes stroke-onset-to-enrollment inclusion interval to14–90days (TIA<90days), reflecting cited2-week timing rationale; clarifies ICA C4–C7/MCA M1/VA V4/BA locations. V2.2 December22,2021: detailed supplying-artery exclusion>50%, nonlesion extracranial>70%, balanced bilateral VA>70%, dominant-VA exceptions (pp124–125); adds24- and36-month target-territory stroke/all-cause death, outside-territory stroke, mRS, stroke/MI/vascular-death secondary outcomes (p125). P126: sample size802→512; newer assumed medical15%/balloon7%, enrollment difficulty from COVID-19 and insufficient funding, DSMB recommended forgoing interim analysis. V2.3 March28,2022 adds secondary any stroke/all-cause death within30days after enrollment or qualifying-lesion balloon angioplasty during follow-up and target-artery revascularization within12months (p126). Original SAP starts actualPDFp127 and isVersion1.0 December27,2018. Preserve each plan version when matching prospective versus reported claims.

### DOC003-FP-SCALES: full outcome and procedure scales

ASITN/SIR(p113–114):0 no collaterals;1 slow peripheral collaterals with persistent incomplete ischemic-site supply;2 rapid peripheral collaterals supplying only part of ischemic territory;3 slow but complete flow by late venous phase;4 complete rapid retrograde flow entire ischemic vascular territory. Poor collateral criterion<3 from earlier procedure section matches this scale.

mRS(p115):0 no symptoms;1 symptoms without disability/no lifestyle interference;2 slight disability/lifestyle restriction but independent self-care;3 moderate disability/restricted lifestyle, not fully independent;4 moderately severe disability/prevents independent existence without constant attention;5 severe disability, fully dependent/constant day-and-night attention;6 death. Higher worse, ordinal0–5 with6 added for death. Match to main-paper ordinal regression/common OR, functional independence cutoffs and survival handling.

NIHSS(pp116–120):0–42 higher worse. Components:1aLOC0–3;1bquestions0–2;1ccommands0–2; gaze0–2; visual0–3; facial0–3; left/right arm each0–4; left/right leg each0–4; ataxia0–2; sensory0–2; language0–3; dysarthria0–2; extinction/inattention0–2. Arm hold90°seated/45°supine10seconds; leg30°5seconds. ComaLOC1a=3 automatically sensory2 and language3. Untestable flags for arm/leg/ataxia with amputation or joint fusion, dysarthria intubation/physical barrier; extinction always testable. Detailed scoring definitions retained in complete layout transcription supplement below.

EQ-5D-5L(p121): mobility, self-care, usual activities, pain/discomfort, anxiety/depression; each5levels increasing impairment, response refers to healthTODAY. EQ visual scale(p122)0worst imaginable/100best imaginable health. No index-weighting formula supplied here.

mTICI(p123):0 no perfusion;1 flow past initial occlusion with limited/little/slow distal filling;2a antegrade reperfusion<half target ischemic territory;2b>half;3 complete antegrade reperfusion without distal branch occlusion. Match to technical success/rescue-stenting rule.

### DOC003-FP-DEVICE: visually completed device table and diagrams

P108 NeuroRX diagram:2F proximal shaft,3F distal shaft, rapid-exchange guidewire exit, semicompliant balloon, hydrophilic coating, laser-bonded tip. Guidewire exit24cm from far tip. The diameter rows in displayed units are1.50,2.00,2.25,2.50,2.75,3.00,3.25,3.50,4.00; length columns6,10,12,15,20,25mm. Available diameter1.50 at10/15/20mm;2.00 and2.25 at10/15/20/25mm; all diameters2.50 through4.00 at all6lengths. Native table values absent, completed from retained render. P107 working length145cm, guidewire<0.014inch, catheter inner diameter≥5F(0.056inch).

P109 NeuroLPS schematic L=1550±100mm, D1 expanded-balloon diameter, L2 effective balloon length, L catheter effective length. Two markers90%platinum/10%iridium. P110 diameter rows1.50,2.00,2.25,2.50,2.75,3.00,3.25,3.50,4.00; length columns8,10,12,15,20mm; all45diameter/length combinations marked available. Device dimensions are operational context, not trial effect estimates. No quantitative table or image remains unmapped.

## Complete per-page native transcription aids

These retained source-linked aids preserve every detailed line, table, footnote, dose and contextual quantity; direct PDF remains final authority.

### PDF page 97

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=97)

```text
BASIS

Number:2017YFC1307900

1640



Patients’ smoking cessation, weight, and exercise data are collected

1641



mRS, MoCA, EQ-5D (MoCA is unnecessary)

1642



Follow-up aspirin and atorvastatin medication orders

1643



AE, SAE and endpoint observation.

1644

16. Management of (transient) ischemic events during follow-up

1645

If any patient in each group had potential clinical neurological events (transient cerebral

1646

ischemia, ischemic stroke), neurologists would determine whether to perform a vessel imaging

1647

examination, including DSA. The most effective treatment for ICAS patients with transient

1648

cerebral ischemia or ischemic stroke is unknown. The researchers determine the best treatment

1649

according to the patient's condition and actively control the risk factors.

1650

If patients in the experimental group experienced transient cerebral ischemia or ischemic

1651

stroke, accompanied by restenosis ≥ 70 % diagnosed by DSA, investigators composed of

1652

neurologists and neurointerventional experts will give advice on whether they should next

1653

undergo revascularization or medical management alone. Revascularization is not recommended

1654

for patients with restenosis < 70 %.

1655

17. Assessment of endpoint and adverse events (AEs)

1656

17.1 Endpoint event assessment

1657

The endpoint events include target vessel haemorrhagic stroke, ischemic stroke, death, and

1658

target vessel revascularization. If a patient has a potential primary endpoint event, the researcher

1659

must report to a third-party monitoring company project team within 48 hours, including the

1660

patient's complete medical records. The project team will submit the patient's data to the event

1661

arbitration committee, and the event arbitration committee will complete the arbitration within 7
97


```

### PDF page 98

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=98)

```text
BASIS

Number:2017YFC1307900

1662

days. The endpoint event arbitration committee is composed of three members. First, two

1663

members use back-to-back arbitration. If the evaluation opinions are inconsistent, a third

1664

evaluation expert will cast a decisive vote.

1665

17.2 AEs assessment

1666

An AE is the presence of any unexpected medical condition during or after being treated with

1667

medical devices. It includes symptoms, signs, or abnormal laboratory parameters that can be

1668

unrelated to treatment. An AE that fulfills at least one of the following criteria is classified as a

1669

severe AE(SAE): AE that results in death; is life-threatening; requires/prolongs inpatient

1670

hospitalization; results in serious disability; or requires medical intervention to prevent one of

1671

the above-mentioned outcomes. If a potential endpoint occurs, the committee board meeting will

1672

be convened to evaluate whether such an event can be categorized as the primary endpoint.

1673

Unanticipated adverse device effect (UADE): Any serious adverse reaction affecting health or

1674

safety, or any life-threatening event or death related to (caused by) the device. The nature,

1675

severity, or degree of such serious adverse reactions, life-threatening events or deaths, or other

1676

unexpected device-related serious events involving patient rights, safety, or welfare, were not

1677

previously identified in the study plan.

1678

The following events are considered as possible (expected) complications of balloon

1679

angioplasty:
Vasospasm

Neurological symptoms

Coagulation disorders

Dissection

Pseudoaneurysm

Death

Vessel occlusion

Renal insufficiency/failure

Vessel perforation

Respiratory
hematoma

embolism (air, tissue, thrombus or
foreign body)
distress/failure Pain, and/or puncture site infection

98


```

### PDF page 99

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=99)

```text
BASIS

Number:2017YFC1307900

Vessel rupture

Seizure

Hemorrhage

Vessel embolism

Infection

Hypertension

Stroke

Drug reaction of antiplatelets

Hypotension

Transient ischemic attack

Syncope

1680
1681

17.3 SAE record and report

1682

The collection time of adverse events and serious adverse events in the study begins with

1683

signing the informed consent, across the study period, until the end of the study. SAEs of

1684

patients who discontinued treatment in advance should also be recorded.

1685

When any SAE occurs during the study, the researcher should immediately treat appropriately

1686

for the patient, and report in writing within 24 hours to the clinical trial institution, ethics

1687

committee, and sponsor (Beijing Tiantan Hospital, Capital Medical University). For death

1688

events, clinical trial institutions and researchers should provide the ethics committee and

1689

sponsors (Beijing Tiantan Hospital, Capital Medical University) with all the required

1690

information.

1691

17.4 Prediction of AEs and countermeasures

1692

AEs that may occur during the procedures include, but are not limited to:

1693

Thromboembolic events

1694

The possible causes include no anticoagulation or insufficient anticoagulation, insufficient

1695

antiplatelet aggregation treatment before and after the procedure or aspirin resistance.

1696

Anticoagulation and antiplatelet aggregation should be standardized. If embolization occurs in

1697

the important vessels, it should be handled by a professional doctor per the patient's condition.
99


```

### PDF page 100

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=100)

```text
BASIS

Number:2017YFC1307900

1698

Cerebral vasospasm

1699

Cerebral vasospasm can be caused by subarachnoid hemorrhage (SAH), or by stimulation of

1700

endovascular catheters and guidewires. If vasospasm occurs, the professional doctor will give

1701

symptomatic treatment per the patient's condition.

1702

Acute vessel occlusion

1703

Possible causes: intimal injury, platelet aggregation, thrombosis, etc., usually occur within 30

1704

minutes after balloon angioplasty or are related to intimal avulsion. Preventive measures:

1705

including aspirin and ticlid or clopidogrel antiplatelet drugs can effectively reduce acute

1706

thrombosis events. Under strict preoprocedure antiplatelet therapy and intraprocedure

1707

anticoagulation, acute vessel occlusion events can be avoided.

1708

Treatment measures: Once acute vessel occlusion occurs, reasonable treatment should be

1709

performed immediately for the cause of occlusion. Thrombolysis can be performed in patients

1710

with acute thrombosis.

1711

Thrombosis and plaque shedding

1712

It is mainly due to plaque fragmentation and shedding caused by squeezing plaque during

1713

balloon dilatation, and sometimes thrombosis caused by catheter and guide wire. The use of

1714

brain protection devices and intraprocedure anticoagulation are the basic measures to prevent

1715

this event.

1716

Vessel rupture

1717

Such complications can directly lead to death. When balloon angioplasty is performed at some

1718

sites, the selected balloon is preferably slightly smaller than the diameter of the target vessel.

100


```

### PDF page 101

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=101)

```text
BASIS

Number:2017YFC1307900

1719

Once vessel rupture occurs, symptomatic treatment should be performed immediately by a

1720

professional doctor.

1721

Cerebral hyperperfusion syndrome

1722

For severe stenotic lesions, the autoregulation ability of distal vessels decreases due to long-term

1723

ischemia. The sudden expansion of the lesion site significantly increases the blood flow. The

1724

distal vessels, especially the cortical arteries, cannot immediately adapt to this sudden increase

1725

in blood flow and passively expand, resulting in cerebral hyperperfusion syndrome. The main

1726

clinical presentations include headache, nausea, vomiting, epilepsy, and disturbance of

1727

consciousness. Some patients can suffer intracranial hemorrhage. The possibility of this

1728

occurrence should be fully recognized before the procedure, and blood pressure should be

1729

appropriately reduced during and after the procedure to prevent this event. If postoperative

1730

cerebral hyperperfusion syndrome occurs, symptomatic treatment should be performed

1731

according to the patient's condition (such as antihypertensives, analgesics, antiepileptic drugs,

1732

hyperosmolar agent to reduce intracranial pressure, surgical treatment of cerebral hemorrhage,

1733

etc.).

1734
1735

18. Core Laboratory

1736

Imaging will be adjudicated by an independent imaging core lab (China National Clinical

1737

Research Center for Neurological Diseases, Tiantan Neuroimaging Center of Excellence). All of

1738

the blood samples and imaging data will be collected, transported, and preserved according to

1739

the study protocol. Imaging will be blind (clinical features and treatment options for patients),

1740

reviewed by experienced MRI experts and DSA experts (over 10-year working experience).
101


```

### PDF page 102

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=102)

```text
BASIS

Number:2017YFC1307900

1741
1742

19. Quality control

1743

To ensure that the collected data is concordant with the protocol, each sub-center of the BASIS

1744

trial will be regularly scrutinized, and by comparing data in the Electronic Data Capture System

1745

(EDC) and data in the original documents (case report form [CRF] vs. source documents) to

1746

confirm data consistency. If a patient develops an AE/severe AE or completed a 1-year

1747

observation after receiving treatment from non-study sites, duplicate copies of the medical

1748

documents will be collected for future reviews.

1749
1750

20. Statistical Analysis

1751

The composite event rates and corresponding 95% CIs of the primary outcome in the two

1752

treatment groups will be estimated by Kaplan-Meier survival analysis and compared by log-rank

1753

test. Hazard ratio between the two groups and its 95% CI will be calculated using a Cox

1754

proportional hazards regression model. Time-to-event endpoints of the secondary outcomes will

1755

also be analyzed using Kaplan-Meier survival analysis and Cox regression, and common odds

1756

ratios of mRS will be estimated using ordinal logistic regression. The widths of the intervals will

1757

not be adjusted for multiplicity for secondary outcomes. The main analysis of this study will be

1758

conducted based on the intention-to-treat principle, and per protocol analysis and as treated

1759

analysis will also be conducted as sensitivity analyses. All analyses will be performed using

1760

SAS software, Version 9.4 (SAS Institute). Detailed statistical methods, missing data imputation

1761

and subgroup analyses are described in the statistical analysis plan.

1762

20.1 Sample size
102


```

### PDF page 103

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=103)

```text
BASIS

Number:2017YFC1307900

1763

According to the VISSIT trial and a previous randomized trial in China, the composite event rate

1764

of the primary outcome in the medical group is anticipated to be 15%.4,16 For the balloon

1765

angioplasty group, we assume a 7% rate of the primary outcome based on studies of angioplasty

1766

without stenting9,17 and the investigator’s clinical practice experience in China. As a result, the

1767

sample size will require detection of an absolute difference of 8% between the two groups. A

1768

total of 512 patients (256 per group) will be enrollled considering an 80% statistical power at a

1769

one-sidedαof 2.5% and a 10% dropout rate.

1770

20.2 Subgroup analysis

1771

Subgroup analyses on the primary outcome will be performed in the following subgroups:

1772



Age, <65 years old vs. ≥ 65 years old

1773



Sex, men vs. women

1774



Hypertension, yes vs. no

1775



Diabetes, yes vs. no

1776



Smoking, yes vs. no

1777



Baseline renal function, eGFR <60 ml/min/1.73m2 vs. eGFR≥60 ml/min/1.73m2

1778



Target vessel stenosis degree, <80%vs. ≥80%

1779



BMI, <25 Kg/m2 vs. 25-30 Kg/m2vs. ≥30 Kg/m2

1780



Hypoperfusion, yes vs. no

1781



Lesion location, anterior circulation vs. posterior circulation

1782



The mechanism, ischemic stroke vs. TIA

1783
1784

21. Data Safety and Monitoring Board
103


```

### PDF page 104

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=104)

```text
BASIS

Number:2017YFC1307900

1785

The data safety and monitoring board (DSMB) is comprised of academic members and an

1786

independent statistician. The DSMB is scheduled to have meetings annually to review the study

1787

progress to guarantee the trial is in accordance with the standards of ethics and to ensure the

1788

safety of all enrollled patients. After each DSMB meeting, the DSMB members will generate a

1789

report including all recommendations, and hand it to the steering committee immediately after

1790

the meeting.

1791
1792

22. Study organization

1793

Twice a year, the steering committee will meet to oversee the trial and provide strategic

1794

guidance. Periodically, the clinical research team of the leading center will meet online with the

1795

project team of the clinical research organization to review the trial progress and data

1796

monitoring each week. An independent clinical events adjudication committee (CEC) will

1797

ensure that defined outcomes are reported and judged uniformly using the same definition by

1798

experts who are blinded to the treatment status. (Table 1)

1799

Table 1. Collaboration team of trial and Study Committee
Collaboration
team

Unit or Hospital name

Sponsor
CRO
Statistical
analysis
Imaging core
lab

Beijing Tian Tan Hospital, Capital Medical University
Beijing Jingchengtong Medicine Technology Co., Ltd.
Department of Biostatistics, Peking University Clinical
Research Institute
China National Clinical Research Center for
Neurological Diseases, Tiantan Neuroimaging Center of
Excellence
China National Clinical Research Center for
Neurological Diseases, Tiantan Neuroimaging Center of
Excellence
Tangdu Hospital of Air Force Medical University

CEC team

104

Investigator Name
NA
NA
NA
Jing Jing

Nan Qi

Zhenwei Zhao


```

### PDF page 105

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=105)

```text
BASIS

Collaboration
team

Number:2017YFC1307900

Unit or Hospital name

Investigator Name

Beijing Tian Tan Hospital, Capital Medical University

Kehui Dong

The First Affiliated Hospital of Harbin Medical
University
People's Liberation Army Air Force General Hospital
Strategic Support Force Specialty Medical Center
China National Clinical Research Center for
Neurological Diseases
Beijing Tian Tan Hospital, Capital Medical University
Beijing Tian Tan Hospital, Capital Medical University
Beijing Tian Tan Hospital, Capital Medical University
Beijing Tian Tan Hospital, Capital Medical University

Huaizhang Shi

Beijing Tian Tan Hospital, Capital Medical University

Yilong Wang

Beijing Tian Tan Hospital, Capital Medical University

Yongjun Wang

Comprehensive Stroke Center, University of California,
Irvine, USA
Beijing Tian Tan Hospital, Capital Medical University
Neurovascular Imaging Research Core and Department
of Neurology, University of California, USA
Department of Neurosurgery, University Hospitals
Cleveland Medical Center/ Case Western Reserve
Univeristy School of Medicine, Ohio, USA

Wengui Yu

Cooperation
team

Unit or Hospital name

Investigator Name

Sponsor
CRO
Statistical
analysis
Imaging core
lab

Beijing Tian Tan Hospital, Capital Medical University
Beijing Jingchengtong Medicine Technology Co., Ltd.
Medical Statistics Office, Peking University First
Hospital, Beijing, China
China National Clinical Research Center for
Neurological Diseases, Tiantan Neuroimaging Center of
Excellence
Tangdu Hospital of Air Force Medical University
Beijing Tian Tan Hospital, Capital Medical University
The First Affiliated Hospital of Harbin Medical
University
People's Liberation Army Air Force General Hospital
Strategic Support Force Specialty Medical Center
Beijing Tian Tan Hospital, Capital Medical University
Beijing Tian Tan Hospital, Capital Medical University
Beijing Tian Tan Hospital, Capital Medical University
Beijing Tian Tan Hospital, Capital Medical University

NA
NA
NA

DSMB

AE
Committee
Steering
Committee

CEC team

DSMB

AE
Committee

105

Jin Shi
Yiling Cai
Yuesong Pan
Xuan Sun
Yiming Deng
Ning Ma
Zhongrong Miao

Xingquan Zhao
David S Liebeskind
Sepideh Amin-Hanjani

Jing Jing
Nan Qi
Zhenwei Zhao
Kehui Dong
Huaizhang Shi
Jin Shi
Yiling Cai
Yuesong Pan
Xuan Sun
Yiming Deng
Ning Ma


```

### PDF page 106

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=106)

```text
BASIS

Collaboration
team

Number:2017YFC1307900

Unit or Hospital name

Technology
Steering
Committee

Strategic Support Force Specialty Medical Center
Xuanwu Hospital Capital Medical University
Aerospace Central Hospital
Beijing Chaoyang Emergency Rescue Hospital of
Integrated Traditional Chinese and Western Medicine
The Sixth Medical Center of the General Hospital of the
People's Liberation Army
Chairs
of Beijing Tian Tan Hospital, Capital Medical University
Steering
Beijing Tian Tan Hospital, Capital Medical University
Committee
Comprehensive Stroke Center, University of California,
Irvine, USA

Investigator Name
Yiling Cai
Yabing Wang
Peifu Wang
Qiang Zhang
Feng Qiu
Zhongrong Miao
Yilong Wang
Wengui Yu

1800

23. Research drug supply and responsibilities division

1801

Clopidogrel will be provided to the patients for free during the screening period of 3-5 days and

1802

the enrollment period of 90 days. Whether to continue taking clopidogrel after 90 days will be

1803

assessed according to the patient's condition, and the patient needs to buy them after 90 days.

1804

Atorvastatin (Ale) are also free for 1 year. Whether to continue taking atorvastatin after 1

1805

year will be assessed per the patient's condition, and patients will need to buy them after 1 year.

1806

The uniform-free drugs used in BASIS will be stored in a safe place by researchers or other

1807

authorized personnel and stored in accordance with the conditions required (the drug

1808

instructions).

1809

Researchers, hospital pharmacists or other persons permitted to store and distribute the

1810

research drugs are responsible for ensuring that the drugs used in clinical trials are safely

1811

maintained in accordance with the requirements of the (research) organizers and meet the

1812

corresponding regulatory requirements.

106


```

### PDF page 107

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=107)

```text
BASIS

Number:2017YFC1307900

1813

All drugs used in clinical studies should be distributed according to the researcher's

1814

prescription, and the researcher should ensure that the drugs used for research distribution and

1815

recovery are accurately recorded.

1816

Any quality problems related to research drugs (labels, failure dates, etc.) encountered in the

1817

reception or use should be reported to the organizer in time, and the organizer should initiate a

1818

complaint procedure.

1819

Under no circumstances will researchers provide research results to third parties, allow the

1820

research results to be used under non-clinical research protocols, or transfer the research results

1821

in any other way.

1822

24. Research Device Processing Mechanism, Characteristics, and

1823

Responsibilities Division

1824

Balloon devices provided by SINOMED will be used in accordance with high-quality clinical

1825

practice guidelines and medical device tracking guidelines. An introduction to the balloon

1826

device contains the following information:

1827

Device name : Neuro RX intracranial balloon catheter

1828

Research and development unit : Sino Medical Science and Technology Co., Ltd.

1829

Registration number: CFDA, 20163772491 (China, Equipment, Registration, Approval,

1830

2016-12-19)

1831

Composition: Neuro RX intracranial balloon catheter is an expandable balloon with a rapid

1832

exchange system that can be used to treat ICAS. Its working length is 145 cm, with a guide wire

1833

of less than 0.014’ and a catheter with an inner diameter of ≥ 5F ( 0.056’). Two opaque markers

107


```

### PDF page 108

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=108)

```text
BASIS

Number:2017YFC1307900

1834

on the catheter shaft indicate the working length of the balloon. The guide wire exit is 24 cm

1835

from the far tip.

1836

Device parameters (length and diameter)

1837

1838
1839

Recommend: Neuro RX intracranial balloon catheter is suitable for ICAS lesion, and balloon

1840

dilatation for improving intracranial perfusion.

1841

Device name: Neuro LPS intracranial balloon dilatation catheter

1842

Research and development unit: Sino Medical Science and Technology Co., Ltd.

1843

Registration number: NMPA, 20203030576 (China, Equipment, Registration,

1844

Approval, 2020-06-19)

1845

Composition:

1846

Neuro LPS intracranial balloon dilatation catheter is composed of medical polypropylene,

1847

polytetrafluoroethylene, polyether amide block copolymer, polycarbonate, polyolefin, stainless

1848

steel, and platinum alloy.
108


```

### PDF page 109

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=109)

```text
BASIS

Number:2017YFC1307900

1849

1850
1851

1) TIP head (polyether amide block copolymer)

1852

2) Balloon protective sheath (polytetrafluoroethylene)

1853

3) Balloon (109olyetherimide block copolymer)

1854

4) Balloon inner tube (109olyetherimide block copolymer)

1855

5) Marker (two Markers are respectively set on the balloon’s inner tube (4), the outer edge of the

1856

two Markers is flush with the neck of the balloon, and the material is 90% platinum and 10%

1857

iridium alloy)

1858

6) Balloon outer tube (109olyetherimide block copolymer)

1859

7) Metal conduit (304 stainless steel)

1860

8) sheath (two layers, inner layer of 304 stainless steel, outer layer of polyolefin)

1861

9) Joint (polycarbonate)

1862

Note 1: D1 represents the diameter of the balloon after expansion.

1863

Note 2: L2 represents the effective length of the balloon on the balloon catheter.

1864

Note 3: L represents the effective length of the balloon catheter.

1865

Note 4: A complete balloon dilatation catheter is inserted into a high-density polyethylene ring protective

1866

sleeve.
109


```

### PDF page 110

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=110)

```text
BASIS

Number:2017YFC1307900

1867
1868

Device parameters (length and diameter)

1869
1870

Description: Neuro RX or Neuro LPS intracranial balloon dilatation catheter is provided by

1871

SINOMED, and the intracranial balloon catheter equipment is not provided free of charge.

1872

Responsibilities Division

1873

Investigators and/or other designated persons/institutions should archive and save the delivery

1874

records of the products to the research center, including the inventory of the research center, the

1875

use of each item, and the unused products that are returned to the sponsor. In the event of

1876

damage, loss, or additional (unscheduled) material, the organizer or relevant party shall be

1877

notified. These records should include the date, quantity, product serial number, shelf life (if

1878

any), and a unique code number assigned to the device and the research object.

1879
1880

25. Control requirements
110


```

### PDF page 111

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=111)

```text
BASIS

Number:2017YFC1307900

1881

BASIS will be carried out in accordance with the relevant provisions of the China Food and

1882

Drug Administration (NMPA): 'medical device clinical trial quality management norms' and

1883

'drug clinical trial quality management norms'.

1884
1885

26. Institutional Review Board (IRB)/Ethics Committee (IEC)

1886

Researchers or organizers must submit a clinical research protocol to the Ethics Committee of

1887

Beijing Tiantan Hospital and obtain a written certificate signed by the Ethics Committee with

1888

clear approval time and approval opinions.

1889

The following information should be clearly marked on the written certificate of approval:

1890

clinical trial information (study number, name, and version number of clinical study protocol),

1891

review documents (study protocol, informed consent, etc.).

1892
1893

The clinical research will be initiated only after the research sponsor has received written
evidence of a clear approval time and approval opinion.

1894

During the clinical research, any revision or modification of the clinical study protocol, any

1895

event that may affect patient safety or the continuation of clinical research, especially any safety

1896

changes, and any updates to the Investigator's Manual should be reported to the Ethics

1897

Committee.

1898
1899

If necessary, a progress report is provided to the ethics committee each year, and the clinical
research results are summarized at the end of the clinical stud

1900
1901
1902
111


```

### PDF page 112

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=112)

```text
BASIS

Number:2017YFC1307900

1903

Reference

1904
1905
1906
1907
1908
1909
1910
1911
1912
1913
1914
1915
1916
1917
1918
1919
1920
1921
1922
1923
1924
1925
1926
1927
1928
1929
1930
1931
1932
1933
1934
1935
1936
1937
1938
1939
1940
1941
1942
1943
1944

1.

Gutierrez J, Turan TN, Hoh BL, Chimowitz MI. Intracranial atherosclerotic stenosis: risk factors,
diagnosis, and treatment. Lancet Neurol. 2022;21:355-368. doi: 10.1016/s1474-4422(21)00376-8

2.

Kasner SE, Chimowitz MI, Lynn MJ, Howlett-Smith H, Stern BJ, Hertzberg VS, Frankel MR, Levine SR,
Chaturvedi S, Benesch CG, et al. Predictors of ischemic stroke in the territory of a symptomatic
intracranial arterial stenosis. Circulation. 2006;113:555-563. doi: 10.1161/circulationaha.105.578229

3.

Zaidat OO, Klucznik R, Alexander MJ, Chaloupka J, Lutsep H, Barnwell S, Mawad M, Lane B, Lynn MJ,
Chimowitz M. The NIH registry on use of the Wingspan stent for symptomatic 70-99% intracranial arterial
stenosis. Neurology. 2008;70:1518-1524. doi: 10.1212/01.wnl.0000306308.08229.a3

4.

Zaidat OO, Fitzsimmons BF, Woodward BK, Wang Z, Killer-Oberpfalzer M, Wakhloo A, Gupta R,
Kirshner H, Megerian JT, Lesko J, et al. Effect of a balloon-expandable intracranial stent vs medical
therapy on risk of stroke in patients with symptomatic intracranial stenosis: the VISSIT randomized
clinical trial. Jama. 2015;313:1240-1248. doi: 10.1001/jama.2015.1693

5.

Chimowitz MI, Lynn MJ, Derdeyn CP, Turan TN, Fiorella D, Lane BF, Janis LS, Lutsep HL, Barnwell SL,
Waters MF, et al. Stenting versus aggressive medical therapy for intracranial arterial stenosis. N Engl J
Med. 2011;365:993-1003. doi: 10.1056/NEJMoa1105335

6.

Gao P, Wang T, Wang D, Liebeskind DS, Shi H, Li T, Zhao Z, Cai Y, Wu W, He W, et al. Effect of
Stenting Plus Medical Therapy vs Medical Therapy Alone on Risk of Stroke and Death in Patients With
Symptomatic Intracranial Stenosis: The CASSISS Randomized Clinical Trial. Jama. 2022;328:534-542.
doi: 10.1001/jama.2022.12000

7.

Wang T, Yang K, Zhang X, Luo J, Xu R, Wang X, Yang Y, Bai X, Ma Y, Yan Y, et al. Endovascular
Therapy for Symptomatic Intracranial Artery Stenosis: a Systematic Review and Network Meta-analysis.
Transl Stroke Res. 2022;13:676-685. doi: 10.1007/s12975-022-00996-8

8.

Seyedsaadat SM, Yolcu YU, Neuhaus A, Rizvi A, Alzuabi M, Murad MH, Brinjikji W, Bydon M, Kallmes
DF. Submaximal angioplasty in the treatment of patients with symptomatic ICAD: a systematic review and
meta-analysis. J Neurointerv Surg. 2020;12:380-385. doi: 10.1136/neurintsurg-2019-015451

9.

Stapleton CJ, Chen YF, Shallwani H, Vakharia K, Turan TN, Woo HH, Derdeyn CP, Charbel FT, Siddiqui
AH, Amin-Hanjani S. Submaximal Angioplasty for Symptomatic Intracranial Atherosclerotic Disease: A
Meta-Analysis of Peri-Procedural and Long-Term Risk. Neurosurgery. 2020;86:755-762. doi:
10.1093/neuros/nyz337

10.

Peng G, Li K, Wang A, Tian X, Qi Z, Li S, Tong X, Deng Y, Sun X, Miao Z. Medical and Endovascular
Treatments for Intracranial Atherosclerotic Stenosis: A Network Meta-Analysis. Transl Stroke Res. 2021.
doi: 10.1007/s12975-021-00957-7

11.

Chimowitz MI, Lynn MJ, Howlett-Smith H, Stern BJ, Hertzberg VS, Frankel MR, Levine SR, Chaturvedi
S, Kasner SE, Benesch CG, et al. Comparison of warfarin and aspirin for symptomatic intracranial arterial
stenosis. N Engl J Med. 2005;352:1305-1316. doi: 10.1056/NEJMoa043033

12.

Ma N, Zhang Y, Shuai J, Jiang C, Zhu Q, Chen K, Liu L, Li B, Shi X, Gao L, et al. Stenting for
symptomatic intracranial arterial stenosis in China: 1-year outcome of a multicenter registry study. Stroke
and vascular neurology. 2018;3:176-184. doi: 10.1136/svn-2017-000137

13.

Higashida RT, Furlan AJ, Roberts H, Tomsick T, Connors B, Barr J, Dillon W, Warach S, Broderick J,
Tilley B, et al. Trial design and reporting standards for intra-arterial cerebral thrombolysis for acute
ischemic stroke. Stroke. 2003;34:e109-137. doi: 10.1161/01.Str.0000082721.62796.09

112


```

### PDF page 113

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=113)

```text
BASIS

1945
1946
1947
1948
1949
1950
1951
1952
1953
1954
1955
1956
1957
1958
1959
1960
1961
1962
1963

14.

Number:2017YFC1307900

Zaidat OO, Yoo AJ, Khatri P, Tomsick TA, von Kummer R, Saver JL, Marks MP, Prabhakaran S, Kallmes
DF, Fitzsimmons BF, et al. Recommendations on angiographic revascularization grading standards for
acute

ischemic

stroke:

a

consensus

statement.

Stroke.

2013;44:2650-2663.

doi:

10.1161/strokeaha.113.001972
15.

Wang Y, Han S, Qin H, Zheng H, Jiang B, Cao Y, Gao Y, Guan L, Jia Q, Jiang Y, et al. Chinese Stroke
Association guidelines for clinical management of cerebrovascular disorders: executive summary and 2019
update of the management of high-risk population. Stroke Vasc Neurol. 2020;5:270-278. doi:
10.1136/svn-2020-000385

16.

Miao Z, Jiang L, Wu H, Bao Y, Jiao L, Li S, Wu J, Hua Y, Li Y, Zhu J, et al. Randomized controlled trial
of symptomatic middle cerebral artery stenosis: endovascular versus medical therapy in a Chinese
population. Stroke. 2012;43:3284-3290. doi: 10.1161/strokeaha.112.662270

17.

Dumont TM, Kan P, Snyder KV, Hopkins LN, Siddiqui AH, Levy EI. Revisiting angioplasty without
stenting for symptomatic intracranial atherosclerotic stenosis after the stenting and aggressive medical
management for preventing recurrent stroke in intracranial stenosis (SAMMPRIS) study. Neurosurgery.
2012;71:1103-1110. doi: 10.1227/NEU.0b013e318271bcb8

1964
1965
1966
1967
1968
1969
1970
1971
1972

Appendix

1973

Appendix Table 1. ASITN/SIR collateral circulation scale

1974

Grade 0

No collaterals visible to the ischemic site

113


```

### PDF page 114

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=114)

```text
BASIS

Grade 1

Number:2017YFC1307900

Slow collaterals to the periphery of the ischemic site with
persistence of some of the defect

Grade 2

Rapid collaterals to the periphery of ischemic site with
persistence of some of the defect and to only a portion of
the ischemic territory

Grade 3

Collaterals with slow but complete angiographic blood
flow of the ischemic bed by the late venous phase

Grade 4

Complete and rapid collateral blood flow to the vascular
bed in the entire ischemic territory by retrograde
perfusion

1975
1976
1977
1978
1979
1980
1981
1982
1983
1984
1985
1986
1987
1988
1989
1990
1991
1992
1993
1994
1995
1996
1997
114


```

### PDF page 115

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=115)

```text
BASIS

Number:2017YFC1307900

1998

Appendix Table 2. modified Rankin Scale

1999

The modified Rankin Scale (mRS) is an ordinal hierarchical scale ranging from 0 to 5, with higher scores

2000

indicating more severe disability. A score of 6 has been added to signify death.
Category Short description

Long description

0

No symptoms

No symptoms
Symptoms,

no

1

Minor symptoms that do not interfere with lifestyle
disability
Slight disability, symptoms that lead to some restriction in

2

Slight disability

lifestyle, but do not interfere with the patient's capacity to
look after himself.
Moderate disability, symptoms that significantly restrict

3

Moderate disability
lifestyle and prevent totally independent existence
Moderately severe disability, symptoms that clearly
Moderately severe

4

prevent independent existence though not needing constant
disability
attention
Severe disability, totally dependent patient requiring

5

Severe disability
constant attention day and night.

6

Death

Death

2001
2002
2003
2004
2005
2006
2007
2008
2009
2010

115


```

### PDF page 116

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=116)

```text
BASIS

Number:2017YFC1307900

2011
2012
2013

Appendix Table 3. National Institute of Health Stroke Scale (NIHSS)

2014

The NIHSS is an ordinal hierarchical scale to evaluate the severity of stroke by assessing a

2015

patient’s performance. Scores range from 0 to 42, with higher scores indicating a more severe

2016

deficit. Administer stroke scale items in the order listed. Record performance in each category

2017

after each subscale exam. Do not go back and change scores. Follow directions provided for

2018

each exam technique. Scores should reflect what the patient does, not what the clinician thinks

2019

the patient can do. The clinician should record answers while administering the exam and work

2020

quickly. Except where indicated, the patient should not be coached (i.e. repeated requests to

2021

patient to make a special effort).
Instructions

1a. Level of consciousness. The investigator must
choose a response if a full evaluation is prevented by
such obstacles as an endotracheal tube, language
barrier, orotracheal trauma/bandages. A 3 is scored
only if the patient makes no movement (other than
reflexive posturing) in response to noxious
stimulation.

Scale definition
0 = Alert; keenly responsive.
1 = Not alert; but arousable by minor
stimulation to obey, answer, or
respond.
2 = Not alert; required repeated
stimulation to attend, or is obtunded
and requires strong or painful
stimulation to make movements (not
stereotyped).
3 = Responds only with reflex motor or
autonomic
effects
or
totally
unresponsive, flaccid and areflexic.

1b. LOC Questions: The patient is asked the month
and his/her age. The answer must be correct – there is
not partial credit for being close. Phasic and stuporous
patients who do not comprehend the questions will
score 2. Patients unable to speak because of 0 = Answers both questions correctly.
endotracheal intubation, orotracheal trauma, severe 1 = Answers one question correctly.
dysarthria from any cause, language barrier, or any 2 = Answers neither question correctly.
other problem not secondary to aphasia are given a 1.
It is important that only the initial answer be graded
and that the examiners not “help” the patient with
verbal or non-verbal clues.
116


```

### PDF page 117

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=117)

```text
BASIS

Number:2017YFC1307900

1c. LOC Commands: The patient is asked to open and
close the eyes and then to grip and release the
non-paretic hand. Substitute another one step
command if the hand cannot be used. Credit is given if
an unequivocal attempt is made but not completed due
to weakness. If the patient does not respond to
command, the task should be demonstrated to him or
her (pantomime), and the result scored (i.e. follows
none, one or two commands). Patients with trauma,
amputation, or other physical impediments should be
given suitable one-step commands. Only the first
attempt is scored.
2. Best Gaze: Only horizontal eye movements will be
tested. Voluntary or reflexive (oculocephalic) eye
movements will be scored, but caloric testing is not
done. If the patient has a conjugate deviation of the
eyes that can be overcome by voluntary or reflexive
activity, the score will be a 1. If a patient has an
isolated peripheral nerve paresis (CN III, IV or VI),
score a 1. Gaze is testable in all aphasic patients.
Patients with ocular trauma, bandages, preexisting
blindness, or other disorder of visual acuity or fields
should be tested with reflexive movements, and a
choice made by the investigator. Establishing eye
contact and then moving about the patient from side to
side will occasionally clarify the presence of a partial
gaze palsy.
3. Visual: Visual fields (upper and lower quadrants)
are tested by confrontation, using finger counting or
visual threat, as appropriate. Patients may be
encouraged, but if they look at the side of the moving
finger appropriately, this can be scored as normal. If
there is unilateral blindness or enucleation, visual
fields in the remaining eye are scored. Score 1 only if
a clear-cut asymmetry, including quadrantanopia, is
found. If patient is blind from any cause, score 3.
Double simultaneous stimulation is performed in this
case.
If there is extinction, the patient receives a 1, and the
results are used to respond to item 11.
4. Facial palsy: Ask or use pantomime to encourage
the patient to show teeth or raise eyebrows and close
eyes. Score symmetry of grimace in response to
noxious stimuli in the poorly response or
117

0 = Performs both tasks correctly.
1 = Performs one task correctly.
2 = Performs neither task correctly.

0= Normal.
1= Partial gaze palsy; gaze is abnormal
in one or both eyes, but forced
deviation or total gaze paresis is not
present.
2= Forced deviation; or total gaze
paresis not overcome by the
oculocephalic maneuver.

0= No visual loss.
1= Partial hemianopia.
2= Complete hemianopia.
3= Bilateral hemianopia
including cortical blindness)

(blind

0 = Normal symmetrical movements.
1=
Minor
paralysis
(flattened
nasolabial fold, asymmetry on smiling)
2= Partial paralysis (total or near-total


```

### PDF page 118

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=118)

```text
BASIS

Number:2017YFC1307900

non-comprehending
patient.
If
facial
trauma/bandages, orotracheal tube, tape or other
physical barriers obscure the face, these should be
removed to the extent possible.

5. Motor arm: The limb is placed in the appropriate
position: extend the arms (palms down) 90 degrees (if
sitting) or 45 degrees (if supine). Drift is scored if the
arm falls before 10 seconds. The aphasic patient is
encouraged using urgency in the voice and
pantomime, but not noxious stimulation. Each limb is
tested in turn, beginning with the non-paretic arm.
Only in the case of amputation or joint fusion at the
shoulder, the examiner should record the score as
untestable (UN), and clearly write the explanation for
this choice.

6. Motor leg: The limb is placed in the appropriate
position:
hold the leg at 30 degrees (always tested supine). Drift
is scored if the leg falls before 5 seconds. The aphasic
patient is encouraged using urgency in the voice and
pantomime, but not noxious stimulation. Each limb is
tested in turn, beginning with the non-paretic leg.
Only in the case of amputation or joint fusion at the
hip, the examiner should record the score as untestable
(UN), and clearly write the explanation for this
choice.
7. Limb ataxia: This item is aimed at finding evidence
of a unilateral cerebellar lesion. Test with eyes open.
In case of visual defect, ensure testing is done in intact
visual field. The finger-nose-finger and heel-shin tests
are performed on both sides, and ataxia is scored only
if present out of proportion to weakness. Ataxia is
absent in the patient who cannot understand or is
paralyzed. Only in the case of amputation or joint
fusion, the examiner should record the score as
untestable (UN), and clearly write the explanation for
this choice. In case of blindness, test by having the
118

paralysis of lower face)
3= Complete paralysis of one or both
sides (absence of facial movement in
the upper and lower face).
0= No drift; limb holds 90 (or 45)
degrees for full 10 seconds.
1= Drift; limb holds 90 (or 45) degrees,
but drifts down before full 10 seconds;
does not hit bed or other support.
2= Some effort against gravity; limb
cannot get to or maintain (if cued) 90
(or 45) degrees, drifts down to bed, but
has some effort against gravity.
3= No effort against gravity; limb falls.
4= No movement.
UN = Amputation or joint fusion:
explain:
5a = Left Arm.
5b = Right arm.
0= No drift; leg holds 30-degree
position for full 5 seconds.
1= Drift; leg falls by the end of the
5-second period but does not hit bed.
2= Some effort against gravity; leg falls
to bed by 5 seconds, but has some
effort against gravity.
3= No effort against gravity; leg falls to
bed immediately.
4= No movement.
UN = Amputation or joint fusion:
explain:
6a. Left Leg
6b. Right Leg.

0= Absent.
1= Present in one limb.
2= Present in two limbs.
UN = Amputation or joint fusion:
explain:


```

### PDF page 119

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=119)

```text
BASIS

Number:2017YFC1307900

patient touch nose from extended arm position.
8. Sensory: Sensation or grimace to pinprick when
tested, or withdrawal from noxious stimulus in the
obtunded or aphasic patient. Only sensory loss
attributed to stroke is scored as abnormal and the
examiner should test as many body areas (arms [not
hands], legs, trunk, face) as needed to accurately
check for hemisensory loss. A score of 2, 'severe or
total sensory loss', should only be given when a severe
or total loss of sensation can be clearly demonstrated.
Stuporous and aphasic patients will, therefore,
probably score 1 or 0. The patient with brainstem
stroke who has bilateral loss of sensation is scored 2.
If the patient does not respond and is quadriplegic,
score 2.
Patients in a coma (item 1a=3) are automatically given
a 2 on this item.

9. Best language: A great deal of information about
comprehension will be obtained during the preceding
sections of the examination. For this scale item, the
patient is asked to describe what is happening in the
attached picture, to name the items on the attached
naming sheet and to read from the attached list of
sentences. Comprehension is judged from responses
here, as well as to all of the commands in the
preceding general neurological exam. If visual loss
interferes with the tests, ask the patient to identify
objects placed in the hand, repeat, and produce
speech. The intubated patient should be asked to
write. The patient in a coma (item 1a=3) will
automatically score 3 on this item. The examiner must
choose a score for the patient with stupor or limited
cooperation, but a score of 3 should be used only if
the patient is mute and follows no one-step
commands.

10. Dysarthria: If patient is thought to be normal, an
adequate sample of speech must be obtained by asking
patient to read or repeat words from the attached list.
119

0= Normal; no sensory loss.
1= Mild-to-moderate sensory loss;
patients feels pinprick is less sharp or is
dull on the affected side; or there is a
loss of superficial pain with pinprick,
but patient is aware of being touched.
2= Severe to total sensory loss; patient
is not aware of being touched in the
face, arm and leg.

0= No aphasia; normal
1= Mild-to-moderate aphasia; some
obvious loss of fluency or facility of
comprehension, without significant
limitation on ideas expressed or form
of expression. Reduction of speech
and/or comprehension, however, makes
conservation about provided materials
difficult or impossible. For example, in
conversation about provided materials,
examiner can identify picture or
naming card content from patient's
response.
2= Severe aphasia; all communication
is through fragmentary expression;
great need for inference, questioning,
and guessing by the listener. Range of
information that can be exchanged is
limited; listener carries burden of
communication. Examiner cannot
identify materials provided from
patient response.
3 = Mute, global aphasia: no usable
speech or auditory comprehension.
0= Normal.
1= Mild-to-moderate dysarthria; patient
slurs at least some words and, at worst,


```

### PDF page 120

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=120)

```text
BASIS

Number:2017YFC1307900

If the patient has severe aphasia, the clarity of
articulation of spontaneous speech can be rated. Only
if patient is intubated or has other physical barriers to
producing speech, the examiner should record the
score as untestable (UN), and clearly write an
explanation for this choice. Do not tell the patient why
he or she is being tested.
11. Extinction and Inattention (formerly Neglect):
Sufficient information to identify neglect may be
obtained during the prior testing. If the patient has a
severe visual loss preventing visual double
simultaneous stimulation, and the cutaneous stimuli
are normal, the score is normal. If the patient has
aphasia but does appear to attend to both sides, the
score is normal. The presence of visual spatial neglect
or anosagnosia may also be taken as evidence of
abnormality. Since the abnormality is scored only if
present, the item is never untestable.
2022

120

can be understood by some difficulty.
2= Severe dysarthria: patient's speech
is so slurred as to be unintelligible in
the absence of or out of proportion to
any dysphasia, or is mute/anarthric.
UN = Intubated or other physical
barrier.
0= No abnormality.
1= Visual, tactile, auditory, spatial, or
personal inattention or extinction to
bilateral
simultaneous stimulation in one of the
sensory modalities.
2= Profound hemi-inattention or
extinction to more than one modality;
does not recognize own hand or orients
to only one side of space.


```

### PDF page 121

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=121)

```text
BASIS

Number:2017YFC1307900

2023

Appendix Table 4. EuroQoL 5D-5L

2024

Under each heading, please tick the ONE box that best describes your health TODAY.

2025

Mobility
I have no problems in walking about
I have slight problems in walking about
I have moderate problems in walking about
I have severe problems in walking about
I am unable to walk about
Self-care
I have no problems washing or dressing myself
I have slight problems washing or dressing myself
I have moderate problems washing or dressing myself
I have severe problems washing or dressing myself
I am unable to wash or dress myself
Usual activities (e.g. work, study, housework, family or leisure activities)
I have no problems doing my usual activities
I have slight problems doing my usual activities
I have moderate problems doing my usual activities
I have severe problems doing my usual activities
I am unable to do my usual activities
Pain/discomfort
I have no pain or discomfort
I have slight pain or discomfort
I have moderate pain or discomfort
I have severe pain or discomfort
I have extreme pain or discomfort
Anxiety/depression
I am not anxious or depressed
I am slightly anxious or depressed
I am moderately anxious or depressed
I am severely anxious or depressed
I am extremely anxious or depressed

2026

121


```

### PDF page 122

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=122)

```text
BASIS








Number:2017YFC1307900

We would like to know how good or bad your
health is TODAY.
This scale is numbered from 0 to 100.
100 means the best health you can imagine.
0 means the worst health you can imagine.
Mark an X on the scale to indicate how your health
is TODAY.
Now, please write the number you marked on the
scale in the box below.

YOUR HEALTH TODAY =
2027

122


```

### PDF page 123

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=123)

```text
BASIS

2028
2029

Number:2017YFC1307900

Appendix Table 5. mTICI grade
mTICI grade
0 grade
1 grade

Definitions
No perfusion
Antegrade reperfusion past the initial occlusion, but limited distal branch
filling with little or slow distal reperfusion

2a grade

Antegrade reperfusion of less than half of the occluded target artery previously
ischemic territory (eg, in 1 major division of the MCA and its territory)

2b grade

Antegrade reperfusion of more than half of the previously occluded target
artery ischemic territory (eg, in 2 major divisions of the MCA and their
territories)

3 grade

Complete antegrade reperfusion of the previously occluded target artery
ischemic territory, with absence of visualized occlusion in all distal branches

2030
2031
2032
2033
2034
2035
2036
2037
2038
2039

2040

2041

2042
123


```

### PDF page 124

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=124)

```text
BASIS

Number:2017YFC1307900

Summary of changes

2043

2044

BASIS Protocol V2.0-20180625 (original version)

2045

BASIS Protocol V2.1-20200414 (amended version)

2046

BASIS Protocol V2.2-20211222 (amended version)

2047

BASIS Protocol V2.3-20220328 (final version)
Version

Date of

Changed

Reasons for change

Change the interval between stroke
onset to enroll in inclusion criteria
(1, 6 and 8.1)

According to the Chinese

Participants with primary or recurrent

Intracranial

sICAS (a recent TIA [<90 days] or

Atherosclerotic Stenosis,

revised
V2.1

2020/04/14

ischemic stroke [14-90 days] before

Expert Consensus 2018 on
Endovascular Treatment of

(ICAS) recommended that
2 weeks endovascular

enrollment attributed to 70-99%

treatment after acute

atherosclerotic stenosis of a major

ischemic stroke may be
safe.

intracranial artery)
Clarify the inclusion criteria of lesion

Clear the specific lesion

artery (1 and 8.1): 3. Diagnosed by DSA: a

location of anterior and

major intracranial artery (terminal internal

posterior circulation

carotid artery [ICA] [C4-C7 segments],
middle cerebral artery [MCA] M1 segment,
vertebral artery [VA] V4 segment, and
basilar artery [BA])
V2.2

2021/12/22

Clarify exclusion criteria (1 and 8.2) 6.
Target artery’s supplying artery stenosis >
50%. For example, patient with MCA severe
stenosis (target artery) and the ipsilateral
ICA stenosis > 50% should be excluded;
patient with BA severe stenosis (target
artery) and the dominant VA stenosis > 50%
124

Clarify exclusion criteria


```

### PDF page 125

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=125)

```text
BASIS

Number:2017YFC1307900

should be excluded; the patient with
extracranial

artery

(non-lesion

side)

stenosis > 70% should be excluded; For
patients with balanced VA, if bilateral VA
stenosis > 70% at the same time, should be
excluded (unable to determine which VA is
the lesion artery). However, if patient’s
dominant VA is the lesion artery with a
dysplasia or slender contralateral VA or a
non-dominant contralateral VA terminating
at posteroinferior cerebellar artery, should
not be excluded.
Add 24-month and 36-month follow-up

To explore the longer-term

outcomes to secondary outcomes (1 and

effect of BA for sICAS.

7.2) 10. Any stroke (ischemic or hemorrhage
stroke) inside of the territory of the target
artery or all-cause deaths within 24 months
after enrollment; 11. Any stroke (ischemic or
hemorrhage stroke) outside of the territory of
the target artery within 24 months after
enrollment;12. mRS at 24 months; 13.
Combined events such as stroke,
myocardial infarction, and vascular death
within 24 months after enrollment; 14. Any
stroke (ischemic or hemorrhage stroke)
inside of the territory of the target artery or
all-cause deaths within 36 months after
enrollment; 15.

Any stroke (ischemic or

hemorrhage stroke) outside of the territory of
the target artery within 36 months after
enrollment; 16.

Neurological

improvement assessed by mRS at 36
months; 17.

Combined events such as

stroke, myocardial infarction, and vascular
death within 36 months after enrollment.

125


```

### PDF page 126

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=126)

```text
BASIS

Number:2017YFC1307900

Re-estimate the sample size (1 and 20.1)

According to more recent
studies and the

Change the sample size from 802 to 512

investigator’s clinical

(Details in SAP 2.0)

practice in China, the
composite event rate in the
AMM group was 15% and
7% in the BA group. With
the updated data of events
rates and considering the
difficulty in enrolling
patients related to the
COVID-19 pandemic and
insufficient funding, the data
safety and monitoring board
recommended to forgo the
interim analysis

V2.3

2022/03/28

Add new outcomes to secondary outcomes

The two outcomes were

(1 and 7.2) 1. Any stroke (ischemic or

also important for the

hemorrhage stroke) or all-cause deaths

BASIS trial.

within 30 days after enrollment or after
balloon

angioplasty

qualifying

lesion

procedure
during

of

the

follow-up.

6.Revascularization of the target artery
within 12 months after enrollment;

2048
2049
2050
2051
2052
2053
2054
2055
2056
2057
2058
2059
2060
2061
2062
126


```

### PDF page 127

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=127)

```text
BASIS

Number:2017YFC1307900

2063

Balloon Angioplasty vs. Aggressive Medical Management for

2064

Symptomatic Intracranial Artery Stenosis: The BASIS Randomized

2065

Clinical Trial

2066

(BASIS)

2067

2068
2069

Statistical Analysis Plan

2070
2071

Principal Investigator

2072
2073

Zhongrong Miao, MD, Professor of Neurology
Beijing Tiantan Hospital, Capital Medical University, Beijing, China

2074

Co-Principal Investigator

2075
2076

Yilong Wang, MD, Professor of Neurology
Beijing Tiantan Hospital, Capital Medical University, Beijing, China

2077

SAP Prepared by

2078

Department of Biostatistics,

2079

Peking University Clinical Research Institute, Beijing, China

2080
2081
2082
2083

Version 1.0

2084

Date: December 27, 2018

127


```

### PDF page 128

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=128)

```text
BASIS

Number:2017YFC1307900

2085

Contents

2086

1.Introduction..........................................................................................................................................130

2087

2.Study Objective....................................................................................................................................130

2088

3.Study Endpoint(s)................................................................................................................................130

2089

3.1. Primary Endpoint...........................................................................................................................130

2090

3.2. Secondary Endpoints.....................................................................................................................130

2091

3.3. Safety Assessment.........................................................................................................................131

2092

4.Study Hypothesis.................................................................................................................................132

2093

5.Design...................................................................................................................................................132

2094

5.1 Study Design..................................................................................................................................132

2095

5.2 Planned Analyses...........................................................................................................................133

2096

5.3 Interim Analyses............................................................................................................................134

2097

6.Sample Size Estimates........................................................................................................................134

2098

7.Analysis Populations..........................................................................................................................134

2099

7.1 Intention-to-treat Set (ITT)...........................................................................................................134

2100

7.2. Per Protocol Set (PPS).................................................................................................................135

2101

7.3. As-treated Set (ATS)...................................................................................................................134

2102

7.4. Safety Set (SS)............................................................................................................................135

2103

8. Treatment Comparisons...................................................................................................................134

2104

9. General Considerations for Data Analyses........................................................................................135

2105

9.1 Multicenter Studies............................................................................................................................135

2106

9.2 Examination of Subgroups................................................................................................................135

2107

9.3 Multiple Comparisons and Multiplicity...........................................................................................135

2108

10. Data Handling Conventions...............................................................................................................136

2109

10.1 Premature Withdrawal and Missing Data......................................................................................136

2110

10.2 Event Rates......................................................................................................................................136

2111

10.3 Time to Event Analysis..............................................................................................................137

2112

11.Study Population.............................................................................................................................138

2113

11.1 Disposition of Subjects...............................................................................................................138

2114

11.2 Protocol Deviations.................................................................................................................... 138
128


```

## Layout transcription supplement: NIHSS and endpoint-scale tables

### Table layout PDF page 115

```text
       BASIS                                                                                  Number:2017YFC1307900



1998   Appendix Table 2. modified Rankin Scale
1999   The modified Rankin Scale (mRS) is an ordinal hierarchical scale ranging from 0 to 5, with higher scores

2000   indicating more severe disability. A score of 6 has been added to signify death.

       Category Short description           Long description

       0           No symptoms              No symptoms

                   Symptoms,           no
       1                                    Minor symptoms that do not interfere with lifestyle
                   disability

                                            Slight disability, symptoms that lead to some restriction in

       2           Slight disability        lifestyle, but do not interfere with the patient's capacity to

                                            look after himself.

                                            Moderate disability, symptoms that significantly restrict
       3           Moderate disability
                                            lifestyle and prevent totally independent existence

                                            Moderately severe disability, symptoms that clearly
                   Moderately severe
       4                                    prevent independent existence though not needing constant
                   disability
                                            attention

                                            Severe disability, totally dependent patient requiring
       5           Severe disability
                                            constant attention day and night.

       6           Death                    Death

2001


2002


2003


2004

2005
2006
2007
2008
2009
2010


                                                            115

```

### Table layout PDF page 116

```text
       BASIS                                                                       Number:2017YFC1307900



2011


2012


2013   Appendix Table 3. National Institute of Health Stroke Scale (NIHSS)


2014       The NIHSS is an ordinal hierarchical scale to evaluate the severity of stroke by assessing a
2015   patient’s performance. Scores range from 0 to 42, with higher scores indicating a more severe
2016   deficit. Administer stroke scale items in the order listed. Record performance in each category
2017   after each subscale exam. Do not go back and change scores. Follow directions provided for
2018   each exam technique. Scores should reflect what the patient does, not what the clinician thinks
2019   the patient can do. The clinician should record answers while administering the exam and work
2020   quickly. Except where indicated, the patient should not be coached (i.e. repeated requests to
2021   patient to make a special effort).

       Instructions                                             Scale definition
                                                                0 = Alert; keenly responsive.
                                                                1 = Not alert; but arousable by minor
                                                                stimulation to obey, answer, or
       1a. Level of consciousness. The investigator must
                                                                respond.
       choose a response if a full evaluation is prevented by
                                                                2 = Not alert; required repeated
       such obstacles as an endotracheal tube, language
                                                                stimulation to attend, or is obtunded
       barrier, orotracheal trauma/bandages. A 3 is scored
                                                                and requires strong or painful
       only if the patient makes no movement (other than
                                                                stimulation to make movements (not
       reflexive posturing) in response to noxious
                                                                stereotyped).
       stimulation.
                                                                3 = Responds only with reflex motor or
                                                                autonomic       effects    or     totally
                                                                unresponsive, flaccid and areflexic.
       1b. LOC Questions: The patient is asked the month
       and his/her age. The answer must be correct – there is
       not partial credit for being close. Phasic and stuporous
       patients who do not comprehend the questions will
       score 2. Patients unable to speak because of 0 = Answers both questions correctly.
       endotracheal intubation, orotracheal trauma, severe 1 = Answers one question correctly.
       dysarthria from any cause, language barrier, or any 2 = Answers neither question correctly.
       other problem not secondary to aphasia are given a 1.
       It is important that only the initial answer be graded
       and that the examiners not “help” the patient with
       verbal or non-verbal clues.
                                                     116

```

### Table layout PDF page 117

```text
BASIS                                                                          Number:2017YFC1307900


1c. LOC Commands: The patient is asked to open and
close the eyes and then to grip and release the
non-paretic hand. Substitute another one step
command if the hand cannot be used. Credit is given if
an unequivocal attempt is made but not completed due
                                                            0 = Performs both tasks correctly.
to weakness. If the patient does not respond to
                                                            1 = Performs one task correctly.
command, the task should be demonstrated to him or
                                                            2 = Performs neither task correctly.
her (pantomime), and the result scored (i.e. follows
none, one or two commands). Patients with trauma,
amputation, or other physical impediments should be
given suitable one-step commands. Only the first
attempt is scored.
2. Best Gaze: Only horizontal eye movements will be
tested. Voluntary or reflexive (oculocephalic) eye
movements will be scored, but caloric testing is not
done. If the patient has a conjugate deviation of the
                                                            0= Normal.
eyes that can be overcome by voluntary or reflexive
                                                            1= Partial gaze palsy; gaze is abnormal
activity, the score will be a 1. If a patient has an
                                                            in one or both eyes, but forced
isolated peripheral nerve paresis (CN III, IV or VI),
                                                            deviation or total gaze paresis is not
score a 1. Gaze is testable in all aphasic patients.
                                                            present.
Patients with ocular trauma, bandages, preexisting
                                                            2= Forced deviation; or total gaze
blindness, or other disorder of visual acuity or fields
                                                            paresis not overcome by the
should be tested with reflexive movements, and a
                                                            oculocephalic maneuver.
choice made by the investigator. Establishing eye
contact and then moving about the patient from side to
side will occasionally clarify the presence of a partial
gaze palsy.
3. Visual: Visual fields (upper and lower quadrants)
are tested by confrontation, using finger counting or
visual threat, as appropriate. Patients may be
encouraged, but if they look at the side of the moving
finger appropriately, this can be scored as normal. If      0= No visual loss.
there is unilateral blindness or enucleation, visual        1= Partial hemianopia.
fields in the remaining eye are scored. Score 1 only if     2= Complete hemianopia.
a clear-cut asymmetry, including quadrantanopia, is         3= Bilateral hemianopia           (blind
found. If patient is blind from any cause, score 3.         including cortical blindness)
Double simultaneous stimulation is performed in this
case.
If there is extinction, the patient receives a 1, and the
results are used to respond to item 11.
4. Facial palsy: Ask or use pantomime to encourage          0 = Normal symmetrical movements.
the patient to show teeth or raise eyebrows and close       1=    Minor       paralysis    (flattened
eyes. Score symmetry of grimace in response to              nasolabial fold, asymmetry on smiling)
noxious stimuli in the poorly response or                   2= Partial paralysis (total or near-total
                                                117

```

### Table layout PDF page 118

```text
BASIS                                                                            Number:2017YFC1307900


non-comprehending         patient.     If     facial         paralysis of lower face)
trauma/bandages, orotracheal tube, tape or other             3= Complete paralysis of one or both
physical barriers obscure the face, these should be          sides (absence of facial movement in
removed to the extent possible.                              the upper and lower face).
                                                             0= No drift; limb holds 90 (or 45)
                                                             degrees for full 10 seconds.
5. Motor arm: The limb is placed in the appropriate          1= Drift; limb holds 90 (or 45) degrees,
position: extend the arms (palms down) 90 degrees (if        but drifts down before full 10 seconds;
sitting) or 45 degrees (if supine). Drift is scored if the   does not hit bed or other support.
arm falls before 10 seconds. The aphasic patient is          2= Some effort against gravity; limb
encouraged using urgency in the voice and                    cannot get to or maintain (if cued) 90
pantomime, but not noxious stimulation. Each limb is         (or 45) degrees, drifts down to bed, but
tested in turn, beginning with the non-paretic arm.          has some effort against gravity.
Only in the case of amputation or joint fusion at the        3= No effort against gravity; limb falls.
shoulder, the examiner should record the score as            4= No movement.
untestable (UN), and clearly write the explanation for       UN = Amputation or joint fusion:
this choice.                                                 explain:
                                                             5a = Left Arm.
                                                             5b = Right arm.
                                                             0= No drift; leg holds 30-degree
                                                             position for full 5 seconds.
6. Motor leg: The limb is placed in the appropriate
                                                             1= Drift; leg falls by the end of the
position:
                                                             5-second period but does not hit bed.
hold the leg at 30 degrees (always tested supine). Drift
                                                             2= Some effort against gravity; leg falls
is scored if the leg falls before 5 seconds. The aphasic
                                                             to bed by 5 seconds, but has some
patient is encouraged using urgency in the voice and
                                                             effort against gravity.
pantomime, but not noxious stimulation. Each limb is
                                                             3= No effort against gravity; leg falls to
tested in turn, beginning with the non-paretic leg.
                                                             bed immediately.
Only in the case of amputation or joint fusion at the
                                                             4= No movement.
hip, the examiner should record the score as untestable
                                                             UN = Amputation or joint fusion:
(UN), and clearly write the explanation for this
                                                             explain:
choice.
                                                             6a. Left Leg
                                                             6b. Right Leg.
7. Limb ataxia: This item is aimed at finding evidence
of a unilateral cerebellar lesion. Test with eyes open.
In case of visual defect, ensure testing is done in intact
visual field. The finger-nose-finger and heel-shin tests     0= Absent.
are performed on both sides, and ataxia is scored only       1= Present in one limb.
if present out of proportion to weakness. Ataxia is          2= Present in two limbs.
absent in the patient who cannot understand or is            UN = Amputation or joint fusion:
paralyzed. Only in the case of amputation or joint           explain:
fusion, the examiner should record the score as
untestable (UN), and clearly write the explanation for
this choice. In case of blindness, test by having the
                                                 118

```

### Table layout PDF page 119

```text
BASIS                                                                         Number:2017YFC1307900


patient touch nose from extended arm position.
8. Sensory: Sensation or grimace to pinprick when
tested, or withdrawal from noxious stimulus in the
obtunded or aphasic patient. Only sensory loss
attributed to stroke is scored as abnormal and the
                                                          0= Normal; no sensory loss.
examiner should test as many body areas (arms [not
                                                          1= Mild-to-moderate sensory loss;
hands], legs, trunk, face) as needed to accurately
                                                          patients feels pinprick is less sharp or is
check for hemisensory loss. A score of 2, 'severe or
                                                          dull on the affected side; or there is a
total sensory loss', should only be given when a severe
                                                          loss of superficial pain with pinprick,
or total loss of sensation can be clearly demonstrated.
                                                          but patient is aware of being touched.
Stuporous and aphasic patients will, therefore,
                                                          2= Severe to total sensory loss; patient
probably score 1 or 0. The patient with brainstem
                                                          is not aware of being touched in the
stroke who has bilateral loss of sensation is scored 2.
                                                          face, arm and leg.
If the patient does not respond and is quadriplegic,
score 2.
Patients in a coma (item 1a=3) are automatically given
a 2 on this item.
                                                          0= No aphasia; normal
                                                          1= Mild-to-moderate aphasia; some
                                                          obvious loss of fluency or facility of
9. Best language: A great deal of information about       comprehension, without significant
comprehension will be obtained during the preceding       limitation on ideas expressed or form
sections of the examination. For this scale item, the     of expression. Reduction of speech
patient is asked to describe what is happening in the     and/or comprehension, however, makes
attached picture, to name the items on the attached       conservation about provided materials
naming sheet and to read from the attached list of        difficult or impossible. For example, in
sentences. Comprehension is judged from responses         conversation about provided materials,
here, as well as to all of the commands in the            examiner can identify picture or
preceding general neurological exam. If visual loss       naming card content from patient's
interferes with the tests, ask the patient to identify    response.
objects placed in the hand, repeat, and produce           2= Severe aphasia; all communication
speech. The intubated patient should be asked to          is through fragmentary expression;
write. The patient in a coma (item 1a=3) will             great need for inference, questioning,
automatically score 3 on this item. The examiner must     and guessing by the listener. Range of
choose a score for the patient with stupor or limited     information that can be exchanged is
cooperation, but a score of 3 should be used only if      limited; listener carries burden of
the patient is mute and follows no one-step               communication. Examiner cannot
commands.                                                 identify materials provided from
                                                          patient response.
                                                          3 = Mute, global aphasia: no usable
                                                          speech or auditory comprehension.
10. Dysarthria: If patient is thought to be normal, an    0= Normal.
adequate sample of speech must be obtained by asking      1= Mild-to-moderate dysarthria; patient
patient to read or repeat words from the attached list.   slurs at least some words and, at worst,
                                               119

```

### Table layout PDF page 120

```text
       BASIS                                                                          Number:2017YFC1307900


       If the patient has severe aphasia, the clarity of           can be understood by some difficulty.
       articulation of spontaneous speech can be rated. Only       2= Severe dysarthria: patient's speech
       if patient is intubated or has other physical barriers to   is so slurred as to be unintelligible in
       producing speech, the examiner should record the            the absence of or out of proportion to
       score as untestable (UN), and clearly write an              any dysphasia, or is mute/anarthric.
       explanation for this choice. Do not tell the patient why    UN = Intubated or other physical
       he or she is being tested.                                  barrier.
       11. Extinction and Inattention (formerly Neglect):
                                                                   0= No abnormality.
       Sufficient information to identify neglect may be
                                                                   1= Visual, tactile, auditory, spatial, or
       obtained during the prior testing. If the patient has a
                                                                   personal inattention or extinction to
       severe visual loss preventing visual double
                                                                   bilateral
       simultaneous stimulation, and the cutaneous stimuli
                                                                   simultaneous stimulation in one of the
       are normal, the score is normal. If the patient has
                                                                   sensory modalities.
       aphasia but does appear to attend to both sides, the
                                                                   2= Profound hemi-inattention or
       score is normal. The presence of visual spatial neglect
                                                                   extinction to more than one modality;
       or anosagnosia may also be taken as evidence of
                                                                   does not recognize own hand or orients
       abnormality. Since the abnormality is scored only if
                                                                   to only one side of space.
       present, the item is never untestable.
2022




                                                       120

```

### Table layout PDF page 121

```text
       BASIS                                                                          Number:2017YFC1307900



2023   Appendix Table 4. EuroQoL 5D-5L


2024   Under each heading, please tick the ONE box that best describes your health TODAY.
2025   Mobility
       I have no problems in walking about
       I have slight problems in walking about
       I have moderate problems in walking about
       I have severe problems in walking about
       I am unable to walk about
       Self-care
       I have no problems washing or dressing myself
       I have slight problems washing or dressing myself
       I have moderate problems washing or dressing myself
       I have severe problems washing or dressing myself
       I am unable to wash or dress myself
       Usual activities (e.g. work, study, housework, family or leisure activities)
       I have no problems doing my usual activities
       I have slight problems doing my usual activities
       I have moderate problems doing my usual activities
       I have severe problems doing my usual activities
       I am unable to do my usual activities
       Pain/discomfort
       I have no pain or discomfort
       I have slight pain or discomfort
       I have moderate pain or discomfort
       I have severe pain or discomfort
       I have extreme pain or discomfort
       Anxiety/depression
       I am not anxious or depressed
       I am slightly anxious or depressed
       I am moderately anxious or depressed
       I am severely anxious or depressed
       I am extremely anxious or depressed
2026




                                                       121

```

### Table layout PDF page 122

```text
       BASIS                                                    Number:2017YFC1307900



          We would like to know how good or bad your
           health is TODAY.
          This scale is numbered from 0 to 100.
          100 means the best health you can imagine.
          0 means the worst health you can imagine.
          Mark an X on the scale to indicate how your health
           is TODAY.
          Now, please write the number you marked on the
           scale in the box below.




       YOUR HEALTH TODAY =
2027




                                                    122

```

### Table layout PDF page 123

```text
       BASIS                                                                     Number:2017YFC1307900


2028   Appendix Table 5. mTICI grade
2029
       mTICI grade
                      Definitions
       0 grade
                      No perfusion
       1 grade
                      Antegrade reperfusion past the initial occlusion, but limited distal branch

                      filling with little or slow distal reperfusion
       2a grade
                      Antegrade reperfusion of less than half of the occluded target artery previously

                      ischemic territory (eg, in 1 major division of the MCA and its territory)
       2b grade
                      Antegrade reperfusion of more than half of the previously occluded target

                      artery ischemic territory (eg, in 2 major divisions of the MCA and their

                      territories)
       3 grade
                      Complete antegrade reperfusion of the previously occluded target artery

                      ischemic territory, with absence of visualized occlusion in all distal branches

2030
2031
2032
2033
2034
2035
2036
2037
2038


2039



2040



2041



2042
                                                    123

```


<!-- END support_doc003_pp097-128.md -->

---


<!-- BEGIN support_doc003_pp129-160.md -->

# DOC-003 support evidence mapping: PDF pages 129–160

Scope: exactly PDF pages 129–160 of `joi240088supp2_prod_1746815064.36071.pdf`; 32 distinct pages mapped. Document role throughout: PLAN. Runtime agent: 01a12bd2-0db1-7382-a67c-feeabceff738. Mapping is new scientific extraction, with no legacy findings or dispositions consulted. Curator gate satisfied: evidence_asset_inventory.md and reused_artifact_hashes_before.sha256 existed before mapping.

Evidence aids: all 32 eligible `page-NNN.layout.txt` files in `.ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/`, with retained native files available and retained page-144-render.png inspected visually. Engine recorded by curator: legacy native/layout extraction and PNG rendering, version unavailable. All aids are reused unchanged; no new extraction, rendering, or OCR was required. No scientific coverage gap. Sources, aids, and other agents' files were preserved. No Office/workbook/CSV units occur in this scope, so formulas versus cached values are not applicable.

The preceding SAP continues through p143, followed by otherwise blank p144. Its title/version/date are outside this shard and must be joined to the pp97–128 shard without inference from bundle contents-page ranges. The final SAP begins with its actual cover at PDF p145: Version 2.0, September 9, 2022. Contents-page pointers are recorded as pointers only; all evidence below uses actual PDF pages. The source page footers match these physical page numbers.

## Exact per-page coverage and evidence relationships

Local evidence IDs are source-prefixed; final global N/S identifiers are assigned downstream. Main-paper matching keys name the intended comparison, without importing main-paper values or diagnosing findings.

| Evidence ID | PDF page and exact printed location | Complete result-relevant extraction or explicit no-applicable record | Main-paper matching key |
|---|---|---|---|
| DOC003-129-A | [p129](../../../joi240088supp2_prod_1746815064.36071.pdf#page=129), lines2115–2122 | Contents continuation only. Statistical Analysis pointer139; demographic/baseline139; primary efficacy139; secondary efficacy140; safety141; concomitant medication142; references142. No new quantitative design or result. | SAP section navigation only |
| DOC003-130-A | [p130](../../../joi240088supp2_prod_1746815064.36071.pdf#page=130), §§1–3.2, lines2123–2144 | SAP based on protocol plus subsequent amendments. Objective: superiority of balloon angioplasty+AMM over AMM alone in high-risk sICAS. Primary composite: ischemic/hemorrhagic stroke or all-cause death within30 days after enrollment OR after qualifying-lesion balloon angioplasty during follow-up; OR any ischemic stroke or qualifying-artery revascularization beyond30 days through12 months after enrollment. §3.1 repeats stroke/death30-day and late ischemic stroke/revascularization12-month formulation. First secondary: target-territory any stroke or all-cause death90 days. | Primary composite, peri-procedural window, superiority, secondary hierarchy |
| DOC003-131-A | [p131](../../../joi240088supp2_prod_1746815064.36071.pdf#page=131), §3.2–3.3, lines2145–2165 | Remaining secondary endpoints: outside-target-territory any stroke90 days; mRS90 days; target-territory any stroke or all-cause death12 months; qualifying-artery revascularization1 year; outside-target any stroke12 months; mRS12 months; target-artery restenosis12 months (>70% stenosis OR increase30% on follow-up neurovascular imaging); stroke/MI/vascular-death composite12 months; EQ-5D quality of life12 months. Safety from enrollment to1 year: blood pressure, heart rate, respiratory rate, temperature; RBC/WBC/platelets/hemoglobin and biochemical tests listed below. | All secondary outcomes, restenosis threshold, quality of life, safety |
| DOC003-132-A | [p132](../../../joi240088supp2_prod_1746815064.36071.pdf#page=132), §§3.3–5.1, lines2166–2185 | Safety laboratory continuation: urea nitrogen, creatinine, coagulation, hepatic/renal function, fasting glucose, HbA1c; AEs and SAEs. Hypothesis50% relative primary-endpoint risk reduction over12 months. Prospective multicenter randomized open-label blinded-endpoint PROBE; recent TIA<90 days or ischemic stroke21–90 days attributed to70–99% major intracranial atherosclerotic stenosis, anterior/posterior circulation; randomization1:1. Center procedural consistency check videos3–5 angioplasty cases. | Hypothesis, eligibility window/stenosis, randomized groups |
| DOC003-133-A | [p133](../../../joi240088supp2_prod_1746815064.36071.pdf#page=133), §§5.1–5.2, lines2186–2206 | Experimental balloon angioplasty+same AMM as control; control AMM alone. Aspirin100mg daily entire follow-up; clopidogrel75mg daily first90 days, continuation individualized thereafter; ticagrelor/cilostazol substitution for resistance. Atorvastatin20–80mg/day1 year, titrated LDL<1.8mmol/L or<70mg/dL; later continuation individualized. BP130–140/90–100mmHg. First100 participants complete30-day peri-operative AE observation, followed by investigator discussion of feasibility/continuation. Analyses after database lock, violation identification and treatment unblinding; Full Analysis and Per Protocol membership by SAP rules. | Intervention dose/duration, AMM targets, safety monitoring, analysis populations |
| DOC003-134-A | [p134](../../../joi240088supp2_prod_1746815064.36071.pdf#page=134), §§5.2–7.1, lines2207–2227 | Dummy-code subset data displays for pre-programming without unblinding. Interim when half complete12-month visit; interim alpha1=.0015; final alpha2=.024. Sample-size assumptions: SAMMPRIS-derived12.2%1-year target-vessel stroke/death;50% relative reduction to6.1%;686 cases,80% power,two-sided alpha=.05. O'Brien–Fleming spending described as6% expansion of total type I error; SAS-calculated interim requirement728;10% lost follow-up; final802. ITT includes randomized participants who receive study intervention, analyzed by assigned intervention. | Interim/stopping, sample-size calculation, efficacy population |
| DOC003-135-A | [p135](../../../joi240088supp2_prod_1746815064.36071.pdf#page=135), §§7.1–8, lines2228–2247 | ITT primary efficacy population. PPS subset FAS(mITT): treatment finished OR no serious protocol violation; serious violations finalized at review, criteria protocol compliance, good compliance, no prohibited drugs, completed CRF contents; partial violators retained until violation; PPS secondary endpoint data set. ATS randomized with more than one use of study products, analyzed by received intervention; secondary data set. SS at least1-time product use plus available safety assessment. | ITT/mITT, PPS, ATS, SS definitions and sensitivity denominators |
| DOC003-136-A | [p136](../../../joi240088supp2_prod_1746815064.36071.pdf#page=136), §§8–9.2, lines2248–2271 | Primary contrast repeats30-day stroke/death and late12-month ischemic stroke/revascularization, angioplasty+AMM vs AMM. SAS9.4; statistics two-sided,P<.05. Main analyses without center adjustment; center-adjusted analysis sensitivity, smaller centers pooled into larger to reasonable size, Cox HR for center-adjusted treatment effect. Subgroup primary-outcome rates and interaction tests planned. | Primary inferential method/sidedness, center sensitivity, interactions |
| DOC003-137-A | [p137](../../../joi240088supp2_prod_1746815064.36071.pdf#page=137), §§9.3–10.3, lines2272–2295 | One primary variable, others secondary/other; one treatment comparison; no multiple-comparison or multiple-endpoint adjustment. Withdrawal visit assigned to next scheduled visit regardless of window; summarize reasons. Withdrawal with >=1 post-baseline measure for endpoint included; no post-randomization visits excluded from every endpoint analysis. Event rate=sum events across all patients / sum treatment periods across all patients, with number of people and person-time documented. | Multiplicity, missingness/exclusion, event-rate denominator |
| DOC003-138-A | [p138](../../../joi240088supp2_prod_1746815064.36071.pdf#page=138), §§10.3–11.2, lines2296–2321 | Kaplan–Meier for stroke or combined vascular events; first event if repeated same type; censor at study termination or death if no event. Counts planned for analysis populations, PP exclusions, clinic visits, randomized/completed/withdrawn and reasons pre/post randomization; deviations listing. Violators included FAS(mITT), excluded PP; full violation excludes all PP data, partial excludes selected data; prohibited treatment/concomitant medication retains only data before violation, with treatment start reference date. | Survival censoring, participant flow, PP data rules |
| DOC003-139-A | [p139](../../../joi240088supp2_prod_1746815064.36071.pdf#page=139), §§11.2–12.2, lines2322–2343 | Final violation exclusion list agreed by study team. Baseline age/sex/height/weight/vital signs, medical/medication/stroke/TIA history; continuous median/IQR, categorical n(%); Wilcoxon rank-sum continuous; chi-square/Fisher categorical. Primary composite rates and95%CIs Kaplan–Meier, log-rank comparison; Cox HR95%CI. Main ITT; PP AND ATS sensitivity analyses; all three sets used for primary efficacy; differences warrant detailed analysis. | Baseline summaries/tests, primary KM/log-rank/Cox, PP/ATS sensitivity |
| DOC003-140-A | [p140](../../../joi240088supp2_prod_1746815064.36071.pdf#page=140), §12.2–12.3, lines2344–2365 | Prespecified subgroups: age<65/≥65; men/women; hypertension yes/no; diabetes yes/no; smoking yes/no; eGFR<60/≥60mL/min/1.73m²; stenosis<80/≥80%; BMI<25,25–30,≥30kg/m²; hypoperfusion CTP/ASITN-SIR collateral scale; anterior/posterior circulation; ischemic stroke/TIA mechanism. Separate Cox model per treatment-by-subgroup interaction, significance testing and forest plot. Secondary target-territory stroke/all-cause death90 days and12 months begins. | Prespecified subgroup inventory and interaction model |
| DOC003-141-A | [p141](../../../joi240088supp2_prod_1746815064.36071.pdf#page=141), §§12.3–12.4, lines2366–2386 | Target-territory stroke/death90 days,12 months: Cox HR95%CI; outside-target stroke90 days,12 months: Cox HR95%CI. mRS90 days,12 months: ordinal logistic common OR. Restenosis12 months >70% OR increase30%: logistic OR95%CI. Stroke/MI/vascular death12 months: Cox HR95%CI. EQ-5D12 months: Student t or Wilcoxon rank-sum as appropriate. AE coding MedDRA26 or later by system organ class. | Each secondary effect measure/model; mRS common OR; AE coding |
| DOC003-142-A | [p142](../../../joi240088supp2_prod_1746815064.36071.pdf#page=142), §§12.4–13, lines2387–2408 | AE subjects n/% by organ class/preferred term; Fisher exact compares each grouped AE. SAE summaries and all-death/SAE case narratives; treatment-period deaths n and Fisher exact; vital-sign description/comparison at different times. Concomitant medications listed: antiplatelet aspirin/clopidogrel/ticagrelor/cilostazol, anticoagulants, statins, antihypertensives (diuretics, ACE inhibitors, ARBs, beta-blockers, calcium antagonists, central alpha agonists, vasodilators); chi-square/Fisher counts comparison. Reference list begins, no additional trial result. | Safety denominator/tests, death tests, medication summaries |
| DOC003-143-A | [p143](../../../joi240088supp2_prod_1746815064.36071.pdf#page=143), §13, lines2409–2430 | Reference continuation only: bibliographic citations; no result-relevant study-specific quantities or statistical design. No-applicable quantitative unit explicitly mapped. | None |
| DOC003-144-A | [p144](../../../joi240088supp2_prod_1746815064.36071.pdf#page=144), lines2431–2432 | Otherwise blank: BASIS header, grant identifier2017YFC1307900, line numbers and footer144 only. Retained render inspected visually. No-applicable quantitative unit explicitly mapped. | None |
| DOC003-145-A | [p145](../../../joi240088supp2_prod_1746815064.36071.pdf#page=145), SAP cover, lines2433–2454 | Final SAP actual cover: Balloon Angioplasty vs Aggressive Medical Management for Symptomatic Intracranial Artery Stenosis, BASIS; Version2.0; September9,2022. PIs Zhongrong Miao/Yilong Wang; prepared by Peking University Clinical Research Institute Biostatistics. No new statistical result. | Version/date and disclosed analysis-plan provenance |
| DOC003-146-A | [p146](../../../joi240088supp2_prod_1746815064.36071.pdf#page=146), contents, lines2455–2484 | Navigation only: Introduction/objective/endpoints148;safety/hypothesis150;design151;planned/interim152;sample size153;analysis populations153–154;treatment/general155;subgroup/multiplicity/missing156;event rates/time-to-event157;disposition/deviations158. TOC population wording Full Analysis Set(FAS),Modified Intention-to-treat(m-ITT) points153. No new quantitative outcome. | Analysis-population navigation label |
| DOC003-147-A | [p147](../../../joi240088supp2_prod_1746815064.36071.pdf#page=147), contents, lines2485–2492 | Navigation only: analysis/baseline/primary159;secondary160;safety/concomitant162;references163. No-applicable quantitative design unit explicitly mapped. | None |
| DOC003-148-A | [p148](../../../joi240088supp2_prod_1746815064.36071.pdf#page=148), §§1–3.2, lines2493–2514 | Version2.0 based on protocol plus amendments. Superiority objective and primary composite repeat: stroke/all-cause death within30 days of enrollment or qualifying-lesion angioplasty during follow-up; late qualifying-artery ischemic stroke/revascularization >30 days through12 months. Secondary list starts any stroke or all-cause death30 days after enrollment/procedure (continued149). | Primary composite and30-day secondary status |
| DOC003-149-A | [p149](../../../joi240088supp2_prod_1746815064.36071.pdf#page=149), §3.2, lines2515–2536 | Completes30-day any-stroke/death procedural window. Secondary: target-territory stroke/death90 days;outside-target stroke90 days;mRS90 days;target-territory stroke/death12 months;target revascularization12 months;outside-target stroke12 months;mRS12 months;restenosis12 months >70% OR increased30%;stroke/MI/vascular death12 months;EQ-5D12 months;target-territory stroke/death24 months;outside-target stroke24 months continued150. | Full secondary outcome hierarchy/time points |
| DOC003-150-A | [p150](../../../joi240088supp2_prod_1746815064.36071.pdf#page=150), §§3.2–4, lines2537–2558 | Secondary continuation: outside-target stroke24 months;mRS24 months;stroke/MI/vascular death24 months;target-territory stroke/death36 months;outside-target stroke36 months;neurological improvement mRS36 months;stroke/MI/vascular death36 months. Safety enrollment–1year,vitals,laboratory list,AEs/SAEs. No hypothesis numbers on this page (continue151). | Long-term secondary outcome status; safety window |
| DOC003-151-A | [p151](../../../joi240088supp2_prod_1746815064.36071.pdf#page=151), §§4–5.1, lines2559–2580 | Hypothesis50% primary-risk reduction over12months. PROBE prospective multicenter randomized trial; recent TIA/stroke attributed70–99% DSA intracranial stenosis; arteries ICA C4–C7,MCA M1,VA V4,BA.1:1 allocation;angioplasty+AMM vs AMM alone.3–5case procedural videos;aspirin100mg/day entire follow-up (continues152). | Hypothesis,eligibility,allocation,intervention |
| DOC003-152-A | [p152](../../../joi240088supp2_prod_1746815064.36071.pdf#page=152), §§5.1–5.3, lines2581–2603 | Clopidogrel75mg/day90days then individualized;resistance substitutions ticagrelor/cilostazol;atorvastatin20–80mg/day1year,LDL<1.8mmol/L or<70mg/dL;BP130–140/90–100mmHg. First100 participants30-day peri-operative AE review and feasibility discussion. SAP analyses after lock/violation identification/unblinding;dummy-code subset programming displays without unblinding. Interim section heading only, rules continue153. | AMM dose/targets,database lock,safety monitoring |
| DOC003-153-A | [p153](../../../joi240088supp2_prod_1746815064.36071.pdf#page=153), §§5.3–7.1, lines2604–2625 | No interim analyses;DSMB independent statistician summaries enrollment/status/baseline/safety/coded SAEs at regular intervals;may recommend modification/premature stop for safety,Steering Committee+Sponsor decide. Sample-size:medical15%,angioplasty7%,absolute difference8%;512 total,256/group;80% power;one-sided alpha2.5%;10% dropout. §7.1 heading ITT;randomized and intervention received (continues154). | Final interim/stopping rules,sample-size assumptions,population |
| DOC003-154-A | [p154](../../../joi240088supp2_prod_1746815064.36071.pdf#page=154), §§7.1–7.4, lines2626–2646 | ITT by randomized intervention,primary efficacy. PPS subset FAS(mITT),finished treatment OR no serious violation;criteria protocol adherence,compliance,no prohibited drugs,completed CRF;partial violations retain until violation,serious criteria finalized at review. ATS randomized with more than one product use,by received treatment;secondary data set. SS at least1-time product use+available safety assessment. | ITT/mITT/PPS/ATS/SS denominators |
| DOC003-155-A | [p155](../../../joi240088supp2_prod_1746815064.36071.pdf#page=155), §§7.4–9.1, lines2647–2666 | Safety-set definition completion. Primary contrast repeats30-day stroke/death and late12-month qualifying-artery stroke/revascularization;angioplasty+AMM vs AMM. SAS9.4;two-sided P<.05 significance. Center adjustment statement begins:main analyses won't consider center effects. | Primary contrast,sidedness/significance,center adjustment |
| DOC003-156-A | [p156](../../../joi240088supp2_prod_1746815064.36071.pdf#page=156), §§9.1–10.1, lines2667–2687 | Center-adjusted sensitivity analysis;small centers pooled into larger;Cox HR considering center adjustment. Subgroup rates and interaction tests. Single primary variable,other efficacy secondary/other;one comparison;no adjustment for multiple comparisons/endpoints. Withdrawal heading/text starts,continued157. | Center sensitivity,multiplicity,subgroup testing |
| DOC003-157-A | [p157](../../../joi240088supp2_prod_1746815064.36071.pdf#page=157), §§10.1–11, lines2688–2708 | Withdrawal visit allocated next scheduled visit regardless of window;reasons summarized. Withdrawal with >=1post-baseline endpoint measure included;no postrandomization visits excluded from all endpoint analyses. Rate=sum events / sum treatment periods for all patients;people/person-time documented. Kaplan–Meier stroke/composite vascular events;first event;event-free censoring study termination/death. | Missingness,efficacy exclusions,event-rate formula,censoring |
| DOC003-158-A | [p158](../../../joi240088supp2_prod_1746815064.36071.pdf#page=158), §§11.1–11.2, lines2709–2730 | Population sizes,PP exclusions,visit contributors,randomized/completed/withdrawn and reasons,eligibility deviations displays. Violators included FAS(mITT),excluded PPS;full removes whole subject,partial selected data;prohibited medication uses pre-violation data,treatment-start reference date. | Flow denominators and PP partial censoring |
| DOC003-159-A | [p159](../../../joi240088supp2_prod_1746815064.36071.pdf#page=159), §§11.2–12.2, lines2731–2752 | Final PP violation list agreed by team. Baseline demographics/history summarized median/IQR,n(%),Wilcoxon continuous,chi-square/Fisher categorical. Primary composite KM event rates95%CIs,log-rank,Cox HR95%CI. Main ITT;PP sensitivity named;ITT,PPS AND ATS all specified for primary efficacy;different results detailed (continued160). | Baseline methods,primary survival models,PP/ATS analyses |
| DOC003-160-A | [p160](../../../joi240088supp2_prod_1746815064.36071.pdf#page=160), §§12.2–12.3, lines2753–2774 | PP/ATS differences from ITT require detailed analysis. Separate Cox treatment-by-subgroup models,significance tests,forest plot. All11 subgroup factors repeat exact thresholds listed onp140. Secondary method section begins any-stroke/death within30days;continues outside shard on161. | Subgroup prespecification,primary sensitivities,30-day secondary method |

## Consolidated outcome lists and model identities

The preceding SAP supplies10 secondary endpoint items (p130 first,p131 remaining). Version2.0 supplies19 items (p148 first,p149 ten further complete items plus beginnings,p150 completes later items):30-day stroke/death;90-day territory stroke/death,outside-territory stroke,mRS;12-month territory stroke/death,revascularization,outside-territory stroke,mRS,restenosis,vascular composite,EQ-5D;24-month territory stroke/death,outside-territory stroke,mRS,vascular composite;36-month territory stroke/death,outside-territory stroke,mRS improvement,vascular composite. Neither list labels an item as key secondary within assigned pages. All are secondary by heading. Primary late stroke/revascularization remains separate from early any-stroke/death and their secondary components.

Preceding-SAP model mapping: primary KM event probability95%CI/log-rank/Cox HR95%CI;secondary territory stroke/death,outside-territory stroke,and stroke/MI/vascular-death use Cox HR95%CI;ordinal mRS uses common OR from ordinal logistic regression;restenosis logistic OR95%CI;EQ-5D t-test/Wilcoxon. Version2.0 secondary methods mostly fall outside this shard and are deliberately not inferred. Planned primary subgroup model is Cox,one separate interaction model per factor;factor cutoffs copied below exactly as printed:

1. Age <65 vs ≥65years.
2. Sex men vs women.
3. Hypertension yes vs no.
4. Diabetes yes vs no.
5. Smoking yes vs no.
6. eGFR <60 vs ≥60mL/min/1.73m².
7. Target-vessel stenosis <80% vs ≥80%.
8. BMI <25,25–30,≥30kg/m² (printed boundaries preserved).
9. Hypoperfusion: CTP, ASITN/SIR collateral circulation scale (no binary thresholds supplied in these pages).
10. Anterior vs posterior circulation.
11. Mechanism ischemic stroke vs TIA.

Complete safety laboratory list in both versions includes RBC,WBC,platelets,hemoglobin,ALT,AST,alkaline phosphatase,glutamylphthalase,total bilirubin,urea nitrogen,serum creatinine,coagulation,hepatic/renal functions,fasting glucose,HbA1c. Laboratory names are recorded as supplied; no statistical finding is inferred from wording. Safety AE/SAE status is distinct from secondary efficacy outcome status.

## Downstream statistical relationship handoff

All statistical-design relationships above require matching to the main-paper methods and reported results. Preserve the original-versus-final plan identities: old interim (.0015/.024,half complete12months),old sample802 with686/728 intermediate values,final no-interim and512/256 sample;these are version-specific facts. Final SAP retains50% hypothesis text alongside15% versus7% planning rates and8%absolute difference;both statements are extracted as printed without diagnosis. Final TOC calls populationFAS/m-ITT while §7.1 callsITT;eligibility requires intervention receipt,withdrawal rules require postbaseline observations,PP/ATS definitions are separately retained. Primary sensitivity text namesPP yet explicitly saysITT,PPS,ATS used;all three factual clauses are preserved. No analysis-choice preference,candidate selection,or classification is made by this mapper.

All assigned pages are COMPLETE. Reusable units32;fresh-required0;mapped32. Explicit no-new-quantitative-content coverage:129,143,144,145,146,147;version/navigation labels on145–146 remain extracted. Missing fresh derivative count0;unresolved scientific coverage gap0. Version1 cover/date and final secondary-method continuation must be linked from neighboring assigned shards,which is a disjoint-scope boundary rather than a coverage omission.


<!-- END support_doc003_pp129-160.md -->

---


<!-- BEGIN support_doc003_pp161-167.md -->

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

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=161)

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

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=162)

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

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=163)

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

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=164)

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

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=165)

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

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=166)

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

[Source page](../../../joi240088supp2_prod_1746815064.36071.pdf#page=167)

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


<!-- END support_doc003_pp161-167.md -->

---

## Current-source glyph confirmation after mapping

Statistical pass1 directly rendered DOC-002p24 at200dpi with CPU PyMuPDF1.26.4. TableS11 footnote b visually reads mRS≥2 for disabling stroke, matching the main article p3. The >2 reading preserved in the retained extraction/map text is a glyph transcription discrepancy, not a source-level definition conflict. The raw eligible transcription remains preserved above; all reviewers are notified to use current PDF/image authority. Image locator: preprocessing/stat1-supp-p24.png (see actual preprocessing path if nested).
