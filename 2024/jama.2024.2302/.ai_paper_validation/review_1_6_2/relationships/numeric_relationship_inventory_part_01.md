# Numeric inventory part 1

Status: COMPLETE. Exact IDs N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033, N034, N035, N036, N037, N038, N039, N040, N041, N042, N043, N044, N045, N046, N047, N048, N049, N050, N051, N052, N053, N054, N055, N056, N057, N058, N059, N060, N061, N062, N063, N064, N065, N066, N067, N068, N069, N070, N071, N072, N073, N074, N075, N076, N077, N078, N079, N080, N081, N082, N083, N084, N085, N086, N087, N088, N089, N090, N091, N092, N093, N094, N095, N096, N097, N098, N099, N100, N101, N102, N103, N104, N105, N106, N107, N108, N109, N110, N111, N112, N113, N114, N115, N116, N117, N118, N119, N120. 120 grouped relationships. Sources and calculations below are complete English; values remain as printed. See canonical index for scope, precision rule and limitations.

### N001

- **Source and role:** REPORT [DOC-001 p.1](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=1); p. 1 abstract Design; p. 2 Trial Funding; p. 4 Patient Characteristics.
- **Printed inputs and definitions:** Multicenter RCT at 39 US hospitals/medical centers; September 2013–April 2021; follow-up completed January 3, 2023.
- **Rule and calculation:** 39 center rows in supplement; randomized totals 172+166=338. Dates administrative; no numeric contradiction.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N002

- **Source and role:** REPORT [DOC-001 p.1](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=1); p. 1 Interventions; p. 2 Study Design; p. 3 Figure 1 footnotes d/e; pp. 5–8 display footnotes/captions.
- **Printed inputs and definitions:** Parallel two-strategy trial: early repair before NICU discharge; late repair after NICU discharge and when older than 55 weeks postmenstrual age. Late strategy includes an in-person visit 1 month after discharge. Timing may vary with condition and family/surgeon availability.
- **Rule and calculation:** 10-month outcome window and late >55-week threshold consistent across report copies; pragmatic deviations are separately counted.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N003

- **Source and role:** REPORT [DOC-001 p.2](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=2); p. 2 Patients.
- **Printed inputs and definitions:** Eligible diagnosed inguinal hernia, gestational age younger than 37 weeks, treated in participating NICU. Four exclusion categories: timing factors; concurrent procedure with hernia repair secondary; major congenital/chromosomal abnormalities likely affecting neurodevelopment; family unable to return for follow-up/late repair.
- **Rule and calculation:** Eligibility threshold <37 weeks; exclusion reasons may overlap by Figure 1 footnote a.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N004

- **Source and role:** REPORT [DOC-001 p.2](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=2); p. 2 Randomization; p. 3 Randomization and Figure 1 footnote c.
- **Printed inputs and definitions:** Infant-level allocation approximately 2 weeks before anticipated discharge; 1:1 allocation; permuted blocks 2–4; stratified by center and gestational age <28 vs ≥28 weeks; allocation concealed until randomization; REDCap module.
- **Rule and calculation:** 1:1 target allows 172/166 realized allocation; block sizes 2–4 and two GA strata retained.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N005

- **Source and role:** REPORT [DOC-001 p.1](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=1); p. 1 Main Outcomes; pp. 3–4 Outcomes; p. 6 Table 2 footnote g.
- **Printed inputs and definitions:** Primary outcome any prespecified serious adverse event in 10 months after randomization, assessed by blinded adjudication committee. Secondary outcomes total hospital days over same 10 months, including remaining NICU stay, postoperative stay and readmission days; individual serious adverse events.
- **Rule and calculation:** Count infants with at least one event, not sum of event types; hospital-day components share 10-month window.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N006

- **Source and role:** REPORT [DOC-001 p.3](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3); pp. 3–4 Outcomes.
- **Printed inputs and definitions:** Primary composite components: pulmonary apnea requiring intervention, prolonged intubation, unplanned reintubation, stridor, pneumonia; cardiac bradycardia requiring intervention, resuscitation, cardiac arrest; surgical intraoperative injury, wound disruption, surgical site infection; hernia incarceration, recurrence, reoperation; death. Table 3 additionally names regional anesthesia toxicity and other events.
- **Rule and calculation:** Event-type sums need not equal unique infants; no exhaustive mutually exclusive partition is stated.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N007

- **Source and role:** REPORT [DOC-001 p.4](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4); p. 4 Outcomes.
- **Printed inputs and definitions:** Inpatient daily and outpatient weekly record review; family assessment 30 days after repair and 10 months after enrollment; ongoing Bayley Scales of Infant Development third-edition cognitive composite at 2 years corrected age. No numerical neurocognitive result is reported.
- **Rule and calculation:** Assessment times retained; no numeric developmental result available to recompute.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N008

- **Source and role:** REPORT [DOC-001 p.1](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=1); p. 1 abstract Results.
- **Printed inputs and definitions:** 338 randomized (172 early, 166 late); printed phrase “320 underwent operative repair”; 86% male; 2% Asian, 30% Black, 16% Hispanic, 59% White; race unknown 9%, ethnicity unknown 4%; mean gestational age at birth 26.6 weeks (SD 2.8); mean postnatal age at enrollment 12 weeks (SD 5). Preserve the abstract population wording exactly, without replacing it with surgery or analysis totals from other locations.
- **Rule and calculation:** 338=172+166; retained=163+157=320; operated=152+129=281. 320 versus281 gap39, relative0.121875: F-NUM-001. Male274/320=85.625%; race/ethnicity use338 per Table1 footnote d; 8/338=2.367%,100/338=29.586%,54/338=15.976%,200/338=59.172%,29/338=8.580%,14/338=4.142%, all match integer-percent intervals.
- **Check status:** F-NUM-001.

### N009

- **Source and role:** REPORT [DOC-001 p.1](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=1); p. 1 abstract Results; p. 4 Patient Characteristics; p. 6 Primary Outcome.
- **Printed inputs and definitions:** Complete data 308 (91% of randomized), 159 early and 149 late; 44 (28%) early and 27 (18%) late with ≥1 event. Abstract RD −7.9%, 95% CrI −16.9% to 0%, posterior benefit probability 97%; matches Table 2 and primary narrative occurrences recorded below.
- **Rule and calculation:** 159+149=308;308/338×100=91.124%;44/159×100=27.673%;27/149×100=18.121%; displayed integer-percent intervals overlap. Matched primary counts reconcile.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N010

- **Source and role:** REPORT [DOC-001 p.1](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=1); p. 1 abstract Results; p. 6 Table 2 and Secondary Outcomes.
- **Printed inputs and definitions:** Hospital-day median 19.0 (IQR 9.8–35.0) early vs 16.0 (7.0–38.0) late; abstract posterior probability 82%; 10-month observation period.
- **Rule and calculation:** 19.0 and16.0 medians/IQR identical to Table2; no mean or rate inferred from medians.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N011

- **Source and role:** REPORT [DOC-001 p.1](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=1); p. 1 abstract Results; p. 7 Heterogeneity; p. 8 Figure 3.
- **Printed inputs and definitions:** Abstract calls subgroup analyses prespecified; benefit probability higher for <28 weeks and bronchopulmonary dysplasia, 99% each. Exact subgroup effects in M093–M099.
- **Rule and calculation:** 99% subgroup benefit probabilities match Figure3 and narrative; no crude/model equality imposed.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N012

- **Source and role:** REPORT [DOC-001 p.2](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=2); p. 2 Key Points; p. 1 Conclusion; p. 8 Conclusions.
- **Printed inputs and definitions:** Key Points: 28% early vs 18% late ≥1 SAE; RD −7.9%; late after discharge and >55 weeks appears to reduce SAE likelihood. Abstract/body conclusions: late strategy fewer infants with ≥1 SAE, supports delaying repair until after initial discharge.
- **Rule and calculation:** 28%,18%,−7.9% match abstract/Table2; late-benefit direction agrees with negative RD.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N013

- **Source and role:** REPORT [DOC-001 p.2](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=2); p. 2 introductory paragraph; p. 8 Discussion.
- **Printed inputs and definitions:** Background context only: hernia incidence reaches 40% in males born at 24 weeks; incarceration published rate range 5%–28%; processus vaginalis closure estimated 60% by age 2 years; other reports >30% clinical resolution. These are not HIP trial outcome counts.
- **Rule and calculation:** Historical incidence/resolution figures distinguish external background from current trial counts; no current-result recomputation.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N014

- **Source and role:** REPORT [DOC-001 p.4](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4); p. 4 Statistical Analysis, opening.
- **Printed inputs and definitions:** Frequentist and Bayesian analyses called prespecified in protocol Supplement 1; Bayesian analyses used primarily; SAP in Supplement 2.
- **Rule and calculation:** Model specification mapped for statistical review; numeric labels distinguish Bayesian CrI and frequentist CI.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N015

- **Source and role:** REPORT [DOC-001 p.4](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4); p. 4 Statistical Analysis, power paragraph.
- **Printed inputs and definitions:** A priori primary hypothesis 30% SAE early, 20% late; target absolute difference 10%; 586 infants with primary outcome data for 80% power at two-sided α=.05; 5% lost to follow-up; planned enrollment 615.
- **Rule and calculation:** 293×2=586;30%−20%=10pp;586/0.95=616.842 versus615. Treating printed5% as[4.5,5.5]% gives required enrollment[613.613,620.106], overlapping615±0.5. No reproduced allocation discrepancy.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N016

- **Source and role:** REPORT [DOC-001 p.4](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4); p. 4 Statistical Analysis, population paragraph.
- **Printed inputs and definitions:** Intention-to-treat analyses in full dataset, including all randomized infants except parent/guardian-requested withdrawals. No missing outcomes imputed.
- **Rule and calculation:** 172−9=163;166−9=157;163−4=159;157−8=149. Analysis uses observed outcomes, with no imputation.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N017

- **Source and role:** REPORT [DOC-001 p.4](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4); p. 4 Statistical Analysis, model paragraph.
- **Printed inputs and definitions:** Primary outcome logistic mixed-effects model. Secondary total hospital days negative-binomial mixed model. All models include gestational age group covariate and site random intercept.
- **Rule and calculation:** Hospital effect is negative-binomial count RR, primary effect derived from logistic fitted risks; medians do not define modeled RR.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N018

- **Source and role:** REPORT [DOC-001 p.4](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4); p. 4 Statistical Analysis, model paragraph.
- **Printed inputs and definitions:** Frequentist and Bayesian analyses same models, but frequentist primary outcome used GEE logistic model, exchangeable correlation for study site, because mixed-effects model nonconvergence.
- **Rule and calculation:** GEE frequentist primary exception is disclosed; primary effect identity still risk ratio/risk difference.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N019

- **Source and role:** REPORT [DOC-001 p.4](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4); p. 4 Statistical Analysis, priors paragraph.
- **Printed inputs and definitions:** All Bayesian analyses neutral priors; categorical/count intervention effect prior centered at OR or RR=1.0, 95% CrI 0.33–3.0; vague priors for other terms.
- **Rule and calculation:** OR/RR prior1 with range0.33–3.0 retained; statistical checker owns distribution/prior comparison.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N020

- **Source and role:** REPORT [DOC-001 p.4](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4); p. 4 Statistical Analysis, treatment modifiers.
- **Printed inputs and definitions:** Prespecified modifiers for primary and secondary: age <28 vs ≥28 weeks, bronchopulmonary dysplasia, open vs laparoscopic approach; Bayesian hierarchical models with main effects and treatment×modifier interaction, one modifier at a time; all 3 interaction priors centered at 1.0 with 95% CrI 0.33–3.0.
- **Rule and calculation:** Three modifier specifications retained; no crude subgroup ratio substituted for hierarchical posterior effects.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N021

- **Source and role:** REPORT [DOC-001 p.4](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4); p. 4 Statistical Analysis, estimates paragraph; p. 6 Table 2 footnotes a/d/e.
- **Printed inputs and definitions:** Primary RRs and RDs from posterior distribution of fitted logistic model. Table 2 says all analytic models include gestational age group/site, with no missing data in these covariates; RD from Bayesian logistic model with repair strategy covariate and site random intercept. Benefit late relative to early: RD<0, RR<1, fewer hospital days.
- **Rule and calculation:** Late-minus-early RD and late/early RR derived from fitted risks; crude primary RD −9.552pp and RR0.654820 do not diagnose model identity.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N022

- **Source and role:** REPORT [DOC-001 p.4](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4); p. 4 Statistical Analysis, interim paragraph; p. 8 Limitations.
- **Printed inputs and definitions:** Formal interim when data available for 309 infants, February 2021; 97% probability of decreased SAE rate with late; exceeds prespecified efficacy stopping threshold 95%; enrollment stopped on monitoring committee recommendation. Limitations repeats early stopping for prespecified Bayesian effectiveness rule.
- **Rule and calculation:** 97%>95% stopping threshold;309 interim observations versus final308 is a different data cut, no asserted same cohort.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N023

- **Source and role:** REPORT [DOC-001 p.4](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4); p. 4 Statistical Analysis, software; p. 6 Figure 2 caption.
- **Printed inputs and definitions:** R version 4.2.3. Figure 2 uses posterior median and percentile-based 95% CrI. No numerical P values, test statistics or standard errors for HIP trial results are displayed in the main paper. These quantities are explicitly absent, not transcribed as zero.
- **Rule and calculation:** Posterior median and percentile CrI; main has no P/test values to combine with counts.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N024

- **Source and role:** REPORT [DOC-001 p.3](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3); p. 3 Figure 1 top nodes.
- **Printed inputs and definitions:** 1514 assessed; 1176 excluded; 338 randomized.
- **Rule and calculation:** 1176+338=1514.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N025

- **Source and role:** REPORT [DOC-001 p.3](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3); p. 3 Figure 1 exclusions.
- **Printed inputs and definitions:** 442 not meeting eligibility: 184 another procedure influencing timing, 108 unavailable for repair/follow-up, 51 associated timing factor, 43 not in NICU, 32 major congenital/chromosomal abnormality, 31 no hernia diagnosis, 25 gestational age >37 weeks.
- **Rule and calculation:** 184+108+51+43+32+31+25=474 listed reasons for442 infants; multiple reasons explicitly permitted.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N026

- **Source and role:** REPORT [DOC-001 p.3](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3); p. 3 Figure 1 exclusions; p. 4 Patient Characteristics.
- **Printed inputs and definitions:** 734 eligible but not randomized: 613 parent/guardian refused, 54 parent/guardian unavailable, 37 physician decision, 14 not approached, 16 other. p. 4: 1072 eligible; 338 (32%) randomized; refusal 613 (84% of 734).
- **Rule and calculation:** 613+54+37+14+16=734;442+734=1176;734+338=1072;338/1072×100=31.530%;613/734×100=83.515%; integer percent intervals overlap32% and84%.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N027

- **Source and role:** REPORT [DOC-001 p.4](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4); p. 4 Patient Characteristics, refusal detail.
- **Printed inputs and definitions:** Within 613 refusals, 280 preferred early, 196 preferred late, 71 wanted clinician decision, 66 other reasons; pointers eTables 1–2 and by-site eTable 3 in Supplement 3.
- **Rule and calculation:** 280+196+71+66=613; identical supplement refusal breakdown.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N028

- **Source and role:** REPORT [DOC-001 p.3](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3); p. 3 Figure 1 randomized branches; p. 1 abstract.
- **Printed inputs and definitions:** 172 early randomized; 166 late randomized.
- **Rule and calculation:** 172+166=338; matches center column totals.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N029

- **Source and role:** REPORT [DOC-001 p.3](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3); p. 3 Figure 1 early branch; p. 4 Patient Characteristics.
- **Printed inputs and definitions:** 163 received treatment as randomized; 147 repair before NICU discharge; 11 no repair; 5 repair after NICU discharge. p. 4: 9 early withdrawals leaves 163.
- **Rule and calculation:** 147+11+5=163;163+9=172.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N030

- **Source and role:** REPORT [DOC-001 p.3](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3); p. 3 Figure 1 early no-repair branch; p. 5 surgery narrative.
- **Printed inputs and definitions:** 11 no repair: 7 clinically resolved untreated, 2 medically unstable, 1 surgeon disagreed with diagnosis (narrative diagnostic uncertainty), 1 transferred for cardiac surgery (narrative transferred facility).
- **Rule and calculation:** 7+2+1+1=11.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N031

- **Source and role:** REPORT [DOC-001 p.3](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3); p. 3 Figure 1 early post-discharge branch; p. 5 surgery narrative.
- **Printed inputs and definitions:** 5 after discharge: 2 changed medical condition, 1 discharged early, 1 initially clinically resolved, 1 twin; narrative gives 2 medical condition and 3 other reasons.
- **Rule and calculation:** 2+1+1+1=5;2+3=5 narrative grouping.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N032

- **Source and role:** REPORT [DOC-001 p.3](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3); p. 3 Figure 1 early branch; p. 4 Patient Characteristics.
- **Printed inputs and definitions:** 9 did not undergo treatment as randomized: 7 parents preferred late, 2 other. Narrative calls 9 withdrawn by parent/guardian because treatment preferences or other reasons.
- **Rule and calculation:** 7+2=9;172−9=163.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N033

- **Source and role:** REPORT [DOC-001 p.3](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3); p. 3 Figure 1 early follow-up and analysis; p. 4 Patient Characteristics.
- **Printed inputs and definitions:** 4 early lost to follow-up; 159 early primary analysis.
- **Rule and calculation:** 163−4=159.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N034

- **Source and role:** REPORT [DOC-001 p.3](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3); p. 3 Figure 1 late branch; p. 4 Patient Characteristics.
- **Printed inputs and definitions:** 157 received treatment as randomized; 90 repair after reaching 55 weeks; 28 no repair; 39 repair before reaching 55 weeks. p. 4: 9 late withdrawals leaves 157.
- **Rule and calculation:** 90+28+39=157;157+9=166.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N035

- **Source and role:** REPORT [DOC-001 p.3](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3); p. 3 Figure 1 late no-repair branch; p. 5 surgery narrative.
- **Printed inputs and definitions:** 28 no repair: 17 clinically resolved untreated, 4 parent refusal, 2 died (narrative unrelated death), 5 other.
- **Rule and calculation:** 17+4+2+5=28.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N036

- **Source and role:** REPORT [DOC-001 p.3](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3); p. 3 Figure 1 late <55-week branch; p. 6 surgery narrative.
- **Printed inputs and definitions:** 39 before 55 weeks: 13 clinician preference, 11 concerned about incarceration, 8 concurrent gastrostomy/repair, 5 parent preference, 2 postmenstrual age miscalculation.
- **Rule and calculation:** 13+11+8+5+2=39.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N037

- **Source and role:** REPORT [DOC-001 p.3](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3); p. 3 Figure 1 late branch; p. 4 Patient Characteristics.
- **Printed inputs and definitions:** 9 did not undergo treatment as randomized: 5 parents preferred early, 4 other; narrative calls 9 withdrawn by parent/guardian.
- **Rule and calculation:** 5+4=9;166−9=157.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N038

- **Source and role:** REPORT [DOC-001 p.3](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3); p. 3 Figure 1 late follow-up and analysis; p. 4 Patient Characteristics.
- **Printed inputs and definitions:** 8 late lost to follow-up; 149 late primary analysis; combined 308 infants available after withdrawals and losses.
- **Rule and calculation:** 157−8=149;159+149=308;4+8=12 lost;338−18−12=308.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N039

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Gestational age at birth, Median (IQR).
- **Printed inputs and definitions:** 26 (25–28); 26 (24–28); weeks; baseline 163/157
- **Rule and calculation:** Displayed means/medians/SD/IQR retained; lower≤median≤upper where applicable; group summaries cannot reconstruct individual-data pooled summaries.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N040

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Gestational age at birth, Mean (SD).
- **Printed inputs and definitions:** 27 (3); 27 (3); weeks; abstract mean/SD 26.6/2.8 in M008
- **Rule and calculation:** Mean (SD) in weeks, not counts or percentages. Each displayed arm mean 27 has interval [26.5,27.5], overlapping the abstract overall mean 26.6 interval [26.55,26.65]. Each displayed SD 3 has interval [2.5,3.5], overlapping abstract SD 2.8 interval [2.75,2.85]. A pooled mean or SD cannot otherwise be reconstructed from rounded arm summaries. No reproduced numerical conflict.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N041

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Gestational age <28 wk.
- **Printed inputs and definitions:** 103 (63); 104 (66); infants (%)
- **Rule and calculation:** 103/163×100=63.190184%; printed interval[62.500,63.500]%; gap=0.000000, relative=0.000000. 104/157×100=66.242038%; printed interval[65.500,66.500]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N042

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Gestational age ≥28 wk.
- **Printed inputs and definitions:** 60 (37); 53 (34); infants (%)
- **Rule and calculation:** 60/163×100=36.809816%; printed interval[36.500,37.500]%; gap=0.000000, relative=0.000000. 53/157×100=33.757962%; printed interval[33.500,34.500]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N043

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Age, Median (IQR), d.
- **Printed inputs and definitions:** 80 (61–112); 82 (64–104); days
- **Rule and calculation:** Displayed means/medians/SD/IQR retained; lower≤median≤upper where applicable; group summaries cannot reconstruct individual-data pooled summaries.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N044

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Postnatal age, Mean (SD), wk.
- **Printed inputs and definitions:** 12 (5); 12 (5); weeks; abstract matching M008
- **Rule and calculation:** Mean (SD) in weeks, not counts or percentages. Both arms print 12 (5), agreeing with abstract postnatal age 12 (5). Mean intervals [11.5,12.5] and SD intervals [4.5,5.5] overlap the matching displays; no reproduced numerical conflict.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N045

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Postmenstrual age, Median (IQR), wk.
- **Printed inputs and definitions:** 39 (37–42); 39 (37–41); weeks
- **Rule and calculation:** Displayed means/medians/SD/IQR retained; lower≤median≤upper where applicable; group summaries cannot reconstruct individual-data pooled summaries.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N046

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Birth weight, Median (IQR), g.
- **Printed inputs and definitions:** 835 (615–1072); 810 (660–1010); grams; p. 4 combined median 820 (640–1040)
- **Rule and calculation:** Displayed means/medians/SD/IQR retained; lower≤median≤upper where applicable; group summaries cannot reconstruct individual-data pooled summaries.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N047

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Male.
- **Printed inputs and definitions:** 141 (87); 133 (85); infants (%); p. 4 combined male 86%; abstract M008
- **Rule and calculation:** 141/163×100=86.503067%; printed interval[86.500,87.500]%; gap=0.000000, relative=0.000000. 133/157×100=84.713376%; printed interval[84.500,85.500]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N048

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Female.
- **Printed inputs and definitions:** 22 (13); 24 (15); infants (%)
- **Rule and calculation:** 22/163×100=13.496933%; printed interval[12.500,13.500]%; gap=0.000000, relative=0.000000. 24/157×100=15.286624%; printed interval[14.500,15.500]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N049

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Race, Asian.
- **Printed inputs and definitions:** 5 (3); 3 (2); denominators 172/166
- **Rule and calculation:** 5/172×100=2.906977%; printed interval[2.500,3.500]%; gap=0.000000, relative=0.000000. 3/166×100=1.807229%; printed interval[1.500,2.500]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N050

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Race, Black.
- **Printed inputs and definitions:** 49 (28); 51 (31); denominators 172/166
- **Rule and calculation:** 49/172×100=28.488372%; printed interval[27.500,28.500]%; gap=0.000000, relative=0.000000. 51/166×100=30.722892%; printed interval[30.500,31.500]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N051

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Race, Native Hawaiian or Other Pacific Islander.
- **Printed inputs and definitions:** 1 (0.6); 0; denominators 172/166; zero has no printed percentage
- **Rule and calculation:** 1/172×100=0.581395%; printed interval[0.550,0.650]%; gap=0.000000, relative=0.000000. No displayed percentage; zero count retained.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N052

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Race, White.
- **Printed inputs and definitions:** 99 (58); 101 (61); denominators 172/166
- **Rule and calculation:** 99/172×100=57.558140%; printed interval[57.500,58.500]%; gap=0.000000, relative=0.000000. 101/166×100=60.843373%; printed interval[60.500,61.500]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N053

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Race, Unknown.
- **Printed inputs and definitions:** 18 (10); 11 (7); denominators 172/166
- **Rule and calculation:** 18/172×100=10.465116%; printed interval[9.500,10.500]%; gap=0.000000, relative=0.000000. 11/166×100=6.626506%; printed interval[6.500,7.500]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N054

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Ethnicity, Hispanic.
- **Printed inputs and definitions:** 28 (16); 26 (16); denominators 172/166
- **Rule and calculation:** 28/172×100=16.279070%; printed interval[15.500,16.500]%; gap=0.000000, relative=0.000000. 26/166×100=15.662651%; printed interval[15.500,16.500]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N055

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Ethnicity, Non-Hispanic.
- **Printed inputs and definitions:** 135 (78); 135 (81); denominators 172/166
- **Rule and calculation:** 135/172×100=78.488372%; printed interval[77.500,78.500]%; gap=0.000000, relative=0.000000. 135/166×100=81.325301%; printed interval[80.500,81.500]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N056

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Ethnicity, Unknown.
- **Printed inputs and definitions:** 9 (5); 5 (3); denominators 172/166
- **Rule and calculation:** 9/172×100=5.232558%; printed interval[4.500,5.500]%; gap=0.000000, relative=0.000000. 5/166×100=3.012048%; printed interval[2.500,3.500]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N057

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Born at participating medical center.
- **Printed inputs and definitions:** 98 (60); 92 (59); rather than born elsewhere/transferred; footnote e
- **Rule and calculation:** 98/163×100=60.122699%; printed interval[59.500,60.500]%; gap=0.000000, relative=0.000000. 92/157×100=58.598726%; printed interval[58.500,59.500]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N058

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Prior to enrollment, Apnea requiring intervention.
- **Printed inputs and definitions:** 137 (85); 122 (79); footnote f missing 1/2; matching p. 4 narrative
- **Rule and calculation:** 137/162×100=84.567901%; printed interval[84.500,85.500]%; gap=0.000000, relative=0.000000. 122/155×100=78.709677%; printed interval[78.500,79.500]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N059

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Prior to enrollment, Bronchopulmonary dysplasia.
- **Printed inputs and definitions:** 82 (50); 78 (50); physician documentation per footnote g; p. 4 combined 50%
- **Rule and calculation:** 82/163×100=50.306748%; printed interval[49.500,50.500]%; gap=0.000000, relative=0.000000. 78/157×100=49.681529%; printed interval[49.500,50.500]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N060

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Prior to enrollment, Bradycardia requiring intervention.
- **Printed inputs and definitions:** 72 (44); 70 (45); footnote h missing 1 each
- **Rule and calculation:** 72/162×100=44.444444%; printed interval[43.500,44.500]%; gap=0.000000, relative=0.000000. 70/156×100=44.871795%; printed interval[44.500,45.500]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N061

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Prior to enrollment, Inguinal hernia incarceration.
- **Printed inputs and definitions:** 2 (1); 3 (2); baseline rather than 10-month outcome
- **Rule and calculation:** 2/163×100=1.226994%; printed interval[0.500,1.500]%; gap=0.000000, relative=0.000000. 3/157×100=1.910828%; printed interval[1.500,2.500]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N062

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Intraventricular hemorrhage grade 3 or 4.
- **Printed inputs and definitions:** 11 (7); 11 (7); footnote i missing 1 early
- **Rule and calculation:** 11/162×100=6.790123%; printed interval[6.500,7.500]%; gap=0.000000, relative=0.000000. 11/157×100=7.006369%; printed interval[6.500,7.500]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N063

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Hernia diagnosis by pediatric surgeon rather than neonatologist.
- **Printed inputs and definitions:** 115 (71); 112 (71); infants (%)
- **Rule and calculation:** 115/163×100=70.552147%; printed interval[70.500,71.500]%; gap=0.000000, relative=0.000000. 112/157×100=71.337580%; printed interval[70.500,71.500]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N064

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); Footnotes f–i.
- **Printed inputs and definitions:** See definition; See definition; Apnea: stimulation, nasal cannula oxygen, CPAP, ventilation, stimulant medication. Bradycardia: chest compressions and atropine. Ultrasound grades 1–4; higher worse; grade 3 fills >50% ventricle and enlarges it, grade 4 periventricular echo density.
- **Rule and calculation:** Explicit missing denominators retained: apnea162/155, bradycardia162/156, IVH162/157. Race/ethnicity172/166.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N065

- **Source and role:** REPORT [DOC-001 p.4](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4); pp. 4–5 Surgery Characteristics.
- **Printed inputs and definitions:** 152/163 (93%) underwent repair; 129/157 (82%) underwent repair; Printed surgery cohorts; retain separately from abstract phrase M008
- **Rule and calculation:** 152/163×100=93.252%;129/157×100=82.166%; operative total281, retained total320. Percent intervals overlap93%/82%; abstract conflict F-NUM-001.
- **Check status:** F-NUM-001.

### N066

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); p. 5 Surgery Characteristics.
- **Printed inputs and definitions:** 41 (39–44); 57 (52–61); median (IQR) postmenstrual age at surgery, weeks
- **Rule and calculation:** 41 within39–44;57 within52–61; units weeks.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N067

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); p. 5 Surgery Characteristics.
- **Printed inputs and definitions:** 3.1 (2.5–3.6); 5.9 (4.7–6.9); median (IQR) weight at surgery, kg
- **Rule and calculation:** 3.1 within2.5–3.6;5.9 within4.7–6.9; units kg.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N068

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); pp. 5–6 Surgery Characteristics.
- **Printed inputs and definitions:** 62 (42%) of 147 before-discharge repairs; 47 (36%) of 129 repairs; laparoscopic surgery; exact narrative denominators
- **Rule and calculation:** 62/147×100=42.177%;47/129×100=36.434%; integer percent intervals overlap42%/36%. Early denominator explicitly pre-discharge147.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N069

- **Source and role:** REPORT [DOC-001 p.5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5); pp. 5–6 Surgery Characteristics.
- **Printed inputs and definitions:** 146 (99%) of 147 before-discharge repairs; 127 (98%) of 129 repairs; general anesthesia
- **Rule and calculation:** 146/147×100=99.320%;127/129×100=98.450%; integer percent intervals overlap99%/98%.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N070

- **Source and role:** REPORT [DOC-001 p.6](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6); p. 6 Surgery Characteristics.
- **Printed inputs and definitions:** 57 (41.8–90.2); 70 (44.0–99.0); median (IQR) operative duration, minutes
- **Rule and calculation:** 57 within41.8–90.2;70 within44.0–99.0; units minutes.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N071

- **Source and role:** REPORT [DOC-001 p.6](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6); p. 6 Surgery Characteristics.
- **Printed inputs and definitions:** Combined >58%; Combined >58%; repaired infants undergoing concurrent operation: circumcision, gastrostomy, umbilical hernia repair or orchiopexy; no exact count/denominator supplied in sentence
- **Rule and calculation:** Threshold >58% lacks printed component count; no conflicting numerator asserted.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N072

- **Source and role:** REPORT [DOC-001 p.6](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6); p. 6 Surgery Characteristics.
- **Printed inputs and definitions:** 1.2%; 4.5%; orchiopexy; sentence lists late 4.5% then early 1.2%; no count supplied
- **Rule and calculation:** 1.2%/4.5% procedure frequencies have no printed numerator; no invented count.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N073

- **Source and role:** REPORT [DOC-001 p.6](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6); p. 6 Secondary Outcomes.
- **Printed inputs and definitions:** 18.0 (8.0–31.5); 13.0 (5.0–36.5); median (IQR) days enrollment to initial NICU discharge
- **Rule and calculation:** 18 within8–31.5;13 within5–36.5; no summation of medians to reconstruct total-hospital median.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N074

- **Source and role:** REPORT [DOC-001 p.6](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6); p. 6 Secondary Outcomes across columns.
- **Printed inputs and definitions:** 6.0 (3.0–11.5); 0.5 (0.5–1.0); median (IQR) days surgery to discharge
- **Rule and calculation:** 6 within3–11.5;0.5 within0.5–1; medians not additive.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N075

- **Source and role:** REPORT [DOC-001 p.6](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6); p. 6 Secondary Outcomes.
- **Printed inputs and definitions:** 35 (22%); median days 0; 42 (28%); median days 0; hospital readmissions and readmission hospital-day medians; sentence does not print IQR
- **Rule and calculation:** 35/159×100=22.013%;42/149×100=28.188%; overlaps22%/28%; readmission median0 is possible despite minority readmissions.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N076

- **Source and role:** REPORT [DOC-001 p.6](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6); pp. 6–7 Secondary Outcomes.
- **Printed inputs and definitions:** 0 spermatic cord injuries; 2 intestinal injuries; 0 spermatic cord injuries; Early intestinal injuries: 1 full thickness, 1 serosal tear
- **Rule and calculation:** 1+1=2 intestinal injuries; both cord injury counts0, no percentage asserted.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N077

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); p. 7 Secondary Outcomes.
- **Printed inputs and definitions:** 2 second repair operations; 2 incarceration; 3 second repair operations; 6 incarceration; Of 8 incarcerated infants, 1 early bowel injury required resection; none emergency operation
- **Rule and calculation:** 2+6=8 incarcerated infants;2 early/3 late reoperations match Table3.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N078

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); p. 7 Secondary Outcomes and Discussion.
- **Printed inputs and definitions:** 7 (4%) clinically resolved; 17 (11%) clinically resolved; precluded surgery; discussion repeats 4%/11%; denominator not printed in sentence; flow gives 163/157 retained
- **Rule and calculation:** 7/163×100=4.294%;17/157×100=10.828%; overlaps4%/11%;7+17=24 clinical resolutions.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N079

- **Source and role:** REPORT [DOC-001 p.6](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6); p. 6 Table 2 first outcome row; Primary Outcome narrative; Figure 2 caption; p. 1 abstract; p. 2 Key Points; p. 8 Figure 3 overall.
- **Printed inputs and definitions:** Any ≥1 SAE during 10 months: early 44/159 (28%), late 27/149 (18%); absolute RD −7.9% (95% CrI −16.9 to 0), RR 0.68 (0.45–1.01), posterior probability benefit 97%. p. 6 narrative gives 97% for both RD and RR, calls frequentist analyses consistent, and points to Supplement 3 eTable 2. Figure 3 separately displays RD −0.08 (−0.17 to 0.002) in proportion scale, preserved in M099.
- **Rule and calculation:** 44/159×100=27.673%,27/149×100=18.121%; primary counts match all locations and supplement. RD/RR model-derived. RD −7.9pp vs Figure3 −0.08 proportion overlaps half-unit intervals after unit conversion.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N080

- **Source and role:** REPORT [DOC-001 p.6](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6); p. 6 Table 2 second outcome row and Secondary Outcomes; p. 1 abstract.
- **Printed inputs and definitions:** Hospital stay median (IQR) days early 19.0 (9.8–35.0), late 16.0 (7.0–38.0); RD NA; RR 0.91 (95% CrI 0.74–1.11); posterior benefit 82%. Table header early n=159, late n=149; footnote g data missing 3 early infants. This count outcome uses negative-binomial model described in M017.
- **Rule and calculation:** Hospital denominator early159−3=156, late149; descriptive median/IQR duplicates match. Negative-binomial RR0.91 is not16/19.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N081

- **Source and role:** REPORT [DOC-001 p.6](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6); p. 6 Table 2 footnotes a–g.
- **Printed inputs and definitions:** Excludes 9 withdrawals each arm and 12 lost (4 early, 8 late). No missing gestational-group/site covariates. Early before NICU discharge; late after NICU discharge and >55 weeks. Footnote d RD model as M021; footnote e late-relative-to-early benefit directions; specific events Table 3; hospital days randomization through 10 months and missing 3 early.
- **Rule and calculation:** 338−2×9−12=308;159+149=308; hospital three early missing gives156/149; covariates have no missing data.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N082

- **Source and role:** REPORT [DOC-001 p.6](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6); p. 6 Figure 2 graph and caption.
- **Printed inputs and definitions:** Title Posterior Probability of the Estimated Relative Risk of Serious Adverse Events. X-axis estimated RR of serious adverse events ticks 0.27, 0.5, 0.7, 1, 1.5, 2; y-axis posterior density ticks 0, 0.2, 0.4, 0.6, 0.8, 1.0. Left of RR=1 favors late; right favors early. Blue dot posterior median, horizontal line percentile-based 95% CrI; caption RR 0.68 (0.45–1.01), probability 97% reduced SAE rate to any extent. No further graph-only numerical estimate is inferred from curve shape.
- **Rule and calculation:** RR0.68 within0.45–1.01; values match Table2; RR<1 late-benefit label agrees.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N083

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); Apnea requiring intervention.
- **Printed inputs and definitions:** 28 (17.6); 9 (6.0)
- **Rule and calculation:** 28/159×100=17.610063%; printed interval[17.550,17.650]%; gap=0.000000, relative=0.000000. 9/149×100=6.040268%; printed interval[5.950,6.050]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N084

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); Prolonged intubation (>48 h).
- **Printed inputs and definitions:** 6 (3.8); 0
- **Rule and calculation:** 6/159×100=3.773585%; printed interval[3.750,3.850]%; gap=0.000000, relative=0.000000. No displayed percentage; zero count retained.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N085

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); Bradycardia requiring intervention.
- **Printed inputs and definitions:** 5 (3.1); 4 (2.7)
- **Rule and calculation:** 5/159×100=3.144654%; printed interval[3.050,3.150]%; gap=0.000000, relative=0.000000. 4/149×100=2.684564%; printed interval[2.650,2.750]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N086

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); Cardiopulmonary resuscitation.
- **Printed inputs and definitions:** 4 (2.5); 4 (2.7)
- **Rule and calculation:** 4/159×100=2.515723%; printed interval[2.450,2.550]%; gap=0.000000, relative=0.000000. 4/149×100=2.684564%; printed interval[2.650,2.750]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N087

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); Stridor.
- **Printed inputs and definitions:** 3 (1.9); 1 (0.7)
- **Rule and calculation:** 3/159×100=1.886792%; printed interval[1.850,1.950]%; gap=0.000000, relative=0.000000. 1/149×100=0.671141%; printed interval[0.650,0.750]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N088

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); Death.
- **Printed inputs and definitions:** 2 (1.3); 3 (2.0)
- **Rule and calculation:** 2/159×100=1.257862%; printed interval[1.250,1.350]%; gap=0.000000, relative=0.000000. 3/149×100=2.013423%; printed interval[1.950,2.050]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N089

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); Pneumonia.
- **Printed inputs and definitions:** 2 (1.3); 0
- **Rule and calculation:** 2/159×100=1.257862%; printed interval[1.250,1.350]%; gap=0.000000, relative=0.000000. No displayed percentage; zero count retained.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N090

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); Regional anesthesia toxicity.
- **Printed inputs and definitions:** 1 (0.6); 0
- **Rule and calculation:** 1/159×100=0.628931%; printed interval[0.550,0.650]%; gap=0.000000, relative=0.000000. No displayed percentage; zero count retained.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N091

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); Unplanned reintubation.
- **Printed inputs and definitions:** 0; 1 (0.7)
- **Rule and calculation:** No displayed percentage; zero count retained. 1/149×100=0.671141%; printed interval[0.650,0.750]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N092

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); Cardiac arrest.
- **Printed inputs and definitions:** 0; 3 (2.0)
- **Rule and calculation:** No displayed percentage; zero count retained. 3/149×100=2.013423%; printed interval[1.950,2.050]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N093

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); Inguinal hernia incarceration.
- **Printed inputs and definitions:** 2 (1.3); 6 (4.0)
- **Rule and calculation:** 2/159×100=1.257862%; printed interval[1.250,1.350]%; gap=0.000000, relative=0.000000. 6/149×100=4.026846%; printed interval[3.950,4.050]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N094

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); Inguinal hernia recurrence.
- **Printed inputs and definitions:** 2 (1.3); 1 (0.7)
- **Rule and calculation:** 2/159×100=1.257862%; printed interval[1.250,1.350]%; gap=0.000000, relative=0.000000. 1/149×100=0.671141%; printed interval[0.650,0.750]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N095

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); Inguinal hernia reoperation.
- **Printed inputs and definitions:** 2 (1.3); 3 (2.0)
- **Rule and calculation:** 2/159×100=1.257862%; printed interval[1.250,1.350]%; gap=0.000000, relative=0.000000. 3/149×100=2.013423%; printed interval[1.950,2.050]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N096

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); Intraoperative injury to adjacent structure.
- **Printed inputs and definitions:** 2 (1.3); 0
- **Rule and calculation:** 2/159×100=1.257862%; printed interval[1.250,1.350]%; gap=0.000000, relative=0.000000. No displayed percentage; zero count retained.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N097

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); Wound disruption.
- **Printed inputs and definitions:** 0; 1 (0.7)
- **Rule and calculation:** No displayed percentage; zero count retained. 1/149×100=0.671141%; printed interval[0.650,0.750]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N098

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); Surgical site infection.
- **Printed inputs and definitions:** 1 (0.6); 2 (1.3)
- **Rule and calculation:** 1/159×100=0.628931%; printed interval[0.550,0.650]%; gap=0.000000, relative=0.000000. 2/149×100=1.342282%; printed interval[1.250,1.350]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N099

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); Other event.
- **Printed inputs and definitions:** 1 (0.6), footnote g; 2 (1.3), footnote h
- **Rule and calculation:** 1/159×100=0.628931%; printed interval[0.550,0.650]%; gap=0.000000, relative=0.000000. 2/149×100=1.342282%; printed interval[1.250,1.350]%; gap=0.000000, relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N100

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); Table 3 footnotes b–h.
- **Printed inputs and definitions:** Early strategy before discharge; footnote d apnea includes increased oxygen/respiratory support, bag-mask ventilation, initiated/increased mechanical ventilation; footnote e bradycardia treated pharmacologically; footnote g pneumothorax after repair requiring high-frequency oscillator ventilation 3 days; Late strategy after discharge and >55 weeks; footnote h 1 infected scrotal hematoma drained, 1 circumcision bleeding requiring overnight admission
- **Rule and calculation:** Other-event counts1/2 match enumerated footnotes; overlap across event categories permitted.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N101

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); Table 3 footnote f.
- **Printed inputs and definitions:** Incarceration is nonreducible hernia requiring urgent repair, or narcotic pain medication/sedation for reduction, or pediatric surgery team; Same definition
- **Rule and calculation:** Count outcome2/6 matches narrative incarceration8; definition retained.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N102

- **Source and role:** REPORT [DOC-001 p.8](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8); Gestational age <28 wk.
- **Printed inputs and definitions:** 33/102 (32); 16/99 (16); −0.11 (−0.21 to −0.01); 0.61 (0.39–0.94); 99; p. 7 Heterogeneity RR/CrI/probability; p. 1 abstract probability
- **Rule and calculation:** 33/102×100=32.352941%; printed interval[31.500,32.500]%; gap=0.000000, relative=0.000000. 16/99×100=16.161616%; printed interval[15.500,16.500]%; gap=0.000000, relative=0.000000. Modeled RD/RR, not crude effects; point/interval direction labels retained. GA partitions159/149 and44/27; BPD partitions159/149 and44/27. Approach strata150/126 and42/23 do not claim coverage of all randomized or analyzed infants.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N103

- **Source and role:** REPORT [DOC-001 p.8](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8); Gestational age ≥28 wk.
- **Printed inputs and definitions:** 11/57 (19); 11/50 (22); −0.02 (−0.14 to 0.11); 0.92 (0.47–1.75); 61; p. 7 Heterogeneity RR/CrI/probability
- **Rule and calculation:** 11/57×100=19.298246%; printed interval[18.500,19.500]%; gap=0.000000, relative=0.000000. 11/50×100=22.000000%; printed interval[21.500,22.500]%; gap=0.000000, relative=0.000000. Modeled RD/RR, not crude effects; point/interval direction labels retained. GA partitions159/149 and44/27; BPD partitions159/149 and44/27. Approach strata150/126 and42/23 do not claim coverage of all randomized or analyzed infants.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N104

- **Source and role:** REPORT [DOC-001 p.8](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8); Bronchopulmonary dysplasia Yes.
- **Printed inputs and definitions:** 26/81 (32); 10/73 (14); −0.14 (−0.26 to −0.03); 0.50 (0.27–0.87); 99; p. 7 Heterogeneity RR/CrI/probability; p. 1 abstract probability
- **Rule and calculation:** 26/81×100=32.098765%; printed interval[31.500,32.500]%; gap=0.000000, relative=0.000000. 10/73×100=13.698630%; printed interval[13.500,14.500]%; gap=0.000000, relative=0.000000. Modeled RD/RR, not crude effects; point/interval direction labels retained. GA partitions159/149 and44/27; BPD partitions159/149 and44/27. Approach strata150/126 and42/23 do not claim coverage of all randomized or analyzed infants.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N105

- **Source and role:** REPORT [DOC-001 p.8](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8); Bronchopulmonary dysplasia No.
- **Printed inputs and definitions:** 18/78 (23); 17/76 (22); −0.04 (−0.14 to 0.07); 0.85 (0.51–1.37); 75; p. 7 Heterogeneity RR/CrI/probability
- **Rule and calculation:** 18/78×100=23.076923%; printed interval[22.500,23.500]%; gap=0.000000, relative=0.000000. 17/76×100=22.368421%; printed interval[21.500,22.500]%; gap=0.000000, relative=0.000000. Modeled RD/RR, not crude effects; point/interval direction labels retained. GA partitions159/149 and44/27; BPD partitions159/149 and44/27. Approach strata150/126 and42/23 do not claim coverage of all randomized or analyzed infants.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N106

- **Source and role:** REPORT [DOC-001 p.8](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8); Surgical approach Laparoscopic.
- **Printed inputs and definitions:** 16/62 (26); 6/47 (13); −0.10 (−0.23 to 0.01); 0.54 (0.25–1.05); 96; p. 7 says open vs laparoscopic did not modify effect
- **Rule and calculation:** 16/62×100=25.806452%; printed interval[25.500,26.500]%; gap=0.000000, relative=0.000000. 6/47×100=12.765957%; printed interval[12.500,13.500]%; gap=0.000000, relative=0.000000. Modeled RD/RR, not crude effects; point/interval direction labels retained. GA partitions159/149 and44/27; BPD partitions159/149 and44/27. Approach strata150/126 and42/23 do not claim coverage of all randomized or analyzed infants.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N107

- **Source and role:** REPORT [DOC-001 p.8](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8); Surgical approach Open repair.
- **Printed inputs and definitions:** 26/88 (30); 17/79 (22); −0.07 (−0.18 to 0.03); 0.74 (0.46–1.16); 90; p. 7 same approach claim
- **Rule and calculation:** 26/88×100=29.545455%; printed interval[29.500,30.500]%; gap=0.000000, relative=0.000000. 17/79×100=21.518987%; printed interval[21.500,22.500]%; gap=0.000000, relative=0.000000. Modeled RD/RR, not crude effects; point/interval direction labels retained. GA partitions159/149 and44/27; BPD partitions159/149 and44/27. Approach strata150/126 and42/23 do not claim coverage of all randomized or analyzed infants.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N108

- **Source and role:** REPORT [DOC-001 p.8](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8); Overall.
- **Printed inputs and definitions:** 44/159 (28); 27/149 (18); −0.08 (−0.17 to 0.002); 0.68 (0.45–1.01); 97; p. 6 Table 2/primary narrative/Figure 2; p. 1 abstract; p. 2 Key Points
- **Rule and calculation:** 44/159,27/149 match Table2; −0.08[−0.085,−0.075] overlaps−7.9pp converted[−0.0795,−0.0785]. −0.17 proportion lower limit likewise overlaps−16.9pp; upper0.002[0.0015,0.0025] overlaps0pp[−0.005,0.005].
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N109

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); p. 7 Heterogeneity, gestational-age interaction.
- **Printed inputs and definitions:** Not displayed; Not displayed; Not displayed; Not displayed; 91; Printed Bayesian probability of gestational age×treatment interaction; distinct from within-subgroup benefit probabilities
- **Rule and calculation:** 91% interaction probability is distinct from99% within-subgroup benefit, not compared as same quantity.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N110

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); p. 7 Heterogeneity, BPD interaction.
- **Printed inputs and definitions:** Not displayed; Not displayed; Not displayed; Not displayed; 95; Printed Bayesian probability of BPD×treatment interaction; distinct from within-subgroup benefit probabilities
- **Rule and calculation:** 95% interaction probability is distinct from99% within-subgroup benefit.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N111

- **Source and role:** REPORT [DOC-001 p.7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7); p. 7 Discussion; p. 8 Conclusions/Limitations.
- **Printed inputs and definitions:** 338 randomized; 32% eligible randomized repeated; Late benefit greatest for <28-week and BPD infants; fewer SAE, fewer hospital days, low incarceration, greater clinical resolution; No added estimate; No added estimate; Not displayed; Withdrawals and lack of data reduced analysis sample; stopped early per Bayesian rule; qualitative claim that late may hasten discharge by several days, no new exact effect
- **Rule and calculation:** 338 randomized and32% eligible-randomized agree with flow; qualitative subgroup directions agree.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N112

- **Source and role:** PLAN DOC-002; SUP-P01 Identity, intervention and endpoint hierarchy.
- **Printed inputs and definitions:** [Protocol page 1](../../../joi240020supp1_prod_1710443209.74911.pdf#page=1) identifies version 7, November 27, 2019, original November 5, 2012, NCT01678638. This supplied PDF is the amended version, not a separate copy of the original protocol. The original specification can be identified only where the document explicitly describes amendment history; do not reconstruct absent earlier versions.  [Pages 2–3](../../../joi240020supp1_prod_1710443209.74911.pdf#page=2): primary proportion of infants with ≥1 SAE during enrollment to 10 months after enrollment, independently adjudicated masked to treatment assignment. Late versus early hypothesis: 10-percentage-point absolute reduction, RR=0.66, number needed to harm=10 for early repair. Assumed 60% randomization, 615 randomized over 2.5 years. Secondary hospital days enrollment to 10 months, median reduction 3 days; page 3 prints early 18 versus late 15 days. Secondary BSIDIII Cognitive Composite difference 0.4 SD = 6 points, at 22–26 months corrected age / approximately 2 years, first 200 infants in selected centers. Corrected age formula: chronological age minus weeks/months premature. Main matching keys: primary any-SAE at 10 months; total hospital days at 10 months; neurodevelopment outcome status/time; intervention early/late timing.  [Page 10](../../../joi240020supp1_prod_1710443209.74911.pdf#page=10): early repair promptly after randomization, before NICU discharge, approximately 38 weeks PMA. Late goal 5 months after discharge, approximately 55–60 weeks PMA. The title specifies after discharge and beyond 55 weeks PMA. Operation/admission determined clinically under pragmatic practice; laparoscopic/open and general/regional/other anesthesia permitted (page 11). Infants may cross intended timing for clinical reasons, including late-group incarceration or early-group condition changes; recorded as outcomes. No fixed drug dose or anesthesia duration is assigned.  Eligibility on page 10: GA <37 weeks 0 days, NICU/other nursery at participating site, surgeon-diagnosed IH, parental consent and provider willingness. Exclusions: factor affecting timing, other operation with IH as secondary procedure affecting timing, known major congenital/chromosomal anomaly, inability to return or monitor as outpatient.
- **Rule and calculation:** 30−20=10pp;20/30=0.666667 versus0.66±0.005 gap0.001667 relative0.002525≤0.05;1/0.10=10;0.4×15=6;18−15=3 and8−5=3days, SAP discloses clarification.
- **Check status:** F-NUM-002.

### N113

- **Source and role:** PLAN DOC-002; SUP-P02 Randomization/measurement design.
- **Printed inputs and definitions:** [Page 6](../../../joi240020supp1_prod_1710443209.74911.pdf#page=6), Figure 1: identify/consent approximately 2 weeks before expected discharge; randomization approximately 36 weeks PMA, study time zero; early approximately 38 weeks PMA; late approximately 55 weeks PMA; prospective SAE measurement until 10 months, approximately 30 sites, N=586; BSIDIII at 22–26 months corrected age. Text: site and GA <28 versus ≥28 weeks stratification. Figure 2 on page 7 is an empty CONSORT template: no observed numerical counts, no trial result to extract. Fields are assessed, excluded (eligibility, declined, other), randomized, allocated/received/did not receive, lost/discontinued, analyzed/excluded, symmetrically for arms.  [Page 8](../../../joi240020supp1_prod_1710443209.74911.pdf#page=8): randomize when approximately 2 weeks from anticipated discharge via REDCap site/GA strata. Screening records count, GA, sex, eligible/ineligible reasons, eligible not enrolled and planned treatment. Center-table footnote uses PHIS 2011 data for 13/19 (68%) sites. Pages 8–10 are administrative site/affiliation/personnel listings without numeric per-site recruitment cells; page 9 has no additional result-relevant quantity.  [Page 11](../../../joi240020supp1_prod_1710443209.74911.pdf#page=11): end ascertainment 10 months after randomization; earliest discharge assumed 35 weeks PMA, latest repair example 65 weeks PMA gives 1.5–2 postoperative months. Equal enrollment-to-end window; early longer postoperative, late longer preoperative. Surveillance ceases at 10 months, then developmental tracking. SAE reliability checked for random 10%; perioperative direct interview through 24 hours after surgery plus records. Adjudication masked; highest harm among ≥1 SAE classified E–I, secondary outcome. Main matching keys: ascertainment window, any-SAE definition, blinded adjudication and safety-event labels.
- **Rule and calculation:** 586 prospective target; blank template no observed count;13/19×100=68.421% overlaps68±0.5%;36/38/55-week timing prospective.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N114

- **Source and role:** PLAN DOC-002; SUP-P03 Sample size/power/analysis.
- **Printed inputs and definitions:** [Page 12](../../../joi240020supp1_prod_1710443209.74911.pdf#page=12): early SAE 30%, late 20%, 293/group, total 586 assessed, 80% power, two-sided alpha .05, absolute difference 10%. Assumes 20 eligible infants/site/year, 60% randomization, 95% follow-up, 19 sites, 615 randomizations over approximately 2.5 years. Hospital days: 98% power for median difference 3 days, lognormal early median 8 / mean 18 versus late median 5 / mean 13. BSIDIII 0.4 SD / 6 points with 200 assessed at 22–26 months.  [Page 13](../../../joi240020supp1_prod_1710443209.74911.pdf#page=13), Table 4:   /  Infants/group  /  Power: 10% SAE-rate difference  /  Power: 3-day median hospital-day difference  /   / ---: / ---: / ---: /   /  293  /  80%  /  98%  /   /  250  /  73%  /  97%  /   /  200  /  64%  /  92%  /   /  150  /  52%  /  81%  /   Intent-to-treat. General linear mixed models for primary/secondary outcomes; inspect symmetry/unimodality, group variance and residuals, adjust key demographics if necessary (sex/ethnicity examples). Primary ≥1 SAE: binomial GLMM log link, treatment and GA <28 / ≥28 covariates, center random effect. Hospital days: lognormal same covariates/random center. BSIDIII: linear mixed model same specification. Primary absolute RD and 95% CI; continuous absolute differences and 95% CI; similar models other secondary outcomes. Additional final Bayesian primary/major-secondary analysis, neutral prior centered RR 1.0 with 95% CrI 0.33–3.0. Main matching keys: sample-size assumptions; analysis population; logistic versus log-binomial model; negative-binomial versus lognormal hospital model; adjustment/site clustering; Bayesian primary/frequentist secondary hierarchy and priors.
- **Rule and calculation:** 293×2=586;30−20=10pp;586/0.95=616.842 versus615 is within half-unit95% interval:required[613.613,620.106]. Four power rows monotonically rise with sample. Statistical checker owns power reproduction.
- **Check status:** F-NUM-002.

### N115

- **Source and role:** PLAN DOC-002; SUP-P04 Subgroups, prediction and stopping.
- **Printed inputs and definitions:** [Page 13](../../../joi240020supp1_prod_1710443209.74911.pdf#page=13): Bayesian hierarchical treatment interactions for primary SAE, hospital days, BSIDIII. Prespecified moderators GA <28/≥28, BPD yes/no, maternal education ≤12 years yes/no, prenatal care yes/no, IH difficult to reduce yes/no. Dixon–Simon shrinkage toward overall mean. Main-effect priors neutral N(0,1000), SD parameters Uniform(0,1000); neutral/skeptical interaction priors. Point effects/95% CrI and probability benefit/harm. Similar sex and race/ethnicity subgroup analyses required for NIH Phase III. Prediction tool uses covariates with large probability of interaction, predicts SAE, hospital days and Bayley <70 impairment; validate posterior predictive checks and ROC where appropriate. Secondary/novel analyses, not primary.  [Page 14](../../../joi240020supp1_prod_1710443209.74911.pdf#page=14): amended interim planned December 2019, approximately 200 infants with 10-month data. Bayesian harm outcomes death and prolonged stay >30 days after surgery; benefit primary proportion with an SAE and secondary total hospital length of stay. Neutral priors imply 50:50 prior chance either strategy better. Safety stopping probability of increased harm >90% in either arm for death/prolonged stay. Efficacy stopping probability of decreased SAEs >95% in either arm. DSMB considers these data. No numerical multiplicity adjustment or noninferiority/equivalence margin is specified in this protocol.  [Page 15](../../../joi240020supp1_prod_1710443209.74911.pdf#page=15): conclusion based on total evidence if under-enrolled; could recommend late repair for significant total-hospital-day reduction if SAE and Bayley do not favor early, particularly posterior probability >80% that SAE lower and Bayley higher with late. Main matching keys: interim decision/stopping, final benefit probability, subgroup model/estimates and secondary outcome reporting.
- **Rule and calculation:** 50+50=100% prior;97%>95% efficacy;90% safety distinct;200 planned vs309 performed interim mapped for design lane.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N116

- **Source and role:** PLAN DOC-002; SUP-P05 Developmental scale and SAE definitions.
- **Printed inputs and definitions:** [Page 12](../../../joi240020supp1_prod_1710443209.74911.pdf#page=12): first 200 developmental assessments, 8 NRN centers and other capable sites; participation voluntary. BSIDIII Cognitive, Language, Motor age-standardized composites mean100 SD15; <70 (>2 SD below mean) significant delay. Severe delay precluding testing assigned 54. Cerebral palsy abnormal tone in ≥1 extremity with abnormal movement/posture; GMFCS severity. Follow-up surgery history collected from end SAE ascertainment through 22–26-month visit. These are planned outcomes, not current observed neurodevelopment results.  [Pages 11–12](../../../joi240020supp1_prod_1710443209.74911.pdf#page=11), Table 3: cardiorespiratory/anesthesia events death, ECMO, cardiac arrest, CPR, hypotension with vasoactive drugs, apnea with increased respiratory support, local anesthetic toxicity (e.g. seizure), prolonged intubation/ventilation >48 hours after operation, unplanned reintubation, intraoperative unplanned extubation. IH/surgery events incarceration, strangulation, recurrence, reoperation IH/initial operation, adjacent-structure injury, deep wound disruption, deep SSI, other SAE requiring intervention to prevent/address harm.  [Page 23](../../../joi240020supp1_prod_1710443209.74911.pdf#page=23), appendix definitions:   /  SAE  /  Recorded definition  /   / --- / --- /   /  Death  /  Any cause, records/vital statistics/maternal report, verified where possible  /   /  ECMO  /  Cannulation for any cause regardless of successful initiation  /   /  Cardiac arrest  /  Heart rate zero in records  /   /  CPR  /  Ventilation and cardiac massage with/without medication/intervention  /   /  Apnea with respiratory support  /  ≥1 episode, increased FiO2 AND increased respiratory support: bag/mask, bag/tube, initiation/increase mechanical ventilation  /   /  Hypotension with vasoactive drugs  /  Vasopressor/other vasoactive treatment for pressure below age-specific standards; fluid bolus alone or unchanged preoperative drug dose excluded  /   /  Persistent bradycardia receiving treatment  /  Low heart rate with pharmacologic intervention  /   /  Local anesthetic toxicity  /  Presumed local-anesthetic event from anesthesia/PACU/PICU/NICU records  /   /  Regional anesthetic toxicity  /  Presumed regional-anesthetic-medication event from corresponding records  /   /  Prolonged intubation  /  Intubated/mechanically ventilated >48 h after procedure completion, only if not mechanically ventilated before surgery  /   /  Unplanned reintubation  /  Reintubation not planned  /   /  Intraoperative unplanned extubation  /  Inadvertent during surgery, record reintubation yes/no  /   /  IH incarceration  /  Nonreducible AND urgent repair; OR narcotic/sedation to reduce; OR surgical-team reduction documented as incarceration  /   /  IH strangulation  /  Incarcerated contents ischemic/damaged at operation  /   /  IH recurrence  /  Return during study by examination/imaging AND recorded  /   /  Reoperation  /  Second/subsequent IH operation same or contralateral side OR operation due to IH-repair SAE  /   [Page 24](../../../joi240020supp1_prod_1710443209.74911.pdf#page=24), appendix continuation:   /  SAE  /  Recorded definition  /   / --- / --- /   /  Adjacent structure/organ injury  /  Believed surgical injury at original operation or identified subsequently  /   /  Deep wound disruption  /  Wound dehiscence including deep external oblique fascia  /   /  Deep surgical-site infection  /  Within 30 days, deep fascia/muscle AND ≥1 of purulent deep drainage, incision dehisces/opened deliberately, documented abscess, or attending/surgeon records deep SSI  /   /  Other SAE requiring intervention  /  Recorded SAE requiring specific intervention to prevent/address harm  /   Footnotes: all ascertainment enrollment through 10 months. PACU means postanesthesia/recovery unit. Prolonged intubation, unplanned reintubation, wound disruption, SSI definitions adapted from ACS Pediatric NSQIP. The appendix separately includes persistent bradycardia and regional toxicity, beyond the condensed Table 3 labels; all are retained for outcome-component matching.  NCC MERP graphical scale on page 24: A potential circumstances; B event does not reach patient; C reaches without harm; D reaches and monitoring/intervention to preclude harm; E temporary harm requiring intervention; F temporary harm requiring initial/prolonged hospitalization; G permanent harm; H intervention necessary to sustain life; I contributes to death. The trial uses E–I. Legend: no event/no harm/harm/death classes. Definitions: harm physical/emotional/psychological function or structure impairment/pain; monitoring observing relevant physiological/psychological signs; intervention may change therapy/active treatment; life-sustaining intervention includes cardiovascular/respiratory support. No numerical risk estimate is printed in the scale.
- **Rule and calculation:** 100−2×15=70;0.4×15=6;54<70;200 developmental subset does not add to586 primary.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N117

- **Source and role:** PLAN DOC-002; SUP-P06 Amendments and administrative quantities.
- **Printed inputs and definitions:** [Page 25](../../../joi240020supp1_prod_1710443209.74911.pdf#page=25): version2 May15,2013 adds selected capable sites to developmental aim and administrative updates; version3 Dec30,2014 coordinator update; version4 Feb13,2015 opens developmental follow-up outside NRN, first200 eligible participants at capable NRN/non-NRN sites; version5 Apr27,2016 PMA terminology, investigators, recruitment/eligibility clarification; version6 Dec20,2018 adjudicators/sites and deletes Appendix I because MOP holds database fields; version7 Nov27,2019 slower enrollment replaces TWO interim safety analyses at33% and66% enrollment with safety/efficacy analysis December2019 approximately200 infants, adds final Bayesian primary/major-secondary alongside planned frequentist analysis. No earlier full plan version or MOP supplied.  Other opened administrative content: page2 success ≥60% randomization; page6 recruitment >60% expected; page7 >500 eligible/year and 2.5-year enrollment; page15 recruitment 240 randomized/year in first two years and120 in first half third year, sites below40% randomization at6 months reviewed, prepared to continue to target; page16 8 organizational components,20–30 sites,30-day data checks/query resolution, DSMC twice/year, primary paper end year3/developmental end year5; page17 IRB and June3,2013 pilot at Vanderbilt plus5 sites, no eligible nonrandomized data sought in pilot. These are administrative/prospective quantities, not current outcome estimates. References pages18–22 were opened completely; citation years, volume/pages and titles do not create current trial-result relationships.
- **Rule and calculation:** 33%/66% interim replaced by approximately200;240×2+120=600 approximate recruitment schedule vs615 target administrative, no observed count.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N118

- **Source and role:** PLAN DOC-002; SUP-P07 Pilot Table 1 (background, not HIP trial results).
- **Printed inputs and definitions:** [Page 5](../../../joi240020supp1_prod_1710443209.74911.pdf#page=5): 39/50 eligible randomized (78%) at4 sites, early19 late20; late goal55 weeks PMA. Printed title describes reduction with early repair. Values are mean/range except the explicitly median/range postoperative stay.   /  Row  /  Early N19  /  Late N20  /   / --- / --- / --- /   /  Estimated GA, weeks  /  28.9 (24–32)  /  28.4 (25–34)  /   /  Birth weight, g  /  959 (520–1550)  /  958 (500–2710)  /   /  PMA operation, weeks  /  38.4 (34–49)  /  48.6 (33–61)  /   /  Weight operation, kg  /  2.55 (1.8–4.0)  /  3.9 (1.3–8.9)  /   /  Postoperative apnea/bradycardia  /  4/19 (21%)  /  0  /   /  Reintubation/failure extubation  /  5/19 (26%)  /  2/12 (17%)  /   /  Any anesthetic event  /  9/19 (47%)  /  2/12 (17%)  /   /  Postoperative stay, median(range), days  /  8 (1–206)  /  1 (0–30)  /   /  Medical attention for IH reduction  /  0  /  6/12 (50%)  /   /  Death after IH repair  /  0  /  0  /   Footnotes:8 late infants without repair during study,2 died from prematurity after discharge,5 lost,1 no identifiable IH;6 repaired before55 weeks (range33–49),4 incarceration,2 parental/provider preference. Pilot did not measure all study-period hospital days. These background results may inform assumptions but do not match current HIP outcome cells.
- **Rule and calculation:** 19+20=39;39/50=78%;20−8=12;2+5+1=8;4+2=6. Pilot4/19=21.053%,5/19=26.316%,9/19=47.368%,2/12=16.667%,6/12=50%;all integer-percent half-unit intervals overlap. All means/medians inside ranges.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N119

- **Source and role:** PLAN DOC-003; SUP-S01 Date, clarified hypotheses and allocation.
- **Printed inputs and definitions:** [SAP page 1](../../../joi240020supp2_prod_1710443209.75411.pdf#page=1): version1 October31,2022; protocol version7 Nov27,2019 original Nov5,2012. Page2 scope: planned analyses included in future manuscripts as deemed necessary by HIP subcommittee; additional exploratory analyses permitted. No independent earlier SAP supplied.  [Pages 2–3](../../../joi240020supp2_prod_1710443209.75411.pdf#page=2): primary ≥1 SAE from enrollment through10 months, late >55 weeks PMA and after discharge, approximately5 months after discharge, early before discharge approximately38 weeks. Assumed SAE30% early20% late, absolute10% reduction. Secondary total hospital days median reduction3 days, early8 late5. Explicit clarification identifies protocol page3 medians18/15 and points to page12 as intended8/5; retain this disclosed clarification. BSIDIII cognitive0.4SD=6 points,22–26 months corrected age. Baseline modifiers expected.  Page3: parallel-group1:1; early after medical optimization before discharge; late >55weeks and after discharge; center/GA (<28 / ≥28weeks) strata, permuted variable blocks, REDCap24/7. Multiple gestation first twin randomized; sibling assigned same arm. Main keys: intervention timing, allocation unit/strata/sibling dependence, hospital hypothesis disclosure.
- **Rule and calculation:** 30−20=10pp;8−5=3days;0.4×15=6;protocol18/15 vs8/5 clarification explicit;1:1 prospective allocation.
- **Check status:** F-NUM-002.

### N120

- **Source and role:** PLAN DOC-003; SUP-S02 Sample, interim and inference hierarchy.
- **Printed inputs and definitions:** [Pages 3–4](../../../joi240020supp2_prod_1710443209.75411.pdf#page=4):293/group586 assessed,80% power, two-sided alpha.05,95% follow-up,615 planned randomized. Hospital98% power, lognormal early median8 mean18; late median5 mean13. BSIDIII0.4SD6points with200. One formal primary-endpoint interim when200 randomized infants have10-month data; protocol14 stopping guidelines. Planned final586 outcomes. Retrospective note: enrollment stopped April2021 after interim97% probability of decreased SAE late, crossing95% efficacy threshold; interim primarily Bayesian.  Page4: complementary frequentist/Bayesian primary and important secondary death, total hospital days, BSIDIII. Bayesian primary, frequentist secondary; designation before final analyses. Frequentist treatment RR/RD/group mean differences and95% CI. Bayesian posterior medians,95% CrI, probability any benefit/harm and clinically important effect. Main keys: interim97%/95%, Bayesian priority, models/priors, credible versus confidence intervals and probabilistic direction.
- **Rule and calculation:** 293×2=586;97%>95%;615×[0.945,0.955]=[581.175,587.325], includes586;586/0.95=616.842 versus615 does not exceed precision threshold.
- **Check status:** NUMERIC_CHECK_COMPLETE.


