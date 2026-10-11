# DOC-003 protocol mapping: physical pages 1–32

Status: COMPLETE. Assigned scope: `joi190092supp2_prod.pdf`, physical PDF pages 1–32 only. Document role: PLAN throughout. Runtime ID: `01a12954-b115-74d2-9bde-a16449bb5a5f`. This artifact maps supplied evidence and makes no candidate diagnoses.

## Identity, evidence, and page convention

Page 1 identifies the bundle as original protocol, final protocol, and summary of changes. Pages 2–32 in this shard belong to the original FAST Manual of Operations and Procedures, header date September 4, 2012; the cover names the DSMC meeting September 11, 2012 and NEI U10 EY021125-01. Physical pages are used in all links. For physical pp.3–32 the printed MOP page is physical page minus 1; the cover has no printed MOP page.

Reusable input: `.ai_paper_validation/review_1_5_1/preprocessing/protocol_pp001_032_layout.txt`, source-linked Poppler layout text (legacy derivative; current matching tool version 26.01.0). Every assigned page's available text was read. Native-empty physical pp.15 and 19 were read from existing OCR and visually inspected in the corresponding numbered PNGs under `.ai_paper_validation/review_1_6_1/preprocessing/protocol_a/`. Physical p.18 flowchart was also visually inspected in `page-018.png` because its branches are not retained in layout extraction. Legacy raster/OCR engine versions are undocumented. No source/reused asset was modified, no fresh rendering/OCR was necessary, and no fresh-required unit was assigned. Compute device: CPU as recorded in tooling_record.md.

OCR transcription handling: p.15 OCR renders the success limits as `<` in places; the source-page image reads `≤ 7.5 mg/day` and `≤ 2 drops/day`. Table 2 source image reads anterior chamber cells `≤ 0.5+`, vitreous haze `≤ 0.5+`, and choroid/retina `No active lesions`. Physical p.19 OCR has incomplete/displaced numerals in the weekly dosing grid; the full visual grid is transcribed below. Those are derivative transcription limitations, not source findings.

Links are relative to this artifact's folder; canonical package source is four levels above it. Matching-main-paper keys below are semantic join keys for the coordinator, not assertions about unassigned main-paper content.

## Complete page coverage

| Physical page | Printed page | Content and mapping | Status |
|---:|---:|---|---|
| 1 | — | Bundle title/version identification; no result-relevant quantitative relationship. | COMPLETE |
| 2 | — | Original MOP cover, grant identifier and meeting date; no result-relevant quantitative relationship. | COMPLETE |
| 3 | 2 | Contents through follow-up specimens; locator only, no independent quantitative relationship. | COMPLETE |
| 4 | 3 | Contents: examinations, adverse events, management, analysis, QC; locator only. | COMPLETE |
| 5 | 4 | Contents: staff, organization, bibliography, appendices; locator only. | COMPLETE |
| 6 | 5 | Investigators/personnel/site listing; administrative only, no result-relevant quantitative relationship. | COMPLETE |
| 7 | 6 | DSMC member listing; administrative only, no stopping or analysis rule stated here. | COMPLETE |
| 8 | 7 | Background epidemiology/historical treatment discussion, not trial data or power inputs; explicit no-applicable trial relationship. | COMPLETE |
| 9 | 8 | Trial question, 216-patient design, 6/12-month treatment phases, Aims 1 and 2. | COMPLETE |
| 10 | 9 | Design, randomization, 108 per arm, primary and full secondary outcome hierarchy. | COMPLETE |
| 11 | 10 | Timeline/site goals and anatomical classification/eligibility population. | COMPLETE |
| 12 | 11 | Inclusion and active inflammation criteria, chronic-condition exceptions, baseline steroid requirements. | COMPLETE |
| 13 | 12 | Exclusion thresholds and randomization block sizes 4/6/8. | COMPLETE |
| 14 | 13 | Assignment access, masking of examiners versus unmasked patients/coordinators. | COMPLETE |
| 15 | 14 | Visual/OCR: masking-deviation retention, primary success composite and Table 2. | COMPLETE |
| 16 | 15 | Efficacy/intolerability/safety failure definitions and Table 3 laboratory AE thresholds. | COMPLETE |
| 17 | 16 | Dropout versus failure rules, missed visits, study-related versus unrelated death. | COMPLETE |
| 18 | 17 | Visual: full primary endpoint flowchart, rescue/continuation pathways and footnotes. | COMPLETE |
| 19 | 18 | Visual/OCR: Tables 4–5 introductory, maintenance, reduction doses and dose-use footnote. | COMPLETE |
| 20 | 19 | MTX and MMF timing, divided dose, tolerability escalation/failure and two reductions. | COMPLETE |
| 21 | 20 | Folic acid, dispensing, diary/pill-count adherence, missed-dose instructions. | COMPLETE |
| 22 | 21 | Oral prednisone starting dose, taper/hold and futility rules. | COMPLETE |
| 23 | 22 | Tables 6–7 taper schedules, reactivation thresholds and rescue instructions. | COMPLETE |
| 24 | 23 | Rescue continuation, supplements, topical taper Table 8, adjunctive treatment rules. | COMPLETE |
| 25 | 24 | Enrollment assignment/procedure sequence, QOL instruments by country and masking. | COMPLETE |
| 26 | 25 | Visit schedule, month-6 endpoint, laboratory allowance and window Table 9. | COMPLETE |
| 27 | 26 | Extended-phase Table 10, Phase II origin/follow-up and non-study failure timing. | COMPLETE |
| 28 | 27 | Full data-collection forms matrix (also labeled Table 9), treatment-failure footnote. | COMPLETE |
| 29 | 28 | Baseline-I eligibility/consent/assignment and data-collection requirements. | COMPLETE |
| 30 | 29 | Baseline specimen/forms and follow-up collection/QOL timing. | COMPLETE |
| 31 | 30 | Follow-up forms, baseline-II eligibility, SAE exit and non-study collection. | COMPLETE |
| 32 | 31 | Non-study collection, months 9/12 extension data, QOL instruments and administration. | COMPLETE |

Counts: 32/32 pages mapped; 32 reusable-backed, 0 fresh-required; 7 administrative/locator pages (pp.1–7), 1 background-only page (p.8), 24 trial-design/endpoint/intervention/measurement pages (pp.9–32). Scientific coverage gaps: none.

## Quantitative and statistical design relationships

### S-P001: randomized population, unit, and phases

[PDF p.9](../../../../joi190092supp2_prod.pdf#page=9), §1/1.2, and [p.10](../../../../joi190092supp2_prod.pdf#page=10), §2.1: patient-level randomized observer-masked comparative effectiveness trial of oral methotrexate (MTX) versus oral mycophenolate mofetil (MMF). Planned 216 patients, 108 per arm, needing corticosteroid-sparing therapy for noninfectious intermediate, posterior, or panuveitis. Initial treatment monthly follow-up for 6 months or until failure; success at month 6 continues the same drug another 6 months to month 12; initial failure switches to the alternate treatment and is followed another 6 months or until second-treatment failure. Aim 1 primary comparison is rate of successful corticosteroid-sparing inflammation control at 6 months after enrollment. Aim 2 evaluates switching after initial failure using the same primary and secondary outcomes, measured 6 months from failure/switch. Main-paper keys: randomized patient count, first-line success at month 6, second-line success, month-12 maintenance success.

### N-P001: enrollment goals and administrative timeline

[PDF p.11](../../../../joi190092supp2_prod.pdf#page=11), Table 1: planned enrollment Nov 2012–May 2015 (2.5 years); site goals Madurai 100, Coimbatore 71, San Francisco 15, Oregon 30; these sum to 216. Finish 6-month Phase-I follow-up +1-month visit window through Dec 2015; printed maximum 12-month +1-month visit-window follow-up line says through July 2015; lock/analyze/publish through Apr 2016. Pre-study Dec 2011–Sept 2012 and first DSMC/certification Sept–Nov 2012. These dates/site allocations are administrative, recorded for complete mapping, not power or decision inputs. Main-paper key: total planned randomized population; administrative dates are peripheral unless a relevant statistical rule depends on them.

### S-P002: planned outcome hierarchy (full list)

[PDF p.10](../../../../joi190092supp2_prod.pdf#page=10), §2.1, with [p.9](../../../../joi190092supp2_prod.pdf#page=9), §1.2. Primary: overall treatment success at 6 months, controlled ocular inflammation with oral prednisone ≤7.5 mg/day and topical prednisolone acetate 1% ≤2 drops/day. The following are all expressly under “Secondary outcomes,” without a separate key-secondary/tertiary/exploratory hierarchy on this page:

1. Specific Aim 2 rate of corticosteroid-sparing success 6 months after switching in patients failing during the first 6 months, same success definition as Aim 1.
2. Time to control of inflammation.
3. Time to treatment success.
4. Proportion achieving success at 5 months and sustaining for at least 28 days to month 6.
5. Proportion achieving success at month 12 in Phase I.
6. Phase-I (months 6–12) success with complete corticosteroid discontinuation.
7. Proportion achieving success at 6 months in Phase II.
8. Phase-II success with complete corticosteroid discontinuation.
9. Change in best spectacle-corrected visual acuity (BSCVA).
10. Presence of macular edema.
11. Change in macular thickness.
12. Change in vitreous haze assessed clinically by Davis scale.
13. Change in vitreous haze assessed photographically by NEI and Davis scales.
14. Efficacy within intermediate, posterior, and panuveitis subgroups.
15. Proportion discontinuing for intolerability.
16. Rate of adverse events.
17. Proportion discontinuing for serious adverse events.
18. Health- and vision-related quality of life.
19. Tabulation of occurrence of immunosuppressive dose reduction.
20. Efficacy in Vogt–Koyanagi–Harada (VKH) disease.

Main-paper keys: each named outcome's status, timing, instrument, anatomical subgroup and VKH subgroup. These are intended comparisons, not observed estimates. No subgroup model, interaction test, multiplicity rule, or confidence level is specified on this page.

### S-P003: anatomical population and inclusion requirements

[PDF p.11](../../../../joi190092supp2_prod.pdf#page=11), §2.3.1: historical intermediate, anterior-and-intermediate, posterior, or panuveitis at any time since diagnosis. SUN classification: anterior chamber / anterior uveitis; vitreous / intermediate; retina or choroid / posterior; anterior chamber plus vitreous plus retina/choroid / panuveitis. [p.12](../../../../joi190092supp2_prod.pdf#page=12) clarifies intermediate classification does not change with peripheral vascular sheathing or macular edema; panuveitis has no predominant site with inflammation in all three, and structural macular edema/neovascularization is not classificatory. More vitritis than iridocyclitis plus more anterior inflammation than intermediate is anterior-and-intermediate, not panuveitis.

Enrollment: historical noninfectious qualifying uveitis in ≥1 eye; active inflammation during last 90 days defined in ≥1 eye by ≥2+ anterior chamber cells, ≥2+ vitreous haze, or active retinal/choroidal lesions. At least one of: persistence after 4 weeks high-dose prednisone-equivalent 1 mg/kg; reduced inflammation then reactivation during steroid taper in prior 14 days; or chronic condition requiring steroid-sparing therapy. Additionally ≥1+ cells and/or ≥1+ haze and/or active lesions (bullous serous detachment qualifies) in ≥1 eye at enrollment, and willingness to begin prednisone 1 mg/kg or 60 mg/day, whichever less. Chronic SUN examples: Behcet with posterior segment involvement, multifocal choroiditis/panuveitis, serpiginous choroidopathy, birdshot; late-phase VKH with specified structural findings can qualify. Main-paper keys: eligibility/anatomic subgroup population; entry inflammation threshold versus success threshold.

### S-P004: exclusion and laboratory eligibility thresholds

[PDF p.13](../../../../joi190092supp2_prod.pdf#page=13), §2.3.3. Any exclusion suffices: infectious cause; inability to examine posterior segment in both eyes owing to media opacity/extensive synechiae; bilateral chronic hypotony IOP <5 mm Hg for >3 months; prior immunosuppressive drug other than prednisone; periocular/intravitreal steroid in past 2 months; fluocinolone implant in either eye <3 years; intraocular surgery <30 days; hand-motion-or-worse better-eye visual acuity; age <16; planning conception/pregnant/breastfeeding; unwilling to abstain from alcohol (2 drinks/month allowed); cancer; systemic autoimmune disease expected to dictate treatment. CBC within prior 14 days excludes WBC ≤2,500, platelets ≤75,000, or hemoglobin ≤10; ALT/AST ≥2× lab upper limit or creatinine ≥1.5 within 14 days excludes. Active TB/HIV/syphilis/hepatitis B or C excludes; specified TB/chest/syphilis/hepatitis tests within 60 days. Latent TB may enter. Printed CBC/creatinine eligibility bullet here does not give laboratory units; Table 3 later provides units for AE thresholds. Main-paper keys: trial eligibility, age, prior immunosuppression, treatment-related laboratory status.

### S-P005: randomization and masking

[PDF p.13](../../../../joi190092supp2_prod.pdf#page=13), §2.4: site-block randomization to equal numbers in each arm at each site, variable block sizes 4, 6, 8 with equal probability, sizes known only to biostatistician. [p.14](../../../../joi190092supp2_prod.pdf#page=14): coordinators know allocation but have no site randomization-list access; separate holders disclose assignment by ID. Patients/coordinators unmasked because appearance/schedules differ; examining ophthalmologists, visual-acuity examiners, OCT operators, fundus photographers/graders masked. [p.15](../../../../joi190092supp2_prod.pdf#page=15) visually: examiner unmasking creates protocol-deviation record, and those patients continue in trial. Main-paper keys: randomization strata/block design, observer masking, retention of participants with masking deviations.

### S-P006: primary success composite and measurement thresholds

[PDF p.15](../../../../joi190092supp2_prod.pdf#page=15), §2.5.1/Table 2 (source visual authority): controlled ocular inflammation **in both eyes** at month-6 visit with prednisone **≤7.5 mg/day**, prednisolone acetate 1% topical **≤2 drops/day**, and no tolerability/safety issue warranting discontinuation. Inflammation control jointly requires anterior chamber cells ≤0.5+ (SUN), vitreous haze ≤0.5+ (NEI), and no active choroidal/retinal lesions; lesions independent of macular edema. The star following both eyes is printed; no separate both-eye explanatory footnote is visible on this page. Main-paper key: binary overall treatment success composite, both-eye aggregation, month-6 index and steroid limits. The text says “rate”; no person-time rate formula is defined here.

### S-P007: failure, temporary cessation, dropout, and death status

[PDF p.15](../../../../joi190092supp2_prod.pdf#page=15), §2.5.2: discontinuation for efficacy/tolerability/safety may produce failure. [p.16](../../../../joi190092supp2_prod.pdf#page=16): efficacy failure for not reaching ≤7.5 mg/day prednisone and ≤2 prednisolone acetate 1% drops/day by 6 months, or clinician judging persistent nonresponse futile at any time. Intolerable side effects require failure if drug discontinued; reduction permitted. Serious AE exits immediately. Nonserious lab threshold abnormality stops medication immediately; up to 1 month to regain normal/eligible labs, then resume; otherwise failure and exit. Other nonserious AE may cause temporary cessation. Resulting uncontrolled inflammation or >7.5 mg/day at month 6 can still be efficacy failure.

[PDF p.17](../../../../joi190092supp2_prod.pdf#page=17): dropout only on declaring no further interest or death; a missed visit, nonserious AE, or medication discontinuation does not itself mean dropout; subsequent follow-up continues. Death related to drug counts as failure, unrelated death counts as dropout, medical-monitor discretion. Main-paper keys: primary failure components, failure versus missing/dropout analysis population, adverse-event cessation and treatment-related death. This shard provides operational missingness/status definitions, **not** an imputation rule or ITT model.

### N-P002: Table 3 nonserious and serious laboratory thresholds

[PDF p.16](../../../../joi190092supp2_prod.pdf#page=16). Leukocytes: nonserious >1,000 and <2,500/µL lasting <1 month; serious <2,500 lasting >1 month or ≤999/µL. Platelets: nonserious 20,000–75,000/µL lasting <1 month; serious ≤20,000/µL or <75,000 lasting >1 month. Hemoglobin: nonserious >6.4 to <10 g/dL; serious ≤6.4 g/dL. AST/ALT: nonserious 2–5× upper limit of normal, serious >5×. Creatinine: nonserious ≥1.5 to <2 mg/dL, serious ≥2 mg/dL. Preserve ranges/endpoints as printed. Main-paper keys: laboratory AE severity definitions and safety-related endpoint component.

### S-P008: primary endpoint flowchart

[PDF p.18](../../../../joi190092supp2_prod.pdf#page=18), §2.5.3, visual. Randomize MTX/MMF → monthly efficacy/tolerability/safety assessment plus adjusted steroid taper. At any time: serious AE → treatment failure; clinician futility → alternate antimetabolite/Phase II; intolerability → reduction I → if persists reduction II → if persists switch/Phase II, or resolution at either reduction → continue. Month 6: controlled inflammation with ≤7.5 mg prednisone and ≤2 drops/day → success → same-treatment Phase I months 6–12 → evaluate same thresholds at month 12, success/failure. No month-6 success → switch/Phase II → evaluate after 6 months on alternate therapy, success/failure. Footnotes: cells ≤0.5+, haze ≤0.5+, no active choroid/retina lesions; 2 drops/day = topical 1% prednisolone acetate or equivalent. Main-paper keys: same as S-P006/007, additionally second-treatment outcome time origin.

### N-P003 / S-P009: introductory, maintenance, and reduction regimen

[PDF p.19](../../../../joi190092supp2_prod.pdf#page=19), Tables 4–5, visual, and [p.20](../../../../joi190092supp2_prod.pdf#page=20), §3.1.1–3.1.2:

| Drug | Introductory weeks 1–2 | Maintenance after week 2 | Reduction I | Reduction II |
|---|---|---|---|---|
| MTX | 15 mg once weekly, day 1 only in grid | 25 mg once weekly, day 1 only | 20 mg once weekly | 15 mg once weekly |
| MMF | 500 mg BID every day 1–7 | 1.5 g BID every day 1–7 | 1 g BID every day 1–7 | 500 mg BID every day 1–7 |
| Folic acid, if MTX | 1 mg every day 1–7 | 1 mg every day 1–7 | 1 mg every day 1–7 | 1 mg every day 1–7 |

MTX weekly dose divided morning/evening; MMF twice daily advised empty stomach. Escalation at 2 weeks; cannot escalate for tolerability → failure, eligible to switch if Phase I, exit if Phase II. After escalation, severe side effects allow at most two specified reductions; persistent intolerance after second reduction can stop/switch. Table 5 footnote: reduce only for intolerance/safety; otherwise stay highest maintenance for follow-up. Stop early for efficacy/AE where specified. Main-paper keys: oral regimen, introductory exposure, assigned 25 mg/week MTX versus 3 g/day MMF maintenance, reduction-frequency outcome. Daily MMF totals of 1, 3, 2, 1 g/day are derived from BID for joining, not additional printed cells.

### N-P004: dispensing and adherence measurements

[PDF p.21](../../../../joi190092supp2_prod.pdf#page=21). Folic acid 1 mg/day to MTX arm. Introductory bottle 14 days at low dose; maintenance bottles 30 days, both dispensed at baseline; 30-day supply at monthly visits until month 5; switchers repeat Phase-I dispensing schedule; continuing-success patients get 120-day supply at month 6. Diaries of missed doses and pill counts measure adherence, recorded in log. MTX missed dose may be taken next day; otherwise wait following week. MMF missed dose: continue regular schedule. Main-paper keys: exposure/adherence and folic-acid cointervention; no percent-adherence formula or compliance cutoff supplied here.

### S-P010 / N-P005: oral prednisone background regimen and taper

[PDF p.22](../../../../joi190092supp2_prod.pdf#page=22), §3.2.1: prednisone unless contraindicated, equivalent alternative only for specific contraindication. Start min(1 mg/kg, 60 mg/day); hold initial dose 2–4 weeks, taper to and hold 7.5 mg/day for first 6 months. Printed paragraph says further reduction allowed “in Phase II, if patients continue on the same medication as Phase I”; preserve this source wording. Switchers starting Phase II follow initial Phase-I steroid protocol. Early uncontrolled inflammation in first 3 months does not necessarily imply failure because drug effect expected 6–8 weeks; clinician may declare futility before endpoint. Severe side effects allow steroid reduction.

[PDF p.23](../../../../joi190092supp2_prod.pdf#page=23), Table 6: doses mg/day 60 (2–4 weeks, decrement 10), 50 (1 week, 10), 40 (1, 5), 35 (1, 5), 30 (1, 5), 25 (1, 5), 20 (1, 2.5), 17.5 (1, 2.5), 15 (1, 2.5), 12.5 (1, 2.5), 10 (1, 2.5), 7.5 (hold). Footnote: no improvement after first 4 weeks → best judgment regarding supplemental pulse/injection/immunosuppressive treatment. Table 7 optional Phase-I months 6–12 taper: 7.5 (1 week minimum, decrement 2.5); <7.5 & ≥5 (2–4 weeks, decrement 1–2.5); <5 & ≥2.5 (2–4 weeks, decrement 1.5–2.5); <2.5 & ≥1 (2–4 weeks, decrement 1); 0. Main-paper keys: intervention steroid background/taper, primary success prednisone limit, complete corticosteroid discontinuation secondary outcome.

### S-P011: reactivation and rescue

[PDF p.23](../../../../joi190092supp2_prod.pdf#page=23) through [p.24](../../../../joi190092supp2_prod.pdf#page=24): mild flare is increase up to 1+ cells/haze; severe to ≥2+; lesion severity clinician discretion. Severe reactivation: prednisone up to 1 mg/kg; mild: up to twice flare dose until control, then retaper. Nonresponsive = no increased inflammation but no further improvement after 4 weeks; hold current prednisone another week, then may declare failure and switch. After suppression retaper Phase I; alternate-drug Phase II uses same taper; second failure exits. Main-paper keys: rescue corticosteroid use and treatment-failure rule.

### N-P006 / S-P012: topical steroid and adjunctive treatment

[PDF p.24](../../../../joi190092supp2_prod.pdf#page=24), §3.2.2–3.2.4: calcium 500 mg three times/day and vitamin D 400–800 IU/day recommended. Topical goal is off steroids but ≤2 times/day prednisolone acetate 1% or equivalent acceptable. Table 8: 8 times/day 1–2 weeks → 6/day 1 week → 4/day 1 → 3/day 1 → 2/day 1 → 1/day 1 → none. IOP-lowering and cycloplegic topicals allowed/recorded; injections, IV therapy, additional immunosuppressives, or surgery not allowed during study; if considered necessary, deviation form to monitor/PI. Main-paper keys: primary drops limit, complete steroid discontinuation outcome, randomized treatment cointerventions and rescue definitions.

### S-P013: scheduled time points, observation windows, and switch origin

[PDF p.26](../../../../joi190092supp2_prod.pdf#page=26), §4.1.1/Table 9: baseline day 1 = first treatment day and visit origin. Baseline data at baseline except labs within prior 14 days or same date. Minimum 2 weeks between visits. Phase I 0–6 months or Phase II: baseline BL-I(II), week 2 Wk2(II), month 1 through 5 M1–M5-I(II) each ±15 days, month 6 M6-I(II) −15 to +30 days. Header says “Window (weeks)” but entries give days; retain those printed units. Monthly dates calculated from baseline using average days/month. SAE failures exit rather than Aim 2. Success at month 6 extends another 6 months.

[PDF p.27](../../../../joi190092supp2_prod.pdf#page=27), Table 10 Phase-I months 6–12: month 6 ±15 days, month 9 ±15 days, month 12 −15 to +30 days, all from original baseline. Phase II after first-6-month efficacy/intolerability failure: alternate treatment for additional 6 months/until second failure; new day 1/visit origin = Baseline II first rescue-treatment day, possibly initial-failure date; dates may not change, minimum 2 weeks between visits. Non-study Phase-I failure: BL-II same visit or within 7 days, rescue as soon as BL-II collected; Phase-II failure exits. Main-paper keys: month-6/12 endpoint windows, switch follow-up origin, failure censoring/retention.

### S-P014: planned observation/forms matrix and endpoint measurements

[PDF p.28](../../../../joi190092supp2_prod.pdf#page=28), §4.2 forms matrix, printed label Table 9. Columns: Phase-I baseline; Phase-I months 1–5/9; Phase-I failure; Phase-I months 6/12; Phase-II baseline; Phase-II months 1–5; Phase-II failure; Phase-II month 6. Consent/eligibility at first baseline only; baseline history at both baselines. Clinical eye exam, visual acuity, OCT every listed column. Fundus photos at both baselines, both failure columns, Phase-I months 6/12 and Phase-II month 6. Lab form at baselines, Phase-I months 1–5/9 and 6/12, Phase-II months 1–5 and month 6 (no X in failure columns). QOL at baselines, failures, Phase-I months 6/12 and Phase-II month 6. Treatment assessment every column except Phase-I baseline. AE and dropout forms conditional at all subsequent columns; deviation conditional at every column. Footnote: treatment failure may be scheduled or non-study.

[PDF p.29](../../../../joi190092supp2_prod.pdf#page=29)–[p.31](../../../../joi190092supp2_prod.pdf#page=31): baseline procedures medical/treatment history, eye/VA/OCT/fundus/labs plus health/vision QOL; CBC differential neutrophil/lymphocyte percentages, AST/ALT/creatinine, pregnancy for non-postmenopausal females. Separate eye VA forms. Follow-up collection within windows; QOL at Phase-I failure or month 6 whichever first and month 12, Phase-II failure or month 6. Forms include medication adherence and treatment assessment. Phase-II eligibility after efficacy/tolerability failure; SAE exits. BL-II data can overlap failure-visit data. Main-paper keys: eye-level longitudinal measures and visit distributions, QOL availability at failure versus scheduled endpoint, adverse-event collection.

### S-P015: non-study visits and quality-of-life instrument populations

[PDF p.25](../../../../joi190092supp2_prod.pdf#page=25), study sequence, and [p.32](../../../../joi190092supp2_prod.pdf#page=32), §4.6/5.1: non-study visits require clinical exam/treatment-assessment forms only if failure; AE checklist/log when serious or nonserious AE; no required specimens. Continuing original-treatment Phase-I patients may be seen freely but study records only month 9, month 12, or non-study failure visits. QOL all patients at baseline and month 6/failure first; first-line sustained-success patients also month 12. Health QOL SF-36 all patients; vision QOL NEI-VFQ-25 US only, IND-VFQ India only. Self-completed where possible; visual/reading impairment permits coordinator oral administration using original questions. Main-paper keys: QOL instrument, country-specific measurement population, failure-dependent QOL time point and longitudinal collection.

## Explicit no-applicable relationships and scope limits

Pages 1–7 contain identity/contents/personnel rather than trial result values or independent analysis definitions. Page 8 has historical incidence >50/100,000 person-years, prevalence approximately 115/100,000, up to 10% US legal blindness/about 30,000 annual cases, and approximately half switching successfully in retrospective literature; these are background, not trial outcomes or stated power inputs, and do not establish a trial numerical relationship. References and addresses are not extracted as trial data.

There are no observed arm-specific trial results, confidence intervals, P values, test statistics, model coefficients, power assumptions, sample-size formula, interim decision boundaries, multiplicity adjustment, primary analysis model/covariates, ITT/per-protocol analysis definition, or statistical imputation rule specified on these 32 pages. Those absences are local mapping facts, not findings and not claims about the remainder of the package. Outcome hierarchy, operational failure/dropout, randomization and intervention details remain fully mapped above. No workbook formulas/cached values or Office units occur in assigned PDF scope.

All 32 assigned physical pages are complete. Remaining package pages belong to disjoint sibling shards. Limitations: legacy OCR/raster engine versions unrecorded; source visuals resolved p.15 inequalities and p.19 dosing numerals, and p.18 branch structure. Scientific gaps: none.
