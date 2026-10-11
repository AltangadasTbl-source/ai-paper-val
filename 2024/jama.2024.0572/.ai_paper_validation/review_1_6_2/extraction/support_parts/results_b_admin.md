# Support quantitative map: results B and administrative sources

Scope: DOC-006 PDF pp. 33-53 (21 pages), DOC-002 PDF pp. 1-30 (30 pages), DOC-007 PDF p. 1 (1 page). Total 52 physical pages, all mapped. All three documents are REPORT by content; none contains a prospective statistical plan. All pages are reusable-backed; fresh-required extraction units: 0. The requested 51-page count was arithmetic shorthand; the exact assignment contains 52 pages.

Only source-linked extraction assets were used. No prior scientific conclusions, candidate sets, screening, checker, classification, adjudication, or final reports were read. No candidate diagnosis is made here. Local B identifiers identify complete display groups, each including every displayed row and cell; they are not finding IDs. The full page transcriptions below preserve all numeric inputs, labels, units, confidence intervals, P values and footnotes. Interpret each cell under its row and column heading, not by proximity in a wrapped native text line.

## Provenance

Read QUALITY_CONTROL_SCOPE.md completely, workflow_1_6_2/review_contract.md completely, source_inventory.md, source_coverage.md, evidence_asset_inventory.md, tooling_record.md, and coverage_manifest.md. Reused DOC-006 native_text/page-033.txt through page-053.txt and corresponding page_images/page-033.png through page-053.png, all under .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/. Visually inspected each of the 21 complete rendered pages. Legacy text/render engines have unrecorded versions; the curator records source identity and hashes. Reused DOC-002 and DOC-007 by_page.txt/layout.txt under .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/. Their direct-layout identity is recorded in inventory.

New durable derivative: this map only. Engine: agent reading/reconstruction plus Bash cat, sed and printf for literal transcription insertion. Commands: cat exact reused native text; view_image exact reused page PNG; sed page-marker-bounded reads of DOC-002 by_page.txt; pdfimages -f 28 -l 28 -list joi240006supp1_prod_1708623114.97236.pdf (Poppler26.01.0, transient output, no raster image on p.28). No new OCR, rendering, or Python extraction was required. Compute device CPU. Sources and reused assets preserved.

## Page coverage and relationship index

| Local ID | DOC-006 physical page | Complete applicable content | Main-paper matching key |
|---|---:|---|---|
| B001 | 33-34 | eFigure20 panels ab-ag: seven-level mRS treatment distributions, mismatch presence by core definition and threshold | 90-day ordinal mRS; randomized treatment; mismatch definition; CTP/MRI vs composite core |
| B002 | 35 | eTable1 first page: all demographic, history, examination and occlusion rows | Baseline as-treated EVT170/MM166; separate from ITT168/168 |
| B003 | 36 | eTable1 continuation: every volume, time and treatment-characteristic cell; NIHSS, ASPECTS and core footnotes | Baseline units; imaging definition; treatment received |
| B004 | 37 | eTable1 continuation footnotes: manual CT delineation3readers; composite maximum definition | CT hypodensity; composite core=max(CTP/MRI core, CT hypodensity) |
| B005 | 38 | eTable2: all ITT clinical/imaging outcome counts, denominators, percentages, medians and IQRs | ITT168/168; 90-day mRS0-2,0-3,5-6; mortality; safety; infarct growth |
| B006 | 39 | eTable3: 5 ASPECTS rows ×4 outcomes, all20estimates and95%CIs | Site-investigator ASPECTS sensitivity; mRS shift/aGenOR and binary/aRR |
| B007 | 40 | eTable4: 6CTP strata×4outcomes, all22estimates/CIs and2N/A cells | CT perfusion only; rCBF<30%; core thresholds70/100/150ml |
| B008 | 41 | eTable5:4outcomes×2volume definitions×2treatment groups, all16estimates/CIs and8interaction Ps, outcome totals | As-treated170/166; ischemic volume per10ml; within-arm prognostic association |
| B009 | 42 | eTable6:3outcomes×4modalities; all12AIC/BIC rows and8AUC/CIs; preferred labels; model footnotes | Model comparison: ordinal logistic mRS; binary discrimination; AIC/BIC/AUC |
| B010 | 43-44 | eTable7: both composite mismatch thresholds, within-arm ordinal and binary results, all counts/RR/RD/CIs and8last-column Ps | As-treated mismatch vs no mismatch(reference); adjustment age/NIHSS/LKW-to-randomization/CTP-MRIcore |
| B011 | 45-46 | eTable8: imaging concordance/discordance within each treatment; all medians/counts/RR/RD/CIs and interaction Ps | Concordant ASPECTS<6/core≥70ml; discordant1 ASPECTS<6/core<70ml; discordant2 ASPECTS6-10/core≥70ml |
| B012 | 47-48 | eTable9: CTP/MRI profile-stratified EVT treatment effects; all medians/counts/aGenOR/aRR/CIs and interactions | Between-arm EVT vs MM within imaging profiles; distinguish from within-arm eTable8 |
| B013 | 49-50 | eTable10: composite profile-stratified EVT treatment effects; all medians/counts/aGenOR/aRR/CIs and interactions | Between-arm EVT vs MM; composite core; concordant/discordant profiles |
| B014 | 51 | eTable11: MRDWI follow-up growth, all3group Ns and9median/IQR cells | Follow-up modality MRDWI; MM101; mTICI0-2a24; mTICI2b-379 |
| B015 | 52 | eTable12: all4growth comparisons with4group Ns,8median/IQR cells and4Ps | Functional independence46/dependence290; independent ambulation96/noambulation240; total336 |
| B016 | 53 | eTable13: all3patient rows×5clinical values; ≥10mloverestimation threshold; N/A footnote | Ischemic core minus follow-up infarct; acquisition/reperfusion windows;3patients |

Every DOC-006 page above is COMPLETE, including footnote-only p.37 and table continuations pp.44,46,48,50. No page is omitted for sparse text. Table6 has12model rows: ordinal mRS AUC not applicable, binary outcomes8AUC/CIs. Table7's columns do not print treatment headings or a last-column heading on these pages; left/right treatment mapping follows surrounding as-treated convention and title. Preserve this limitation rather than inventing a printed label. Each ordinal ratio and binary RR/RD is adjusted as indicated; interaction P values test between-treatment interaction and are not automatically individual-arm estimate tests. Table9/10 columns explicitly run MM then EVT, while Table1/2/5/8 run EVT then MM.

## Explicit eFigure20 panel transcription (B001)

Each row is a seven-element percentage vector in legend order mRS0,1,2,3,4,5,6. Axis0%-100% in10%increments. Values below are visually read, including crowded zeros and single digits. No counts are inferred from rounded percentages. The next-page first panel continues ae heading on p.33.

| Physical page | Panel/core/threshold/presence | EVT N; mRS0-6 percentages | MM N; mRS0-6 percentages |
|---:|---|---|---|
|33|ab composite, ratio≥1.2 AND volume≥10ml absent|34;0,3,12,24,26,3,32|40;0,0,8,10,25,20,38|
|33|ac composite, ratio≥1.2 AND volume≥10ml present|134;1,5,15,17,13,10,38|128;0,2,5,12,20,19,43|
|33|ad CTP/MRI, ratio≥1.8 AND volume≥15ml absent|58;0,3,7,14,24,10,41|62;0,2,2,6,19,21,50|
|34|ae CTP/MRI, ratio≥1.8 AND volume≥15ml present|110;2,5,18,21,12,7,35|106;0,2,8,14,22,18,37|
|34|af composite, ratio≥1.8 AND volume≥15ml absent|111;1,5,13,16,20,7,38|100;0,2,6,10,21,20,41|
|34|ag composite, ratio≥1.8 AND volume≥15ml present|57;2,4,18,23,9,11,35|68;0,1,4,13,21,18,43|

## Statistical and numeric comparison structure

Each table below is a complete display group, with named key outcome/contrast/population. For statistical inventory, independently track every estimate-CI combination, each interaction test and each model-selection comparison. Reference cells and N/A cells are retained as source definitions. For numeric inventory, track every numerator/denominator/percentage triple and row/column partition without replacing printed adjusted measures with crude ratios.

B002/B003 baseline categorical counts partition sex, race, referral and occlusion groups against as-treated170/166 headers. Other rows may have variable-specific denominators; the printed cells remain authoritative and denominators absent from cells are not invented. Table1 printed CTP/MRI footnote uses rCBF<30%, ADC<620×10^-6 mm/s²; units transcribed as printed, including superscripts visible on p.36. ASPECTS10points, lower=worse injury; NIHSS42points, higher=more deficits. B004 CT delineation3readers and composite larger-of-two definition affect core measures.

B005 ITT168/168 differs by population definition from B008170/166. Binary outcomes use 90-day mRS0-2/0-3/5-6, all-cause mortality, symptomatic hemorrhage, parenchymal hemorrhage, neurological worsening and early neurological improvement. Early improvement denominators165/166 are printed explicitly. Growth measures in ml distinguish CTP/MRI, composite and CT baseline measures; each median/IQR stands separately, so do not subtract summary medians to recreate growth.

B006 site ASPECTS3-5/6-10 and individual3/4/5 strata cross four outcomes. B007 CT-perfusion-only sensitivity uses nested <70/≥70,<100/≥100,<150/≥150 groups, so totals across all six rows are not a partition. N/A means could not be evaluated.

B008 within-treatment prognostic volume effects use per10ml increments, separately for CT hypodensity/composite. mRS distribution medians4(3-6)/5(4-6); binary outcome counts34/170 vs12/166,66/170 vs30/166,77/170 vs101/166. Interaction tests belong to paired slopes across treatment groups, not effect-CI null checks within one arm.

B009 lower AIC/BIC means more parsimonious; higher AUC means better predictive value. Composite marked preferred for all three outcomes. Ordinal mRS parameters explicitly use ordinal logistic regression; AUC is NA for those4rows.

B010 mismatch presence reference=no mismatch. Composite thresholds1.2/10ml and1.8/15ml are separate analyses. First criterion groups34/136EVT and40/126MM; second112/58EVT and99/67MM. Ordinal and binary effects are adjusted for age, NIHSS, time from last known well to randomization, CTP/MRI core volume. All aRD signs and intervals are retained literally, including -0.000 and positive0.168(0.011,0.325).

B011 concordant and two discordant profiles reference concordant; analysis headers EVT163/MM156. Table8 within-arm effects differ in estimand from Table9's treatment-effect rows. Each3profile count set must be examined within its own display. Table9 explicitly prints MM1/11(9.1%) vsEVT0/12(0%) for discordant2 mRS0-2 and MM3/11(27.3%) vsEVT0/12(0%) for mRS0-3; preserve these cells as printed. Table8 prints EVT1/12(8%) vsMM0/11(0%) and EVT3/12(25%) vsMM0/11(0%) for those respective rows. No adjudication is made here.

B012/B013 effects use aGenOR for ordinal distribution, aRR for binary thresholds; printed last column is interaction P, reference concordant. N/A could not be evaluated. Core modalities differ between Table9 and10; do not equate denominators across them. Both report exact profile-specific counts and outcome medians.

B014 MRI-follow-up restriction gives101+24+79=204contributors, not the full336. B015 outcome group totals290+46=336 and240+96=336; P<0.001 printed for each of4comparisons. Test identity is not supplied in these table pages and should be matched to eMethods by its assigned mapper. B016 IDs1-3 are patient identifiers, not counts for subgroup analysis. Printed threshold≥10ml applies to ischemic-core overestimation relative to follow-up volume. N/A denotes patient with medical management.

## Complete native table-cell transcriptions, visually checked

The following physical-page records preserve every row and cell. They complement the structured index and figure transcription. Page footer numbers are printed page numbers one less than PDF physical page; evidence links use the physical PDF page. All links below are package-root-relative source paths; the coordinator resolves them relative to final-report location.

### DOC-006 physical page 35

Source: joi240006supp5_prod_1708623115.01733.pdf#page=35

```text
eTables
eTable 1. Baseline clinical and imaging characteristics of study population (as-treated),
stratified based on treatment.

                                                 Endovascular           Medical care only
                                                 thrombectomy
                                                 N=170                  N=166
 Demographics
 Age (years)                                     66.0 (59.0-75.0)       67.0 (58.0-75.0)
 Sex                    Female                   68 (40.0%)             71 (42.8%)
                        Male                     102 (60.0%)            95 (57.2%)
 Race                   Asian                    5 (2.9%)               3 (1.8%)
                        Black                    24 (14.1%)             24 (14.5%)
                        Caucasian                126 (74.1%)            123 (74.1%)
                        Native Hawaiian or       2 (1.2%)               0
                        Pacific Islander
                        Other or unknown         13 (7.6%)              16 (9.6%)
 Transferred         to Directly Presenting to   71 (41.8%)             65 (39.2%)
 thrombectomy-          thrombectomy-capable
 Capable Center         Center
                        Transferred         to   99 (58.2%)             101 (60.8%)
                        thrombectomy-
                        Capable Center
 Medical History
 H/o Hypertension                                132 (77.6%)            120 (72.3%)
 H/o Diabetes Mellitus                           50 (29.4%)             54 (32.5%)
 H/o Atrial Fibrillation                         44 (25.9%)             38 (22.9%)
 H/o Coronary Artery                             39 (23.2%)             25 (15.6%)
 Disease
 H/o Congestive Heart                            20 (11.8%)             18 (10.8%)
 Failure
 H/o Ischemic Stroke                             18 (10.6%)             13 (7.8%)
 H/o          Transient                          4 (2.4%)               8 (4.8%)
 Ischemic Attack
 Physical Examination
 Hemisphere affected                             78 (45.9%)             69 (41.6%)
 NIH Stroke Scale at                             19 (15-23)             19 (15-22)
 thrombectomy
 hospital
 Neuroimaging findings
 Occlusion location      ICA                     75 (44.1%)             64 (38.6%)
                         MCA M1                  88 (51.8%)             94 (56.6%)
                         MCA M2                  7 (4.1%)               8 (4.8%)
 Tandem occlusions                               54 (31.8%)             43 (25.9%)


                                           34

```

### DOC-006 physical page 36

Source: joi240006supp5_prod_1708623115.01733.pdf#page=36

```text
                                                     Endovascular              Medical care only
                                                     thrombectomy
 CT ASPECTS at                                       4 (3-5)                 4 (4-5)
 thrombectomy
 hospital
 Composite          core                            103 (69-140)             100 (74-136)
 volume (ml)
 CTP/MRI core volume                                70 (39-110)              77 (48-104)
 (ml)
 CT         Hypodensity                             84 (45-114)              87 (49-113)
 volume (ml)
 Critically                                         161 (117-206)            166 (119-212)
 hypoperfused
 (Tmax>6s)       volume
 (ml)
 Time metrics
 Time      from     Last                            550 (311-920)            588 (345-928)
 Known        Well     to
 Randomization
 (minutes)
 Time from Arrival to                               16 (9-27)                16 (7-24)
 CT          Acquisition
 (minutes)
 Time from Arrival to                               26 (17-42)               25 (13-36)
 CTP         Acquisition
 (minutes)
 Additional characteristics
 IV       Thrombolytics                             33 (19.4%)               28 (17.0%)
 Administered
 Tenecteplase used                                  4 (12.5%)                1 (3.7%)
 General      Anesthesia                            100 (59.5%)
 Used
Footnotes:
CT – computed tomography
MRI – Magnetic Resonance Imaging
NIH Stroke Scale – a 42 point scoring system measuring neurological deficits, with higher score
representing more neurological deficits.
Tmax – Time to maximum intensity
CT Alberta Stroke Program Early CT Score (ASPECTS) – a 10 point ordinal scoring system
measuring areas of hypoattenuation due to ischemic changes in the middle cerebral artery territory
on non-contrast CT of brain, with a point deducted for each location demonstrating
hypoattenuation. Thus, lower scores represent worse the ischemic injury.
CTP/MRI core volume – volumetric estimates obtained from CT perfusion using relative Cerebral
Blood Flow <30% threshold/MR perfusion imaging using apparent diffusion coefficient <620
X10-6 mm/s2 threshold using automated RAPIDAi processing.


                                               35

```

### DOC-006 physical page 37

Source: joi240006supp5_prod_1708623115.01733.pdf#page=37

```text
CT hypodensity volume – volumetric estimates of observed hypodensity on non-contrast CT by
manual delineation of the region of interest by consensus from 3 expert readers using ITK-SNAP
Composite core volume – the larger of CTP/MRI core volume and CT hypodensity volume
estimates.




                                             36

```

### DOC-006 physical page 38

Source: joi240006supp5_prod_1708623115.01733.pdf#page=38

```text
eTable 2. Clinical and imaging outcomes in intention-to-treat population, stratified by
treatment.



                            Endovascular                    Medical Care Only
                            Thrombectomy             Plus
                            Medical Care
                            N=168                           N=168
 Distribution of Modified 4 (3-6)                           5 (4-6)
 Rankin Scale Scores at 90d
 Follow-up

 Functional    independence    34/168 (20.2%)               12/168 (7.1%)
 (mRS 0-2) at 90-day follow-
 up
 Independent     Ambulation    65/168 (38.7%)               31/168 (18.5%)
 (mRS 0-3) at 90-day follow-
 up
 Complete dependence or        76/168 (45.2%)               102/168 (60.7%)
 death (mRS 5-6) at 90d
 follow-up
 All-cause Mortality within    62/168 (36.9%)               70/168 (41.7%)
 90-day Follow-up Period

 Symptomatic Intracerebral 0/168 (0.0%)                     2/168 (1.2%)
 hemorrhage

 Parenchymal hemorrhage        4/168 (2.4%)                 3/168 (1.8%)

 Neurological Worsening        38/168 (22.6%)               27/168 (16.1%)

 Early          Neurological   19/165 (11.5%)               13/166 (7.8%)
 Improvement
 Follow-up infarct volume      170 (123-266)                168 (109-254)
 Infarct    growth      from   100 (42-177)                 90 (53-140)
 CTP/MRI core (ml)
 Infarct    growth      from   68 (22-128)                  66 (24-110)
 composite core (ml)
 Infarct growth from CT        87 (37-152)                  73 (31-135)
 hypodensity (ml)




                                              37

```

### DOC-006 physical page 39

Source: joi240006supp5_prod_1708623115.01733.pdf#page=39

```text
   eTable 3. Sensitivity analyses using site-investigator adjudicated ASPECTS.
                     mRS            shift
ASPECTS                                    mRS 0-2 (aRR mRS 0-3 (aRR             mRS 5-6 (aRR
                     (aGenOR        with
category                                   with 95% CI)          with 95% CI)    with 95% CI)
                     95% CI)
                     aGenOR:       1.70, aRR: 2.97, 95% CI: aRR: 2.23, 95%       aRR: 0.74, 95%
ASPECTS 3-5
                     95% CI: 1.33-2.17 1.60-5.49                 CI: 1.56-3.16   CI: 0.61-0.91
                     aGenOR:       1.91, aRR: 2.93, 95% CI: aRR: 1.91, 95%       aRR: 0.60, 95%
ASPECTS 6-10
                     95% CI: 1.04-3.54 0.42-20.47                CI: 0.75-4.90   CI: 0.35-1.02
                     aGenOR:       1.88, aRR: 7.82, 95% CI: aRR: 2.53, 95%       aRR: 0.66, 95%
ASPECTS 3
                     95% CI: 1.27-2.78 1.14-53.56                CI: 1.00-6.36   CI: 0.49-0.88
                     aGenOR:       1.51, aRR: 4.11, 95% CI: aRR: 2.44, 95%       aRR: 0.94, 95%
ASPECTS 4
                     95% CI: 0.92-2.48 1.40-12.09                CI: 1.39-4.29   CI: 0.62-1.44
                     aGenOR:       1.93, aRR: 2.08, 95% CI: aRR: 2.46, 95%       aRR: 0.71, 95%
ASPECTS 5
                     95% CI: 1.25-2.98 1.02-4.22                 CI: 1.56-3.90   CI: 0.50-1.01




                                               38

```

### DOC-006 physical page 40

Source: joi240006supp5_prod_1708623115.01733.pdf#page=40

```text
   eTable 4. Sensitivity analyses evaluating EVT treatment effect across CTP core strata (restricted
   to patients who received CT Perfusion only).
CTP core (rCBF mRS                   shift
                                            mRS 0-2 (aRR mRS 0-3 (aRR mRS 5-6 (aRR
<30%)      volume (aGenOR with 95%
                                            with 95% CI)       with 95% CI)        with 95% CI)
categories           CI)
                     aGenOR: 1.73, 95% aRR: 2.26, 95% aRR: 1.76, 95% aRR: 0.77, 95%
<70ml
                     CI: 1.20-2.48          CI: 1.15-4.43      CI: 1.24-2.50       CI: 0.53-1.11
                     aGenOR: 1.61, 95% aRR: 4.12, 95% aRR: 2.89, 95% aRR: 0.75, 95%
≥70ml
                     CI: 1.21-2.15          CI: 1.25-13.63     CI: 1.39-6.02       CI: 0.61-0.92
                     aGenOR: 1.86, 95% aRR: 2.75, 95% aRR: 2.05, 95% aRR: 0.68, 95%
<100ml
                     CI: 1.40-2.49          CI: 1.49-5.07      CI: 1.45-2.89       CI: 0.52-0.88
                     aGenOR: 1.44, 95% aRR: 3.36, 95% aRR: 3.04, 95% aRR: 0.82, 95%
≥100ml
                     CI: 1.00-2.06          CI: 0.52-21.64     CI: 0.95-9.73       CI: 0.64-1.04
                     aGenOR: 1.78, 95% aRR: 2.93, 95% aRR: 2.10, 95% aRR: 0.70, 95%
<150ml
                     CI: 1.39-2.30          CI: 1.62-5.30      CI: 1.51-2.92       CI: 0.56-0.87
                     aGenOR: 1.43, 95%                                             aRR: 0.83, 95%
≥150ml                                      N/A                N/A
                     CI: 0.80-2.54                                                 CI: 0.56-1.23
   N/A – could not be evaluated




                                                 39

```

### DOC-006 physical page 41

Source: joi240006supp5_prod_1708623115.01733.pdf#page=41

```text
eTable 5. Association of extent of ischemic injury on CT hypodensity and composite core
volumes and clinical outcomes within patients receiving EVT and MM.
                           Endovascular                   Medical Care Only Interaction
                           Thrombectomy (N=170)           (N=166)                  p-value
 mRS Distribution          Median (IQR): 4 (3-6)          Median (IQR): 5 (4-6)
 CT         hypodensity
                           aGenOR: 0.95, 95% CI: aGenOR: 0.98, 95% CI:
 volume(per        10ml                                                            0.14
                           0.93-0.98                      0.95-1.00
 increment)
 Composite          core
                           aGenOR: 0.92, 95% CI: aGenOR: 0.95, 95% CI:
 volume(per        10ml                                                            0.13
                           0.88-0.95                      0.92-0.98
 increment)
 mRS 0-2                   34/170 (20.0%)                 12/166 (7.2%)
 CT         hypodensity
                           aRR: 0.93, 95% CI: 0.89- aRR: 0.97, 95% CI:
 volume(per        10ml                                                            0.53
                           0.98                           0.87-1.09
 increment)
 Composite          core
                           aRR: 0.87, 95% CI: 0.82- aRR: 0.93, 95% CI:
 volume(per        10ml                                                            0.82
                           0.93                           0.83-1.05
 increment)
 mRS 0-3                   66/170 (38.8%)                 30/166 (18.1%)
 CT         hypodensity
                           aRR: 0.97, 95% CI: 0.91- aRR: 0.97, 95% CI:
 volume(per        10ml                                                            0.32
                           1.03                           0.91-1.03
 increment)
 Composite          core
                           aRR: 0.91, 95% CI: 0.85- aRR: 0.91, 95% CI:
 volume(per        10ml                                                            0.82
                           0.98                           0.85-0.98
 increment)
 mRS 5-6                   77/170 (45.3%)                 101/166 (60.8%)
 CT         hypodensity
                           aRR: 1.04, 95% CI: 1.02- aRR: 1.03, 95% CI:
 volume(per        10ml                                                            0.76
                           1.07                           1.01-1.05
 increment)
 Composite          core
                           aRR: 1.03, 95% CI: 1.00- aRR: 1.01, 95% CI:
 volume(per        10ml                                                            0.63
                           1.05                           1.00-1.03
 increment)
Footnotes:
CT- computed tomography
CTP – CT perfusion
MRI – Magnetic resonance imaging
ASPECTS – Alberta Stroke Program Early CT Score, a 10 point ordinal scoring system measuring
areas of hypoattenuation due to ischemic changes in the middle cerebral artery territory on non-
contrast CT of brain, with a point deducted for each location demonstrating hypoattenuation. Thus,
lower scores represent worse ischemic injury.
mRS – modified Rankin Scale score, a 7 level ordinal scoring system representing functional
status, with higher scores representing worse functional status (0 being without any deficits and 6
being dead).



                                                40

```

### DOC-006 physical page 42

Source: joi240006supp5_prod_1708623115.01733.pdf#page=42

```text
    eTable 6. Evaluation parameters for regression models for functional outcomes


Outcome     Modality            AIC                BIC           AUC (with 95% CI)        Preferred
                                                                                           modality
                                                                                          (based on
                                                                                             BIC
                                                                                         conventions)
Ordinal     ASPECTS        417.2590          447.8850           NA
 mRS
               CT          412.6195          443.2454           NA
           hypodensity
             volume
            CTP/MRI        403.2944          433.9203           NA
           core volume
            Composite      398.6922          429.3182           NA                       Preferred
           core volume
mRS 0-2     ASPECTS        256.9212          276.0068           0.7106 (0.6343-0.7870)
               CT          252.1431          271.2287           0.7224 (0.6481-0.7968)
           hypodensity
             volume
            CTP/MRI        239.4032          258.4887           0.7716 (0.7062-0.8370)
           core volume
            Composite      236.5431          255.6287           0.7783 (0.7103-0.8463) Preferred
           core volume
mRS 0-3     ASPECTS        358.6683          377.7538           0.7500 (0.6937-0.8062)
               CT          352.1023          371.1878           0.7522 (0.6965-0.8079)
           hypodensity
             volume
            CTP/MRI        329.0319          348.1174           0.7952 (0.7454-0.8450)
           core volume
            Composite      324.2519          343.3374           0.7977 (0.7472-0.8482) Preferred
           core volume


    Parameters for mRS distribution were calculated using ordinal logistic regression.
    Models with lower AIC and BIC values are considered more parsimonious
    Models with higher AUC values are considered to have better predictive value.
    N/A – not applicable




                                                   41

```

### DOC-006 physical page 43

Source: joi240006supp5_prod_1708623115.01733.pdf#page=43

```text
eTable 7. Association of presence or absence of mismatch profile based on composite core
volume with clinical outcomes within patients receiving EVT and MM (as-treated analysis).
 Presence       of mRS distribution
 mismatch
 profile(mismatc No mismatch (ref) 4 (3, 6)                  5 (4, 6)
 h volume≥10ml Mismatch                  4 (3, 6)            5 (4, 6)
 &       mismatch
 ratio≥1.2)      – Effect size with aGenOR:            0.77, aGenOR:        0.69, 0.73
 based          on   uncertainty         95%   CI: 0.50-1.17 95%   CI: 0.46-1.05
 Composite core estimates
 volume
                     Functional independence (mRS 0-2)
                   No mismatch (ref) 5/34 (14.7%)         3/40 (7.5%)
                   Mismatch            29/136 (21.3%)     9/126 (7.1%)
                   Effect size with aRR: 1.02, 95%        aRR: 0.63, 95% CI: 0.47
                   uncertainty      CI:    0.48-2.15,     0.20-1.94, aRD:-
                   estimates        aRD:-0.000, 95%       0.034, 95% CI: -
                                    CI: -0.155 to         0.123 to 0.056
                                    0.154
                   Independent ambulation (mRS 0-3)
                   No mismatch (ref) 13/34 (38.2%)        7/40 (17.5%)
                   Mismatch            53/136 (39.0%)     23/126 (18.3%)
                   Effect size with aRR: 0.77, 95%        aRR: 0.68, 95% CI: 0.79
                   uncertainty      CI:    0.48-1.26,     0.33-1.38, aRD:-
                   estimates        aRD:-0.097, 95%       0.064, 95% CI: -
                                    CI: -0.263 to         0.184 to 0.055
                                    0.070
                   Complete dependence or death (mRS 5-6)
                   No mismatch (ref) 12/34 (35.3%)        23/40 (57.5%)
                   Mismatch            65/136 (47.8%)     78/126 (61.9%)
                   Effect size with aRR: 1.31, 95%        aRR: 1.29, 95% CI: 0.83
                   uncertainty      CI:    0.80-2.15,     0.93-1.79,
                   estimates        aRD:0.127, 95%        aRD:0.168, 95%
                                    CI: -0.039 to         CI: 0.011 to 0.325
                                    0.293
 Presence      of mRS distribution
 mismatch
 profile(mismatc No mismatch (ref) 4 (3, 6)               5 (4, 6)
 h volume≥15ml Mismatch            4 (3, 6)               5 (4, 6)

                                           42

```

### DOC-006 physical page 44

Source: joi240006supp5_prod_1708623115.01733.pdf#page=44

```text
 &      mismatch     Effect size with aGenOR:     0.76, aGenOR:      0.73, 0.88
 ratio≥1.8)    –     uncertainty      95% CI: 0.50-1.18 95% CI: 0.53-1.02
 based        on     estimates
 Composite core
 volume              Functional independence (mRS 0-2)
                     No mismatch (ref) 21/112 (18.8%)           8/99 (8.1%)
                     Mismatch              13/58 (22.4%)        4/67 (6.0%)
                     Effect size with aRR: 0.60, 95%            aRR: 0.44, 95% CI: 0.76
                     uncertainty      CI:    0.30-1.21,         0.15-1.26, aRD:-
                     estimates        aRD:-0.099, 95%           0.061, 95% CI: -
                                      CI: -0.224 to             0.144 to 0.022
                                      0.027
                     Independent ambulation (mRS 0-3)
                     No mismatch (ref) 39/112 (34.8%)           18/99 (18.2%)
                     Mismatch              27/58 (46.6%)        12/67 (17.9%)
                     Effect size with aRR: 0.81, 95%            aRR: 0.66, 95% CI: 0.68
                     uncertainty      CI:    0.55-1.21,         0.38-1.14, aRD: -
                     estimates        aRD: -0.076, 95%          0.091, 95% CI: -
                                      CI: -0.228 to             0.202 to 0.020
                                      0.075
                     Complete dependence or death (mRS 5-6)
                     No mismatch (ref) 51/112 (45.5%)           60/99 (60.6%)
                     Mismatch              26/58 (44.8%)        41/67 (61.2%)
                     Effect size with aRR: 1.09, 95%            aRR: 1.21, 95% CI: 0.79
                     uncertainty      CI:    0.74-1.61,         0.94-1.56,
                     estimates        aRD:0.068, 95%            aRD:0.121, 95%
                                      CI: -0.088 to             CI: -0.017 to 0.260
                                      0.224
mRS – modified Rankin Scale score, a 7 level ordinal scoring system representing functional
status, with higher scores representing worse functional status (0 being without any deficits and 6
being dead).
Analyses are adjusted for age, NIHSS, time from last known well to randomization and CTP/MRI
core volume.




                                                43

```

### DOC-006 physical page 45

Source: joi240006supp5_prod_1708623115.01733.pdf#page=45

```text
eTable 8. Association of concordance/discordance between CT ASPECTS and ischemic core
estimates on CTP/MRI, within patients receiving EVT and MM.
                         Endovascular
                                                     Medical Care Only (N=156)
                         Thrombectomy (N=163)
                                                                                  Interaction
                         Median                      Median
                                    Effect      size             Effect size with p-value
 mRS Distribution        (IQR): 4                    (IQR): 5
                                    with 95% CI                  95% CI
                         (3-6)                       (4-6)
 Concordant imaging
 profiles
 (ASPECTS<6          & 5 (4-6)      Ref              5 (4-6)     Ref
 CTP/MRI
 core≥70ml)
 Discordant imaging
 profile             –                                           aGenOR: 1.50,
                                    aGenOR: 0.91
 1(ASPECTS<6         & 3 (2-6)                       4 (3-6)     95% CI: 0.94- 0.20
                                    (0.50, 1.65)
 CTP/MRI                                                         2.40
 core<70ml)
 Discordant imaging
                                                                 aGenOR: 0.65,
 profile – 2(ASPECTS                aGenOR: 1.01
                         5 (3.5-6)                   6 (6-6)     95% CI: 0.43- 0.26
 6-10 & CTP/MRI                     (0.53-1.92)
                                                                 0.99
 core≥70ml)
                         N (%):                      N      (%):
                                    Effect      size             Effect size with
 mRS 0-2                 32/163                      10/156
                                    with 95% CI                  95% CI
                         (19.6%)                     (6.4%)
 Concordant imaging
 profiles(ASPECTS<6 10/75
                                    Ref              3/82 (4%)   Ref
 &           CTP/MRI (13%)
 core≥70ml)
 Discordant imaging                 aRR:       0.51              aRR:        1.26
 profile             –              (0.16-1.56)                  (0.17-9.43)
                         21/76
 1(ASPECTS<6         &                               7/63 (11%)                   0.78
                         (28%)      aRD: -0.055 (-               aRD: 0.040 (-
 CTP/MRI
                                    0.201, 0.092)                0.059, 0.138)
 core<70ml)
 Discordant imaging                 aRR:       0.85
 profile – 2(ASPECTS                (0.12-5.79)
                         1/12 (8%)                   0/11 (0%)   N/A              N/A
 6-10 & CTP/MRI                     aRD: 0.010 (-
 core≥70ml)                         0.395, 0.415)
                         N (%):                      N      (%):
                                    Effect      size             Effect size with
 mRS 0-3                 62/163                      27/156
                                    with 95% CI                  95% CI
                         (38.0%)                     (17.3%)
 Concordant imaging
 profiles(ASPECTS<6 18/75
                                    Ref              8/82 (10%) Ref
 &           CTP/MRI (24%)
 core≥70ml)
 Discordant imaging 41/76           aRR:       0.86 19/63        aRR:        1.24
                                                                                  0.72
 profile             – (54%)        (0.43-1.71)      (30%)       (0.38-4.07)

                                           44

```

### DOC-006 physical page 46

Source: joi240006supp5_prod_1708623115.01733.pdf#page=46

```text
 1(ASPECTS<6           &
                                        aRD: 0.043 (-                   aRD: 0.060 (-
 CTP/MRI
                                        0.125, 0.211)                   0.075, 0.196)
 core<70ml)
 Discordant imaging                     aRR:       1.19
 profile – 2(ASPECTS 3/12               (0.43-3.28)
                                                           0/11 (0%)    N/A               N/A
 6-10 & CTP/MRI (25%)                   aRD: -0.065 (-
 core≥70ml)                             0.421, 0.291)
                           N (%):                          N      (%):
                                        Effect      size                Effect size with
 mRS 5-6                   75/163                          97/156
                                        with 95% CI                     95% CI
                           (46.0%)                         (62.2%)
 Concordant imaging
 profiles(ASPECTS<6 42/75                                  59/82
                                        Ref                             Ref
 &            CTP/MRI (56%)                                (72%)
 core≥70ml)
 Discordant imaging                     aRR:       0.92                 aRR:        0.69
 profile               –                (0.57-1.48)                     (0.49-0.97)
                           25/76                           28/63
 1(ASPECTS<6           &                                                                  0.14
                           (33%)        aRD: -0.077 (- (44%)            aRD: -0.076 (-
 CTP/MRI
                                        0.244, 0.091)                   0.248, 0.096)
 core<70ml)
 Discordant imaging                     aRR:       1.08                 aRR:        1.28
 profile – 2(ASPECTS 8/12               (0.69-1.68)        10/11        (1.01-1.63)
                                                                                          0.02
 6-10 & CTP/MRI (67%)                   aRD: 0.143 (- (91%)             aRD:       0.324
 core≥70ml)                             0.212, 0.498)                   (0.165, 0.483)
Footnotes:
CT- computed tomography
CTP – CT perfusion
MRI – Magnetic resonance imaging
ASPECTS – Alberta Stroke Program Early CT Score, a 10 point ordinal scoring system measuring
areas of hypoattenuation due to ischemic changes in the middle cerebral artery territory on non-
contrast CT of brain, with a point deducted for each location demonstrating hypoattenuation. Thus,
lower scores represent worse ischemic injury.
mRS – modified Rankin Scale score, a 7 level ordinal scoring system representing functional
status, with higher scores representing worse functional status (0 being without any deficits and 6
being dead).




                                                45

```

### DOC-006 physical page 47

Source: joi240006supp5_prod_1708623115.01733.pdf#page=47

```text
   eTable 9. Estimates of EVT treatment effect and corresponding interaction terms for concordant
   and discordant imaging profiles based on CTP/MRI core volume estimates
                            mRS distribution

                                                        mRS distribution(aGenOR Interaction
                           MM             EVT
                                                        with 95% CI)            p-value
Concordant        imaging
                                                    aGenOR: 1.60, 95% CI: 1.18 to
profiles(ASPECTS<6      & 5 (4, 6)       5 (4, 6)                                   Ref
                                                    2.18
CTP/MRI core≥70ml)
Discordant imaging profile
                                                    aGenOR: 1.87, 95% CI: 1.28 to
–     1(ASPECTS<6       & 4 (3, 6)       3 (2, 6)                                   0.66
                                                    2.74
CTP/MRI core<70ml)
Discordant imaging profile
                                                    aGenOR: 2.46, 95% CI: 1.14 to
– 2(ASPECTS 6-10 & 6 (6, 6)              5 (3.5, 6)                                 0.18
                                                    5.32
CTP/MRI core≥70ml)
                           Functional independence(mRS 0-2)
                                                                                    Interaction
                           MM            EVT        aRR with 95% CI
                                                                                    p-value
Concordant        imaging
                                         10/74      aRR: 4.62, 95% CI: 1.27 to
profiles(ASPECTS<6      & 3/83 (3.6%)                                               Ref
                                         (13.5%)    16.71
CTP/MRI core≥70ml)
Discordant imaging profile
                           7/63          21/76
–     1(ASPECTS<6       &                           aRR: 2.68, 95% CI: 1.25 to 5.76 0.56
                           (11.1%)       (27.6%)
CTP/MRI core<70ml)
Discordant imaging profile
– 2(ASPECTS 6-10 & 1/11 (9.1%) 0/12 (0%)            N/A                             N/A
CTP/MRI core≥70ml)
                           Independent ambulation(mRS 0-3)
                                                                                    Interaction
                           MM            EVT        aRR with 95% CI
                                                                                    p-value
Concordant        imaging
                                         18/74
profiles(ASPECTS<6      & 8/83 (9.6%)               aRR: 2.98, 95% CI: 1.44 to 6.17 Ref
                                         (24.3%)
CTP/MRI core≥70ml)
Discordant imaging profile               41/76
                           19/63
–     1(ASPECTS<6       &                (53.9%)    aRR: 1.90, 95% CI: 1.29 to 2.78 0.38
                           (30.2%)
CTP/MRI core<70ml)
Discordant imaging profile
                           3/11
– 2(ASPECTS 6-10 &                       0/12 (0%)  N/A                             N/A
                           (27.3%)
CTP/MRI core≥70ml)
                           Complete dependence or death (mRS 5-6)
                                                                                    Interaction
                           MM            EVT        aRR with 95% CI
                                                                                    p-value
Concordant        imaging
                           60/83         41/74
profiles(ASPECTS<6      &                           aRR: 0.76, 95% CI: 0.61 to 0.95 Ref
                           (72.3%)       (55.4%)
CTP/MRI core≥70ml)

                                                46

```

### DOC-006 physical page 48

Source: joi240006supp5_prod_1708623115.01733.pdf#page=48

```text
Discordant imaging profile
                             28/63     25/76
–    1(ASPECTS<6         &                       aRR: 0.72, 95% CI: 0.49 to 1.05 0.83
                             (44.4%)   (32.9%)
CTP/MRI core<70ml)
Discordant imaging profile
                             10/11     8/12
– 2(ASPECTS 6-10 &                               aRR: 0.59, 95% CI: 0.37 to 0.96 0.40
                             (90.9%)   (66.7%)
CTP/MRI core≥70ml)
    N/A – could not be evaluated




                                            47

```

### DOC-006 physical page 49

Source: joi240006supp5_prod_1708623115.01733.pdf#page=49

```text
eTable 10. Estimates of EVT treatment effect and corresponding interaction terms for
concordant and discordant imaging profiles based on composite core volume estimates
                           mRS distribution

                                                        mRS distribution(aGenOR with Interaction
                             MM             EVT
                                                        95% CI)                      p-value
Concordant        imaging
profiles(ASPECTS<6      & 5 (4, 6)        4 (3, 6)  aGenOR: 1.65, 95% CI: 1.26 to 2.16    Ref
composite core≥70ml)
Discordant imaging profile
–     1(ASPECTS<6       & 4.5 (3, 6)      3 (2, 6)  aGenOR: 1.80, 95% CI: 1.00 to 3.22    0.61
composite core<70ml)
Discordant imaging profile
– 2(ASPECTS 6-10 & 6 (6, 6)               5 (3, 6)  aGenOR: 2.66, 95% CI: 1.34 to 5.28    0.13
composite core≥70ml)
                           Functional independence(mRS 0-2)
                                                                                          Interaction
                             MM             EVT         aRR with 95% CI
                                                                                          p-value
Concordant        imaging
                                        18/112
profiles(ASPECTS<6      & 8/118 (6.8%)             aRR: 2.88, 95% CI: 1.34 to 6.20        Ref
                                        (16.1%)
composite core≥70ml)
Discordant imaging profile
                                        13/38
–     1(ASPECTS<6       & 2/28 (7.1%)              aRR: 3.71, 95% CI: 0.93 to 14.82       0.71
                                        (34.2%)
composite core<70ml)
Discordant imaging profile
– 2(ASPECTS 6-10 & 2/12 (16.7%) 0/14 (0%) N/A                                             N/A
composite core≥70ml)
                           Independent ambulation(mRS 0-3)
                                                                                          Interaction
                             MM             EVT         aRR with 95% CI
                                                                                          p-value
Concordant        imaging
                             19/118         35/112
profiles(ASPECTS<6      &                               aRR: 2.21, 95% CI: 1.41 to 3.48   Ref
                             (16.1%)        (31.3%)
composite core≥70ml)
Discordant imaging profile
                                            24/38
–     1(ASPECTS<6       &    8/28 (28.6%)               aRR: 1.83, 95% CI: 1.04 to 3.22   0.68
                                            (63.2%)
composite core<70ml)
Discordant imaging profile
– 2(ASPECTS 6-10 &           4/12 (33.3%)   0/14 (0%)   N/A                               N/A
composite core≥70ml)
                             Complete dependence or death (mRS 5-6)
                                                                                          Interaction
                             MM             EVT         aRR with 95% CI
                                                                                          p-value
Concordant       imaging
                         74/118             53/112
profiles(ASPECTS<6    &                                 aRR: 0.75, 95% CI: 0.60 to 0.92   Ref
                         (62.7%)            (47.3%)
composite core≥70ml)

                                             48

```

### DOC-006 physical page 50

Source: joi240006supp5_prod_1708623115.01733.pdf#page=50

```text
Discordant imaging profile
                             14/28     13/38
–    1(ASPECTS<6         &                       aRR: 0.90, 95% CI: 0.52 to 1.56   0.92
                             (50.0%)   (34.2%)
composite core<70ml)
Discordant imaging profile
                             11/12     9/14
– 2(ASPECTS 6-10 &                               aRR: 0.59, 95% CI: 0.39 to 0.88   0.38
                             (91.7%)   (64.3%)
composite core≥70ml)
 N/A – could not be evaluated




                                        49

```

### DOC-006 physical page 51

Source: joi240006supp5_prod_1708623115.01733.pdf#page=51

```text
eTable 11. Estimates of infarct growth from baseline in patients with MR DWI follow-up,
stratified based on treatment arm and reperfusion status.
 Factor                                MM                 mTICI 0-2a    mTICI 2b-3
 N                                     101                24            79
 Infarct growth from CTP/MRI
                                       95 (56, 135)       125 (76, 179) 68 (37, 142)
 core (ml), median (IQR)
 Infarct growth from composite
                                       63 (22, 102)       91 (71, 142)  45 (16, 90)
 core (ml), median (IQR)
 Infarct      growth     from    CT
                                       69 (31, 122)       107 (87, 152) 60 (24, 110)
 hypodensity (ml), median (IQR)




                                          50

```

### DOC-006 physical page 52

Source: joi240006supp5_prod_1708623115.01733.pdf#page=52

```text
eTable 12. Comparison of infarct growth in study population, based on functional outcomes.
                       Functionally Dependent Functionally                    p-value
                       (mRS 3-6)                   Independent (mRS 0-2)
                       N=290                       N=46
 Infarct growth from 102 (61-167)                  45 (32-88)                 <0.001
 CTP/MRI core (ml)
 Infarct growth from 77 (31-127)                   23.5 (11-48)               <0.001
 composite core (ml)
                       No           independent Independent Ambulation p-value
                       ambulation (mRS 4-6)        (mRS 0-3)
                       N=240                       N=96
 Infarct growth from 110.5 (65.5-174.5)            65.5 (32.5-100.5)          <0.001
 CTP/MRI core (ml)
 Infarct growth from 85.5 (36-144)                 31.5 (10-67)               <0.001
 composite core (ml)




                                            51

```

### DOC-006 physical page 53

Source: joi240006supp5_prod_1708623115.01733.pdf#page=53

```text
eTable 13. Characteristics of patients demonstrating significant(≥10ml) overestimation of
ischemic core as compared to follow-up infarct volume.
                                                                        Time from CTP
         CTP       or CT                Follow-up    Time from last acquisition to
 ID      MRI core hypodensity infarct                known well to CTP reperfusion/end
         volume(ml) volume(ml) volume(ml) acquisition(minutes) of                    the
                                                                        procedure(min)
 1       162            33              143          642                77
 2       140            0               90           289                N/A
 3       93             5               11           51                 125
N/A – not applicable (patient received medical management)




                                           52

```

## Administrative per-page map (B017)

DOC-002 is REPORT administrative content. Each of its30physical pages was opened in page-marked reusable text/layout. No result-relevant numeric, statistical, endpoint, intervention, population or prospective design relation appears. Names/institutional affiliations and form instructions are administrative observations. The printed form footer v02-22 and "Nof33" are form/page metadata, not participant counts. Pages18-25 repeat flattened name/institution data; pp26-27/29-30 contain institution-name continuations. Page28 contains no native text and no raster image according to direct pdfimages -f28 -l28 -list. This assessment is based on content inspection, not source naming.

| Source | Physical page | Inspected content | Quantitative applicability | Status |
|---|---:|---|---|---|
|DOC-002|1|SELECT2 Investigators group heading; Cleveland collaborator names/institutions|No applicable relationship|COMPLETE|
|DOC-002|2|Cleveland/Houston collaborator names/institutions|No applicable relationship|COMPLETE|
|DOC-002|3|Houston collaborator names/institutions|No applicable relationship|COMPLETE|
|DOC-002|4|Houston/Kansas collaborator names/institutions|No applicable relationship|COMPLETE|
|DOC-002|5|Kansas/Baptist/Cleveland Clinic names/institutions|No applicable relationship|COMPLETE|
|DOC-002|6|Cleveland Clinic/Rush/Austin/OhioHealth names/institutions|No applicable relationship|COMPLETE|
|DOC-002|7|OhioHealth/Kaiser/Abington names/institutions|No applicable relationship|COMPLETE|
|DOC-002|8|Abington/Valley Baptist/Ascension/Iowa names/institutions|No applicable relationship|COMPLETE|
|DOC-002|9|Iowa/Semmes Murphey/Thomas Jefferson names/institutions|No applicable relationship|COMPLETE|
|DOC-002|10|Thomas Jefferson/Pennsylvania names/institutions|No applicable relationship|COMPLETE|
|DOC-002|11|Pennsylvania names/institutions|No applicable relationship|COMPLETE|
|DOC-002|12|Pennsylvania/Corewell/Ascension names/institutions|No applicable relationship|COMPLETE|
|DOC-002|13|Ascension/Westchester/Toronto/Alberta/Melbourne names/institutions|No applicable relationship|COMPLETE|
|DOC-002|14|Melbourne/Adelaide/Liverpool names/institutions|No applicable relationship|COMPLETE|
|DOC-002|15|Liverpool/Christchurch/Vall d'Hebron names/institutions|No applicable relationship|COMPLETE|
|DOC-002|16|Vall d'Hebron/Barcelona/Germans Trias/Bellvitge names/institutions|No applicable relationship|COMPLETE|
|DOC-002|17|Bellvitge/Valladolid/Basel names/institutions|No applicable relationship|COMPLETE|
|DOC-002|18|Flattened repeated Cleveland/Houston name columns|No applicable relationship|COMPLETE|
|DOC-002|19|Flattened repeated Houston/Kansas/Baptist/Clinic/Rush columns|No applicable relationship|COMPLETE|
|DOC-002|20|Flattened repeated Rush/Austin/OhioHealth/Kaiser/Abington/Valley/Ascension columns|No applicable relationship|COMPLETE|
|DOC-002|21|Flattened repeated Ascension/Iowa/Semmes/Jefferson/Pennsylvania columns|No applicable relationship|COMPLETE|
|DOC-002|22|Flattened repeated Pennsylvania/Corewell/Ascension/Westchester columns|No applicable relationship|COMPLETE|
|DOC-002|23|Flattened repeated Westchester/Toronto/Alberta/Melbourne/Adelaide/Liverpool columns|No applicable relationship|COMPLETE|
|DOC-002|24|Flattened repeated Liverpool/Christchurch/Vall d'Hebron/Barcelona/Germans Trias columns|No applicable relationship|COMPLETE|
|DOC-002|25|Flattened repeated Germans Trias/Bellvitge/Valladolid/Basel columns|No applicable relationship|COMPLETE|
|DOC-002|26|Cleveland Medical Center and Houston institution-text continuations|No applicable relationship|COMPLETE|
|DOC-002|27|Houston institution-text continuation|No applicable relationship|COMPLETE|
|DOC-002|28|No native text or raster image; administrative continuation sheet|No applicable relationship|COMPLETE|
|DOC-002|29|Pennsylvania institution-text continuation|No applicable relationship|COMPLETE|
|DOC-002|30|Pennsylvania institution-text continuation|No applicable relationship|COMPLETE|
|DOC-007|1|Data-sharing statement, bibliographic date/DOI; Data available:No|No applicable result/design relationship|COMPLETE|

Exact source locator for each administrative row: joi240006supp1_prod_1708623114.97236.pdf#page=N where N is its printed Physical page column. DOC-007: joi240006supp6_prod_1708623115.02733.pdf#page=1. DOC-007 statement identifies Sarraj, Endovascular Thrombectomy for Large Ischemic Stroke Across Ischemic Injury and Penumbra Profiles, JAMA, published February07,2024, doi:10.1001/jama.2024.0572. The only data-availability response is "No"; it supplies no participant values or analysis definition.

## Handoff counts and limitations

Mapped52/52assigned physical pages: DOC-00621/21, DOC-00230/30, DOC-0071/1. DOC-006 all13eTables (19physical pages, including continuations) and6eFigure20panels (2pages) mapped; DOC-002/00731administrative pages explicitly not applicable.17local display/administrative group IDs B001-B017. Inferential scope by independently tracked pairs/tests is approximately180relationships:20eTable3estimate-CIs;22eTable4estimate-CIs;24eTable5(16estimate-CIs+8interactions);12eTable6model-comparison rows;36eTable7(28estimate-CIs+8last-column tests);30eTable8(24estimate-CIs+6interactions);16eTable9(10estimate-CIs+6interactions);16eTable10(same structure);4eTable12P-value comparisons. These are scope counts, not findings; table7last-column heading is not printed on assigned pages, so its8values require exact method-context matching. All displayed numeric/table cells are preserved; no inferential result is omitted to satisfy a scope bound.

No scientific coverage gap. Derivative limitations: legacy engine versions unrecorded, native figure digits crowded (resolved by visual reading), DOC-006Table7treatment/last-column headings absent on its assigned pages (preserved as label ambiguity), variable-specific denominators absent in some baseline rows (not invented), exact Table12test method absent from table pages (match assigned eMethods). There are no workbook formulas/cached values, direct Office sources or CSV result sources in this disjoint scope. No model/result diagnosis or candidate selection was performed.
