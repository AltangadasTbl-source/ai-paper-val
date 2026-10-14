# Cross-source consistency review

Runtime agent: /root/cross_source_checker. Fresh mandatory cross_source_consistency_reviewer, gpt-6.1-sol/medium. Scope: complete main map M001–M100 and six support parts, encompassing all 404 mapped PDF pages in six supplied sources. All applicable relationships were reviewed by content and matched on population, time, contrast, model, measure, analysis set and precision. No supplied structured data exists. Administrative collaborator/data-sharing material contains no additional matched numerical results. Source PDFs are final authority; old scientific outputs and external sources were not read.

## Source precedence and evidence

DOC-001 and DOC-004–006 are REPORT. DOC-002 and DOC-003 are PLAN throughout, including bound prior versions. R-SAP version3 dated22July2022 identifies MasterSAP1.0, MasterProtocol4.0 and RSA5.0 as governing; its authority table on PDF104 gives R-SAP precedence for secondary analyses and shared controls. Supplied MasterSAP3.0 applies later RSAs initiated after February2023 and is not retroactively substituted for the regimen plan. MasterProtocol5.0/RSA6.0 are later supplied versions. Explicit amendments and version scope are retained in findings; a status or analysis change in routeA5 remains reportable and does not imply a protocol violation.

Direct source extraction: bundled pdf_tools.py with /home/juliz/venvs/stt/bin/python, PyMuPDF1.28.0, sorted native/layout engine, generated preprocessing/cross-source/main.txt (DOC001pp1–9), sap.txt (DOC003pp109–130), rsa.txt (DOC002pp184–185). DOC004 direct-layout extraction produced by support mapper was also read. Source-rendered main-p4.png, supp-p15.png and sap-p118.png were generated and visually inspected using PyMuPDF1.28.0, CPU200dpi. Native text plus reusable source-linked images cover remaining exact locations. No new OCR needed; no CPU OCR was used.

## Complete matched-relationship checklist

Thirty disjoint comparison families summarize the full applicable union rather than selecting findings. Each family includes every applicable mapped member, including dose variants and all criterion-list items.

| Family | Matched content | Result |
|---|---|---|
| XS01 | Abstract/KeyPoints/body primary DRR, CrI, posterior probability, doses, allocation, duration | Reconcile, including .6450 displayed .65 |
| XS02 | Abstract/body demographics and completion; Figure1 | Precision-screened age/completion copies; death-count locator correction below |
| XS03 | Abstract/body/supplement common adverse events and safety denominators | Precision-screened fatigue/count copies; efficacy164 distinguished from safety163 |
| XS04 | Primary component function slopes and all CrI limits in body/Figure2/eTable2 | Precision differences screened |
| XS05 | Primary mortality component rates, body/eTable2 | F-XS-001 |
| XS06 | All pooled/dose/FAS/ERO SVC and ALSFRS counterparts | F-XS-002; populations otherwise match |
| XS07 | All six Table2 HR/CI/count/P counterparts and Figure2/narrative | F-XS-003; sex-covariate specification F-XS-004 |
| XS08 | Mortality counts, follow-up versus treatment discontinuation, figure/body/discussion | Source correction reconciles death1; 13vs14 precision-screened |
| XS09 | Serum/plasma NfL body/Figure3/eTable3B and sensitivity/eFigure | Exploratory numerical copies screened as peripheral; prespecification F-XS-010 |
| XS10 | All35 subgroup rows and labels/narrative/eMethods/eTable4 | Specification F-XS-009; printed subgroup inference otherwise matches |
| XS11 | Every master/regimen eligibility criterion and gold allergy | Criteria correspond; report explicitly refers to full protocol; abbreviated list is not a changed eligibility list |
| XS12 | Randomization strata, two-stage assignment, dose3:3:2, pool3:1 | Regimen rules match; later master third-drug stratum not applicable |
| XS13 | Randomized oral30/60mg, bottles/concentration,24weeks, dose reduction | Match; OLE amendments explicitly separate from RCT |
| XS14 | Primary endpoint/function-survival composite/24week time point/DRR direction | Match |
| XS15 | Secondary/exploratory/safety outcome criterion lists, hierarchy | Status pattern F-XS-008 |
| XS16 | Six-point ALSFRS outcome, proportion versus first-event/death composite | F-XS-011 |
| XS17 | Primary shared-parameter model, adjustment and death contribution | Report model/4covariates match regimen-era description; later six-covariate master not substituted |
| XS18 | Shared-control FAS, concurrency/ECC, ERO, ECM, EPP, as-randomized/as-treated | FAS/ERO and safety match; unreported planned ECM/EPP F-XS-007 |
| XS19 | Missing data, treatment-policy follow-up, covariance and imputation sensitivity | MAR reported; planned sensitivity results absent F-XS-007 |
| XS20 | CAFS ranking, pair-comparison time, adjustment/test/version | F-XS-005 |
| XS21 | SVC repeated-measures versus random slopes, covariates/visit interaction | Report distinguishes models; unit issue XS06; missing sensitivities XS19 |
| XS22 | PAV/death definitions, threshold>22h/day>7days, baseline exclusions | Composite definition matches; exclusions XS07 |
| XS23 | Survival logrank/KM, adjusted/unadjusted Cox, covariates, follow-up | F-XS-006; extended result omissions F-XS-007 |
| XS24 | Noninferiority/equivalence margin/hypothesis direction | No such margin; superiority/slowing direction matches |
| XS25 | Sample160,120active40control, shared controls, simulated power/slowing | Approximately80% vs77% is precision-screened; simulation basis matches |
| XS26 | Interim40with24week opportunity,12week cadence, futility<.05 forDRR<.9 | Match; “active randomized” clarified by explicit30active10placebo |
| XS27 | No early-success stopping, final posterior.979, nominal secondary tests | Match; strict/inclusive boundary does not change actual.65 decision |
| XS28 | CAFS→SVC→survival gate, two-sided.05, closed testing and nominal inference | Sequence matches; CAFS changedanalysis XS20 |
| XS29 | Within-plan applicable primary model, endpoint, population, missingness and decision rules | Version precedence recorded; six-point/status patterns below; residual shared-baseline model/code logic delegated statistical lane |
| XS30 | Baseline copies, other exploratory displays, background simulations, administrative sources | Scope tiers applied; no omitted applicable comparison |

## Findings

### F-XS-001 — Primary mortality component rates differ between the article and eTable2

**Locations and roles:** REPORT [main PDF4, Primary Efficacy Outcome](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4) versus REPORT [results supplement PDF15, eTable2](../../../joi240158supp3_prod_1742927563.7911.pdf#page=15).

**Printed inputs:** Main Bayesian shared-parameter mortality rates shared placebo.007 and pooledactive.006 events/month. eTable2 same primary model/population prints both median and mean.010 and.009, respectively. Main explicitly cites eTable2.

**Comparison/calculation:** Shared placebo intervals [.0065,.0075] and [.0095,.0105] have gap.002, relative to.007 =28.57%. Active [.0055,.0065] and [.0085,.0095] gap.002/.006 =33.33%. Both exceed5%. No crude event-rate recomputation used.

**Focus area:** A/C. **Proposed review domain:** statistical_results. **Proposed relationship:** S_C; all relationships S_C. **Qualifying route:** Route B.

**Affected result or extracted value:** The mortality component of the primary pooled-active/shared-control disease-progression model.

**Why context does not resolve it:** Same population, time horizon, model and events/month unit; mean-versus-median cannot explain it because both eTable2 columns agree. **Supported alternatives:** An undisclosed different model run or a different primary mortality parameter; neither is labeled. **Human question:** Which monthly primary-model mortality rates apply, and what distinguishes the article's .007/.006 from eTable2's .010/.009?

### F-XS-002 — Identical SVC estimates are labeled per month in the article and 24-week change in the supplement

**Locations and roles:** REPORT [main PDF4, Secondary Efficacy Outcomes](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4) versus REPORT [supplement PDF16, eTable3A](../../../joi240158supp3_prod_1742927563.7911.pdf#page=16); matching PLAN [R-SAP PDF119–121, repeated-measures specification](../../../joi240158supp2_prod_1742927563.7711.pdf#page=119) corroborates the latter quantity, without creating a PLAN/REPORT conflict.

**Printed inputs:** Main “mean change ... over24weeks” then −9.32/−8.53 “PPN per month”; difference−.78 PPN/month, CI−4.25 to2.68; doses−7.84/−10.79. eTable3A labels all these same values “24-week Change Estimate”; contrast/CI match exactly.

**Comparison/calculation:** Numerical copies have identical half-unit intervals and gap0. The conflict concerns the quantity label: a24week change versus a monthly slope. 24weeks is168days, approximately5.52calendar months using the SAP's days×12/365.25; assigning a monthly interpretation changes the integrated24week magnitude by approximately5.52-fold. Both repeated-measures and slope models were used, and the neighboring sensitivity gives different monthly magnitudes−1.73/−1.55.

**Focus area:** C. **Proposed review domain:** report_internal_inconsistency. **Proposed relationship:** S_C; all relationships S_C. **Qualifying route:** Route B.

**Affected result or extracted value:** Key-secondary SVC mean-change/slope estimates and their units. **Why context does not resolve it:** Two model types and two time scales are explicitly present; extraction cannot safely select a time scale by treating the label as a missing unit. **Supported alternatives:** Repeated-measures24week change, or random-slope/month output with a different numerical result. **Human question:** Do −9.32/−8.53 and difference−.78 describe24week changes or monthly slopes, and which units belong to their CI?

### F-XS-003 — Survival exclusion statement does not reconcile with the displayed regimen-placebo analysis population

**Locations and roles:** REPORT [main PDF4, secondary survival paragraph](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4) versus REPORT [main PDF7, Table2 and footnotea](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=7).

**Printed inputs:** Narrative states “4 of the41 participants in the regimen placebo group and2 in the shared placebo group were excluded due to having no follow-up time”, with parenthesis naming1baselinePAV and1earlytermination. Table2 retains4/41 regimen-placebo events/denominator in every applicable row; shared control denominator162; footnote identifies only2shared-placebo exclusions.

**Comparison/calculation:** A4-person exclusion from41 implies37, rather than displayed41. Allowing printed half-units, subtraction range[36,38] versus denominator[40.5,41.5] leaves gap2.5/41 =6.10%, above5%. Event count4 appears in table as the numerator, whereas narrative makes it an exclusion count. The two named reasons account for2 shared-control exclusions, not4additional regimen exclusions.

**Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W; all relationships S_W. **Qualifying route:** Route B.

**Affected result or extracted value:** Regimen-only key-secondary PAV-free survival denominator and exclusion population. **Why context does not resolve it:** The sentence asserts exclusion; the table retains the full41-person regimen denominator and lists a distinct shared-control exclusion. **Supported alternatives:** The4is a regimen event count; alternatively an additional4-person exclusion population requires specification. **Human question:** Were four regimen-placebo participants excluded from this survival analysis, or did they experience events, and what regimen denominator applies?

### F-XS-004 — Sex appears in the survival table adjustment set but not the reported methods or regimen specification

**Locations and roles:** REPORT [main PDF3, survival methods](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=3), REPORT [main PDF7, Table2 footnoteb](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=7), REPORT [supplement PDF10 and12, Cox description](../../../joi240158supp3_prod_1742927563.7911.pdf#page=10), PLAN [R-SAP PDF121, survival](../../../joi240158supp2_prod_1742927563.7711.pdf#page=121).

**Printed inputs:** Methods list baselineage, monthssinceonset, deltaFRS, riluzole, edaravone. Table2 adds sex. Supplement describes the same primarycovariates plusage. RegimenSAP specifies age as additional covariate in adjusted survival models; baselineNfL is separately supportive.

**Comparison/calculation:** Item-wise adjustment list: age/onset/deltaFRS/riluzole/edaravone appear on both sides; sex appears only in Table2. This is categorical model-specification logic; numeric display precision does not apply.

**Focus area:** C/D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; all relationships P_R, S_W, S_C. **Qualifying route:** Route B.

**Affected result or extracted value:** Table2's adjusted pooled/dose-specific PAV-free survival HRs and intervals. **Why context does not resolve it:** Afootnote explicitly claims an additional model covariate, while prose and supplied regimen plan identify another adjustment set. **Supported alternatives:** Table2used an additional sex adjustment, or its footnote describes a different run. **Human question:** Which exact adjustment set produced Table2, and was the inclusion of sex prespecified or added?

### F-XS-005 — Reported primary CAFS test differs from the supplied revised primary CAFS analysis

**Locations and roles:** PLAN [R-SAPv3 PDF118–119](../../../joi240158supp2_prod_1742927563.7711.pdf#page=118), PLAN [earlier R-SAPv1 PDF84](../../../joi240158supp2_prod_1742927563.7711.pdf#page=84), REPORT [main PDF3 methods andPDF4 result](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=3).

**Printed inputs:** Latest regimen plan calls primaryCAFS covariate-adjusted linear comparison of ranks with onsettime, deltaFRS, baseline riluzole/edaravone; PDF119 explicitly requires covariate adjustment and labels unadjusted comparison sensitivity. Earlier v1 specifies Wilcoxon. Article reports Wilcoxonrank-sum with mean ranks143.9/140.5,P=.51; baselineNfLsensitivity P=.88 is separately reported.

**Comparison/calculation:** Required fourcovariate adjusted primary analysis is not the described Wilcoxonrank-sum. The article's result aligns with the priorplan method, while laterplan explicitly promotes adjustment. Numeric precision cannot reconcile different tests.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; all relationships P_R. **Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Primary inference for key-secondary CAFS and prespecification of P=.51. **Why context does not resolve it:** RouteA5 covers replacement/nonreporting of a planned key-secondary analysis; a nonsignificant result does not remove it. **Supported alternatives:** Report may use the earlierplan; adjusted primary result may be among unshown analyses; baselineNfL sensitivity may contain fourcovariates but is not the specified non-NfL primary result. **Classification ambiguity:** Earlier v1 and later v3 coexist; the article does not say which governs its reported CAFS. **Human question:** Which plan version governed CAFS, and where is the prespecified fourcovariate adjusted primary result?

### F-XS-006 — Planned primary key-secondary survival logrank analysis is not reported

**Locations and roles:** PLAN [R-SAPv3 PDF117 and121](../../../joi240158supp2_prod_1742927563.7711.pdf#page=121), PLAN [v1 PDF85–86](../../../joi240158supp2_prod_1742927563.7711.pdf#page=85), REPORT [main PDF3,4,7](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=7), REPORT [supplement PDF10](../../../joi240158supp3_prod_1742927563.7911.pdf#page=10).

**Printed inputs:** Both regimen versions specify primary survival KM/logrank; unadjusted Cox inference if logrank significant. Article instead describes Cox adjustment and Table2 presents adjustedHR/CI/P, including pooled.46(.12–1.49),P=.22. A KMplot is provided; no logrank statistic/P or unadjusted primary test result occurs in report materials.

**Comparison/calculation:** Primaryplanned logrank≠adjustedCox P. Full report/table/footnote search finds only adjustedCox results. Display precision is inapplicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; all relationships P_R. **Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecified primarytest for key-secondary PAV-free survival. **Why context does not resolve it:** RouteA5 includes a planned key-secondary analysis not reported, even when adjusted exploratory results are shown. **Supported alternatives:** Analysis performed but unreported, or changed to adjustedCox. **Human question:** Where is the planned pooled-active FAS logrank result, and what is its relationship to the reported adjustedCoxP=.22?

### F-XS-007 — Named planned primary/key-secondary supportive and sensitivity results are absent from the supplied report

**Locations and roles:** PLAN [R-SAP PDF116–117](../../../joi240158supp2_prod_1742927563.7711.pdf#page=116), [PDF119](../../../joi240158supp2_prod_1742927563.7711.pdf#page=119), [PDF113](../../../joi240158supp2_prod_1742927563.7711.pdf#page=113), [PDF121](../../../joi240158supp2_prod_1742927563.7711.pdf#page=121), [PDF125](../../../joi240158supp2_prod_1742927563.7711.pdf#page=125), versus REPORT [main PDF4 and7 results](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4), REPORT [supplement PDF9, sensitivity statement](../../../joi240158supp3_prod_1742927563.7911.pdf#page=9), [eTable2 PDF15](../../../joi240158supp3_prod_1742927563.7911.pdf#page=15), [eTables3A/3B PDF16–17](../../../joi240158supp3_prod_1742927563.7911.pdf#page=16).

**Printed inputs and item-wise audit:** SAP: primaryBayesian ECMsensitivity and EPPsupportive (in addition to FAS/ERO); CAFS/SVCjoint-rank with death-alone variants and multipleimputation; reference-based placeboMI ALSFRS/SVC with50imputations; PAV/death and death-alone at24weeks and laterlastregimenfollow-up. Reports give FAS/EROprimaryDRR, FAS/EROSVC, ordinaryCAFS and baselineNfLsensitivities,24week adjustedPAV/death. The supplement says prespecified sensitivities “were performed” but provides no estimates for the named ECM/EPP/MI/joint-rank variants or extended-time survival results. No per-protocol efficacy display exists.

**Comparison/calculation:** The named planned analysis→report result mapping is absent for each enumerated family. R-SAP PDF125–126 also specifies early disease (all ALSFRSitems≥2 AND SVC≥80% AND onset<24months), serumurate<5.5/≥5.5mg/dL, anybulbar/nobulbar onset, and individual/pooledclinic-site subgroup analyses for primary/secondary endpoints. Supplement PDF13 calls these prespecified; eTable4 PDF18–20 contains no result for these four subgroup families. These are planned primary/key-secondary analyses, not an expectation that every exploratory measurement be reported. No unprovided prior-master specification is assumed; all entries come from explicit supplied regimenplan. Display precision does not apply.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; all relationships P_R. **Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Robustness of the primary DRR and three key-secondary results to analysispopulation, missingness, mortality definition and follow-up time. **Why context does not resolve it:** RouteA5 always registers a planned primary/key-secondary analysis not reported; a generic statement of completed sensitivity analyses supplies no extractable result. **Supported alternatives:** Separate reports may hold these analyses; they are not supplied. Analyses may be omitted from this publication or revised. **Human question:** Where are the named planned primary/key-secondary analysis results, or which documented amendment removed them from this report's analysis set?

### F-XS-008 — Muscle-strength outcome status changes from secondary to exploratory

**Locations and roles:** PLAN [RSA3 PDF112](../../../joi240158supp1_prod_1742927563.7611.pdf#page=112), PLAN [RSA6 PDF184](../../../joi240158supp1_prod_1742927563.7611.pdf#page=184), PLAN [R-SAPv1 PDF76–77](../../../joi240158supp2_prod_1742927563.7711.pdf#page=76), PLAN [R-SAPv3 PDF109–110](../../../joi240158supp2_prod_1742927563.7711.pdf#page=109), REPORT [main PDF3 outcome list](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=3), REPORT [supplement PDF5–6](../../../joi240158supp3_prod_1742927563.7911.pdf#page=5).

**Printed inputs:** Both protocolappendices list change in isometricHHD andgrip as secondary efficacy. Both regimenSAPversions and report list HHD strength among exploratory outcomes, with CAFS/SVC/survival as three keysecondaries.

**Comparison/calculation:** Item-wise endpoint match establishes same strengthmeasure but changed status secondary→exploratory. R-SAPprecedence tells which analysishierarchy was used; it does not make the observable statuschange disappear. Precision is inapplicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; all relationships P_R, P_P. **Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecified classification and inferential status of HHD/grip results. **Why context does not resolve it:** RouteA5 expressly includes an outcome whose statuschanges. **Supported alternatives:** Intentional regimenSAPamendment with secondaryhierarchy authorization. **Classification ambiguity:** Change is present inside the PLANbundle and between protocol and REPORT; R-SAP supports the reported hierarchy. **Human question:** What amendment documents the change of muscle-strength outcomes from secondary to exploratory, and which status should evidence extraction record?

### F-XS-009 — Reported prespecified delta-FRS subgroup analysis uses a median split instead of planned three thresholds

**Locations and roles:** PLAN [R-SAPv1 PDF89](../../../joi240158supp2_prod_1742927563.7711.pdf#page=89), PLAN [R-SAPv3 PDF126](../../../joi240158supp2_prod_1742927563.7711.pdf#page=126), REPORT [supplement PDF13, prespecified subgroups](../../../joi240158supp3_prod_1742927563.7911.pdf#page=13), REPORT [eTable4 PDF20](../../../joi240158supp3_prod_1742927563.7911.pdf#page=20), REPORT [main PDF8, subgroup inference](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8).

**Printed inputs:** Both regimenplans list deltaFRS<.47,.47–<1.11,≥1.11 points/year. Supplement calls fastversusslow median split prespecified; eTable4 uses dFRS<Median/≥Median, P=.70, differences.06(−.21,.34) and−.01(−.29,.27).

**Comparison/calculation:** Three mutually exclusive prespecified thresholdgroups cannot be the two median-groups; no thresholdrounding or conversion changes three categories into two. The plan's unitlabel versus monthlydefinition is separately a plan-statistical logic issue; regardless ofunit, partition mismatch remains. Later masterSAPdoes not replace explicit regimenlist.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; all relationships P_R. **Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Claim that the displayed ALSFRS-R slow/fast-progressor subgroup result is prespecified. **Why context does not resolve it:** RouteA5 includes analysis described as prespecified that the supplied applicableplan does not contain. **Supported alternatives:** Unprovided amendment or another prespecifiedmaster-era analysis, alongside omitted regimenthresholdanalysis. **Human question:** Which applicable prospective specification defines the reported median-splitdeltaFRS analysis, and where is the planned three-category result?

### F-XS-010 — Plasma NfL analysis is called prespecified in the article and post hoc in the results supplement

**Locations and roles:** REPORT [main PDF3, NfL prespecification](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=3), REPORT [main PDF8/Figure3 plasma result](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8), REPORT [supplement PDF6](../../../joi240158supp3_prod_1742927563.7911.pdf#page=6), REPORT [supplement PDF11, assay/prespecification](../../../joi240158supp3_prod_1742927563.7911.pdf#page=11).

**Printed inputs:** Main says plasmaNfL “was prespecified” in regimen-only samples. Supplement says plasmaNfL addedlater asposthoc; originalClenePDplan was UCH-L1alone, unavailableassay prompted multiplex includingNfL, “thus it is considered post-hoc for the purposes of this manuscript.”

**Comparison/calculation:** Same reported plasmaNfL population/result, differing prospective versus posthocanalysis status. No numericprecision issue. This is a conflict in analysisstatus rather than synonymous wording or peripheral effect-estimate comparison.

**Focus area:** C. **Proposed review domain:** report_internal_inconsistency. **Proposed relationship:** S_C; all relationships S_C. **Qualifying route:** Route B.

**Affected result or extracted value:** Prespecification status of plasmaNfL−9.5%,P=.04. **Why context does not resolve it:** The supplement explicitly statesposthoc “for ... this manuscript,” while the mainassertion calls the same plasmaNfL analysisprespecified. **Supported alternatives:** Planned plasma collection versus subsequently chosenNfL assay; prespecified externalPDanalysis differs from manuscriptanalysis. **Human question:** Was the reported plasmaNfL analysis prespecified or posthoc, and how does the original UCH-L1-only plan relate to the mainassertion?

### F-XS-011 — Six-point ALSFRS outcome changes from a week24 proportion to a time-to-event death composite inside plan material

**Locations and roles:** PLAN [RSA3 PDF112](../../../joi240158supp1_prod_1742927563.7611.pdf#page=112), PLAN [RSA6 PDF184](../../../joi240158supp1_prod_1742927563.7611.pdf#page=184), PLAN [R-SAPv1 PDF78](../../../joi240158supp2_prod_1742927563.7711.pdf#page=78), PLAN [R-SAPv3 PDF111](../../../joi240158supp2_prod_1742927563.7711.pdf#page=111). REPORT [main PDF3](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=3) describes time to six-point decline but does not supply a separate quantitative result or explicit death-component definition and therefore is not an additional conflict relationship.

**Printed inputs:** Protocol: active-versus-placebo difference in proportion experiencing≥6point decline baseline–week24. SAP: firstoccurrence≥6point decline composite with death/deathequivalent, whicheverfirst, censored lastALSFRassessment throughweek24window.

**Comparison/calculation:** Item-wise: threshold6 and24weekwindow match; outcome summary proportion differs from eventtime; SAPexplicitly adds death/PAV regardless of observed6pointdecline. Protocol does not contain this composite component. R-SAPprecedence identifies operational definition without erasing the changed composite. Precision is inapplicable.

**Focus area:** D. **Proposed review domain:** plan_material. **Proposed relationship:** P_P; all relationships P_P. **Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecified identity of the six-point progression exploratory outcome referenced as prespecified in the report. **Why context does not resolve it:** RouteA5 includes a changed composite definition; death/PAV are additional qualifying events rather than an abbreviation for functionaldecline. **Supported alternatives:** Intentional SAP refinement/amendment, with time-to-event composite replacing protocol's proportion. **Human question:** What amendment specifies the time-to-event death/PAV composite in place of the week24 decline proportion, and which definition governed the reported exploratory analysis?

## Excluded observations

Only apparent issues excluded after self-screening appear here; reconciled checks are in the checklist.

| Location | Observation | Reason code |
|---|---|---|
| MainPDF4/Figure1PDF5 | Initial mapperlocator transcribed regimenplacebo3deaths; directsource rendering confirms1death, matchingnarrative | NOT_REPRODUCED |
| eTable4PDF20 versus R-SAPPDF126 | Complementary ElEscorial label “Not Definite and<18months” resolves as the counterpart of “Definite and<18months” in the paired display | TERMINOLOGY_OR_WORDING |
| eTable4PDF19 versus R-SAPPDF126 | Weight<56 combines planned<43 and43–<56 labels; no published membershipcount establishes participants<43 exist, so a changed classification is conditional | CONDITIONAL_OR_UNREPORTED |
| MainPDF1/PDF4 | Age58.4vs57.7: intervals[58.35,58.45]/[57.65,57.75],gap.60/58.4=1.03% | ROUNDING_OR_DISPLAY_PRECISION |
| MainPDF1/supplementPDF22 | Fatiguecount12vs13: half-unit intervals touchat12.5,gap0; count12with10.8% also within5% after roundingintervals | ROUNDING_OR_DISPLAY_PRECISION |
| MainPDF9/Table2PDF7 |13events versus5+9=14: copy/sumintervals overlap; no relative discrepancyabove5% after requiredhalf-unit treatment | ROUNDING_OR_DISPLAY_PRECISION |
| MainPDF4/supplementPDF15 | FunctionalCrI limits−1.176vs−1.181,−.892vs−.894,−1.153vs−1.143,−.858vs−.847: remainingrelativegaps each<5% | ROUNDING_OR_DISPLAY_PRECISION |
| MainPDF8/Figure3/eTable3BPDF17 | SerumNfL placebopercent30.8vs26.8 and pooleddifference−23.2vs−26.4; matchedexploratory numerical copies, absentabstract/key-secondary status | PERIPHERAL_COMPARISON |
| MainPDF8/supplementPDF25 | NfLsensitivityP=.05vs.051; intervals overlap; opposingcontrast signs explainedbycomparator order | ROUNDING_OR_DISPLAY_PRECISION |
| MainPDF8Figure3/supplementPDF17 | PlasmaCIendpoint−.4/−.5vs0 and exploratorydosage copies acrossdisplays; comparecrosscopies, not within-display interval/test conflict | PERIPHERAL_COMPARISON |
| MainTable1/supplementeTable1PDF14 | Descriptivebaseline mean/SD copies and pervisit contributorN differfromflow atweek24 | PERIPHERAL_COMPARISON |
| MasterProtocolPDF65/mainPDF3 | Approximately80%power versus77%: allowing80integerhalfunit and77integerhalfunit leavesgap2/80=2.5% | ROUNDING_OR_DISPLAY_PRECISION |
| LaterMasterSAPPDF9–10/mainPDF2–3 | Third-drugrandomization/covariates and28weekdefault versus regimen'stwo-drug/24week design belongtolaterRSAversions | CONTEXT_RESOLVES |
| ProtocolRSAOLEschedule/body | OLEweek2/4windows andlater52weekversusongoingduration; separateextension/explicitamendments, no primary/keysecondary decisionchange | PERIPHERAL_COMPARISON |
| MainPDF3/supplementPDF9 | “40active randomizedparticipants” immediatelyspecified30study-drug+10placebo | TERMINOLOGY_OR_WORDING |
| MainMethods/Table2 | AdjustedHRdiffersfromcrudeeventratio; modelidentifiedasadjusted/profilelikelihood | MODEL_VERSUS_CRUDE |
| MasterSAPsimulationfigures versustrial | Historical/simulatedplanvaluesnotmatchedclinicalresults; no regimenanalysisreliesonbackgroundcopy difference | PERIPHERAL_COMPARISON |
| LaterMasterSAP/suppliedpriorversions | Full earlierM-SAP1.0/MPRDRnotseparatelysupplied; omittedmodeldetailalonehasno conflictingprintedresult | CONDITIONAL_OR_UNREPORTED |
| R-SAPmodelsPDF120/122 | Equationindex/covarianceletter differences whoseintendedrandomintercept/slope meaningsareexplicit | NOTATION_OR_TYPOGRAPHY |

## Completion and limitations

Thirty matchedcomparisonfamilies complete, eleven findings, nineteen excludedobservations. Everyapplicable mappedrelationship was considered without a findinglimit. Missingprior governingMasterSAP1.0 and externalPDplan constrain definitiveplanversionattribution; exactnamedregimenstatements remain available. Reported exploratory numericalcopies are screened underperipheraltiers; their within-display arithmetic/interval-versus-test checks belongto independentnumeric/statistical lanes. No directsourceunit or assignedscientificrelationship is omitted. Findings are proposed issues for independentinclusionscreening and humanquestions; no candidateIDs or adjudications assigned.
