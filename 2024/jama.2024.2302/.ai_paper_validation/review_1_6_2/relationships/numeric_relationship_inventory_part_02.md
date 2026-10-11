# Numeric inventory part 2

Status: COMPLETE. Exact IDs N121, N122, N123, N124, N125, N126, N127, N128, N129, N130, N131, N132, N133, N134, N135, N136, N137, N138, N139, N140, N141, N142, N143, N144, N145, N146, N147, N148, N149, N150, N151, N152, N153, N154, N155, N156, N157, N158, N159, N160, N161, N162, N163, N164, N165. 45 grouped relationships. Sources and calculations below are complete English; values remain as printed. See canonical index for scope, precision rule and limitations.

### N121

- **Source and role:** PLAN DOC-003; SUP-S03 Analysis populations, follow-up and endpoints.
- **Printed inputs and definitions:** [Page 5](../../../joi240020supp2_prod_1710443209.75411.pdf#page=5): mITT all randomized with ascertained primary outcome; PP received randomized intervention plus determined primary outcome. Deviation counts/infants per arm summarized (timing not followed, other intervention, ineligible, no consent, strata issue, other). Eligibility matches protocol (<37weeks0days etc.). CONSORT includes eligible randomized/unrandomized, received/did not receive, lost/discontinued, analyzed/excluded with reasons.  [Page 6](../../../joi240020supp2_prod_1710443209.75411.pdf#page=6): no data after withdrawal, earlier data retained; missing follow-up can occur between discharge/late repair/10-month call and between10months and developmental22–26months. Baseline infant age(GA/PMA/chronological),sex,race,Hispanic,birthweight g,singleton,inborn,1/5-minute Apgar,previous operations,apnea/bradycardia,mechanical ventilation >24h,IVH grade/laterality,ROP/RDS/BPD/CLD/cardiac/NEC/SIP,reducibility,caffeine/steroids,respiratory status; maternal age,race,ethnicity,marital/education/parity,multiple birth,prenatal care,insurance,residence ZIP. Categorical n/%; continuous normal mean/SD/range, skewed median/IQR/range.  [Page 7](../../../joi240020supp2_prod_1710443209.75411.pdf#page=7): primary ANY SAE randomization through10months, protocol definitions and masked adjudication. Table3 complete list mirrors protocol condensed table (10 cardiorespiratory/anesthesia and8 surgery/IH rows). Secondary highest harm for ≥1SAE NCC MERP; total hospital days=randomization-to-discharge days+readmission days+postsurgical days; prolonged stay >30days postsurgery; NICU stay; postsurgery stay; IH repair occurred; BSIDIII cognitive; overall AE(any). Main keys: primary/composite and secondary statuses, hospital summation/window, prolonged-stay definition, neurodevelopment deferred result, highest harm, repair occurrence.
- **Rule and calculation:** Observed-primary159+149=308;PP definition different with no printed total;10months vs22–26months distinct windows. Hospital-day component periods explicit;medians need not add;SAP no observed numerical result display.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N122

- **Source and role:** PLAN DOC-003; SUP-S04 Models, effect measures, priors and computation.
- **Printed inputs and definitions:** [Pages 7–8](../../../joi240020supp2_prod_1710443209.75411.pdf#page=8): all outcomes by group; categorical n/%, counts median/IQR/mean/SD, continuous normal mean/SD. Same multilevel model for Bayesian/frequentist outcome. Binary logistic; ordinal proportional-odds logistic; count negative-binomial; continuous normal. Each random site intercept plus GA<28/≥28 covariate. Binary RR and RD calculated from logistic; count RR; ordinal OR; continuous mean group difference.95% CI/CrI. Probability any effect and at least3%/5% SAE risk reduction;10% hypothesized reduction. R, Stan via rstanarm/brms;3chains/model,≥5000 burn-in and≥50000 additional iterations/chain.  Categorical treatment neutral OR1, stated95%CrI0.2–4, Normal(mean0,SD0.7) on logOR. Count treatment neutral RR1,95%CrI0.33–3.3. Intercept Normal(0,SD10),GA Normal(0,SD1),site SD halfNormal(0,SD1). Continuous standardized outcome: treatment Normal(0,SD2),intercept Normal(0,SD10),GA Normal(0,SD3),siteSD halfNormal(0,SD2). No fully specified count-treatment log-scale SD supplied beyond the RR prior range. Residual plots for frequentist; three-chain trace,Geweke,Gelman/Rubin convergence; posterior predictive1000trials, average probabilities/counts/means by treatment and GA; observed values expected within simulation cloud. Main keys: effect-measure identity, statistical family/covariates/clustering, treatment prior range/scale, iterations and convergence.
- **Rule and calculation:** Logistic fitted RR/RD, ordinal OR, negative-binomial RR identities explicit;3chains×50000≥150000 retained iterations plus≥15000 burn-in;prior interval/scale retained for statistical lane, not crude count comparison.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N123

- **Source and role:** PLAN DOC-003; SUP-S05 Sensitivity/subgroups/association/missing data.
- **Printed inputs and definitions:** [SAP page 9](../../../joi240020supp2_prod_1710443209.75411.pdf#page=9): sensitivity covariate adjustment if important baseline imbalance, primary only, mITT, already adjusts GA/site. PP primary analysis in addition to mITT. Exploratory primary subgroup mITT; hierarchical interactions treatment with GA<28/≥28,BPD,maternal education≤12years,prenatal care,IH difficult to reduce; primary plus hospital days and BSIDIII. Main-effect priors as primary; interaction Normal(0,SD0.6); subgroup point effects,95%CrI,benefit/harm probability. Similar sex/race/ethnicity. Two additional exploratory moderators explicitly absent from trial protocol: laparoscopic/open repair and distance from home to facility. Continuous GA association: splines/polynomials assess linear/nonlinear best fit, all other primary model details retained, then interaction GA term/treatment via subgroup methods.  [Page 10](../../../joi240020supp2_prod_1710443209.75411.pdf#page=10): additional ad hoc analyses must be clearly labeled as motivated by planned analyses; no imputation for missing data; R. References opened, no independent result display. No prespecified multiple-imputation sensitivity or adjusted multiplicity decision is stated. Main keys: mITT/PP, conditional imbalance sensitivity, continuous GA interaction, specified subgroup results, missing outcomes exclusion versus imputation, ad hoc labels.
- **Rule and calculation:** No numerical unprinted sensitivity/subgroup outcome inferred;no imputation specified;planned moderator definitions retained.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N124

- **Source and role:** REPORT DOC-004; SUP-R01 eTable 1 enrollment reasons.
- **Printed inputs and definitions:** [Page 2](../../../joi240020supp3_prod_1710443209.75411.pdf#page=2), continued [page 3](../../../joi240020supp3_prod_1710443209.75411.pdf#page=3): site-level ineligibility because associated factor affecting timing. Unit is infants; no percentage printed and no section total printed. All22 rows:   /  Reason  /  Infants  /  PDF page  /   / --- / ---: / ---: /   /  Incarceration during NICU  /  10  /  2  /   /  Multiple prior abdominal operations  /  5  /  2  /   /  Severe respiratory disease  /  5  /  2  /   /  Hernia contains ovary, preferred early  /  4  /  2  /   /  Severe cardiac disease  /  4  /  2  /   /  Airway anomaly requiring operation  /  2  /  2  /   /  Research contact too close to discharge for enrollment  /  2  /  2  /   /  Associated undescended testicle  /  2  /  2  /   /  Viral upper respiratory infection  /  2  /  2  /   /  COVID restriction, no elective operation  /  2  /  2  /   /  Transfer closer to home/nonparticipating hospital  /  2  /  2  /   /  Anticoagulant therapy  /  1  /  2  /   /  Very large hernia, surgeon preferred early  /  1  /  2  /   /  Infant too small  /  1  /  2  /   /  Unsure hydrocele or hernia, prefer wait  /  1  /  2  /   /  Coordinate ophthalmology procedure  /  1  /  2  /   /  Coordinate neurosurgery/shunt  /  1  /  2  /   /  Planning G-tube  /  1  /  3  /   /  Severe pulmonary hypertension  /  1  /  3  /   /  Unexplained thrombocytopenia  /  1  /  3  /   /  Await stopping steroids  /  1  /  3  /   /  Hernia thought to cause feeding intolerance  /  1  /  3  /   [Page 3](../../../joi240020supp3_prod_1710443209.75411.pdf#page=3): parent/guardian refusal n613: early280,late196,physician decide71,no reason66. Physician refusal n37: early14,late14,no reason9. Other reasons eligible not consented n16: non-English/only English forms4,COVID4,custody3 (page3); incarceration concerns NICU2,insurance1,medically unstable1,transfer cardiac surgery1 ([page4](../../../joi240020supp3_prod_1710443209.75411.pdf#page=4)). These14 refusal/other rows plus22 ineligibility rows are complete. Main matching key: participant-flow exclusions/refusal categories and enrollment population; do not use these as outcome denominators.
- **Rule and calculation:** Ineligibility counts sum51:10+5+5+4+4+six2+eleven1. Refusal280+196+71+66=613;physician14+14+9=37;other4+4+3+2+1+1+1=16;all36 rows checked against flow.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N125

- **Source and role:** REPORT DOC-004; SUP-R02 eTable 2 frequentist analyses and complete footnote.
- **Printed inputs and definitions:** [Page 5](../../../joi240020supp3_prod_1710443209.75411.pdf#page=5). Headings: Early Repair n159; Late Repair n149; risk difference (95% confidence interval), P value; relative risk (95% confidence interval), P value. These are frequentist confidence intervals, not Bayesian credible intervals. Late versus early direction is negative RD / RR below1 for lower late risk.   /  Status/outcome  /  Early  /  Late  /  RD (95% CI)  /  RD P  /  RR (95% CI)  /  RR P  /   / --- / --- / --- / --- / --- / --- / --- /   /  Primary: Infant had ≥1 SAE  /  44 (28%)  /  27 (18%)  /  −9.0% (−16.5%, −2.0%)  /  .01  /  0.65 (0.46–0.92)  /  .01  /   /  Secondary: Total hospital days during study period, median(IQR)  /  19.0 (9.8,35)  /  16.0 (7,38)  /  blank  /  blank  /  0.91 (0.74–1.12)  /  .36  /   Footnote begins logistic mixed-effect primary model, negative-binomial mixed hospital-days model; all models GA-group covariate and center random intercept. Then explicitly excepts frequentist primary analysis: generalized estimating equation logistic, exchangeable center correlation, due to mixed-model nonconvergence. Bayesian and frequentist otherwise same models. Participating centers large pediatric facilities with surgical services/almost all university affiliated; surgeons pediatric general/thoracic, no pediatric urologists; surgeon counts varied but no numeric range; site infant counts below. All footnote statements retained; no diagnosis assigned. Main keys: primary any-SAE10-month mITT counts44/159 and27/149; primary Bayesian comparator/RR/RD; total hospital days median/IQR/RR; GEE versus mixed model disclosure.
- **Rule and calculation:** 44/159=27.673%,27/149=18.121% overlap28±0.5%/18±0.5%;frequentist RR0.65 model-derived, not OR0.578428;hospital RR0.91 negative-binomial not16/19;counts match main.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N126

- **Source and role:** REPORT DOC-004; SUP-R03 eTable 3 full enrollment by center.
- **Printed inputs and definitions:** [Page 6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6): column unit No.(%); Early Repair n172; Late Repair n166; Overall N338. These are randomized enrollment denominators, distinct from eTable2 analyzed159/149. All39 center rows follow; percentages are printed, not recalculated.   /  Center  /  Early n(%)  /  Late n(%)  /  Overall n(%)  /   / --- / --- / --- / --- /   /  Akron Children's Hospital  /  2 (1.2%)  /  2 (1.2%)  /  4 (1.2%)  /   /  Albany Medical Center  /  4 (2.3%)  /  2 (1.2%)  /  6 (1.8%)  /   /  All Children's Johns Hopkins  /  3 (1.7%)  /  4 (2.4%)  /  7 (2.1%)  /   /  Amplatz Children's Hospital  /  5 (2.9%)  /  5 (3.0%)  /  10 (3.0%)  /   /  Arkansas Children's Hospital  /  16 (9.3%)  /  17 (10%)  /  33 (9.8%)  /   /  Cardinal Glennon/SLU  /  7 (4.1%)  /  5 (3.0%)  /  12 (3.6%)  /   /  Children's Hospital of Alabama  /  3 (1.7%)  /  3 (1.8%)  /  6 (1.8%)  /   /  Children's Hospital of Wisconsin  /  2 (1.2%)  /  0 (0%)  /  2 (0.6%)  /   /  Children's Memorial Hermann Hospital  /  7 (4.1%)  /  8 (4.8%)  /  15 (4.4%)  /   /  Cincinnati Children's Hospital  /  2 (1.2%)  /  0 (0%)  /  2 (0.6%)  /   /  Cohen Children's Medical Center  /  0 (0%)  /  1 (0.6%)  /  1 (0.3%)  /   /  Columbia University Medical Center  /  5 (2.9%)  /  5 (3.0%)  /  10 (3.0%)  /   /  Connecticut Children's Medical Center  /  4 (2.3%)  /  4 (2.4%)  /  8 (2.4%)  /   /  Dartmouth-Hitchcock Medical Center  /  2 (1.2%)  /  0 (0%)  /  2 (0.6%)  /   /  Dayton Children's Hospital  /  5 (2.9%)  /  5 (3.0%)  /  10 (3.0%)  /   /  Duke Children's Hospital  /  11 (6.4%)  /  9 (5.4%)  /  20 (5.9%)  /   /  Erlanger/UT Chattanooga  /  11 (6.4%)  /  10 (6.0%)  /  21 (6.2%)  /   /  Le Bonheur Children's Hospital  /  8 (4.7%)  /  8 (4.8%)  /  16 (4.7%)  /   /  Medical University of South Carolina Children's Hospital  /  7 (4.1%)  /  7 (4.2%)  /  14 (4.1%)  /   /  Nationwide Children's Hospital  /  9 (5.2%)  /  8 (4.8%)  /  17 (5.0%)  /   /  Naval Medical Center San Diego  /  1 (0.6%)  /  2 (1.2%)  /  3 (0.9%)  /   /  Penn State Milton S. Hershey MC  /  0 (0%)  /  1 (0.6%)  /  1 (0.3%)  /   /  Rady Children's Hospital/UCSD  /  1 (0.6%)  /  1 (0.6%)  /  2 (0.6%)  /   /  Seattle Children's Hospital  /  1 (0.6%)  /  0 (0%)  /  1 (0.3%)  /   /  Shands Hospital for Children  /  1 (0.6%)  /  1 (0.6%)  /  2 (0.6%)  /   /  Southern California Permanente Group  /  6 (3.5%)  /  7 (4.2%)  /  13 (3.8%)  /   /  St. Louis Children's Hospital  /  2 (1.2%)  /  1 (0.6%)  /  3 (0.9%)  /   /  Texas Children's Hospital  /  3 (1.7%)  /  1 (0.6%)  /  4 (1.2%)  /   /  Tufts University  /  1 (0.6%)  /  2 (1.2%)  /  3 (0.9%)  /   /  UCLA  /  1 (0.6%)  /  2 (1.2%)  /  3 (0.9%)  /   /  UCLA-Harbor  /  1 (0.6%)  /  2 (1.2%)  /  3 (0.9%)  /   /  University of Iowa Children's Hospital  /  11 (6.4%)  /  13 (7.8%)  /  24 (7.1%)  /   /  University of Nebraska Medical Center  /  0 (0%)  /  1 (0.6%)  /  1 (0.3%)  /   /  University of Virginia  /  3 (1.7%)  /  4 (2.4%)  /  7 (2.1%)  /   /  Utah/Primary Children's  /  3 (1.7%)  /  3 (1.8%)  /  6 (1.8%)  /   /  Valley Children's  /  4 (2.3%)  /  2 (1.2%)  /  6 (1.8%)  /   /  Vanderbilt Children's Hospital  /  11 (6.4%)  /  13 (7.8%)  /  24 (7.1%)  /   /  Women & Children's Hospital of Buffalo  /  6 (3.5%)  /  6 (3.6%)  /  12 (3.6%)  /   /  Women & Infants Hospital Rhode Island  /  3 (1.7%)  /  1 (0.6%)  /  4 (1.2%)  /   Main matching key: randomized totals172/166/338, center/random-effect structure and participant-flow population. No other footnote or total row on page6.
- **Rule and calculation:** All 39 center rows sum to early 172, late 166 and overall 338; 172+166=338. Each row early+late=overall, with row-specific count and percentage checks in N127 through N165. These enrollment denominators are distinct from analyzed 159/149 in eTable 2.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N127

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Akron Children's Hospital.
- **Printed inputs and definitions:** Early 2 (1.2%);late 2 (1.2%);overall 4 (1.2%);denominators172/166/338
- **Rule and calculation:** 2+2=4. 2/172×100=1.162791%;printed[1.150,1.250]%;gap=0.000000,relative=0.000000. 2/166×100=1.204819%;printed[1.150,1.250]%;gap=0.000000,relative=0.000000. 4/338×100=1.183432%;printed[1.150,1.250]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N128

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Albany Medical Center.
- **Printed inputs and definitions:** Early 4 (2.3%);late 2 (1.2%);overall 6 (1.8%);denominators172/166/338
- **Rule and calculation:** 4+2=6. 4/172×100=2.325581%;printed[2.250,2.350]%;gap=0.000000,relative=0.000000. 2/166×100=1.204819%;printed[1.150,1.250]%;gap=0.000000,relative=0.000000. 6/338×100=1.775148%;printed[1.750,1.850]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N129

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 All Children's Johns Hopkins.
- **Printed inputs and definitions:** Early 3 (1.7%);late 4 (2.4%);overall 7 (2.1%);denominators172/166/338
- **Rule and calculation:** 3+4=7. 3/172×100=1.744186%;printed[1.650,1.750]%;gap=0.000000,relative=0.000000. 4/166×100=2.409639%;printed[2.350,2.450]%;gap=0.000000,relative=0.000000. 7/338×100=2.071006%;printed[2.050,2.150]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N130

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Amplatz Children's Hospital.
- **Printed inputs and definitions:** Early 5 (2.9%);late 5 (3.0%);overall 10 (3.0%);denominators172/166/338
- **Rule and calculation:** 5+5=10. 5/172×100=2.906977%;printed[2.850,2.950]%;gap=0.000000,relative=0.000000. 5/166×100=3.012048%;printed[2.950,3.050]%;gap=0.000000,relative=0.000000. 10/338×100=2.958580%;printed[2.950,3.050]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N131

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Arkansas Children's Hospital.
- **Printed inputs and definitions:** Early 16 (9.3%);late 17 (10%);overall 33 (9.8%);denominators172/166/338
- **Rule and calculation:** 16+17=33. 16/172×100=9.302326%;printed[9.250,9.350]%;gap=0.000000,relative=0.000000. 17/166×100=10.240964%;printed[9.500,10.500]%;gap=0.000000,relative=0.000000. 33/338×100=9.763314%;printed[9.750,9.850]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N132

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Cardinal Glennon/SLU.
- **Printed inputs and definitions:** Early 7 (4.1%);late 5 (3.0%);overall 12 (3.6%);denominators172/166/338
- **Rule and calculation:** 7+5=12. 7/172×100=4.069767%;printed[4.050,4.150]%;gap=0.000000,relative=0.000000. 5/166×100=3.012048%;printed[2.950,3.050]%;gap=0.000000,relative=0.000000. 12/338×100=3.550296%;printed[3.550,3.650]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N133

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Children's Hospital of Alabama.
- **Printed inputs and definitions:** Early 3 (1.7%);late 3 (1.8%);overall 6 (1.8%);denominators172/166/338
- **Rule and calculation:** 3+3=6. 3/172×100=1.744186%;printed[1.650,1.750]%;gap=0.000000,relative=0.000000. 3/166×100=1.807229%;printed[1.750,1.850]%;gap=0.000000,relative=0.000000. 6/338×100=1.775148%;printed[1.750,1.850]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N134

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Children's Hospital of Wisconsin.
- **Printed inputs and definitions:** Early 2 (1.2%);late 0 (0%);overall 2 (0.6%);denominators172/166/338
- **Rule and calculation:** 2+0=2. 2/172×100=1.162791%;printed[1.150,1.250]%;gap=0.000000,relative=0.000000. 0/166×100=0.000000%;printed[-0.500,0.500]%;gap=0.000000,relative=0.000000. 2/338×100=0.591716%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N135

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Children's Memorial Hermann Hospital.
- **Printed inputs and definitions:** Early 7 (4.1%);late 8 (4.8%);overall 15 (4.4%);denominators172/166/338
- **Rule and calculation:** 7+8=15. 7/172×100=4.069767%;printed[4.050,4.150]%;gap=0.000000,relative=0.000000. 8/166×100=4.819277%;printed[4.750,4.850]%;gap=0.000000,relative=0.000000. 15/338×100=4.437870%;printed[4.350,4.450]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N136

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Cincinnati Children's Hospital.
- **Printed inputs and definitions:** Early 2 (1.2%);late 0 (0%);overall 2 (0.6%);denominators172/166/338
- **Rule and calculation:** 2+0=2. 2/172×100=1.162791%;printed[1.150,1.250]%;gap=0.000000,relative=0.000000. 0/166×100=0.000000%;printed[-0.500,0.500]%;gap=0.000000,relative=0.000000. 2/338×100=0.591716%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N137

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Cohen Children's Medical Center.
- **Printed inputs and definitions:** Early 0 (0%);late 1 (0.6%);overall 1 (0.3%);denominators172/166/338
- **Rule and calculation:** 0+1=1. 0/172×100=0.000000%;printed[-0.500,0.500]%;gap=0.000000,relative=0.000000. 1/166×100=0.602410%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000. 1/338×100=0.295858%;printed[0.250,0.350]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N138

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Columbia University Medical Center.
- **Printed inputs and definitions:** Early 5 (2.9%);late 5 (3.0%);overall 10 (3.0%);denominators172/166/338
- **Rule and calculation:** 5+5=10. 5/172×100=2.906977%;printed[2.850,2.950]%;gap=0.000000,relative=0.000000. 5/166×100=3.012048%;printed[2.950,3.050]%;gap=0.000000,relative=0.000000. 10/338×100=2.958580%;printed[2.950,3.050]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N139

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Connecticut Children's Medical Center.
- **Printed inputs and definitions:** Early 4 (2.3%);late 4 (2.4%);overall 8 (2.4%);denominators172/166/338
- **Rule and calculation:** 4+4=8. 4/172×100=2.325581%;printed[2.250,2.350]%;gap=0.000000,relative=0.000000. 4/166×100=2.409639%;printed[2.350,2.450]%;gap=0.000000,relative=0.000000. 8/338×100=2.366864%;printed[2.350,2.450]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N140

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Dartmouth-Hitchcock Medical Center.
- **Printed inputs and definitions:** Early 2 (1.2%);late 0 (0%);overall 2 (0.6%);denominators172/166/338
- **Rule and calculation:** 2+0=2. 2/172×100=1.162791%;printed[1.150,1.250]%;gap=0.000000,relative=0.000000. 0/166×100=0.000000%;printed[-0.500,0.500]%;gap=0.000000,relative=0.000000. 2/338×100=0.591716%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N141

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Dayton Children's Hospital.
- **Printed inputs and definitions:** Early 5 (2.9%);late 5 (3.0%);overall 10 (3.0%);denominators172/166/338
- **Rule and calculation:** 5+5=10. 5/172×100=2.906977%;printed[2.850,2.950]%;gap=0.000000,relative=0.000000. 5/166×100=3.012048%;printed[2.950,3.050]%;gap=0.000000,relative=0.000000. 10/338×100=2.958580%;printed[2.950,3.050]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N142

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Duke Children's Hospital.
- **Printed inputs and definitions:** Early 11 (6.4%);late 9 (5.4%);overall 20 (5.9%);denominators172/166/338
- **Rule and calculation:** 11+9=20. 11/172×100=6.395349%;printed[6.350,6.450]%;gap=0.000000,relative=0.000000. 9/166×100=5.421687%;printed[5.350,5.450]%;gap=0.000000,relative=0.000000. 20/338×100=5.917160%;printed[5.850,5.950]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N143

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Erlanger/UT Chattanooga.
- **Printed inputs and definitions:** Early 11 (6.4%);late 10 (6.0%);overall 21 (6.2%);denominators172/166/338
- **Rule and calculation:** 11+10=21. 11/172×100=6.395349%;printed[6.350,6.450]%;gap=0.000000,relative=0.000000. 10/166×100=6.024096%;printed[5.950,6.050]%;gap=0.000000,relative=0.000000. 21/338×100=6.213018%;printed[6.150,6.250]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N144

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Le Bonheur Children's Hospital.
- **Printed inputs and definitions:** Early 8 (4.7%);late 8 (4.8%);overall 16 (4.7%);denominators172/166/338
- **Rule and calculation:** 8+8=16. 8/172×100=4.651163%;printed[4.650,4.750]%;gap=0.000000,relative=0.000000. 8/166×100=4.819277%;printed[4.750,4.850]%;gap=0.000000,relative=0.000000. 16/338×100=4.733728%;printed[4.650,4.750]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N145

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Medical University of South Carolina Children's Hospital.
- **Printed inputs and definitions:** Early 7 (4.1%);late 7 (4.2%);overall 14 (4.1%);denominators172/166/338
- **Rule and calculation:** 7+7=14. 7/172×100=4.069767%;printed[4.050,4.150]%;gap=0.000000,relative=0.000000. 7/166×100=4.216867%;printed[4.150,4.250]%;gap=0.000000,relative=0.000000. 14/338×100=4.142012%;printed[4.050,4.150]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N146

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Nationwide Children's Hospital.
- **Printed inputs and definitions:** Early 9 (5.2%);late 8 (4.8%);overall 17 (5.0%);denominators172/166/338
- **Rule and calculation:** 9+8=17. 9/172×100=5.232558%;printed[5.150,5.250]%;gap=0.000000,relative=0.000000. 8/166×100=4.819277%;printed[4.750,4.850]%;gap=0.000000,relative=0.000000. 17/338×100=5.029586%;printed[4.950,5.050]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N147

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Naval Medical Center San Diego.
- **Printed inputs and definitions:** Early 1 (0.6%);late 2 (1.2%);overall 3 (0.9%);denominators172/166/338
- **Rule and calculation:** 1+2=3. 1/172×100=0.581395%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000. 2/166×100=1.204819%;printed[1.150,1.250]%;gap=0.000000,relative=0.000000. 3/338×100=0.887574%;printed[0.850,0.950]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N148

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Penn State Milton S. Hershey MC.
- **Printed inputs and definitions:** Early 0 (0%);late 1 (0.6%);overall 1 (0.3%);denominators172/166/338
- **Rule and calculation:** 0+1=1. 0/172×100=0.000000%;printed[-0.500,0.500]%;gap=0.000000,relative=0.000000. 1/166×100=0.602410%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000. 1/338×100=0.295858%;printed[0.250,0.350]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N149

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Rady Children's Hospital/UCSD.
- **Printed inputs and definitions:** Early 1 (0.6%);late 1 (0.6%);overall 2 (0.6%);denominators172/166/338
- **Rule and calculation:** 1+1=2. 1/172×100=0.581395%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000. 1/166×100=0.602410%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000. 2/338×100=0.591716%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N150

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Seattle Children's Hospital.
- **Printed inputs and definitions:** Early 1 (0.6%);late 0 (0%);overall 1 (0.3%);denominators172/166/338
- **Rule and calculation:** 1+0=1. 1/172×100=0.581395%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000. 0/166×100=0.000000%;printed[-0.500,0.500]%;gap=0.000000,relative=0.000000. 1/338×100=0.295858%;printed[0.250,0.350]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N151

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Shands Hospital for Children.
- **Printed inputs and definitions:** Early 1 (0.6%);late 1 (0.6%);overall 2 (0.6%);denominators172/166/338
- **Rule and calculation:** 1+1=2. 1/172×100=0.581395%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000. 1/166×100=0.602410%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000. 2/338×100=0.591716%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N152

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Southern California Permanente Group.
- **Printed inputs and definitions:** Early 6 (3.5%);late 7 (4.2%);overall 13 (3.8%);denominators172/166/338
- **Rule and calculation:** 6+7=13. 6/172×100=3.488372%;printed[3.450,3.550]%;gap=0.000000,relative=0.000000. 7/166×100=4.216867%;printed[4.150,4.250]%;gap=0.000000,relative=0.000000. 13/338×100=3.846154%;printed[3.750,3.850]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N153

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 St. Louis Children's Hospital.
- **Printed inputs and definitions:** Early 2 (1.2%);late 1 (0.6%);overall 3 (0.9%);denominators172/166/338
- **Rule and calculation:** 2+1=3. 2/172×100=1.162791%;printed[1.150,1.250]%;gap=0.000000,relative=0.000000. 1/166×100=0.602410%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000. 3/338×100=0.887574%;printed[0.850,0.950]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N154

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Texas Children's Hospital.
- **Printed inputs and definitions:** Early 3 (1.7%);late 1 (0.6%);overall 4 (1.2%);denominators172/166/338
- **Rule and calculation:** 3+1=4. 3/172×100=1.744186%;printed[1.650,1.750]%;gap=0.000000,relative=0.000000. 1/166×100=0.602410%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000. 4/338×100=1.183432%;printed[1.150,1.250]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N155

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Tufts University.
- **Printed inputs and definitions:** Early 1 (0.6%);late 2 (1.2%);overall 3 (0.9%);denominators172/166/338
- **Rule and calculation:** 1+2=3. 1/172×100=0.581395%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000. 2/166×100=1.204819%;printed[1.150,1.250]%;gap=0.000000,relative=0.000000. 3/338×100=0.887574%;printed[0.850,0.950]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N156

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 UCLA.
- **Printed inputs and definitions:** Early 1 (0.6%);late 2 (1.2%);overall 3 (0.9%);denominators172/166/338
- **Rule and calculation:** 1+2=3. 1/172×100=0.581395%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000. 2/166×100=1.204819%;printed[1.150,1.250]%;gap=0.000000,relative=0.000000. 3/338×100=0.887574%;printed[0.850,0.950]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N157

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 UCLA-Harbor.
- **Printed inputs and definitions:** Early 1 (0.6%);late 2 (1.2%);overall 3 (0.9%);denominators172/166/338
- **Rule and calculation:** 1+2=3. 1/172×100=0.581395%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000. 2/166×100=1.204819%;printed[1.150,1.250]%;gap=0.000000,relative=0.000000. 3/338×100=0.887574%;printed[0.850,0.950]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N158

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 University of Iowa Children's Hospital.
- **Printed inputs and definitions:** Early 11 (6.4%);late 13 (7.8%);overall 24 (7.1%);denominators172/166/338
- **Rule and calculation:** 11+13=24. 11/172×100=6.395349%;printed[6.350,6.450]%;gap=0.000000,relative=0.000000. 13/166×100=7.831325%;printed[7.750,7.850]%;gap=0.000000,relative=0.000000. 24/338×100=7.100592%;printed[7.050,7.150]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N159

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 University of Nebraska Medical Center.
- **Printed inputs and definitions:** Early 0 (0%);late 1 (0.6%);overall 1 (0.3%);denominators172/166/338
- **Rule and calculation:** 0+1=1. 0/172×100=0.000000%;printed[-0.500,0.500]%;gap=0.000000,relative=0.000000. 1/166×100=0.602410%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000. 1/338×100=0.295858%;printed[0.250,0.350]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N160

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 University of Virginia.
- **Printed inputs and definitions:** Early 3 (1.7%);late 4 (2.4%);overall 7 (2.1%);denominators172/166/338
- **Rule and calculation:** 3+4=7. 3/172×100=1.744186%;printed[1.650,1.750]%;gap=0.000000,relative=0.000000. 4/166×100=2.409639%;printed[2.350,2.450]%;gap=0.000000,relative=0.000000. 7/338×100=2.071006%;printed[2.050,2.150]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N161

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Utah/Primary Children's.
- **Printed inputs and definitions:** Early 3 (1.7%);late 3 (1.8%);overall 6 (1.8%);denominators172/166/338
- **Rule and calculation:** 3+3=6. 3/172×100=1.744186%;printed[1.650,1.750]%;gap=0.000000,relative=0.000000. 3/166×100=1.807229%;printed[1.750,1.850]%;gap=0.000000,relative=0.000000. 6/338×100=1.775148%;printed[1.750,1.850]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N162

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Valley Children's.
- **Printed inputs and definitions:** Early 4 (2.3%);late 2 (1.2%);overall 6 (1.8%);denominators172/166/338
- **Rule and calculation:** 4+2=6. 4/172×100=2.325581%;printed[2.250,2.350]%;gap=0.000000,relative=0.000000. 2/166×100=1.204819%;printed[1.150,1.250]%;gap=0.000000,relative=0.000000. 6/338×100=1.775148%;printed[1.750,1.850]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N163

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Vanderbilt Children's Hospital.
- **Printed inputs and definitions:** Early 11 (6.4%);late 13 (7.8%);overall 24 (7.1%);denominators172/166/338
- **Rule and calculation:** 11+13=24. 11/172×100=6.395349%;printed[6.350,6.450]%;gap=0.000000,relative=0.000000. 13/166×100=7.831325%;printed[7.750,7.850]%;gap=0.000000,relative=0.000000. 24/338×100=7.100592%;printed[7.050,7.150]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N164

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Women & Children's Hospital of Buffalo.
- **Printed inputs and definitions:** Early 6 (3.5%);late 6 (3.6%);overall 12 (3.6%);denominators172/166/338
- **Rule and calculation:** 6+6=12. 6/172×100=3.488372%;printed[3.450,3.550]%;gap=0.000000,relative=0.000000. 6/166×100=3.614458%;printed[3.550,3.650]%;gap=0.000000,relative=0.000000. 12/338×100=3.550296%;printed[3.550,3.650]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.

### N165

- **Source and role:** REPORT [DOC-004 p.6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6), eTable3 Women & Infants Hospital Rhode Island.
- **Printed inputs and definitions:** Early 3 (1.7%);late 1 (0.6%);overall 4 (1.2%);denominators172/166/338
- **Rule and calculation:** 3+1=4. 3/172×100=1.744186%;printed[1.650,1.750]%;gap=0.000000,relative=0.000000. 1/166×100=0.602410%;printed[0.550,0.650]%;gap=0.000000,relative=0.000000. 4/338×100=1.183432%;printed[1.150,1.250]%;gap=0.000000,relative=0.000000.
- **Check status:** NUMERIC_CHECK_COMPLETE.


