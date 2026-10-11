# Support quantitative evidence, shard 1

Exact assigned scope: DOC-002, `joi180075supp1_prod.pdf`, physical PDF pages 1–32 inclusive. Document role: PLAN throughout, including background, recruitment, measurement, and COPTR blinding policy. Status: COMPLETE, 32/32 assigned units inspected. This is extraction and relationship mapping only; no candidate diagnosis or selection is performed. Local keys `SUP1-*` are distinct shard keys for the coordinator's global numeric/statistical inventory.

Evidence used: source-matched reusable native/layout text `.ai_paper_validation/review_1_5_2/preprocessing/{native_text,layout_text}/joi180075supp1_prod.txt`, split at form feeds with direct `awk`. The curator confirms current source/native equivalence. Every assigned page was opened in its page-bounded layout representation. The embedded design graphic on physical page 13 was additionally inspected from a fresh direct source rendering: `pdftoppm -f 13 -l 13 -singlefile -scale-to 1600 -png joi180075supp1_prod.pdf .ai_paper_validation/review_1_6_1/preprocessing/support001-p013`, Poppler 25.03.0, CPU. Derivative: `preprocessing/support001-p013.png`. No new OCR required; no sources or reused assets modified. References below use physical PDF page numbers and four parent traversals to the package root.

## Page-by-page coverage

| Physical page | Inspected content | Result-relevant mapping / explicit applicability | Status |
|---|---|---|---|
| 1 | Protocol bundle cover | Original/revised protocol, amendments, original/final analysis plan; PLAN identity. No applicable quantitative result. | COMPLETE |
| 2 | Table of contents | Original protocol section pointers; no applicable quantitative result or design input beyond locators. | COMPLETE |
| 3 | Table of contents | Original analysis section and revised protocol pointers; no applicable quantitative result beyond locators. | COMPLETE |
| 4 | Table of contents | Revised analysis section and SAP pointers; no applicable quantitative result beyond locators. | COMPLETE |
| 5 | Original protocol specific aims | SUP1-01, SUP1-02: primary child BMI trajectory and secondary behavior hypotheses. | COMPLETE |
| 6 | Aims 5–6 and background | SUP1-03: genetic moderation/program count hypotheses; SUP1-04 target BMI categories; historical background recorded separately. | COMPLETE |
| 7 | Family/physical-environment background | Historical quantities only; no applicable trial estimate, model, or decision rule. | COMPLETE |
| 8 | Social/genetic background | Historical statistical claims recorded separately; SUP1-05 genetic score construction begins. | COMPLETE |
| 9 | Genetic score and recruitment | SUP1-05 score range; SUP1-06 sample target/cohorts/follow-up. | COMPLETE |
| 10 | Recruitment operations | Pilot screening counts and recruitment frame recorded separately; no trial result or additional analysis specification. | COMPLETE |
| 11 | Consent and eligibility | SUP1-07 baseline BMI/age/measurement eligibility and unit. | COMPLETE |
| 12 | Eligibility, exclusions, procedural overview | SUP1-07, SUP1-08 baseline requirements and language stratification. Figure heading precedes diagram on p13. | COMPLETE |
| 13 | GROW RCT design diagram and cohort allocation | Direct visual inspection; SUP1-06, SUP1-09, SUP1-10: 600/300/300, 3 cohorts, doses/time points, group-size/added-control-curriculum footnotes. | COMPLETE |
| 14 | Table 1 timeline; intervention/control phases | SUP1-09, SUP1-10: every timeline row and intervention duration. | COMPLETE |
| 15 | Control curriculum; six collection times; adaptive intervention | SUP1-10, SUP1-11: time mapping and BMI category worsening rule. | COMPLETE |
| 16 | Primary/secondary outcomes Tables 2–3 | SUP1-12, SUP1-13: child BMI percentile trajectory, parent BMI and adiposity measurements. | COMPLETE |
| 17 | Moderator/mediator Table 4 | SUP1-14, SUP1-15: activity/diet units, valid wear, collection times. | COMPLETE |
| 18 | Table 4 continuation | SUP1-16: nutrition/social/cohesion/advice/feeding scales and schedules. | COMPLETE |
| 19 | Table 4 continuation | SUP1-16: family meal/sleep/media/center/environment/stress scales and schedules. | COMPLETE |
| 20 | Table 4 continuation | SUP1-16: depression/goals/executive function/literacy/weight/self-efficacy/demographics/genotype/perinatal/literacy/food security. | COMPLETE |
| 21 | Table 4 completion; process and anthropometry | SUP1-16, SUP1-17, SUP1-18: food security/intelligence, CES-D threshold, process definitions, measurement arithmetic. | COMPLETE |
| 22 | Skinfold, accelerometry, dietary recall | SUP1-19, SUP1-20, SUP1-21: precision/repeat rules, activity quantities, dietary inclusion/window. | COMPLETE |
| 23 | Dietary exclusions; questionnaire; genetic collection; control measures | SUP1-21, SUP1-22: dietary thresholds/software, instrument/genetic/child-task definitions. | COMPLETE |
| 24 | Intelligence; incentives Tables 5–6 | SUP1-22, SUP1-23: collection-payment structure, completion footnote, intensive-session/group counts. | COMPLETE |
| 25 | Incentive continuation; control incentives; center membership | SUP1-23, SUP1-24: intervention/control incentives, dose-linked rewards, membership exposure. | COMPLETE |
| 26 | Membership continuation; blocked randomization | SUP1-24, SUP1-25: intervention exposure and four schedules/block maximum. | COMPLETE |
| 27 | Randomization management; risk/benefit | SUP1-26 assignment/masking mechanics; no new trial count/model. | COMPLETE |
| 28 | Safety data management/adverse event assessment | SUP1-27: enrollment/time-point assessments and possible/probable attribution thresholds. | COMPLETE |
| 29 | Definite attribution; COPTR blinding policy | SUP1-27, SUP1-28: attribution ≥4, definition of start/end/interim. | COMPLETE |
| 30 | Individual/arm data access and interim blinding | SUP1-28: aggregated OMM restrictions; no numeric efficacy stopping boundary. | COMPLETE |
| 31 | Table 7 masking and independent statistician | SUP1-28: complete masking table; no quantitative outcome estimate. | COMPLETE |
| 32 | Site/RCU statistician responsibilities | SUP1-28: common/site-specific interim access and report responsibilities. | COMPLETE |

Initial inventory assigned all pages as reusable-backed. Mapping found page 13 has a partial native/layout derivative: the entire embedded graphic is omitted. Final scientific coverage is 31 reusable-backed pages plus 1 fresh-required page (p13), all 32 mapped. The fresh rendering and direct visual inspection close that gap. No scientific coverage gap remains within this shard. Statistical model, covariance, missing-data, power, multiplicity, and efficacy stopping specifications occur outside the assigned scope according to the contents; no absence is inferred for the complete bundle.

## Prospective relationships and matching main-paper keys

### SUP1-01 — Primary aim and hypothesis

[PDF p5, lines107–114](../../../../joi180075supp1_prod.pdf#page=5): one primary and five secondary aims. Aim1 tests efficacy of multilevel nutrition/physical-activity intervention at public recreation centers in high-risk parent–preschool child dyads (child ages3–5). Hypothesis1: treatment children's BMI trajectories accelerate at a slower rate than control over time. Population/unit: child nested in enrolled parent–child dyad; contrast treatment versus control; direction slower BMI acceleration. Matching main-paper key: primary outcome child BMI trajectory over36months and trajectory/group-by-time test, distinct from any endpoint BMI contrast. No test statistic, effect estimate, confidence level, or model is printed here.

### SUP1-02 — Behavior, parental change, and social-network hypotheses

[PDF p5, lines116–146](../../../../joi180075supp1_prod.pdf#page=5): Aim2 compares intervention effect in children whose parents significantly change dietary/activity behavior versus those whose parents do not. H2 treatment versus control children: lower sedentary activity by actigraphy after intensive phase T2 and at completion; better adherence to age-specific USDA recommendations at T2 and completion, including total calories, fruit/vegetables, and sugar-sweetened beverages by diet recall. Aim3/H3 compares children of parents with significantly decreased sedentary activity and improved USDA adherence versus parents without those changes; expected child outcomes decreased post-treatment sedentary activity and better dietary adherence. Aim4/H4 expects new parental treatment-group social networks, strength positively associated with less sedentary activity and improved dietary behavior in both parents and children. No numeric significance threshold or analysis model appears on this page. Matching keys: child/parent physical activity and energy/diet outcomes, behavior-mediated intervention effect, network mediation.

### SUP1-03 — Genetic moderation and center programming hypotheses

[PDF p6, lines148–160](../../../../joi180075supp1_prod.pdf#page=6): Aim5/H5 higher child genetic susceptibility (higher genetic risk score) associated with heavier-for-age baseline BMI and moderates BMI growth over study. Aim6/H6 two participating Metro centers expected to implement more activity/nutrition programs for young-child families at completion than nonparticipating centers. Genetic moderator matches BMI trajectory interaction/subgroup keys; program-count hypothesis uses center as measurement unit, not child BMI analysis unit. No statistical procedure or numeric significance threshold here.

### SUP1-04 — BMI target and category boundaries

[PDF p6, lines182–185](../../../../joi180075supp1_prod.pdf#page=6): normal BMI expressed as >50% and <85%; improvement target BMI ≥85% and <95%, ages3–5. [PDF p11, lines380–383,405–421](../../../../joi180075supp1_prod.pdf#page=11) uses eligible BMI ≥50% and <95%; [PDF p12, lines438–460](../../../../joi180075supp1_prod.pdf#page=12) repeats exclusion <50% or ≥95% and inclusion ≥50% and <95%. Preserve each printed boundary and percentile notation. Matching keys: baseline eligibility percentile, normal/overweight/obese categories and intervention population. These are plan statements, not measured cohort percentages.

### SUP1-05 — Genetic risk score

[PDF p8, lines275–285](../../../../joi180075supp1_prod.pdf#page=8) and [p9, lines286–288](../../../../joi180075supp1_prod.pdf#page=9): eight obesity-related genes/risk loci, zero/one/two risk alleles at each autosomal locus, sum yields GRS0–16. Text says genes on different chromosomes/unlinked and treated as an independent variable. Highest score calculation:8loci×2alleles=16. GRS is prospective moderator identified in SUP1-03; source also provides historical genetic findings, separately catalogued below. No risk weights, fitted coefficient, or study-sample genotype result in assigned pages.

### SUP1-06 — Recruitment/sample size and planned allocation

[PDF p9, lines316–323](../../../../joi180075supp1_prod.pdf#page=9): target600 adult–preschool-child dyads, three-year participation, 3cohorts×200dyads with200 recruited annually for first3years. [PDF p13, graphic and lines468–476](../../../../joi180075supp1_prod.pdf#page=13): N600 parent–child dyads from two Nashville regions randomly assigned; intervention N300, control N300. Each cohort:100intervention+100control=200; two recreation centers and two libraries,50dyads per site per cohort. Within-site dyads subdivided by group-session availability. Recruitment/study cohorts staggered over a5-year span. Graphic names intervention Region1 East Community Center and Region2 Coleman; control Region1 East Library and Region2 Thompson Lane Library. Matching keys: planned total/randomized allocation and dyad-level sample unit. This is recruitment allocation, not a power calculation.

### SUP1-07 — Eligibility population and baseline completeness

[PDF p11, lines405–421](../../../../joi180075supp1_prod.pdf#page=11) and [p12, lines422–460](../../../../joi180075supp1_prod.pdf#page=12): child3–5years, BMI≥50th and <95th percentile, English/Spanish household, parent≥18, commitment3years, phone access, healthy without activity-limiting conditions. Child baseline height/weight, two diet recalls, ≥4days accelerometry, and all parent-willing survey items required. Underserved defined by self-reported household participation in TennCare/CoverKids/WIC/SNAP/free or reduced school meals/TANF. Parent means legal guardian spending majority of home time with child; only one consenting/enrolled adult per family although both parents/family may attend. Residence two Nashville regions. Exclusion: age outside interval, child BMI<50% or ≥95%, language/phone/commitment/health failures, child dissent, other eligibility failure. Matching keys: trial eligibility, enrolled/analysis unit, baseline measurement completeness. No outcome-dependent analysis exclusion specified here.

### SUP1-08 — Baseline prerequisites and language stratification

[PDF p12, lines431–437](../../../../joi180075supp1_prod.pdf#page=12): randomization requires completed height/weight, at least2diet recalls, at least4valid child accelerometer days, and all surveys families willing to complete. Dyads grouped into English/Spanish dominant-language strata, then randomized within strata. Cross-reference SUP1-25 for region and blocked schedule. Matching key: randomization stratification and pre-randomization analysis-population eligibility.

### SUP1-09 — Time points and original cohort schedule

[PDF p13, graphic](../../../../joi180075supp1_prod.pdf#page=13), [p14, Table1](../../../../joi180075supp1_prod.pdf#page=14), [p15, lines516–522](../../../../joi180075supp1_prod.pdf#page=15): six data collections T1baseline, T2month3, T3month9, T4month12, T5month24, T6month36. Diagram labels primary outcome child BMI trajectory over3years. Table1 rows preserve literal calendar values:

| Cohort | Recruitment start/duration | Baseline start/duration | Intervention start/duration | Follow-up times/duration |
|---|---|---|---|---|
| 1 | May2012 /6months | August2012 /2months | September2012 /36months | 3,9,12,24,36months /2months |
| 2 | December2012 /6months | June2013 /2months | June2013 /36months | 3,9,12,24,36months /2months |
| 3 | September2014 /6months | March2014 /2months | March2014 /36months | 3,9,12,24,36months /2months |

Calendar entries are recruitment-administration locators; collection timing matches child BMI/activity/diet result keys. No correction or reconciliation is applied to printed calendar entries.

### SUP1-10 — Randomized intervention and comparison doses

[PDF p13, direct diagram](../../../../joi180075supp1_prod.pdf#page=13), [p14, lines483–506](../../../../joi180075supp1_prod.pdf#page=14), [p15, lines507–540](../../../../joi180075supp1_prod.pdf#page=15):

- Intensive phase: weekly3months,12sessions of90minutes, nutrition/activity/parent–child skills, goal setting and self-monitoring, new networks. Diagram footnote says every session has tested curriculum with groups up to17dyads and promotes social network development.
- Maintenance: monthly9months; diagram9calls, each30minutes with15minute follow-up; narrative specifies follow-up1week later. Monthly GROW activities/events (narrative60minutes), optional weekly activity classes, internet/print engagement, problem-solving and self-monitoring.
- Sustainability: monthly24months; no phone coaching; continued monthly GROW activities, optional weekly activity classes, internet/print engagement.
- Control:12in-person60minute sessions, quarterly36months, school readiness Every Child Ready to Read, later Parent Involvement Education for entry to elementary school.
- Diagram first footnote: intervention group also receives quarterly-administered control curriculum. Preserve because it defines exposure; it is not in extracted diagram text.
- Intervention receives age/gender BMI growth-curve feedback after every measurement, plus parental BMI explanation. Monthly email/mail for families lacking Facebook account; intervention private Facebook group.

Matching key: intervention dose, duration, control curriculum and concurrent exposure. The diagram's dose arithmetic is12×90=1080minutes intensive,9×30=270minutes coaching plus9×15=135minutes follow-up,12×60=720minutes control curriculum; these are simple implied exposure totals, not separately reported outcomes. Three main behavior pillars: goal setting, self-monitoring, problem-solving.

### SUP1-11 — Adaptive intervention rule

[PDF p15, lines542–556](../../../../joi180075supp1_prod.pdf#page=15): child nonresponse when BMI category worsens T1→T2, normal→overweight/obese or overweight→obese. Growth report mailed after T2; first maintenance phone coaching reviews report, successes/barriers. Responders get report but no report-explanation phone-coach session. BMI category/nonresponse reassessed T3,T4,T5 and additional feedback sessions follow. Matching key: intervention escalation conditional on BMI category; it is not an efficacy stopping rule or a randomization change. Numeric overweight/obese cutpoints are not given in this specific paragraph; enrollment categories elsewhere retained under SUP1-04.

### SUP1-12 — Child primary outcome Table2

[PDF p16, lines558–568/Table2](../../../../joi180075supp1_prod.pdf#page=16): narrative explicitly calls child's BMI Percentile primary; change BMI% over six times assesses growth trajectory. Table2 early-childhood BMI trajectory: scale/stadiometer, change BMI% over time, child respondent, printed weight(kg)/height(m2), T1–T6. Additional rows: child body-fat% (triceps skinfold), caliper, change%bodyfat over time, staff measured,T1–T6; child waist circumference, measuring tape, change circumference, staff measured, collection-time cell unfilled in layout representation. Narrative says triceps/waist more specific adiposity measurements correlated with BMI. Matching keys: BMI raw/percentile/z-score quantity, primary trajectory endpoint, secondary adiposity measures, collection times. Preserve source quantity label rather than silently substituting raw BMI.

### SUP1-13 — Parental anthropometric secondary outcome Table3

[PDF p16/Table3](../../../../joi180075supp1_prod.pdf#page=16), continuation [p17](../../../../joi180075supp1_prod.pdf#page=17): narrative secondary parental BMI. Rows: parental BMI, scale/stadiometer, change BMI over time, weight(kg)/height(m2),T1–T6; parental body-fat%/triceps caliper, change%bodyfat,staff measured,T1–T6; parental waist measuring tape, change circumference,staff measured, collection-time cell unfilled in layout representation. Matching keys: parental BMI/activity trajectory and adiposity distributions. Do not infer a printed collection-time value for an empty cell.

### SUP1-14 — Activity moderator/mediator Table4

[PDF p17/Table4](../../../../joi180075supp1_prod.pdf#page=17): moderators defined as on whom/under what circumstances effects differ; mediators why/how treatment works. Parent+child physical activity by ActiGraph GT3X+, sedentary activity% = sedentaryminutes/totalwearingtime;≥4days,≥6hours/day valid wear, T1,T2,T4,T6. Parent self-reported physical-activity habits,2question GROW survey,T1–T6. Matching keys: accelerometer wear threshold, sedentary proportion denominator, time schedule, activity outcomes. Cross-reference SUP1-20 for narrative ActiGraph name and additional quantity definitions.

### SUP1-15 — Nutrition moderator/mediator Table4

[PDF p17/Table4](../../../../joi180075supp1_prod.pdf#page=17): parent-reported parent/child3-day diet recall; total calories and macronutrient content(%fat/protein/carbohydrate), USDA adherence,T1,T2,T4,T6. Nutrition behavior continuation [p18](../../../../joi180075supp1_prod.pdf#page=18): parent/child eating-feeding habits,8question computerized parent survey,T1–T6. Matching keys: calories/day, child dietary intake, nutrient fractions and parent report. Cross-reference SUP1-21 for averaging and exclusion rules.

### SUP1-16 — Complete remaining Table4 measures, schedules and quantities

Every following row uses parental respondent unless child or both are explicitly stated. Sources: [p18](../../../../joi180075supp1_prod.pdf#page=18), [p19](../../../../joi180075supp1_prod.pdf#page=19), [p20](../../../../joi180075supp1_prod.pdf#page=20), [p21](../../../../joi180075supp1_prod.pdf#page=21).

| Domain / instrument | Quantity and measurement | Collection times |
|---|---|---|
| Social network / GROW survey |20questions, networking influence on behavior |T1–T6|
| Group cohesion / Bollen–Hoyle Perceived Cohesion Scale |6questions |T1,week4,T6|
| Information sharing / GROW Advice Scale |2questions |T1,week4,T6|
| Parenting approaches / Toddler Feeding Questionnaire |31questions, child feeding |T1–T6|
| Parenting beliefs / Child Feeding Questionnaire |3questions, child feeding |T1–T6|
| Eating together / HHHK eating-behavior subscale |3questions, frequency meals together |T1–T6|
| Meal location / GROW survey |3questions, where together |T1–T6|
| Sleep / GROW survey |6questions, parent/child sleep |T1–T6|
| Media availability / Stanford GEMS/ECHALE questions |3questions, household media |T1–T6|
| Child media use / YRBS subscale |3questions |T1–T6|
| Recreation center use / GROW survey |3questions, knowledge/use outside GROW |T1–T6|
| Built environment / Participant Physical Activity and Neighborhood Supports |40questions, resource knowledge |T2|
| Stress / Cohen Perceived Stress Scale |10questions, parental stress |T1–T6|
| Depression / CES-D |20questions, parental depression |T1–T6|
| Goal setting and monitoring / GROW survey |6questions, set/track goals |T1–T6|
| Executive functioning / Carlson scale |Child,hands-on tasks,comprehensive executive functioning |T1,T6|
| Literacy / Receptive One-Word Picture Vocabulary Test fourth edition |Child,hands-on aptitude task |T1,T6|
| Weight perception / COPTR survey |2questions,parent and child weight |T1–T6|
| Self-efficacy / Parenting Sense of Confidence Scale |16questions,confidence in parenting decisions |T1–T6|
| Demographics / GROW survey |17questions |T1|
| Genotype / Oragene adult kit, child baby brush |Parent+child saliva genetic risk score |T1|
| Perinatal health / updated WIC questions |5questions,maternal gestational health,birth weight,breastfeeding |T1|
| Health literacy / Newest Vital Sign |6questions,food-label understanding |T1|
| Food security / USDA2008 subscale |6questions,financial barriers to home food availability |T1|
| Intelligence / Woodcock–JohnsonIII Brief Battery |Child,hands-on standard intelligence measurement |T1|

Footnote [p21, lines591–592](../../../../joi180075supp1_prod.pdf#page=21): CES-D≥27 severe depression triggers alert/resources. Table's Sleep6Q also has an asterisk; retain that marking without treating it as a separate score rule. These measures are prospective covariate/moderator/mediator/secondary-domain definitions; assigned pages give no fitted associations or numerical scale ranges beyond question counts.

### SUP1-17 — Process measurements

[PDF p21, lines593–602](../../../../joi180075supp1_prod.pdf#page=21): participation rates via attendance logs; data-collection process via timed logs/issues; retention barriers/facilitators via call logs; fidelity checks; center/library use outside mandatory sessions; facility-staff satisfaction/barriers/facilitators; parent/child satisfaction. Matching keys: attendance, adherence, retention/fidelity process variables. No numerical process rate denominator or analysis model on this page.

### SUP1-18 — Anthropometric precision and averaging

[PDF p21, lines606–619](../../../../joi180075supp1_prod.pdf#page=21): weight after voiding/light clothes nearest100g, calibrated scale; no-shoes height nearest0.1cm; BMI printed weight[kg]/height[m2] using CDC calculator. Height/weight collected twice; final mean of two closest measures. Waist at umbilicus nearest0.1cm, two measures; third if difference≥1cm; final mean of two closest. Matching keys: measured height/weight/BMI/waist, physical units, averaging/repeat threshold. No printed child BMI percentile algorithm beyond CDC calculator identification in these assigned pages.

### SUP1-19 — Skinfold repeat rule and arithmetic

[PDF p21–22, lines621–638](../../../../joi180075supp1_prod.pdf#page=22): triceps thickness nearest0.1mm; two measurements; third when (a) two triceps values<10mm differ≥2mm, or (b) skinfold≥10mm and percentage difference>10%, formula `((maximum−minimum)/minimum)×100`. Final mean of two closest. Lange caliper, Harpenden for morbid obesity. Skinfold used in equations to predict body-fat composition, but equations not supplied on these pages. Matching key: triceps/bodyfat quantity definition and measurement rule; not a study effect estimate.

### SUP1-20 — Activity quantities and accelerometer narrative

[PDF p22, lines640–654](../../../../joi180075supp1_prod.pdf#page=22): ActiGraph GT3M named; prior reliability r0.93. Parent+child wear1week during waking/sleeping except bath/shower/swim; waist belt. Physical activity expressed counts/day; total and physical-activity expenditure kcal/day from validated equations; validation-study thresholds yield time sedentary/light/moderate/vigorous. Activity log tracks activities/wearhours/day. No numerical activity cutpoints or equations supplied here. Matching keys: activity counts versus activity minutes/% versus energy expenditure, valid-wear schedule SUP1-14. Preserve differing device model text as printed without diagnosing it.

### SUP1-21 — Dietary recall averaging, window and exclusion

[PDF p22, lines656–673](../../../../joi180075supp1_prod.pdf#page=22), [p23, lines674–676](../../../../joi180075supp1_prod.pdf#page=23): total food/beverage/snack energy, energy density, macronutrients, added sugars, specific food groups; trained technicians use USDA multipass24hour recall. Target average2nonconsecutive weekdays+1weekend day within14day period at each main time point. Three phone sessions by UNC master trainers over maximum30days for complete information. Parents report own and child's intake. Analyses omit unrealistically low `<600kcal/day` or high `>4000kcal/day`. NDS-R processing; added sugars from USDA database. Matching keys: energy intake kcal/day, recall averaging and eligibility, missing/incomplete dietary measurement. These paragraphs specify exclusion but not primary BMI missing-data strategy.

### SUP1-22 — Instrument administration and genetic sampling

[PDF p23, lines678–718](../../../../joi180075supp1_prod.pdf#page=23), [p24, lines719–723](../../../../joi180075supp1_prod.pdf#page=24): English/Spanish parental computerized survey30–45minutes, paper backup. Parent saliva2–3cc; child4baby-brush sponges; modified4ml-saliva purification,4stages, approximateDNA200ng/u, working4°C/archival−80°C. Built-environment questionnaire15–20minutes links responses to3policy types(personal safety/transportation/landuse). Carlson executive-function tasks approximately10minutes; Woodcock–JohnsonIII child brief battery15–20minutes. These are instrument/procedure quantities; no result-relevant genetic fitted value or child intelligence distribution here. Matching keys: genotype moderator and control cognitive measures SUP1-16.

### SUP1-23 — Attendance/completion-linked incentives and group counts

[PDF p24, Table5/lines726–751](../../../../joi180075supp1_prod.pdf#page=24), [p25, Table6/lines754–787](../../../../joi180075supp1_prod.pdf#page=25):

| Data time | Gift-card amount | When |
|---|---:|---|
|T1baseline|$40|At randomization|
|T2|$40|Pick-up day|
|T3|$15|Immediately after|
|T4|$40|Pick-up day|
|T5|$15|Immediately after|
|T6|$50|Pick-up day|

Table5 footnote T1,T2,T4,T6: half before accelerometer wear, half upon return and≥2of3diet recalls completed. Intensive giveaways approximately$3.50perdyad/week,12sessions gives$42. Raffles sessions3/6/9/12, items respectively$10/$15/$20/$25,total$70; substitutions similar value; expected odds approximately1:15 conditional on15attendees, individual/session attendance changes odds.6–8intervention groups/cohort,3–4/site. Kitchen inventory historical42–57%lacking given items. Maintenance coupon$2for each monthly coaching call,9calls gives$18. Maintenance/sustainability punch-card gift$5per6event punches,5opportunities=>$25over33months if every event attended. Control giveaway approximately$5perdyad/session,12sessions=> $60over36months; raffle$20quarterly, odds approximately1:15conditional on15attendance. Matching keys: planned attendance/dose/measurement completion process; incentive sums are not efficacy endpoints or hypothesis thresholds.

### SUP1-24 — Center access co-intervention

[PDF p25–26, lines794–811](../../../../joi180075supp1_prod.pdf#page=25), [p27–28, lines892–895](../../../../joi180075supp1_prod.pdf#page=28): both arms family recreation memberships1year, free adult weight room and swimming lessons at50%normalcost. Intervention during study, control at completion. Membership extended annually up to3years if center used≥1time/month. Annual parent/child membership value$400. Matching key: intervention exposure and delayed control access, not a sample size or result. Risk/benefit passage repeats during/after timing and swimming cost proportion.

### SUP1-25 — Randomization unit, strata and blocks

[PDF p26, lines813–846](../../../../joi180075supp1_prod.pdf#page=26): identical procedure per3cohorts; software such as SAS/Stata creates blocked schedules perstratum within bothregions:2languages×2regions=4schedules. Blocksize randomly permuted, maximum10. Dyad familyID assigned next available slot in appropriate schedule after requirements completed. Ratio implied by cohort100/100 and graphic300/300; not separately restated as a numeric ratio in this paragraph. Matching keys: individually randomized dyad, language/region stratification, allocation ratio/block design. No cluster-level randomization specified here; intervention session grouping SUP1-10 is distinct from randomization.

### SUP1-26 — Assignment data and assessor masking

[PDF p26–27, lines823–873](../../../../joi180075supp1_prod.pdf#page=27): schedules loaded bystratum, only statistician reads, no study-team writes. Arm assignment linked irreversibly to familyID. Randomized dyads retained in recruitment database; measurement database receives IDs and necessary fields without arm; intervention database implicitly reveals arm through delivery. Staff can view dyad assignment case-by-case in recruitment records. Matching keys: masking/outcome collection and randomized cohort retention; no post-randomization analysis set/exclusion defined.

### SUP1-27 — Safety attribution thresholds

[PDF p28, lines897–939](../../../../joi180075supp1_prod.pdf#page=28), [p29, lines940–946](../../../../joi180075supp1_prod.pdf#page=29): adverse events assessed enrollment and every collection time; spontaneous/observed/family/provider reports investigated. Text categories notrelated/possiblyrelated/definitelyrelated; attribution criteria list possible≥2of5conditions, probable≥3of5conditions, definite≥4of5conditions. The5conditions: reasonable temporal relationship, not readily attributable to clinicalstate, not readily attributable to environment/otherintervention, knownresponsepattern, diminishes on intervention cessation/reduction. Matching keys: adverse-event attribution and timing. No quantitative safety comparison or efficacy interim boundary. Tenyear storage/destruction requirement is administrative, not follow-up length.

### SUP1-28 — Interim data access and blinding policy

[PDF p29–32, Policy for Blinding in COPTR dated January 26, 2012](../../../../joi180075supp1_prod.pdf#page=29): study starts at first participant randomization; ends once all important primary/secondary outcomes are collected for all participants; interim is between start and end. Common measures collected by ≥2 sites; site-specific measures at only 1 site. OMM means outcomes, mediators, moderators. Individual-level OMM/process/demographics unblinded; arm-level demographics unblinded. Arm-level OMM and blinded process information restricted while trial ongoing. A-priori unblinded process variables reviewed by design/analysis group and approved by PI; additional requests after start reviewed, require PI/DSMB approval and documented amendment.

[PDF p31, Table7](../../../../joi180075supp1_prod.pdf#page=31): intervention comparable/suitable for blinding: NO by design; investigators/staff blind to individual arm: NOT POSSIBLE; participants blind to intervention: NOT POSSIBLE; outcome assessors blind to individual intervention: YES; investigators/all staff except site analysts blind to all interim arm-aggregated OMM/blinded process: YES; site statistician blind to common interim arm OMM: YES; site statistician blind to site-specific interim arm OMM: NO; site staff unblinded to declared process measures: YES. RCU acts as Independent Statistician, centers as Site Statistician; each of 4 COPTR sites identifies a site statistician.

[PDF p32, lines1054–1090](../../../../joi180075supp1_prod.pdf#page=32): site statistician blinded to postrandomization common arm comparisons until endpoints complete unless DSMB instructs otherwise; manages schemes/randomization/data/reports/site-specific OMM; protects investigator blind. Only RCU personnel unblinded to common arm OMM during trial; prepares common OMM/adverse events DSMB reports as requested. Site statistician should not analyze common OMM/adverse event/follow-up arm aggregates, may prepare site-specific descriptive reports if DSMB/RCU directs. Matching keys: interim monitoring access, final analysis blind. These pages specify confidentiality/access rather than significance, stopping, or alpha-spending rules; their absence here does not establish absence from other assigned shards.

## Historical and administrative numerical statements inspected

These are retained as source observations for full-unit coverage, distinguished from prospective trial design and trial results. They do not create trial relationships or findings by themselves.

| Page | Printed quantities/context | Trial-result applicability |
|---|---|---|
|6|Obesity rates tripled over 30 years; 30–40% children may develop type 2 diabetes; preschool-ever-overweight fivefold adolescent risk; 80% school-age-ever-overweight later overweight; adult all-cause mortality twofold; first 3 month weight gain; target ages 3–5.|Historical background; target categories retained SUP1-04.|
|7|Viva La Familia almost 1000 children, 67% meals home; children nearly 6 times more likely active if parents active; 10 year treatment follow-up; ADA 2006 position paper 4 intervention elements.|Historical background, no GROW study estimate.|
|8|Peer activity adjustments ≥10%, OR 6.89, P<.01; own age OR .92, P<.10; obesity OR .66, P<.10; friendship selection child BMI z-score t 2.08, P<.05; heritability 40–70%; GIANT January 2009 meta-analysis >100000 patients, 8 alleles, genome-wide significance 5×10^-7.|Historical statistical statements, not GROW results; GRS construction retained SUP1-05.|
|9|Historical BMI 25–27 at extremes of GRS; 60% overweight preschoolers later overweight adolescents; repeated planned 600/3×200.|Background versus trial sample target distinguished.|
|10|3–6 liaisons per 2 communities; formative pilot 439 assessed, 50 eligible/baseline, described 10% return; clinic panel 15000, 90% Medicaid, >200 pediatricians, majority age ≤5.|Recruitment feasibility/frame, not trial randomization/outcome denominators.|
|12|Region 1 zip codes 37206/37207/37208/37213/37216/37228; Region 2 zip codes 37013/37204/37210/37211/37217/37220.|Operational eligibility geography.|
|21–23|Literature skinfold ages 3–8 and adiposity rebound 3–5; accelerometer reliability r .93; saliva chemical percentages 100% isopropanol/70% ethanol.|Prior validation/procedures, not reported trial estimates.|
|24–26|Money, raffle odds, session counts and membership values.|Attendance/exposure retained SUP1-23/24; no efficacy inference.|
|28|Paper/electronic data storage 10 years after completion.|Administrative storage duration distinct from 3 year follow-up.|
|29–32|COPTR policy date Jan 26, 2012; common measure ≥2 sites; 4 COPTR sites.|Masking/common data access policy retained SUP1-28; administrative counts do not define this trial's randomization count.|

## Handoff boundaries

Assigned32physical pages fully inspected and mapped:32complete,0gaps. There are28local prospective relationship groups plus1historical/administrative catalogue. No XLS/XLSX/CSV/DOC/DOCX assigned or supplied in this package; no formulas/cached workbook values applicable. No study effect estimates, confidence intervals, fitted test results, formal primary model, power formula, missing-BMI model, multiplicity rule, or efficacy stopping rule is printed within the assigned pages. Later plan analysis sections are outside this shard and are delegated independently. Matching main-paper keys are supplied by semantic outcome/population/quantity labels, without reading unassigned report pages. The coordinator assigns global N/S IDs and merges this part with the other complete support shards.
