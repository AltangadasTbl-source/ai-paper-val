# Support quantitative evidence map: protocol shard

## Scope and evidence authority

Assigned source: DOC-002, [joi190039supp1_prod.pdf](../../../../joi190039supp1_prod.pdf#page=1), exclusively physical PDF pages 1–62. Role: PLAN throughout, including appendices and signed/unsigned signature pages. This is clinical study protocol K357/ASTER, EudraCT 2011-005603-32, version 1.5 dated 24 July 2015. No separate earlier protocol version, amendment history, or amendment document occurs in this source. References to future amendments are governance provisions, not supplied amendments.

Read completely: QUALITY_CONTROL_SCOPE.md, workflow_1_6_1/review_contract.md, workflow_1_6_1/settings.toml, current source_inventory.md, evidence_asset_inventory.md, source_coverage.md, coverage_manifest.md, and tooling_record.md. No historical conclusions, candidates, checker outputs, or adjudication records were used. This map extracts supplied evidence without diagnosing findings.

Canonical reusable locator: `.ai_paper_validation/review_1_5_1/preprocessing/support/DOC-002_pp1-62_layout.txt`, Poppler pdftotext -layout, form-feed segment N = physical PDF page N. Every segment was read. Physical pages 1–48 carry matching printed page numbers; physical p.49 is a scanned signed printed p.49, physical p.50 is an unsigned printed p.49, and physical pp.51–62 carry printed pp.50–61. Links always use physical PDF pages.

Coverage: 62/62 pages mapped; 59 reusable-backed pages; 3 fresh-required pages (16, 20, 49) directly rendered and visually inspected. The reusable p.49 segment is empty despite nonempty scanned source content; p.20 has unusable encoded diagram labels; p.16 lacks graph axes and has an encoded cutpoint unit. These derivative limitations were closed by direct-source viewing. No scientific coverage gaps remain.

Direct visual derivative engine: Poppler pdftoppm, CPU, as available in tooling_record.md. Commands used `pdftoppm -f N -l N -singlefile -scale-to 1600 -png joi190039supp1_prod.pdf /tmp/protocol-pN` for N = 16, 20, 49. Resulting full-page images were moved unchanged to `extraction/parts/DOC-002-p16.png`, `extraction/parts/DOC-002-p20.png`, and `extraction/parts/DOC-002-p49.png` within review_1_6_1. Visual inspection used view_image. No OCR was needed. Native text for other pages remains readable for applicable content; encoded isolated clinical wording and administrative font runs are not new quantitative evidence. Direct PDF remains authority for subsequent evidence recheck.

No Office files, worksheets, CSV records, workbook formulas, or cached workbook values occur in this assigned source. All numerical values are printed PDF text or figure labels. No raw trial results are present; prior-study results are explicitly distinguished below.

## Complete page coverage

Each row records the whole physical page, including administrative and appendix content. PR keys are local evidence-map keys for later matching; they are not finding or candidate IDs and do not replace coordinator N/S relationship IDs.

| Physical PDF page | Printed page / section | Mapped applicable evidence or explicit no-applicable record | Matching key |
|---:|---|---|---|
| 1 | 1, title | Protocol identity/version/date, sponsor and study code; no result-relevant quantitative relationship on title/contact page. | Identity |
| 2 | 2, contact continuation | No applicable quantitative/statistical design content; coordinating-center contact details only. | None |
| 3 | 3, protocol development | No applicable quantitative/statistical design content; developer/contact roster only. | None |
| 4 | 4, centers/laboratories | No applicable numeric result or decision rule; laboratory/storage responsibilities identify blinded-test infrastructure. | PR-08 |
| 5 | 5, statistician/management | No applicable numeric result; statistician, data management, monitoring and pharmacovigilance responsibilities; participating sites in separate document. | None |
| 6 | 6, contents | Contents locating synopsis, design, stopping/drop-outs and statistical approach; no independent applicable relationship. | None |
| 7 | 7, contents | Contents locating safety, amendments, data handling, medication and appendices; no independent applicable relationship. | None |
| 8 | 8, abbreviations | Diagnostic/statistical labels: ASA, CRC, iFOBT, ITT, CRF, DMC; no independent numerical result or rule. | PR-01, PR-09 |
| 9 | 9, abbreviations | ROC, SAE, SDV, LLN/ULN and administrative abbreviations; no independent numerical result or rule. | PR-01, PR-15 |
| 10 | 10, summary | Two iFOBTs; single 300 mg ASA vs placebo; 2,400 participants age 40–80; drug at least 5 days before colonoscopy with at least 4 full intervening days; baseline and three postdose sampling days; colonoscopy gold standard; sex and multiday analyses; optional biomarkers. Prior-study sensitivity/AUC values distinguished from current trial. | PR-01–04, PR-18 |
| 11 | 11, synopsis 3.2–3.4 | Main diagnostic-performance objective for 2 tests; secondary sex/multiday/safety/optional biomarkers; single oral uncoated 300 mg tablet vs single placebo; participant duration 5 days; primary sensitivity at predefined FOBGold cutpoints; secondary PPV, NPV, specificity, AUC, likelihood ratios, sex, multiday and SAEs. | PR-01–04, PR-15 |
| 12 | 12, synopsis 3.5–3.8 | Multicenter randomized double-blind placebo-controlled confirmatory trial; men/women 40–80 undergoing screening or diagnostic colonoscopy; eligibility/exclusion exposures and timing. | PR-05–06 |
| 13 | 13, eligibility / 3.9 | Safety and other eligibility exclusions; GFR <30 mL/min, myocardial infarction within 6 months, methotrexate threshold; diagnostic analyses in total population with primary endpoint and colonoscopy available, statement continues p.14. | PR-06, PR-09 |
| 14 | 14, 3.9–3.11 | Day-3 FOBGold endpoint/ROC availability; sex strata; baseline if available and 3 days at least 2 days after dosing; combined 2-/3-day tests; safety all randomized ITT; randomized N=2,400 and primary analyzed N=2,000. Administrative duration 60 months total / 48 months clinical, dates recorded below. | PR-04, PR-09–11, PR-20 |
| 15 | 15, background | Background only: prior-study n=1,979 and sensitivity/specificity/AUC and P values; contextual screening percentages. No ASTER participant result. | PR-18 |
| 16 | 16, Figure 1 / benefit-risk | Fresh visual map of prior-study ROC: sensitivity vs 100−specificity, both percent; top specificity axis; male users bold/filled circles vs nonusers thin/open circles; cutpoints 8,4,2,1 μg/g stool. Dose rationale and historical sensitivity 51.2%→66.7%. | PR-18–19 |
| 17 | 17, rationale | Prior users approximately 10%; rationale for sex and multiday analyses; no ASTER result, count or new decision rule. | PR-18 |
| 18 | 18, study design | N=2,400, age 40–80; 4 kits for each of 2 tests (8 total); optional 2 EDTA+2 serum tubes; baseline day 0/1 before dose, skip baseline if unavailable; dose day 1; three postdose days preferably 3,4,5; postponement allowed; two-sample participation baseline/day3 allowed; each time point uses one kit of each test. | PR-02–06 |
| 19 | 19, study design | At least 4 ASA-free days before colonoscopy; maximum 3 months from study start; sensitivity analysis for longer delays; no colonoscopy = drop-out; blinded standardized colonoscopy/pathology extraction and laboratory analyses. | PR-07–08, PR-12 |
| 20 | 20, Figure 2 | Fresh full-page visual map: day0 first appointment; day1 both stool tests then single dose; days3,4,5 both stool tests; trial end day5; colonoscopy from day6 onward outside clinical study. | PR-04 |
| 21 | 21, Table 1 | Full schedule and all 6 footnotes transcribed in PR-04/PR-15/PR-21 below; stool collection exceptions and safety ascertainment timing retained. | PR-04, PR-15, PR-21 |
| 22 | 22, 6.1–6.2 | Primary/secondary endpoint hierarchy repeated; age 40–80 and endpoint-relevant exclusions repeated. | PR-01, PR-06 |
| 23 | 23, exclusions continuation | Safety and other exclusions repeated, including GFR <30 mL/min, MI within 6 months, interacting therapy; defines eligible randomized population. | PR-06 |
| 24 | 24, 6.3–6.6 | Placebo diagnostic comparator; single oral 300 mg ASA/placebo; unique medication numbers 1–4,000; sequential within-block assignment; concealed allocation envelopes; blinded laboratories/colonoscopy extraction and double data reviewers. | PR-02, PR-05, PR-08 |
| 25 | 25, bias / 6.7–6.8 | Preanalysis handling recorded; medication diary/accountability; FOBGold and FD Hb/Hp Complex lab plans; optional future biomarkers without fixed marker list, not required for main participation. | PR-08, PR-22 |
| 26 | 26, 6.9–6.10 | Recruitment target 2,400/48 months; individual stopping/withdrawal provisions and late-dose condition continuing p.27; reasons recorded for withdrawal within 3 weeks. €75 recruitment incentive and prior 4,150 recruits are administrative/background, not current result denominators. | PR-12–13, PR-20 |
| 27 | 27, 6.10–6.11 | Dose-to-colonoscopy ≤4 days leads withdrawal or postponement; >3 months protocol violation with end-trial sensitivity analyses; stop for ≤25% recruitment after half planned time if added centers unpromising, or unexpectedly high serious reactions; all drop-outs recorded and cannot be reincluded; participant numbers never reused. | PR-12–14 |
| 28 | 28, 7.1–7.2 | Entire statistical approach, endpoint comparison, ITT, 95% CIs, specificity >90%, ROC/AUC, sex/neoplasm/multiday analyses, safety set, confirmatory/exploratory split and sample size assumptions mapped below. | PR-01, PR-09–11, PR-16–17 |
| 29 | 29, 7.2 continuation | Specificity assumed 90%, anticipated CI 88%–92% in both groups. | PR-17 |
| 30 | 30, risks / pharmacology | Single 300 mg dose repeated; historical risk/pharmacology figures, not trial result or power assumptions. | PR-02, PR-19 |
| 31 | 31, pharmacology | At least 4 full drug-free days; shorter interval withdrawal or postponement. Background platelet/colonoscopy safety quantities separately identified. | PR-07, PR-12, PR-19 |
| 32 | 32, dose / safety | Non-enteric-coated single 300 mg rationale; AE observation days1–5; before-colonoscopy interview; if colonoscopy >3 weeks, phone within 3 weeks; SAE follow-up through recovery/stabilization; reporting deadlines. | PR-02, PR-15, PR-19 |
| 33 | 33, safety / unblinding | SUSAR reporting 15 days or 7 if fatal/life-threatening; yearly DSUR; no colonoscopy telephone contact within 3 weeks, possible rescheduling within 3 months; participant-specific emergency unblinding. | PR-07, PR-12, PR-15 |
| 34 | 34, results / legal | Positive stool result disclosure if no colonoscopy within 3 months; later colonoscopy permits reinclusion; optional biomarkers do not determine main participation. No observed trial result. | PR-12, PR-22 |
| 35 | 35, legal / consent | Approval prerequisites, planned termination notification ≤90 days, premature ≤15 days, report ≤1 year; updated consent/amendment communication. No independent applicable numeric endpoint/model rule. | PR-23 |
| 36 | 36, confidentiality / archiving | Participant code and ≥10-year retention; insurance and confidentiality. No applicable numeric result/statistical design rule. | None |
| 37 | 37, amendments / collection | Written signed amendment with applicable ethics/authority approval; no change list. eCRF includes medication last2 weeks, eligibility, participation/colonoscopy dates, optional blood, AE, drop-out date/reason within3 weeks. | PR-23–24 |
| 38 | 38, data/source/accountability | Diary records actual dose/sample timing; screening failures lack randomized participant number; source colonoscopy/histology verification; 10-year retention. | PR-08, PR-24 |
| 39 | 39, funding | Appendix4 financial statement pointer only; no applicable endpoint, statistical result, or decision rule. | None |
| 40 | 40, data handling / monitoring | Blinded double-entry of diary/colonoscopy/histology; request missing reports/data; site monitoring estimated4/year (2 KKS+2 center), early visit after approximately20 recruits, not interim statistical analyses. | PR-08, PR-24 |
| 41 | 41, monitoring / committee | Missing-data queries and adaptive monitoring intensity; steering/publication policy; no additional model, numerical stopping boundary, or statistical interim plan. | PR-24 |
| 42 | 42, study medication | Oral 300 mg tablet, day1 with glass water; placebo ingredients; ≤25°C storage; historical pharmacology quantities separately recorded. | PR-02, PR-19 |
| 43 | 43, medication preparation | RITA version1.24 randomization software; one tablet per blister unit, blinded packing. Background pharmacokinetics only otherwise. | PR-05, PR-19 |
| 44 | 44, labeling / accountability | Medication labeling, storage below25°C and dispensed/used/returned quantities logged; no applicable result count, analysis rule or new endpoint. | PR-24 |
| 45 | 45, references1–16 | No applicable independent quantitative/statistical relationship; bibliographic identifiers and study titles only. Prior-study bibliography is not imported as trial evidence. | None |
| 46 | 46, references17–34 | No applicable independent quantitative relationship; methods references18–19 identify general diagnostic-test texts without supplying a specific formula/test algorithm. | PR-16 |
| 47 | 47, references35–51 | No applicable independent quantitative/statistical relationship; cited historical studies only. | None |
| 48 | 48, reference52 | No applicable independent quantitative/statistical relationship; final bibliography entry. | None |
| 49 | 49, signed signatures | Fresh source visual inspection: signed approval page for version1.5. Four named signatories and handwritten dates; no applicable quantitative/statistical relationship. Not a blank source page. | PR-23 |
| 50 | 49, unsigned signatures | Unsigned form repeating protocol approval statement/signatories; no applicable quantitative/statistical relationship. | PR-23 |
| 51 | 50, Appendix1 | AE/SAE/unexpected-event definitions, safety outcome classification; all explicit SAE criteria mapped. | PR-15 |
| 52 | 51, Appendix1 | SUSAR definition; intensity categories mild/moderate/severe and causality certain/probable/possible/unlikely/not assessable/not related, not numerical severity grades for review candidates. | PR-15 |
| 53 | 52, Appendix1 | SAE ≤24h/next working day; second assessment ≤3 working days/72h; fatal/life-threatening SUSAR ≤7 calendar days +8-day follow-up; others ≤15 days. | PR-15 |
| 54 | 53, Appendix1 | Minimum SUSAR report criteria; six AE outcome categories and action categories; fatal designation restricted to event leading to death. | PR-15 |
| 55 | 54, Appendix1 references | No applicable independent quantitative/statistical relationship; regulatory bibliography only. | None |
| 56 | 55, Appendix2 | Optional blood day0, four9–10mL tubes (2 EDTA/2 serum); serum8.5–9mL, EDTA9–10mL; storage/processing conditions mapped as peripheral biomarker operations, no trial result. | PR-22 |
| 57 | 56, Appendix2 continuation | Laboratory contacts and access restriction; no applicable independent numeric result or analysis rule. | PR-22 |
| 58 | 57, Appendix3 | Investigator agreement to protocol/future amendments, prior approval except immediate hazard; no supplied amendment, numerical result or new decision rule. | PR-23 |
| 59 | 58, Appendix4 | Financial statement project/monitoring costs only; no applicable primary/key secondary result or statistical design relationship. | PR-25 |
| 60 | 59, Appendix4 | Financial statement safety/data/lab/medication/training costs only; no applicable reported trial relationship. | PR-25 |
| 61 | 60, Appendix4 | Budget €505,570 and cost footnotes; financial assumptions mention2,000 completed cases,2,400 material recipients,4 assays/person, assumed SAE/SUSAR workloads; not a sample-size calculation or decision rule. | PR-25 |
| 62 | 61, Appendix4 | Financial footnotes concerning fees/insurance/printing/shipping/meetings; assumed3 amendments are costing, not supplied amendments or a statistical amendment history. | PR-25 |

## Protocol relationship map for report/plan matching

### PR-01: diagnostic outcomes and hierarchy

Locations: physical pp.10–11,13–14,22,24,28–29. Main-paper matching key: FOBGold sensitivity for advanced colorectal neoplasms, day3, ASA versus placebo; secondary diagnostic performance.

Main objective: evaluate sensitivity, specificity, positive and negative predictive values, likelihood ratios, and AUC of two immunochemical FOBTs after one ASA dose versus placebo. Synopsis3.4 and section6.1 primary endpoint: sensitivity at predefined cutpoints of test positivity of FOBGold Tube Screen to detect advanced neoplasms. Listed secondary endpoints: positive/negative predictive values; specificity and AUC in ROC analyses; likelihood ratios; gender-specific performance; gain from multiple-day application; SAEs. Section7.1 calls primary endpoints confirmatory and other analyses exploratory. Section7.2 separately describes primary endpoint as sensitivity and specificity at predefined test-specific cutpoints and ROC AUC of two immunochemical FOBTs taken on day3. Preserve these distinct statements for downstream matching without collapsing their hierarchy.

Advanced neoplasms are discussed as advanced adenomas and carcinomas. This protocol does not supply a size/villous-component/high-grade-dysplasia threshold definition for advanced adenoma. It does not print numeric positivity cutpoints for the ASTER primary test. Cutpoints1,2,4,8 μg/g in Figure1 concern a prior RIDASCREEN study, not the planned FOBGold primary cutpoints.

### PR-02: randomized intervention

Locations: pp.10–11,18,24,30–32,42–44. Key: single-dose aspirin300mg versus placebo. Experimental: one oral tablet containing300mg acetylsalicylic acid, without enteric coating; control: one placebo tablet. Study medication taken day1 (p.42 specifies glass of water). Participant study duration5 days; day1 is medication day. Placebo ingredients p.42: cellulose, lactose monohydrate, magnesium stearate. p.43 packaging one tablet/blister unit, blinded. Medication storage not above25°C/protected from humidity (p.42), below25°C/protected from humidity (p.44). Storage is operational context, not an endpoint definition.

### PR-03: tests and specimen numbers

Locations: pp.10–11,18,21,25,28. Key: FOBGold quantitative test and FD Hb/Hp Complex qualitative test. Two commercially available validated iFOBTs: FOBGold Tube Screen and FD Hb/Hp Complex quick test. Four kits per test → eight kits/participant. Each stool collection uses one kit of each test. Laboratory FOBGold planned at Limbach; FD Hb/Hp Complex at DKFZ Division of Clinical Epidemiology and Aging Research; laboratory analyses blinded. No ASTER numeric assay threshold or conversion formula is printed here.

### PR-04: timing, Table1, Figure2 and sampling exceptions

Locations: pp.10–11,14,18–21,28. Key: baseline, day3 primary, day4/day5 secondary, combined tests. Baseline sample day0 or day1 before dose; if unable on first day, skip baseline and take study drug day1. Subsequent samples day3 onward on three different preferably consecutive days3,4,5; postpone when unable because of constipation or other reasons. Participation with only two samples (before medication and day3) allowed. Actual collection date documented. All sampling at home before colonoscopy bowel preparation. p.14 describes postdose tests on3 days at least2 days after dose. p.28 primary day3; it also states participants whose first sample is day4 because of constipation excluded from study (recorded separately in PR-12).

Figure2 direct visual labels: day0 first visit including information/consent/eligibility, kit/diary, questionnaire, optional blood, randomization and study medication; day1 both tests followed by dose; days3,4,5 both tests; day5 trial end; day6 onward screening/diagnostic colonoscopy outside clinical study.

Table1 matrix: columns screening0, treatmentday1, observationday3/day4/day5, post-study colonoscopyday6 onward. Screening0: consent, eligibility, randomization, examination, patient parameters, optional blood, questionnaire, kits/diary. Day1: drug administration and both stool tests. Days3,4,5: both stool tests. Concomitant therapy and (S)AE recording: day1,3,4,5 and colonoscopy. Footnotes: (1) age, gender, weight, height, blood pressure; (2) family history of CRC, smoking/alcohol lifestyle; (3) eight kits; (4) postponement allowed if collection impossible, two samples allowed ondays1 and3; (5) two EDTA and two serum tubes; (6) interview before colonoscopy, or phone within3 weeks if colonoscopy later than3 weeks after medication start.

### PR-05: design and assignment unit

Locations: pp.12,18,24,43. Key: multicenter participant randomization, concealed blinded ASA/placebo allocation. Randomized double-blind placebo-controlled multicenter trial, formally phaseIII for potential new indication with confirmatory approach. Individual medication packs randomly assigned unique numbers1–4,000; list links number to treatment, held sealed at DKFZ. Centers receive blocks; physician takes next ascending participant number within block. Number used across eCRF, identification list, kits, blood, diary, questionnaire, consent. Participant-specific envelopes at center/KKS/DKFZ for emergencies; other participants remain blinded. Randomization software RITA1.24 and packing by pharmacy p.43. This protocol does not state numeric block size, stratification factors, allocation ratio, random-sequence algorithm, adjusted covariates, or cluster randomization. Those are bounded absent definitions, not inferred designs.

### PR-06: target eligible population

Locations: pp.10,12–13,18,22–23. Key: age40–80 screening/diagnostic colonoscopy population and endpoint-affecting exclusion set. Both sexes,40–80 years, screening or diagnostic colonoscopy planned, sufficient German to consent/comply. Premenopausal negative pregnancy test; postmenopause defined ≥12 months without menstrual bleeding or surgical sterilization. Endpoint exclusions: chronic inflammatory bowel disease; colonoscopy due to positive FOBT; history CRC; colonic angiodysplasia; anamnestic/observed rectal blood loss. Drug exclusions: anticoagulants/antiplatelets within2 weeks; ASA within1 week; NSAIDs/COX2 inhibitors within3 days. Safety exclusions include gastrointestinal ulcer signs, relevant thrombocytopenia, infection/dehydration/allergy, severe/uncontrolled asthma, severe renal/hepatic disease (example GFR<30mL/min, cirrhosis), severe untreated heart failure/hypertension or other unexplained symptoms; severe prior GI bleed, hemorrhagic diathesis, asthma unless prior tolerated ASA, salicylate/drug hypersensitivity or prior NSAID/COX2/antirheumatic intolerance, severe gout, hereditary oxaluria, G6PD/glutathione peroxidase deficiency, epilepsy with generalized seizures, severe cardiac disease including MI within6 months. Planned interacting drugs during study: anticoagulants, antiplatelets, NSAIDs/COX2 inhibitors, methotrexate≥15mg/week, systemic glucocorticoids, SSRIs, valproate; planned surgery/dental work excluded. Other exclusions: alcohol/illicit drug abuse, pregnancy, suspected noncompliance, another clinical study. No outcome results arise from these criteria.

### PR-07: reference standard and colonoscopy window

Locations: pp.10,18–21,27,31,33–34. Key: colonoscopy/histology gold standard and delayed-colonoscopy sensitivity analysis. Colonoscopy scheduled independently of trial; diagnostic accuracy compared against colonoscopy. At least4 full ASA-free days between drug day and colonoscopy; figure/table use day6 onward for day1 dose. Maximum interval from study start to colonoscopy3 months. If postponed >3 months, p.19 end-trial sensitivity analyses and p.27 protocol violation with sensitivity analyses. No colonoscopy considered drop-out p.19. p.33 new appointment within3 months after randomization may retain participation. p.34 later colonoscopy after3 months can permit reinclusion (preserve alongside general drop-out prohibition PR-12).

### PR-08: blinded data and assay procedures

Locations: pp.19,24–25,38,40. Key: measurement/data extraction and analysis population source. Colonoscopy/histology records pseudonymized and linked by participant number; trained blinded standardized extraction. Laboratory analyses blinded to treatment and clinical/colonoscopy data. Two independent blinded reviewers for extraction/entry; disagreements resolved via SOP; checks against original records. Diaries record dose and stool sample timing. Preanalysis storage/duration/transport documented. No particular adjusted analysis model is specified by these operational safeguards.

### PR-09: diagnostic and safety analysis populations

Locations: pp.13–14,28. Key: ITT diagnostic available-case and all-randomized safety populations. Synopsis diagnostic analyses in total population with primary endpoint data (day3 FOBGold sensitivity/specificity predefined cutpoints and ROC AUC) and available colonoscopy. Baseline analyzed if available. Section7.1 compares participants randomized to ASA vs placebo in an intention-to-treat analysis; safety all randomized independently of stool samples or colonoscopy reports. Synopsis likewise safety total randomized ITT. No imputation model, numerical missing-data threshold, per-protocol definition, or explicit handling of absent histology is specified in this protocol.

### PR-10: prespecified stratified/secondary analyses

Locations: pp.10–11,14,28. Key: sex strata, advanced adenoma versus carcinoma, individual days, multiday combinations, both assays. All analyses total population and stratified by gender; separately for colonoscopy findings advanced adenomas and carcinomas. Compare both test performances and enhancement by ASA. Evaluate baseline and different postdose days. Combine tests from2 or3 different days to assess gain. No explicit logical combination rule (such as any-positive/all-positive), interaction test, subgroup model, multiplicity adjustment, or fixed subgroup sample size is printed.

### PR-11: total sample size

Locations: pp.10,14,18,26,28–29. Key: randomized2400, analyzed2000, prevalence/power. Synopsis randomized N=2,400; analyzed primary N=2,000. Recruitment narrative repeats2,400 over48 months. Section7.2 assumes10% advanced-neoplasm prevalence and100 affected participants in each of two groups. The printed analyzed target and prevalence imply200 advanced neoplasms total; 100/group is the printed planned affected sample. No explicit attrition percentage or equation is printed. There are no observed participant counts here.

### PR-12: exclusions, withdrawal and drop-outs affecting analysis

Locations: pp.18–19,26–28,31,33–34. Key: day4-first-sample exclusion, drug/colonoscopy interval, >3months, withdrawal/reinclusion. Baseline may be missing and participants may contribute only two samples p.18. Section7.2 p.28 explicitly excludes patients who because of constipation give first sample onday4. Individual withdrawal permitted anytime; intolerable AE participants followed; investigators may withdraw for SAE/safety, incomplete procedures, protocol violation or event interfering with target criteria. p.26–27 late dosing with medication-to-colonoscopy interval≤4days requires withdrawal or postponement to required4-day drug-free period. p.31 states fewer than4 full intervening days requires withdrawal/postponement. >3months treated as protocol violation with sensitivity analysis. p.19 no colonoscopy drop-out; p.27 all drop-outs recorded, cannot be reincluded, numbers not reused; p.34 patients undergoing colonoscopy after>3months may be reincluded. These statements are recorded as printed without a proposed interpretation.

### PR-13: recruitment stopping rule

Location: p.27. Key: study termination boundary. Stop for inadequate recruitment defined as only25% of participants or less after half planned recruiting time, when additional centers appear unpromising. Recruitment target2400/48months elsewhere; derived locators are ≤600 by24months if that target/duration supplies the rule's denominator/time (derived, not separately printed). No efficacy/futility interim rule is printed.

### PR-14: safety stopping rule

Location: p.27. Key: unexpected serious-adverse-reaction stopping. Study terminated for unexpectedly high rate of serious adverse reactions; no numeric rate/boundary specified. Premature termination authority notification within15days is administrative reporting, not a statistical decision boundary.

### PR-15: safety endpoints, ascertainment and classification

Locations: pp.11,14,21,28,32–33,51–54. Key: AE/SAE counts in randomized participants and observationdays1–5. Secondary endpoint SAEs; safety all randomized independently of diagnostic availability. Observation periodday1–day5. Ask before colonoscopy; telephone within3weeks after dose if colonoscopy later than3weeks, or when colonoscopy not performed; SAE followed until recovery/stabilization. All AEs documented; SAE reported ≤24h or next working day; second assessor assesses causality/expectedness. SUSAR reporting≤15days,≤7 if fatal/life-threatening; Appendix1 adds8calendar-day follow-up after7-day report and second assessment3working days/72h.

AE: untoward medical occurrence after pharmaceutical administration, no causal relationship required; new symptoms/diagnoses/labs/intercurrent illness/accidents, worsening/recurrence/increased frequency/intensity of existing disease. Stable preexisting disease not AE. Surgery itself not AE; condition requiring unplanned surgery may be AE; planned permitted surgery for preexisting condition not AE. SAE criteria: death, life-threatening, requires/prolongs hospitalization, persistent/significant disability/incapacity, congenital anomaly. Unexpected: nature/severity inconsistent with product information, including new specificity/severity/frequency information. SUSAR: suspected treatment-related + serious + unexpected, including placebo evaluation.

Intensity: mild minimal discomfort/no interference, moderate interference with normal activities, severe prevents normal activities. Causality categories certain, probable, possible, unlikely, not assessable (temporary), not related. Outcomes: recovered/resolved, recovering/resolving, not recovered/not resolved, recovered with sequel, fatal, unknown; only event leading to death called fatal when multiple events. Actions: unknown, not applicable, none, drug treatment, others. These source safety classifications describe endpoints; they do not classify quality-control candidates.

### PR-16: inferential specification

Locations: pp.28–29,46 references18–19. Key: CI confidence, comparison method, alpha, confirmatory endpoint. General standard diagnostic-test techniques, sensitivity/specificity/LR/PPV/NPV with corresponding95%CIs at cutpoints yielding specificity>90%; colonoscopy reference. Primary compares day3 FOBGold sensitivity at predefined test-specific positivity cutpoints between ASA and placebo. ROC across full cutpoint range, AUC determined. No named exact test for reported primary comparison, CI formula, variance estimator, regression family/link, adjustment covariates, interaction test, repeated-measure model, missing-value model, or multiplicity procedure is supplied here. Sample-size section separately specifies two-sided statistical tests at alpha0.05 with continuity correction. No equivalence/noninferiority margin or hypothesis is printed. Methods references are supplied bibliography only and do not authorize external method import.

### PR-17: power and specificity precision

Locations: pp.28–29. Key: power36%→60% overall and36%→70% sex-specific. Expected prevalence10%;100 advanced neoplasms/group. Assume placebo sensitivity36%, two-sided alpha0.05 tests with continuity correction. Power90% for ASA sensitivity60% overall; power90% for sensitivity70% in gender-specific analyses. Previous-study sensitivity71% is supportive background, not an observed ASTER value. Expected specificity90% with CI88%–92% for both groups. No written sample-size formula, software name for power, explicit affected sample by sex, continuity correction formula, or specific CI method is printed.

### PR-18: prior-study quantitative evidence, not ASTER results

Locations: pp.10,15–17,28. Key: background only. Prior n=1979 screening-colonoscopy participants; sensitivity70.8% ASA users vs35.9% nonusers, P=.001; specificity85.7% users vs89.2%–91.1% nonusers. Male AUC .87 vs.68, P=.003. Prior users approximately10%; insufficient women for diagnostic-performance assessment. Another observational study sensitivity51.2%→66.7%, difference not significant. Context: global>1.2million cases/>600000 deaths annually; Germany>70000 cases/almost30000 deaths;60%–90% prevention estimate;20%–30% reduction with FOBT screening; advanced-neoplasm sensitivity<50% at90%–95%specificity. These numbers are background and must not be matched as current trial outcome results.

Figure1 p.16 direct visual: RIDASCREEN Hemoglobin prior male ROC; y sensitivity%,0–100, ticks20; bottom x100−specificity%,0–100, ticks20; top specificity%,100→0. Bold line/filled circles=users; thin line/open circles=nonusers; circles mark8,4,2,1μg/g stool cutpoints. Diagonal reference line. No printed coordinate table, CI, participant denominator, or trial cutpoint specification accompanies graph; no approximate digitized coordinates substituted for exact values.

### PR-19: historical safety/pharmacology quantities, operational context

Locations: pp.16,30–32,42–43. Key: not current-trial diagnostic results. ASA marketed>100years/since1899; comparator normal pain dose500mg and prevention75–325mg. Long-term upper-GI excess risk .12%/year; one-week excess mortality185/100million=.000185%overall/.000417%age>60. Salicylic acid half-life2–3h; platelet life10±1days, markers normalize within2weeks. Platelet-addition studies10%–40%,40%functioning→40%TxB2/80%aggregation;4volunteers recovery5–6.8days vs survival10.4days;50%functioning platelets deemed sufficient, mean5days (7 low turnover); aggregation4–6days, bleeding2–4days, colonic bleeding3days. Colonoscopy bleed .16% without polypectomy/.4%–3.4% with; prior1174polypectomy patients. Typical prior ASA100mg/day, maximal suppression~5days, loading500mg and planned300mg uncoated. p.42 platelets replaced10%–15%/day; Tmax.5–2h; volume.16L/kg; protein binding>90%. p.43 unchanged ASA excretion1%, ASA half-life15–20min. These are historical pharmacological rationale, not planned power assumptions or current safety estimates.

### PR-20: administrative schedule and feasibility

Locations: pp.14,26. Key: administrative calendar only. Total60months, clinical48months; preparation Q1/Jan2012, first subject Q2/June2013, last subject and last observation Q2/June2017, DBL Q3/Sept2017, analyses completed Q4/Dec2017, report Q1/March2018. Target2400 over48months; prior feasibility4150 recruits sinceJan2006;€75/participant site incentive. Recruitment target/duration feed PR-13; other calendar/site/cost quantities are peripheral.

### PR-21: participant parameters and auxiliary specimens

Locations: pp.18,21. Key: Table1footnotes. Screening records age,gender,weight,height,blood pressure; family history/lifestyle questionnaire smoking/alcohol. Optional4blood tubes (2EDTA+2serum). These are collection variables; no stated adjusted covariate set follows from their collection.

### PR-22: optional future biomarker specimens

Locations: pp.25–26,34,56–57. Key: optional biomarker work is separate from main diagnostic set. No fixed biomarker list or future timing; genetic/epigenetic and potentially exome/genome work permitted only for colorectal-neoplasia-related markers. Participation in main trial does not require blood. Day0four extra9–10mLtubes (2EDTA/2serum); serum8.5–9mL, EDTA9–10mL. Serum room temperature30min, maximum60min; centrifuge10min2500–3500RPM; EDTA invert8–10times; center storage4–8°C, pickup2–3days, transport onice; laboratory centrifuges2500–3500RPM/aliquots same day; serum/plasma stored−20°C, no time limit for future work. Blinded to treatment/clinical data; destruction can be requested. These auxiliary specimen quantities do not supply a trial result or change primary diagnostic denominator.

### PR-23: version and amendment authority

Locations: pp.1–62 headers,37,49–50,58. Key: protocolv1.5date24July2015. Change after approval requires written amendment signed by principal investigator/director/clinical pharmacology consultant and applicable approvals before implementation, immediate hazard exception. No actual amendment text/history provided here. p.49 scanned signed approval shows four signatories: principal investigator Thomas Seufferlein, coordinating director Brenner, clinical pharmacology consultant Czock, biometrician Kopp-Schneider; handwritten dates visibly August11,2015;July27,2015;July27,2015;July24,2015 respectively (administrative date transcription only). p.50 unsigned duplicate form. Appendix3 investigator future-amendment undertaking p.58. Footer pagination repeats49 at physical49/50; this is why physical links are mandatory.

### PR-24: missingness/data audit operations

Locations: pp.37–38,40–41,44. Key: request missing reports, actual timing/accountability. eCRF records eligibility, previous2week medication, dates including colonoscopy, optional blood, available clinical thrombocytes, AE and drop-out reasons if within3weeks. Diaries record if/when medication and stool samples. Randomized number generated only after randomization; screening failures documented without participant number. Original-entry audit trail preserved. Double blinded entry into additional study database; missing reports/data requested from centers by email/monitoring; original records checked for differing entries. No inferential imputation/exclusion algorithm is specified by these requests. Medication dispensed/used/returned quantities logged. Four site visits/year, early visit~20recruits are operational monitoring rather than statistical interim analysis.

### PR-25: financial appendix opened and mapped as administrative

Locations: pp.59–62. Key: not applicable to quantitative result review unless another source establishes a link. Three-page cost table and final footnotes are administrative budget, not observed trial counts or a power calculation. Printed category totals (€): external project13383; internal153000; clinical pharmacology30950; monitoring24790; monitoring travel3000; pharmacovigilance28922; data management40642; general KKS12731; practice compensation60000; medication3400; training2430; lab24881; other meetings500; fees6800; insurance67116; general35060; study budget505570. Footnotes cost2,000completed cases at€30,2,400participants for specimen/insurance/postage costs,4FOBGold assays/person at€1.5 (2400×4×1.5=14400 printed cost), assumptions1SAE/20participants and1SUSAR/1000 (100and2workloads),3amendments and other personnel/travel/printing schedules. These are financial workloads and cannot be treated as efficacy endpoint denominators, numeric safety stopping thresholds, observed events, or evidence of supplied amendments. No workbook formulas/caches exist; arithmetic expressions are PDF budget footnotes.

## Matching and bounded limitations

For downstream comparisons use keys for primary day3 FOBGold sensitivity/positivity cutpoints, advanced-neoplasm reference definition, secondary specificity/AUC/predictive values/LR, ASA300mg single uncoated dose, available diagnostic versus all-randomized safety populations, target2400/analyzed2000, power/prevalence assumptions, sex/neoplasm/multiday analyses, delayed-colonoscopy sensitivity analysis, withdrawals, and confirmatory/exploratory hierarchy. Main-paper page/relationship identifiers belong to the disjoint main mapper; none were invented here.

Bounded definition gaps in this protocol: no numeric ASTER positivity cutpoints, detailed advanced-adenoma morphology definition, exact diagnostic comparison/CI algorithm, adjustment covariates, explicit diagnostic imputation, multiday positivity-combination algorithm, numeric safety stopping rate, multiplicity adjustment, efficacy interim rule, or actual amendment history. These are extracted absences within DOC-002 only; the supplied SAP/report may provide them. This mapper does not classify absence as a finding.

Final scope status COMPLETE:62pages,25local relationship keys,3fresh visual pages,59reusable-backed pages,0unmapped pages. Every administrative/reference/signature/appendix page explicitly opened; no candidate diagnosis or external evidence used.
