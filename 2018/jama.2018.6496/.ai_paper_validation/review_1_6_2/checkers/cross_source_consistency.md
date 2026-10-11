# Cross-source consistency review

Status: COMPLETE. Scope: all 49 mapped PDF pages, DOC-001 pp.1–11, DOC-002 pp.1–25, DOC-003 pp.1–13. Both complete extraction maps and the complete QUALITY_CONTROL_SCOPE.md and review contract were read. Matched abstract, Key Points, narrative, all table rows/notes, figures/captions, supplement results, protocol statistical/design clauses, and all blank-form items were reviewed. No structured result source is supplied. Sources and reusable assets were preserved. Candidate evidence below was checked using direct Poppler pdftotext -layout on the cited supplied PDFs; CPU, no new OCR/rendering or external evidence. The maps are locators, not old conclusions.

Roles: DOC-001 REPORT; DOC-002 PLAN; DOC-003 pp.1–6 REPORT, including the explicit prospective quotation in its interim-results context; DOC-003 pp.7–13 PLAN (blank prospective operational form). The original DOC-002 is used as the PLAN comparator for the interim finding. Local MN/MS/U keys refer to fresh maps.

## Findings

### F-XS-001

**Issue:** Primary difficult-airway criterion list differs between protocol and report/form.

**Compared locations and roles:** [DOC-002 p.13 §5.1, lines 427–431](../../../joi180054supp1_prod.pdf#page=13), PLAN; [DOC-001 p.2 Patient Selection](../../../jama_driver_2018_oi_180054.pdf#page=2), REPORT; [DOC-001 p.4 Figure 1 definition](../../../jama_driver_2018_oi_180054.pdf#page=4), REPORT; [DOC-003 p.9 item 12](../../../joi180054supp2_prod.pdf#page=9), PLAN. Result affected: [DOC-001 p.7 Table 3 primary row](../../../jama_driver_2018_oi_180054.pdf#page=7), REPORT.

**Printed evidence and comparison:** Protocol includes cervical immobility, obesity, large tongue, short neck, small mandible, facial OR neck trauma, airway edema, blood in airway, vomit in airway. Report/form list cervical immobilization, obesity, large tongue, short neck, small mandible, facial trauma, airway obstruction OR edema, blood/vomit (report: body fluids obscuring view). Matching common items does not supply the omitted neck-trauma criterion or establish that all obstruction without edema was eligible under the original list. Item-by-item comparison therefore leaves a changed definition of the primary subgroup. Form explicitly gives foreign body, angioedema, anaphylaxis, infection under obstruction/edema. Neck trauma is separately recognizable in form p.7 indication categories; it is not automatically synonymous with facial trauma or immobilization.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R, P_P (protocol/form criterion lists also differ). **Qualifying route:** Route B.

**Affected result or extracted value:** The 380-patient primary population and its 191/198 versus 150/182 successes, difference 14 percentage points (95% CI 8–20).

**Why context does not resolve it:** Overlapping features may make actual membership unchanged, but no supplied cross-classification or amendment establishes that neck-only trauma and obstruction-only patients were assigned identically. This affects who belongs to the primary subgroup, rather than merely a name.

**Supported alternatives:** The operational form may represent an amended definition; omitted neck trauma may have always co-occurred with another qualifying feature. Neither is established. Display-precision arithmetic is not applicable to criterion lists; no numerical discrepancy or count change is inferred.

**Human question:** Which criterion list defined the primary 380-patient analysis, and how were neck trauma without another listed feature and airway obstruction without edema handled?

### F-XS-002

**Issue:** Planned and reported randomization strata differ by the facial/neck-trauma criterion.

**Compared locations and roles:** [DOC-002 p.11 §4.1.1, lines 373–378](../../../joi180054supp1_prod.pdf#page=11), PLAN; [DOC-001 pp.2–3 Randomization and Trial Procedures, continuation p.3](../../../jama_driver_2018_oi_180054.pdf#page=3), REPORT.

**Printed evidence and comparison:** Both give 1:1 allocation and block sizes 2,4,6,8,10. Protocol first stratum is any cervical collar, gestalt obesity, OR apparent facial/neck trauma; report first stratum is obesity OR cervical immobilization, with neither in the second. Facial/neck trauma is not retained as an independent qualifying criterion. This is distinct from the primary analysis-subgroup list in F-XS-001: it changes allocation strata.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R. **Qualifying route:** Route B.

**Affected result or extracted value:** The stratified randomized design underlying the primary first-attempt-success comparison (191/198 versus 150/182).

**Why context does not resolve it:** Trauma without obesity/immobilization could be allocated under different randomization strata. The supplied report does not identify a revised allocation specification or equate all trauma with the remaining predictors.

**Supported alternatives:** An amended stratum definition or overlap of all affected patients with immobilization may explain implementation, but neither is supplied. Display precision is not applicable to this categorical design comparison.

**Human question:** Did the actual allocation schedule include apparent facial or neck trauma, and which approved specification underlies the reported randomization?

### F-XS-003

**Issue:** Planned cuff-inflation time-to-intubation is replaced by blade-removal first-attempt duration.

**Compared locations and roles:** [DOC-002 p.9 §2.2(2), lines 315–317](../../../joi180054supp1_prod.pdf#page=9) and [p.10 §3.2, lines 346–347](../../../joi180054supp1_prod.pdf#page=10), PLAN; [DOC-001 p.3 Trial Outcomes](../../../jama_driver_2018_oi_180054.pdf#page=3), [p.7 Table 3 duration rows/footnote c](../../../jama_driver_2018_oi_180054.pdf#page=7), REPORT; [DOC-003 pp.2–3 eTable 1 duration rows/footnote](../../../joi180054supp2_prod.pdf#page=3), REPORT.

**Printed evidence and comparison:** Protocol secondary 2 measures beginning of first attempt to cuff inflation when ETT is in trachea. Report measures blade insertion to blade removal, and labels those Table 3 rows planned secondary duration. They are distinct terminal events; failed first attempts have blade-removal times without successful cuff inflation at that attempt. Both report documents use the latter definition. Main abstract reports all-patient medians 38/36 seconds; difficult-subgroup medians are 39/40 seconds.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R. **Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Planned secondary time-to-intubation and reported duration medians 38/36 seconds overall, 39/40 seconds in difficult airways, their contrasts, and duration-based time-to-success analyses.

**Why context does not resolve it:** Route A category 5 applies to a changed prespecified endpoint definition and the absent planned cuff-inflation measure. Reading the printed definition identifies the reported measure but does not reconcile it with the planned endpoint.

**Supported alternatives:** A revised endpoint may have been approved; cuff inflation may often precede blade removal by little time. No supplied amendment or paired measurements establish equivalence. Numeric rounding cannot equate different terminal events; no recomputed discrepancy is asserted.

**Human question:** Was the planned cuff-inflation endpoint amended to blade-removal duration, and where is the planned measure or its documented replacement reported?

### F-XS-004

**Issue:** Hypoxemia observation window changes its terminal anchor.

**Compared locations and roles:** [DOC-002 p.9 §2.2(1)/(4), lines 304–325](../../../joi180054supp1_prod.pdf#page=9), [p.10 §3.2, lines 340–344/353–354](../../../joi180054supp1_prod.pdf#page=10), PLAN; [DOC-001 p.3 Measurements](../../../jama_driver_2018_oi_180054.pdf#page=3), [p.7 Table 3 footnote b](../../../jama_driver_2018_oi_180054.pdf#page=7), [p.9 Table 5 footnote b](../../../jama_driver_2018_oi_180054.pdf#page=9), REPORT; [DOC-003 p.3 eTable 1 hypoxemia footnote](../../../joi180054supp2_prod.pdf#page=3), REPORT.

**Printed evidence and comparison:** Thresholds agree: saturation <90%, or >10% absolute fall when starting <90%. Protocol observation ends one minute after ETT cuff inflation. Report observation ends one minute after completion of the first attempt, whose printed end is blade removal. The two terminal anchors differ, especially after an unsuccessful first attempt and subsequent rescue. This is a hypoxemia capture-window comparison, distinct from the duration measurement in F-XS-003.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R. **Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Success-without-hypoxemia composite 156/191 versus 123/177 in difficult airways and 317/371 versus 282/366 overall; hypoxemia 47/371 versus 50/364 (abstract 13%/14%).

**Why context does not resolve it:** Route A category 5 applies to a changed prespecified outcome/composite capture window. Matching the threshold does not reconcile observation periods.

**Supported alternatives:** Cuff inflation and first-attempt completion may coincide closely in successful cases; an amended window may exist. The sources do not establish this for all patients, particularly failures. Display precision cannot settle a categorical timing-anchor change.

**Human question:** Which timing anchor was used for hypoxemia ascertainment, and was the planned cuff-inflation window revised for the standalone and composite outcomes?

### F-XS-005

**Issue:** Enrollment stopping criterion differs between supplied plan and report.

**Compared locations and roles:** [DOC-002 p.19 §8.2, lines 665–674](../../../joi180054supp1_prod.pdf#page=19), PLAN; [DOC-001 p.3 Statistical Analysis](../../../jama_driver_2018_oi_180054.pdf#page=3), REPORT; [DOC-001 p.2 trial dates](../../../jama_driver_2018_oi_180054.pdf#page=2), REPORT context.

**Printed evidence and comparison:** Protocol targets 374 difficult-airway patients but directs enrollment for one calendar year OR 1000 total patients, whichever first, with IRB discussion of extension if 374 not reached. Report says difficult-airway count was monitored and trial stopped when MORE THAN 374 such patients enrolled; 380 difficult patients and 757 total were enrolled. A one-year/total-count boundary and a difficult-subgroup boundary are different planned decision rules, even if observed dates September 2016–August 2017 could coincide with the calendar boundary.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R. **Qualifying route:** Route B.

**Affected result or extracted value:** The 380-patient primary analysis and 757-patient secondary cohort, and whether final enrollment was governed by the planned boundary.

**Why context does not resolve it:** Dates alone do not identify which event triggered closure; the report explicitly attributes stopping to the difficult-airway count. No amended stopping rule is supplied.

**Supported alternatives:** Both boundaries may have been reached together; a documented amendment may have replaced the rule. Neither can be determined from the printed account. No discrepancy is claimed between rounded counts: this finding concerns the decision rule, not 374 versus 380 as a copied number.

**Human question:** Which stopping criterion governed final enrollment, and how does the reported difficult-subgroup boundary reconcile with protocol §8.2?

### F-XS-006

**Issue:** Primary-only interim plan is documented using all-patient success rates.

**Compared locations and roles:** [DOC-002 p.20 §8.4.1/8.5, lines 693–706](../../../joi180054supp1_prod.pdf#page=20) and [p.21 §8.6.2, lines 730–741](../../../joi180054supp1_prod.pdf#page=21), PLAN; [DOC-003 p.6 eAppendix 1 observed interim results](../../../joi180054supp2_prod.pdf#page=6), REPORT. The quoted protocol passage on the latter REPORT page corroborates prospective origin; it is not treated as a second PLAN document.

**Printed evidence and comparison:** Protocol primary analysis is the any-difficult-airway subset; interim is explicitly primary outcome only after 500 enrolled. Supplement reports after 507 enrolled: bougie 250/257 (97%), tube 213/250 (85%), and uses those assumptions to state no futility stopping. Printed denominators sum to ALL 507 enrolled (257+250), not a stated difficult-airway subset. No difficult-airway interim rates or separate primary-only calculation are supplied. Counts are exact, percentages rounding-compatible; finding is analysis population, not numeric percentage arithmetic.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R. **Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The prespecified primary-population futility analysis and the documented decision to continue enrollment.

**Why context does not resolve it:** Route A category 5 applies because the planned primary-only analysis is not reported and the documented calculation uses a different population. The statement linking the displayed rates to continuation creates more than an absent method detail.

**Supported alternatives:** Primary-only interim analysis may also have been performed but not displayed; unusually, all first 507 may have had a difficult feature (not established and unlike final distribution). The supplied documents do not distinguish these possibilities.

**Human question:** Was futility assessed in the difficult-airway primary population or the entire interim cohort, and what primary-population calculation supports the continuation decision?

### F-XS-007

**Issue:** Protocol primary missing-data reconstruction targets a secondary composite.

**Compared locations and roles:** [DOC-002 pp.8–9 §2.1 primary definition](../../../joi180054supp1_prod.pdf#page=9), [p.9 §2.2(1) secondary composite](../../../joi180054supp1_prod.pdf#page=9), [pp.20–21 §8.6.1, lines 719–722](../../../joi180054supp1_prod.pdf#page=21), all PLAN. [DOC-001 p.7 Table 3](../../../jama_driver_2018_oi_180054.pdf#page=7), REPORT, only identifies affected results; it does not create a separate P_R relationship.

**Printed evidence and comparison:** Primary is successful first-pass tracheal intubation. Secondary 1 requires that success AND no hypoxemia. Yet missing-data clause says FOR THE PRIMARY outcome, when both forms missing, video determines whether first-pass success WITHOUT HYPOXEMIA was achieved; if no video, exclude. The target in the recovery clause differs from the primary target and adds a component that is explicitly secondary.

**Focus area:** D. **Proposed review domain:** plan_material. **Proposed relationship type:** P_P. **All relationships:** P_P. **Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Definition/reconstruction of primary first-attempt success (191/198 versus 150/182), distinct from secondary success-without-hypoxemia (156/191 versus 123/177).

**Why context does not resolve it:** Route A category 5 applies to the internally changed outcome/composite used in a planned primary analysis step. The intended primary outcome is stated elsewhere, but that does not settle which outcome missing observations were to receive.

**Supported alternatives:** Video review may recover both components separately and retain intubation success for primary analysis; “without hypoxemia” may be unintended in this clause. No implementation statement resolves the two targets. No claim is made that any actual primary values were recovered under this clause. Display precision is not applicable.

**Human question:** Does §8.6.1 reconstruct primary success alone or success without hypoxemia, and how was this distinction implemented if primary forms were missing?

### F-XS-008

**Issue:** Planned Kaplan–Meier quartile confidence summaries for the key secondary time outcome are not supplied.

**Compared locations and roles:** [DOC-002 p.19 §8.1, lines 657–660](../../../joi180054supp1_prod.pdf#page=19), PLAN, with [p.9 §2.2(2)](../../../joi180054supp1_prod.pdf#page=9), PLAN; [DOC-001 p.4 time-to-event methods](../../../jama_driver_2018_oi_180054.pdf#page=4), [p.5 secondary results](../../../jama_driver_2018_oi_180054.pdf#page=5), [p.7 Table 3 duration rows](../../../jama_driver_2018_oi_180054.pdf#page=7), [p.8 Figure 2](../../../jama_driver_2018_oi_180054.pdf#page=8), REPORT; [DOC-003 p.4 eFigure 1](../../../joi180054supp2_prod.pdf#page=4), REPORT.

**Printed evidence and comparison:** Plan states time-to-event data will be summarized using KM estimates of the 25th, 50th, 75th percentiles WITH two-sided 95% CIs, and percentage censored. Report instead supplies KM curves, risk counts, log-rank P and Cox HR/CI, and raw first-attempt duration medians/IQR with Hodges–Lehmann contrast CIs. No KM quartile CIs or percent censored are supplied in either result document. A median with IQR is not a KM quartile with a confidence interval, and an HR CI is not a percentile CI. Duration appears in abstract and therefore is key secondary under scope.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R. **Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecified time-to-event summaries of the key secondary intubation-time result, alongside reported difficult-airway HR 1.29 (1.04–1.60) and overall HR 1.12 (.97–1.30).

**Why context does not resolve it:** Route A category 5 applies to a planned key-secondary analysis summary that is not reported; other time analyses do not provide the specified quantities. This does not request an additional preferred analysis.

**Supported alternatives:** Planned summaries may have been replaced by the displayed curve/HR strategy, or may exist outside the supplied package. No supplied amendment or percentile-CI result establishes either explanation. This missing planned summary is distinct from the terminal-event change in F-XS-003. Display precision is not applicable because the planned results are absent.

**Human question:** Were the specified KM percentile confidence intervals and censoring summaries produced for the key secondary time outcome, and where are they reported or their replacement documented?

## Checks that reconcile or remain bounded

Complete report-copy matching: primary abstract/Key Points/narrative/Table 3 counts, percentages, difference and CI align; all-patient success and duration medians and hypoxemia percentages align with abstract. Difficult and overall populations, randomized and actual-device groups, continuous IQR versus CI, time-to-success versus all-attempt medians, and model-based clustering adjustments were kept distinct. eTable 1 explicitly changes difference intervals/P values for physician clustering while retaining arm columns, so it is not an unadjusted duplicate. HR/log-rank results and PH disclosure agree across main narrative/captions and eFigure 1. Table 3 individual-feature/grade subgroups and actual-device analyses are explicitly unplanned; clustering explicitly post hoc. The protocol does not assert prespecification for them.

Plan/report primary test chi-square, two-sided .05, difficult-subgroup primary/all-patient secondary analyses, equal allocation and variable block sizes, no imputation, secondary complete-case denominators, and intervention first-attempt bougie versus tube/stylet are coherent apart from findings above. Missing waveform denominators do not establish a missing-form recovery discrepancy. Eligibility criteria were compared item by item: adult presumed age/actual age, ED orotracheal Macintosh direct/video, anatomic distortion, prisoner/arrest, pregnancy, and consent objections; no reproduced extraction-relevant conflict beyond the primary subgroup finding. Esophageal intubation and hypoxemia remain explicitly secondary in main Trial Outcomes despite Table 5 complications presentation. Safety DSMB stopping and futility-only efficacy stopping have different purposes. No noninferiority/equivalence margin is supplied or inferred; no unreported covariate adjustment is inferred. Sample-size numerical reproduction is delegated to statistical checking; all stated inputs and plan command were examined.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| [DOC-002 p.11 §4.1](../../../joi180054supp1_prod.pdf#page=11) vs [p.19 §8.2](../../../joi180054supp1_prod.pdf#page=19) and [DOC-001 p.3](../../../jama_driver_2018_oi_180054.pdf#page=3) | Aim “more than 9%” might look like a superiority margin; adjacent power specification uses 9% as the detectable alternative and analysis explicitly uses ordinary chi-square, so no separate 9% decision threshold is established. | CONTEXT_RESOLVES |
| [DOC-001 p.3 randomization](../../../jama_driver_2018_oi_180054.pdf#page=3) vs [p.9 limitations](../../../jama_driver_2018_oi_180054.pdf#page=9) | “Could not stratify randomization by difficult airway characteristics” refers to the full retrospectively defined primary subgroup; the two preattempt predictor strata are described separately. | TERMINOLOGY_OR_WORDING |
| [DOC-002 p.19](../../../joi180054supp1_prod.pdf#page=19) vs [DOC-001 p.4](../../../jama_driver_2018_oi_180054.pdf#page=4) | Stata 12.1 versus 15.1 software version does not establish a changed primary/key-secondary analysis or decision rule. | PERIPHERAL_COMPARISON |
| [DOC-002 pp.12/18](../../../joi180054supp1_prod.pdf#page=12) vs [DOC-003 p.13 form](../../../joi180054supp2_prod.pdf#page=13) | One-minute participation/no further data versus ED-wide AE observation and 5-minute/ED arrest fields are safety collection-window differences without a demonstrated change to primary/key-secondary result, analysis-population size, or planned decision rule. | PERIPHERAL_COMPARISON |
| [DOC-002 p.21](../../../joi180054supp1_prod.pdf#page=21) vs [DOC-003 p.6](../../../joi180054supp2_prod.pdf#page=6) | Interim scheduled at 500, performed after 507. This timing increment is separate from the substantive analysis-population finding and does not establish altered futility boundary. | PERIPHERAL_COMPARISON |
| [DOC-001 p.5 process text](../../../jama_driver_2018_oi_180054.pdf#page=5) vs [p.9 discussion](../../../jama_driver_2018_oi_180054.pdf#page=9) | Tube resistance 31/444 (7%) among anyone receiving bougie versus discussion “7% ... in the bougie group” is a peripheral process observation; no primary/key-secondary result is relabeled. | PERIPHERAL_COMPARISON |
| [DOC-001 p.3](../../../jama_driver_2018_oi_180054.pdf#page=3) vs [p.9 Table 5](../../../jama_driver_2018_oi_180054.pdf#page=9) | Secondary hypoxemia/esophageal endpoints presented under complications do not lose their explicitly stated secondary status. | TERMINOLOGY_OR_WORDING |
| [DOC-002 p.9 esophageal definition](../../../joi180054supp1_prod.pdf#page=9) vs [DOC-001 p.9](../../../jama_driver_2018_oi_180054.pdf#page=9) | Report does not repeat the protocol requirement for ventilation before esophageal-tube removal; absence alone supplies no changed printed definition. | CONDITIONAL_OR_UNREPORTED |

## Limitations and closure

Findings: 8. Excluded apparent observations: 8. Scientific source coverage gaps: none. No data-level reconstruction, amendment record, allocation schedule, individual timing pairs or interim primary-subgroup result is supplied; those missing facts are explicitly bounded alternatives/questions, not inferred values. Numerical table arithmetic and inferential compatibility are covered by parallel mandatory checkers; all copies and design specifications assigned here were reviewed without stopping at a finding count.
