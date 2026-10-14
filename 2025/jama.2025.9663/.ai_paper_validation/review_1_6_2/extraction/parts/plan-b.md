# DOC-002 plan-b source evidence mapping

Scope: supplied PDF `joi250042supp1_prod_1753377747.92525.pdf`, physical PDF pages 29–56, 28/28 pages mapped. Document role PLAN throughout. Pages 29–41 are original protocol v1.1, 14 December 2020 (printed pages 28–40); pages 42–56 start final protocol v1.8, 14 October 2024 (printed pages 1–15). No source outside this assignment was read for scientific mapping.

Evidence method: every assigned page opened visually using the hashed, source-linked full-page PNG `.ai_paper_validation/review_1_5_1/preprocessing/doc002_b/page-NNN.png`; new coordinator GPU OCR `.ai_paper_validation/review_1_6_2/preprocessing/doc002/ocr-NNN.txt` was used as a locator where available. Legacy raster engine metadata is incomplete. GPU OCR omitted entire lines in multiple design paragraphs and rotated labels in the intervention graphic; the following transcription is based on visual page contents. No rendering, OCR, source modification or reusable-asset modification was performed by this mapper. No scientific coverage gaps remain. Final candidate recheck must use the exact supplied source page.

## Complete page coverage

| Physical PDF page | Content and complete mapping | Relationship keys | Status |
|---:|---|---|---|
| 29 | v1.1 clinical/economic outcomes; complete sample-size inputs; pilot progression; ITT and prospective SAP declaration | N2001–N2003; S2001–S2003 | COMPLETE |
| 30 | v1.1 primary and secondary models; covariate selection; subgroup interactions; interim stopping; economic resource sampling | N2004; S2004–S2009 | COMPLETE |
| 31 | v1.1 economic costs, HrQoL, QALYs, net monetary benefit, clustered model and lifetime projection | N2005; S2010–S2012 | COMPLETE |
| 32 | v1.1 monitoring; trial closure; repeated interim stopping; archiving | S2008; non-applicable administrative numbers recorded below | COMPLETE |
| 33 | v1.1 oversight and ethics; no additional quantitative analysis specification | Not applicable: administrative content | COMPLETE |
| 34 | v1.1 ethics, registration, confidentiality and dissemination; no additional statistical design | Not applicable: administrative content | COMPLETE |
| 35 | v1.1 dataset access, sponsorship and funding; no result-relevant numeric relationship | Not applicable: administrative content | COMPLETE |
| 36 | v1.1 references 1–16; bibliographic numbers only | Not applicable: references | COMPLETE |
| 37 | v1.1 references 16–30; bibliographic numbers only | Not applicable: references | COMPLETE |
| 38 | v1.1 version-history table: initial approved version 1.1, 14 December 2020 | Version provenance; no additional result relationship | COMPLETE |
| 39 | v1.1 conservative intervention algorithm, both receiving and not receiving oxygen | N2006 | COMPLETE |
| 40 | v1.1 usual-oxygen algorithm | N2007 | COMPLETE |
| 41 | v1.1 expected SAE types and ascertainment window | N2008 | COMPLETE |
| 42 | v1.8 title page; conservative versus usual oxygen in invasively ventilated adults | Version provenance; no additional numeric design | COMPLETE |
| 43 | v1.8 identifiers and date; no result-relevant quantity | Version provenance; not applicable administrative identifiers | COMPLETE |
| 44 | v1.8 signatures and commitment to explain discrepancies from plan | Version provenance; not applicable administrative content | COMPLETE |
| 45 | v1.8 contacts; no statistical content | Not applicable: contact information | COMPLETE |
| 46 | v1.8 investigator roster; no statistical content | Not applicable: personnel | COMPLETE |
| 47 | v1.8 summary eligibility and intervention definitions | N2009 | COMPLETE |
| 48 | v1.8 summary sample size and full clinical/economic outcome hierarchy | N2010–N2011; S2013 | COMPLETE |
| 49 | v1.8 contents: navigation only, no new design inputs | Not applicable: table of contents | COMPLETE |
| 50 | v1.8 contents continued: navigation only | Not applicable: table of contents | COMPLETE |
| 51 | v1.8 abbreviations, including ARR, RRR, FiO2, SpO2, QALY | N2012 | COMPLETE |
| 52 | v1.8 rationale and historical observational/meta-analysis results | N2013; background context explicitly bounded below | COMPLETE |
| 53 | v1.8 historical trials and anticipated baseline mortality; stated recruitment target | N2014; S2014 | COMPLETE |
| 54 | v1.8 standalone power/target and planned pooled analysis; historical feasibility trial; routine-data design; superiority aim and outcomes | N2015; S2015–S2016 | COMPLETE |
| 55 | v1.8 outcome objectives continued; ordinal organ-support definition; registry-embedded individual-randomization design and setting | N2011; S2013 | COMPLETE |
| 56 | v1.8 full population and eligibility, 12-hour enrolment window | N2009; S2017 | COMPLETE |

## Source-grounded extraction

### Original protocol v1.1, PDF page 29

Clinical primary: “90-day all-cause mortality.” Primary economic: incremental costs, QALYs and net monetary benefit at 90 days. Clinical secondary: ICU and hospital mortality censored at 90 days; mortality at 60 days and one year; ICU and acute-hospital duration censored at 90 days; HrQoL by EQ-5D-5L at 90 days. Economic secondary: HrQoL EQ-5D-5L at 90 days; resource use and costs at 90 days; estimated lifetime incremental cost-effectiveness.

Sample-size inputs: CMP potentially eligible patients N=96,028, April 2017–March 2019; Risk II N=82,075, April 2014–March 2016; anticipated 90-day mortality 37%; clinically important absolute reduction 2.5%, relative reduction 6.8%; alternative mortality 34.5%; power 90%; required total 15,444; allowance 6% refusal of consent/withdrawal/loss to follow-up; recruitment total 16,500. This page does not state test family, allocation ratio or significance level for the calculation. Recruitment assumptions 8 patients per unit per month, half the observed eligible-patient median, 100 ICUs, two years, staggered opening over 6 months.

Pilot analysis: end of internal-pilot months 7–12, analysis month 14; all green permits unchanged progression, any amber leads to amendment, any red stops trial; funder decides after TSC recommendation. Clinical analyses lodged a priori in SAP before investigators are unblinded to study outcomes; “All analyses will follow the intention to treat principle.”

### Original protocol v1.1, PDF page 30

Baseline characteristics compared to observe balance/success of randomization; “These comparisons will not be subject to statistical testing.” Primary 90-day outcome analyzed both with stratification-only adjustment (site, hypoxic ischaemic encephalopathy, acute brain pathologies excluding that encephalopathy, sepsis) and adjustment for additional baseline covariates. Primary analysis adjusts stratification variables and other prespecified risk factors. Regression incorporates site random effects; absolute risk reduction and relative risk reported. Additional covariates selected a priori for established outcome relationship, not observed imbalance, univariable significance or stepwise selection.

Secondary outcomes: similar regression with binomial/Poisson family for binary, normal family for continuous outcomes; critical-care/acute-hospital duration by Wilcoxon rank-sum tests stratified by survival status; Kaplan–Meier plots and Cox models with shared site frailty. Primary outcome subgroup analysis tests treatment-by-subgroup interaction in adjusted regression. Named key subgroups: suspected hypoxic-ischaemic encephalopathy; acute brain injury excluding such encephalopathy; sepsis.

Two interim analyses after recruitment and 90-day follow-up of 4,500 and 10,000 patients; Peto–Haybittle P<0.001 to recommend early termination for effectiveness or harm; further analyses if DMEC requests. This is repeated in section 6.1.1 on PDF page 32, with follow-up rather than explicitly 90-day follow-up.

Economic evaluation follows ITT; compares conservative versus usual oxygen; patient outcomes/resources linked to CMP and hospital episode statistics; health and personal-health-services perspective; detailed inpatient/resource monitoring for 15% of participants, subsequent health-service and EQ-5D-5L questionnaires; validated regression predicts resource use for all participants.

### Original protocol v1.1, PDF page 31

Total per-patient costs up to 90 days from resource use multiplied by NHS/PSSRU unit costs. HrQoL at 90 days measured in 15% selected participants, appropriate EQ-5D-5L value set; predicts HrQoL for all. QALYs by area-under-curve: survivors' baseline EQ-5D assumed zero, linear interpolation to day-90 score; decedents before day 90 assigned zero QALYs. “Net monetary benefits will be calculated by valuing QALY gains at £20,000 per QALY and subtracting incremental costs.” ITT mean incremental costs, QALYs, net monetary benefit with 95% CI at 90 days; multilevel linear regression accounts for site clustering and adjusts patient/site baseline covariates. Extensive sensitivity analyses; all clinical subgroups repeated for economic outcomes. Lifetime projection: survivors of initial acute-hospital episode and readmissions to same critical-care unit to day 90; estimate excess mortality relative to age/gender-matched population; model survival/HrQoL during excess-mortality period, then use general-population values; morbidity costs estimated at day 90 projected during excess-mortality period; derive lifetime incremental costs, QALYs and net benefits.

### Original protocol v1.1, PDF pages 32–38

PDF32 contains repeated interim rule above, plus last-patient/last-follow-up end definition; 25% sites anticipated to receive monitoring visit; central and local archiving 15 years. PDF33 contains TSC 75% independent membership, quarterly TMG meetings and at-least-annual TSC. PDF34–35 contain ethical identifiers, dataset access, confidentiality and funding, without further statistical design. PDF36–37 contain references, with no local reported-result inputs. PDF38 version history lists only initial approved v1.1 dated 14 December 2020. Administrative quantities are covered but are not result-relevant relationships.

### Original protocol v1.1, PDF pages 39–41

Conservative oxygen while receiving oxygen: upper SpO2 alarm 94%, lower 89%; SpO2>93%: reduce FiO2 until SpO2<94%; provide lowest FiO2 achieving SpO2 90%; SpO2<90%: increase FiO2 until SpO2>89%. When not receiving oxygen: lower alarm 89%, SpO2<90% leads to FiO2 increase until SpO2>89%. Footnote permits lower alarm reduction when clinically indicated. Usual oxygen: do not set upper SpO2 alarm, lower 89%, same clinical-indication footnote. Expected SAEs to critical-care discharge after randomization: sinus tachycardia; supraventricular tachycardia; atrial fibrillation; myocardial ischaemia/infarction; mesenteric ischaemia; recorded/reported under section 3.7.

### Final protocol v1.8, PDF pages 42–51

Title/identifier/signature/contact/roster pages42–46 establish prospective protocol v1.8 dated 14 October 2024, not a results supplement. Summary PDF47: adults ≥18; invasive MV in ICU after unplanned ICU admission OR MV started in ICU; supplemental FiO2>0.21 at enrolment. Exclusions: prior UK-ROX randomization in last 90 days; current ECMO; clinician considers either arm indicated/contraindicated. Conservative versus usual oxygen.

PDF48: randomized, unblinded registry-embedded trial with internal pilot/economic evaluation; target16,500; primary90-day all-cause mortality. Secondary: in-hospital mortality censored90 days; mortality at ICU discharge,60 days,one year; ICU/acute-hospital duration censored90 days; days alive/free of organ support at30 days, “an ordinal outcome with death as the worst outcome”, organ support defined respiratory/cardiovascular/renal within critical care by Critical Care Minimum Dataset; EQ-5D-5L HrQoL90 days. Economic primary costs/QALYs/net monetary benefit90 days; secondary HrQoL90 days, resources/costs90 days,lifetime incremental cost-effectiveness. PDF49–50 navigation only. PDF51 defines ARR absolute risk reduction, RRR relative risk reduction, FiO2 fractional inspired oxygen concentration, SpO2 peripheral arterial oxygen saturation, QALY quality-adjusted life year, INB incremental net benefit; CI in abbreviation table denotes Chief Investigator, whereas interval notation is spelled out locally in statistical text.

### Final protocol v1.8, PDF pages 52–56

Historical/context inputs, bounded to supplied printed text, without consulting cited external literature: PDF52 UK184,000 annual adult ICU admissions, over30%(55,000) MV; oxygen21%–100%; background guidance avoids SpO2>96%; observational study12 ICUs/ABGs to7 days/multivariable logistic regression; ten ARDS studies; historical meta-analyses RR1.21(95%CI1.03–1.43), OR1.22(1.12–1.33); ICU-ROX1000 participants. PDF53: ICU-ROX target91%–96%, day28 ventilator-free outcome; four ICU RCTs1983 participants pooled mortality RR0.91(0.75–1.09), uncertain benefit; ARDS trial205,28-day survival; CMP337,312 ICU admissions April2017–March2019,96,028(29%)MV,34%hospital mortality, anticipated37%90-day mortality; extrapolated >3000 lives annually; COVID MV72%; UK-ROX target16,500.

PDF54: planned harmonization of16,500 UK-ROX participants with Mega-ROX individual-patient meta-analysis; UK-ROX standalone90%power for2.5%absolute90-day mortality reduction; hospital mortality secondary to harmonize with Mega-ROX primary. Historical feasibility target60 across2 sites, recruited34; prior conservative target88%–92%, control≥96%, distinct from current protocol algorithm. Routine-data design requires additional primary collection in15%. Explicit current aim: conservative oxygen “superior to usual oxygen therapy” in non-elective adults receiving MV and supplemental oxygen, all-cause mortality90 days. Objectives name primary clinical90-day mortality, primary economic costs/QALYs/net monetary benefit90 days, ICU/hospital mortality censored90 days.

PDF55 continues secondary objectives:60-day/one-year mortality; ICU/acute-hospital duration censored90 days;30-day organ-support-free survival ordinal with death worst, respiratory/cardiovascular/renal CCMDS definition; HrQoL90 days. Individual patient randomization, registry-embedded/internal pilot/economic evaluation;100 NHS adult ICUs in England/Wales/Northern Ireland, general and specialist/medical/surgical/mixed units.

PDF56: adults in those countries receiving invasive MV enrolled within12 hours of fulfilling eligibility. Age≥18; unplanned ICU admission means not after elective procedure, OR MV started in ICU means intubated in ICU; FiO2>0.21 at enrolment. Exclusions repeated exactly as summary PDF47–48. No further primary model, imputation, multiplicity or subgroup definition appears on this page.

## Bounded limitations

No missing scientific page coverage. Native PDF prose is unusable glyph-mapped text and GPU OCR is incomplete; all28 page images were read directly to resolve these derivative limitations. Exact quantitative/design details above are visually legible. No workbook formulas/cached values, CSV cells or Office paragraph groups exist in this assigned PDF scope. Historical/background numbers are mapped as context and are not implicitly promoted into current-trial inputs. Main-paper matching keys are semantic endpoint/population/model identifiers in the two companion inventories; external-scope counterparts were not read or diagnosed here.
