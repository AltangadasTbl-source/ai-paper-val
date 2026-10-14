# Fresh support REPORT quantitative evidence map

Exact scope: DOC-003 physical PDF pages 1-54; DOC-004 physical PDF pages 1-28; DOC-005 physical PDF page 1. All 83 assigned pages mapped. These three documents have REPORT roles by content. Prospective protocol/SAP DOC-002 is outside this disjoint assignment. No candidate selection or diagnosis is performed here.

Methods: retained Poppler pdftotext native/layout extraction for DOC-003 pages 1,6-53; retained versioned layout extraction for pages 2-5,54; retained Poppler native/layout text for DOC-004 and DOC-005. Figure data and table alignment were freshly read from source-matched Poppler pdftocairo 200 dpi rendered pages, with retained RapidOCR CUDA text used only as locator. Visual inspections specifically covered DOC-003 pp.22,44,45,46,47,48,49,50,51,52,53. No newly rendered or OCR derivatives were required. Reusable assets were left unchanged. Source links are relative to this extraction artifact, three levels below package root.

No supplied Office workbook, formula, cached cell value, CSV, DOC/DOCX, or structured result source falls in this scope. Statistical tables contain printed results, not workbook formulas. No scientific coverage gap remains; individual heat-map cells and forest-plot coordinates have no printed exact values and are recorded as visual quantities rather than invented numeric estimates.

## Relationship index and matching keys

IDs R001-R028 are local evidence groups, not canonical workflow N/S IDs. Every printed table row is preserved in the page transcriptions below; a group covers all constituent rows, subcategories and footnotes.

| Local ID | Source scope | Relationship, definition and matching main-paper key |
|---|---|---|
| R001 | DOC-003 p.3 | Eligibility: age ≥18; Sepsis-3 SOFA ≥2 or increase ≥2; study drug <72 hours from sepsis classification; CAP/HAP/VAP/primary BSI; MALS takes precedence over immunoparalysis; active COVID only MALS, secondary infection after COVID may enter immunoparalysis. Match main eligibility/immune-state assignment. |
| R002 | DOC-003 p.4 | Exclusions: age <18; ANC <1500/mm3; corticosteroids ≥0.4 mg/kg prednisone daily >15 days; anti-cytokine biological last month; other listed exclusion conditions in full transcription. Match main eligibility. |
| R003 | DOC-003 p.5 | Ferritin lower detection 75 ng/ml; HLA-DR absolute antibodies on CD45/CD14-monocytes, shared reagents/protocols across sites. Match immunotest definition. |
| R004 | DOC-003 pp.6-8 eTable1 | All 29 site screened/randomized count pairs; preserve every row and matching recruitment total. |
| R005 | DOC-003 pp.9-10 eTable2 | Administrative approval dates and identifiers; no applicable quantitative result, model or decision rule. |
| R006 | DOC-003 pp.11-12 eTable3 | Three eligibility criteria sets and resolution criteria: BSI sterile blood cultures after 7 days; CAP/HAP/VAP thresholds and resolution components. Match day15 infection outcome definition. |
| R007 | DOC-003 p.13 eTable4 | MALS ferritin >4420 regardless HLA-DR; unclassified ferritin ≤4420 and HLA-DR ≥5000; immunoparalysis ferritin ≤4420 and HLA-DR <5000 antibodies/monocyte. Match main immune strata. |
| R008 | DOC-003 p.14 eTable5 | All baseline blood and respiratory microbiology counts/%; immunotherapy N131, placebo N145; respiratory culture >10^5 cfu/ml. |
| R009 | DOC-003 pp.15-16 eTable6 | All medication/intervention counts/% N131/N145; active antibiotic 34/41(82.9) versus33/38(86.8); N restricted to susceptibility available; low-dose hydrocortisone 200mg/day. |
| R010 | DOC-003 pp.17-19 eTable7 | Every baseline row in four columns: MALS anakinra25/placebo23, immunoparalysis rhIFNγ106/placebo122; counts,%,means(SD),medians(Q1-Q3), units and treatment delay. Match main baseline/immune-state denominators. |
| R011 | DOC-003 p.20 eTable8 | Daily measured/LOCF/death SOFA components days2-9 in N131/N145; death assigned SOFA24, ICU discharged LOCF. Match primary missing-data construction and sensitivity exclusions. |
| R012 | DOC-003 p.21 eTable9 | Five logistic-regression covariates: precision therapy, APACHEII,CCI,SOFA,sites enrolling >8%; univariate/multivariate OR, CI,P; endpoint No204/Yes72. Match adjusted primary OR and adjustment model. |
| R013 | DOC-003 p.22 eTable10 | Four immune-state primary/day15 response rows; numerator/denominator,%,RD95%CI,unadjustedOR95%CI,P; complete visually aligned table below. Match primary state-specific/day15 endpoint. |
| R014 | DOC-003 pp.23-24 eTable11 | Every baseline row comparing SIDF reversal-analysis included125 versus nonincluded151; history resolved COVID; count/%,mean(SD),median(Q1-Q3),units. Match immune reversal subset. |
| R015 | DOC-003 pp.25-26 eTable12 | All SUSAR SOC/PT rows and expectancy; four treatment-state columns plus total276; any5; patients vs events footnote; capture days1-90, Medra27.0. Match safety. |
| R016 | DOC-003 pp.27-29 eTable13 | All serious TEAE SOC/PT rows and relationship categories; four columns plus total276; anySAE245; SOC/patient vs other/event distinction; capture90 days, Medra27.0. Match serious safety incidence and NNH. |
| R017 | DOC-003 pp.30-43 eTable14 | All nonserious TEAE SOC/PT rows, drug relationship and maximum severity categories; four columns plus total276; anyAE256; patient/event distinction; capture90 days, Medra27.0. Match nonserious safety incidence. |
| R018 | DOC-003 p.44 eTable15 | All18 NNT/NNH point estimates and95%CIs across overall,MALS,immunoparalysis; thresholds≥1 through≥5 seriousTEAEs. Match benefit-risk and response/safety source counts. |
| R019 | DOC-003 p.45 eFigure1 | Participant heat-map N145 placebo/N131 therapy; days2-9 minus baseline day1; deltaSOFA scale -10,0,10,20; red endpoint achievers/blue nonachievers. No exact individual-cell values printed. |
| R020 | DOC-003 p.46 eFigure2 | Sensitivity exclude early discharges with LOCF:38/121(31.4%) therapy vs19/132(14.4%) placebo; OR2.72(1.47-5.05),P.001,95%CI bars. Match primary sensitivity and day9 assumed counts. |
| R021 | DOC-003 p.47 eFigure3 | Day28 survival HR0.83(0.59-1.18),P.298; both complete at-risk rows and graph direction below. Match28-day mortality. |
| R022 | DOC-003 p.48 eFigure4 | Day90 survival HR0.84(0.63-1.12),P.231; both complete at-risk rows below. Match90-day mortality. |
| R023 | DOC-003 p.49 eFigure5 | Day15 four infection dispositions; therapy/placebo percentages below; worse-dispositionOR0.59(0.38-0.91),P.018; worse includes superinfection,failure,intermediate. Match main infection disposition result. |
| R024 | DOC-003 p.50 eFigure6 | Reversal HR2.38(1.50-3.77),P<.001,Cox censoredday28,N59/N66; complete at-risk rows, biomarkers and persistence definition below. Match main reversal endpoint/125-subset. |
| R025 | DOC-003 p.51 eFigure7 | Six severity-stratum response count comparisons,P,OR forest visual; six interaction model OR/CI/P rows; APACHE≥25,CCI≥5,SOFA≥10; claimed pre-defined SAP cutoffs for28-day mortality. |
| R026 | DOC-003 p.52 eFigure8 | Six severity-stratum28-day death count comparisons,P,OR forest visual; six interaction OR/CI/P rows; claimed pre-defined SAP28-day mortality cutoffs. |
| R027 | DOC-003 p.53 eFigure9 | Six severity-stratum90-day death count comparisons,P,OR forest visual; six interaction OR/CI/P rows; claimed pre-defined SAP90-day mortality cutoffs. |
| R028 | DOC-003 p.54; DOC-004 pp.1-28; DOC-005 p.1 | References, collaborators, data-sharing administrative units; no applicable statistical result/design relationship. Data access12 months is administrative, not trial follow-up. |

## Figure and aligned inferential transcriptions

### R013: eTable10, PDF p.22

All contrast directions are precision immunotherapy minus/versus placebo. CI columns are95%; OR explicitly unadjusted.

| Endpoint/window/state | Therapy n/N(%) | Placebo n/N(%) | Difference % (CI) | OR(CI) | P |
|---|---|---|---|---|---|
| ≥1.4 decrease mean SOFA days2-9 from day1; MALS |12/25(48.0)|4/23(17.4)|30.6(3.9-51.8)|4.38(1.15-16.64)|.034|
| Same days2-9; immunoparalysis |34/106(32.1)|22/122(18.0)|14.0(2.8-25.1)|2.15(1.16-3.97)|.020|
| ≥1.4 decrease mean SOFA days2-15 from day1; MALS |12/25(48.0)|5/23(21.7)|26.3(0.0-48.4)|3.32(0.94-11.76)|.075|
| Same days2-15; immunoparalysis |40/106(37.7)|29/122(23.8)|13.9(1.9-25.6)|1.194(1.09-3.45)|.030|

The last point estimate is transcribed exactly as visibly printed, 1.194. No normalization is applied.

### R019-R024: eFigures1-6, PDF pp.45-50

- eFigure1: placebo n145, therapy n131; changes on D2,D3,D4,D5,D6,D7,D8,D9 relative to day1; red/blue right strips designate achievers/nonachievers; colors represent deltaSOFA(-10 to20). Treatment startsday1.
- eFigure2: therapy n121 with38(31.4%) endpoint achievers; placebo n132 with19(14.4%); OR2.72,95%CI1.47-5.05,P.001. Y-axis percentage±95%CIs. Patients discharged beforeday9 whose SOFA carried forward excluded.
- eFigure3:28-day survival percentage on x=0,4,8,12,16,20,24,28days; HR0.83,95%CI0.59-1.18,P.298. Placebo at risk145,131,116,104,92,87,78,73; therapy131,120,110,97,88,86,79,74. Therapy curve generally above placebo.
- eFigure4:90-day survival percentage on x=0,15,30,45,60,75,90days; HR0.84,95%CI0.63-1.12,P.231. Placebo at risk145,93,72,62,54,52,47; therapy131,92,71,63,51,46,41. Curves converge/cross later.
- eFigure5:therapy n131 percentages superinfection22.9,failure24.4,intermediate8.4,resolution44.3; placebo n145 percentages31.7,30.3,6.2,31.7 respectively. Printed decimal commas are represented as decimal points here. OR for worse disposition0.59,95%CI0.38-0.91,P.018. Day15 resolved by eTable3; failure means persistence/relapse; superinfection new pathogen; intermediate cannot classify; worse includes all three nonresolution categories.
- eFigure6:CoxHR2.38,95%CI1.50-3.77,printed P=<.001. At-risk displayed columns (left-to-right, near0,4,8,12,16,20,24,28days) placebo66,51,44,44,38,38,37,34; therapy59,18,16,16,14,14,14,13. Biomarkers measured before drug then days2,4,7,15,21,28. Missing draws death/discharge. MALS reversal ≥15% ferritin decrease sustained; immunoparalysis reversal HLA-DR >8000 receptors/monocyte sustained. At least two serial draws required to confirm permanence; otherwise not attaining reversal. Caption states almost half studied according to protocol; HR censoredday28.

### R025-R027: eFigures7-9, PDF pp.51-53

Forest estimates/intervals are plotted rather than numerically labeled in panelA. Exact printed count pairs and P values are below; plot positions must not be substituted for precise printed numeric estimates. Favor direction: eFigure7 OR>1 favors precision therapy; eFigures8/9 OR<1 favors precision therapy. All intervals labeled95%.

| Figure/outcome | Stratum | Placebo events/N | Therapy events/N | PanelA P |
|---|---|---|---|---|
|7 primary response|APACHEII≥25|8/40|12/38|.439|
|7 primary response|APACHEII<25|18/105|34/93|.002|
|7 primary response|CCI≥5|7/76|20/54|.003|
|7 primary response|CCI<5|19/69|26/77|.475|
|7 primary response|SOFA≥10|11/68|25/67|.035|
|7 primary response|SOFA<10|15/77|21/64|.083|
|8 day28 death|APACHEII≥25|27/40|22/38|.489|
|8 day28 death|APACHEII<25|45/105|35/93|.472|
|8 day28 death|CCI≥5|50/76|24/54|.020|
|8 day28 death|CCI<5|22/69|33/77|.231|
|8 day28 death|SOFA≥10|48/68|35/67|.045|
|8 day28 death|SOFA<10|24/77|22/64|.721|
|9 day90 death|APACHEII≥25|32/40|31/38|>.99|
|9 day90 death|APACHEII<25|66/105|59/93|>.99|
|9 day90 death|CCI≥5|64/76|39/54|.123|
|9 day90 death|CCI<5|34/69|51/77|.045|
|9 day90 death|SOFA≥10|57/68|49/67|.209|
|9 day90 death|SOFA<10|41/77|41/64|.231|

Source/OCR disagreement: retained CUDA OCR reads the therapy denominator for APACHEII<25 as6 or omits it in pp51-53. All three source-matched images visibly show93. The image-derived93 is used above. This is a derivative transcription matter, not a candidate diagnosis.

| PanelB figure | Variable | OR |95%CI|P|
|---|---|---|---|---|
|7 primary response|APACHEII≥25|0.47|0.30-1.62|.70|
|7 primary response|APACHEII≥25×therapy|1.85|0.66-5.19|.24|
|7 primary response|CCI≥5|0.22|0.09-0.53|.001|
|7 primary response|CCI≥5×therapy|5.79|2.34-15.05|<.0001|
|7 primary response|SOFA≥10|0.56|0.27-1.19|.13|
|7 primary response|SOFA≥10×therapy|3.08|1.37-6.96|.007|
|8 day28 mortality|APACHEII≥25|0.47|0.30-1.62|.70|
|8 day28 mortality|APACHEII≥25×therapy|1.85|0.66-5.19|.24|
|8 day28 mortality|CCI≥5|0.22|0.09-0.53|.001|
|8 day28 mortality|CCI≥5×therapy|5.79|2.34-15.05|<.0001|
|8 day28 mortality|SOFA≥10|0.56|0.27-1.19|.13|
|8 day28 mortality|SOFA≥10×therapy|3.08|1.37-6.96|.007|
|9 day90 mortality|APACHEII≥25|2.34|1.02-5.34|.044|
|9 day90 mortality|APACHEII≥25×therapy|0.11|0.36-3.42|.86|
|9 day90 mortality|CCI≥5|3.83|1.90-7.69|<.0001|
|9 day90 mortality|CCI≥5×therapy|0.49|0.21-1.15|.10|
|9 day90 mortality|SOFA≥10|3.72|1.80-7.71|<.0001|
|9 day90 mortality|SOFA≥10×therapy|0.53|0.22-1.22|.13|

The panelB rows above preserve every source-printed value. eFigure7 caption: pre-defined SAP cutoffs indicating increased risk for28-day mortality; primary response ≥1.4-point decrease mean days2-9 fromday1; interaction tests for primary endpoint. eFigure8 caption: same28-day mortality cutoff claim; odds of death and interaction tests for28-day mortality. eFigure9 caption: cutoffs indicating increased risk for90-day mortality; odds of death and interaction tests for90-day mortality.

## Exhaustive page-level coverage

| Source | Page | Status | Content mapped |
|---|---:|---|---|
| DOC-003 | 1 | COMPLETE | Index of eMethods,15 tables,9 figures; no numeric result on cover |
| DOC-003 | 2 | COMPLETE | No-applicable: punctuation-only/blank content |
| DOC-003 | 3 | COMPLETE | R001 eligibility |
| DOC-003 | 4 | COMPLETE | R002 exclusions |
| DOC-003 | 5 | COMPLETE | R003 lab definitions |
| DOC-003 | 6 | COMPLETE | R004 eTable1 all site count pairs |
| DOC-003 | 7 | COMPLETE | R004 eTable1 all site count pairs |
| DOC-003 | 8 | COMPLETE | R004 eTable1 all site count pairs |
| DOC-003 | 9 | COMPLETE | R005 no-applicable administrative ethics approval identifiers/dates |
| DOC-003 | 10 | COMPLETE | R005 no-applicable administrative ethics approval identifiers/dates |
| DOC-003 | 11 | COMPLETE | R006 eTable3 infection and resolution criteria |
| DOC-003 | 12 | COMPLETE | R006 eTable3 infection and resolution criteria |
| DOC-003 | 13 | COMPLETE | R007 eTable4 immune-state thresholds |
| DOC-003 | 14 | COMPLETE | R008 eTable5 all microbiology rows |
| DOC-003 | 15 | COMPLETE | R009 eTable6 all medication rows and footnotes |
| DOC-003 | 16 | COMPLETE | R009 eTable6 all medication rows and footnotes |
| DOC-003 | 17 | COMPLETE | R010 eTable7 all baseline rows and footnotes |
| DOC-003 | 18 | COMPLETE | R010 eTable7 all baseline rows and footnotes |
| DOC-003 | 19 | COMPLETE | R010 eTable7 all baseline rows and footnotes |
| DOC-003 | 20 | COMPLETE | R011 eTable8 all day/group SOFA components |
| DOC-003 | 21 | COMPLETE | R012 eTable9 all5 model rows |
| DOC-003 | 22 | COMPLETE | R013 eTable10 all4 outcome rows |
| DOC-003 | 23 | COMPLETE | R014 eTable11 all serial-subset baseline rows |
| DOC-003 | 24 | COMPLETE | R014 eTable11 all serial-subset baseline rows |
| DOC-003 | 25 | COMPLETE | R015 eTable12 all SUSAR rows and footnotes |
| DOC-003 | 26 | COMPLETE | R015 eTable12 all SUSAR rows and footnotes |
| DOC-003 | 27 | COMPLETE | R016 eTable13 all seriousTEAE rows and footnotes |
| DOC-003 | 28 | COMPLETE | R016 eTable13 all seriousTEAE rows and footnotes |
| DOC-003 | 29 | COMPLETE | R016 eTable13 all seriousTEAE rows and footnotes |
| DOC-003 | 30 | COMPLETE | R017 eTable14 all nonseriousTEAE rows and footnotes |
| DOC-003 | 31 | COMPLETE | R017 eTable14 all nonseriousTEAE rows and footnotes |
| DOC-003 | 32 | COMPLETE | R017 eTable14 all nonseriousTEAE rows and footnotes |
| DOC-003 | 33 | COMPLETE | R017 eTable14 all nonseriousTEAE rows and footnotes |
| DOC-003 | 34 | COMPLETE | R017 eTable14 all nonseriousTEAE rows and footnotes |
| DOC-003 | 35 | COMPLETE | R017 eTable14 all nonseriousTEAE rows and footnotes |
| DOC-003 | 36 | COMPLETE | R017 eTable14 all nonseriousTEAE rows and footnotes |
| DOC-003 | 37 | COMPLETE | R017 eTable14 all nonseriousTEAE rows and footnotes |
| DOC-003 | 38 | COMPLETE | R017 eTable14 all nonseriousTEAE rows and footnotes |
| DOC-003 | 39 | COMPLETE | R017 eTable14 all nonseriousTEAE rows and footnotes |
| DOC-003 | 40 | COMPLETE | R017 eTable14 all nonseriousTEAE rows and footnotes |
| DOC-003 | 41 | COMPLETE | R017 eTable14 all nonseriousTEAE rows and footnotes |
| DOC-003 | 42 | COMPLETE | R017 eTable14 all nonseriousTEAE rows and footnotes |
| DOC-003 | 43 | COMPLETE | R017 eTable14 all nonseriousTEAE rows and footnotes |
| DOC-003 | 44 | COMPLETE | R018 eTable15 all18 benefit/risk rows |
| DOC-003 | 45 | COMPLETE | R019 eFigure1 visual heat-map |
| DOC-003 | 46 | COMPLETE | R020 eFigure2 sensitivity |
| DOC-003 | 47 | COMPLETE | R021 eFigure3 day28 survival |
| DOC-003 | 48 | COMPLETE | R022 eFigure4 day90 survival |
| DOC-003 | 49 | COMPLETE | R023 eFigure5 infection disposition |
| DOC-003 | 50 | COMPLETE | R024 eFigure6 reversal |
| DOC-003 | 51 | COMPLETE | R025 eFigure7 primary severity subgroups |
| DOC-003 | 52 | COMPLETE | R026 eFigure8 day28 severity subgroups |
| DOC-003 | 53 | COMPLETE | R027 eFigure9 day90 severity subgroups |
| DOC-003 | 54 | COMPLETE | R028 no-applicable reference bibliography; no extracted external evidence |
| DOC-004 | 1 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 2 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 3 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 4 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 5 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 6 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 7 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 8 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 9 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 10 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 11 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 12 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 13 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 14 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 15 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 16 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 17 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 18 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 19 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 20 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 21 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 22 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 23 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 24 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 25 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 26 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 27 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-004 | 28 | COMPLETE | R028 no-applicable: nonauthor collaborator names, affiliations, roles and administrative page numbering; no result, model or prospective decision rule |
| DOC-005 |1|COMPLETE|R028 no-applicable: deidentified participant data available at publication by sponsor request; DSA;12-month access with possible extension; administrative access terms, no trial result/model/decision rule|

## Complete table/eMethods locator transcriptions

The following retained native/layout transcriptions preserve every printed row, unit, footnote, model label and table continuation for DOC-003 pp.3-44. They are transcription aids; direct PDF authority is retained. Figure content is reconstructed separately above. All DOC-004 pages were opened and mapped as administrative collaborator tables; their names are outside quantitative scope.

### DOC-003 PDF pages2-5: eMethods

```text
                                                  2


.




© 2025 American Medical Association. All rights reserved, including those for text and data mining,
AI training, and similar technologies.
                                                  3


eMethods.
Eligibility Criteria
Inclusion criteria (patients meeting ALL the following criteria were enrolled):
•   Age equal to or above 18 years.
•   Both genders.
•   In case of women, unwillingness to become pregnant during the study period.
•   Written informed consent provided by the patient or by one first-degree
    relative/spouse in case of patients unable to consent.
•   Community-acquired pneumonia (CAP) or hospital-acquired pneumonia (HAP) or
    ventilator-associated pneumonia (VAP) or primary bacteremia (BSI). These are
    defined in eTable 3 using three sets of criteria per infection. Enrolled patients
    should meet criteria as defined in eTable 3.
•   Sepsis defined by the Sepsis-3 definitions. More precisely, sepsis is defined as
    the presence of total SOFA (sequential organ failure assessment) score equal to
    2 or more for patients who are admitted with infection at the emergency
    department OR as any increase of admission SOFA by 2 or more points for
    patients already hospitalized.1
•   Patients with signs of fulminant hyper-inflammation (macrophage activation-like
    syndrome, MALS) or sepsis-induced immunoparalysis as defined in eTable 4.
    Since the state of MALS is considered more life-threatening than the state of
    immunoparalysis, patients with lab findings of both immune states are allocated to
    treatment targeting MALS. Patients with active COVID-19 infection according to
    the attending physicians may participate only in the MALS arm. Patients
    developing secondary infection in the field of COVID-19 according to the
    judgment of the attending physicians were allowed to be enrolled only if they had
    laboratory finding of sepsis-induced immunoparalysis (eTable 4)
•   Time from classification into sepsis by the Sepsis-3 definitions and start of blind
    intervention less than 72 hours.




© 2025 American Medical Association. All rights reserved, including those for text and data mining,
AI training, and similar technologies.
                                                  4


Exclusion criteria (patients meeting ANY of the following criteria COULD NOT be
enrolled in the study):
•   Age below 18 years.
•   Denial for written informed consent.
•   Acute pyelonephritis or intraabdominal infection, meningitis or skin infection.
•   Any stage IV malignancy.
•   Neutropenia defined as an absolute neutrophil count lower than 1,500/mm3.
•   Any “do not resuscitate” decision in the hospital.
•   In the case of BSI, patients with blood cultures growing coagulase-negative
    staphylococci or skin commensals or catheter-related infections could not be
    enrolled.
•   Active tuberculosis (TB) as defined by the co-administration of drugs for the
    treatment of TB.
•   Infection by the human immunodeficiency virus (HIV).
•   Any primary immunodeficiency.
•   Oral or intravenous intake of corticosteroids at a daily dose equal or greater than
    0.4 mg/kg prednisone for more than the last 15 days.
•   Any anti-cytokine biological treatment the last one month.
•   Medical history of systemic lupus erythematosus.
•   Medical history of multiple sclerosis or any other demyelinating disorder.
•   Pregnancy or lactation. Women of child-bearing potential were screened by a
    urine pregnancy test before inclusion in the study.




© 2025 American Medical Association. All rights reserved, including those for text and data mining,
AI training, and similar technologies.
                                                  5


Lab measurements
        Ferritin was measured in serum by an enzyme immunosorbent assay
(ORGENTEC Diagnostika GmbH, Mainz, Germany; lower detection limit 75ng/ml).
Using whole blood collected in EDTA-coated vials, white blood cells were incubated
for 15 minutes in the dark with the following monoclonal antibodies: anti-CD14 FITC,
anti-HLA-DR-PE, anti-CD45 PC5 (Immunotech, Marseille, France) and Quantibrite
HLA-DR/anti-monocyte PerCP-Cy5 (Quantibrite, BD Biosciences, Franklin Lakes,
NJ, USA, CE-marked in vitro diagnostic (IVD) test). After incubation, cells were
analysed by flow cytometer FC500 versus cells stained with anti-CD45 PC5 and anti-
idiotypic IgG1. The number of antibodies bound on the surface antigen HLA-DR on
CD45/CD14-positive monocytes was counted by the Navios EX flow cytometer
(Beckman Coulter, Brea, USA) and considered an expression of the absolute count
of HLA-DR receptors. Measurements of ferritin and HLA-DR of Greek study sites
were done in the study central lab (Research Laboratory of Immunology, 4th
Department of Internal Medicine, ATTIKON University General Hospital, Greece).
Measurements of ferritin and HLA-DR in the other study sites were done following
study lab protocols shared by the study sponsor (Hellenic Institute for the Study of
Sepsis) and by using exactly the same reagents.




© 2025 American Medical Association. All rights reserved, including those for text and data mining,
AI training, and similar technologies.

```

### DOC-003 PDF page6

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=6)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 6]]

                                                         6


       eTable 1. Total Number of Patients Screened and Randomized from each Study
       Site
Study site                                                                   Total Number         Total Number of
                                                                             of Screened          Randomized
                                                                             Patients             Patients
•   4th Department of Internal Medicine ATTIKON University                   64                   23
    Hospital, National and Kapodistrian University of Athens,
    Greece
•   2nd Department of Propaedeutic Internal Medicine ATTIKON                 4                    2
    University Hospital, National and Kapodistrian University of
    Athens, Greece
•   2nd Critical Care Department ATTIKON University Hospital,                19                   13
    National and Kapodistrian University of Athens, Greece
•   1st Department of Pulmonary Medicine and Intensive Care                  1                    0
    Unit Sotiria General Hospital, Athens, Greece
•   Department of Internal Medicine Larissa University Hospital,             5                    1
    Larissa, Greece
•   2nd Intensive Care Unit, KAT Attica General Hospital,                    20                   11
    Kifissia, Greece
•   Department of Critical Care Medicine, University of Ioannina,            4                    1
    Ioannina, Greece
•   Department of Critical Care Medicine, Democritus University              15                   6
    of Thrace, Alexandroupolis, Greece
•   Intensive Care Unit, G. Gennimatas General Hospital,                     21                   4
    Thessaloniki, Greece
•   Intensive Care Unit, Aghios Dimitrios General Hospital,                  22                   6
    Thessaloniki, Greece
•   Department of Anesthesiology and Intensive Care, AHEPA                   93                   28
    Thessaloniki University General Hospital, Thessaloniki,
    Greece
•   Intensive Care Unit, Ippokrateion General Hospital of                    157                  79
    Thessaloniki, Thessaloniki, Greece


       © 2025 American Medical Association. All rights reserved, including those for text and data mining,
       AI training, and similar technologies.


```

### DOC-003 PDF page7

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=7)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 7]]

                                                         7


•   Intensive Care Unit, Theageneion Anticancer Hospital,                    24                   5
    Thessaloniki, Greece
•   Intensive Care Unit, Tzaneio General Hospital, Piraeus,                  1                    1
    Greece
•   Intensive Care Unit, Koutlibaneio & Triantafylleio General               1                    1
    Hospital, Larissa, Greece
•   Intensive Care Unit of Latseion Burn Center, Thriasio General 12                              3
    Hospital, Eleusis, Greece
•   Department of Anesthesiology and Intensive Care, Jena                    11                   9
    University Hospital, Jena, Germany
•   Departments of Intensive Care Medicine and Infectious                    24                   5
    Diseases, Amsterdam Medical University Center, Amsterdam,
    the Netherlands
•   Intensive Care Unit and Department of Internal Medicine and              17                   5
    Infectious Diseases, Radboud University Medical Center,
    Nijmegen, the Netherlands
•   Department of Infectious Diseases, Clinical Hospital for                 4                    2
    Infectious Diseases Cluj-Napoca, Romania
•   Service of Immunology and Allergy, Infectious Diseases and               8                    4
    Adult Intensive Care Unit, Lausanne University Hospital,
    University of Lausanne, Lausanne, Switzerland
•   Polyvalent Intensive Care Unit, Sotiria Athens General                   37                   20
    Hospital of Chest Diseases, Athens, Greece
•   Intensive Care Unit, 424 Military General Hospital,                      2                    2
    Thessaloniki, Greece
•   Intensive Care Unit, Asklipieion General Hospital, Voula,                32                   14
    Greece
•   Intensive Care Unit of Center for Respiratory Failure, Sotiria           28                   17
    Chest Diseases Athens General Hospital, Greece
•   Intensive Care Unit, Korgialeneio-Benakeio Athens General                21                   5
    Hospital, Athens, Greece




       © 2025 American Medical Association. All rights reserved, including those for text and data mining,
       AI training, and similar technologies.


```

### DOC-003 PDF page8

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=8)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 8]]

                                                         8


•   Department of Intensive Care Medicine, University Hospital of 16                              7
    Heraklion, University of Crete, Heraklion, Greece
•   Clinic of Intensive Care and Pulmonary Diseases, Faculty of              7                    5
    Nursing, School of Health Sciences, National and
    Kapodistrian University of Athens, Athens, Greece
•   Dipartimento di Scienze Biotecnologiche di Base, Cliniche                2                    2
    Intensivologiche e Perioperatorie, Università Cattolica del
    Sacro Cuore; Dipartimento di Scienze dell'Emergenza,
    Anestesiologiche e della Rianimazione, Fondazione
    Policlinico Universitario A. Gemelli IRCCS, Rome, Italy




       © 2025 American Medical Association. All rights reserved, including those for text and data mining,
       AI training, and similar technologies.


```

### DOC-003 PDF page9

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=9)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 9]]

                                                  9


eTable 2. List of Approvals from the Ethics Committees, Institution Review
Boards or/and Central Regulatory Bodies for each Participating Country
Participating        Ethics Committee,                    Date of          Number of
Country              Institution Review Board            Approval          Approval
                     or/and Central Regulatory
                     Body
Greece               National Organization for           18/02/2021        IS008/21
                     Medicines of Greece
                     National Ethics Committee           22/01/2021        02/2021
                     of Greece
Germany              German Federal Institute for        25/05/2022        61-3910-4045295
                     Drugs and Medical Devices
                     Ethics Committee of the             02/03/2022        2022-2540-AMG-ff
                     Jena University Hospital
The                  Central Committee on                03/06/2021        NL76706.091.21
Netherlands          Research Involving Human
                     Subjects for the Netherlands
                     Ethics Committee of                 21/10/2021        PW/METC ON 512
                     Radboud universitair
                     medisch centrum
Switzerland          Commission cantonale                01/06/2022        2022-00606
                     d’éthique de la recherche
                     sur l’être humain (CER-VD)
                     Swiss Agency for                    23/05/2022
                     Therapeutic Products,
                     Swissmedic
Romania              National Agency for                 26/09/2022        129E
                     Medicine and Medical
                     Products of Romania
                     Comisia Nationala de                04/07/2022        19S1-4
                     Bioetica a Medicamentului si
                     a Dispozitivelor Medicale


© 2025 American Medical Association. All rights reserved, including those for text and data mining,
AI training, and similar technologies.


```

### DOC-003 PDF page10

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=10)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 10]]

                                                 10


Italy                Italian Medicines Agency –          15/02/2023        0019561-
                     AIFA                                                  15/02/2023-AIFA-
                                                                           AIFA_USC-P
                     Direzione Scientifica               28/03/2023        0010056/23
                     Fondazione Policlinico
                     Gemelli




© 2025 American Medical Association. All rights reserved, including those for text and data mining,
AI training, and similar technologies.


```

### DOC-003 PDF page11

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=11)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 11]]

                                                                              11


        eTable 3. Definitions of Eligible Infections
                       Criterion 1                          Criterion 2                        Criterion 3                          Resolution criteria
 Infection             All the following                    At least 2 of the following At least 1 of the following                 (to be considered
                                                                                                                                    for the secondary
                                                                                                                                    study endpoint)
 Primary               •   At least one positive            None                               None                                 Sterile blood cultures
 bacteremia2               blood culture                                                                                            after seven days
                       •   Failure to identify a
                           primary infection site
                           despite thorough clinical
                           and radiology
                           investigation
 Community-            New infiltrate on chest X-ray        •   New onset or                   •   Procalcitonin ≥0.25 ng/ml •          None of criterion
 acquired                                                       worsening of cough             •   Hypoxemia with partial               2 findings making
 pneumonia3                                                 •   Dyspnea                            oxygen pressure                      the patient
                                                            •   Auscultatory findings              ≤60mmHg or oxygen                    eligible
                                                                compatible with                    saturation ≤90% in                   for the study AND
                                                                pulmonary                          ambient air                      •   None of criterion
                                                                consolidation                  •   Respiratory rate ≥20                 3 findings making
                                                                                                   breaths/min                          the patient




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page12

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=12)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 12]]

                                                                              12


                                                                                                                                        eligible for the
                                                                                                                                        study
 Hospital-             •   Onset >48 hours from             •   New onset or                   •   Procalcitonin ≥0.25 ng/ml •          None of criterion
 acquired                  hospital admission                   worsening of cough or          •   Hypoxemia with partial               2 findings making
 pneumonia4            •   New or evolving infiltrate           dyspnea                            oxygen pressure                      the patient
                           on chest X-ray                   •   Purulent                           ≤60mmHg or oxygen                    eligible
                                                                tracheobronchial                   saturation ≤90% in                   for the study AND
                                                                secretions                         ambient air                      •   None of criterion
                                                            •   Auscultatory findings          •   Respiratory rate ≥20                 3 findings making
                                                                compatible with                    breaths/min                          the patient
                                                                pulmonary                                                               eligible for the
                                                                consolidation                                                           study
 Ventilator-           •   Onset >48 hours from             •   Purulent                       •   Procalcitonin ≥0.25 ng/ml •          None of criterion
 associated                start of mechanical                  tracheobronchial               •   Clinical pulmonary                   2 findings making
 pneumonia4,5              ventilation                          secretions                         infection score (CPIS) ≥6            the patient
                       •   New or evolving infiltrate       •   Auscultatory findings                                                   eligible
                           on chest X-ray                       compatible with                                                         for the study AND
                                                                pulmonary                                                           •   None of criterion
                                                                consolidation                                                           3 findings making
                                                                                                                                        the patient eligible
                                                                                                                                        for the study
        Footnote: Any patient can be classified as suffering from one of the following infections if he/she meets listed criteria 1 to 3.

© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page13

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=13)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 13]]

                                                     13


    eTable 4. Combinations of Immunotests Guiding Randomization
                              Macrophage activation-              Unclassified          Sepsis-induced
                              like syndrome                                             immunoparalysis
Ferritin (ng/ml)              >4,420        >4,420                ≤4,420                ≤4,420


HLA-DR (antibodies per        ≥5,000        <5,000                ≥5,000                <5,000
CD45/CD14-monocyte)
    Abbreviations: HLA-DR, Histocompatibility Complex DR.




    © 2025 American Medical Association. All rights reserved, including those for text and data mining,
    AI training, and similar technologies.


```

### DOC-003 PDF page14

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=14)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 14]]

                                                         14


        eTable 5. Baseline Microbiology of Study Participants
                                                              Standard care + Precision             Standard care +
                                                              Immunotherapy (n=131)                 Placebo (n=145)
Baseline microbiology: blood cultures, No. (%)


Gram-negative bacteria                                        19 (14.5)                             16 (11.0)
   Acinetobacter baumannii                                    5 (3.8)                               9 (6.2)
   Klebsiella pneumoniae                                      6 (4.6)                               5 (3.4)
   Others                                                     8 (6.1)                               2 (1.4)

Gram-positive bacteria                                        12 (9.2)                              11 (7.6)
   Enterococcus faecium                                       2 (1.5)                               2 (1.4)
   Streptococcus pneumoniae                                   0 (0.0)                               2 (1.4)
   Staphylococcus aureus                                      3 (2.3)                               0 (0.0)
   Coagulase-negative Staphylococcus spp                      5 (3.8)                               4 (2.8)
   Others                                                     2 (1.5)                               3 (2.1)
Candida spp                                                   1 (0.8)                               3 (2.1)
Baseline microbiology: respiratory cultures*, No. (%)
Gram-negative bacteria                                        47 (35.9)                             48 (33.1)
   Acinetobacter baumannii                                    14 (10.7)                             22 (15.2)
   Klebsiella pneumoniae                                      7 (5.3)                               7 (4.8)
   Pseudomonas aeruginosa                                     15 (11.5)                             12 (8.3)
   Others                                                     11 (8.4)                              7 (4.8)
Gram-positive bacteria                                        3 (2.3)                               4 (2.8)
Candida spp                                                   4 (3.1)                               8 (5.5)
        *isolated at >105 cfu/ml of tracheobronchial secretions
        Abbreviations: n, number of patients.




        © 2025 American Medical Association. All rights reserved, including those for text and data mining,
        AI training, and similar technologies.


```

### DOC-003 PDF page15

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=15)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 15]]

                                                       15


      eTable 6. Co-Administered Medication and Interventions
                                                            Standard care + Precision Standard care +
                                                            Immunotherapy (n=131)              Placebo (n=145)
Antibiotics, No. (%)
   Ampicillin/sulbactam                                     16 (12.2)                          27 (18.6)
   Piperacillin/tazobactam                                  27 (20.6)                          25 (17.2)
   3rd generation cephalosporins                            12 (9.2)                           14 (9.7)
   Ceftaroline                                              6 (4.6)                            4 (2.8)
   Ceftazidime/avibactam                                    31 (23.7)                          34 (23.4)
   Ceftolozane/tazobactam                                   0 (0.0)                            4 (2.8)
   Ertapenem                                                3 (2.3)                            3 (2.1)
   Meropenem                                                47 (35.9)                          43 (29.7)
   Meropenem/varobactam                                     2 (1.5)                            3 (2.1)
   Tigecycline                                              27 (20.6)                          25 (17.2)
   Levofloxacin/Moxifloxacin                                11 (8.4)                           16 (11.0)
   Colistin                                                 74 (56.5)                          84 (57.9)
   Gentamycin                                               10 (7.6)                           7 (4.8)
   Amikacin                                                 9 (6.9)                            12 (8.3)
   Fosfomycin                                               3 (2.3)                            9 (6.2)
   Linezolid                                                39 (29.8)                          42 (29.0)
   Glycopeptide (Vancomycin or Teicoplanin)                 32 (24.4)                          29 (20.0)
   Daptomycin                                               37 (28.2)                          40 (27.6)
   Echinocandins                                            18 (13.7)                          26 (17.9)
Treatment with at least one active antibiotic               34/41 (82.9)                       33/38 (86.8)
against the isolated pathogen, n/N (%)a
Other drugs/interventions, No. (%)
   Norepinephrine                                           110 (84.0)                         126 (86.9)
   Vasopressin                                              31 (23.7)                          34 (23.4)
   Mechanical ventilation                                   116 (88.5)                         129 (89.0)
   CVVH                                                     23 (17.6)                          24 (16.6)
   LMWH                                                     102 (77.9)                         108 (74.5)
   Low-dose hydrocortisoneb                                 56 (42.7)                          72 (49.7)


      © 2025 American Medical Association. All rights reserved, including those for text and data mining,
      AI training, and similar technologies.


```

### DOC-003 PDF page16

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=16)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 16]]

                                                   16


Dexamethasone                                           7 (5.3)                            9 (6.2)
Methylprednisolone                                      21 (16.0)                          20 (13.8)
Fast-acting insulin                                     44 (33.6)                          50 (34.5)
Esmolol                                                 16 (12.2)                          24 (16.6)
Landiolol                                               9 (6.9)                            8 (5.5)
Furosemide                                              82 (62.6)                          95 (65.5)
Ipratropium                                             27 (20.6)                          29 (20.0)
Ipratropium/salbutamol                                  43 (32.8)                          41 (28.3)
Salbutamol                                              5 (3.8)                            10 (6.9)
  Abbreviations: CVVH, continuous veno-venal hemofiltration; LMWH, low molecular
  weight heparin; Q, quartile; SD, standard deviation.
  a
      n refers to the number of patients treated with at least one active antibiotic against
  the isolated pathogen and N refers to the number of patients for whom antimicrobial
  susceptibility test was available.
  b
      Low-dose hydrocortisone indicates hydrocortisone at a dose of 200mg per day
  according to Surviving Sepsis Campaign Guidelines.6




  © 2025 American Medical Association. All rights reserved, including those for text and data mining,
  AI training, and similar technologies.


```

### DOC-003 PDF page17

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=17)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 17]]

             eTable 7. Baseline Characteristics of Study Participants by State of Sepsis-Induced Immune Dysregulation
                                                   Macrophage activation-like syndrome             Sepsis-induced immunoparalysis


                                                   Standard care +         Standard care +         Standard care +      Standard care +
                                                   Anakinra (n=25)         Placebo (n=23)          rhIFNγ (n=106)       Placebo (n=122)
Μale, No. (%)                                      17 (68.0)               13 (56.5)               72 (67.9)            81 (66.4)
Female, No. (%)                                    8 (32.0)                10 (43.5)               34 (32.1)            41(33.6)
Age, mean (SD), years                              66 (13)                 66 (14)                 70 (13)              70 (13)
Race, No. (%)
   African                                         0 (0.0)                 0 (0.0)                 1 (0.9)              0 (0.0)
   Caucasian                                       25 (100.0)              23 (100.0)              104 (98.1)           122 (100.0)
   Middle Eastern                                  0 (0.0)                 0 (0.0)                 1 (0.9)              0 (0.0)
Underlying Infection, No. (%)
   Ventilator-associated pneumonia                 9 (36.0)                4 (17.4)                39 (36.8)            50 (41.0)
   Hospital-acquired pneumonia                     7 (28.0)                5 (21.7)                28 (26.4)            27 (22.1)
   Community-acquired pneumonia                    5 (20.0)                8 (34.8)                26 (24.5)            36 (29.5)
   Primary bacteremia                              3 (12.0)                3 (13.0)                13 (12.3)            9 (7.4)
   Active SARS-CoV-2 pneumonia                     1 (4.0)                 3 (13.0)                0 (0.0)              0 (0.0)
APACHE II, median (Q1-Q3)                          21 (17-26)              20 (16-26)              19 (15-25)           19 (14-25)
CCI, median (Q1-Q3)                                3 (2-5)                 4 (2-6)                 4 (3-6)              5 (3-6)
SOFA, median (Q1-Q3)                               10 (8-14)               10 (6-13.5)             9 (7-11)             9 (6-10)


```

### DOC-003 PDF page18

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=18)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 18]]

                                                                                           18


Baseline laboratory values

   Ferritin, median (Q1-Q3), ng/ml                              5438 (5000-7009)                6221 (5000-7500)               633 (353-1149)             703 (340-1488)
   mHLA-DR, median (Q1-Q3), antibodies per CD-                  3576 (2124-6205)                4990 (3068-7811)               3043 (2297-4135)           3078 (1762-4004)
   14 cell
   Total white blood cell count, mean (SD), /mm3                16,834.0 (6,775.9)              18,597.4 (11,271.1)            17,044.2 (9,568.1)         16,585.4 (9,248.2)
   Hemoglobin, mean (SD), g/dl                                  9.4 (1.8)                       10.1 (1.9)                     10.6 (7.6)                 9.8 (1.8)
   Platelets, mean (SD), /mm3                                   233,480 (226,605)               142,683 (114,729)              193,729 (121,231)          227,385 (135,123)
   International normalized ratio, median (Q1-Q3)               1.4 (1.1-1.5)                   1.3 (1.1-1.5)                  1.2 (1.1-1.3)              1.1 (1.0-1.3)
   Fibrinogen, mean (SD), mg/dl                                 500.9 (258.9)                   738.5 (950.7)                  604.5 (220.3)              604.8 (922.2)
   D-dimers, median (Q1-Q3), mg/dl                              3.1 (0.6-8.9)                   1.1 (0.6-3.4)                  1.1 (0.5-2.9)              2.1 (0.5-5.9)
   Creatinine, median (Q1-Q3), mg/dl                            1.3 (0.8-2.5)                   1.6 (0.9-2.8)                  1.3 (0.8-1.9)              0.9 (0.7-1.5)
     Creatinine 1.2-1.9 mg/dl, No. (%)                          5 (20.0)                        5 (21.7)                       31 (29.2)                  25 (20.5)
     Creatinine 2.0-3.4 mg/dl, No. (%)                          8 (32.0)                        9 (39.1)                       16 (15.1)                  16 (13.1)
     Creatinine 3.5-4.9 mg/dl, No. (%)                          0 (0.0)                         0 (0.0)                        3 (2.8)                    5 (4.1)
     Creatinine ≥ 5.0 mg/dl, No. (%)                            1 (4.0)                         1 (4.3)                        6 (5.7)                    0 (0.0)
   Total Bilirubin, median (Q1-Q3), mg/dl                       0.9 (0.6-1.5)                   0.5 (0.3-0.9)                  0.6 (0.4-1.2)              0.6 (0.4-1.1)
     Total bilirubin 1.2-1.9 mg/dl, No. (%)                     4 (16.0)                        2 (8.7)                        12 (11.3)                  14 (11.5)
     Total bilirubin 2.0-5.9 mg/dl, No. (%)                     4 (16.0)                        2 (8.7)                        10 (9.4)                   11 (9.0)
     Total bilirubin 6.0-11.9 mg/dl, No. (%)                    1 (4.0)                         0 (0.0)                        1 (0.9)                    0 (0.0)
     Total bilirubin ≥ 12.0 mg/dl, No. (%)                      0 (0.0)                         0 (0.0)                        0 (0.0)                    1 (0.8)



             © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page19

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=19)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 19]]

                                                                                      19


Aspartate aminotransferase, median (Q1-Q3), U/l 184 (36-553)                               71 (52-266)                    39 (24-64)                 37 (20-86)
Alanine aminotransaminase, median (Q1-Q3),                 187 (36-468)                    46 (33-284)                    32 (17-55)                 33 (17-70)
U/l
pO2/FiO2, median (Q1-Q3)                                   143.1 (105.3-296.6)             159.7 (113.8-254.3)            167.5 (133.2-239.6)        172.0 (128.0-231.3)
Lactate, median (Q1-Q3), mmol/l                            2.1 (1.3-5.9)                   1.8 (1.2-3.6)                  1.6 (1.1-2.3)              1.7 (1.0-3.0)
C-reactive protein, median (Q1-Q3), mg/l                   18.0 (10.7-147.0)               41 (9.3-117.0)                 31.3 (14.3-190.0)          32.0 (14.8-146.0)
Procalcitonin, median (Q1-Q3), ng/ml                       3.4 (1.3-17.5)                  1.8 (0.5-53.6)                 1.1 (0.4-4.8)              1.1 (0.4-10.2)
Time between sepsis onset and start of the study 34 (24-48)                                48 (24-53)                     38 (24-48)                 46.5 (24-48)
drug, median (Q1-Q3), hours
                Abbreviations: APACHE, acute physiology and chronic health evaluation; CCI, Chalron’s comorbidity index; mHLA-DR,
                monocytic histocompatibility complex DR; rhIFNγ, recombinant human activated interferon-gamma; Q, quartile; SARS-CoV-2,
                severe acute respiratory syndrome coronavirus-2; SD, standard deviation; SOFA, sequential organ failure assessment.




        © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page20

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=20)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 20]]

                                                                                  20


    eTable 8. Cumulative Distribution of SOFA scores between Days 2 and 9
    Each cell indicates on the respective day how many SOFA scores were actually measured; how many SOFA scores were given as
    24 because of patients dying; and how many SOFA scores were assumed as last observations carried forward for patients
    discharged earlier from the ICU
Day 2              Day 3                 Day 4                  Day 5                  Day 6                 Day 7                  Day 8           Day 9
                                                          Standard care + Precision Immunotherapy
Measured= 130      Measured= 125         Measured= 119          Measured= 115          Measured= 114         Measured= 107          Measured= 102   Measured= 100
Assumed= 0         Assumed= 1            Assumed= 4             Assumed= 5             Assumed= 5            Assumed= 7             Assumed= 9      Assumed= 10
Death= 1           Death= 5              Death= 8               Death= 11              Death= 12             Death= 17              Death= 20       Death= 21
                                                                      Standard care + Placebo
Measured= 144      Measured= 135         Measured= 133          Measured= 127          Measured= 119         Measured= 117          Measured= 111   Measured= 103
Assumed= 0         Assumed= 2            Assumed= 2             Assumed= 4             Assumed= 7            Assumed= 8             Assumed= 10     Assumed= 13
Death= 1           Death= 8              Death= 10              Death= 14              Death= 19             Death= 20              Death= 24       Death= 29


    Abbreviations: ICU, intensive care unit; SOFA, sequential organ failure assessment




    © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page21

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=21)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 21]]

                                                                              21


eTable 9. Logistic Regression of Variables Impacting on the Primary Endpoint
                                      Meeting the endpoint           Univariate analysis                  Multivariate analysis

                                      No             Yes             OR                    P value        OR                     P value


       Precision immuno-              85/204         46/72           2.48                  .001           2.49                   .001
       therapy, n/Ν (%)               (41.7)         (63.9)          (1.42 to 4.31)                       (1.42 to 4.36)
       APACHE II, median              19             20              1.01                  .650           1.00                   .826
       (Q1-Q3)                        (14-25)        (16-25)         (0.97 to 1.05)                       (0.96 to 1.05)
       CCI, median (Q1-Q3)            5 (3-6)        4 (3-6)         0.94                  .338           0.95                   .375
                                                                     (0.84 to 1.06)                       (0.84 to 1.07)
       SOFA, median (Q1-              9 (7-11)       9.5 (7-12.8) 1.03                     .433           1.02                   .562
       Q3)                                                           (0.96 to 1.10)                       (0.95 to 1.09)
       Sites enrolling more           100            32 (44.4)       0.83                  .504           0.80                   .453
       than 8%, No. (%)               (49.0)                         (0.48 to 1.42)                       (0.46 to 1.41)
Abbreviations CCI, Charlson’s comorbidity index; CI, confidence interval; n, number of patients; N, number of patients studied; OR
odds ratio; Q, quartile, SOFA, sequential organ failure assessment.




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page22

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=22)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 22]]

                                                                                      22


        eTable 10. Change of the mean SOFA score by Days 9 and 15 by the Level of Sepsis-Induced Immune Dysregulation
Endpoints                                                  Standard care + Precision Standard care + Placebo                      Difference,        ORunadjusted      P value
                                                           Immunotherapy                                                          % (95%CIs)         (95% CI)
≥1.4-point decrease of mean SOFA of days 2 to 9
from baseline day 1 per state of immune
activation, n/N (%)
   Macrophage activation-like syndromea                    12/25 (48.0)                        4/23 (17.4)                        30.6               4.38              .034
                                                                                                                                  (3.9 to 51.8)      (1.15 to 16.64)
   Sepsis-induced immunoparalysisb                         34/106 (32.1)                       22/122 (18.0)                      14.0               2.15              .020
                                                                                                                                  (2.8 to 25.1)      (1.16 to 3.97)
≥1.4-point decrease of mean SOFA of days 2 to
15 from baseline day 1, n/N (%)
   Macrophage activation-like syndromea (%)                12/25 (48.0)                        5/23 (21.7)                        26.3               3.32              .075
                                                                                                                                  (0.0 to 48.4)      (0.94 to 11.76)
   Sepsis-induced immunoparalysisb (%)                     40/106 (37.7)                       29/122 (23.8)                      13.9               1.194             .030
                                                                                                                                  (1.9 to 25.6)      (1.09 to 3.45)
        Abbreviations CI, Confidence Interval; OR, Odds Ratio; n, number of patients; N, number of studied patients; NA, not applicable;
        SOFA, Sequential Organ Failure Assessment.
        a
            defined as blood ferritin >4,420 ng/ml.
        b
            defined as ferritin ≤ 4,420 ng/ml and HLA-DR < 5,000 molecules on CD45/CD14-monocytes.




        © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page23

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=23)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 23]]

                                                           23


          eTable 11. Comparison of Baseline Characteristics Between Patients With and
          Without Serial Measurements for the Secondary Endpoint of SIDF Reversal
                                                                Reversal of SIDF               No Reversal of SIDF
                                                                analysis (n=125)               analysis (n=151)
Male, No. (%)                                                   84 (67.2)                      99 (65.6)
Female, No. (%)                                                 41 (32.8)                      52 (34.4)
Age, mean (SD), years                                           72 (12)                        68 (14)
Most common comorbidities, No. (%)
   Diabetes mellitus                                            47 (37.6)                      46 (30.5)
   COVID-19a                                                    41 (32.8)                      28 (18.5)
   Coronary heart disease                                       33 (26.4)                      26 (17.2)
   Atrial fibrillation                                          27 (21.6)                      32 (21.2)
   Chronic obstructive pulmonary disease                        25 (20.0)                      40 (26.5)
   Heart failure                                                18 (14.4)                      23 (15.2)
   Cerebral stroke                                              18 (14.4)                      18 (11.9)
   Chronic renal disease                                        12 (9.6)                       17 (11.3)
   Solid tumor malignancy without metastasis                    9 (7.2)                        12 (7.9)
   Cerebral hemorrhage                                          7 (5.6)                        11 (7.3)
Underlying Infection, No. (%)
   Ventilator-associated pneumonia                              47 (37.6)                      54 (35.8)
   Hospital-acquired pneumonia                                  19 (15.2)                      47 (31.1)
   Community-acquired pneumonia                                 34 (27.2)                      41 (27.2)
   Primary bacteremia                                           19 (15.2)                      9 (6.0)
   Pneumonia by SARS-CoV-2                                      6 (4.8)                        0 (0.0)
APACHE II, median (Q1-Q3)                                       19 (14-26)                     20 (16-25)
CCI, median (Q1-Q3)                                             4 (3-6)                        4 (3-5)
SOFA score, median (Q1-Q3)                                      9 (6-11)                       10 (7-12)
Baseline laboratory values
   Ferritin at screening, median (Q1-Q3), ng/ml
   MALS                                                         6170 (5425-7500)               5000 (4812-7598)
   Immunoparalysis                                              678 (362-1140)                 671 (337-1566)




          © 2025 American Medical Association. All rights reserved, including those for text and data mining,
          AI training, and similar technologies.


```

### DOC-003 PDF page24

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=24)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 24]]

                                                          24


   mHLA-DR at screening, median (Q1-Q3),
   antibodies per CD-14 cell
   MALS                                                        4425 (2130-6205)               4990 (2900-7811)
   Immunoparalysis                                             3056 (1989-3962)               3075 (1932-4227)
   Total white blood cell count, mean (SD), /mm3               17,551.1 (10,352.4)            16,459.1 (8,399.7)
   Hemoglobin, mean (SD), g/dl                                 9.96 (1.93)                    10.21 (6.41)
   Platelets, mean (SD), /mm3                                  212,877 (128,703)              199,775 (152,901)
   International normalized ratio, median (Q1-Q3)              1.2 (1.1-1.3)                  1.2 (1.1-1.4)
   Fibrinogen, mean (SD), mg/dl                                584.4 (242.4)                  625.8 (900.4)
   D-dimers, median (Q1-Q3), mg/dl                             717.0 (0.8-3432.7)             3.1 (0.7-1095.2)
   Creatinine, median (Q1-Q3), mg/dl                           1.0 (0.7-1.8)                  1.2 (0.7-2.0)
   Aspartate aminotransferase, median (Q1-Q3), U/l             37 (23-63)                     53 (25-116)
   Alanine aminotransaminase, median (Q1-Q3), U/l              33 (17-65)                     40 (19-89)
   Total bilirubin, median (Q1-Q3), mg/dl                      0.6 (0.4-1.1)                  0.6 (0.4-1.2)
   pO2/FiO2, median (Q1-Q3)                                    164.2 (128.8-246.0)            173.1 (124.5-235.9)
   Lactate, median (Q1-Q3), mmol/l                             1.7 (1.10-2.60)                1.7 (1.10-3.10)
   C-reactive protein, median (Q1-Q3), mg/l                    35.0 (14.3-201.1)              30.1 (14.3-116.5)
   Procalcitonin, median (Q1-Q3), ng/ml                        1.3 (0.5-3.4)                  1.3 (0.5-13.8)
Time between sepsis onset and start of the study               30.0 (24.0-48.0)               48.0 (24.0-50.0)
drug, median (Q1-Q3), hours
         Abbreviations: APACHE, Acute Physiology and Chronic Health Evaluation; CCI,
         Charlson’s comorbidity index; mHLA-DR, monocytic histocompability complex DR;
         MALS, macrophage activation-like syndrome; Q, quartile; SARS-CoV-2, severe acute
         respiratory syndrome coronavirus-2; SD, standard deviation; SIDF, sepsis-induced
         immune dysfunction; SOFA, sequential organ failure assessment.
         a
             Refers to history of resolved COVID-19 infection.




         © 2025 American Medical Association. All rights reserved, including those for text and data mining,
         AI training, and similar technologies.


```

### DOC-003 PDF page25

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=25)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 25]]

     eTable 12. Suspected Unexpected Serious Adverse Reactions (SUSARs) by System-Organ Class and Preferred Term
     Classified by Expectancy (Safety Set)
                                        Macrophage Activation-like           Sepsis-Induced Immunoparalysis
                                        Syndrome (N= 48)                     (N= 228)
                                        Standard care +    Standard care +   Standard care + Standard care +    Total (N=276)
                                        Anakinra (N=25)    Placebo (N=23)    rhIFNγ (N=106)   Placebo (N=122)
Any SUSAR, n (%)a                       0 (0.0)            0 (0.0)           2 (1.9)          3 (2.5)           5 (1.8)
   Unexpected                           0 (0.0)            0 (0.0)           2 (1.9)          3 (2.5)           5 (1.8)
Cardiac disorders, n (%)a               0 (0.0)            0 (0.0)           0 (0.0)          1 (0.8)           1 (0.4)
 Cardiac arrest, n (%)                  0 (0.0)            0 (0.0)           0 (0.0)          1 (0.8)           1 (0.4)
   Unexpected                           0 (0.0)            0 (0.0)           0 (0.0)          1 (0.8)           1 (0.4)
General disorders and administration    0 (0.0)            0 (0.0)           1 (0.9)          0 (0.0)           1 (0.4)
site conditions, n (%)a
 Multiple organ dysfunction             0 (0.0)            0 (0.0)           1 (0.9)          0 (0.0)           1 (0.4)
 syndrome, n (%)b
   Unexpected                           0 (0.0)            0 (0.0)           1 (0.9)          0 (0.0)           1 (0.4)
Hepatobiliary disorders, n (%)a         0 (0.0)            0 (0.0)           1 (0.9)          0 (0.0)           1 (0.4)
 Liver injury, n (%)                    0 (0.0)            0 (0.0)           1 (0.9)          0 (0.0)           1 (0.4)
   Unexpected                           0 (0.0)            0 (0.0)           1 (0.9)          0 (0.0)           1 (0.4)
Infections and infestations, n (%)a     0 (0.0)            0 (0.0)           0 (0.0)          1 (0.8)           1 (0.4)
 Septic shock, n (%)c                   0 (0.0)            0 (0.0)           0 (0.0)          1 (0.8)           1 (0.4)


```

### DOC-003 PDF page26

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=26)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 26]]

                                                                              26


     Unexpected                                       0 (0.0)                      0 (0.0)               0 (0.0)                1 (0.8)      1 (0.4)
 Respiratory, thoracic and mediastinal                0 (0.0)                      0 (0.0)               0 (0.0)                1 (0.8)      1 (0.4)
 disorders, n (%)a
   Mediastinal haemorrhage, n (%)                     0 (0.0)                      0 (0.0)               0 (0.0)                1 (0.8)      1 (0.4)
     Unexpected                                       0 (0.0)                      0 (0.0)               0 (0.0)                1 (0.8)      1 (0.4)
 Vascular disorders, n (%)a                           0 (0.0)                      0 (0.0)               0 (0.0)                1 (0.8)      1 (0.4)
   Hypotension, n (%)                                 0 (0.0)                      0 (0.0)               0 (0.0)                1 (0.8)      1 (0.4)
     Unexpected                                       0 (0.0)                      0 (0.0)               0 (0.0)                1 (0.8)      1 (0.4)
        Abbreviations: PT, preferred term; rhIFNγ, recombinant human activated interferon-gamma; SOC, system organ class;
        SUSAR, suspected unexpected serious adverse reaction.
        Footnote: The SUSARs were classified by expectancy using Medra 27.0 for events captured between days 1 and 90 of
        follow-up for the 276 patients. It is clarified that the total of each SOC refers to the number of patients and not to the
        cumulative number of events.
        a
            These data represent the number of patients, whereas all other data in the table correspond to the number of events.
        b
            Represents the progression to Multiple organ dysfunction syndrome (MODS) of the initial sepsis or septic shock for which
        the patient was enrolled in the study.
        c
            Represents a new episode of sepsis or septic shock after the resolution of the initial sepsis or septic shock for which the
        patient was enrolled in the study.




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page27

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=27)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 27]]

                                                                              27


        eTable 13. Serious TEAEs (>2% Incidence) by System-Organ Class and Preferred Term; Total Events Classified by
        Relationship to Study Drug (Safety set)
                                                   Macrophage Activation-like                      Sepsis-Induced Immunoparalysis
                                                   Syndrome (N= 48)                                (N= 228)
                                                   Standard care +         Standard care +         Standard care +        Standard care +    Total
                                                   Anakinra (N=25)         Placebo (N=23)          rhIFNγ (N=106)         Placebo (N=122)    (N=276)
 Any SAE, n (%)a                                   20 (80.0)               21 (91.3)               96 (90.6)              108 (88.5)         245 (88.8)
     Probably related                              1 (4.0)                 0 (0.0)                 1 (0.9)                1 (0.8)            3 (1.1)
     Possibly related                              1 (4.0)                 0 (0.0)                 5 (4.7)                2 (1.6)            8 (2.9)
     Probably not related                          4 (16.0)                9 (39.1)                28 (26.4)              26 (21.3)          67 (24.3)
     Unrelated                                     14 (56.0)               12 (52.2)               62 (58.5)              79 (64.8)          167 (60.5)
 Blood and lymphatic system                        13 (52.0)               4 (17.4)                40 (37.7)              38 (31.1)          95 (34.4)
 disorders, n (%)a
   Anaemia, n (%)                                  12 (48.0)               4 (17.4)                35 (33.0)              34 (27.9)          85 (30.8)
   Thrombocytopenia, n (%)                         2 (8.0)                 2 (8.7)                 12 (11.3)              7 (5.7)            23 (8.3)
 Cardiac disorders, n (%)a                         3 (12.0)                6 (26.1)                31 (29.2)              29 (23.8)          69 (25.0)
   Atrial fibrillation, n (%)                      2 (8.0)                 4 (17.4)                17 (16.0)              10 (8.2)           33 (12.0)
   Bradycardia, n (%)                              1 (4.0)                 2 (8.7)                 5 (4.7)                4 (3.3)            12 (4.3)
   Cardiac arrest, n (%)                           1 (4.0)                 3 (13.0)                8 (7.5)                13 (10.7)          25 (9.1)
 General disorders and                             10 (40.0)               11 (47.8)               46 (43.4)              51 (41.8)          118 (42.8)
 administration site conditions, n (%)a



© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page28

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=28)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 28]]

                                                                              28


   Multiple organ dysfunction                      9 (36.0)                10 (43.5)               44 (41.5)              48 (39.3)          111 (40.2)
   syndrome, n (%)b
 Infections and infestations, n (%)a               11 (44.0)               9 (39.1)                59 (55.7)              56 (45.9)          135 (48.9)
   Bacteraemia, n (%)                              6 (24.0)                6 (26.1)                30 (28.3)              21 (17.2)          63 (22.8)
   Device related infection, n (%)                 0 (0.0)                 2 (8.7)                 2 (1.9)                2 (1.6)            6 (2.2)
   Fungaemia, n (%)                                2 (8.0)                 2 (8.7)                 15 (14.2)              10 (8.2)           29 (10.5)
   Fungal infection, n (%)                         1 (4.0)                 0 (0.0)                 6 (5.7)                5 (4.1)            12 (4.3)
   Pneumonia, n (%)                                5 (20.0)                6 (26.1)                30 (28.3)              26 (21.3)          67 (24.3)
   Sepsis, n (%)c                                  3 (12.0)                2 (8.7)                 6 (5.7)                10 (8.2)           21 (7.6)
   Septic shock, n (%)c                            7 (28.0)                3 (13.0)                22 (20.8)              14 (11.5)          46 (16.7)
   Urinary tract infection, n (%)                  1 (4.0)                 0 (0.0)                 3 (2.8)                7 (5.7)            11 (4.0)
 Renal and urinary disorders, n (%)a               4 (16.0)                4 (17.4)                19 (17.9)              16 (13.1)          43 (15.6)
   Acute kidney injury, n (%)                      3 (12.0)                3 (13.0)                18 (17.0)              16 (13.1)          40 (14.5)
 Respiratory, thoracic and                         4 (16.0)                4 (17.4)                27 (25.5)              24 (19.7)          59 (21.4)
 mediastinal disorders, n (%)a
   Bronchial obstruction, n (%)                    1 (4.0)                 1 (4.3)                 2 (1.9)                2 (1.6)            6 (2.2)
   Hypoxia, n (%)                                  1 (4.0)                 1 (4.3)                 3 (2.8)                6 (4.9)            11 (4.0)
   Pleural effusion, n (%)                         0 (0.0)                 2 (8.7)                 5 (4.7)                1 (0.8)            8 (2.9)
   Pneumothorax, n (%)                             3 (12.0)                0 (0.0)                 7 (6.6)                7 (5.7)            17 (6.2)
   Respiratory failure, n (%)                      0 (0.0)                 0 (0.0)                 2 (1.9)                7 (5.7)            9 (3.3)
   Tracheal stenosis, n (%)                        1 (4.0)                 1 (4.3)                 6 (5.7)                7 (5.7)            15 (5.4)



© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page29

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=29)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 29]]

                                                                              29


 Vascular disorders, n (%)a                        2 (8.0)                 3 (13.0)                8 (7.5)                7 (5.7)            20 (7.2)
   Haemorrhage, n (%)                              1 (4.0)                 0 (0.0)                 5 (4.7)                0 (0.0)            6 (2.2)
        Abbreviations: MALS, macrophage activation-like syndrome; PT, preferred term; rhIFNγ, recombinant human activated
        interferon-gamma; SOC, system organ class; TEAE, treatment-emergent adverse event.
        Footnote: The serious TEAEs (sTEAEs) were classified by relationship to the study drug using Medra 27.0 for events
        captured during the 90 days of follow-up for the enrolled 276 patients. In the analysis, sTEAEs are graded as probably
        related, possibly related, probably not related, and unrelated. It is clarified that the total of each SOC refers to the number of
        patients and not to the cumulative number of events.
        a
            These data represent the number of patients, whereas all other data in the table correspond to the number of events.
        b
            Represents the progression to Multiple organ dysfunction syndrome (MODS) of the initial sepsis or septic shock for which
        the patient was enrolled in the study.
        c
            Represents a new episode of sepsis or septic shock after the resolution of the initial sepsis or septic shock for which the
        patient was enrolled in the study.




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page30

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=30)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 30]]

                                                                                  30


            eTable 14. Non-Serious TEAEs (>2% Incidence) by System-Organ Class and Preferred Term Classified by Maximum
            Severity; Total Events Classified by Relationship to Study Drug and by Maximum Severity (Safety Set)
                                                          Macrophage Activation-like                        Sepsis-Induced Immunoparalysis (N=
                                                          Syndrome (N= 48)                                  228)
                                                          Standard care +           Standard care +         Standard care +            Standard care +   Total
                                                          Anakinra (N=25)           Placebo (N=23)          rhIFNγ (N=106)             Placebo (N=122)   (N=276)
Any AE; Classification by Relationship to                 20 (80.0)                 20 (87.0)               104 (98.1)                 112 (91.8)        256 (92.8)
Study Drug, n (%)a
   Probably related                                       0 0 (0.0)                 1 (4.3)                 3 (2.8)                    1 (0.8)           5 (1.8)
   Possibly related                                       2 (8.0)                   1 (4.3)                 8 (7.5)                    5 (4.1)           16 (5.8)
   Probably not related                                   13 (52.0)                 11 (47.8)               70 (66.0)                  77 (63.1)         171 (62.0)
   Unrelated                                              5 (20.0)                  7 (30.4)                23 (21.7)                  29 (23.8)         64 (23.2)
Any AE; Classification by Maximum                         20 (80.0)                 20 (87.0)               104 (98.1)                 112 (91.8)        256 (92.8)
Severity, n (%)a
   Mild                                                   2 (8.0)                   1 (4.3)                 19 (17.9)                  25 (20.5)         47 (17.0)
   Moderate                                               6 (24.0)                  5 (21.7)                40 (37.7)                  42 (34.4)         93 (33.7)
   Severe                                                 12 (48.0)                 14 (60.9)               45 42.5)                   45 (36.9)         116 (42.0)
Blood and lymphatic system disorders, n                   15 (60.0)                 14 (60.9)               61 (57.5)                  65 (53.3)         155 (56.2)
(%)a
 Anaemia                                                  9 (36.0)                  9 (39.1)                44 (41.5)                  47 (38.5)         109 (39.5)
   Mild                                                   0 (0.0)                   2 (8.7)                 11 (10.4)                  11 (9.0)          24 (8.7)



    © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page31

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=31)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 31]]

                                                                                  31


  Moderate                                                2 (8.0)                   2 (8.7)                 13 (12.3)                  14 (11.5)   31 (11.2)
  Severe                                                  7 (28.0)                  5 (21.7)                20 (18.9)                  22 (18.0)   54 (19.6)
 Leukocytosis                                             5 (20.0)                  4 (17.4)                19 (17.9)                  19 (15.6)   47 (17.0)
  Mild                                                    1 (4.0)                   2 (8.7)                 7 (6.6)                    9 (7.4)     19 (6.9)
  Moderate                                                3 (12.0)                  2 (8.7)                 9 (8.5)                    10 (8.2)    24 (8.7)
  Severe                                                  1 (4.0)                   0 (0.0)                 3 (2.8)                    0 (0.0)     4 (1.4)
Cardiac disordersa                                        3 (12.0)                  5 (21.7)                19 (17.9)                  27 (22.1)   54 (19.6)
 Atrial fibrillation                                      1 (4.0)                   2 (8.7)                 7 (6.6)                    8 (6.6)     18 (6.5)
  Mild                                                    0 (0.0)                   0 (0.0)                 0 (0.0)                    3 (2.5)     3 (1.1)
  Moderate                                                1 (4.0)                   1 (4.3)                 2 (1.9)                    4 (3.3)     8 (2.9)
  Severe                                                  0 (0.0)                   1 (4.3)                 5 (4.7)                    1 (0.8)     7 (2.5)
 Bradycardia                                              0 (0.0)                   2 (8.7)                 1 (0.9)                    9 (7.4)     12 (4.3)
  Mild                                                    0 (0.0)                   1 (4.3)                 0 (0.0)                    7 (5.7)     8 (2.9)
  Moderate                                                0 (0.0)                   1 (4.3)                 1 (0.9)                    1 (0.8)     3 (1.1)
  Severe                                                  0 (0.0)                   0 (0.0)                 0 (0.0)                    1 (0.8)     1 (0.4)
 Tachycardia                                              1 (4.0)                   0 (0.0)                 10 (9.4)                   10 (8.2)    21 (7.6)
  Mild                                                    0 (0.0)                   0 (0.0)                 6 (5.7)                    9 (7.4)     15 (5.4)
  Moderate                                                1 (4.0)                   0 (0.0)                 4 (3.8)                    1 (0.8)     6 (2.2)
  Severe                                                  0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
Gastrointestinal disordersa                               3 (12.0)                  5 (21.7)                30 (28.3)                  30 (24.6)   68 (24.6)
 Constipation                                             0 (0.0)                   1 (4.3)                 7 (6.6)                    10 (8.2)    18 (6.5)



    © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page32

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=32)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 32]]

                                                                                  32


   Mild                                                   0 (0.0)                   1 (4.3)                 6 (5.7)                    9 (7.4)     16 (5.8)
   Moderate                                               0 (0.0)                   0 (0.0)                 1 (0.9)                    1 (0.8)     2 (0.7)
   Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
 Diarrhoea                                                3 (12.0)                  2 (8.7)                 20 (18.9)                  19 (15.6)   44 (15.9)
   Mild                                                   2 (8.0)                   2 (8.7)                 18 (17.0)                  17 (13.9)   39 (14.1)
   Moderate                                               1 (4.0)                   0 (0.0)                 2 (1.9)                    1 (0.8)     4 (1.4)
   Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    1 (0.8)     1 (0.4)
 Ileus                                                    0 (0.0)                   4 (17.4)                2 (1.9)                    3 (2.5)     9 (3.3)
   Mild                                                   0 (0.0)                   0 (0.0)                 0 (0.0)                    1 (0.8)     1 (0.4)
   Moderate                                               0 (0.0)                   4 (17.4)                2 (1.9)                    1 (0.8)     7 (2.5)
   Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    1 (0.8)     1 (0.4)
 Vomiting                                                 0 (0.0)                   0 (0.0)                 5 (4.7)                    5 (4.1)     10 (3.6)
   Mild                                                   0 (0.0)                   0 (0.0)                 5 (4.7)                    4 (3.3)     9 (3.3)
   Moderate                                               0 (0.0)                   0 (0.0)                 0 (0.0)                    1 (0.8)     1 (0.4)
   Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
General disorders and administration site                 3 (12.0)                  2 (8.7)                 25 (23.6)                  29 (23.8)   59 (21.4)
conditions, n (%)a
 Hypothermia                                              1 (4.0)                   1 (4.3)                 5 (4.7)                    6 (4.9)     13 (4.7)
   Mild                                                   1 (4.0)                   1 (4.3)                 4 (3.8)                    5 (4.1)     11 (4.0)
   Moderate                                               0 (0.0)                   0 (0.0)                 1 (0.9)                    1 (0.8)     2 (0.7)
   Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)



    © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page33

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=33)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 33]]

                                                                                  33


 Pyrexia                                                  2 (8.0)                   1 (4.3)                 20 (18.9)                  23 (18.9)   46 (16.7)
   Mild                                                   2 (8.0)                   1 (4.3)                 16 (15.1)                  18 (14.8)   37 (13.4)
   Moderate                                               0 (0.0)                   0 (0.0)                 4 (3.8)                    5 (4.1)     9 (3.3)
   Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
Infections and infestations, n (%)a                       3 (12.0)                  3 (13.0)                18 (17.0)                  21 (17.2)   45 (16.3)
 Fungal infection                                         1 (4.0)                   0 (0.0)                 7 (6.6)                    9 (7.4)     17 (6.2)
   Mild                                                   1 (4.0)                   0 (0.0)                 7 (6.6)                    9 (7.4)     17 (6.2)
   Moderate                                               0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
   Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
 Urinary tract infection                                  1 (4.0)                   0 (0.0)                 4 (3.8)                    4 (3.3)     9 (3.3)
   Mild                                                   0 (0.0)                   0 (0.0)                 2 (1.9)                    3 (2.5)     5 (1.8)
   Moderate                                               0 (0.0)                   0 (0.0)                 2 (1.9)                    1 (0.8)     3 (1.1)
   Severe                                                 1 (4.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     1 (0.4)
Injury, poisoning and procedural                          1 (4.0)                   0 (0.0)                 2 (1.9)                    6 (4.9)     9 (3.3)
complications, n (%)a
 Vascular access complication                             1 (4.0)                   0 (0.0)                 2 (1.9)                    5 (4.1)     8 (2.9)
   Mild                                                   1 (4.0)                   0 (0.0)                 1 (0.9)                    3 (2.5)     5 (1.8)
   Moderate                                               0 (0.0)                   0 (0.0)                 1 (0.9)                    1 (0.8)     2 (0.7)
   Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    1 (0.8)     1 (0.4)
Investigations, n (%)a                                    18 (72.0)                 17 (73.9)               86 (81.1)                  92 (75.4)   213 (77.2)




    © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page34

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=34)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 34]]

                                                                                34


Activated partial thromboplastin time                   0 (0.0)                   2 (8.7)                 3 (2.8)                    6 (4.9)     11 (4.0)
prolonged
 Mild                                                   0 (0.0)                   0 (0.0)                 0 (0.0)                    3 (2.5)     3 (1.1)
 Moderate                                               0 (0.0)                   1 (4.3)                 2 (1.9)                    2 (1.6)     5 (1.8)
 Severe                                                 0 (0.0)                   1 (4.3)                 1 (0.9)                    1 (0.8)     3 (1.1)
Alanine aminotransferase increased                      7 (28.0)                  9 (39.1)                42 (39.6)                  36 (29.5)   94 (34.1)
 Mild                                                   3 (12.0)                  3 (13.0)                27 (25.5)                  23 (18.9)   56 (20.3)
 Moderate                                               3 (12.0)                  3 (13.0)                8 (7.5)                    9 (7.4)     23 (8.3)
 Severe                                                 1 (4.0)                   3 (13.0)                7 (6.6)                    4 (3.3)     15 (5.4)
Amylase increased                                       4 (16.0)                  7 (30.4)                22 (20.8)                  22 (18.0)   55 (19.9)
 Mild                                                   2 (8.0)                   4 (17.4)                16 (15.1)                  16 (13.1)   38 (13.8)
 Moderate                                               2 (8.0)                   3 (13.0)                5 (4.7)                    3 (2.5)     13 (4.7)
 Severe                                                 0 (0.0)                   0 (0.0)                 1 (0.9)                    3 (2.5)     4 (1.4)
Aspartate aminotransferase increased                    9 (36.0)                  10 (43.5)               54 (50.9)                  47 (38.5)   120 (43.5)
 Mild                                                   3 (12.0)                  5 (21.7)                30 (28.3)                  30 (24.6)   68 (24.6)
 Moderate                                               5 (20.0)                  3 (13.0)                15 (14.2)                  13 (10.7)   36 (13.0)
 Severe                                                 1 (4.0)                   2 (8.7)                 9 (8.5)                    4 (3.3)     16 (5.8)
Blood alkaline phosphatase increased                    8 (32.0)                  7 (30.4)                28 (26.4)                  42 (34.4)   85 (30.8)
 Mild                                                   5 (20.0)                  5 (21.7)                22 (20.8)                  29 (23.8)   61 (22.1)
 Moderate                                               2 (8.0)                   0 (0.0)                 4 (3.8)                    6 (4.9)     12 (4.3)
 Severe                                                 1 (4.0)                   2 (8.7)                 2 (1.9)                    7 (5.7)     12 (4.3)



  © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page35

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=35)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 35]]

                                                                                35


Blood bilirubin increased                               4 (16.0)                  7 (30.4)                22 (20.8)                  23 (18.9)   56 (20.3)
 Mild                                                   3 (12.0)                  3 (13.0)                9 (8.5)                    12 (9.8)    27 (9.8)
 Moderate                                               0 (0.0)                   3 (13.0)                9 (8.5)                    5 (4.1)     17 (6.2)
 Severe                                                 1 (4.0)                   1 (4.3)                 4 (3.8)                    6 (4.9)     12 (4.3)
Blood creatine phosphokinase increased                  1 (4.0)                   3 (13.0)                14 (13.2)                  13 (10.7)   31 (11.2)
 Mild                                                   1 (4.0)                   3 (13.0)                11 (10.4)                  12 (9.8)    27 (9.8)
 Moderate                                               0 (0.0)                   0 (0.0)                 2 (1.9)                    1 (0.8)     3 (1.1)
 Severe                                                 0 (0.0)                   0 (0.0)                 1 (0.9)                    0 (0.0)     1 (0.4)
Blood creatinine increased                              8 (32.0)                  8 (34.8)                32 (30.2)                  22 (18.0)   70 (25.4)
 Mild                                                   3 (12.0)                  5 (21.7)                13 (12.3)                  12 (9.8)    33 (12.0)
 Moderate                                               4 (16.0)                  1 (4.3)                 17 (16.0)                  9 (7.4)     31 (11.2)
 Severe                                                 1 (4.0)                   2 (8.7)                 2 (1.9)                    1 (0.8)     6 (2.2)
Blood fibrinogen decreased                              0 (0.0)                   0 (0.0)                 7 (6.6)                    1 (0.8)     8 (2.9)
 Mild                                                   0 (0.0)                   0 (0.0)                 4 (3.8)                    0 (0.0)     4 (1.4)
 Moderate                                               0 (0.0)                   0 (0.0)                 3 (2.8)                    0 (0.0)     3 (1.1)
 Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    1 (0.8)     1 (0.4)
Blood lactate dehydrogenase increased                   1 (4.0)                   3 (13.0)                13 (12.3)                  13 (10.7)   30 (10.9)
 Mild                                                   1 (4.0)                   2 (8.7)                 10 (9.4)                   12 (9.8)    25 (9.1)
 Moderate                                               0 (0.0)                   0 (0.0)                 2 (1.9)                    1 (0.8)     3 (1.1)
 Severe                                                 0 (0.0)                   1 (4.3)                 1 (0.9)                    0 (0.0)     2 (0.7)
Blood urea increased                                    0 (0.0)                   0 (0.0)                 6 (5.7)                    6 (4.9)     12 (4.3)



  © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page36

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=36)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 36]]

                                                                                36


 Mild                                                   0 (0.0)                   0 (0.0)                 5 (4.7)                    5 (4.1)     10 (3.6)
 Moderate                                               0 (0.0)                   0 (0.0)                 1 (0.9)                    1 (0.8)     2 (0.7)
 Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
Cortisol decreased                                      1 (4.0)                   1 (4.3)                 2 (1.9)                    4 (3.3)     8 (2.9)
 Mild                                                   0 (0.0)                   1 (4.3)                 2 (1.9)                    3 (2.5)     6 (2.2)
 Moderate                                               1 (4.0)                   0 (0.0)                 0 (0.0)                    1 (0.8)     2 (0.7)
 Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
Creatinine renal clearance decreased                    0 (0.0)                   1 (4.3)                 3 (2.8)                    2 (1.6)     6 (2.2)
 Mild                                                   0 (0.0)                   0 (0.0)                 1 (0.9)                    0 (0.0)     1 (0.4)
 Moderate                                               0 (0.0)                   0 (0.0)                 1 (0.9)                    1 (0.8)     2 (0.7)
 Severe                                                 0 (0.0)                   1 (4.3)                 1 (0.9)                    1 (0.8)     3 (1.1)
Gamma-glutamyltransferase increased                     9 (36.0)                  10 (43.5)               39 (36.8)                  29 (23.8)   87 (31.5)
 Mild                                                   5 (20.0)                  4 (17.4)                24 (22.6)                  15 (12.3)   48 (17.4)
 Moderate                                               1 (4.0)                   6 (26.1)                13 (12.3)                  9 (7.4)     29 (10.5)
 Severe                                                 3 (12.0)                  0 (0.0)                 2 (1.9)                    5 (4.1)     10 (3.6)
Hepatic enzyme increased                                1 (4.0)                   0 (0.0)                 7 (6.6)                    6 (4.9)     14 (5.1)
 Mild                                                   1 (4.0)                   0 (0.0)                 3 (2.8)                    3 (2.5)     7 (2.5)
 Moderate                                               0 (0.0)                   0 (0.0)                 3 (2.8)                    2 (1.6)     5 (1.8)
 Severe                                                 0 (0.0)                   0 (0.0)                 1 (0.9)                    1 (0.8)     2 (0.7)
International normalised ratio increased                1 (4.0)                   5 (21.7)                19 (17.9)                  21 (17.2)   46 (16.7)
 Mild                                                   0 (0.0)                   4 (17.4)                12 (11.3)                  13 (10.7)   29 (10.5)



  © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page37

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=37)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 37]]

                                                                                37


 Moderate                                               0 (0.0)                   1 (4.3)                 7 (6.6)                    6 (4.9)     14 (5.1)
 Severe                                                 1 (4.0)                   0 (0.0)                 0 (0.0)                    2 (1.6)     3 (1.1)
Lymphocyte count decreased                              1 (4.0)                   1 (4.3)                 4 (3.8)                    3 (2.5)     9 (3.3)
 Mild                                                   1 (4.0)                   1 (4.3)                 2 (1.9)                    1 (0.8)     5 (1.8)
 Moderate                                               0 (0.0)                   0 (0.0)                 2 (1.9)                    1 (0.8)     3 (1.1)
 Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    1 (0.8)     1 (0.4)
Platelet count decreased                                9 (36.0)                  13 (56.5)               42 (39.6)                  49 (40.2)   113 (40.9)
 Mild                                                   3 (12.0)                  4 (17.4)                16 (15.1)                  30 (24.6)   53 (19.2)
 Moderate                                               2 (8.0)                   4 (17.4)                13 (12.3)                  9 (7.4)     28 (10.1)
 Severe                                                 4 (16.0)                  5 (21.7)                13 (12.3)                  10 (8.2)    32 (11.6)
Platelet count increased                                0 (0.0)                   1 (4.3)                 4 (3.8)                    4 (3.3)     9 (3.3)
 Mild                                                   0 (0.0)                   1 (4.3)                 4 (3.8)                    3 (2.5)     8 (2.9)
 Moderate                                               0 (0.0)                   0 (0.0)                 0 (0.0)                    1 (0.8)     1 (0.4)
 Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
Troponin increased                                      2 (8.0)                   1 (4.3)                 5 (4.7)                    6 (4.9)     14 (5.1)
 Mild                                                   1 (4.0)                   0 (0.0)                 1 (0.9)                    5 (4.1)     7 (2.5)
 Moderate                                               0 (0.0)                   1 (4.3)                 1 (0.9)                    0 (0.0)     2 (0.7)
 Severe                                                 1 (4.0)                   0 (0.0)                 3 (2.8)                    1 (0.8)     5 (1.8)
Urine output decreased                                  0 (0.0)                   1 (4.3)                 2 (1.9)                    5 (4.1)     8 (2.9)
 Mild                                                   0 (0.0)                   0 (0.0)                 2 (1.9)                    3 (2.5)     5 (1.8)
 Moderate                                               0 (0.0)                   1 (4.3)                 0 (0.0)                    0 (0.0)     1 (0.4)



  © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page38

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=38)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 38]]

                                                                                  38


  Severe                                                  0 (0.0)                   0 (0.0)                 0 (0.0)                    2 (1.6)     2 (0.7)
 White blood cell count decreased                         3 (12.0)                  0 (0.0)                 12 (11.3)                  9 (7.4)     24 (8.7)
  Mild                                                    1 (4.0)                   0 (0.0)                 9 (8.5)                    9 (7.4)     19 (6.9)
  Moderate                                                2 (8.0)                   0 (0.0)                 3 (2.8)                    0 (0.0)     5 (1.8)
  Severe                                                  0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
Metabolism and nutrition disorders, n (%)a                12 (48.0)                 15 (65.2)               64 (60.4)                  65 (53.3)   156 (56.5)
 Acidosis                                                 0 (0.0)                   1 (4.3)                 3 (2.8)                    6 (4.9)     10 (3.6)
  Mild                                                    0 (0.0)                   0 (0.0)                 1 (0.9)                    1 (0.8)     2 (0.7)
  Moderate                                                0 (0.0)                   0 (0.0)                 0 (0.0)                    1 (0.8)     1 (0.4)
  Severe                                                  0 (0.0)                   1 (4.3)                 2 (1.9)                    4 (3.3)     7 (2.5)
 Alkalosis                                                0 (0.0)                   2 (8.7)                 4 (3.8)                    5 (4.1)     11 (4.0)
  Mild                                                    0 (0.0)                   0 (0.0)                 0 (0.0)                    2 (1.6)     2 (0.7)
  Moderate                                                0 (0.0)                   1 (4.3)                 0 (0.0)                    0 (0.0)     1 (0.4)
  Severe                                                  0 (0.0)                   1 (4.3)                 4 (3.8)                    3 (2.5)     8 (2.9)
 Hyperglycaemia                                           3 (12.0)                  3 (13.0)                11 (10.4)                  19 (15.6)   36 (13.0)
  Mild                                                    2 (8.0)                   3 (13.0)                8 (7.5)                    15 (12.3)   28 (10.1)
  Moderate                                                1 (4.0)                   0 (0.0)                 0 (0.0)                    4 (3.3)     5 (1.8)
  Severe                                                  0 (0.0)                   0 (0.0)                 3 (2.8)                    0 (0.0)     3 (1.1)
 Hyperkalaemia                                            4 (16.0)                  4 (17.4)                17 (16.0)                  16 (13.1)   41 (14.9)
  Mild                                                    2 (8.0)                   1 (4.3)                 8 (7.5)                    13 (10.7)   24 (8.7)
  Moderate                                                2 (8.0)                   1 (4.3)                 5 (4.7)                    3 (2.5)     11 (4.0)



    © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page39

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=39)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 39]]

                                                                                39


 Severe                                                 0 (0.0)                   2 (8.7)                 4 (3.8)                    0 (0.0)     6 (2.2)
Hypermagnesaemia                                        1 (4.0)                   4 (17.4)                9 (8.5)                    5 (4.1)     19 (6.9)
 Mild                                                   0 (0.0)                   3 (13.0)                5 (4.7)                    5 (4.1)     13 (4.7)
 Moderate                                               1 (4.0)                   0 (0.0)                 1 (0.9)                    0 (0.0)     2 (0.7)
 Severe                                                 0 (0.0)                   1 (4.3)                 3 (2.8)                    0 (0.0)     4 (1.4)
Hypernatraemia                                          7 (28.0)                  10 (43.5)               37 (34.9)                  36 (29.5)   90 (32.6)
 Mild                                                   4 (16.0)                  5 (21.7)                23 (21.7)                  24 (19.7)   56 (20.3)
 Moderate                                               0 (0.0)                   4 (17.4)                10 (9.4)                   10 (8.2)    24 (8.7)
 Severe                                                 3 (12.0)                  1 (4.3)                 4 (3.8)                    2 (1.6)     10 (3.6)
Hyperphosphataemia                                      1 (4.0)                   4 (17.4)                6 (5.7)                    6 (4.9)     17 (6.2)
 Mild                                                   1 (4.0)                   3 (13.0)                6 (5.7)                    6 (4.9)     16 (5.8)
 Moderate                                               0 (0.0)                   1 (4.3)                 0 (0.0)                    0 (0.0)     1 (0.4)
 Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
Hypertriglyceridaemia                                   2 (8.0)                   0 (0.0)                 2 (1.9)                    4 (3.3)     8 (2.9)
 Mild                                                   0 (0.0)                   0 (0.0)                 1 (0.9)                    3 (2.5)     4 (1.4)
 Moderate                                               1 (4.0)                   0 (0.0)                 1 (0.9)                    1 (0.8)     3 (1.1)
 Severe                                                 1 (4.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     1 (0.4)
Hypoalbuminaemia                                        3 (12.0)                  4 (17.4)                15 (14.2)                  14 (11.5)   36 (13.0)
 Mild                                                   0 (0.0)                   0 (0.0)                 3 (2.8)                    4 (3.3)     7 (2.5)
 Moderate                                               3 (12.0)                  2 (8.7)                 9 (8.5)                    8 (6.6)     22 (8.0)
 Severe                                                 0 (0.0)                   2 (8.7)                 3 (2.8)                    2 (1.6)     7 (2.5)



  © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page40

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=40)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 40]]

                                                                                40


Hypocalcaemia                                           2 (8.0)                   2 (8.7)                 15 (14.2)                  8 (6.6)     27 (9.8)
 Mild                                                   1 (4.0)                   0 (0.0)                 6 (5.7)                    6 (4.9)     13 (4.7)
 Moderate                                               0 (0.0)                   1 (4.3)                 6 (5.7)                    1 (0.8)     8 (2.9)
 Severe                                                 1 (4.0)                   1 (4.3)                 3 (2.8)                    1 (0.8)     6 (2.2)
Hypoglycaemia                                           4 (16.0)                  4 (17.4)                15 (14.2)                  17 (13.9)   40 (14.5)
 Mild                                                   2 (8.0)                   3 (13.0)                9 (8.5)                    14 (11.5)   28 (10.1)
 Moderate                                               2 (8.0)                   1 (4.3)                 6 (5.7)                    3 (2.5)     12 (4.3)
 Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
Hypokalaemia                                            2 (8.0)                   3 (13.0)                23 (21.7)                  24 (19.7)   52 (18.8)
 Mild                                                   2 (8.0)                   1 (4.3)                 12 (11.3)                  21 (17.2)   36 (13.0)
 Moderate                                               0 (0.0)                   1 (4.3)                 7 (6.6)                    1 (0.8)     9 (3.3)
 Severe                                                 0 (0.0)                   1 (4.3)                 4 (3.8)                    2 (1.6)     7 (2.5)
Hypomagnesaemia                                         1 (4.0)                   3 (13.0)                8 (7.5)                    8 (6.6)     20 (7.2)
 Mild                                                   1 (4.0)                   3 (13.0)                8 (7.5)                    7 (5.7)     19 (6.9)
 Moderate                                               0 (0.0)                   0 (0.0)                 0 (0.0)                    1 (0.8)     1 (0.4)
 Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
Hyponatraemia                                           2 (8.0)                   3 (13.0)                17 (16.0)                  11 (9.0)    33 (12.0)
 Mild                                                   2 (8.0)                   3 (13.0)                17 (16.0)                  10 (8.2)    32 (11.6)
 Moderate                                               0 (0.0)                   0 (0.0)                 0 (0.0)                    1 (0.8)     1 (0.4)
 Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
Hypophosphataemia                                       1 (4.0)                   4 (17.4)                11 (10.4)                  12 (9.8)    28 (10.1)



  © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page41

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=41)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 41]]

                                                                                  41


   Mild                                                   0 (0.0)                   2 (8.7)                 8 (7.5)                    9 (7.4)     19 (6.9)
   Moderate                                               1 (4.0)                   2 (8.7)                 3 (2.8)                    3 (2.5)     9 (3.3)
   Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
 Metabolic acidosis                                       1 (4.0)                   1 (4.3)                 2 (1.9)                    2 (1.6)     6 (2.2)
   Mild                                                   0 (0.0)                   0 (0.0)                 1 (0.9)                    0 (0.0)     1 (0.4)
   Moderate                                               0 (0.0)                   1 (4.3)                 0 (0.0)                    1 (0.8)     2 (0.7)
   Severe                                                 1 (4.0)                   0 (0.0)                 1 (0.9)                    1 (0.8)     3 (1.1)
Psychiatric disorders, n (%)a                             0 (0.0)                   3 (13.0)                11 (10.4)                  12 (9.8)    26 (9.4)
 Agitation                                                0 (0.0)                   0 (0.0)                 5 (4.7)                    6 (4.9)     11 (4.0)
   Mild                                                   0 (0.0)                   0 (0.0)                 5 (4.7)                    6 (4.9)     11 (4.0)
   Moderate                                               0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
   Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
 Delirium                                                 0 (0.0)                   3 (13.0)                3 (2.8)                    4 (3.3)     10 (3.6)
   Mild                                                   0 (0.0)                   2 (8.7)                 1 (0.9)                    2 (1.6)     5 (1.8)
   Moderate                                               0 (0.0)                   1 (4.3)                 2 (1.9)                    1 (0.8)     4 (1.4)
   Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    1 (0.8)     1 (0.4)
Renal and urinary disorders, n (%)a                       0 (0.0)                   1 (4.3)                 15 (14.2)                  13 (10.7)   29 (10.5)
 Acute kidney injury                                      0 (0.0)                   0 (0.0)                 9 (8.5)                    8 (6.6)     17 (6.2)
   Mild                                                   0 (0.0)                   0 (0.0)                 2 (1.9)                    3 (2.5)     5 (1.8)
   Moderate                                               0 (0.0)                   0 (0.0)                 5 (4.7)                    4 (3.3)     9 (3.3)
   Severe                                                 0 (0.0)                   0 (0.0)                 2 (1.9)                    1 (0.8)     3 (1.1)



    © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page42

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=42)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 42]]

                                                                                  42


 Haematuria                                               0 (0.0)                   0 (0.0)                 5 (4.7)                    1 (0.8)     6 (2.2)
   Mild                                                   0 (0.0)                   0 (0.0)                 2 (1.9)                    1 (0.8)     3 (1.1)
   Moderate                                               0 (0.0)                   0 (0.0)                 3 (2.8)                    0 (0.0)     3 (1.1)
   Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
Respiratory, thoracic and mediastinal                     3 (12.0)                  2 (8.7)                 17 (16.0)                  14 (11.5)   36 (13.0)
disorders, n (%)a
 Aspiration                                               1 (4.0)                   0 (0.0)                 2 (1.9)                    3 (2.5)     6 (2.2)
   Mild                                                   0 (0.0)                   0 (0.0)                 1 (0.9)                    2 (1.6)     3 (1.1)
   Moderate                                               0 (0.0)                   0 (0.0)                 0 (0.0)                    1 (0.8)     1 (0.4)
   Severe                                                 1 (4.0)                   0 (0.0)                 1 (0.9)                    0 (0.0)     2 (0.7)
 Pleural effusion                                         0 (0.0)                   1 (4.3)                 3 (2.8)                    2 (1.6)     6 (2.2)
   Mild                                                   0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
   Moderate                                               0 (0.0)                   1 (4.3)                 1 (0.9)                    2 (1.6)     4 (1.4)
   Severe                                                 0 (0.0)                   0 (0.0)                 2 (1.9)                    0 (0.0)     2 (0.7)
Skin and subcutaneous tissue disorders, n                 2 (8.0)                   1 (4.3)                 7 (6.6)                    8 (6.6)     18 (6.5)
(%)a
 Rash                                                     1 (4.0)                   0 (0.0)                 2 (1.9)                    5 (4.1)     8 (2.9)
   Mild                                                   0 (0.0)                   0 (0.0)                 1 (0.9)                    5 (4.1)     6 (2.2)
   Moderate                                               1 (4.0)                   0 (0.0)                 1 (0.9)                    0 (0.0)     2 (0.7)
   Severe                                                 0 (0.0)                   0 (0.0)                 0 (0.0)                    0 (0.0)     0 (0.0)
Vascular disorders                                        4 (16.0)                  8 (34.8)                29 (27.4)                  32 (26.2)   73 (26.4)



    © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page43

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=43)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 43]]

                                                                                43


Hypertension                                            3 (12.0)                  4 (17.4)                23 (21.7)                  25 (20.5)   55 (19.9)
 Mild                                                   1 (4.0)                   1 (4.3)                 14 (13.2)                  12 (9.8)    28 (10.1)
 Moderate                                               1 (4.0)                   2 (8.7)                 4 (3.8)                    6 (4.9)     13 (4.7)
 Severe                                                 1 (4.0)                   1 (4.3)                 5 (4.7)                    7 (5.7)     14 (5.1)
Hypotension                                             2 (8.0)                   4 (17.4)                11 (10.4)                  10 (8.2)    27 (9.8)
 Mild                                                   0 (0.0)                   2 (8.7)                 5 (4.7)                    5 (4.1)     12 (4.3)
 Moderate                                               1 (4.0)                   0 (0.0)                 4 (3.8)                    1 (0.8)     6 (2.2)
 Severe                                                 1 (4.0)                   2 (8.7)                 2 (1.9)                    4 (3.3)     9 (3.3)
          Abbreviations: MALS, macrophage activation-like syndrome; PT, preferred term; rhIFNγ, recombinant human activated
          interferon-gamma; SOC, system organ class; TEAE, treatment-emergent adverse event.
          Footnote: The non-serious TEAEs were classified by severity using Medra 27.0 for events captured during the 90 days of
          follow-up for the enrolled 276 patients. In the analysis, non-serious TEAEs are categorised by severity gradings (mild,
          moderate and severe). It is clarified that the total of each SOC refers to the number of patients and not to the cumulative
          number of events.
          a
              These data represent the number of patients, whereas all other data in the table correspond to the number of events.




  © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.


```

### DOC-003 PDF page44

[Direct source](../../../joi250116supp2_prod_1771885794.27755.pdf#page=44)

```text
[[source_document_id: DOC-003]]
[[source_pdf: joi250116supp2_prod_1771885794.27755.pdf]]
[[source_pdf_page: 44]]

          eTable 15. Quantification of the Benefit/Risk Ratio in the ImmunoSep Trial
Total enrolled patients                                                                      95% CIs
     Number of patients needed to treat to attain the primary endpoint (NNT)          5.9    3.9 to 14.7
     Number of patients needed to treat to induce at least 1 serious TEAE (NNH1)      200    -14.1 to
                                                                                             1220
     Number of patients needed to treat to induce at least 2 serious TEAEs (NNH2)     6.6    3.0 to 27.8
     Number of patients needed to treat to induce at least 3 serious TEAEs (NNH3)     10.3   4.7 to 50.0
     Number of patients needed to treat to induce at least 4 serious TEAEs (NNH4)     7.7    4.18 to 58.8
     Number of patients needed to treat to induce at least 5 serious TEAEs (NNH5)     12.5   5.4 to 37.0
Patients with macrophage activation-like syndrome
     Number of patients needed to treat to attain the primary endpoint (NNT)          3.3    1.9 to 25.6
     Number of patients needed to treat to induce at least 1 serious TEAE (NNH1)      8.8    3.2 to 10.0
     Number of patients needed to treat to induce at least 2 serious TEAEs (NNH2)     23.8   -5.7 to 33.3
     Number of patients needed to treat to induce at least 3 serious TEAEs (NNH3)     10.9   -5.7 to 12.9
     Number of patients needed to treat to induce at least 4 serious TEAEs (NNH4)     10.4   -5.9 to 12.9
     Number of patients needed to treat to induce at least 5 serious TEAEs (NNH5)     10.1   -0.3 to 12.9
Patients with sepsis-induced immunoparalysis
     Number of patients needed to treat to attain the primary endpoint (NNT)          7.1    3.9 to 35.7
     Number of patients needed to treat to induce at least 1 serious TEAE (NNH1)      47.6   9.9 to 55.8
     Number of patients needed to treat to induce at least 2 serious TEAEs (NNH2)     5.6    3.4 to 17.9
     Number of patients needed to treat to induce at least 3 serious TEAEs (NNH3)     9.9    3.9 to 76.2
     Number of patients needed to treat to induce at least 4 serious TEAEs (NNH4)     7.2    5.9 to 23.8
     Number of patients needed to treat to induce at least 5 serious TEAEs (NNH5)     13.7   5.9 to 23.8
          Abbreviations: CI, confidence interval; NNT, number of patients needed to treat;
          NNH, number of patients needed to harm.


```
