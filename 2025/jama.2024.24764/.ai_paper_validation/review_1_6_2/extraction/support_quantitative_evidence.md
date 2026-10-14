# Support evidence mapping: SAP and results supplement

Fresh support-mapper stage; exact scope DOC-002 PDF pages 1–46 and DOC-003 PDF pages 1–9. DOC-004 is outside this disjoint assignment. This is an evidence map, without candidate diagnosis or screening. Local relationship keys U001–U034 identify extraction families; global numeric and inferential IDs are assigned by checkers.

## Provenance and coverage

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely, then the current source inventory, evidence-asset inventory, source coverage and tooling record. Sources: DOC-002 `joi240145supp1_prod_1741627844.87412.pdf` is PLAN (SAP 1.0 for protocol 4.0); DOC-003 `joi240145supp3_prod_1741627844.89412.pdf` is REPORT (non-plan eTables/eFigures). SAP amendment table on page 2 has blank entries; no populated amendment or effective approval date is printed on its title/amendment pages. Prospective table shells remain PLAN, never observed results.

Reused preferred assets: `.ai_paper_validation/review_1_5_3/preprocessing/support_mapper/DOC-002_pp01-23_layout.txt`, `DOC-002_pp24-46_layout.txt` (110819 characters combined); `.ai_paper_validation/document_outputs/JAMA2024-24764-SUPP3/normalized_text/native_text.txt` (12110 characters); `.ai_paper_validation/review_1_5_3/preprocessing/numeric_direct/DOC-003_pp03-08_layout.txt` (19793 characters). Legacy layout engine/version was not retained; native text is legacy normalized pypdf, version not retained. Their full source-matched coverage is recorded and hashed by the curator. Reusable DOC-003 full-page images pages 3–9 were visually inspected (seven pages), particularly table column alignment, signed limits, forest-plot numbers and tipping-point axes. No new OCR or text extraction was needed. SAP page 32 required a fresh visual companion because its schedule is image-only in layout text; the coordinator renders this page with the recorded CPU PyMuPDF fallback. No GPU OCR inference is claimed.

No workbook/CSV/DOC/DOCX scientific source belongs to this scope; formula versus cached-value distinction is not applicable. All formulas below are printed SAP formulas, rather than computed workbook values.

| Source | PDF page | Mapping / applicability | Keys |
|---|---:|---|---|
| DOC-002 | 1 | MAPPED: SAP/protocol version and trial identity; no result values | U001 |
| DOC-002 | 2 | MAPPED: blank amendment table; no populated amendment | U001 |
| DOC-002 | 3 | MAPPED: abbreviations/definitions; no independent numerical result | U001 |
| DOC-002 | 4 | MAPPED: contents covering all analysis sections and shells | U001 |
| DOC-002 | 5 | MAPPED: reporting/deviation policy; historical background numbers only | U002 |
| DOC-002 | 6 | MAPPED: objectives, superiority design and intervention duration | U003 |
| DOC-002 | 7 | MAPPED: primary and all secondary outcomes/scales/time points | U004 |
| DOC-002 | 8 | MAPPED: individual 1:1 minimisation and factors | U005 |
| DOC-002 | 9 | MAPPED: power/sample size/hypotheses and DMC arrangements | U006, U007 |
| DOC-002 | 10 | MAPPED: interim stopping/final alpha rule | U007 |
| DOC-002 | 11 | MAPPED: feasibility stop-go rules and final analysis timing | U008 |
| DOC-002 | 12 | MAPPED: CIs/tests/multiplicity/ITT/PP/adherence | U009 |
| DOC-002 | 13 | MAPPED: ITT deviations, 30-day window and blinding | U010 |
| DOC-002 | 14 | MAPPED: descriptive summaries, intervention/adherence | U011 |
| DOC-002 | 15 | MAPPED: adjustment/fallback/missingness/distributions | U012 |
| DOC-002 | 16 | MAPPED: age/BMI formulas and operative grouping | U013 |
| DOC-002 | 17 | MAPPED: grouping precedence and subgroup thresholds | U013 |
| DOC-002 | 18 | MAPPED: SSI coding/diary rules and UK stay | U014 |
| DOC-002 | 19 | MAPPED: wound complication coding and grades | U015 |
| DOC-002 | 20 | MAPPED: readmission and SF-12 response coding | U016, U017 |
| DOC-002 | 21 | MAPPED: SF-12 response coding | U017 |
| DOC-002 | 22 | MAPPED: SF-12 domains and z formulas | U017 |
| DOC-002 | 23 | MAPPED: SF-12 summaries and EQ scoring/missing/death | U017, U018 |
| DOC-002 | 24 | MAPPED: SAE counting and duplicate-event rule | U019 |
| DOC-002 | 25 | MAPPED: primary/binary models and UK stay model | U020 |
| DOC-002 | 26 | MAPPED: repeated-measures quality-of-life and pain models | U021 |
| DOC-002 | 27 | MAPPED: acceptability, exploratory status and safety | U022 |
| DOC-002 | 28 | MAPPED: every prespecified subgroup and interaction | U023 |
| DOC-002 | 29 | MAPPED: every sensitivity/missingness analysis; economics separate | U024 |
| DOC-002 | 30 | MAPPED: software; references not independent study results | U025 |
| DOC-002 | 31 | MAPPED: deviation shell and 840-participant schema | U026 |
| DOC-002 | 32 | MAPPED: assessment schedule; visual companion required | U026 |
| DOC-002 | 33 | MAPPED: flow shell (blank counts), analysis availability | U027 |
| DOC-002 | 34 | MAPPED: baseline/minimisation/surgery shell | U028 |
| DOC-002 | 35 | MAPPED: baseline/COVID shell and durations | U028 |
| DOC-002 | 36 | MAPPED: operative details shell and units/categories | U028 |
| DOC-002 | 37 | MAPPED: operative details shell, closure and duration | U028 |
| DOC-002 | 38 | MAPPED: adherence/PP shell and missing classifications | U029 |
| DOC-002 | 39 | MAPPED: protocol-deviation shell, no populated counts | U029 |
| DOC-002 | 40 | MAPPED: primary RR/RD shell and SSI ascertainment breakdown | U030 |
| DOC-002 | 41 | MAPPED: binary secondary/grade shell | U030 |
| DOC-002 | 42 | MAPPED: stay/SF12/pain continuous shells | U030 |
| DOC-002 | 43 | MAPPED: EQ index/health continuous shells | U030 |
| DOC-002 | 44 | MAPPED: acceptability continuous shell | U030 |
| DOC-002 | 45 | MAPPED: safety binary/count/event-type shells | U030 |
| DOC-002 | 46 | MAPPED: subgroup shell including exact wound thresholds | U030 |
| DOC-003 | 1 | MAPPED: report identity/contents; no independent result | U031 |
| DOC-003 | 2 | MAPPED: contents; no independent result | U031 |
| DOC-003 | 3 | MAPPED: complete adherence and SF12 tables | U031, U032 |
| DOC-003 | 4 | MAPPED: complete EQ index/health tables | U032 |
| DOC-003 | 5 | MAPPED: both complete Clavien-Dindo tables | U033 |
| DOC-003 | 6 | MAPPED: SSI source-time counts and overlap rules | U033 |
| DOC-003 | 7 | MAPPED: PRECIS-2 visual and complete CDC definition | U034 |
| DOC-003 | 8 | MAPPED: all eight forest-plot rows, directions and six definitions | U034 |
| DOC-003 | 9 | MAPPED: both tipping-point plots, axes and conclusions | U034 |

## SAP relationships and main-paper matching keys

Each U family retains its source location, population, outcome, method and matching key. Cross-document comparison is deferred to fresh checkers.

| Key | PLAN PDF location | Extracted specification | Match in report |
|---|---|---|---|
| U001 | DOC-002 pp.1–4 | Trial ISRCTN17599457; SAP1.0/protocol4.0. Blank amendment rows. Definitions distinguish ITT, SAE, SF12 PCS/MCS and SUNPD. | Trial identity, SAP version and amendment disclosure |
| U002 | p.5 §1–2 | Main publications should follow SAP, describe/justify deviations using Appendix A; later exploratory analyses need not follow identical strategy. Background only: ≥200000 UK SSI/year, £3500/infection, £700m/year, twofold mortality, one-third postoperative deaths, 50–80% reduction in historical nonabdominal studies. | Analysis prespecification/deviation statements; background is not trial result |
| U003 | p.6 §3–4.2; p.14 §7.1 | Adult emergency laparotomy; international multicentre pragmatic phase III randomized trial with internal feasibility. SUNPD until discharge or day7, whichever sooner; replace with SUNPD if clinically needed, no routine change. Control surgeon preference (occlusive, glue, none; excludes another SUNPD); local duration. Secondary objectives stay, wound complications/readmissions, QoL, safety, acceptability and cost effectiveness. | Randomized intervention dose/duration; trial design |
| U004 | p.7 §4.3–4.4 | Primary SSI within30days CDC. Secondary: UK stay; wound complications within30days graded Clavien-Dindo; wound-related readmission within30days including SSI/dehiscence/seroma/wound pain; SF12 baseline/day7/day30; EQ5D5L baseline/day7/day14/day21/day30; wound pain VAS1=no pain to10=worst, day7/day30; SAE up to30days; diary healthcare resource cost effectiveness; patient acceptability VAS1=completely acceptable to10=totally unacceptable day7; UK health-professional SUNPD survey acceptability. | Full outcome status/definition/time-point inventory |
| U005 | p.8 §4.6 | Individual randomization1:1 in theatre after commencing skin closure; minimisation on contamination(clean/clean-contaminated/contaminated/dirty), stoma yes/no and recruiting centre; preexisting versus newly formed stoma not minimisation factor. Random element probability not specified. | Randomization and model covariates |
| U006 | p.9 §4.7–4.8 | Control SSI25%, intervention15%, RR reduction40%, absolute10 percentage points; two-sided two-sample proportions test,90% power, alpha.05;336/group=672;20% attrition (approx10%death+10%other) yields840=420/group; Stata15 sample-size calculation. Superiority; null no difference versus alternative difference. | Sample size, power, hypothesis direction |
| U007 | pp.9–10 §4.9 | Annual DMC, earlier/later discretionary meetings; major-endpoint/safety interim analyses. Stopping advice requires overwhelming major-endpoint benefit/harm and influence on management. Approx p<.001 Haybittle-Peto may justify stopping/modification; no fixed interim schedule; no multiplicity adjustment, final p=.05. | Interim/stopping/final significance |
| U008 | p.11 §4.10–4.11 | Six-month feasibility target70 from≥5sites. Green recruitment>70%, adherence>80%, dropout<20%; amber recruitment50–70%, adherence50–80%, dropout20–35%; red recruitment<50%, adherence<50%, dropout>35%. Recruitment=target fraction; feasibility adherence correct dressing≥24h; dropout complete withdrawal/no data. Final analysis after all day30 assessments and validated database. | Feasibility and timing rules; distinguish feasibility adherence from PP |
| U009 | p.12 §5 | All estimates two-sided95% CIs; two-sided tests5%; no multiple-testing correction. Primary, secondary and safety analyses ITT by randomized allocation regardless received intervention. Primary PP sensitivity: SUNPD received≥3days or earlier discharge; control no SUNPD and surgeon preference. Possible stringent SUNPD≥5days or earlier discharge. | Analysis populations, PP eligibility, tests/multiplicity |
| U010 | p.13 §5.5–5.6 | Strict ITT includes protocol deviations in some form. Day30 responses relate to first30days even if assessment later; protocol late window+14days. Primary/secondary ITT ignores assessment timing and includes all day30 forms. Sensitivities exclude early forms or restrict30–44days. Day7 unblinded; day30 independent trained assessor blinded to allocation. | Assessment window/analysis exclusions |
| U011 | p.14 §6–7 | Flow losses/reasons; categorical n/%; continuous n, mean/SD if normal or median/IQR if skewed, ranges as appropriate. No baseline tests/CIs. Allocation-by-adherence cross-tabulation. | Flow/baseline and received-intervention summaries |
| U012 | p.15 §9.1–9.3 | All outcomes adjust minimisation factors where possible: centre random, contamination/stoma fixed; baseline values also covariates where available. Control reference. Binomial-log fallback order: Poisson robust SE; binomial-log without centre random; unadjusted binomial-log; explain convergence issue. Assess residual distributions visually; follow primary proposed method first; sensitivities transforms or nonparametric methods if skewness/violations. Received-data first; primary missing-data sensitivities. | Exact primary/secondary model and missingness specification |
| U013 | pp.16–17 §9.4 | Age=(randomization−birth date)/365.25years; missing BMI=kg/m². BMI<18.5;18.5–24.9;25.0–29.9;≥30.0. Operative grouping precedence colonic>noncolonic>nonbowel; uncategorizable omitted. Wound<15cm/≥15cm. Skin prep2%alcoholic chlorhexidine/aqueous betadine/all other. | Subgroup cutpoints and surgery coding |
| U014 | p.18 §9.4 | SSI yes if CDC positive day7/discharge, day30, theatre form OR wound antibiotics in diary within30days; no requires completed day30, no CDC SSI and no diary wound antibiotics. Diary on/before discharge excluded; theatre return after day30 assessment excluded. UK stay=discharge−surgery date days, same-day0. | Primary event ascertainment and UK stay |
| U015 | p.19 §9.4 | Wound complication excludes infection; yes any day7/day30 occurrence, no completed day30 with none. Management grade I conservative/on-ward, II antibiotics, III surgical/radiological, IV ITU, V death on SAE form (n/a here). | Complication definition/Clavien-Dindo denominator |
| U016 | p.20 §9.4 | Wound-related readmission binary from SSI/other-complication questions; no requires completed day30 with no such readmission. | Readmission endpoint |
| U017 | pp.20–23 §9.4 | SF12 detailed printed scoring formulas below; any missing item prevents PCS/MCS. | SF12 scoring and availability |
| U018 | p.23 §9.4 | EQ5D5L scored using5L→3L crosswalk; do not use stated England2018 value set. Any of5items missing prevents index computation. Index0 imputed at all postdeath time points. | EQ scoring/missing/death treatment |
| U019 | p.24 §9.4 | Any SAE within30days binary; count each SAE form event; count numbers exactly0,1,2,…; day7/day30 duplicate anastomotic leak/other listed events or prolonged-stay reports counted once. Day30 wound-related readmission contributes SAE. | Safety event versus patient denominator and duplicates |
| U020 | p.25 §9.5–9.6 | Primary n/% plus adjustedRR95% CI using mixed binomial log link, adjustedRD95% CI using identity link; P for adjustedRR. Binary wound complication/readmission use same method. UK stay means/SD and mixed linear adjustedMD95% CI; Australia excluded. | Primary RR/RD; binary outcomes; stay |
| U021 | p.26 §9.6 | Separate PCS/MCS and EQ index/health models; repeated-measures mixed linear, all baseline/posttimes; participant,treatment,baseline,time,minimisation factors fixed except centre random; categoricaltime; time×treatment; unstructured covariance; sandwich robust SE; time-specificMD95% CI. Pain separate day7/day30 continuous mixed linear as stay. | Repeated QoL model, baseline/time terms and covariance; pain |
| U022 | p.27 §9.6–9.8 | Patient/professional acceptability separately, continuous mixed linear as stay. Nonprespecified exploratory data simple n/% or mean/median and SD/IQR. Any SAE binary as primary, counts exactly1,2,… plus SAE/URSAE patient percentages and event totals by category/group. | Acceptability; safety status/model |
| U023 | p.28 §9.9 | Primary-only hypothesis-generating subgroup interactions: contamination4;stoma2;procedure3;wound<15/≥15;prep3;countryUK/Australia;BMI4;day30 method inperson/remotevideo-or-photo/remotewithoutvisualization;UK randomization before/after11March2020. Binomial subgroup×treatment; heterogeneityP and subgroupRR95% CI. | Entire subgroup inventory, including COVID and assessment method |
| U024 | p.29 §9.10 | Primary sensitivities PP; exclude early day30 forms;restrict30–44days;exclude diary-onlySSI;exclude return-to-theatre without priorSSI; missingworstSUNPD/bestcontrol and reverse. Restricted-window analysis retains SSI on eligible other forms even if day30 outside window. Missing=day30 absent and no SSI on otherforms. No subrandomizations; economics separately documented. | Primary sensitivities and missing case definition |
| U025 | p.30 §12–13 | SAS9.4orhigher and/or Stata17orhigher all analyses; references contextual only. | Software |
| U026 | pp.31–32 AppendicesA–C | Blank deviations shell; schema840, emergency laparotomy, primary skin closure incision≥5cm; randomization on closure; early day7/discharge(5–10days), day30(30–44days), diary between discharge/followup. Schedule visual mapping recorded below. | Assessment schedule and population |
| U027 | p.33 AppendixD1 | Blank flow counts: screened/excluded/randomized/postrandomizationexcluded; allocated SUNPD/control; adherence; deaths/withdrawals/lostFU; expected/completedday7 andday30; primary available=ITTanalysispopulation. Control lower completion label printed Day3; blank shell has no observed value. | Flow shell/status |
| U028 | pp.34–37 AppendicesD2–D3 | All baseline/surgery/COVID variables and units, detailed below; blank N/means/counts. | Baseline and operative descriptive display inventory |
| U029 | pp.38–39 AppendicesD4–D5 | Allocation/sizes10×20,10×30,10×40cm;PP3day/earlierdischarge as p12; reasons and missingoperationdate/day7form/finalremovaldate; skinreaction/dressingpain counts. Blank protocol-deviation byallocation shell. | Adherence and PP missingness |
| U030 | pp.40–46 AppendicesD6–D9 | All primary/secondary/safety/subgroup shells and explicit effect direction, detailed below. | Exact prespecified display inventory |

### U013: complete operative grouping

DOC-002 pp.16–17: colonic options2,4,5,6,7,8,13,26,28 (appendicectomy; left/right/subtotal/other colorectal resection; colostomy; Hartmann; colon bypass; colon abscess drainage). Noncolonic11,14,16,17,18,20,27,29 (gastric; ileostomy; ulcer bleed/perforation; intestinal perforation; small bowel resection; noncolon bypass; smallbowel/stomach abscess). Nonbowel1,3,10,12,21,22,23,24,25,30 (adhesiolysis; cholecystectomy; exploration; other; transplant; trauma; vascular; washout; hernia; nonbowel abscess). Unassigned9,15,19 (unspecified abscess, unspecified bypass, other intraabdominal malignancy). Multiple procedures use colonic then noncolonic then nonbowel precedence; no category yields omission. Seven skin preparation inputs are aqueous/alcoholic betadine,0.5%aqueous/alcoholic chlorhexidine,2%aqueous/alcoholic chlorhexidine,other.

### U017: full printed SF-12 scoring

[PLAN SF-12 coding](../../../joi240145supp1_prod_1741627844.87412.pdf#page=20), continued pp.21–23. SFQ1 excellent5/very good4.4/good3.4/fair2/poor1. SFQ2a moderate activity and SFQ2b stairs: limited a lot1/alittle2/not limited3. SFQ3a physical accomplished less,3b physical limited work,4a emotional accomplished less,4b emotional less careful,6c downhearted and7 social interference: all of the time1/most2/some3/little4/none5. SFQ5 pain interference: not at all5/little4/moderately3/quite a bit2/extremely1. SFQ6a calm and6b energy: all of the time5/most4/some3/little2/none1.

Domains: PF=Q2a+Q2b, score100(PF−2)/4; RP=Q3a+Q3b,100(RP−2)/8; RE=Q4a+Q4b,100(RE−2)/8; SF=Q7,100(SF−1)/4; MH=Q6a+Q6c,100(MH−2)/8; VT=Q6b,100(VT−1)/4; P=Q5,100(P−1)/4; GHP=Q1,100(GHP−1)/4. Printed z-score names are PF,RP,BP,GH,VT,SF,RE,MH: (value−mean)/SD, respectively81.18122/29.10558;80.52856/27.13526;81.74015/24.53019;72.19795/23.19041;55.59090/24.84380;83.73973/24.75775;86.41051/22.35543;70.18217/20.50597. Printed coefficients for AGG_PHYS in that order:0.42402,0.35119,0.31754,0.24954,0.02877,−0.00753,−0.19206,−0.22069; AGG_MENT:−0.22999,−0.12329,−0.09731,−0.01571,0.23534,0.26876,0.43407,0.48581. PCS=50+10AGG_PHYS; MCS=50+10AGG_MENT. Preserve printed domain names P/GHP and BP/GH instead of silently changing them. No missing item permitted for either summary.

### U026: fresh page-32 visual mapping

[PLAN schedule](../../../joi240145supp1_prod_1741627844.87412.pdf#page=32). Fresh-required page32 inspected completely using `.ai_paper_validation/review_1_6_2/preprocessing/support_mapper/DOC-002-p32.png`. Engine PyMuPDF1.26.4, CPU,200dpi; coordinator command: `.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py render joi240145supp1_prod_1741627844.87412.pdf --page 32 .ai_paper_validation/review_1_6_2/preprocessing/support_mapper/DOC-002-p32.png`. Thus DOC-002 partition is45reusable+1fresh-required=46mapped, DOC-0039reusable+0fresh-required=9mapped. Visual inspection suffices; no OCR.

Schedule columns pretheatre,intheatre,day7(−2/+3days),day14(±2days),day21(±2days),day30(+14days),day30+. Screening by oncall surgical team pretheatre; standard consent patient/research member pretheatre. UK delayed consent consultee/representative/research member pretheatre, patient/research member when capacity regained afterward. Randomization form starts pretheatre and completed surgeon/research member intheatre; intheatre form ideally operating surgeon/research member. Day7/discharge sooner wound assessment by research member atday7. EQ participant baseline/day7/day14/day21/day30; SF12 participant baseline/day7/day30. Diary daily after discharge until day 30 review, continues beyond30if ongoingSSI. Bluebelle wound-healing questionnaire atday30 independently participant then participant with blinded researcher reviewing wound. Day30 wound assessment blinded researcher inperson or remotevideo. SAE reports all events from intheatre throughday30 (SAEform or woundCRF if excluded from expedited reporting), relatedSAEs only beyond30. Return-to-theatre form completed researcher for returns. PI declaration at end of involvement. Footnotes pain assessed by researcher asking participant at day7/day30, patient dressing acceptability similarly atday7.

### U028: every baseline/surgery/COVID shell variable

DOC-002 pp.34–37, blank group SUNPD/control/total Ns. Ageyears mean and SD,minimum and maximum; sexfemale/male; BMI mean and SD,minimum and maximum; smokingnever/current/ex; diabetesno/yes and diet/tablets/insulin; albuming/L mean and SD,minimum and maximum; immunosuppressiveno/yes; clinical jaundice or bilirubin>50µmol/L; malignancyno/yes; fourcontaminationgroups; stomano/yes(preexisting/formed); ASAI–V. Antibioticsnone/during/induction/both, postoperative continuationno/yes; seven skinprepoptions. COVID symptomsno/yes, antibodyprovenno/yes, SARSCoV2screenpositive/negative/resultsunknown/notscreened; positive swab/clinicalCOVIDno-or-unknown/yes and elapseddiagnosisday0,1–7,8–14,15–28days,5–6weeks,7–8weeks,3–4months,5–6months,6+months. Procedure options and3groups/n/a; approachopenmidline/opennonmidline/laparoscopicassisted-or-converted; incisioncm mean and SD,minimum and maximum,<15/≥15; WHOsafetychecklist; MRSAcolonization; malignancyyes-suspected/no; bloodloss<100,100–500,501–1000,>1000mL; transfusion; inotropes; woundedgeprotector; triclosansutures; anaestheticcatheters; incisedrapeno/iodine/plain; woundwashno/betadine/salinewater/other; gloves/instrumentchange; skinclosurestaples/interrupted/continuous; operating/fascia/skin surgeon gradesconsultant/registrar/SHO/ANP; durationminutesmean and SD,minimum and maximum. These are prospective categories, with no observed counts.

### U030: every analysis shell and direction label

[PLAN primary shell](../../../joi240145supp1_prod_1741627844.87412.pdf#page=40): SSIyes/no n bygroup/total; adjustedRR andRD effect,95% CI,P columns; adjust minimisation with random centre; control reference; RR<1 andRD<0 favor SUNPD. Ascertainment breakdown day7/discharge,theatre,day30,diary anddiaryonly for eacharm.

p41 binary wound complication/readmission with sameRR/RDcolumns and directions; wound typegranuloma/seroma/haematoma/dehiscence/other by gradesI–V andarm. p42 UKstay,PCS/MCSbaseline/day7/day30,painday7/day30: N,mean and SD,minimum and maximum,adjustedMD95% CI/P,baseline noMD. p43 EQindex/health baseline/day7/day14/day21/day30 same summary; p44 patientacceptabilityday7 andUKprofessionalacceptability, MD adjustedminimisation/random centre/baselinewhereavailable. p45 patientsanySAEyes/no adjustedRR95% CI/P; exact1,2,…SAEpatientcounts andtotalevents; incidence-rate-ratio footnote adjustedminimisation; SAEcategorypatientn/% versus eventn distinguished. CategoriesprolongedstaySSI/otherwound,readmissionSSI/otherwound,anastomoticleak,intraabdominalsepsis,intraperitonealcollection,thromboembolism,nonwoundinfection,cardiac/CNS,otherSAEs. RR>1/higher countmeasureworseSUNPD. p46 subgroup n/group,interactionP,RR95% CI; contamination4/stoma2/procedure3/BMI4/wound≤15cm versus>15cm/prep3/country2/assessment3. Preserve p46≤15/>15 separately from p17/p28<15/≥15. No COVID rows printed in p46 shell, while p28 expressly specifies UKCOVID-date subgroup. All shell values blank.

## Observed supplementary results

All numeric cells below were read from the reusable text/layout and inspected on matching page images. I=iNPWT; C=surgeon's preference; T=total. Counts at different QoL timepoints are contributors to that display. These modeled differences are not labeled crude.

### U031: adherence (eTable1, DOC-003 p3)

[REPORT eTable1](../../../joi240145supp3_prod_1741627844.89412.pdf#page=3). Group denominators I411,C410,T821. Received allocation no6(2%),8(2%),14(2%); yes404(98%),402(98%),806(98%); unable1(<1%),0(0%),1(<1%). One CRF lacked intervention tick and cannot compute adherence. Applied SUNPD404,8,412; occlusive4,353,357; glue3,50,53; none0,1,1; other0,9,9. Dressing choices not mutually exclusive and can exceed participants. Match main flow/intervention and SAP received-versus-PP distinction.

### U032: complete QoL descriptive and inferential rows

[REPORT SF12](../../../joi240145supp3_prod_1741627844.89412.pdf#page=3). Each descriptive cell is n;mean[SD];min–max. Inference columns are modeled I−C difference,95% CI,P, followed by one treatment×time interactionP per component. Footnotes: all minimisation variables adjusted,centre random,treatment×time included; SF12 range0–100,higher is better; control reference,positive MD indicates better outcomes for I.

| Component/time | I | C | T | MD [95% CI]; P |
|---|---|---|---|---|
| PCS baseline | 306;39.1[11.7];12.7–66.9 | 297;39.5[11.3];13.4–62.1 | 603;39.3[11.5];12.7–66.9 | — |
| PCS day7 | 248;30.4[9.8];8.7–66.8 | 232;30.5[9.5];7.9–62.1 | 480;30.5[9.6];7.9–66.8 | 0.130[−1.755,2.014];.89 |
| PCS day30 | 235;36.1[9.8];9.7–60.7 | 211;37.2[10.2];15.1–57.8 | 446;36.6[10];9.7–60.7 | −0.861[−2.829,1.106];.39 |
| MCS baseline | 306;44.8[13];7.7–70.6 | 297;45.5[13.1];10.6–70.6 | 603;45.1[13];7.7–70.6 | — |
| MCS day7 | 248;40.6[13.2];8.1–71.2 | 232;42.8[12.4];8.5–70.6 | 480;41.7[12.9];8.1–71.2 | −2.190[−4.470,0.088];.06 |
| MCS day30 | 235;46.9[11.8];11.5–69.7 | 211;47.7[12];12.4–73 | 446;47.3[11.9];11.5–73 | −1.904[−4.276,0.469];.12 |

PCS interactionP=.44; MCS=.84. Matching key SAP p26 repeated-measures model, p42 shells, main quality-of-life narrative.

[REPORT EQ5D tables](../../../joi240145supp3_prod_1741627844.89412.pdf#page=4). Index range−0.594to1,healthrange0to100;higher is better,control reference,positive MD indicates better outcomes for I. Same model footnote as SF12. All hyphens in printed intervals were inspected in the image; eTable4 day7 prints `(-2.389 -4.557)` and day21 `(-5.926 -1.597)`, without a spaced separator after the lower limit. Preserve that exact display string alongside the endpoints transcribed as lower/upper according to the table's range syntax. No candidate inference is made here.

| Scale/time | I | C | T | MD; printed 95% CI; P |
|---|---|---|---|---|
| Index baseline | 345;0.57[0.35];−0.59–1 | 339;0.55[0.35];−0.59–1 | 684;0.56[0.35];−0.59–1 | — |
| Index day7 | 292;0.44[0.32];−0.41–1 | 283;0.49[0.30];−0.44–1 | 575;0.46[0.31];−0.44–1 | −0.057;(-0.104 -0.010);.02 |
| Index day14 | 233;0.56[0.26];−0.15–1 | 238;0.56[0.29];−0.24–1 | 471;0.56[0.28];−0.24–1 | −0.023;(−0.072,0.027);.37 |
| Index day21 | 229;0.60[0.28];−0.41–1 | 231;0.61[0.28];−0.22–1 | 460;0.60[0.28];−0.41–1 | −0.017;(−0.067,0.032);.49 |
| Index day30 | 289;0.66[0.27];−0.33–1 | 264;0.65[0.29];−0.17–1 | 553;0.65[0.28];−0.33–1 | −0.007;(−0.054,0.040);.78 |
| Health baseline | 340;46.9[26.6];0–100 | 336;47.9[26.8];0–100 | 676;47.4[26.7];0–100 | — |
| Health day7 | 289;54.9[23];0–100 | 278;54.3[21.6];0–100 | 567;54.6[22.3];0–100 | 1.084;(-2.389 -4.557);.54 |
| Health day14 | 231;60.8[20.1];0–100 | 226;60.8[19.5];0–95 | 457;60.8[19.8];0–100 | −0.668;(−4.379,3.042);.72 |
| Health day21 | 222;65.5[20.1];5–100 | 215;66.6[19.1];0–100 | 437;66[19.6];0–100 | −2.164;(-5.926 -1.597);.26 |
| Health day30 | 281;71.4[19.1];10–100 | 250;71.7[18.7];0–100 | 531;71.5[18.9];0–100 | −2.010;(−5.559,1.540);.27 |

Index interactionP=.10;health=.22. eTable3 day7 string has only one hyphen between printed lower−.104 and .010; extraction records exact typography, with signed statistical interpretation reserved to source recheck/checkers. Matching keys SAP p23 scoring/death rule,p26model,p43shells/mainQoL.

### U033: complete wound complication and SSI ascertainment counts

[REPORT grades](../../../joi240145supp3_prod_1741627844.89412.pdf#page=5). GradesI conservative/onward;IIantibiotics;IIIsurgical/radiological;IVITU;Vdeath. Entries are complication-type counts; participants can have>1type, counted separately.

| Arm/type | I | II | III | IV | V | Total |
|---|---:|---:|---:|---:|---:|---:|
| iNPWT granuloma | 7 | 1 | 0 | 0 | 0 | 8 |
| iNPWT seroma | 9 | 0 | 1 | 0 | 0 | 10 |
| iNPWT haematoma | 7 | 0 | 0 | 0 | 0 | 7 |
| iNPWT dehiscence | 34 | 14 | 3 | 0 | 0 | 51 |
| iNPWT skin reaction | 5 | 0 | 0 | 0 | 0 | 5 |
| iNPWT other | 2 | 1 | 0 | 0 | 0 | 3 |
| iNPWT total | 64 | 16 | 4 | 0 | 0 | 84 |
| Control granuloma | 7 | 0 | 0 | 0 | 0 | 7 |
| Control seroma | 12 | 3 | 1 | 0 | 0 | 16 |
| Control haematoma | 2 | 0 | 0 | 0 | 0 | 2 |
| Control dehiscence | 32 | 13 | 5 | 0 | 0 | 50 |
| Control skin reaction | 2 | 0 | 0 | 0 | 0 | 2 |
| Control other | 4 | 1 | 1 | 0 | 0 | 6 |
| Control total | 59 | 17 | 7 | 0 | 0 | 83 |

iNPWTother retainedstaple,sinus,missing;controlother intramuscularleftiliacushematoma,prominentstitch,soreonstitch,smallfatcollection,abdominalcompartmentsyndrome,enteroatmosphericfistula. Match main wound-complication patient totals only with explicit nonexclusive-type footnote; SAP p19gradecoding,p41shell.

[REPORT SSI by timepoint](../../../joi240145supp3_prod_1741627844.89412.pdf#page=6): day7/discharge37/43;theatre4/7;diary38/25;day30109/107;day7-or-theatreonly0/1;diaryonly3/0 (I/C). Earlier SSI is also day30 if assessment completed; earlier confirmedSSI withoutday30 counts primary. Lasttwo rows italicized exclusive additions. Therefore primary ascertainment match is109+0+3=112I and107+1+0=108C; firstfour rows overlap and must not sum as distinct participants. No denominator is printed here. Match main primaryeventcounts and SAP p18,p29,p40.

### U034: complete figures and definitions

[REPORT CDC/PRECIS](../../../joi240145supp3_prod_1741627844.89412.pdf#page=7). PRECIS2 radar scale1–5 across eligibility,recruitment,setting,organisation,flexibilitydelivery,flexibilityadherence,followup,primaryoutcome,primaryanalysis. Visual vertices respectively5,5,5,5,4,4,3,5,4 (reading of chart vertices, no separately printed score table). This characterizes design rather than efficacy. CDC SSIwithin30days requires purulentdrainage OR organismsonwoundswab OR woundopensspontaneously/clinician AND pain/tenderness,swelling,redness,heatorfever>38°C OR diagnosisclinician/imaging. Match SAP p7,p18 andmainprimarydefinition; no diary criterion is drawn in this figure.

[REPORT sensitivities](../../../joi240145supp3_prod_1741627844.89412.pdf#page=8). RR95% CI;control reference;leftRR<1 favorsiNPWT,rightRR>1 favorssurgeonpreference; axis0.50,1.00,2.00. No P value printed.

| Analysis | RR | 95% CI | Definition / matching SAP |
|---|---:|---|---|
| Primary | 1.03 | 0.83,1.28 | ITT;mainprimary/SAP p25 |
| Per protocol | 1.00 | 0.80,1.25 | SAP p12,p29adherence |
| Sensitivity1 | 0.95 | 0.76,1.19 | ITTexcludesday 30 formsbeforeday30;includeslate;SAP p29 |
| Sensitivity2 | 0.99 | 0.79,1.23 | ITTforms30–44days;+14window;SAP p29 |
| Sensitivity3 | 1.01 | 0.81,1.26 | ITTexcludesdiaryonlySSI;SAP p29 |
| Sensitivity4 | 1.02 | 0.82,1.27 | ITTexcludesreturntotheatrewithoutpriorSSI;SAP p29 |
| Sensitivity5 | 1.19 | 0.96,1.46 | MissingSSIinI,no SSIinC;SAP p29 |
| Sensitivity6 | 0.89 | 0.72,1.10 | Missingno SSIinI,SSIinC;SAP p29 |

[REPORT tipping point](../../../joi240145supp3_prod_1741627844.89412.pdf#page=9). GraphA horizontal missingeventrate intervention%,GraphB control%;both0to100by5,21points each. VerticalriskratioSUNPDversuscontrolticks0,.25,.5,.75,1,1.25,1.5;dashednull1,pointestimatesandverticalintervals. CaptionGraphAevenallmissing SSIinSUNPD/noneincontroldoesnotstatisticallyfavorcontrol;GraphBviceversadoesnotstatisticallyfavorSUNPD. All 42 drawn intervals cross null 1. A estimates rise from approximately 1.03 to 1.19; B fall from approximately 1.03 to .89. Exactnumericalvaluesofintermediatepointsarenotprinted andcannotbeclaimed;endpointrowsmatchp8sensitivities5/6,subjecttocaptionpopulation. BothnotesRR<1favorsSUNPD. These are visual values and conclusions, not new calculations.

## Completeness and limitations

All 55 assigned pages opened and mapped: 46 SAP pages and 9 results pages. Revised reusable/fresh partition: 54 + 1 = 55; fresh page 32 visual inspection closed its content gap. All eTables 1–6 (5a/5b separately) and eFigures 1–4 are mapped, including graphical data absent from native extraction. There are 34 local extraction families. No scientific coverage gap remains. Derivative versions for reusedlayout/images are not retained; exact source confirmation remains required for candidate evidence. Tipping point intermediate estimates/limits lack printed numerical cells and are recorded at truthful visual precision. Administrative/reference units are explicitly mapped as not independent results. Sources and reusable assets were preserved; no old candidate, checker or report conclusions were read.
# Protocol quantitative evidence map — DOC-004

## Scope and provenance

Fresh scientific mapping of DOC-004, `joi240145supp4_prod_1741627844.90412.pdf`, all PDF pages 1–48. Document role: **PLAN**, established by prospective trial protocol, protocol version, amendments, and specified procedures; no report-result document is included in this shard. Runtime agent: `/root/protocol_mapper`; model and effort recorded by coordinator. Ownership is this artifact only. DOC-002 and DOC-003 are assigned to another support mapper; no content from their maps or sources is inferred here. Matching main-paper keys below are semantic locators for later comparison, not claims about report content.

Required controls read completely: `QUALITY_CONTROL_SCOPE.md`, `workflow_1_6_2/review_contract.md`, current source inventory, source coverage, evidence-asset inventory, tooling record, and coverage manifest. No legacy scientific conclusions, candidate selections, or reports were read.

Reusable transcription assets, each approved USABLE and source-linked by curator:

- `.ai_paper_validation/review_1_5_3/preprocessing/support_mapper/DOC-004_pp01-24_layout.txt`: PDF pp. 1–24, form-feed records 1–24; 88452 characters.
- `.ai_paper_validation/review_1_5_3/preprocessing/support_mapper/DOC-004_pp25-48_layout.txt`: PDF pp. 25–48, form-feed records 1–24; 84035 characters.

Engine: legacy geometric layout extraction, engine/version not retained. Both complete blocks were read page by page using `awk 'BEGIN {RS="\f"} ...'` in disjoint eight-page batches, adding page numbers to tool output only. No derivative was generated or source/reused asset modified. Complete recoverable text exists for every assigned page. No fresh-required pages, OCR, rendering, Office extraction, formula/cached-value distinction, or GPU invocation was needed in this shard. The source is PDF, not a workbook. Exact-source visual confirmation remains the subsequent recheck's authority if a candidate is registered.

Local IDs P001–P034 are mapping locators only; coordinator/checkers assign global N/S IDs. A row can contain several linked statements that belong to one coherent specification. No candidate diagnosis or inclusion decision is made here.

## Complete page coverage

PDF pagination agrees with printed protocol pagination 1–48. Each page was opened, including administrative and reference content. `NO_APPLICABLE` means no new result-relevant quantitative relationship on that page, not unread or omitted content.

| PDF page | Content examined and mapped | Local relationships | Coverage |
|---:|---|---|---|
| 1 | Protocol title, version 4.0, 16 March 2021 | P001 | COMPLETE |
| 2 | Full amendment table, versions 2.0/3.0/4.0 and changes to outcomes, review windows, analysis | P001, P002 | COMPLETE |
| 3 | Funding/support, study registration and reference identifiers; no analysis specification | NO_APPLICABLE | COMPLETE |
| 4 | Chief investigator signature, protocol version/date; prospective amendment approval | P001 | COMPLETE |
| 5 | Principal investigator signature, protocol version/date | P001 | COMPLETE |
| 6 | Trial management/steering committee members; no quantitative relationship | NO_APPLICABLE | COMPLETE |
| 7 | DMC membership, administrative contacts; no quantitative relationship | NO_APPLICABLE | COMPLETE |
| 8 | Trial summary: primary objective, 840 participants, 1:1, eligibility, intervention, primary/secondary outcomes | P003, P004, P005, P006, P007, P008 | COMPLETE |
| 9 | Contents references to substantive sections; no additional quantitative relationship | NO_APPLICABLE | COMPLETE |
| 10 | Contents references to assessments/safety/data sections; no additional quantitative relationship | NO_APPLICABLE | COMPLETE |
| 11 | Contents references to statistical/health-economic sections and appendices; no additional relationship | NO_APPLICABLE | COMPLETE |
| 12 | Historical/background burden/rates and rationale, distinguished from planned trial inputs | P034 | COMPLETE |
| 13 | Design, controls, 1:1, timing/minimisation, SSI 30 days, wound-review windows/blinding | P003, P004, P005, P007, P009, P010 | COMPLETE |
| 14 | PICO 80 mmHg, 7 days/discharge, COVID-related pathways/status collection | P005, P011 | COMPLETE |
| 15 | Feasibility target/traffic lights/definitions and green continuation statement | P012 | COMPLETE |
| 16 | Primary/secondary objectives, Bluebelle substudy, pragmatic design/site assessment procedures | P003, P007, P008, P013 | COMPLETE |
| 17 | Full eligibility including incision/age/previous surgery/reoperation and laparoscopic conversion | P006 | COMPLETE |
| 18 | Consent, 30-day review, weekly reminders; no new inferential model | P014 | COMPLETE |
| 19 | Temporary capacity, exclusions/withdrawal, anticipated <2% without capacity by day 30, retained data | P015 | COMPLETE |
| 20 | Same retained-data provision for Scotland; Australian incapacity exclusion | P015 | COMPLETE |
| 21 | Screening/randomisation, individual level, 1:1, timing and minimisation introduction | P003, P004 | COMPLETE |
| 22 | Minimisation covariates/random element, blinding, intervention/control duration/replacement | P004, P005, P010 | COMPLETE |
| 23 | Dressing application/replacement, maximum 7 days, permitted closure/control dressings | P005 | COMPLETE |
| 24 | Reoperation treatment rules; CDC primary definition; initial secondary definitions | P005, P007, P008, P016 | COMPLETE |
| 25 | Remaining secondary endpoints/scales/timepoints; baseline instruction; day-7 window/removal | P008, P009, P017, P018 | COMPLETE |
| 26 | Day-7 removal example, questionnaires/inpatient/outpatient diary, day-30 window/method/grade | P009, P017, P018, P019 | COMPLETE |
| 27 | Day-30 pain/QoL, ongoing SSI diaries, acceptability, Bluebelle substudy | P008, P013, P017, P019, P020 | COMPLETE |
| 28 | Bluebelle independent/assessor/CDC comparison and external validation | P013 | COMPLETE |
| 29 | Full schedule table including all time windows, questionnaires, diary, pain/acceptability footnotes | P009, P017, P018, P019, P021 | COMPLETE |
| 30 | Withdrawal types/data retention/recovery and sensitivity statement; safety collection context | P022 | COMPLETE |
| 31 | AE selection and complete SAE reporting versus routine-CRF categories | P023 | COMPLETE |
| 32 | AE/SAE reporting period, related events after 30 days, causality scale | P023, P024 | COMPLETE |
| 33 | Independent safety classification, DMC safety review, source-data introduction | P024 | COMPLETE |
| 34 | Source data, units, questionnaires and independent Bluebelle completion | P013, P017, P025 | COMPLETE |
| 35 | Missing/ambiguous data queries, validation/security administration | P025 | COMPLETE |
| 36 | Archiving/training and central monitoring; no new inferential relationship | NO_APPLICABLE | COMPLETE |
| 37 | Monitoring, end-of-trial 12 months after last day-30 review and analysis-ready database | P026 | COMPLETE |
| 38 | Entire sample-size section, general analysis conventions, primary and binary secondary models | P027, P028, P029, P030 | COMPLETE |
| 39 | Continuous/repeated analysis, primary-outcome subgroups, missing/sensitivity, interim/final, economics | P031, P032, P033 | COMPLETE |
| 40 | Economic evaluation, QALYs, imputation/sensitivity/CEACs, DMC remit and schedule | P033 | COMPLETE |
| 41 | Interim stopping considerations and p<.001/final .05, ethics administration | P033 | COMPLETE |
| 42 | Ethics/confidentiality/funding/indemnity; no new quantitative relationship | NO_APPLICABLE | COMPLETE |
| 43 | Publication/authorship administration (six-participant authorship threshold peripheral) | NO_APPLICABLE | COMPLETE |
| 44 | References 1–21, historical bibliographic numeric content only | NO_APPLICABLE | COMPLETE |
| 45 | References 22–29, historical bibliographic numeric content only | NO_APPLICABLE | COMPLETE |
| 46 | Abbreviations including outcome/inferential/economic scale names | P007, P017, P023, P033 | COMPLETE |
| 47 | AE/SAE/event definitions, source-data definition | P023, P024, P025 | COMPLETE |
| 48 | Scottish nearest-relative hierarchy and complete Clavien-Dindo wound complication table | P016 | COMPLETE |

Mapped units: 48/48. Reusable-backed: 48. Fresh-required: 0. Scientific gaps: 0. Administrative/reference-only pages are explicitly mapped above.

## Source-grounded relationships

### P001 — Protocol identity and supplied version

Locations: [PDF p. 1](../../../joi240145supp4_prod_1741627844.90412.pdf#page=1), [p. 2](../../../joi240145supp4_prod_1741627844.90412.pdf#page=2), [p. 4](../../../joi240145supp4_prod_1741627844.90412.pdf#page=4), [p. 5](../../../joi240145supp4_prod_1741627844.90412.pdf#page=5). PLAN throughout. Title/version and headers: SUNRRISE, version 4.0, 16 March 2021. Amendment table prints amendment 1: 29-Oct-18, version 2.0, substantial; amendment 2: 05-Aug-20, version 3.0, substantial; amendment 3: 25-Mar-21, version 4.0, non-substantial. Only current version 4.0 text and retrospective summaries of earlier changes are supplied in this document. Do not reconstruct earlier full specifications from summaries. Matching key: protocol version/date and disclosed amendments.

### P002 — Prospective amendments bearing on quantitative design

Location: [PDF p. 2](../../../joi240145supp4_prod_1741627844.90412.pdf#page=2). Version 2.0 added pain as a secondary outcome/how/when assessed, ongoing-SSI diary beyond day 30, death as reportable SAE and ileus as non-expedited SAE, and clarified statistical/economic sections. Version 3.0 expanded setting to Australia; changed eligibility/follow-up for COVID-19; clarified length-of-stay parameters; relaxed day-7 review by five days and day-30 review by seven days; allowed remote video or telephone assessments; clarified statistical analysis. Version 4.0 clarified statistical analysis and data security, changed terminology for patient acceptability/pain collection tools, and clarified background/feasibility. These are disclosed changes, not numerical report results. Matching key: prespecification/outcome status and assessment windows, with amendment context.

### P003 — Design, comparator, randomisation and sample population

Locations: [PDF p. 8](../../../joi240145supp4_prod_1741627844.90412.pdf#page=8), [p. 13](../../../joi240145supp4_prod_1741627844.90412.pdf#page=13), [p. 16](../../../joi240145supp4_prod_1741627844.90412.pdf#page=16), [p. 21](../../../joi240145supp4_prod_1741627844.90412.pdf#page=21). International multicentre pragmatic prospective phase III two-arm RCT, internal feasibility phase, UK/Australia. 840 participants, individual randomisation, 1:1 SUNPD versus surgeon's preferred dressing. Randomisation in theatre after commencement of skin closure, after intraoperative eligibility confirmed. Control may be conventional occlusive dressing, skin glue as dressing, or no dressing; excludes another SUNPD. Matching keys: randomized participant totals, analysis unit, intervention/reference contrast, design.

### P004 — Minimisation and allocation

Locations: [PDF p. 13](../../../joi240145supp4_prod_1741627844.90412.pdf#page=13), [p. 21](../../../joi240145supp4_prod_1741627844.90412.pdf#page=21), [p. 22](../../../joi240145supp4_prod_1741627844.90412.pdf#page=22). Covariates: contamination (clean, clean contaminated, contaminated, dirty), stoma presence (yes/no), recruiting site. Existing versus newly formed stoma is ascertained but **not** a minimisation distinction. Algorithm includes an unspecified random element; no numeric random-element probability is given here. Matching keys: minimisation strata, model-adjustment covariates, subgroup variables.

### P005 — Randomized intervention intensity/duration and treatment rules

Locations: [PDF p. 8](../../../joi240145supp4_prod_1741627844.90412.pdf#page=8), [p. 14](../../../joi240145supp4_prod_1741627844.90412.pdf#page=14), [p. 22](../../../joi240145supp4_prod_1741627844.90412.pdf#page=22), [p. 23](../../../joi240145supp4_prod_1741627844.90412.pdf#page=23), [p. 24](../../../joi240145supp4_prod_1741627844.90412.pdf#page=24), [p. 25](../../../joi240145supp4_prod_1741627844.90412.pdf#page=25), [p. 26](../../../joi240145supp4_prod_1741627844.90412.pdf#page=26). Smith & Nephew PICO portable topical dressing; negative pressure **80 mmHg**. Maximum **7 days** from index operation or discharge, whichever sooner. Routine replacement discouraged; clinical replacement uses another SUNPD, one extra dressing per box. Saturated dressing can be replaced during seven-day treatment. If review on day 5, remove on day 5; if review on day 9, remove SUNPD by day 7 and use standard dressing until review. Reoperation within seven days: reapply same allocated type, retaining original seven-day treatment period; later reoperation: surgeon's preference excluding SUNPD regardless of allocation. Skin closure sutures/staples; glue cannot be primary closure, but may be control dressing. Control options exclude silver/honey/iodine dressings and other negative-pressure dressing. Matching keys: intervention pressure and intended exposure, adherence, crossover/reoperation treatment handling.

### P006 — Eligibility affecting trial population

Locations: [PDF p. 8](../../../joi240145supp4_prod_1741627844.90412.pdf#page=8), [p. 17](../../../joi240145supp4_prod_1741627844.90412.pdf#page=17), [p. 20](../../../joi240145supp4_prod_1741627844.90412.pdf#page=20). Emergency non-elective laparotomy, primarily closed skin, incision at least **5 cm**; UK age **≥16**, Australia **≥18**; consent or temporary-incapacity representative in UK only; willingness/ability for day-30 follow-up. Exclusions: abdominal surgery in previous **3 months**, anticipated reopening within **30 days**. Laparoscopic procedures remaining with incisions <5 cm not randomized; conversion to open with incision described as >5 cm enables randomisation after closure starts. Australian patients without consent capacity not enrolled. Matching key: randomized eligibility/population.

### P007 — Primary outcome status, threshold, definition and ascertainment

Locations: [PDF p. 8](../../../joi240145supp4_prod_1741627844.90412.pdf#page=8), [p. 13](../../../joi240145supp4_prod_1741627844.90412.pdf#page=13), [p. 16](../../../joi240145supp4_prod_1741627844.90412.pdf#page=16), [p. 24](../../../joi240145supp4_prod_1741627844.90412.pdf#page=24), [p. 38](../../../joi240145supp4_prod_1741627844.90412.pdf#page=38). **Primary**: SSI within **30 days** of index surgery according to CDC criteria, binary yes/no. Infection within 30 days AND at least one: purulent wound drainage; organisms detected from wound swab; wound opened spontaneously/by clinician AND pain/tenderness, localized swelling, redness, heat or systemic fever **>38°C**; diagnosis of SSI by clinician or imaging. Ascertainment by day-7/discharge review, blinded day-30 trained assessor and intervening patient diary. Summary objective wording says SSI at 30 days; definition specifies within 30 days. This is infection presence over window, not only point prevalence. Matching key: primary SSI definition/components/time horizon and event/denominator.

### P008 — Complete secondary-outcome status inventory

Locations: [PDF p. 8](../../../joi240145supp4_prod_1741627844.90412.pdf#page=8), [p. 16](../../../joi240145supp4_prod_1741627844.90412.pdf#page=16), [p. 24](../../../joi240145supp4_prod_1741627844.90412.pdf#page=24), [p. 25](../../../joi240145supp4_prod_1741627844.90412.pdf#page=25), [p. 27](../../../joi240145supp4_prod_1741627844.90412.pdf#page=27). Explicitly **secondary**, with no separately named key-secondary hierarchy in this protocol: (1) length of hospital stay index surgery to discharge, **UK patients only** in detailed definition; (2) wound complications within 30 days, Clavien-Dindo grade; (3) hospital readmission for wound-related complications within 30 days, including SSI, breakdown/dehiscence, seroma, wound-related pain; (4) HRQoL SF-12 and EQ-5D-5L; (5) primary-laparotomy site pain, 10-point visual analogue scale, days 7/30; (6) SAEs up to 30 days; (7) cost-effectiveness/resource-use diary; (8) patient dressing acceptability, 10-point VAS, day 7 or discharge; (9) healthcare professional SUNPD acceptability/ease of application, maintenance/monitoring and overall experience, **UK only** user survey. Pain is present in detailed section though summary list omits it; amendment explicitly records its addition. Matching keys: reported endpoint status, length-of-stay population, readmission composite, pain/QoL/acceptability/safety outcomes.

### P009 — Assessment windows distinct from event window

Locations: [PDF p. 13](../../../joi240145supp4_prod_1741627844.90412.pdf#page=13), [p. 25](../../../joi240145supp4_prod_1741627844.90412.pdf#page=25), [p. 26](../../../joi240145supp4_prod_1741627844.90412.pdf#page=26), [p. 29](../../../joi240145supp4_prod_1741627844.90412.pdf#page=29). Day-7 wound assessment: **days 5–10**, or discharge if earlier; schedule labels **−2/+3 days**. Day-30 wound review: **days 30–44**, day 0=randomisation; schedule **+14 days**. EQ-5D assessments days 14 and 21 carry **±2 days** in schedule. Allowing ascertainment after day 30 does not itself redefine within-30-day primary event window. Matching keys: timing/windows for outcome assessments and extraction of 30-day result.

### P010 — Blinding relevant to endpoint ascertainment

Locations: [PDF p. 13](../../../joi240145supp4_prod_1741627844.90412.pdf#page=13), [p. 22](../../../joi240145supp4_prod_1741627844.90412.pdf#page=22), [p. 25](../../../joi240145supp4_prod_1741627844.90412.pdf#page=25), [p. 26](../../../joi240145supp4_prod_1741627844.90412.pdf#page=26). Participants/day-7 inpatient assessors unblinded because dressing identifiable. Day-30 trained assessor blinded and not previously involved in participant care; operating note preferably generic trial-allocation wording. In-person day-30 preferred, real-time video when unavailable, telephone as last resort. Matching key: primary outcome assessment method and assessor blinding.

### P011 — COVID context and collected factor

Location: [PDF p. 14](../../../joi240145supp4_prod_1741627844.90412.pdf#page=14). UK recruitment paused centrally 20 March 2020; Australia continued at reduced rate. Eligibility/follow-up pathways amended. All SARS-CoV-2 status categories eligible (positive, negative, untested); status collected to allow potential assessment in analysis. No definite prespecified COVID subgroup model appears in this paragraph. Calendar information is contextual, not a planned test. Matching key: disclosed follow-up amendment and possible analysis factor.

### P012 — Feasibility quantities, decision rules and outcome

Location: [PDF p. 15](../../../joi240145supp4_prod_1741627844.90412.pdf#page=15). Six-month internal phase target **70 patients** at **≥5 sites**. Recruitment proportion=achieved/70; adherence=appropriate dressing successfully applied **≥24 hours**; dropout=complete withdrawal/no further collection. Green: recruitment **>70%**, adherence **>80%**, dropout **<20%**; all three required for unchanged continuation. Amber: recruitment **50–70%**, adherence **50–80%**, or dropout **20–35%**; one or more triggers review/possible changes. Red: recruitment **<50%**, adherence **<50%**, or dropout **>35%**; one or more triggers discussion with TSC/funder. Safety DMC review required. Outcome statement: all criteria GREEN, no safety issue, TSC approved continuation without protocol change. No realized numerators/denominators are printed here. Matching key: internal-feasibility stopping/continuation and adherence definition.

### P013 — Prespecified Bluebelle substudy

Locations: [PDF p. 16](../../../joi240145supp4_prod_1741627844.90412.pdf#page=16), [p. 27](../../../joi240145supp4_prod_1741627844.90412.pdf#page=27), [p. 28](../../../joi240145supp4_prod_1741627844.90412.pdf#page=28), [p. 34](../../../joi240145supp4_prod_1741627844.90412.pdf#page=34). Compare patient-completed independent pre-day-30 questionnaire, assessor-completed day-30 questionnaire and CDC clinical SSI outcome, including SSI diagnosed at any trial assessment. External validation access to limited anonymised data. Day-30 inpatients need not complete/repeat Bluebelle. No diagnostic cut-point, test or sample-size formula is specified here. Matching key: planned substudy, questionnaire population and matching CDC outcome.

### P014 — Consent follow-up context

Location: [PDF p. 18](../../../joi240145supp4_prod_1741627844.90412.pdf#page=18). Participants informed of one additional follow-up at 30 days, post-discharge diary and weekly telephone/text reminders. No minimum interval between information and consent. These are prospective ascertainment procedures, not event results. Matching key: diary/follow-up collection context.

### P015 — Capacity and retained analysis data

Locations: [PDF p. 19](../../../joi240145supp4_prod_1741627844.90412.pdf#page=19), [p. 20](../../../joi240145supp4_prod_1741627844.90412.pdf#page=20). Long-term cognitive incapacity excluded in England/Wales/Scotland; temporary incapacity may enter with appropriate consultee/legal representative. Anticipated **<2%** not regaining capacity by 30 days: already treated/reached primary outcome; data retained for final analysis, consent sought later when practical. Refusal/withdrawal respected. Australia unable to consent excluded. Matching key: analysis population and consent-related data availability.

### P016 — Wound-complication grade definition

Locations: [PDF p. 24](../../../joi240145supp4_prod_1741627844.90412.pdf#page=24), [p. 26](../../../joi240145supp4_prod_1741627844.90412.pdf#page=26), [p. 48](../../../joi240145supp4_prod_1741627844.90412.pdf#page=48). Record highest Clavien-Dindo wound-complication grade since surgery at day-30 review; secondary outcome within 30 days. Appendix table: I=deviation without surgical/endoscopic/radiological intervention, including bedside opening and conservative/on-ward management; II=drug treatment beyond grade-I permitted drugs, including antibiotics, transfusion/TPN; III=surgical/endoscopic/radiological intervention; IV=life-threatening complication requiring intensive care (CNS examples excluding TIA); V=death, recorded via SAE form rather than wound-management action. Scottish hierarchy also inspected on p48; no numeric result relevance. Matching key: ordinal categories, highest grade, death classification and binary complication summaries.

### P017 — HRQoL and pain scale/timepoints

Locations: [PDF p. 25](../../../joi240145supp4_prod_1741627844.90412.pdf#page=25), [p. 26](../../../joi240145supp4_prod_1741627844.90412.pdf#page=26), [p. 27](../../../joi240145supp4_prod_1741627844.90412.pdf#page=27), [p. 29](../../../joi240145supp4_prod_1741627844.90412.pdf#page=29), [p. 34](../../../joi240145supp4_prod_1741627844.90412.pdf#page=34), [p. 39](../../../joi240145supp4_prod_1741627844.90412.pdf#page=39). SF-12 at baseline/day7/day30; EQ-5D-5L baseline/day7/day14/day21/day30. Baseline instructed to reflect health before acute episode leading to surgery. Pain at primary laparotomy site, **10-point VAS**, day7/day30, asked by research team and recorded on CRF. If discharged before day7, QoL completed on actual day7 via diary. Inpatients asked for corresponding day-specific questionnaires. No SF-12 domain scoring formula or EQ-5D tariff printed in clinical analysis section; economic tariff described separately. Matching keys: continuous outcome definitions, baseline adjustment, time-specific and repeated measures results.

### P018 — Acceptability definition and timing

Locations: [PDF p. 25](../../../joi240145supp4_prod_1741627844.90412.pdf#page=25), [p. 27](../../../joi240145supp4_prod_1741627844.90412.pdf#page=27), [p. 29](../../../joi240145supp4_prod_1741627844.90412.pdf#page=29). All participants including control assess own dressing via **10-point VAS** at day7/discharge (earlier). Schedule footnote identifies asked/research-team-recorded score. UK professionals use online questionnaire; surgeons, ward nurses, research nurses. Matching keys: patient dressing acceptability, timepoint, population and profession survey.

### P019 — Diary and extended follow-up

Locations: [PDF p. 26](../../../joi240145supp4_prod_1741627844.90412.pdf#page=26), [p. 27](../../../joi240145supp4_prod_1741627844.90412.pdf#page=27), [p. 29](../../../joi240145supp4_prod_1741627844.90412.pdf#page=29), [p. 34](../../../joi240145supp4_prod_1741627844.90412.pdf#page=34). Daily diary after discharge to day30 review: healthcare contact/resource use, infection diagnosis, dressing changes, antibiotics, QoL. No daily diary/resource-use collection during hospitalization; questionnaires still collected in hospital. Ongoing SSI at day30 gets continuing diary until wound heals/discharge from district nursing or treating clinician care, or trial follow-up period. Weekly reminders. Matching key: primary SSI ascertainment, healthcare resource-use window and prolonged wound follow-up.

### P020 — Additional endpoint completion conditions

Location: [PDF p. 27](../../../joi240145supp4_prod_1741627844.90412.pdf#page=27). No evident infection at day30 means clinical study completed. Ongoing SSI continues diary for health economics, not redefinition of primary time horizon. Day30 pain and QoL collected if not yet completed in diary. Matching key: outcome follow-up completeness and post-30-day economic data.

### P021 — Assessment table cross-location matching

Location: [PDF p. 29](../../../joi240145supp4_prod_1741627844.90412.pdf#page=29), Table 1. Rows: identification/screening and standard/delayed UK consent; pre/in-theatre randomisation; in-theatre form; wound review day7/discharge; EQ-5D-5L baseline/7/14/21/30; SF-12 baseline/7/30; diary post-discharge to day30, continued for ongoing SSI; Bluebelle independent plus blinded assessor at day30; blinded wound assessment in person/video; SAE collection from theatre through day30 with related-only thereafter; return-to-theatre form for any return; PI declaration at completion. Footnote1=pain at both wound reviews; footnote2=acceptability at early review. Windows are P009. Matching keys: all planned assessment/outcome timepoints and safety reporting period.

### P022 — Withdrawal, recoverable data and sensitivity

Location: [PDF p. 30](../../../joi240145supp4_prod_1741627844.90412.pdf#page=30). Three withdrawal types: treatment only but scheduled follow-up/data allowed; treatment plus trial visits stopped but standard-clinic/central-data follow-up allowed; treatment/all follow-up/no further data, prior data usable only. Date/reason/type recorded. Primary SSI data for withdrawn participants derived where possible from routine outpatient/hospital records. Impact explored in sensitivity analysis. Matching keys: population, withdrawal denominator, missing primary outcome and sensitivity.

### P023 — Safety outcome event sets and recording channels

Locations: [PDF p. 25](../../../joi240145supp4_prod_1741627844.90412.pdf#page=25), [p. 31](../../../joi240145supp4_prod_1741627844.90412.pdf#page=31), [p. 32](../../../joi240145supp4_prod_1741627844.90412.pdf#page=32), [p. 47](../../../joi240145supp4_prod_1741627844.90412.pdf#page=47). Secondary SAEs up to day30. Selected intervention-related AEs: skin reaction and dressing-related pain/discomfort, early/day30 CRFs. SSI/wound complication already routine CRF rather than separately reported. Always SAE-form-report entero-cutaneous fistula, fascial dehiscence, death. Pre-existing-condition/disease-progression/preplanned-hospitalization SAEs excluded from Trial Office reports, retained in notes. Expected serious complications not expedited but captured routine day7/day30 CRFs: wound-infection drainage interventions; wound-related prolonged stay/readmission; anastomotic leak; intraperitoneal collection ±intervention; thromboembolism; non-wound infection (pneumonia/UTI); cardiac/CNS complication; paralytic ileus. SAE definition: death, life-threatening, admission/prolonged admission, persistent/significant disability/incapacity, congenital anomaly, or investigator-medically-significant occurrence. Routine collection and expedited reporting are distinct. Matching key: SAE denominator/event composition and report safety tables.

### P024 — Safety timing and relatedness

Locations: [PDF p. 32](../../../joi240145supp4_prod_1741627844.90412.pdf#page=32), [p. 33](../../../joi240145supp4_prod_1741627844.90412.pdf#page=33), [p. 47](../../../joi240145supp4_prod_1741627844.90412.pdf#page=47). Monitored events from randomisation to **30 days post-surgery**; at-least-possibly-related SUNPD SAEs still expedited regardless of time after device use unless specified exclusion. Five-category causality: definitely/probably/possibly/unlikely/unrelated. CI/PI independent causality; PI assessment not downgraded, both opinions recorded when differing. Unexpected=not listed as expected in protocol; DMC reviews all SAEs. Reporting within24h, office confirmation1 working day, unexpected-related REC reporting15days are administrative deadlines, not endpoint windows. Matching key: related SAE definition/time window.

### P025 — Source-data definitions, units and missing-data queries

Locations: [PDF p. 34](../../../joi240145supp4_prod_1741627844.90412.pdf#page=34), [p. 35](../../../joi240145supp4_prod_1741627844.90412.pdf#page=35), [p. 47](../../../joi240145supp4_prod_1741627844.90412.pdf#page=47). Source data=medical notes, completed QoL questionnaires, diaries; CRFs transcribed into REDCap. Weight **kg**, height **cm**, date day/month/year. Missing/incomplete/unknown data explicitly marked; missing/ambiguous data queried via clarification forms. Diaries checked and missing points clarified at review. No raw dataset, statistical software output or worksheet supplied. Matching key: units and missing-data acquisition context; this does not state an imputation method.

### P026 — Analysis-ready completion

Location: [PDF p. 37](../../../joi240145supp4_prod_1741627844.90412.pdf#page=37). End of trial **12 months after final participant's day30 wound review**, permitting protocol completion/data entry/cleaning/database lock. Final statistical analysis separately specified after all day30 data validated (P033). Administrative timing is distinguished from outcome horizon. Matching key: final-analysis timing if reported.

### P027 — Sample-size and power specification

Location: [PDF p. 38](../../../joi240145supp4_prod_1741627844.90412.pdf#page=38), section14.1; summary n840 on p8. Control SSI **25%** from ROSSINI; target intervention **15%**; relative reduction **40%**, absolute difference **10 percentage points**. Standard difference between proportions/two-sample proportions test, **two-sided**, power **90%**, typeI rate **5% (α=.05)**. Required **336 per arm, 672 total**; assumed **20% attrition**, comprising approximately **10%30-day death +10% further dropout**; recruitment **420 per arm, 840 total**. **Stata15**. Relationships available for downstream calculation: .15=.25×(1−.40); .25−.15=.10;672=2×336;840=672/(1−.20);420=336/.80. No calculation is offered as candidate diagnosis. Matching key: stated sample size, power inputs, expected effect, death/dropout assumptions.

### P028 — General inferential conventions and analysis population

Location: [PDF p. 38](../../../joi240145supp4_prod_1741627844.90412.pdf#page=38), section14.2. Separate SAP to contain comprehensive analysis detail. SUNPD versus surgeon's-preferred dressing. All analyses **intention-to-treat**, assigned group regardless of compliance. Major outcomes: summaries, group differences (examples mean differences/RRs), **95% CIs**, **two-sided P values**. Adjust minimisation variables where possible and baseline scores where appropriate; recruiting centre random effect, other covariates fixed effects. **P<.05**, **no multiple-testing adjustment**. Initial missing-primary exclusion and sensitivities specified on p39 (P032). Matching keys: all effect/reference conventions, confidence/significance, model adjustment, ITT/complete-case definition, multiplicity.

### P029 — Primary effect measure and model

Location: [PDF p. 38](../../../joi240145supp4_prod_1741627844.90412.pdf#page=38), section14.2.1. Number/percentage with SSI within30days by randomized group. **Adjusted relative risk +95%CI**, **mixed-effects log-binomial regression**; **risk difference +95%CI** also. Treatment parameter model P determines significance. Centre random, minimisation covariates fixed as P028. Primary binary infection vs no infection. No odds ratio or hazard ratio is specified here. Matching keys: primary adjusted RR, RD, model and confidence/test.

### P030 — Binary secondary analysis

Location: [PDF p. 38](../../../joi240145supp4_prod_1741627844.90412.pdf#page=38), section14.2.2. Listed categorical outcomes: wound complications, wound-related hospital readmission, SAEs. For binary secondary outcomes: n/% by group, adjusted **RR+95%CI** from **mixed-effects log-binomial** model. Ordinal Clavien-Dindo definition also exists but no ordinal model is specified in this paragraph. Matching keys: complication/readmission/safety effects, populations, adjustment and model.

### P031 — Continuous/repeated secondary analysis

Locations: [PDF p. 38](../../../joi240145supp4_prod_1741627844.90412.pdf#page=38), [p. 39](../../../joi240145supp4_prod_1741627844.90412.pdf#page=39), section14.2.2. Hospital stay: mean/SD, **mixed-effects linear model adjusted mean difference+95%CI**; if skewed, median/IQR and **unadjusted difference in medians**. SF-12, EQ-5D-5L, laparotomy pain VAS continuous: mean/SD, day7/day30 **mixed-effects linear model adjusted mean difference+95%CI**. EQ-5D data baseline/7/14/21/30: additionally **mixed-effects repeated-measures model** as secondary analysis. Generic baseline/minimisation adjustment P028. No explicit clinical acceptability regression model, correlation structure, or SF-12 component formula is stated here. Matching keys: reported continuous contrasts/timepoints, adjusted mean vs unadjusted median, QoL repeated analysis.

### P032 — Subgroups, missing-primary data and sensitivity

Location: [PDF p. 39](../../../joi240145supp4_prod_1741627844.90412.pdf#page=39), sections14.2.3–14.2.4; withdrawal sensitivity p30 (P022). Subgroups **primary outcome only**: minimisation variables except centre (**contamination, stoma**), **operative procedure**, **country**. Treatment×subgroup interaction in regression; hypothesis-generation, caution. Missing primary outcome excluded initially; follow-up pursued, sensitivity analyzes possible bias and never supplants planned primary analysis regardless of differences; full details deferred to SAP. No explicit extreme-case assignment or clinical multiple-imputation formula supplied in this protocol section. Matching keys: prespecified primary subgroups/interaction tests, complete cases, missing-data sensitivities and withdrawal analysis.

### P033 — Interim/final and economic specifications

Locations: [PDF p. 39](../../../joi240145supp4_prod_1741627844.90412.pdf#page=39), [p. 40](../../../joi240145supp4_prod_1741627844.90412.pdf#page=40), [p. 41](../../../joi240145supp4_prod_1741627844.90412.pdf#page=41). Sections14.3/14.4: interim major endpoints/safety confidential to DMC, charter/SAP detail; final once all day30 assessments complete and corresponding entered data validated. DMC ordinarily annual, additional/emergency meetings possible, one DMC overseeing both countries. Stopping considers proof beyond reasonable doubt and impact on clinical management, not P alone. Difference **at least P<.001**, Haybittle-Peto-like, may justify halting/modifying; no fixed interim count/schedule; proposed boundary permits final **P=.05** without multiple-testing adjustment. Text says SAP statistical methods followed for agreed interim endpoints.

Health economics section15 (pp39–40): **UK**, NHS/personal social services perspective; resource diary through healing for ongoing SSI; national tariffs. EQ-5D-5L **crosswalk value sets** base case, **England value set** sensitivity. **QALYs area under curve**, regression baseline EQ-5D/minimisation adjustment. Cost-utility analysis, **incremental cost-utility ratios (ICURs)**; ITT. Missing data sensitivity including **multiple imputation**; deterministic/probabilistic sensitivities across assumptions/methods; **CEACs**, probability cost-effective over willingness-to-pay per additional QALY. No numeric willingness-to-pay threshold/cost/QALY result printed. Matching keys: interim/final significance/stopping and separately planned health-economic outcomes.

### P034 — Historical quantitative context distinguished from trial specifications

Location: [PDF p. 12](../../../joi240145supp4_prod_1741627844.90412.pdf#page=12). Supplied protocol background: ≥200000 UK SSI/year; £3500 average infection cost; ~£700million/year; SSI patients twice death likelihood; ~one-third postoperative deaths partly attributable; other incision studies 50–80% reduction; >30000 England emergency laparotomies/year; ~12000 Australia; historical emergency SSI25–40%. These are historical literature statements, not observed SUNRRISE results or direct power-input assumptions (25% control is explicitly P027). No external citations were opened. Matching key: background only; no registered statistical result implied.

## Completeness and limitations

All 48 pages were inspected and mapped. All substantive prospective outcome definitions, scales, windows, interventions, analysis populations, sample-size inputs, primary/secondary models, subgroups, missing-data/sensitivity, interim/multiplicity/stopping, economics, and amended elements were retained. Full assessment table and Clavien-Dindo table are mapped. Reference and administration pages contain no new applicable trial quantitative relationship, as recorded individually.

There is no supplied raw dataset, workbook/cached value, CSV, DOC or DOCX within this assigned scope. No actual endpoint counts, estimates, CIs, or P values for the final trial appear in this prospective protocol. Realized feasibility counts are not printed. Several detailed statistical definitions are prospectively deferred to SAP; this is recorded without diagnosing a candidate. Reused layout provenance lacks retained engine/version; all pages have usable native geometric text, so no scientific-coverage gap follows. Mechanical source verification is still required for any registered issue. No new OCR or GPU processing was required.
