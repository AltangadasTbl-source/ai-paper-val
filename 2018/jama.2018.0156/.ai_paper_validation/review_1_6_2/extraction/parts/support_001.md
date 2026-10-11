# Support extraction part 001: original protocol and final-protocol front matter

Scope: DOC-002, `joi180004supp1_prod.pdf`, physical PDF pages 1–63 inclusive. All content is PLAN. Runtime agent: `01a129b2-7db6-7d30-acec-7d2915ec00eb`; mandatory support quantitative mapper, run model gpt-6.1-sol, medium effort. This artifact maps evidence only and supplies no issue diagnoses or candidate classifications. SUP1-N and SUP1-S identifiers are provisional mapper locators; fresh reviewers own the canonical numeric/statistical inventories.

Read completely: QUALITY_CONTROL_SCOPE.md, workflow_1_6_2/review_contract.md, current source inventory, source coverage, evidence-asset inventory, and tooling record. Assigned text was read in bounded physical-page chunks (1–8, 9–12, 13–23, 24–35, 36–46, 47–54, 55–57, 58–63), with targeted rereads where tool output was truncated. No old scientific conclusions were read. Source-hash-matched canonical Poppler layout extraction `.ai_paper_validation/review_1_5_2/preprocessing/layout_text/joi180004supp1_prod.txt` is the reusable aid for all 63 pages. The curator's direct-source byte comparison establishes current-source identity. Page 52 native text omits the scoring tables; supplied OCR `.ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_pages/page_052.txt` and image `images/page_052.png` were read, then the exact source page was freshly rendered and visually read. Engine: direct Poppler pdftoppm 25.03.0, CPU; command `pdftoppm -f 52 -l 52 -singlefile -scale-to 1800 -png joi180004supp1_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/support_001/page052`; derivative `.ai_paper_validation/review_1_6_2/preprocessing/support_001/page052.png`. No new OCR or Python extraction was used. Historical GPU OCR is reused only.

There are no workbook formulas, cached workbook values, displayed spreadsheet values, DOC/DOCX paragraph units, or CSV records in this scope. All form boxes below are unfilled templates rather than participant observations. No fresh-required unit was assigned; page 52's reusable-text incompleteness is closed through source rendering. Scientific gaps: none within assigned pages. Main-paper keys below are conceptual join keys for the main mapper/checkers, not assertions about report values outside this scope.

## Numeric, endpoint, intervention, and measurement relationships

| Locator | Exact physical source pages / section | Extracted relationship and quantities | Matching main-paper key |
|---|---|---|---|
| SUP1-N001 | [p9](../../../../joi180004supp1_prod.pdf#page=9), [p14](../../../../joi180004supp1_prod.pdf#page=14), [p15](../../../../joi180004supp1_prod.pdf#page=15), [p17](../../../../joi180004supp1_prod.pdf#page=17): summary, 3.1, 4.1.1, flow diagram | Primary outcome: survival at day 28 with favorable neurological function; favorable means Glasgow-Pittsburgh CPC ≤2. Contrast TI versus BVM in objective; experimental BVM versus reference TI in design. Flow diagram requires eligible OHCA and attempted resuscitation, randomizes into control TI/intervention BVM, then observes this primary endpoint. | Primary favorable neurological survival, day 28, CPC1–2, randomized arm |
| SUP1-N002 | p9, p15–16: secondary objectives and endpoints | Survival at hospital admission; survival at day 28; survival at hospital discharge; day 28 mRS neurologic outcome; ROSC rate. All listed as secondary endpoints. Secondary objectives explicitly mention hospital-admission and day 28 survival and neurological outcomes. | Secondary survival/ROSC/mRS outcomes and prespecified status |
| SUP1-N003 | p9–10, p15–16, p19, p32 | Secondary difficulty outcomes: IDS for intubation; BVM difficulty on VAS; Han mask-ventilation classification and difficult-mask signs are explicitly included in summary p10 and collection list p19. IDS/VAS also in main endpoint list p16. | Intubation/ventilation difficulty; measurement scales |
| SUP1-N004 | p9, p16 | TI complications during advanced CPR: failure, esophageal intubation, mainstem intubation, vomiting, pulmonary aspiration, dental trauma; p16 also lists extubation. BVM complication: regurgitation of gastric content. These are secondary endpoints. | Adverse-event/airway complication outcome definitions |
| SUP1-N005 | p10, p16, p19, p32 | Secondary technique failure composite: mortality at day 28 OR regurgitation during procedure OR procedure failure. Detailed p16/19/32 definition: inability to ventilate in BVM or inability to intubate in TI. | Technique-failure composite, status, components |
| SUP1-N006 | p10, p16 | Time to completion of TI: blade touches patient to tracheal-tube cuff inflation. Additional secondary outcomes: interruption of chest compression during TI; interruption during advanced CPR (medical-team arrival to decision to stop CPR); duration of advanced CPR over the same arrival-to-stop window. Time unit not explicitly given here. | Procedure time, chest-compression interruption, advanced CPR duration |
| SUP1-N007 | p15, p18, p25, p27 | Group A experimental: initial BVM during OHCA; intubate after ROSC. If BVM impossible or massive aspiration after randomization, TI is preferred rescue. Group B reference: TI during OHCA; standard non-styletted tube, no sedation; alternate procedure if standard laryngoscopy impossible. p15 says all intubated after hospital admission; p18 says successfully resuscitated BVM patients intubated and mechanically ventilated before transport. p25 permits TI with or without sedation after ROSC. Retain these distinct temporal statements without diagnosis. | Randomized airway strategy, rescue/crossover, post-ROSC intubation |
| SUP1-N008 | p10, p23 §6 | Eligible: age ≥18 years; OHCA on medical-team arrival; resuscitation attempted; medical insurance. Excluded before randomization: suspected massive aspiration, do-not-resuscitate order, pregnancy, prisoners. Planned population 2000 adult patients. | Eligibility, randomized population |
| SUP1-N009 | p10, p17, p24 recruitment table, p47–49 site lists | Planned enrollment 2000; 20 centres in 2 countries; p17 specifies 15 France and 5 Belgium; expected 100 patients/centre and 5 patients/month/centre over 24 months. Sites are listed sequentially 01–20 across p47–49. Recruitment table p24 prints total2000/centres20/months24/subjects-per-centre100/subjects-per-centre-per-month5. These are plans, not observed enrollment counts. | Sample-size target; centre-stratified randomization; peripheral recruitment schedule |
| SUP1-N010 | p10, p17, p20–21, p32 | Planned individual participation day28; follow-up window day28 +7 days (up to day35), reporting status specifically at day28 even when obtained later. No earlier status is permitted unless death occurs before day28, which is recorded as dead day28. Recruitment24 months; total research24 months and28 days. | Primary outcome time point, ascertainment window |
| SUP1-N011 | p18–21, p32 | Out-of-hospital period: randomization to admission. Hospital period: admission to discharge. Follow-up: day28 status. Baseline/history, arrest etiology/collapse, basic/advanced-resuscitation duration, shock number, drug name/quantity, ROSC, IDS, VAS, admission survival, SAE, regurgitation, technique failure collected prehospital. p19 also collects difficult-airway factors, Han classification, difficult-mask signs. Hospital collects all-cause death and primary cause. Follow-up collects all-cause death/cause, CPC, mRS. | Baseline table, procedure outcomes, survival/time windows |
| SUP1-N012 | p21 chronology table | Medical history/demographics/baseline/eligibility/emergency inclusion/randomization/airway administration/IDS/VAS/SAE marked in enrollment/pre-hospital column. Consent marked in all three periods. CPC and mRS marked only day28 follow-up. Mortality marked in all three periods. | Timing of measurement by endpoint |
| SUP1-N013 | p22 care/research table | Routine care marks medical history, demographics, baseline, airway administration. Research additions mark eligibility, emergency inclusion, consent, randomization, IDS, VAS, CPC, mRS, SAE, mortality. No numeric effect estimate. | Measurement provenance and outcome status |
| SUP1-N014 | p24 §§7.1.2–7.1.5, p25 §7.2, p33 §10.2 | IDS described as seven parameters: supplementary attempts, operators, alternate techniques, laryngoscopic grade, lifting force, external laryngeal manipulation, vocal-cord mobility/position. VAS investigator subjective difficulty. mRS measures day28 disability/dependence; CPC day28 neurologic status. p25 describes IDS/VAS/mRS/CPC assessment of neurologic function day28; p33 states these four directly collected in CRF day28 +7days. Other temporal occurrences retained in SUP1-N011/012. | Scale definition and measurement time |
| SUP1-N015 | [p50](../../../../joi180004supp1_prod.pdf#page=50), §17.2 | mRS table scores:0 no symptoms;1 no significant disability, all usual duties;2 slight disability, cannot do all previous activities but manages affairs without assistance;3 moderate disability, some help but walks without assistance;4 moderately severe, cannot walk or attend bodily needs without assistance;5 severe, bedridden/incontinent/constant care;6 dead. TOTAL printed range0–6, blank response. | Day28 mRS distribution and death coding |
| SUP1-N016 | [p51](../../../../joi180004supp1_prod.pdf#page=51), §17.3 | CPC table:1 good cerebral performance, conscious/alert/work-capable, possible mild deficit;2 moderate disability, conscious/independent daily activities/sheltered work;3 severe disability, conscious/dependent support, ambulatory to severe dementia/paralysis;4 coma/vegetative, no interaction, may have sleep/wake cycles and eye opening;5 brain death, apnea/areflexia/EEG silence. Footnote: if anesthetized, paralyzed, or intubated use current clinical condition “as is.” | Primary CPC ≤2, CPC distribution |
| SUP1-N017 | [p52](../../../../joi180004supp1_prod.pdf#page=52), §17.4 | IDS = sum of N1–N7. N1 each attempt beyond1 adds1; N2 each operator beyond1 adds1; N3 each alternative technique adds1; N4 Cormack grade minus1; N5 normal lifting0/increased1; N6 laryngeal pressure absent0/applied1; N7 vocal cords abducted0/adducted1. Full table/footnotes below. | Intubation difficulty scale total and category |
| SUP1-N018 | [p53](../../../../joi180004supp1_prod.pdf#page=53), §17.5 | VAS question: whether BVM ventilation difficult; anchors0 “No, not at all,”100 “Yes, extremely difficult.” Continuous line graphic. No explicit length unit. | Ventilation difficulty VAS, 0–100 |
| SUP1-N019 | [p54](../../../../joi180004supp1_prod.pdf#page=54), §17.6 | Han grades:0 not attempted;1 ventilated by mask;2 with oral airway/other adjuvant;3 difficult mask ventilation (inadequate, unstable, or needs two practitioners);4 unable. Reference footnote supplied Han et al 2004; no report-result values here. | Mask-ventilation category distribution |
| SUP1-N020 | p26–29 §§9.1 | SAE definition: death, life-threatening, inpatient/prolonged hospitalization, persistent/significant disability/incapacity, congenital anomaly. All serious/nonserious AEs reported in CRF. Death is SAE recorded only, no immediate notification. TI known record-only complications: aspiration during insertion, mainstem/esophageal intubation, dental trauma. BVM record-only complications: aspiration during BVM; vomiting, desaturation, hypotension, aspiration, bronchospasm/laryngospasm, mainstem/esophageal TI, dental trauma during post-ROSC TI. Expected research-related SAE requiring notification: failure to insert TI device. Sponsor-report period ends prehospital medical management. | Safety endpoint composition, procedure attribution, time window |
| SUP1-N021 | p55 SAE form page1 | Blank identifiers center3 digits/randomization4 digits/name initials; gender M/F; weight kg; height cm; age years; birth/date fields dd/mm/yyyy. Emergency-inclusion date equals randomization date. Separate consent date, assigned BVM/TI group, procedure chronology before/after SAE, realization date. Concomitant drugs record product/dose/form, indication, administration route, daily dose, dates, ongoing indicator; five blank rows. No cached data or computed quantity. | Safety data schema and units |
| SUP1-N022 | p56 SAE form page2 | Blank SAE onset date/time (hh/min) and latency from last research procedure (dd/hh/min); missing-data tick; interruption yes/no and temporary/permanent; restart/recurrence dates; unblinding yes/no/NA; seriousness hospital dates/ongoing/death/life-threatening/disability/congenital/other; severity mild/moderate/severe. Outcome death related/unrelated, resolved with/without sequelae and date/time, or ongoing stable/worse/improving. Relatedness certain/probable/possible/unlikely; other etiologies/investigations/causation tick fields. Route legend PO oral, IM intramuscular, IV intravenous, SC subcutaneous/other; ongoing means at SAE. No observed participant value. | Safety outcome/attribution schema |
| SUP1-N023 | p12 background | Cited historical data only: pediatric trial830; population649359; day30 favorable neurological survival BVM2.9%/367837 vs TI1.0%/41972; post-ROSC TI survival33% (40/120) vs pre-ROSC12% (69/573), P<0.0001. Not CAAM outcomes. | Background and sample-size provenance only |
| SUP1-N024 | p13–14 background; p18/p20 operational estimates | Historical adult comparison10455=8487 TI+1968 SGA; discharge survival4.7% TI vs3.9% SGA. Practitioner TI1–4 annually. Population burden600000 annual deaths and >80% outside hospital. p18 anticipated successfully resuscitated/transported20–23% of total enrolled; p20 estimates3–5% of admitted patients able to sign delayed consent. These are cited contextual/operational expectations, not trial-result denominators. | Background/consent context only |

## Statistical design and analysis relationships

All following relationships belong to the original v1.3 protocol dated20 November2014; subsequent final-protocol scientific sections fall outside this shard. No inferential test result is reported here.

| Locator | Exact physical pages / section | Complete planned statistical relationship | Matching main-paper key |
|---|---|---|---|
| SUP1-S001 | p10, p16–17, p35 §11.1 | Prospective multicentre international open randomized controlled parallel two-arm noninferiority trial. Individual patient randomization; centre-stratified blocks for group balance. No block size specified. BVM experimental, TI reference. | Design/randomization and primary contrast |
| SUP1-S002 | [p36](../../../../joi180004supp1_prod.pdf#page=36), §11.2 | Printed H0: πbag−πtracheal ≤−0.01; printed H1: πbag−πtracheal ≥−0.01. Success means favorable neurological survival. Preserve both printed boundary signs. | Noninferiority hypothesis direction/margin |
| SUP1-S003 | p11, p36–37 §11.4.1 | Primary ITT:95% two-sided CI of difference πbag−πtracheal; declare noninferiority if lower bound higher than−0.01. Use exact rather than asymptotic CI if necessary. No primary adjusted model/covariate list specified in this section. | Primary risk difference,95% CI,−1 percentage-point decision |
| SUP1-S004 | p36 §11.2 | If noninferiority demonstrated, test of difference carried out. No further significance allocation, formula, or test name given in this statement. | Sequential superiority/difference decision |
| SUP1-S005 | p10, p36 §11.3.1 | Main analysis both ITT (all randomized irrespective of delivered/adequately received treatment) and PP (randomized and treated without major protocol violations/deviations). | ITT and PP primary analysis population |
| SUP1-S006 | p22 §5.7.1, p36 §11.3.2 | Premature leavers' data usable unless objection. Withdrawal of consent prevents data use unless written no-objection; otherwise subject excluded. Disposition/status/PP exclusions by group; withdrawal primary reason descriptive by group and patient list; dropout reasons and detailed list. | Consent exclusions/analysis denominators/disposition |
| SUP1-S007 | p36 §11.3.3 | Baseline tabulation and group comparability by descriptive statistics; no tests on baseline variables per CONSORT. | Baseline table tests/description |
| SUP1-S008 | p11, p36 §11.3.4 | Interim looks after50% and75% inclusion; only futility and/or sample-size recalculation; ADDPLAN software. No efficacy interim purpose or numerical futility boundary given in assigned pages. | Interim timing/purpose/sample recalculation |
| SUP1-S009 | p23 §5.7.3, p30–31 §9.1.6 | Futility interim may terminate. Other termination grounds unacceptable SAE risk/benefit, ethics, slow recruitment, authority/sponsor decisions. DSMB recommends continue/change/temporary halt/permanent end; validates termination criteria and stopping rules, can modify eligibility/monitoring; sponsor retains authority. Charter to describe precise operations. No numeric safety threshold here. | Stopping decision and monitoring |
| SUP1-S010 | p11, p37 §11.4.2 | Secondary ITT rates:chi-square test on proportions;95% CI on odds ratios and differences. | Secondary binary-outcome tests, OR and difference CIs |
| SUP1-S011 | p11, p37 §11.4.2 | Quantitative secondary criteria:t-test for Gaussian or Mann–Whitney for non-Gaussian distribution. Sidedness/test statistic not further stated here. | Continuous/ordinal secondary tests |
| SUP1-S012 | p37 §11.5 | Serious and other adverse events tabulated by treatment; all dichotomized safety endpoints tested via chi-square proportions and95% CI on OR. | Safety analysis/tests/effect measure |
| SUP1-S013 | p37 §11.6 | Exploratory multivariate logistic regression identifies potentially important prognostic factors for main and/or secondary efficacy parameters. No specific predictors, selection threshold, or adjustment covariate set given here. | Exploratory adjusted model/prognostic factors |
| SUP1-S014 | p37 §11.7 | ITT primary missing outcome imputed by worst-case “no success.” | Primary missingness and unfavorable-outcome imputation |
| SUP1-S015 | p37 §11.7 | If large PP/ITT population differences, sensitivity analyses with different replacement methods including multiple imputation. No numerical “large” threshold or imputation algorithm specified here. | Prespecified sensitivity/multiple imputation |
| SUP1-S016 | p11, p37 §11.9 | Power assumptions:3% favorable neurological survival BVM (Hasegawa JAMA2013) and2% TI (Gueugniaud NEJM2008). NI margin1%=0.01 absolute success-proportion difference. These planning rates differ from contextual raw rates p12; each is preserved separately. | Sample-size inputs and expected risk difference |
| SUP1-S017 | p11, p37 §11.9 |956 per arm, power0.8, type I rate0.025; planned recruitment2000 total. No attrition percentage explicitly supplied. | Required/planned sample and power/alpha |
| SUP1-S018 | p11, p37 §11.9 | Calculation uses CI NI approach,5000 simulations, Newcomb-Wilson score method, cited Statistics in Medicine1988,17:873–890. Preserve printed method and citation; no formula or simulation seed supplied. | Sample-size reproduction method |
| SUP1-S019 | p38 §11.10 | All analyses SAS9.2. Interim sample recalculation ADDPLAN separately. | Analysis software |
| SUP1-S020 | p11, p36–38 statistical sections | No numerical multiplicity correction, prespecified subgroup list, or specific primary regression covariates is described in assigned original-protocol statistical sections. Positive specifications are sequential difference testing after NI, ITT/PP, missingness sensitivity, and exploratory logistic prognostic analysis. This absence is an extraction fact, not a finding. | Multiplicity/subgroup/adjustment comparison keys |

## Page 52 IDS tables and figure: source-confirmed transcription

The direct-source rendering matches the supplied legacy image. OCR corrupts subscripts in lifting-force/laryngeal-pressure/vocal-cord rows and omits words in alternative-technique instructions. The following values are transcribed from the image, preserving source distinctions; these transcription corrections are not scientific findings.

| Parameter | Printed component / value |
|---|---|
| Number of attempts >1 | N1; every additional attempt adds1 point |
| Number of operators >1 | N2; every additional operator adds1 point |
| Number of alternative techniques | N3; each technique adds1 point |
| Cormack grade−1 | N4 |
| Lifting force normal / increased | N5=0 / N5=1 |
| Laryngeal pressure not applied / applied | N6=0 / N6=1 |
| Vocal-cord mobility abduction / adduction | N7=0 / N7=1 |
| Total IDS | Sum of scores N1–N7 |
| Easy | IDS0 |
| Slight difficulty | 0<IDS≤5 |
| Moderate to major difficulty | 5<IDS |
| Impossible intubation category | IDS=∞ |

N3 examples: repositioning patient; changing blade/ET tube/adding stylette; changing nasotracheal/orotracheal approach; using another technique such as fibroscopy or intubation through laryngeal mask. N4 rules: use Cormack grade for first oral attempt; successful blind intubation N4=0. N6 rule: Sellick maneuver adds no points. Separate impossible-intubation instruction says IDS takes the value reached before abandonment of attempts; both this instruction and the ∞ category are retained. Cormack-grade schematic depicts I,II,III,IV, progressively less visible laryngeal view. Footnote cites Cormack/Lehane1984; this citation is a scale reference rather than trial evidence.

## Administrative units opened and mapped

The bound cover p1 lists original/final protocol, amendments, summary of changes, original SAP. Original protocol p2–56 has title v1.3 dated20 November2014, projectP130932/EudraCT2014-A01109-38. Final-protocol front matter p57–63 prints V1.4 dated22 September2015 and V2 dated22 January2016; title p57 and signature p58 preserve this composite version display. Approval dates on p58: ethics4 November2014, ANSM22 October2014. No sample-size or analysis text occurs in final front matter within this shard. Its TOC indexes primary/secondary/design, eligibility, procedures, safety, data management, statistical model/hypotheses/populations/interim/efficacy/safety/exploratory/missingness/randomization/power/software and scale appendices. These index entries are not substituted for mapping the scientific pages assigned to other shards.

Operational numeric content not a trial result: p28 emergency-department admission<12hours; fatal/life-threatening SAE detailed follow-up8days, other cases15days; p29–30 sponsor initial declaration7calendar days fatal/life-threatening or15days other, follow-up within8days thereafter; new safety facts15days plus8days additional information; annual report due60days after authorization anniversary. p31 DSMB≥3 independent people including≥1 clinician. p33 source records15years; p34 retention≥2years after relevant regulatory milestones; p35 investigator/identity/consent records≥15years. p43 final report within1year of last follow-up or90days after premature termination. These were inspected and do not supply endpoint counts or statistical decision thresholds. p34 requires clearly defined laboratory units or transformations; no numeric laboratory results are supplied. p39 requires each missing-data item coded, eCRF consistency checks, investigator validation and audit trail. p41 emergency inclusion and delayed consent; p42 other medication-trial participation prohibited through day28+7days, noninterventional participation permitted. Administrative procedures contain no workbook value or formula.

## Complete physical-page coverage

Every row is COMPLETE for scientific mapping. “No applicable relationship” means the page was opened and read and contains no direct trial-result/analysis relationship beyond the stated administrative or index context.

| Physical page | Printed page / unit | Mapped content / provisional relationships | Status |
|---:|---|---|---|
|1|Bundle contents|PLAN identity; no applicable relationship; contents only|COMPLETE|
|2|Original1|v1.3 identity/contact cover; no applicable relationship|COMPLETE|
|3|Original2|Signature/administrative IDs; no applicable relationship|COMPLETE|
|4|Original3|Abbreviations CPC/CI/IDS-context; no separate numeric relationship|COMPLETE|
|5|Original4|TOC primary/secondary/procedures; no applicable relationship|COMPLETE|
|6|Original5|TOC measurement/safety/data; no applicable relationship|COMPLETE|
|7|Original6|TOC statistical/administrative; no applicable relationship|COMPLETE|
|8|Original7|TOC scale/form appendices; no applicable relationship|COMPLETE|
|9|Original8|Primary/secondary summary; SUP1-N001–N004|COMPLETE|
|10|Original9|Outcome/design/population/recruitment summary; SUP1-N003,N005–N010;SUP1-S001,S005|COMPLETE|
|11|Original10|CI/test/interim/power summary; SUP1-S003,S008,S010,S011,S016–S018|COMPLETE|
|12|Original11|Historical data only; SUP1-N023|COMPLETE|
|13|Original12|Historical SGA/TI and provider exposure; SUP1-N024|COMPLETE|
|14|Original13|Primary objective; SUP1-N001; contextual burden SUP1-N024|COMPLETE|
|15|Original14|Secondary objectives/interventions/primary endpoint; SUP1-N001–N004,N007|COMPLETE|
|16|Original15|Full secondary-endpoint list/design; SUP1-N002–N006;SUP1-S001|COMPLETE|
|17|Original16|Trial flow/stratified blocks/follow-up; SUP1-N001,N008–N010;SUP1-S001|COMPLETE|
|18|Original17|Emergency consent/out-of-hospital/ROSC TI; SUP1-N007,N011,N024|COMPLETE|
|19|Original18|Collection list/technique failure/hospital period; SUP1-N003,N005,N011|COMPLETE|
|20|Original19|Day28 ascertainment+7/CPC/mRS/deaths; SUP1-N010,N011,N024|COMPLETE|
|21|Original20|Duration and chronology table; SUP1-N010,N012|COMPLETE|
|22|Original21|Care/research table/withdrawal data-use rules; SUP1-N013;SUP1-S006|COMPLETE|
|23|Original22|Termination/eligibility; SUP1-N008;SUP1-S009|COMPLETE|
|24|Original23|Recruitment table and IDS/VAS/mRS/CPC; SUP1-N009,N014|COMPLETE|
|25|Original24|Post-ROSC sedation rule/measurement timing/committees; SUP1-N007,N014|COMPLETE|
|26|Original25|Safety definition; SUP1-N020|COMPLETE|
|27|Original26|AE capture, death and procedure-specific record-only complications; SUP1-N020|COMPLETE|
|28|Original27|Additional complications/TI failure/reporting periods; SUP1-N020; operational deadlines mapped|COMPLETE|
|29|Original28|Prehospital SAE window/sponsor declaration; SUP1-N020; operational deadlines mapped|COMPLETE|
|30|Original29|DSMB mission/annual reporting; SUP1-S009; operational deadlines mapped|COMPLETE|
|31|Original30|DSMB authority/stopping rules/data source; SUP1-S009|COMPLETE|
|32|Original31|Endpoint collection by period/28+7; SUP1-N005,N010,N011|COMPLETE|
|33|Original32|CRF assessment timing; SUP1-N014; confidentiality/access opened|COMPLETE|
|34|Original33|Data-recording/unit policy/retention; no separate trial statistical relationship|COMPLETE|
|35|Original34|Plan design/hypothesis introduction; SUP1-S001; ownership/archiving opened|COMPLETE|
|36|Original35|Hypotheses,NI-to-difference,ITT/PP,withdrawals,baseline,interim,CI; SUP1-S002–S008|COMPLETE|
|37|Original36|CI decision,secondary/safety/exploratory/missingness/randomization/power; SUP1-S003,S010–S018|COMPLETE|
|38|Original37|SAS9.2; SUP1-S019; quality administration opened|COMPLETE|
|39|Original38|Missing items coded/eCRF consistency/audit; no additional analysis rule|COMPLETE|
|40|Original39|Audit/responsibility/consent introduction; no applicable relationship|COMPLETE|
|41|Original40|Emergency inclusion/delayed consent/support; confirms SUP1-S006 population context|COMPLETE|
|42|Original41|Other research participation/study interruption/amendments; operational content mapped|COMPLETE|
|43|Original42|Final-report deadlines/budget/insurance; no applicable statistical relationship|COMPLETE|
|44|Original43|Publication rules; no applicable relationship|COMPLETE|
|45|Original44|Bibliography; provenance references only, no applicable quantitative relationship|COMPLETE|
|46|Original45|Bibliography remainder; no applicable quantitative relationship|COMPLETE|
|47|Original46|Centres01–08; SUP1-N009 site-list context, no result count|COMPLETE|
|48|Original47|Centres09–16; SUP1-N009 site-list context, no result count|COMPLETE|
|49|Original48|Centres17–20; SUP1-N009 site-list context, no result count|COMPLETE|
|50|Original49|mRS scoring table0–6; SUP1-N015|COMPLETE|
|51|Original50|CPC categories1–5 and scoring footnote; SUP1-N016|COMPLETE|
|52|Original51|IDS component/threshold/rule tables and Cormack figure; SUP1-N017; OCR+fresh source visual|COMPLETE|
|53|Original52|VAS0–100 graphical anchors; SUP1-N018|COMPLETE|
|54|Original53|Han mask-ventilation0–4 table; SUP1-N019|COMPLETE|
|55|Original54|Blank SAE form1, numeric fields/units/arm/date schema; SUP1-N021|COMPLETE|
|56|Original55|Blank SAE form2, dates/time/latency/outcome/attribution; SUP1-N022|COMPLETE|
|57|Final1of51|V1.4/V2 cover; no applicable relationship|COMPLETE|
|58|Final2of51|Signature/version/approval dates; no applicable relationship|COMPLETE|
|59|Final3of51|Abbreviations; no applicable numeric relationship|COMPLETE|
|60|Final4of51|TOC scientific/procedure sections; no applicable relationship|COMPLETE|
|61|Final5of51|TOC measurements/safety/data; no applicable relationship|COMPLETE|
|62|Final6of51|TOC statistical/administrative sections; no applicable relationship|COMPLETE|
|63|Final7of51|TOC scoring/form appendices; no applicable relationship|COMPLETE|

Completion:63/63 assigned physical pages mapped,24 numeric/definition groups and20 statistical groups, with every IDS/mRS/CPC/Han scoring row retained. No observed CAAM support results occur in this assigned PLAN scope. No unresolved scientific gap; reusable text omission p52 closed by direct-source image. Remaining uncertainty is solely unspecified details in the printed plan as recorded, not omitted extraction.
