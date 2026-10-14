# Main-paper quantitative evidence map

Scope: DOC-001, jama_sun_2024_oi_240088_1746815064.14747.pdf, PDF pages 1-11 (printed pages 1059-1069). Document role REPORT. All 11 units mapped; no scientific coverage gap. This artifact reconstructs source evidence without candidate diagnosis or judgments. B denotes balloon angioplasty plus aggressive medical management; M denotes aggressive medical management alone. Unless a row explicitly says otherwise, percentages use B n=249 and M n=252, follow-up is 1 year, comparison is B versus M, and CIs are 95%. A count is not a person-time rate unless the source specifies one; no person-time totals, test statistics, or standard errors are printed in this article.

Controls read: QUALITY_CONTROL_SCOPE.md in full, workflow_1_6_2/review_contract.md in full, tooling_record.md, source_inventory.md, source_coverage.md, coverage_manifest.md, evidence_asset_inventory.md. Both curator prerequisite files were present before source mapping. No prior candidate, checker, recheck, disposition, classification, screening or report record was read.

Evidence aids: every individual `document_outputs/basis_main_article/extraction/native_pages/page-NNN.txt` for pages 001-011, recorded legacy pdftotext layout output. Retained exact page images `document_outputs/basis_main_article/extraction/page_images/page-005-05.png` through `page-009-09.png` were inspected visually, including complete table/figure bodies and footnotes. Direct-current-source confirmation used the pinned fallback interpreter with `pdf_tools.py text SOURCE --first 6 --last 8 /dev/stdout --layout`, engine PyMuPDF 1.26.4 sorted reading order. No persisted new derivative or OCR. Tool capabilities used: text, layout. Source printed readings below preserve signs and decimals.

All source links below resolve from this extraction artifact using `../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=N`.

## Page coverage

| PDF page | Printed page | Complete inspected content | Status |
|---|---|---|---|
| 1 | 1059 | Title, abstract, design/interventions/endpoints/results/conclusions, publication metadata | COMPLETE |
| 2 | 1060 | Background, Key Points, trial design, participants, randomization/blinding, procedure beginning | COMPLETE |
| 3 | 1061 | Procedure continuation, all primary/secondary outcome definitions, adverse events, original/revised sample size | COMPLETE |
| 4 | 1062 | Sample-size amendment continuation, full statistical analysis, patient population, primary results beginning | COMPLETE |
| 5 | 1063 | Figure 1 all boxes, primary/secondary narrative, post hoc narrative beginning | COMPLETE |
| 6 | 1064 | Table 1 every row and footnote, post hoc narrative continuation, adverse events | COMPLETE |
| 7 | 1065 | Figure 2 every subgroup/interaction/footnote, deaths and complications, Discussion beginning | COMPLETE |
| 8 | 1066 | Table 2 every row and footnote, Discussion continuation | COMPLETE |
| 9 | 1067 | Figure 3 axes/risk table/annotations/footnote, all quantitative Discussion comparisons | COMPLETE |
| 10 | 1068 | Event-free statement, limitations, conclusions, article information and disclosures | COMPLETE |
| 11 | 1069 | References only; no applicable original-study quantitative relationship | COMPLETE; NO_APPLICABLE_ORIGINAL_RESULT |

## Numeric relationships

Each row is one numeric relationship containing all displayed quantities for that coherent result or partition. Statistical counterparts cross-reference these rows; they do not duplicate numeric relationship IDs.

| ID | Exact REPORT location | Printed quantities and associated definition | Matching occurrences / linkage |
|---|---|---|---|
| N001 | [p1 abstract](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=1) | 512 randomized; 501 confirmed eligible and completed trial; mean age 58.0 years; 158 women (31.5%); B249, M252 | p4 population; Figure 1 p5; Table 1 p6; p2 Key Points 501 |
| N002 | [p4 population](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=4) | 1409 assessed, 512 randomized, 256 each; 11 excluded attributed to consent withdrawal; 501 primary, M252/B249; 258/501 (51.5%) from lead center | Figure 1 p5 reasons separately; p10 more than half lead-center participants |
| N003 | [p5 Figure 1 screening](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5) | 1409 assessed; 897 excluded: 326 no consent, 238 severe stenosis outside target, 89 qualifying event ≤2 wk, 73 stenosis <70%, 46 target occlusion, 43 dual-antiplatelet intolerance/bleeding, 35 contrast allergy, 24 aneurysm/vascular malformation, 23 another study; 512 randomized | p4 assessed/randomized narrative |
| N004 | [p5 Figure 1 B flow](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5) | 256 randomized; 7 withdrew consent; 249 primary; 16 adjudication exclusions: 7 crossover, 4 stroke <2wk, 2 tandem lesion, 1 length >15mm, 1 direct balloon-expanding stent without balloon first, 1 target occlusion; 233 per-protocol | p4 population/analysis definitions |
| N005 | [p5 Figure 1 M flow](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5) | 256 randomized; 3 withdrew consent, 1 not successfully recruited but assigned randomization number; 252 primary; 14 adjudication exclusions: 5 crossover, 2 stroke <2wk, 1 tandem lesion, 2 length >15mm, 2 stenosis <70%, 1 target occlusion, 1 aneurysm; 238 per-protocol | p4 population/analysis definitions |
| N006 | [p4 baseline narrative](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=4) | Median age 58.0 (52.0-65.0); 343 male (69.1%); 494 Han Chinese (98.6%); TIA 78 (15.6%), stroke423 (84.4%) | N001 mean age/women; Table1 groups |
| N007 | [p4 ischemic mechanism](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=4) | Among stroke423: embolism135 (31.9%), isolated border zone69 (16.3%), perforator42 (9.9%), mixed177 (41.8%); mixed-mechanism border zone100; total border zone169 (40.0%); M40.9%, B39.1% | Table1 nested stroke mechanisms; Discussion p9 B39%, M40.9% |
| N008 | [p4 stenosis narrative](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=4) | 60%-69%:2 (0.4%); 70%-79%:289 (57.6%); 80%-89%:163 (32.5%); 90%-99%:45 (9.0%); 100%:2 (0.4%) | Table1 p6 |
| N009 | [p6 Table1 age](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6) | Median age years B58.0 (52.0-65.0), M58.0 (52.0-65.0) | p4 pooled median; p1 mean |
| N010 | p6 Table1 sex | Male B172 (69.1), M171 (67.9); female B77 (30.1), M81 (32.1) | p1 women158 (31.5); p4 male343 (69.1); Figure2 denominators |
| N011 | p6 Table1 history | Hypertension B181 (72.7), M185 (73.4); hyperlipidemia176 (70.7),191 (75.8); diabetes82 (32.9),87 (34.5) | Figure2 hypertension/diabetes denominators |
| N012 | p6 Table1 prior treatment | Antiplatelet before latest event B118 (47.4), M113 (44.8); statin123 (49.4),126 (50.0) | Supplement medication baseline locators eTable3 |
| N013 | p6 Table1 current smoking | B60 (24.1), M66 (26.2) | Figure2 smoking denominators |
| N014 | p6 Table1 qualifying event | TIA B34 (13.7), M44 (17.5); ischemic stroke B215 (86.4), M208 (82.5) | N006 pooled; Figure2 mechanism; Discussion B86% |
| N015 | p6 Table1 stroke subtypes | Within B215/M208 stroke: embolism78 (36.3)/57 (27.4); isolated border zone37 (17.2)/32 (15.4); perforator18 (8.4)/24 (12); mixed82 (38.1)/95 (45.7) | N007 pooled counts; Table1 footnote a definitions |
| N016 | p6 Table1 artery | MCA143 (57.4)/154 (61.1); basilar73 (29.3)/73 (29.0); internal carotid21 (8.4)/8 (3.2); vertebral12 (4.8)/17 (6.8) | Figure2 anterior/posterior denominators |
| N017 | p6 Table1 mRS | Admission mRS0-1 B227 (91.2), M231 (91.7); scale0-6, higher disability | Eligibility mRS<3 p2; outcome scale p3/p8 |
| N018 | p6 Table1 NIHSS | Median (IQR) B0 (0-2), M0 (0-2); 0-1:186 (74.7)/187 (74.2); 2-4:51 (20.5)/51 (20.5); 5-10:12 (4.8)/14 (5.6); scale0-42 higher neurologic deficit | Full three-bin partition and footnote c |
| N019 | p6 Table1 stenosis | 60%-69% B0/M2 (0.8); 70%-79%140 (56.2)/149 (59.1); 80%-89%83 (33.3)/80 (31.7); 90%-99%25 (10.4)/20 (7.9); 100%1 (0.4)/1 (0.4); WASID assessment | N008 pooled; Figure2 <80/≥80 |
| N020 | p6 Table1 timing | Days median(IQR) last event to randomization B34.0 (21.0-53.0)/M32.0 (22.0-51.0); TIA33.0 (21.0-56.0)/33.0 (19.0-47.0); stroke34.0 (20.0-51.0)/32.0 (22.0-51.0) | p4 all-event timing; p9 stroke34 (20-51) |
| N021 | p4 procedure timing | B days enrollment/randomization to procedure median2 (1-2) | p3 recommended ≤3 business days |
| N022 | [p8 Table2 primary](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8) | Composite B11 (4.4)/M34 (13.5); first event only; component overlap 1 B patient,10 M patients; separately counted components | p1 abstract, p2 Key Points, pp4-5 narrative, Figure2 overall, Figure3 |
| N023 | p8 Table2 components | Stroke/death≤30d B8 (3.2)/M4 (1.6); qualifying ischemic stroke>30d-1y1 (0.4)/19 (7.5); revascularization>30d-1y3 (1.2)/21 (8.3) | p1 abstract, pp5-6 post hoc narrative; footnote b separate components |
| N024 | p8 Table2 secondary 90d | Stroke qualifying territory/death7 (2.8)/10 (4.0); stroke outside territory2 (0.8)/0; mRS median0 (0-0)/0 (0-1) | Outcome definitions p3 |
| N025 | p8 Table2 secondary 1y | Stroke qualifying territory/death8 (3.2)/23 (9.1); revascularization4 (1.6)/24 (9.5); stroke outside3 (1.2)/4 (1.6); mRS median0 (0-0)/0 (0-1) | p5 narrative key results; p9 M9.1% discussion |
| N026 | p8 Table2 vascular events | Composite10 (4.0)/26 (10.3); stroke9 (3.6)/26 (10.3); MI0/0; vascular death1 (0.4)/0 | p5 composite narrative; component first-event logic p4 |
| N027 | p8 Table2 QoL | EuroQol-5-Dimensions at1y median100 (100-100) both groups | p3 scale0-100, low worse/high better |
| N028 | p8 footnotes d,g | Stroke≤30d B7/249 (2.8), M4/252 (1.6); death≤30d B1/249 (0.4), M0; death≤1y B1/249 (0.4), M1/252 (0.4) | p7 Bdeath sICH≤30d, Mdeath vehicle crash>30d-1y; p4 two deaths and follow-up completeness |
| N029 | p5 revascularization narrative | >30d-1y B1 acute occlusion +2 elective hard TIA; M1 acute occlusion +10 elective hard TIA +10 elective ischemic stroke | N023 3/21; p9 M10/21 (47.6%) hard TIA |
| N030 | p5 restenosis narrative | B restenosis≤1y15.7%; TIA/stroke clearly related2.0% | eTable4 supplement locator; p3 definition >70% or increase30% |
| N031 | pp1,6 hemorrhage narrative | sICH B1.2%, M0.4%; asymptomatic ICH B1.2%, M0%; procedural complications B17.4% (abstract) | eTable4/11 supplement locators; p7 deaths |
| N032 | p6 disabling stroke | B2.4%, M7.1%; P=.02 (statistical S047) | Definition mRS≥2 at1y p3; eTable11 locator |
| N033 | p7 complications; pp1,8 dissection | Bvasospasm1.2%; dissection14.5%; pseudoaneurysm0.0%; occlusion0.4%; perforation0.4%; rupture0.0%; hemorrhage0.4%; thrombosis1.7% | eTable4 locator; p9 rescue stenting71.4% with dissection, impaired distal flow mTICI<2b |
| N034 | [p7 Figure2 age](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=7) | <65 B9/176 (5.1), M23/187 (12.3); ≥65 B2/73 (2.7), M11/65 (16.9) | S020,S021; B249/M252 partition |
| N035 | p7 Figure2 sex | Male5/172 (2.9),19/171 (11.1); female6/77 (7.8),15/81 (18.5) | Table1; S022,S023 |
| N036 | p7 Figure2 hypertension | Yes9/181 (5.0),25/185 (13.5); no2/68 (2.9),9/67 (13.4) | Table1; S024,S025 |
| N037 | p7 Figure2 diabetes | Yes4/82 (4.9),13/87 (14.9); no7/167 (4.2),21/165 (12.7) | Table1; S026,S027 |
| N038 | p7 Figure2 smoking | Yes1/60 (1.7),7/66 (10.6); no10/189 (5.3),27/186 (14.5) | Table1; S028,S029 |
| N039 | p7 Figure2 eGFR | <60 mL/min/1.73m²5/88 (5.7),16/96 (16.7); ≥60 6/161 (3.7),18/156 (11.5) | S030,S031 |
| N040 | p7 Figure2 stenosis | <80%5/140 (3.6),15/151 (9.9); ≥80%6/109 (5.5),19/101 (18.8) | Table1; S032,S033 |
| N041 | p7 Figure2 BMI | <25 3/110 (2.7),17/110 (15.5); ≥25 8/139 (5.8),17/142 (12.0); kg/m² | S034,S035 |
| N042 | p7 Figure2 hypoperfusion | Yes4/103 (3.9),16/106 (15.1); no1/19 (5.3),0/21; assessed CT perfusion; stages3/4 decompensated | Only assessed subset, not full population; S036,S037 |
| N043 | p7 Figure2 location | Anterior9/164 (5.5),21/162 (13.0); posterior2/85 (2.4),13/90 (14.4) | Table1 arteries; S038,S039 |
| N044 | p7 Figure2 mechanism | TIA1/34 (2.9),6/44 (13.6); stroke10/215 (4.7),28/208 (13.5) | Table1 qualifying events; S040,S041 |
| N045 | [p9 Figure3 risk table](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=9) | Days0,60,120,180,240,300,365; B249,241,240,240,240,239,238; M252,236,232,228,226,222,218; cumulative incidence %, main y0,20,40,60,80,100; inset0,5,10,15 | Kaplan-Meier primary, S001,S042,S043; no interpolation or event reconstruction from plotted curve |
| N046 | p9 Discussion comparisons | BASIS stroke-onset enrollment34 (20-51)d >14d; prior trials SAMMPRIS7 (4-16),VISSIT9 (0-42),CASSISS38 (27-75); experimental qualifying stroke BASIS86%,prior63%,62%,51%; border zone B39%,prior37% and20%; Mborder zone BASIS40.9%,CASSISS21.0%; M1y event BASIS9.1%,CASSISS7.2% | Historical comparison statements only, not external data verified; source N007,N014,N020,N025 |
| N047 | [p10 discussion](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=10) | More than85% of M event-free/no revascularization at1y; more than half enrolled from lead center | N022 13.5% primary; N00251.5% lead center |
| N048 | pp1-3 eligibility/intervention/time | 31 centers; age35-80; TIA<90d or stroke14-90d; stenosis70%-99%; ≥1 antithrombotic/risk management; exclude thrombolysis or worsening≤24h, other severe stenosis70%-99%, parent>50%, baseline mRS≥3; random1:1, center-stratified blocks4 | Design/population definitions for all outcomes; recruitment Nov8,2018-Apr2,2022, final Apr3,2023 |
| N049 | pp2-3 dose/targets/follow-up | Aspirin100mg daily entire follow-up; clopidogrel75mg daily90d; replacement ticagrelor/cilostazol for ADP platelet aggregation>40% or CYP2C19 loss-of-function; BP≤140/90mmHg; LDL<70mg/dL; HbA1c<7%; balloon≤3business days, inflation50%-70% proximal diameter; visits30±7d,90±7d,6mo±14d,1y±30d then6monthly to3y | Randomized intervention and endpoint-window comparators for supplied PLAN |
| N050 | p2 background | ICAS up to50% ischemic stroke; recurrent risk7.2%-15.1% within1y, up to37% with border zone/poor collaterals; neurointerventionist annual angioplasty>50 | Contextual/historical numbers, no external comparison conducted |

Rows whose location is abbreviated `p6`, `p7`, `p8`, or `p9` use the exact linked page anchors in N009, N034, N022, and N045 respectively.

## Inferential-statistical relationships

N and S labels in this artifact are **MAIN provisional identifiers only**. Global canonical numeric and statistical IDs are assigned by the checkers after the full evidence merge. These local labels do not impose any support-source scope.

For Table2 rows, incidence difference is percentage points B minus M, explicitly marked post hoc in footnote a. HR column heading prints `HR ratio (95% CI)`; footnote f makes mRS rows generalized ORs rather than HRs. A blank P cell below means no P value printed for that row, not zero. Primary P is specifically a log-rank P; HRs are from Cox models. The paper says similar approaches for secondary outcomes; it does not provide each individual model formula or a CI construction formula for incidence differences.

| Local ID | Exact REPORT source | Result, estimate, interval and test | Related numeric record / narrative |
|---|---|---|---|
| S001 | p8 Table2 primary; pp1,5; p7 Figure2 overall; p9 Figure3 | Primary HR0.32 (0.16-0.63), P<.001; incidence difference−9.1 (−14.0 to−4.1) | N022; statistically significant lower B risk in abstract/Key Points/conclusion |
| S002 | p8 Table2 first component and secondary≤30d; p5 narrative | HR2.05 (0.62-6.81); incidence difference1.6 (−1.1 to4.3); secondary P=.24; component P blank | N023,N028; p9 short-term numerically higher B, not significant |
| S003 | p8 Table2 qualifying ischemic stroke>30d-1y | HR0.05 (0.01-0.39); difference−7.1 (−10.5 to−3.8); P blank; post hoc | N023; pp1,5-6 percentages |
| S004 | p8 Table2 revascularization>30d-1y | HR0.14 (0.04-0.47); difference−7.1 (−10.8 to−3.5); P blank; post hoc | N023,N029 |
| S005 | p8 Table2 qualifying stroke/death90d | HR0.72 (0.27-1.88), P=.49; difference−1.2 (−4.3 to2.0) | N024 |
| S006 | p8 Table2 outside stroke90d | HRNA, P=.15; difference0.8 (−0.3 to1.9) | N024; zero M events |
| S007 | p8 Table2 mRS90d; p5 narrative | Generalized OR1.21 (1.03-1.38), P=.01; incidence differenceNA | N024; >1 favors B more favorable mRS shift |
| S008 | p8 Table2 qualifying stroke/death1y; p5 narrative | HR0.35 (0.16-0.78), P=.01; difference−5.9 (−10.1 to−1.7) | N025 |
| S009 | p8 Table2 revascularization1y; p5 narrative | HR0.16 (0.06-0.47), P<.001; difference−7.9 (−11.9 to−4.0) | N025 |
| S010 | p8 Table2 outside stroke1y | HR0.76 (0.17-3.40), P=.72; printed difference−0.4 (−2.4 to−1.7) | N025; printed sign in upper bound retained as visually read |
| S011 | p8 Table2 mRS1y; p5 narrative | Generalized OR1.26 (1.06-1.45), P=.01; incidence differenceNA | N025; >1 favors B |
| S012 | p8 Table2 combined vascular1y; p5 narrative | HR0.38 (0.19-0.80), P=.01; difference−6.3 (−10.8 to−1.8) | N026 |
| S013 | p8 Table2 combined-event stroke component | Difference−6.7 (−11.1 to−2.3); HR and P blank | N026 |
| S014 | p8 Table2 myocardial infarction | Counts0/0, differenceNA; HR/P blank | N026 |
| S015 | p8 Table2 vascular death | Difference0.4 (−0.4 to1.2); HR/P blank | N026 |
| S016 | p8 Table2 quality of life | P=.40; effect and interval blank | N027 |
| S017 | p6 post hoc center adjustment narrative | Primary HR0.32 (0.16-0.62), P=.001 | Supplement eTable6 locator; compare S001 after matching adjustment |
| S018 | p6 post hoc center interaction narrative | P for treatment-by-center interaction=.10 | eTable7 locator; p10 no interaction stated |
| S019 | p6 composite excluding revascularization | Stroke/death≤30d or after qualifying-lesion balloon or qualifying ischemic stroke>30d-1y: B3.6%/M9.1%; HR0.39 (0.18-0.85), P=.01 | eTable10 locator; p9 M risk remained higher |
| S020 | p7 Figure2 age<65 | HR0.41 (0.19-0.88); age interaction P=.26 | N034 |
| S021 | p7 Figure2 age≥65 | HR0.16 (0.03-0.70); same age interaction P=.26 | N034 |
| S022 | p7 Figure2 male | HR0.26 (0.10-0.68); sex interaction P=.50 | N035 |
| S023 | p7 Figure2 female | HR0.41 (0.16-1.05); same sex interaction P=.50 | N035 |
| S024 | p7 Figure2 hypertension yes | HR0.36 (0.17-0.77); interaction P=.53 | N036 |
| S025 | p7 Figure2 hypertension no | HR0.21 (0.05-0.96); same interaction P=.53 | N036 |
| S026 | p7 Figure2 diabetes yes | HR0.32 (0.10-0.97); interaction P=.99 | N037 |
| S027 | p7 Figure2 diabetes no | HR0.32 (0.14-0.76); same interaction P=.99 | N037 |
| S028 | p7 Figure2 smoking yes | HR0.15 (0.02-1.24); interaction P=.46 | N038 |
| S029 | p7 Figure2 smoking no | HR0.35 (0.17-0.73); same interaction P=.46 | N038 |
| S030 | p7 Figure2 eGFR<60 | HR0.33 (0.12-0.89); interaction P=.95 | N039 |
| S031 | p7 Figure2 eGFR≥60 | HR0.32 (0.13-0.80); same interaction P=.95 | N039 |
| S032 | p7 Figure2 stenosis<80% | HR0.35 (0.13-0.97); interaction P=.74 | N040 |
| S033 | p7 Figure2 stenosis≥80% | HR0.28 (0.11-0.71); same interaction P=.74 | N040 |
| S034 | p7 Figure2 BMI<25 | HR0.17 (0.05-0.57); interaction P=.17 | N041 |
| S035 | p7 Figure2 BMI≥25 | HR0.48 (0.21-1.11); same interaction P=.17 | N041 |
| S036 | p7 Figure2 hypoperfusion yes | HR0.25 (0.08-0.75); interaction P=.99 | N042 |
| S037 | p7 Figure2 hypoperfusion no | HRNA; interaction P=.99; footnote b: no M events so HR estimation NA | N042 |
| S038 | p7 Figure2 anterior | HR0.42 (0.19-0.91); location interaction P=.26 | N043 |
| S039 | p7 Figure2 posterior | HR0.16 (0.04-0.69); same interaction P=.26 | N043 |
| S040 | p7 Figure2 TIA | HR0.21 (0.03-1.75); mechanism interaction P=.67 | N044 |
| S041 | p7 Figure2 stroke | HR0.34 (0.16-0.69); same interaction P=.67 | N044 |
| S042 | p9 Figure3 early landmark annotation | HR2.05 (0.62-6.81) at≤30d; P not printed locally | N045; S002 counterpart |
| S043 | p9 Figure3 late landmark annotation | HR0.10 (0.03-0.31) beyond30d; P not printed locally | N045; distinct composite landmark, not individual S003/S004 components |
| S044 | pp3-4 sample-size calculation | Originally802 (401/arm), control12%, relative reduction50%,1interim; revised512 (256/arm), M15%, B7%, power80%, two-sided alpha.05, attrition10% | Amendment recommended Dec29,2021; approved Feb15,2022; no interim; end-point results inaccessible during reestimation |
| S045 | p4 analysis population/method | Primary all eligible treated analyzed as randomized; PP/as-treated sensitivities; KM/log-rank; Cox HR95% CI; no center adjustment in primary; Schoenfeld-residual PH test P=.12 despite curves cross at30d; post hoc landmark | Every survival relationship; pp5-6 sensitivities said similar, supplemental eTables8/9 |
| S046 | p4 ordinal and missing-data method | Planned ordinal logistic shift90d/12mo; proportional odds not met, switch to assumption-free ordinal approach; generalized OR via Wilcoxon-Mann-Whitney; missing censor last visit; event incidence difference missing cases assumed no event; two deaths otherwise complete1y | S007,S011,N028; no mRS proportional-odds test P printed |
| S047 | p6 disabling stroke narrative | B2.4% vs M7.1%, P=.02; estimate/CI not printed here | N032; eTable11 locator |
| S048 | p4 inferential conventions | All tests2-sided; P<.05 significant; point estimates95% CI; no multiplicity correction planned for secondary tests; CIs unadjusted, not definitive secondary treatment effects; SAS9.4 | Applies to all inferential results |
| S049 | pp3-4 endpoint status and analysis lineage | Full primary/secondary endpoint inventory below; all forest subgroups said prespecified; post hoc individual components, landmark, center adjustment, incidence differences of all endpoints, composite excluding revascularization | Planned/reported design comparator for supplied PLAN; no diagnosis here |

## Endpoint definitions, footnotes and analysis context

Primary at p3: any stroke or death≤30 days after enrollment **or after balloon angioplasty of qualifying lesion**, or qualifying-territory ischemic stroke or qualifying-artery revascularization after30 days through12 months following enrollment. p1 abstract includes the same procedural-window clause; p2 Key Points, Table2 and p10 conclusion use abbreviated enrollment windows. Ischemic stroke defined new focal sudden-onset deficit from cerebral infarct confirmed CT/MRI. sICH: subarachnoid, parenchymal or intraventricular blood on CT/MRI causing new neurologic symptoms>24h or seizure; sICH≤30d enrollment/procedure enters primary.

Revascularization p3: qualifying artery from30d-1y, acute occlusion with deficit requiring IV/IA thrombolysis, thrombectomy or balloon/stent; elective neurologic symptom driven balloon/stent for recurrent qualifying stroke CT/MRI or hard TIA. Hard TIA: recurrent target-territory TIA>10min or new disabling weakness/numbness, dysarthria, diplopia or dystaxia versus baseline. Table2 footnote c additionally lists intracranial-extracranial bypass among acute/elective procedures. Event count first only for composite, each component separate; footnote b specifically attributes component overlap to1 B and10 M patients. No assumption that component totals equal composite totals is made in this map.

Secondary complete p3 list: (1) stroke/all-cause death≤30d enrollment or after balloon during follow-up; (2) qualifying-territory stroke/death90d/1y; (3) outside-territory stroke90d/1y; (4) mRS90d/1y; (5) revascularization1y; (6) restenosis1y (>70% or increase30% on imaging); (7) stroke/MI/vascular death1y; (8) QoL1y EuroQol0-100; (9) target-territory stroke/death24/36mo; (10) outside-territory stroke24/36mo; (11) mRS24mo; (12) stroke/MI/vascular death24/36mo; (13) neurologic improvement by mRS36mo. Article expressly says24/36mo outcomes not reported. No numerical restenosis comparator or mRS complete category distribution is printed in main article; supplement locations are assigned to support mapping.

Adverse events p3: nervous system disorders, sICH, asymptomatic/any ICH, disabling stroke (mRS≥2 at1y), vascular/lymphatic, metabolic/nutritional, infection, surgical/medical, respiratory/thoracic/mediastinal, gastrointestinal, injury/poisoning, neoplasms/cysts/polyps, reproductive/breast. Procedural complication categories vasospasm, dissection, pseudoaneurysm, occlusion, perforation, rupture, hemorrhage, thrombosis. Definitions affect adverse-event extraction; categories have separate printed rates in N031-N033 and must not be automatically summed as exclusive.

Figure2 footnotes p7: BMI weight kg divided by height m squared; eGFR mL/min/1.73m²; CT perfusion for hypoperfusion. Stage1 TTP/MTT/rCBF/rCBV unchanged versus contralateral; stage2 prolonged TTP, MTT/rCBF/rCBV normal/slightly increased; stage3 TTP/MTT prolonged, rCBF decreased, rCBV normal/slightly decreased; stage4 TTP/MTT prolonged and rCBF/rCBV decreased. Stages3/4 hypoperfusion. Forest axis ticks0.015,0.031,0.062,0.125,0.25,0.5,1,2,4; left side B better, right M better, vertical null1. Numerical subgroup P cells are interaction tests for paired subgroup categories, **not** each row's treatment-effect test. Every row has been reconstructed; no significant-result sampling.

Figure3 p9: days since randomization (different wording than enrollment endpoint definition), cumulative incidence %; inset landmark30d dashed line, beyond30d curve starts from landmark origin and contains late HR0.10; entire-period HR0.32, P<.001. Figure caption states curves crossed at30d and post hoc landmark in addition to main analysis. Narrative says short-term B risk numerically higher but nonsignificant; later overall B superiority. Curves are read for direction/label/time, not digitized.

p4 statistical mechanics: censor last follow-up,1y,or withdrawal if no event; first event time if multiple; all subgroup analyses forest said prespecified; planned mRS ordinal logistic replaced for assumption failure. Post hoc list specifically labels individual components, landmark, center adjustment, endpoint incidence differences and composite excluding revascularization. Independent data/safety committee and biostatistics institute described; no unprinted stopping boundary, additional interim estimate or preferred analysis is inferred.

## Matching narrative and external-locator index

Abstract p1 and Key Points p2 share primary4.4%/13.5%,501 participants; pp4-5 primary narrative shares HR0.32 (0.16-0.63),P<.001. Abstract short-term stroke/death3.2%/1.6%, late stroke0.4%/7.5%,late revascularization1.2%/8.3%,sICH1.2%/0.4%,complications17.4%,dissection14.5% link to N023,N031,N033. p5 narrative states all subgroup point estimates favor B, and all estimable Figure2 point estimates are separately retained. p5 secondary narrative matches S002,S007-S009,S011-S012. p6 center-adjusted and alternative-composite results map S017-S019. p9/p10 text reiterates risk directions and center discussion; no additional original-study effect number beyond mapped rows.

Main article's supplied supplement locators: eTable1 expanded baseline; eTables2/12 risk targets3mo/1y; eTable3 antiplatelet/statins baseline3mo/1y; eTable4 procedure complications/restenosis; eTable5 late revascularization reasons; eTable6 adjusted primary; eTable7 center interaction; eTables8/9 PP/as-treated; eTable10 composite removing revascularization; eTable11 adverse events. These are locator relationships only; support source content is not inspected in this disjoint main scope.

## Completion and limitations

50 MAIN provisional numeric relationships and49 MAIN provisional statistical relationships mapped, covering all displayed original-study results and source-grounded statistical definitions. Source units11/11 complete, including references-only page11. All printed baseline/outcome/subgroup rows and footnotes are retained. No new OCR needed, no coverage gap, and no source or reused asset altered. Legacy image/text engine versions are unavailable; retained images and native extraction serve as locators, with direct-source mechanical confirmation remaining mandatory for any registered issue. Historical figures quoted in the supplied article were recorded as contextual claims only; no external literature was used.
