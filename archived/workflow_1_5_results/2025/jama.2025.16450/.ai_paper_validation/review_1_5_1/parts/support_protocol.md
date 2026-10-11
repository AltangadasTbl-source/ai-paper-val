# DOC-002 Protocol Quantitative Evidence Map — support-001

## Scope and extraction record

- **Direct source:** `joi250072supp1_prod_1761000786.68881.pdf` (DOC-002), PDF pages 1-35, read only.
- **Fresh extraction:** native and layout `pdftotext` outputs for pp. 1-35 are retained at `preprocessing/protocol/DOC-002-native-pp001-035.txt` and `preprocessing/protocol/DOC-002-layout-pp001-035.txt`. The source embeds a nonstandard character map, so the text is materially unusable for exact transcription. CPU page rendering was therefore used; readable rendered pages are in `preprocessing/protocol/images/` and targeted direct visual checks were performed for the protocol synopsis, background results, analytical plan, sample-size table, and monitoring plan. Interrupted OCR outputs are not used as evidence.
- **Source role:** protocol/administrative support, not a trial-results report. It specifies the planned population, intervention, outcome definitions, estimands, models, sample-size assumptions, and monitoring boundaries. Values describing prior external studies are retained as protocol-background values and are not matched to the trial result unless explicitly labelled below.
- **Main-paper matching convention:** `BiB | randomized infant | budesonide+surfactant versus surfactant alone | physiologic BPD or death by 36 weeks PMA`; match only after checking final population, treatment-received versus intention-to-treat set, endpoint definition, timing, and model.

## Numeric/reporting relationships

| ID | Direct protocol evidence | Relationship / definition / match key |
|---|---|---|
| PRO-N001 | p. 4, Synopsis | Planned allocation is 1:1, stratified by NICU and gestational age `<26` versus `>=26` weeks. Match key: randomization design/strata. |
| PRO-N002 | p. 4, Synopsis | Eligible newborn: 22 0/7 to 27 6/7 weeks' gestation; birth weight 401-1000 g; clinical decision to give surfactant. Enrollment must allow first study dose by <48 h postnatal age. Match key: eligibility population/timing. |
| PRO-N003 | p. 4, Synopsis | Intervention planned as poractant alfa 1.25 mL/kg mixed with 0.25 mg/kg budesonide; control poractant alfa 1.25 mL/kg for first dose; maximum two study-drug doses, with second-dose criteria at 12-36 h. Match key: intervention dose/unit/maximum. |
| PRO-N004 | p. 4, Synopsis | Primary outcome is physiologic BPD or death by 36 weeks postmenstrual age (PMA). The synopsis also names physiologic BPD, BPD severity, ventilation days, post-randomization extubation, repeat-dose count, and respiratory outcomes as secondary outcomes. Match key: primary endpoint/timepoint. |
| PRO-N005 | pp. 4-5, Synopsis definitions | Physiologic BPD is defined by the NICHD 2001 physiologic definition, including room-air challenge for infants receiving respiratory support at 36 0/7 weeks PMA; death is death before the 36-week assessment; severe BPD is defined by the NICHD/Rome 2001 definition. Match key: endpoint definition. |
| PRO-N006 | pp. 4-5, Synopsis | Safety outcomes include events in the first week after last study drug, events within 28 days after last study drug, and growth parameters at 36 weeks PMA (weight, length, head circumference). Match key: safety-window/measurement-unit. |
| PRO-N007 | p. 5, Objectives and outcomes | Primary clinical question and all planned efficacy analyses use the comparison budesonide+surfactant versus surfactant alone and the incidence of physiologic BPD or death at 36 weeks PMA; analyses are intention-to-treat unless otherwise specified. Match key: primary contrast/analysis population. |
| PRO-N008 | p. 5, Secondary outcomes | Secondary items include death and physiologic BPD at 36 weeks PMA, a four-level BPD severity scale, grade 3 BPD, postnatal steroid use from day 7 through 36 weeks PMA, severe neurodevelopmental impairment (NDI) at 22-26 months corrected age, death by 22-26 months corrected age, and severe NDI or death. Match keys: outcome/timepoint/scale. |
| PRO-N009 | p. 5, Background | Protocol-background burden values: approximately 0.65 million neonatal deaths worldwide, 35% of all neonatal deaths; approximately 1 in 10 US births preterm; US societal economic burden at least $26.2 billion in 2005. These are not trial result values. |
| PRO-N010 | pp. 9-10, prior human studies | Protocol-background pilot trial: 116 VLBW infants (2004-2006); BPD/death at 36 weeks was 19/60 treatment versus 34/56 control; blood samples were obtained in 22 infants (10 treated, 12 control); peak budesonide at about 30 minutes, 16alpha-hydroxyprednisolone peak at 2 h, terminal half-life 4.13 h, 0-8 h budesonide AUC 115.73 ng/mL, assumed blood volume 80 mL/kg, total blood amount 9258 ng, approximately 4% of the instilled dose. Do not cross-match this external study to BiB final results. |
| PRO-N011 | p. 10, prior human study | Protocol-background later trial: 256 VLBW infants, 2009-2013; intervention n=131 and control n=134; BPD/death 55/131 (42%) versus 89/134 (66%); one-dose use 64.9% versus 36.6%; follow-up comparison 85 versus 87 infants; NDI 30.6% versus 39.1%. This is external evidence, not a BiB result. |
| PRO-N012 | p. 10, prior human-study estimates | The same external comparison reports RR 0.58 (95% CI 0.44-0.77), NNT 4.1 (95% CI 2.8-7.8), and `p<0.001` for fewer surfactant doses. The P-value is a nonzero threshold display; no display-zero issue. |
| PRO-N013 | p. 10, prior meta-analysis | Protocol-background meta-analysis reports 43% BPD-risk reduction, RR 0.57 (95% CI 0.43-0.76), NNT=5; mortality OR 0.61 (95% CI 0.34-1.04); composite death/BPD RR 0.60 (95% CI 0.49-0.74), NNT=3. External evidence only. |
| PRO-N014 | p. 14, dose-ranging background | Protocol-background dose-ranging study: doses 0.025-0.1 mg/kg; 24 infants; mean gestational age 25.0 weeks, mean birth weight 743 g, mean enrollment age 6 days; half-life 3.4 h; mean 65% decrease in tracheal-aspirate cytokines; average four doses (range 2-5); 0.1-mg/kg arm total 0.4 mg/kg. External evidence only. |
| PRO-N015 | p. 14, safety background | Early-dexamethasone historical comparison: 0.15 mg/kg/day for 3 days starting within 24 h, taper over 7 days, total 0.89 mg/kg; SIP 13% versus 4% placebo, p=0.02. Protocol states SIP incidence in extremely preterm infants as 4% (range 0%-8% across centers). External safety context only. |
| PRO-N016 | p. 25, analytical plan | The planned primary analysis is a proportion comparison for death or physiologic BPD by 36 weeks PMA, adjusted for study site/NICU and dichotomous gestational-age stratum. Match key: adjusted primary estimand. |
| PRO-N017 | pp. 25-26, sample-size assumptions | Target primary-event assumptions: in GDB, 19% do not survive to 36 weeks PMA and 42% of survivors have physiologic BPD, combined approximately 53%; target extremely preterm subgroup assumes 24% nonsurvival and 45% BPD among survivors, combined approximately 58%. Expected absolute-risk reduction is about 10 percentage points, 58% to 48%; protocol says an earlier external result had 24% absolute reduction. Match key: planning baseline/effect assumptions, not final estimates. |
| PRO-N018 | p. 26, Table 5 | Sample size per treatment arm: 80% power 406 at overall alpha 0.05/final alpha 0.044 and 593 at overall alpha 0.01/final alpha 0.009; 90% power 539 and 753; 95% power 664 and 900. Table is a planning calculation. |
| PRO-N019 | p. 26, sample-size text | At 90% power and overall two-sided type-I error 0.05 (final 0.044), estimate is 539/arm (1078 total); simulation recommends 550/group (1100 total); allowing approximately 5% attrition, planned enrollment is 1160 infants, equally allocated. Match key: planned N versus actual randomized/analysed N. |
| PRO-N020 | p. 26, available population/recruitment | Planning flow: about 2000 extremely preterm infants/year, 10% excluded, about 70% of remaining 1800 need surfactant (=1260 eligible/year), 33% consent, about 415 enrolled/year; 1160/415=2.8 years. Planned development 1 year + enrollment 2.8 years + follow-up 2 years, total five to six years. Planning only. |
| PRO-N021 | p. 27, adverse-event monitoring | AEs are monitored from treatment initiation through 168 h (7 days) after completing study drug. Deaths/immediately life-threatening events are to be recorded and submitted within 24 h of site awareness. Match key: AE window/reporting time. |
| PRO-N022 | p. 29, safety monitoring | Formal safety monitoring uses robust Poisson regression adjusted for site and gestational-age strata; 15 centers are stated. Match key: safety population/model/adjusters. |
| PRO-N023 | p. 29, interim efficacy | Three formal interim analyses occur at 25%, 50%, and 75% of planned enrolled infants who reach 36 weeks PMA. Lan-DeMets alpha-spending with O'Brien-Fleming-type boundary uses alpha 0.00015, 0.0030, 0.0183, and 0.0440 at the three interim looks and final analysis, respectively. Match key: interim plan/nominal threshold. |
| PRO-N024 | p. 29, futility | DSMC may recommend futility stop if the upper limit of a two-sided 80% CI on conditional power for the primary treatment effect fails to exceed 0.50 at the 50% interim analysis or 0.30 at the 75% interim analysis. Match key: futility rule. |

## Inferential-statistical relationships

| ID | Direct protocol evidence | Statistical definition / exact linkage |
|---|---|---|
| PRO-S001 | p. 4; p. 25 | Primary endpoint: risk/proportion of death or physiologic BPD by 36 weeks PMA, contrast budesonide+surfactant versus surfactant alone, intended ITT analysis. |
| PRO-S002 | p. 25 | Planned primary model: Poisson regression with robust sandwich variance (robust Poisson); fixed adjustment for NICU/site and dichotomized gestational age. The protocol does not supply the final-paper effect-measure label; match final model before comparison. |
| PRO-S003 | p. 25 | Secondary continuous outcomes: linear regression; dichotomous outcomes: robust Poisson; count outcomes: Poisson; ordinal outcomes: proportional odds; nominal outcomes with >2 levels: generalized logits. All models planned to adjust for randomization strata. |
| PRO-S004 | p. 25 | Safety analysis differs from primary efficacy set: treatment received rather than randomized arm; protocol plans a prespecified treatment-received sensitivity analysis because some randomized infants may not receive study drug. |
| PRO-S005 | pp. 25-26 | Sample-size hypothesis is a prospective two-arm relative-risk comparison, two-sided type-I error and three interim efficacy analyses. Planning assumptions 58% versus 48% correspond to 10 percentage-point absolute reduction; do not treat as final estimates. |
| PRO-S006 | p. 26, Table 5/text | Overall alpha 0.05 is spent to final alpha 0.044 after interim multiplicity adjustment; the 90% target uses 550/group by simulation, then 1160 total with approximately 5% attrition. |
| PRO-S007 | p. 29 | Interim analysis uses Lan-DeMets/O'Brien-Fleming-type spending at information times 25%, 50%, and 75%, with four stated nominal alpha levels including final 0.0440. Final-paper P value should not be mechanically compared to 0.05 without confirming its endpoint/model and whether it is multiplicity-adjusted. |
| PRO-S008 | p. 29 | Safety formal model: robust Poisson, site and gestational-age stratum fixed effects; possible site pooling or random-effect GLMM only if needed for site adjustment. |
| PRO-S009 | p. 29 | Futility is conditional power bounded by the upper limit of a two-sided 80% CI: >0.50 required at 50% look and >0.30 at 75% look to avoid the stated futility criterion. |
| PRO-S010 | p. 10, historical evidence | External-study estimates use RR, OR, CI, NNT, and p-value; they are background and must not be matched to BiB final estimates merely because endpoint labels overlap. |

## Page-by-page source coverage

| PDF page | Coverage status | Result-relevant quantitative content / explicit no-applicable record |
|---:|---|---|
| 1 | COMPLETE | Title/authorship/version page; no result-relevant quantitative relationship. |
| 2 | COMPLETE | Table of contents; no result-relevant relationship beyond section locator. |
| 3 | COMPLETE | Table of contents; no result-relevant relationship beyond section locator. |
| 4 | COMPLETE | Synopsis: eligibility, randomization, doses, primary/secondary/safety outcomes (PRO-N001-N006; PRO-S001). |
| 5 | COMPLETE | Objectives/outcomes and background burden (PRO-N007-N009). |
| 6 | COMPLETE | Background narrative; no new trial-result relationship; endpoint context carried by pp. 4-5. |
| 7 | COMPLETE | Background/preclinical rationale; no final-trial result. |
| 8 | COMPLETE | Background/preclinical rationale; no final-trial result. |
| 9 | COMPLETE | Prior-human-study background continuing to p. 10; no BiB final result. |
| 10 | COMPLETE | Prior human trials/meta-analysis, with complete external numerical estimates (PRO-N010-N013; PRO-S010). |
| 11 | COMPLETE | Background evidence; no newly applicable BiB result relationship. |
| 12 | COMPLETE | Background evidence; no newly applicable BiB result relationship. |
| 13 | COMPLETE | Background/dose rationale; no final-trial result. |
| 14 | COMPLETE | Dose-ranging and safety numerical context (PRO-N014-N015). |
| 15 | COMPLETE | Rationale/transition to methods; no new result-relevant numeric relationship. |
| 16 | COMPLETE | Study population/eligibility operational details; no new quantitative result beyond p. 4 eligibility. |
| 17 | COMPLETE | Screening/consent procedures; no applicable reported-result relationship. |
| 18 | COMPLETE | Consent procedures; no applicable reported-result relationship. |
| 19 | COMPLETE | Randomization procedures; no new quantity beyond p. 4 design/strata. |
| 20 | COMPLETE | Intervention procedures; no new quantity beyond p. 4 planned dose/dose count. |
| 21 | COMPLETE | Blinding/concomitant-treatment procedures; no applicable reported-result relationship. |
| 22 | COMPLETE | Study assessments; no new quantitative result beyond outcome timing/windows. |
| 23 | COMPLETE | Participant risks/benefits; no applicable reported-result relationship. |
| 24 | COMPLETE | Analytical-plan section opener; no additional relationship. |
| 25 | COMPLETE | Primary/secondary models and baseline planning assumptions (PRO-N016-N017; PRO-S002-S005). |
| 26 | COMPLETE | Sample-size Table 5 and recruitment-time calculations (PRO-N018-N020; PRO-S005-S006). |
| 27 | COMPLETE | AE/SAE definitions and timing (PRO-N021). |
| 28 | COMPLETE | AE/SAE reporting continuation; no additional result-relevant numeric relationship beyond p. 27. |
| 29 | COMPLETE | Safety model, interim efficacy alpha schedule, and futility rule (PRO-N022-N024; PRO-S007-S009). |
| 30 | COMPLETE | Data-monitoring/staffing procedures; no applicable reported-result relationship. |
| 31 | COMPLETE | References; no applicable reported-result relationship. |
| 32 | COMPLETE | References; no applicable reported-result relationship. |
| 33 | COMPLETE | References; no applicable reported-result relationship. |
| 34 | COMPLETE | References; no applicable reported-result relationship. |
| 35 | COMPLETE | References; no applicable reported-result relationship. |

## Scope limitations for downstream checking

1. This source is a protocol dated June 9, 2022 / September 8, 2023. Its sample size, expected risks, alpha spending, and model language are prospective plans. A difference from final reported analysis is not itself a candidate; determine whether a final SAP amendment or final report supplies the governing definition.
2. Native PDF text extraction is character-map corrupted. Exact page-linked evidence above was transcribed from rendered direct-source pages, with the raw/layout outputs retained only as an extraction audit trail.
3. Historical-study numbers at pp. 9-14 are protocol background. They are intentionally not asserted to be values from the paper under review.
4. No candidate diagnosis is made in this map.
