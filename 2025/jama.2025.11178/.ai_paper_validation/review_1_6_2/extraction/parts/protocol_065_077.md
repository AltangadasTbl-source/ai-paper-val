# Fresh protocol support mapping: DOC-002 physical pages 65–77

- Runtime scope: protocol_mapper_c; fresh support quantitative mapping shard.
- Exact source: joi250046supp1_prod_1755300121.14087.pdf; document role PLAN, determined by prospective protocol content.
- Version: RESOLVE UH3 Protocol, version 5.0, 10 Nov 2022, repeated in page headers. Physical pages 65–77 correspond to printed pages 53–65.
- Assigned units: 13; reusable-backed 0; fresh-required 13; freshly mapped 13. All 13 source-derived page images were opened visually and all 13 OCR transcriptions were read. No other scientific source unit was inspected by this shard.
- Extraction engines: direct Poppler pdftotext 26.01.0 (native and layout per page); direct Poppler pdftoppm 26.01.0 (150 dpi PNG CPU render); Tesseract 5.5.0, eng, psm 3, OMP_THREAD_LIMIT=1, CPU. No fallback environment, Python extraction, external sources or prior scientific conclusions used.
- Derivative names: preprocessing/protocol_c/native-N.txt, layout-N.txt, page-N.png, ocr-N.txt for each physical page N from 65 through 77. Every native/layout file is retained as a font-corrupted derivative, not usable scientific prose. Fresh image and OCR derivatives close coverage.
- Exact command patterns: `pdftotext -f N -l N SOURCE native-N.txt`; `pdftotext -layout -f N -l N SOURCE layout-N.txt`; `pdftoppm -f 65 -l 77 -r 150 -png SOURCE page`; `OMP_THREAD_LIMIT=1 tesseract page-N.png ocr-N -l eng --psm 3`.
- Scientific coverage gaps: None. OCR limitations: minor punctuation, bullet, superscript and reference-number segmentation artifacts; cited substantive passages below were confirmed on images. Raw OCR is preserved verbatim after the mapping and is a transcription aid. No statistical formulas, workbook values, tables, figures, result estimates or inferential tests occur in this shard.

## Page-by-page complete coverage

Source links are relative to this part's actual location; physical PDF page anchors are used throughout.

| Physical page | Printed page | Content inspected | Mapping / no-applicable record | Status |
|---|---:|---|---|---|
| [65](../../../../joi250046supp1_prod_1755300121.14087.pdf#page=65) | 53 | Section 18 Quality control and quality assurance | P-C001 missing-data/data-anomaly clarification; no statistical missing-data method, endpoint, sample or result | COMPLETE |
| [66](../../../../joi250046supp1_prod_1755300121.14087.pdf#page=66) | 54 | Sections 19.1–19.4 ethics, IRB, exclusions, confidentiality | P-C002 age and language exclusions; P-C003 amendment approval provision; remaining content administrative, no quantitative result | COMPLETE |
| [67](../../../../joi250046supp1_prod_1755300121.14087.pdf#page=67) | 55 | Section 19.4.1 certificate of confidentiality | Administrative legal/privacy provisions only; no applicable result-relevant quantitative relationship | COMPLETE |
| [68](../../../../joi250046supp1_prod_1755300121.14087.pdf#page=68) | 56 | Sections 20–20.4 data handling, reports, records, deviations | P-C004 safety/DSMB reports and EDA; P-C005 primary/secondary/derivative analysis completion; record retention at least three years is administrative | COMPLETE |
| [69](../../../../joi250046supp1_prod_1755300121.14087.pdf#page=69) | 57 | Section 20.4 continuation, deviation reporting | Administrative reporting within 7 calendar days, repeated for rights/safety/welfare risk; no analysis rule or stopping threshold | COMPLETE |
| [70](../../../../joi250046supp1_prod_1755300121.14087.pdf#page=70) | 58 | Section 21 publication | Publication, registration and results submission policy; no applicable outcome hierarchy or statistical rule | COMPLETE |
| [71](../../../../joi250046supp1_prod_1755300121.14087.pdf#page=71) | 59 | Section 22 data sharing | P-C006 public database dictionary and unreliable elements; release at primary manuscript publication or within 12 months of last patient procedure, whichever first, is administrative | COMPLETE |
| [72](../../../../joi250046supp1_prod_1755300121.14087.pdf#page=72) | 60 | Section 23 references 1–19 | Bibliographic only; no trial quantitative relationship; reference years/volumes/pages are not trial quantities | COMPLETE |
| [73](../../../../joi250046supp1_prod_1755300121.14087.pdf#page=73) | 61 | References 20–37 | Bibliographic only; no trial quantitative relationship | COMPLETE |
| [74](../../../../joi250046supp1_prod_1755300121.14087.pdf#page=74) | 62 | References 38–55 (55 continues) | Bibliographic only; instrument names BPI, PROMIS, EQ-5D-5L, PHQ-8, GAD-7, pain scales locate cited methods; no trial outcome status/definition follows from citation alone | COMPLETE |
| [75](../../../../joi250046supp1_prod_1755300121.14087.pdf#page=75) | 63 | Reference 55 continuation, references 56–71 | Bibliographic only; no trial quantitative relationship | COMPLETE |
| [76](../../../../joi250046supp1_prod_1755300121.14087.pdf#page=76) | 64 | References 72–90 | P-C007 method citation locators 86–89; no new statistical specification; remaining bibliographic only | COMPLETE |
| [77](../../../../joi250046supp1_prod_1755300121.14087.pdf#page=77) | 65 | References 91–102 | Bibliographic only; economic net-benefit regression/acceptability-curve reference locators 91–93, childhood-intervention references 101–102; no new statistical specification | COMPLETE |

## Local relationship and context keys

These are source mapping records, not checker observations or candidates. Seven P-C keys retain all applicable contextual statements. Only P-C002 defines a numeric trial-population boundary; the others preserve administrative/analysis context without inventing a statistical design rule. No sample-size/power, endpoint definition/status/timepoint, model/covariates, analysis population label, imputation, sensitivity/subgroup result, multiplicity/interim/stopping rule, intervention dose/duration, or amendment/version difference is present in this exact shard. Its consistent version/date header identifies this content as version 5.0; comparison with other versions belongs to their assigned source scopes.

### P-C001 — Missing data clarification, section 18, physical page 65

Image-confirmed quotation: “Quality control (QC) procedures will be implemented beginning with the data collection and data QC checks that will be run on the database. Any missing data or data anomalies will be communicated to the site(s) for clarification/resolution.”

The Clinical Monitoring Plan is maintained by the CCC and Data Management Plan by the DCC. This is data collection/QC handling, with no imputation, missing-at-random assumption, excluded-participant rule or model specification. Matching main-paper key: data quality / missing data handling; do not equate database clarification with an inferential missing-data method.

### P-C002 — Eligibility boundary, section 19.3, physical page 66

Image-confirmed quotations: “Children under the age of 18 will be excluded.” “Adults who do not speak English will be excluded from study participation.”

The adult-tested telehealth CBT-CP interventions and assessment validation in adult samples are the stated rationale; pediatric mHealth versions contain a family component. Numeric population boundary: age less than 18 excluded; language boundary: non-English-speaking adults excluded. This section supplies no upper age limit or analyzed denominator. Matching main-paper keys: adult eligibility, age minimum and English language requirement.

### P-C003 — Amendment approval, section 19.2, physical page 66

Image-confirmed quotation: “Any amendment to the protocol will require review and approval by the IRB before the changes are implemented in the study.”

VUMC is the single IRB; KPGA, KPNW, KPWA and Essentia cede oversight. Approval of protocol and consent forms is required before enrollment. This states an administrative amendment process; no actual amendment or changed endpoint/model is supplied on this page. Matching main-paper key: disclosed protocol changes only if another source supplies the change itself.

### P-C004 — Safety and monitoring reports, section 20.2, physical page 68

Image-confirmed quotation: “For safety analyses and DSMB report production, the JHU-Tufts Statistical Core, physically located at the Johns Hopkins University will examine or oversee data quality, create secondary variables, and perform exploratory data analyses (EDA).”

DCC creates recruitment/data-collection, ongoing QA/DSMB and intervention monitoring reports or makes data available to the appropriate TIC/RIC. “Secondary variables” here denotes generated variables and does not designate secondary clinical outcomes. No stopping rule, safety threshold or safety-analysis population is defined. Matching main-paper key: monitoring/safety reporting, EDA scope.

### P-C005 — Completion of analyses, section 20.3, physical page 68

Image-confirmed quotation: “Completion of the research for this protocol should be anticipated to include planned primary and secondary analyses, as well as subsequent derivative analyses.”

Record retention is at least three years from submission of the last grant federal financial report. The completion statement does not name an outcome, hierarchy, analysis model or reporting time. Matching main-paper key: planned analysis completion; use named outcome/analysis definitions from other assigned pages for actual comparisons.

### P-C006 — Public database, section 22, physical page 71

Image-confirmed quotation: “The DCC will also prepare a data dictionary that provides a concise definition of every data element included in the database. If specific data elements have idiosyncrasies that might affect interpretation or analysis, this will be discussed in the dictionary document. Data elements that are considered unreliable will be deleted, and this will be noted in the documentation.”

Immediate context is the public/releasable de-identified database, which lacks institutional identifiers. It does not say the trial primary analysis deletes unreliable outcome data or define a missing-data strategy. Release timing is primary manuscript publication or within 12 months of last patient procedure, whichever first. Matching main-paper key: data availability/dictionary; no inferential analysis specification inferred.

### P-C007 — Bibliographic statistical-method locators, physical pages 76–77

Source-confirmed reference entries relevant as locators only:

- 86, physical page 76: “Zou G. A modified poisson regression approach to prospective studies with binary data. Am J Epidemiol. 2004;159(7):702-706.”
- 87, physical page 76: “SL LJZ. Longitudinal data analysis using generalized linear models. Biometrika. 1986;73(1):13-22.” Author string is preserved as supplied; no expansion inferred.
- 88, physical page 76: “COST-EFFECTIVENESS in HEALTH and MEDICINE. New York, NY: Oxford University Press, Inc.; 1996.”
- 89, physical page 76: “Sanders GD, Neumann PJ, Basu A, et al. Recommendations for Conduct, Methodological Practices, and Reporting of Cost-effectiveness Analyses: Second Panel on Cost-Effectiveness in Health and Medicine. Jama. 2016;316(10):1093-1103.”
- 91, physical page 77: “Hoch JS, Briggs AH, Willan AR. Something old, something new, something borrowed, something blue: a framework for the marriage of health econometrics and cost-effectiveness analysis. Health economics. 2002;11(5):415-430.”
- 92, physical page 77: “Hoch JS, Rockx MA, Krahn AD. Using the net benefit regression framework to construct cost-effectiveness acceptability curves: an example using data from a trial of external loop recorders versus Holter monitoring for ambulatory monitoring of ‘community acquired’ syncope. BMC Health Serv Res. 2006;6:68.”

No external reference was accessed. Matching main-paper keys: modified Poisson binary analysis, longitudinal GLM/GEE, economic analysis, only when identified by supplied plan/report prose elsewhere. These citations alone establish neither a covariance estimator nor a particular inferential method for the trial.

## Full per-page fresh OCR transcription

The following unedited OCR blocks preserve all page contents for locator use, including administrative text and bibliography. Source images govern punctuation, superscripts, reference numbering and any ambiguous token. Substantive passages quoted above were visually checked. Complete images remain in preprocessing/protocol_c.

### DOC-002 physical page 65 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

18 QUALITY CONTROL AND QUALITY ASSURANCE

The Clinical Monitoring Plan, maintained by the CCC, and Data Management Plan, maintained
by the DCC, describe the processes related to quality management for the study.

Quality control (QC) procedures will be implemented beginning with the data collection and data
QC checks that will be run on the database. Any missing data or data anomalies will be
communicated to the site(s) for clarification/resolution.

Following written Standard Operating Procedures (SOPs), the study monitors will verify that the
clinical trial is conducted, and data are generated, documented (recorded), and reported in
compliance with the protocol, International Conference on Harmonisation Good Clinical Practice
(ICH GCP), and applicable regulatory requirements.

The study sites will provide access to all trial-related locations, source data/documents, and
reports for the purpose of monitoring and auditing by the sponsor, and inspection by local and
regulatory authorities.

53

```

### DOC-002 physical page 66 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

19 ETHICS/PROTECTION OF HUMAN SUBJECTS
19.1 Ethical Standard

The investigator will ensure that this study is conducted in full conformity with the principles set
forth in The Belmont Report: Ethical Principles and Guidelines for the Protection of Human
Subjects of Research, as drafted by the US National Commission for the Protection of Human
Subjects of Biomedical and Behavioral Research (April 18, 1979) and codified in 45 CFR Part
46 and/or the ICH E6.

19.2 Institutional Review Board

The Vanderbilt University Medical Center (VUMC) IRB will serve as the single IRB (SIRB) for
this study. The local IRBs for KPGA, KPNW, KPWA and Essentia will cede oversight to the
VUMC IRB.

The protocol, informed consent form(s), recruitment materials, and all participant materials will
be submitted to the IRB for review and approval. Approval of both the protocol and the consent
form(s) must be obtained before any participant is enrolled. Any amendment to the protocol will
require review and approval by the IRB before the changes are implemented in the study.

19.3. Exclusion of Women, Minorities, and Children (Special Populations)

Children under the age of 18 will be excluded. mHealth versions of CBT-CP have been
developed for children and adolescents," but they all include a family component that differs
substantially from the telehealth CBT-CP programs under evaluation in this study, both of which
were developed and tested among adult samples. Further, our standardized assessment
measures were validated in adult samples and as such, are not always applicable to children
and adolescents.

Adults who do not speak English will be excluded from study participation. The interventions to
be studied in this comparative effectiveness trial have not been developed for or tested for
effectiveness in non-English speaking populations and are therefore not available for inclusion
in this trial.

19.4 Subject Confidentiality

Subject confidentiality is strictly held in trust by the investigators, study staff, and the study
sponsor(s) and their agents. This confidentiality is extended to any study information relating to
participants.

The study protocol, documentation, data, and all other information generated will be held in
strict confidence. No information concerning the study, or the data will be released to any
unauthorized third party without prior written approval of the study sponsor.

The study monitor(s) or other authorized representatives of the Data and Clinical Coordinating
Centers (DCC & CCC), NIH and the Institutional Review Board (IRB), may inspect all study
documents and records required to be maintained by the site investigators.

54

```

### DOC-002 physical page 67 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

19.4.1 Certificate of Confidentiality

To further protect the privacy of study participants, the Secretary, Health and Human Services
(HHS), has issued a Certificate of Confidentiality (CoC) to all researchers engaged in
biomedical, behavioral, clinical, or other human subjects research funded wholly or in part by
the federal government. Recipients of NIH funding for human subjects research are required to
protect identifiable research information from forced disclosure per the terms of the NIH Policy
(https:/humansubjects.nih.gov/coc/index). As set forth in 45 CFR Part 75.303(a) and NIHGPS
Chapter 8.3, recipients conducting NIH-supported research covered by this Policy are required
to establish and maintain effective internal controls (e.g., policies and procedures) that provide
reasonable assurance that the award is managed in compliance with Federal statutes,
regulations, and the terms and conditions of the award. It is the NIH policy that investigators and
others who have access to research records will not disclose identifying information except
when the participant consents or in certain instances when federal, state, or local law or
regulation requires disclosure. NIH expects investigators to inform research participants of the
protections and the limits to protections provided by a Certificate issued by this Policy.

55

```

### DOC-002 physical page 68 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

20 DATA HANDLING AND RECORD KEEPING

The investigators are responsible for ensuring the accuracy, completeness, legibility, and
timeliness of the data reported. All source documents should be completed in a neat, legible
manner to ensure accurate interpretation of data and kept in a secure file container throughout
the duration of the study. The investigators will maintain adequate case histories of study
participants, including accurate case report forms (CRFs), and source documentation.

20.1 Data Management Responsibilities

Data collection and accurate documentation are the responsibility of the study staff under the
supervision of the investigator. All source documents must be reviewed by the study team and
data entry staff, who will ensure that they are accurate and complete. Study staff are
responsible for training interviewers and providing participants’ clear and adequate instructions
for survey completion so that valid data capture is accomplished.

Unanticipated problems and AEs identified must be reviewed by the investigator or designee.

Data will be stored at the University of Utah and KP CHR, which are responsible for security of
their information systems.

20.2 Schedule and Content of Reports

The Data Coordinating Center will be responsible for creating the following reports or making
the data available to the appropriate TIC/RIC: recruitment and data collection reports, ongoing
QA monitoring and DSMB reports, and intervention monitoring reports. For safety analyses and
DSMB report production, the JHU-Tufts Statistical Core, physically located at the Johns Hopkins
University will examine or oversee data quality, create secondary variables, and perform
exploratory data analyses (EDA).

20.3 Study Records Retention

Study records will be maintained for at least three years from the date that the last grant federal
financial report (FFR) is submitted to the NIH.

Completion of the research for this protocol should be anticipated to include planned primary
and secondary analyses, as well as subsequent derivative analyses.

Completion of the research also entails completion of all publications relating to the research. All
records shall be accessible for inspection and copying by authorized representatives of the
regulatory authorities at reasonable times and in a reasonable manner [45 CFR §46.115(b)].

20.4 Protocol Deviations

A protocol deviation is any noncompliance with the clinical study protocol or Good Clinical
Practice requirements. The noncompliance may be on the part of the participant, the
investigator, or study staff. As a result of deviations, corrective actions are to be developed by
the study staff and implemented promptly as determined by the IRB.

These practices are consistent with ICH E6:

56

```

### DOC-002 physical page 69 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

e¢ Compliance with Protocol, section 4.5
¢ Quality Assurance and Quality Control, section 5.1
e Noncompliance, section 5.20

It is the responsibility of the Principal Investigator(s) to use continuous vigilance to identify and
report any deviations within 7 calendar days of identification of the protocol deviation to the
HEAL ERN within the DCC REDCap system. Protocol deviations that result in increased risk or
affect the participant’s rights, safety, or welfare will also be reported to the IRB and the NIA
Program Official within 7 calendar days of identification of the problem.

57

```

### DOC-002 physical page 70 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

21 PUBLICATION

The study PI in collaboration with select study team members will develop a publication policy
which will specify publication procedures and authorship requirements. The study will comply
with NIH’s Public Access Policy and Policy on the Dissemination of NIH-Funded Clinical Trial
Information, as described below.

NIH Public Access Policy
The NIH Public Access Policy requires scientists to submit final peer-reviewed journal

manuscripts that arise from NIH funds to PubMed Central immediately upon acceptance for
publication. This ensures that the public has access to the published results of NIH funded
research.

NIH Policy on the Dissemination of NIH-Funded Clinical Trial Information

The study is a clinical trial and will comply with the NIH policy that establishes the expectation
that all investigators conducting clinical trials funded in whole or in part by the NIH will ensure
that these trials are registered at ClinicalTrials.gov, and that results of these trials are submitted
to ClinicalTrials.gov.

58

```

### DOC-002 physical page 71 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

22 DATA SHARING

This study will comply with all applicable NIH Data Sharing Policies. (See
https://grants.nih.gov/policy/sharing.htm for policies and resources)

The DCC will produce a public/releasable database from the RESOLVE study. The releasable
database will be completely de-identified in accordance with the definitions provided in the
Health Insurance Portability and Accountability Act (HIPAA). Namely, all identifiers specified in
HIPAA will be recoded in a manner that will make it impossible to deduce or impute the specific
identity of any patient. The database will not contain any institutional identifiers.

The DCC will also prepare a data dictionary that provides a concise definition of every data
element included in the database. If specific data elements have idiosyncrasies that might affect
interpretation or analysis, this will be discussed in the dictionary document. Data elements that
are considered unreliable will be deleted, and this will be noted in the documentation.

The policies for release of this database will be determined by the NIH. These policies are
expected to focus primarily on the timing of data release. The preliminary plan is to release the
database (defined below) at the time of publication of the primary manuscript, or within 12
months of last patient procedure, whichever comes first. Implementation of the plan will follow
the HEAL Public Access and Data Sharing Policy as outlined at
https://heal.nih.gov/about/public-access-data.

In accordance with policies of the NIH, the DCC will send the releasable database and its
relevant documentation to the entity determined by the NIH or specific institute to be the
repository for data created under the HEAL initiative.

Access to the releasable database housed in the NIH-assigned repository will be in accordance
with procedures and regulations of the NIH or specific institute.

59

```

### DOC-002 physical page 72 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0

10 Nov 2022

23 REFERENCES

1.

2.

10.

11.

12.

13.

14.

15.

16.

17.

18.

19.

Institute of Medicine. Relieving Pain in America: A Blueprint for Transforming Prevention,
Care, Education and Research. Washington DC2011.

Pain Management Task Force. Providing a Standardized DoD and VHA Vision and
Approach to Pain Management to Optimize the Care for Warriors and their Families.
5/2010 2010.

Von Korff M, Scher Al, Helmick C, et al. United States National Pain Strategy for
Population Research: Concepts, Definitions, and Pilot Data. J Pain. 2016;17(10):1068-
1080.

Dahlhamer J, Lucas J, Zelaya C, et al. Prevalence of Chronic Pain and High-Impact
Chronic Pain Among Adults - United States, 2016. MMWR Morbidity and mortality
weekly report. 2018;67(36):1001-1006.

Rost K, Fortney J, Fischer E, Smith J. Use, quality, and outcomes of care for mental
health: the rural perspective. Med Care Res Rev. 2002;59(3):231-265; discussion 266-
271.

Tollefson J, Usher K. Chronic pain in the rural arena. The Australian journal of rural
health. 2006;14(3):134-135.

Goode AP, Freburger JK, Carey TS. The influence of rural versus urban residence on
utilization and receipt of care for chronic low back pain. J Rural Health. 2013;29(2):205-
214.

Hoffman PK, Meier BP, Council JR. A comparison of chronic pain between an urban and
rural population. Journal of community health nursing. 2002;19(4):213-224.

Nelson JA GB. Rural health: access to care and services. Home Health Care
Management and Practice. 2010;22(5):339-343.

Chou R, Turner JA, Devine EB, et al. The effectiveness and risks of long-term opioid
therapy for chronic pain: a systematic review for a National Institutes of Health Pathways
to Prevention Workshop. Ann Intern Med. 2015;162(4):276-286.

Von Korff MR, Franklin G. Responding to America's latrogenic Epidemic of Prescription
Opioid Addiction and Overdose. Med Care. 2016;54(5):426-429.

Von Korff M, Kolodny A, Deyo RA, Chou R. Long-term opioid therapy reconsidered. Ann
Intern Med. 2011;155(5):325-328.

Cicero TJ, Surratt H, Inciardi JA, Munoz A. Relationship between therapeutic use and
abuse of opioid analgesics in rural, suburban, and urban locations in the United States.
Pharmacoepidemiol Drug Saf. 2007;16(8):827-840.

Okie S. A flood of opioids, a rising tide of deaths. N Engl J Med. 2010;363(21):1981-
1985.

Von Korff MR. Health care for chronic pain: overuse, underuse, and treatment needs:
commentary on: chronic pain and health services utilization-is there overuse of
diagnostic tests and inequalities in nonpharmacologic methods utilization? Med Care.
2013;51(10):857-858.

Skelly AC, Chou R, Dettori JR, et al. AHRQ Comparative Effectiveness Reviews. In:
Noninvasive Nonpharmacological Treatment for Chronic Pain: A Systematic Review.
Rockville (MD): Agency for Healthcare Research and Quality (US); 2018.

Thorn BE, Day MA, Burns J, et al. Randomized trial of group cognitive behavioral
therapy compared with a pain education control for low-literacy rural people with chronic
pain. Pain. 2011;152(12):2710-2720.

Turk DC, Meichenbaum D, Genest M. Pain and behavioral medicine: A cognitive
behavioral perspective. New York: Guilford Press; 1983.

Interagency Pain Research Coordinating Committee. National Pain Strategy: A
Comprehensive Population Health-Level Strategy by Pain. 2015 2015.

60

```

### DOC-002 physical page 73 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0

10 Nov 2022

20,

21.

22.

23,

24.

25.

26.

27.

28.

29.

30.

31.

32.

33.

34.

35.

36.

37.

Stewart MO, Karlin BE, Murphy JL, et al. National dissemination of cognitive-behavioral
therapy for chronic pain in veterans: therapist and patient-level outcomes. Clin J Pain.
2015;31(8):722-729.

Keefe FJ, Main CJ, George SZ. Advancing Psychologically Informed Practice for
Patients With Persistent Musculoskeletal Pain: Promise, Pitfalls, and Solutions. Phys
Ther. 2018;98(5):398-407.

Waller G, Turner H. Therapist drift redux: Why well-meaning clinicians fail to deliver
evidence-based therapy, and how to get back on track. Behav Res Ther. 2016;77:129-
137.

Kapoor S, Thorn BE. Healthcare use and prescription of opioids in rural residents with
pain. Rural Remote Health. 2014;14(3):2879.

Cully JA, Jameson JP, Phillips LL, Kunik ME, Fortney JC. Use of psychotherapy by rural
and urban veterans. J Rural Health. 2010;26(3):225-233.

Cherkin DC, Sherman KJ, Balderson BH, et al. Effect of Mindfulness-Based Stress
Reduction vs Cognitive Behavioral Therapy or Usual Care on Back Pain and Functional
Limitations in Adults With Chronic Low Back Pain: A Randomized Clinical Trial. Jama.
2016;315(12):1240-1249.

Jensen MP, Nielson WR, Kerns RD. Toward the development of a motivational model of
pain self-management. J Pain. 2003;4(9):477-492.

Bair MJ, Matthias MS, Nyland KA, et al. Barriers and facilitators to chronic pain self-
management: a qualitative study of primary care patients with comorbid musculoskeletal
pain and depression. Pain medicine (Malden, Mass). 2009; 10(7):1280-1290.

Ludman EJ, Simon GE, Tutty S, Von Korff M. A randomized trial of telephone
psychotherapy and pharmacotherapy for depression: continuation and durability of
effects. J Consult Clin Psychol. 2007;75(2):257-266.

Simon GE, Ludman EJ, Tutty S, Operskalski B, Von Korff M. Telephone psychotherapy
and telephone care management for primary care patients starting antidepressant
treatment: a randomized controlled trial. Jama. 2004;292(8):935-942.

McBeth J, Prescott G, Scotland G, et al. Cognitive behavior therapy, exercise, or both for
treating chronic widespread pain. Arch Intern Med. 2012;172(1):48-57.

Eccleston C, Fisher E, Craig L, Duggan GB, Rosser BA, Keogh E. Psychological
therapies (Internet-delivered) for the management of chronic pain in adults. Cochrane
Database Syst Rev. 2014(2):Cd010152.

Macea DD, Gajos K, Daglia Calil YA, Fregni F. The efficacy of Web-based cognitive
behavioral interventions for chronic pain: a systematic review and meta-analysis. J Pain.
2010;11(10):917-929.

Waegemann CP. mHealth: the next generation of telemedicine? Telemedicine journal
and e-health : the official journal of the American Telemedicine Association.
2010;16(1):23-25.

Hamine S, Gerth-Guyette E, Faulx D, Green BB, Ginsburg AS. Impact of mHealth
chronic disease management on treatment adherence and patient outcomes: a
systematic review. J Med Internet Res. 2015;17(2):e52.

Mehrotra A RK, Brockmeyer DM, Barnett ML, Bender JA. Rapidly Converting to “Virtual
Practices : Outpatient Care in the Era of Covid-19. NEJM Catalyst. 2020.

Eccleston C, Blyth FM, Dear BF, et al. Managing patients with chronic pain during the
COVID-19 outbreak: considerations for the rapid introduction of remotely supported
(eHealth) pain management services. Pain. 2020;161(5):889-893.

Pitcher MH, Von Korff M, Bushnell MC, Porter L. Prevalence and Profile of High-Impact
Chronic Pain in the United States. J Pain. 2019;20(2):146-160.

61

```

### DOC-002 physical page 74 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0

10 Nov 2022

38.

39.

40.

41,

42.

43.

44.

45.

46.

47.

48.

49.

50.

51.

52.

53.

54.

55.

Ehde DM, Dillworth TM, Turner JA. Cognitive-behavioral therapy for individuals with
chronic pain: efficacy, innovations, and directions for research. Am Psychol.
2014;69(2):153-166.

Feinberg S, Feinberg R, Pohl M, Bokarius V, Darnall B. American Chronic Pain
Association Resource Guide to Chronic Pain Management. In. An Integrated Guide to
Medical, Interventional, Behavioral, Pharmacologic and Rehabilitation Therapies:
Rocklin, CA: American Chronic Pain Association, Inc; 2018.

Cleeland C, Ryan K. Pain assessment: global use of the Brief Pain Inventory. Annals of
the Academy of Medicine, Singapore. 1994;23(2):129-138.

Keller S, Bann CM, Dodd SL, Schein J, Mendoza TR, Cleeland CS. Validity of the brief
pain inventory for use in documenting the outcomes of patients with noncancer pain. The
Clinical journal of pain. 2004;20(5):309-318.

Tan G, Jensen MP, Thornby JI, Shanti BF. Validation of the Brief Pain Inventory for
chronic nonmalignant pain. The Journal of Pain. 2004;5(2):133-137.

Dworkin RH, Turk DC, McDermott MP, et al. Interpreting the clinical importance of group
differences in chronic pain clinical trials: IMMPACT recommendations. Pain.

2009; 146(3):238-244.

Carle AC, Riley W, Hays RD, Cella D. Confirmatory Factor Analysis of the Patient
Reported Outcomes Measurement Information System (PROMIS) Adult Domain
Framework Using Item Response Theory Scores. Med Care. 2015;53(10):894-900.
Herdman M, Gudex C, Lloyd A, et al. Development and preliminary testing of the new
five-level version of EQ-5D (EQ-5D-5L). Qual Life Res. 2011;20(10):1727-1736.
Hornbrook M, Goodman, M.J., ed Adjusting health benefit contributions to reflect risks.
Greenwich: JAI Press; 1991. Hornbrook M, ed. Risk Based Contributions to Private
Health Insurance; No. 41.

O'Keeffe-Rosetti MC, Hornbrook MC, Fishman PA, et al. A standardized relative
resource cost model for medical care: application to cancer control programs. Journal of
the National Cancer Institute Monographs. 2013;2013(46):106-116.

Kroenke K, Strine TW, Spitzer RL, Williams JB, Berry JT, Mokdad AH. The PHQ-8 as a
measure of current depression in the general population. J Affect Disord. 2009;114(1-
3):163-173.

Spitzer RL, Kroenke K, Williams JB, Lowe B. A brief measure for assessing generalized
anxiety disorder: the GAD-7. Arch Intern Med. 2006;166(10):1092-1097.

Full KM, Malhotra A, Crist K, Moran K, Kerr J. Assessing psychometric properties of the
PROMIS Sleep Disturbance Scale in older adults in independent-living and continuing
care retirement communities. Sleep Health. 2019;5(1):18-22.

Von Korff M, DeBar LL, Krebs EE, Kerns RD, Deyo RA, Keefe FJ. Graded chronic pain
scale revised: mild, bothersome, and high-impact chronic pain. Pain. 2020;161(3):651-
661.

Mayhew M, DeBar LL, Deyo RA, et al. Development and Assessment of a Crosswalk
Between ICD-9-CM and ICD-10-CM to Identify Patients with Common Pain Conditions. J
Pain. 2019.

McWilliams LA, Kowal J, Wilson KG. Development and evaluation of short forms of the
Pain Catastrophizing Scale and the Pain Self-efficacy Questionnaire. Eur J Pain.
2015;19(9):1342-1349.

Anderson KO, Dowds BN, Pelletz RE, Edwards WT, Peeters-Asdourian C. Development
and initial validation of a scale to measure self-efficacy beliefs in patients with chronic
pain. Pain. 1995;63(1):77-84.

Vugts MAP, Joosen MCW, van der Geer JE, Zedlitz A, Vrijhoef HJM. The effectiveness
of various computer-based interventions for patients with chronic pain or functional

62

```

### DOC-002 physical page 75 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

somatic syndromes: A systematic review and meta-analysis. PloS one.
2018;13(5):e0196467.

56. Martorella G, Boitor M, Berube M, Fredericks S, Le May S, Gelinas C. Tailored Web-
Based Interventions for Pain: Systematic Review and Meta-Analysis. J Med Internet
Res. 2017;19(11):e385.

57. Bennell KL, Nelligan RK, Rini C, et al. Effects of internet-based pain coping skills training
before home exercise for individuals with hip osteoarthritis (HOPE trial): a randomised
controlled trial. Pain. 2018;159(9):1833-1842.

58. Bennell KL, Nelligan R, Dobson F, et al. Effectiveness of an Internet-Delivered Exercise
and Pain-Coping Skills Training Intervention for Persons With Chronic Knee Pain: A
Randomized Trial. Ann Intern Med. 2017;166(7):453-462.

59. Rini C, Porter LS, Somers TJ, et al. Automated Internet-based pain coping skills training
to manage osteoarthritis pain: a randomized controlled trial. Pain. 2015;156(5):837-848.

60. Rini C, Porter LS, Somers TJ, McKee DC, Keefe FJ. Retaining critical therapeutic
elements of behavioral interventions translated for delivery via the Internet:
recommendations and an example using pain coping skills training. J Med Internet Res.
2014;16(12):e245.

61. Bair MJ, Ang D, Wu J, et al. Evaluation of Stepped Care for Chronic Pain (ESCAPE) in
Veterans of the Iraq and Afghanistan Conflicts: A Randomized Clinical Trial. JAMA
Intern Med. 2015;175(5):682-689.

62. Kroenke K, Bair MJ, Damush TM, et al. Optimized antidepressant therapy and pain self-
management in primary care patients with depression and musculoskeletal pain: a
randomized controlled trial. JAMA. 2009;301(20):2099-2110.

63. Kealey KA, Ludman EJ, Marek PM, Mann SL, Bricker JB, Peterson AV. Design and
implementation of an effective telephone counseling intervention for adolescent smoking
cessation. Journal of the National Cancer Institute. 2009;101(20):1393-1405.

64. McClure JB, Ludman EJ, Grothaus L, Pabiniak C, Richards J. Impact of a brief
motivational smoking cessation intervention the Get PHIT randomized controlled trial.
Am J Prev Med. 2009;37(2):116-123.

65. Simon GE, Ludman EJ, Rutter CM. Incremental benefit and cost of telephone care
management and telephone psychotherapy for depression in primary care. Arch Gen
Psychiatry. 2009;66(10):1081-1089.

66. Simon GE, VonKorff M, Rutter C, Wagner E. Randomised trial of monitoring, feedback,
and management of care by telephone to improve treatment of depression in primary
care. Bmj. 2000;320(7234):550-554.

67. Wang PS, Simon GE, Avorn J, et al. Telephone screening, outreach, and care
management for depressed workers and impact on clinical and work productivity
outcomes: a randomized controlled trial. JAMA. 2007;298(12):1401-1411.

68. Carmody TP, Duncan CL, Huggins J, et al. Telephone-delivered cognitive-behavioral
therapy for pain management among older military veterans: a randomized trial. Psychol
Serv. 2013;10(3):265-275.

69. Rutledge T, Atkinson JH, Chircop-Rollick T, et al. Randomized Controlled Trial of
Telephone-delivered Cognitive Behavioral Therapy Versus Supportive Care for Chronic
Back Pain. Clin J Pain. 2018;34(4):322-327.

70. DeBar L, Mayhew M, Benes L, et al. A Primary Care-Based Cognitive Behavioral
Therapy Intervention for Long-Term Opioid Users With Chronic Pain: A Randomized
Pragmatic Trial. Annals of internal medicine. 2022;175(1):46-55.

71. DeBar L, Benes L, Bonifay A, et al. Interdisciplinary team-based care for patients with
chronic pain on long-term opioid treatment in primary care (PPACT) - Protocol for a
pragmatic cluster randomized trial. Contemp Clin Trials. 2018;67:91-99.

63

```

### DOC-002 physical page 76 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0

10 Nov 2022

72,

73.

74.

75.

76.

77.

78.

79.

80.

81.

82.

83.

84.

85.

86.

87.

88.

89.

90.

Bandura A. Self-efficacy: The exercise of control. New York: W.H. Freeman and
Company.; 1997.

Bandura A. Social foundations of thought and action: A social cognitive theory.
Englewood Cliffs, N.J.: Prentice-Hall; 1986.

Kennedy CM, Powell J, Payne TH, Ainsworth J, Boyd A, Buchan I. Active Assistance
Technology for Health-Related Behavior Change: An Interdisciplinary Review. Journal of
Medical Internet Research. 2012;14(3):e80.

Knowles MS, Holton EF, Swanson RA. The adult learner: The definitive classic in adult
education and human resource development. 7th ed. Boston: Elsevier; 2011.

Mayer RE. Applying the science of learning: evidence-based principles for the design of
multimedia instruction. American Psychologist. 2008;63(8):760-769.

Michie S, Richardson M, Johnston M, et al. The behavior change technique taxonomy
(v1) of 93 hierarchically clustered techniques: building an international consensus for the
reporting of behavior change interventions. Ann Behav Med. 2013;46(1):81-95.

Rini C, Williams DA, Broderick JE, Keefe FJ. Meeting them where they are: Using the
Internet to deliver behavioral medicine interventions for pain. Trans! Behav Med.
2012;2(1):82-92.

The Plain Language Action and Information Network. plainlanguage.gov.
https://plainlanquage.gov/. Accessed February 5, 2019.

Bellg AJ, Borrelli B, Resnick B, et al. Enhancing treatment fidelity in health behavior
changer studies: Best practices and recommendations from the NIH Behavior Change
Consortium. Health Psychology. 2004;23(5):443-451.

Von Korff M, Balderson BH, Saunders K, et al. A trial of an activating intervention for
chronic back pain in primary care and physical therapy settings. Pain. 2005;113(3):323-
330.

Vitiello MV, McCurry SM, Shortreed SM, et al. Cognitive-behavioral treatment for
comorbid insomnia and osteoarthritis pain in primary care: the lifestyles randomized
controlled trial. J Am Geriatr Soc. 2013;61(6):947-956.

Bennell KL, Ahamed Y, Jull G, et al. Physical Therapist-Delivered Pain Coping Skills
Training and Exercise for Knee Osteoarthritis: Randomized Controlled Trial. Arthritis
Care Res (Hoboken). 2016;68(5):590-602.

Palermo TM, Slack K, Loren D, Eccleston C, Jamison RN. Measuring and reporting
adverse events in clinical trials of psychological treatments for chronic pain. Pain.
2020;161(4):713-717.

Peterson K, Anderson J, Bourne D, Mackey K, Helfand M. Effectiveness of Models Used
to Deliver Multimodal Care for Chronic Musculoskeletal Pain: a Rapid Evidence Review.
J Gen Intern Med. 2018;33(Suppl 1):71-81.

Zou G. A modified poisson regression approach to prospective studies with binary data.
Am J Epidemiol. 2004;159(7):702-706.

SL LJZ. Longitudinal data analysis using generalized linear models. Biometrika.
1986;73(1):13-22.

COST-EFFECTIVENESS in HEALTH and MEDICINE. New York, NY: Oxford University
Press, Inc.; 1996.

Sanders GD, Neumann PJ, Basu A, et al. Recommendations for Conduct,
Methodological Practices, and Reporting of Cost-effectiveness Analyses: Second Panel
on Cost-Effectiveness in Health and Medicine. Jama. 2016;316(10):1093-1103.

Smith DH, O'Keeffe-Rosetti M, Owen-Smith AA, et al. Improving Adherence to
Cardiovascular Therapies: An Economic Evaluation of a Randomized Pragmatic Trial.
Value in Health. 2016;19(2):176-184.

64

```

### DOC-002 physical page 77 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0

10 Nov 2022

91,

92.

93.

94,

95.

96.

97.

98.
99.
100.
101.

102.

Hoch JS, Briggs AH, Willan AR. Something old, something new, something borrowed,
something blue: a framework for the marriage of health econometrics and cost-
effectiveness analysis. Health economics. 2002;11(5):415-430.

Hoch JS, Rockx MA, Krahn AD. Using the net benefit regression framework to construct
cost-effectiveness acceptability curves: an example using data from a trial of external
loop recorders versus Holter monitoring for ambulatory monitoring of "community
acquired" syncope. BMC Health Serv Res. 2006;6:68.

Meenan RT, Stevens VJ, Hornbrook MC, et al. Cost-effectiveness of a hospital-based
smoking cessation intervention. Medical care. 1998;36(5):670-678.

Aarons GA, Hurlburt M, Horwitz SM. Advancing a conceptual model of evidence-based
practice implementation in public service sectors. Adm Policy Ment Health. 2011;38(1):4-
23.

Glasgow RE. RE-AlMing research for application: ways to improve evidence for family
medicine. J Am Board Fam Med. 2006;19(1):11-19.

Glasgow RE, Vogt TM, Boles SM. Evaluating the public health impact of health
promotion interventions: the RE-AIM framework. Am J Public Health. 1999;89(9):1322-
1327.

Sekhon M, Cartwright M, Francis JJ. Acceptability of healthcare interventions: an
overview of reviews and development of a theoretical framework. BMC Health Services
Research. 2017;17(1):88.

Bernard HR. Research methods in anthropology: Qualitative and quantitative
approaches. 2nd Edition ed. Thousand Oaks, CA: Sage Publications; 1994.

Miller WL, Crabtree BF. Clinical research. In: Denzin NK, Lincoln YS, eds. Strategies of
Qualitative Inquiry. Thousand Oaks, California: Sage Publications; 1998:292-314.
Spradley JP. Participant Observation. New York: Holt, Rinehart & Winston; 1980.
Palermo TM, Law EF, Fales J, Bromberg MH, Jessen-Fiddick T, Tai G. Internet-
delivered cognitive-behavioral treatment for adolescents with chronic pain and their
parents: a randomized controlled multicenter trial. Pain. 2016;157(1):174-185.
Eccleston C, Palermo TM, Williams AC, et al. Psychological therapies for the
management of chronic and recurrent pain in children and adolescents. Cochrane
Database Syst Rev. 2014(5):Cd003968.

65

```
