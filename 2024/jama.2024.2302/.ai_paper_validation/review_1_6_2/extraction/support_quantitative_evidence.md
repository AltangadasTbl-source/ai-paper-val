# Support quantitative evidence — Workflow 1.6.2

Status: COMPLETE. Mapper: /root/support_mapper, fresh qc162_support_quantitative_mapper agent, gpt-6.1-sol / medium. Exact scope: DOC-002 physical PDF pages 1–25 (PLAN); DOC-003 pages 1–10 (PLAN); DOC-004 pages 1–8 (REPORT). All 43 pages mapped; no scientific coverage gaps. This is an extraction map, with no findings, screening, candidate selection or adjudication. Canonical numeric/statistical IDs are assigned downstream. No direct Office or CSV files exist, so workbook formulas, cached/displayed workbook values, worksheets, cells and structured-data row groups are not applicable.

Source paths from this file use three parent-directory levels to reach the package root. PDF page numbers below are physical pages. Main-paper matching keys identify outcome/model/population concepts for the coordinator; the main mapper owns main-paper locations.

## Extraction engines, assets and transcription differences

DOC-002 and DOC-003 use complete reusable native/layout extraction at `.ai_paper_validation/review_1_5_3/preprocessing/support_pdf_text/PDF-002_native.txt`, `PDF-002_layout.txt`, `PDF-003_native.txt` and `PDF-003_layout.txt`. Current curator confirmed byte identity to direct Poppler 26.01.0. The original engine version is unrecorded. Reusable DOC-002 images pages 6,7,11,12,13,14 were visually inspected, especially figures and inequality signs. DOC-004 pages 2–5 use readable 300-dpi reusable images under `.ai_paper_validation/document_outputs/jama-2024-2302-supp3-results/preprocessing/page_images/`; the historical renderer version is unrecorded. All four pages were visually read in full. Their native text is corrupted and is a locator only.

Fresh direct Poppler pdftotext 26.01.0 native and layout extraction was performed for DOC-004 pages 1,6,7,8. Fresh Poppler pdftoppm 26.01.0 CPU PNG rendering at 180 dpi covers those pages. Fresh Tesseract 5.5.0 CPU, English, psm 6 OCR covers all eight DOC-004 pages, using the reusable images for pages 2–5. All OCR is a locator; table values below come from visual reading. Fresh additional Poppler CPU rendering at 150 dpi covers DOC-002 pages 2,3,24 and DOC-003 pages 2,3,8,9, for visually checking symbols or the graphical harm index. Derivatives are all under `.ai_paper_validation/review_1_6_2/preprocessing/support_mapping/`, named `DOC-00N-pP.png`, `DOC-004-pP-native.txt`, `DOC-004-pP-layout.txt`, `DOC-004-pP-ocr.txt`. There are 11 fresh PNGs, eight OCR text derivatives, four native text derivatives and four layout derivatives. No fallback or GPU used.

Commands: `pdftotext -f P -l P SOURCE OUTPUT`; `pdftotext -layout -f P -l P SOURCE OUTPUT`; `pdftoppm -f P -l P -r 180 -singlefile -png SOURCE STEM` (150 dpi for plan symbol checks); `tesseract IMAGE STEM -l eng --psm 6`. No unapproved extraction script used.

Explicit derivative/source differences: protocol/SAP native extraction drops the underline in ≥ and ≤. Visually observed source readings take precedence: protocol pages 2,3,11,13 and SAP page 2 use ≥1 SAE; protocol pages 6,13 and SAP pages 3,8,9 use ≥28 weeks for the upper GA stratum; protocol page 13 and SAP page 9 use maternal education ≤12 years. The protocol page 13 rendering therefore supplies the original prior/moderator definitions below. Tesseract psm 6 misses numerous table cells in DOC-004 pages 2–6; none of those omissions limits the manually completed visual transcription. DOC-004 page 5 source CI is −16.5 to −2.0%, not a positive upper endpoint. No source reporting inference is drawn from derivative differences.

## Page-level coverage

| Source | Page | Role | Content opened and mapped | Status |
|---|---:|---|---|---|
| DOC-002 | 1 | PLAN | Protocol version 7, November 27, 2019; original November 5, 2012; registry and governance | COMPLETE |
| DOC-002 | 2 | PLAN | Abstract, primary/secondary hypotheses, recruitment target and outcome timing | COMPLETE |
| DOC-002 | 3 | PLAN | Primary/secondary aims; hospital-day hypotheses; BSIDIII follow-up | COMPLETE |
| DOC-002 | 4 | PLAN | Safety definition and anesthesia background; no additional trial result display | COMPLETE |
| DOC-002 | 5 | PLAN | Pilot trial Table 1 and footnotes; trial methods introduction | COMPLETE |
| DOC-002 | 6 | PLAN | Study-design Figure 1, randomization strata and recruitment assumptions | COMPLETE |
| DOC-002 | 7 | PLAN | Recruitment estimates and empty CONSORT template Figure 2 | COMPLETE |
| DOC-002 | 8 | PLAN | Screening capture, enrollment timing, start of administrative center table | COMPLETE |
| DOC-002 | 9 | PLAN | Administrative participating-site/affiliation/investigator table continuation; no trial-result quantities | COMPLETE |
| DOC-002 | 10 | PLAN | Site table end, study population, eligibility, intervention timing and crossover | COMPLETE |
| DOC-002 | 11 | PLAN | Ascertainment window, adjudication, harm classification and SAE Table 3 start | COMPLETE |
| DOC-002 | 12 | PLAN | SAE table end, developmental definitions and sample-size inputs | COMPLETE |
| DOC-002 | 13 | PLAN | Power Table 4, primary/secondary models, Bayesian final analysis, modifiers, prediction tool | COMPLETE |
| DOC-002 | 14 | PLAN | Prediction-tool continuation; amended interim/stopping rules; retention | COMPLETE |
| DOC-002 | 15 | PLAN | Recruitment fallback, interpretation/decision guidance, result dissemination timing | COMPLETE |
| DOC-002 | 16 | PLAN | Governance, administrative investigator Table 5, monitoring and publication schedule | COMPLETE |
| DOC-002 | 17 | PLAN | IRB and June 3, 2013 pilot start; eligible nonrandomized data not sought in pilot | COMPLETE |
| DOC-002 | 18 | PLAN | Bibliography 1–24; not applicable for independent trial-result relationships | COMPLETE |
| DOC-002 | 19 | PLAN | Bibliography 25–46; not applicable for independent trial-result relationships | COMPLETE |
| DOC-002 | 20 | PLAN | Bibliography 47–63; not applicable for independent trial-result relationships | COMPLETE |
| DOC-002 | 21 | PLAN | Bibliography 64–87; not applicable for independent trial-result relationships | COMPLETE |
| DOC-002 | 22 | PLAN | Bibliography 88–105; not applicable for independent trial-result relationships | COMPLETE |
| DOC-002 | 23 | PLAN | Appendix SAE definitions, including anesthesia and incarceration | COMPLETE |
| DOC-002 | 24 | PLAN | Appendix definitions/footnotes and graphical NCC MERP harm index | COMPLETE |
| DOC-002 | 25 | PLAN | Version 2–7 dated amendment history, including interim/final-analysis amendment | COMPLETE |
| DOC-003 | 1 | PLAN | SAP version 1 dated October 31, 2022; references protocol version 7 | COMPLETE |
| DOC-003 | 2 | PLAN | SAP scope, objectives, primary hypothesis | COMPLETE |
| DOC-003 | 3 | PLAN | Hypotheses and clarification, allocation, interventions, twins, sample size start | COMPLETE |
| DOC-003 | 4 | PLAN | Power, interim/final timing, Bayesian priority, reporting definitions | COMPLETE |
| DOC-003 | 5 | PLAN | Protocol deviations, mITT/PP definitions, eligibility and flow | COMPLETE |
| DOC-003 | 6 | PLAN | Withdrawal/missing follow-up, baseline variables and summary statistics | COMPLETE |
| DOC-003 | 7 | PLAN | Complete outcome list, SAE table, analysis families | COMPLETE |
| DOC-003 | 8 | PLAN | Covariates, effect measures, priors, MCMC and model checks | COMPLETE |
| DOC-003 | 9 | PLAN | Sensitivity, modifiers, additional exploratory subgroups and continuous GA | COMPLETE |
| DOC-003 | 10 | PLAN | Ad hoc analyses, no imputation, software and bibliography; references not applicable as independent results | COMPLETE |
| DOC-004 | 1 | REPORT | Results supplement title/index/date; no numeric trial results | COMPLETE |
| DOC-004 | 2 | REPORT | eTable 1, ineligible infants, first 17 reasons | COMPLETE |
| DOC-004 | 3 | REPORT | eTable 1 continuation, five reasons plus parent/physician/other refusals | COMPLETE |
| DOC-004 | 4 | REPORT | eTable 1 end, remaining four other reasons | COMPLETE |
| DOC-004 | 5 | REPORT | All eTable 2 results and model/center footnote | COMPLETE |
| DOC-004 | 6 | REPORT | Entire eTable 3: three denominators and all 39 center rows | COMPLETE |
| DOC-004 | 7 | REPORT | Acknowledgments: DSMC and trial personnel; no applicable trial-result quantity | COMPLETE |
| DOC-004 | 8 | REPORT | Acknowledgments continuation; no applicable trial-result quantity | COMPLETE |

## DOC-002 protocol relationships

### SUP-P01 — Identity, intervention and endpoint hierarchy

[Protocol page 1](../../../joi240020supp1_prod_1710443209.74911.pdf#page=1) identifies version 7, November 27, 2019, original November 5, 2012, NCT01678638. This supplied PDF is the amended version, not a separate copy of the original protocol. The original specification can be identified only where the document explicitly describes amendment history; do not reconstruct absent earlier versions.

[Pages 2–3](../../../joi240020supp1_prod_1710443209.74911.pdf#page=2): primary proportion of infants with ≥1 SAE during enrollment to 10 months after enrollment, independently adjudicated masked to treatment assignment. Late versus early hypothesis: 10-percentage-point absolute reduction, RR=0.66, number needed to harm=10 for early repair. Assumed 60% randomization, 615 randomized over 2.5 years. Secondary hospital days enrollment to 10 months, median reduction 3 days; page 3 prints early 18 versus late 15 days. Secondary BSIDIII Cognitive Composite difference 0.4 SD = 6 points, at 22–26 months corrected age / approximately 2 years, first 200 infants in selected centers. Corrected age formula: chronological age minus weeks/months premature. Main matching keys: primary any-SAE at 10 months; total hospital days at 10 months; neurodevelopment outcome status/time; intervention early/late timing.

[Page 10](../../../joi240020supp1_prod_1710443209.74911.pdf#page=10): early repair promptly after randomization, before NICU discharge, approximately 38 weeks PMA. Late goal 5 months after discharge, approximately 55–60 weeks PMA. The title specifies after discharge and beyond 55 weeks PMA. Operation/admission determined clinically under pragmatic practice; laparoscopic/open and general/regional/other anesthesia permitted (page 11). Infants may cross intended timing for clinical reasons, including late-group incarceration or early-group condition changes; recorded as outcomes. No fixed drug dose or anesthesia duration is assigned.

Eligibility on page 10: GA <37 weeks 0 days, NICU/other nursery at participating site, surgeon-diagnosed IH, parental consent and provider willingness. Exclusions: factor affecting timing, other operation with IH as secondary procedure affecting timing, known major congenital/chromosomal anomaly, inability to return or monitor as outpatient.

### SUP-P02 — Randomization/measurement design

[Page 6](../../../joi240020supp1_prod_1710443209.74911.pdf#page=6), Figure 1: identify/consent approximately 2 weeks before expected discharge; randomization approximately 36 weeks PMA, study time zero; early approximately 38 weeks PMA; late approximately 55 weeks PMA; prospective SAE measurement until 10 months, approximately 30 sites, N=586; BSIDIII at 22–26 months corrected age. Text: site and GA <28 versus ≥28 weeks stratification. Figure 2 on page 7 is an empty CONSORT template: no observed numerical counts, no trial result to extract. Fields are assessed, excluded (eligibility, declined, other), randomized, allocated/received/did not receive, lost/discontinued, analyzed/excluded, symmetrically for arms.

[Page 8](../../../joi240020supp1_prod_1710443209.74911.pdf#page=8): randomize when approximately 2 weeks from anticipated discharge via REDCap site/GA strata. Screening records count, GA, sex, eligible/ineligible reasons, eligible not enrolled and planned treatment. Center-table footnote uses PHIS 2011 data for 13/19 (68%) sites. Pages 8–10 are administrative site/affiliation/personnel listings without numeric per-site recruitment cells; page 9 has no additional result-relevant quantity.

[Page 11](../../../joi240020supp1_prod_1710443209.74911.pdf#page=11): end ascertainment 10 months after randomization; earliest discharge assumed 35 weeks PMA, latest repair example 65 weeks PMA gives 1.5–2 postoperative months. Equal enrollment-to-end window; early longer postoperative, late longer preoperative. Surveillance ceases at 10 months, then developmental tracking. SAE reliability checked for random 10%; perioperative direct interview through 24 hours after surgery plus records. Adjudication masked; highest harm among ≥1 SAE classified E–I, secondary outcome. Main matching keys: ascertainment window, any-SAE definition, blinded adjudication and safety-event labels.

### SUP-P03 — Sample size/power/analysis

[Page 12](../../../joi240020supp1_prod_1710443209.74911.pdf#page=12): early SAE 30%, late 20%, 293/group, total 586 assessed, 80% power, two-sided alpha .05, absolute difference 10%. Assumes 20 eligible infants/site/year, 60% randomization, 95% follow-up, 19 sites, 615 randomizations over approximately 2.5 years. Hospital days: 98% power for median difference 3 days, lognormal early median 8 / mean 18 versus late median 5 / mean 13. BSIDIII 0.4 SD / 6 points with 200 assessed at 22–26 months.

[Page 13](../../../joi240020supp1_prod_1710443209.74911.pdf#page=13), Table 4:

| Infants/group | Power: 10% SAE-rate difference | Power: 3-day median hospital-day difference |
|---:|---:|---:|
| 293 | 80% | 98% |
| 250 | 73% | 97% |
| 200 | 64% | 92% |
| 150 | 52% | 81% |

Intent-to-treat. General linear mixed models for primary/secondary outcomes; inspect symmetry/unimodality, group variance and residuals, adjust key demographics if necessary (sex/ethnicity examples). Primary ≥1 SAE: binomial GLMM log link, treatment and GA <28 / ≥28 covariates, center random effect. Hospital days: lognormal same covariates/random center. BSIDIII: linear mixed model same specification. Primary absolute RD and 95% CI; continuous absolute differences and 95% CI; similar models other secondary outcomes. Additional final Bayesian primary/major-secondary analysis, neutral prior centered RR 1.0 with 95% CrI 0.33–3.0. Main matching keys: sample-size assumptions; analysis population; logistic versus log-binomial model; negative-binomial versus lognormal hospital model; adjustment/site clustering; Bayesian primary/frequentist secondary hierarchy and priors.

### SUP-P04 — Subgroups, prediction and stopping

[Page 13](../../../joi240020supp1_prod_1710443209.74911.pdf#page=13): Bayesian hierarchical treatment interactions for primary SAE, hospital days, BSIDIII. Prespecified moderators GA <28/≥28, BPD yes/no, maternal education ≤12 years yes/no, prenatal care yes/no, IH difficult to reduce yes/no. Dixon–Simon shrinkage toward overall mean. Main-effect priors neutral N(0,1000), SD parameters Uniform(0,1000); neutral/skeptical interaction priors. Point effects/95% CrI and probability benefit/harm. Similar sex and race/ethnicity subgroup analyses required for NIH Phase III. Prediction tool uses covariates with large probability of interaction, predicts SAE, hospital days and Bayley <70 impairment; validate posterior predictive checks and ROC where appropriate. Secondary/novel analyses, not primary.

[Page 14](../../../joi240020supp1_prod_1710443209.74911.pdf#page=14): amended interim planned December 2019, approximately 200 infants with 10-month data. Bayesian harm outcomes death and prolonged stay >30 days after surgery; benefit primary proportion with an SAE and secondary total hospital length of stay. Neutral priors imply 50:50 prior chance either strategy better. Safety stopping probability of increased harm >90% in either arm for death/prolonged stay. Efficacy stopping probability of decreased SAEs >95% in either arm. DSMB considers these data. No numerical multiplicity adjustment or noninferiority/equivalence margin is specified in this protocol.

[Page 15](../../../joi240020supp1_prod_1710443209.74911.pdf#page=15): conclusion based on total evidence if under-enrolled; could recommend late repair for significant total-hospital-day reduction if SAE and Bayley do not favor early, particularly posterior probability >80% that SAE lower and Bayley higher with late. Main matching keys: interim decision/stopping, final benefit probability, subgroup model/estimates and secondary outcome reporting.

### SUP-P05 — Developmental scale and SAE definitions

[Page 12](../../../joi240020supp1_prod_1710443209.74911.pdf#page=12): first 200 developmental assessments, 8 NRN centers and other capable sites; participation voluntary. BSIDIII Cognitive, Language, Motor age-standardized composites mean100 SD15; <70 (>2 SD below mean) significant delay. Severe delay precluding testing assigned 54. Cerebral palsy abnormal tone in ≥1 extremity with abnormal movement/posture; GMFCS severity. Follow-up surgery history collected from end SAE ascertainment through 22–26-month visit. These are planned outcomes, not current observed neurodevelopment results.

[Pages 11–12](../../../joi240020supp1_prod_1710443209.74911.pdf#page=11), Table 3: cardiorespiratory/anesthesia events death, ECMO, cardiac arrest, CPR, hypotension with vasoactive drugs, apnea with increased respiratory support, local anesthetic toxicity (e.g. seizure), prolonged intubation/ventilation >48 hours after operation, unplanned reintubation, intraoperative unplanned extubation. IH/surgery events incarceration, strangulation, recurrence, reoperation IH/initial operation, adjacent-structure injury, deep wound disruption, deep SSI, other SAE requiring intervention to prevent/address harm.

[Page 23](../../../joi240020supp1_prod_1710443209.74911.pdf#page=23), appendix definitions:

| SAE | Recorded definition |
|---|---|
| Death | Any cause, records/vital statistics/maternal report, verified where possible |
| ECMO | Cannulation for any cause regardless of successful initiation |
| Cardiac arrest | Heart rate zero in records |
| CPR | Ventilation and cardiac massage with/without medication/intervention |
| Apnea with respiratory support | ≥1 episode, increased FiO2 AND increased respiratory support: bag/mask, bag/tube, initiation/increase mechanical ventilation |
| Hypotension with vasoactive drugs | Vasopressor/other vasoactive treatment for pressure below age-specific standards; fluid bolus alone or unchanged preoperative drug dose excluded |
| Persistent bradycardia receiving treatment | Low heart rate with pharmacologic intervention |
| Local anesthetic toxicity | Presumed local-anesthetic event from anesthesia/PACU/PICU/NICU records |
| Regional anesthetic toxicity | Presumed regional-anesthetic-medication event from corresponding records |
| Prolonged intubation | Intubated/mechanically ventilated >48 h after procedure completion, only if not mechanically ventilated before surgery |
| Unplanned reintubation | Reintubation not planned |
| Intraoperative unplanned extubation | Inadvertent during surgery, record reintubation yes/no |
| IH incarceration | Nonreducible AND urgent repair; OR narcotic/sedation to reduce; OR surgical-team reduction documented as incarceration |
| IH strangulation | Incarcerated contents ischemic/damaged at operation |
| IH recurrence | Return during study by examination/imaging AND recorded |
| Reoperation | Second/subsequent IH operation same or contralateral side OR operation due to IH-repair SAE |

[Page 24](../../../joi240020supp1_prod_1710443209.74911.pdf#page=24), appendix continuation:

| SAE | Recorded definition |
|---|---|
| Adjacent structure/organ injury | Believed surgical injury at original operation or identified subsequently |
| Deep wound disruption | Wound dehiscence including deep external oblique fascia |
| Deep surgical-site infection | Within 30 days, deep fascia/muscle AND ≥1 of purulent deep drainage, incision dehisces/opened deliberately, documented abscess, or attending/surgeon records deep SSI |
| Other SAE requiring intervention | Recorded SAE requiring specific intervention to prevent/address harm |

Footnotes: all ascertainment enrollment through 10 months. PACU means postanesthesia/recovery unit. Prolonged intubation, unplanned reintubation, wound disruption, SSI definitions adapted from ACS Pediatric NSQIP. The appendix separately includes persistent bradycardia and regional toxicity, beyond the condensed Table 3 labels; all are retained for outcome-component matching.

NCC MERP graphical scale on page 24: A potential circumstances; B event does not reach patient; C reaches without harm; D reaches and monitoring/intervention to preclude harm; E temporary harm requiring intervention; F temporary harm requiring initial/prolonged hospitalization; G permanent harm; H intervention necessary to sustain life; I contributes to death. The trial uses E–I. Legend: no event/no harm/harm/death classes. Definitions: harm physical/emotional/psychological function or structure impairment/pain; monitoring observing relevant physiological/psychological signs; intervention may change therapy/active treatment; life-sustaining intervention includes cardiovascular/respiratory support. No numerical risk estimate is printed in the scale.

### SUP-P06 — Amendments and administrative quantities

[Page 25](../../../joi240020supp1_prod_1710443209.74911.pdf#page=25): version2 May15,2013 adds selected capable sites to developmental aim and administrative updates; version3 Dec30,2014 coordinator update; version4 Feb13,2015 opens developmental follow-up outside NRN, first200 eligible participants at capable NRN/non-NRN sites; version5 Apr27,2016 PMA terminology, investigators, recruitment/eligibility clarification; version6 Dec20,2018 adjudicators/sites and deletes Appendix I because MOP holds database fields; version7 Nov27,2019 slower enrollment replaces TWO interim safety analyses at33% and66% enrollment with safety/efficacy analysis December2019 approximately200 infants, adds final Bayesian primary/major-secondary alongside planned frequentist analysis. No earlier full plan version or MOP supplied.

Other opened administrative content: page2 success ≥60% randomization; page6 recruitment >60% expected; page7 >500 eligible/year and 2.5-year enrollment; page15 recruitment 240 randomized/year in first two years and120 in first half third year, sites below40% randomization at6 months reviewed, prepared to continue to target; page16 8 organizational components,20–30 sites,30-day data checks/query resolution, DSMC twice/year, primary paper end year3/developmental end year5; page17 IRB and June3,2013 pilot at Vanderbilt plus5 sites, no eligible nonrandomized data sought in pilot. These are administrative/prospective quantities, not current outcome estimates. References pages18–22 were opened completely; citation years, volume/pages and titles do not create current trial-result relationships.

### SUP-P07 — Pilot Table 1 (background, not HIP trial results)

[Page 5](../../../joi240020supp1_prod_1710443209.74911.pdf#page=5): 39/50 eligible randomized (78%) at4 sites, early19 late20; late goal55 weeks PMA. Printed title describes reduction with early repair. Values are mean/range except the explicitly median/range postoperative stay.

| Row | Early N19 | Late N20 |
|---|---|---|
| Estimated GA, weeks | 28.9 (24–32) | 28.4 (25–34) |
| Birth weight, g | 959 (520–1550) | 958 (500–2710) |
| PMA operation, weeks | 38.4 (34–49) | 48.6 (33–61) |
| Weight operation, kg | 2.55 (1.8–4.0) | 3.9 (1.3–8.9) |
| Postoperative apnea/bradycardia | 4/19 (21%) | 0 |
| Reintubation/failure extubation | 5/19 (26%) | 2/12 (17%) |
| Any anesthetic event | 9/19 (47%) | 2/12 (17%) |
| Postoperative stay, median(range), days | 8 (1–206) | 1 (0–30) |
| Medical attention for IH reduction | 0 | 6/12 (50%) |
| Death after IH repair | 0 | 0 |

Footnotes:8 late infants without repair during study,2 died from prematurity after discharge,5 lost,1 no identifiable IH;6 repaired before55 weeks (range33–49),4 incarceration,2 parental/provider preference. Pilot did not measure all study-period hospital days. These background results may inform assumptions but do not match current HIP outcome cells.

## DOC-003 SAP relationships

### SUP-S01 — Date, clarified hypotheses and allocation

[SAP page 1](../../../joi240020supp2_prod_1710443209.75411.pdf#page=1): version1 October31,2022; protocol version7 Nov27,2019 original Nov5,2012. Page2 scope: planned analyses included in future manuscripts as deemed necessary by HIP subcommittee; additional exploratory analyses permitted. No independent earlier SAP supplied.

[Pages 2–3](../../../joi240020supp2_prod_1710443209.75411.pdf#page=2): primary ≥1 SAE from enrollment through10 months, late >55 weeks PMA and after discharge, approximately5 months after discharge, early before discharge approximately38 weeks. Assumed SAE30% early20% late, absolute10% reduction. Secondary total hospital days median reduction3 days, early8 late5. Explicit clarification identifies protocol page3 medians18/15 and points to page12 as intended8/5; retain this disclosed clarification. BSIDIII cognitive0.4SD=6 points,22–26 months corrected age. Baseline modifiers expected.

Page3: parallel-group1:1; early after medical optimization before discharge; late >55weeks and after discharge; center/GA (<28 / ≥28weeks) strata, permuted variable blocks, REDCap24/7. Multiple gestation first twin randomized; sibling assigned same arm. Main keys: intervention timing, allocation unit/strata/sibling dependence, hospital hypothesis disclosure.

### SUP-S02 — Sample, interim and inference hierarchy

[Pages 3–4](../../../joi240020supp2_prod_1710443209.75411.pdf#page=4):293/group586 assessed,80% power, two-sided alpha.05,95% follow-up,615 planned randomized. Hospital98% power, lognormal early median8 mean18; late median5 mean13. BSIDIII0.4SD6points with200. One formal primary-endpoint interim when200 randomized infants have10-month data; protocol14 stopping guidelines. Planned final586 outcomes. Retrospective note: enrollment stopped April2021 after interim97% probability of decreased SAE late, crossing95% efficacy threshold; interim primarily Bayesian.

Page4: complementary frequentist/Bayesian primary and important secondary death, total hospital days, BSIDIII. Bayesian primary, frequentist secondary; designation before final analyses. Frequentist treatment RR/RD/group mean differences and95% CI. Bayesian posterior medians,95% CrI, probability any benefit/harm and clinically important effect. Main keys: interim97%/95%, Bayesian priority, models/priors, credible versus confidence intervals and probabilistic direction.

### SUP-S03 — Analysis populations, follow-up and endpoints

[Page 5](../../../joi240020supp2_prod_1710443209.75411.pdf#page=5): mITT all randomized with ascertained primary outcome; PP received randomized intervention plus determined primary outcome. Deviation counts/infants per arm summarized (timing not followed, other intervention, ineligible, no consent, strata issue, other). Eligibility matches protocol (<37weeks0days etc.). CONSORT includes eligible randomized/unrandomized, received/did not receive, lost/discontinued, analyzed/excluded with reasons.

[Page 6](../../../joi240020supp2_prod_1710443209.75411.pdf#page=6): no data after withdrawal, earlier data retained; missing follow-up can occur between discharge/late repair/10-month call and between10months and developmental22–26months. Baseline infant age(GA/PMA/chronological),sex,race,Hispanic,birthweight g,singleton,inborn,1/5-minute Apgar,previous operations,apnea/bradycardia,mechanical ventilation >24h,IVH grade/laterality,ROP/RDS/BPD/CLD/cardiac/NEC/SIP,reducibility,caffeine/steroids,respiratory status; maternal age,race,ethnicity,marital/education/parity,multiple birth,prenatal care,insurance,residence ZIP. Categorical n/%; continuous normal mean/SD/range, skewed median/IQR/range.

[Page 7](../../../joi240020supp2_prod_1710443209.75411.pdf#page=7): primary ANY SAE randomization through10months, protocol definitions and masked adjudication. Table3 complete list mirrors protocol condensed table (10 cardiorespiratory/anesthesia and8 surgery/IH rows). Secondary highest harm for ≥1SAE NCC MERP; total hospital days=randomization-to-discharge days+readmission days+postsurgical days; prolonged stay >30days postsurgery; NICU stay; postsurgery stay; IH repair occurred; BSIDIII cognitive; overall AE(any). Main keys: primary/composite and secondary statuses, hospital summation/window, prolonged-stay definition, neurodevelopment deferred result, highest harm, repair occurrence.

### SUP-S04 — Models, effect measures, priors and computation

[Pages 7–8](../../../joi240020supp2_prod_1710443209.75411.pdf#page=8): all outcomes by group; categorical n/%, counts median/IQR/mean/SD, continuous normal mean/SD. Same multilevel model for Bayesian/frequentist outcome. Binary logistic; ordinal proportional-odds logistic; count negative-binomial; continuous normal. Each random site intercept plus GA<28/≥28 covariate. Binary RR and RD calculated from logistic; count RR; ordinal OR; continuous mean group difference.95% CI/CrI. Probability any effect and at least3%/5% SAE risk reduction;10% hypothesized reduction. R, Stan via rstanarm/brms;3chains/model,≥5000 burn-in and≥50000 additional iterations/chain.

Categorical treatment neutral OR1, stated95%CrI0.2–4, Normal(mean0,SD0.7) on logOR. Count treatment neutral RR1,95%CrI0.33–3.3. Intercept Normal(0,SD10),GA Normal(0,SD1),site SD halfNormal(0,SD1). Continuous standardized outcome: treatment Normal(0,SD2),intercept Normal(0,SD10),GA Normal(0,SD3),siteSD halfNormal(0,SD2). No fully specified count-treatment log-scale SD supplied beyond the RR prior range. Residual plots for frequentist; three-chain trace,Geweke,Gelman/Rubin convergence; posterior predictive1000trials, average probabilities/counts/means by treatment and GA; observed values expected within simulation cloud. Main keys: effect-measure identity, statistical family/covariates/clustering, treatment prior range/scale, iterations and convergence.

### SUP-S05 — Sensitivity/subgroups/association/missing data

[SAP page 9](../../../joi240020supp2_prod_1710443209.75411.pdf#page=9): sensitivity covariate adjustment if important baseline imbalance, primary only, mITT, already adjusts GA/site. PP primary analysis in addition to mITT. Exploratory primary subgroup mITT; hierarchical interactions treatment with GA<28/≥28,BPD,maternal education≤12years,prenatal care,IH difficult to reduce; primary plus hospital days and BSIDIII. Main-effect priors as primary; interaction Normal(0,SD0.6); subgroup point effects,95%CrI,benefit/harm probability. Similar sex/race/ethnicity. Two additional exploratory moderators explicitly absent from trial protocol: laparoscopic/open repair and distance from home to facility. Continuous GA association: splines/polynomials assess linear/nonlinear best fit, all other primary model details retained, then interaction GA term/treatment via subgroup methods.

[Page 10](../../../joi240020supp2_prod_1710443209.75411.pdf#page=10): additional ad hoc analyses must be clearly labeled as motivated by planned analyses; no imputation for missing data; R. References opened, no independent result display. No prespecified multiple-imputation sensitivity or adjusted multiplicity decision is stated. Main keys: mITT/PP, conditional imbalance sensitivity, continuous GA interaction, specified subgroup results, missing outcomes exclusion versus imputation, ad hoc labels.

## DOC-004 reported quantitative relationships

### SUP-R01 — eTable 1 enrollment reasons

[Page 2](../../../joi240020supp3_prod_1710443209.75411.pdf#page=2), continued [page 3](../../../joi240020supp3_prod_1710443209.75411.pdf#page=3): site-level ineligibility because associated factor affecting timing. Unit is infants; no percentage printed and no section total printed. All22 rows:

| Reason | Infants | PDF page |
|---|---:|---:|
| Incarceration during NICU | 10 | 2 |
| Multiple prior abdominal operations | 5 | 2 |
| Severe respiratory disease | 5 | 2 |
| Hernia contains ovary, preferred early | 4 | 2 |
| Severe cardiac disease | 4 | 2 |
| Airway anomaly requiring operation | 2 | 2 |
| Research contact too close to discharge for enrollment | 2 | 2 |
| Associated undescended testicle | 2 | 2 |
| Viral upper respiratory infection | 2 | 2 |
| COVID restriction, no elective operation | 2 | 2 |
| Transfer closer to home/nonparticipating hospital | 2 | 2 |
| Anticoagulant therapy | 1 | 2 |
| Very large hernia, surgeon preferred early | 1 | 2 |
| Infant too small | 1 | 2 |
| Unsure hydrocele or hernia, prefer wait | 1 | 2 |
| Coordinate ophthalmology procedure | 1 | 2 |
| Coordinate neurosurgery/shunt | 1 | 2 |
| Planning G-tube | 1 | 3 |
| Severe pulmonary hypertension | 1 | 3 |
| Unexplained thrombocytopenia | 1 | 3 |
| Await stopping steroids | 1 | 3 |
| Hernia thought to cause feeding intolerance | 1 | 3 |

[Page 3](../../../joi240020supp3_prod_1710443209.75411.pdf#page=3): parent/guardian refusal n613: early280,late196,physician decide71,no reason66. Physician refusal n37: early14,late14,no reason9. Other reasons eligible not consented n16: non-English/only English forms4,COVID4,custody3 (page3); incarceration concerns NICU2,insurance1,medically unstable1,transfer cardiac surgery1 ([page4](../../../joi240020supp3_prod_1710443209.75411.pdf#page=4)). These14 refusal/other rows plus22 ineligibility rows are complete. Main matching key: participant-flow exclusions/refusal categories and enrollment population; do not use these as outcome denominators.

### SUP-R02 — eTable 2 frequentist analyses and complete footnote

[Page 5](../../../joi240020supp3_prod_1710443209.75411.pdf#page=5). Headings: Early Repair n159; Late Repair n149; risk difference (95% confidence interval), P value; relative risk (95% confidence interval), P value. These are frequentist confidence intervals, not Bayesian credible intervals. Late versus early direction is negative RD / RR below1 for lower late risk.

| Status/outcome | Early | Late | RD (95% CI) | RD P | RR (95% CI) | RR P |
|---|---|---|---|---|---|---|
| Primary: Infant had ≥1 SAE | 44 (28%) | 27 (18%) | −9.0% (−16.5%, −2.0%) | .01 | 0.65 (0.46–0.92) | .01 |
| Secondary: Total hospital days during study period, median(IQR) | 19.0 (9.8,35) | 16.0 (7,38) | blank | blank | 0.91 (0.74–1.12) | .36 |

Footnote begins logistic mixed-effect primary model, negative-binomial mixed hospital-days model; all models GA-group covariate and center random intercept. Then explicitly excepts frequentist primary analysis: generalized estimating equation logistic, exchangeable center correlation, due to mixed-model nonconvergence. Bayesian and frequentist otherwise same models. Participating centers large pediatric facilities with surgical services/almost all university affiliated; surgeons pediatric general/thoracic, no pediatric urologists; surgeon counts varied but no numeric range; site infant counts below. All footnote statements retained; no diagnosis assigned. Main keys: primary any-SAE10-month mITT counts44/159 and27/149; primary Bayesian comparator/RR/RD; total hospital days median/IQR/RR; GEE versus mixed model disclosure.

### SUP-R03 — eTable 3 full enrollment by center

[Page 6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6): column unit No.(%); Early Repair n172; Late Repair n166; Overall N338. These are randomized enrollment denominators, distinct from eTable2 analyzed159/149. All39 center rows follow; percentages are printed, not recalculated.

| Center | Early n(%) | Late n(%) | Overall n(%) |
|---|---|---|---|
| Akron Children's Hospital | 2 (1.2%) | 2 (1.2%) | 4 (1.2%) |
| Albany Medical Center | 4 (2.3%) | 2 (1.2%) | 6 (1.8%) |
| All Children's Johns Hopkins | 3 (1.7%) | 4 (2.4%) | 7 (2.1%) |
| Amplatz Children's Hospital | 5 (2.9%) | 5 (3.0%) | 10 (3.0%) |
| Arkansas Children's Hospital | 16 (9.3%) | 17 (10%) | 33 (9.8%) |
| Cardinal Glennon/SLU | 7 (4.1%) | 5 (3.0%) | 12 (3.6%) |
| Children's Hospital of Alabama | 3 (1.7%) | 3 (1.8%) | 6 (1.8%) |
| Children's Hospital of Wisconsin | 2 (1.2%) | 0 (0%) | 2 (0.6%) |
| Children's Memorial Hermann Hospital | 7 (4.1%) | 8 (4.8%) | 15 (4.4%) |
| Cincinnati Children's Hospital | 2 (1.2%) | 0 (0%) | 2 (0.6%) |
| Cohen Children's Medical Center | 0 (0%) | 1 (0.6%) | 1 (0.3%) |
| Columbia University Medical Center | 5 (2.9%) | 5 (3.0%) | 10 (3.0%) |
| Connecticut Children's Medical Center | 4 (2.3%) | 4 (2.4%) | 8 (2.4%) |
| Dartmouth-Hitchcock Medical Center | 2 (1.2%) | 0 (0%) | 2 (0.6%) |
| Dayton Children's Hospital | 5 (2.9%) | 5 (3.0%) | 10 (3.0%) |
| Duke Children's Hospital | 11 (6.4%) | 9 (5.4%) | 20 (5.9%) |
| Erlanger/UT Chattanooga | 11 (6.4%) | 10 (6.0%) | 21 (6.2%) |
| Le Bonheur Children's Hospital | 8 (4.7%) | 8 (4.8%) | 16 (4.7%) |
| Medical University of South Carolina Children's Hospital | 7 (4.1%) | 7 (4.2%) | 14 (4.1%) |
| Nationwide Children's Hospital | 9 (5.2%) | 8 (4.8%) | 17 (5.0%) |
| Naval Medical Center San Diego | 1 (0.6%) | 2 (1.2%) | 3 (0.9%) |
| Penn State Milton S. Hershey MC | 0 (0%) | 1 (0.6%) | 1 (0.3%) |
| Rady Children's Hospital/UCSD | 1 (0.6%) | 1 (0.6%) | 2 (0.6%) |
| Seattle Children's Hospital | 1 (0.6%) | 0 (0%) | 1 (0.3%) |
| Shands Hospital for Children | 1 (0.6%) | 1 (0.6%) | 2 (0.6%) |
| Southern California Permanente Group | 6 (3.5%) | 7 (4.2%) | 13 (3.8%) |
| St. Louis Children's Hospital | 2 (1.2%) | 1 (0.6%) | 3 (0.9%) |
| Texas Children's Hospital | 3 (1.7%) | 1 (0.6%) | 4 (1.2%) |
| Tufts University | 1 (0.6%) | 2 (1.2%) | 3 (0.9%) |
| UCLA | 1 (0.6%) | 2 (1.2%) | 3 (0.9%) |
| UCLA-Harbor | 1 (0.6%) | 2 (1.2%) | 3 (0.9%) |
| University of Iowa Children's Hospital | 11 (6.4%) | 13 (7.8%) | 24 (7.1%) |
| University of Nebraska Medical Center | 0 (0%) | 1 (0.6%) | 1 (0.3%) |
| University of Virginia | 3 (1.7%) | 4 (2.4%) | 7 (2.1%) |
| Utah/Primary Children's | 3 (1.7%) | 3 (1.8%) | 6 (1.8%) |
| Valley Children's | 4 (2.3%) | 2 (1.2%) | 6 (1.8%) |
| Vanderbilt Children's Hospital | 11 (6.4%) | 13 (7.8%) | 24 (7.1%) |
| Women & Children's Hospital of Buffalo | 6 (3.5%) | 6 (3.6%) | 12 (3.6%) |
| Women & Infants Hospital Rhode Island | 3 (1.7%) | 1 (0.6%) | 4 (1.2%) |

Main matching key: randomized totals172/166/338, center/random-effect structure and participant-flow population. No other footnote or total row on page6.

## Completeness and matching handoff

There are15 locally grouped relationship records:7 protocol,5 SAP and3 results-supplement groups. Display row counts: protocol pilot10 plus power4; results enrollment reasons36, primary/major-secondary results2 and centers39, total91 numeric display rows (77 in DOC-004,14 protocol). SAE definitions and statistical specifications are additionally complete and are not counted as observed numeric display rows. No source-backed sensitivity or subgroup result table occurs in the results supplement; their specifications are mapped from protocol/SAP, with main reported counterparts to be located by main mapper. No workbook formula/cached value or CSV unit applies.

Every source page was opened through complete native/layout text, usable page image, or fresh source rendering. No blank/administrative/reference unit was inferred solely from absence of reusable extraction. DOC-004 fresh-required pages1,6,7,8 received native AND layout plus render/visual inspection; OCR locators were added. All scientific coverage gaps closed. Remaining derivative limitations: corrupted supplement glyphs and dropped plan inequality underlines, resolved by visual readings documented above; historical renderer versions unrecorded. No old candidates, conclusions or reports read, no web used, and sources/reused assets unchanged.
