# Mechanical evidence recheck

Runtime agent ID: 01a12bd9-0312-71a2-a567-4af3c979ae63. Stage: evidence_rechecker. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN.

Assigned and covered stable IDs: C001, C002, C003. Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely, together with the current ledger and initial inclusion screen. Every cited location, including locations retained from the duplicate ventilation finding F-ST1-002, was independently reread against the supplied PDF through newly extracted native text or a newly rendered source page. Earlier scientific decisions did not substitute for these observations. All candidates remain **Pending Human Adjudication**.

The recorded compute request is GPU_USER_REQUESTED for OCR; rendering and native text extraction are CPU operations, as explained in tooling_record.md. No OCR was necessary or performed. The plan PDFs' native glyph encoding is unusable, so their readable source-page renders govern transcription. New derivatives use the recorded fallback helper with pinned PyMuPDF 1.26.4 and are listed below. No supplied source or reusable artifact was changed.

## C001 — Planned ventilation Cox analysis replaced by a tobit mean contrast

**Candidate:** Planned ventilation Cox analysis replaced by a tobit mean contrast.

**Evidence state: reproduced.** The supplied SAP and protocol explicitly specify ventilation time-to-event Cox analysis and a cause-specific HR, whereas the supplied results supplement explicitly describes the replacement continuous-outcome tobit analysis. Main abstract, narrative and Table 2 report the mean-hour contrast. All registered transcribed values and cited pages match; the classification refinement below is not a transcription correction.

### Exact locations and matched source content

Every row is **location found: yes; printed source text/value matched: yes**. The prospective specification is the comparator; report rows are the observed implementation/result. Roles are assigned from compared content.

| Source location | Document role and content basis | Exact observed content and confirmation method |
|---|---|---|
| [Main PDF p.1, abstract](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1) | REPORT: numerical trial results | Difference in mean duration of invasive ventilation 6.8 h, 95% CI −3.0 to 16.5. Native source extraction matched the ventilation outcome and units. Its abstract reporting makes it key secondary under the scope. |
| [Main PDF p.4, Statistical Analysis](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=4) | REPORT: description of completed analyses | States that all analyses were conducted in accordance with the SAP, and points to results-supplement eMethods for secondary analysis detail. Native source extraction matched. |
| [Main PDF p.7, Table 2 ventilation row and footnote j](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7) | REPORT: treatment-effect result | Mean difference 6.8 (−3.0 to 16.5), P=.17, in hours. Footnote j defines total ICU ventilation hours, including reintubation and ventilation before trial enteral nutrition. Fresh source render confirms row alignment, decimal values and units. |
| [Protocol PDF p.21, lines 679–684](../../../joi250040supp1_prod_1753124024.37199.pdf#page=21) | PLAN: prospective secondary-analysis specification | Time-to-event secondary outcomes expressly include invasive ventilation; Cox models adjust for period/delayed start, stratify by ICU and use ICU-cluster robust standard errors; cause-specific HRs/CIs, with deaths censored. Fresh source render matches every compared specification. |
| [SAP PDF p.18, lines 416–431](../../../joi250040supp2_prod_1753124024.37799.pdf#page=18) | PLAN: prospective ventilation/ICU/hospital models | Liberation from ventilation is summarized by cumulative-incidence medians/IQRs with mortality a competing risk. Cox comparisons estimate cause-specific HRs, with period/start adjustment, ICU stratification and ICU-cluster robust standard errors. Death censoring and the 48-hour palliative-extubation censoring rule are expressly printed. Fresh render matches. |
| [SAP PDF p.28, Table 1 secondary time-to-event row](../../../joi250040supp2_prod_1753124024.37799.pdf#page=28) | PLAN: prospective analysis table | Ventilation/ICU/hospital duration: time to event, liberation or discharge alive, using Cox regression adjusted for period and delayed start, accounting for competing mortality. Fresh render confirms the ventilation row belongs to this model. |
| [Results PDF p.4, Duration of invasive ventilation](../../../joi250040supp3_prod_1753124024.38098.pdf#page=4) | REPORT: retrospective analysis description | Explicitly considers duration as a lower-bounded continuous response rather than the SAP time-to-event outcome. Tobit mixed model compares mean ventilation durations; period/delayed-start adjustment and a normal ICU random effect are supplied; effect is a difference in means with 95% CI. Native source output matches. |
| [Results PDF p.6, Duration of invasive ventilation](../../../joi250040supp3_prod_1753124024.38098.pdf#page=6) | REPORT: implemented analysis commands | Stata metobit gives the latent-response estimates by default. margins with dydx(treatment variable) and predict(ystar(0,.)) derives treatment effect on the observed outcome; estat icc estimates ICC. Native source output matches. |
| [Main PDF p.5, Secondary Outcomes, additional repeated occurrence](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5) | REPORT: repeated treatment-effect result | Independently matched 6.8 h (95% CI −3.0 to 16.5) as a difference in mean invasive ventilation duration. This corroborating repetition supplements the registered location list. |
| [SAP PDF p.6, lines 128–131, contextual active-plan statement](../../../joi250040supp2_prod_1753124024.37799.pdf#page=6) | PLAN: analysis-plan supersession | States that this SAP supersedes the previously published protocol and registry plan. Fresh source render confirms that the comparator SAP, rather than the older protocol alone, supplies the current package specification. |

**Comparator matched:** Yes. Both exact plan passages and SAP Table 1 specify the time-to-event Cox model; their ventilation rows do not instead specify tobit means. The older protocol corroborates the SAP and does not add a plan-internal inconsistency.

### Rule, reproduced comparison and inputs

**Consistency rule applicable:** Focus D; Route A, category 5, a planned key-secondary analysis replaced and not reported. A cause-specific HR for liberation and a difference in observed ventilation hours are different effect quantities. The report itself identifies this as replacement; no preferred analysis is inferred.

**Logical comparison reproduced:** Planned time-to-liberation/Cox/HR versus reported lower-bounded hours/tobit/observed-mean difference. The specified mortality/censoring construction is attached to the planned analysis. The replacement paragraph does not describe an equivalent cause-specific HR. The repeated report values agree with each other and identify what was reported.

**Display-precision interval check:** Not applicable to the categorical model/estimand replacement. The repeated 6.8, −3.0 and 16.5 values have identical half-unit intervals, hence zero gap; they are not the source of this candidate. No arithmetic conversion between a mean-hour contrast and an HR is justified by the supplied inputs.

**Necessary inputs available:** Ventilation outcome identity, key-secondary status, prospective model, planned effect measure, adjustment/stratification/clustering and censoring rules, implemented model, observed-outcome margins transformation, and printed replacement estimate/CI/P. These suffice for the registered comparison. Native search across all 10 main pages and all 34 results pages, with visual inspection of image-only results pp.23–32, found ventilation mean/descriptive results but no ventilation Cox HR. The results pp.6 Cox statements explicitly refer to ICU/hospital admission; the forest and ICEMAN image pages concern primary-outcome subgroup analyses, not ventilation-liberation HRs. The complete current source maps independently locate the same report inventory. This is a bounded observation about the supplied report files, not a claim that the analysis was never run.

**Exact missing inputs or definitions:** The planned ventilation Cox HR/CI output; any superseding ventilation-model amendment, its date and authorization; an explicit statement whether the planned analysis was performed and intentionally omitted. Individual data or an unreported HR cannot be reconstructed from the mean contrast. The replacement description does not fully specify how mortality/palliative extubation enters its continuous-outcome treatment, so equivalence to the SAP censoring estimand is not established.

### Classification confirmation and proposed refinement

**Review domain:** protocol_report, confirmed. **Primary relationship type:** P_R, confirmed. **All relationships:** P_R, S_C, proposed refinement from ledger P_R. **Compared document roles:** PLAN protocol and SAP vs REPORT main article and results supplement, confirmed by the content in the location table.

**Reason for refinement:** Main REPORT p.4 states all analyses accorded with the SAP, while the separate REPORT results supplement p.4 explicitly states this analysis used a continuous response rather than the published SAP's time-to-event outcome. These compared report assertions form an additional S_C relationship within the same issue. Primary P_R takes precedence over S_C. Plan agreement is corroboration, not P_P. Main abstract/Table 2/narrative agree numerically; no additional S_W is established. This proposes no additional candidate ID.

**Classification ambiguity:** The report openly discloses replacement, and a later amendment could explain the broad SAP-concordance statement. Such an amendment is not identified in the supplied plan map. Disclosure defines the reported analysis but does not supply the planned key-secondary HR.

### Observations, alternatives and human question

**Direct observation:** The prospective model and replacement model are explicitly printed, the change is expressly acknowledged, and the report supplies the mean-hour estimate. No ventilation HR was located in the bounded supplied report inventory above.

**Inferred explanation:** Whether a later authorized amendment, analytic practicality or another reason led to replacement cannot be inferred from this text. The absence of a located HR does not show that the analysis was never performed.

**Source-grounded alternative interpretation:** A formally revised analysis may underlie the supplement, and the report may intentionally present only the replacement. The results supplement's disclosure supports intentional replacement as a possibility. It does not supply a further prospective plan or HR output.

**Exact remaining human question:** Was the SAP ventilation Cox analysis formally replaced, under which amendment and date, and is its cause-specific HR available or intentionally unreported? How was mortality/palliative extubation handled in the reported continuous-outcome analysis?

## C002 — Printed ICU confidence interval and P value have different null-status readings

**Candidate:** Printed ICU confidence interval and P value have different null-status readings.

**Evidence state: reproduced.** Fresh source-page inspection confirms HR 0.93 (95% CI 0.88 to 1.00), P=.04 in the same Table 2 ICU row. The printed interval contains ratio null 1 while the printed P value is below .05. The scope expressly retains this category despite a possible rounded upper limit.

### Exact locations and matched source content

Every row is **location found: yes; source printed value/text matched: yes; comparator matched: yes**.

| Source location | Role by content | Source observation and comparator matching |
|---|---|---|
| [Main PDF p.1, abstract ICU-discharge result](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1) | REPORT: trial result | Cause-specific HR for time to live ICU discharge 0.93 (95% CI 0.88–1.00). Native extraction matches the outcome and limits. No P value is printed here. |
| [Main PDF p.4, primary statistical-analysis paragraph](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=4) | REPORT: completed analysis description | States P<.05 as significance threshold and two-sided statistical testing. Native output matches. Its immediate paragraph describes primary analysis; this is recorded as context rather than a separate secondary multiplicity decision. The scope's default .05 convention also suffices for the ICU printed pairing. |
| [Main PDF p.5, Secondary Outcomes](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5) | REPORT: repeated result | Identifies time to live ICU discharge, death in ICU as competing risk, cause-specific HR 0.93 (95% CI 0.88–1.00). Native output matches Table 2. |
| [Main PDF p.7, Table 2 ICU row and footnotes b/c](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7) | REPORT: effect estimate, interval and test in one display | Fresh render confirms ICU duration row HR 0.93 (0.88 to 1.00), P=.04, separate from hospital row HR 0.96/P=.15. Header/footnote b establish frequentist 95% CI except the identified Bayesian row; footnote c's Bayesian posterior quantity does not apply to this ICU row. |

### Rule, calculation, display precision and inputs

**Consistency rule applicable:** Focus B; Route A, category 1, printed confidence interval versus P-value/test null status. Confidence level is explicitly 95%, null for the HR is 1, significance threshold is .05. No fitted Wald identity or reconstructed standard error is assumed.

**Calculation reproduced:** 0.88 ≤ 0.93 ≤ 1.00, so estimate containment and endpoint order reconcile. For null status, 0.88 ≤ 1 ≤ 1.00, while .04<.05. This is the registered printed pairing.

**Display-precision interval check:** HR 0.93 allows [0.925,0.935]; lower CI 0.88 allows [0.875,0.885]; upper CI 1.00 allows [0.995,1.005]; P=.04 allows [0.035,0.045]. The P range remains entirely below .05. An underlying upper limit in [0.995,1) could exclude 1 while printing as 1.00. This is a supported alternative, not a rounding exclusion: the scope expressly exempts Route A category 1 from that exclusion. No relative discrepancy cutoff applies to this interval/test category, and no diagnostic log-HR approximation is used as proof.

**Necessary inputs available:** Same-row effect estimate/limits/P, outcome identity, frequentist 95% CI label, ratio-null definition, repeated abstract/narrative mapping and .05 comparison convention. These suffice for the printed null-status comparison.

**Exact missing inputs or definitions:** Unrounded CI endpoints and P value; numeric standard error and test statistic; precise interval and test constructions (for example which Wald/score/likelihood or reference distribution was used), including whether the interval and P arise from different procedures. Those are needed to reconcile the underlying output, not to find the printed pairing.

### Classification confirmation

**Review domain:** statistical_results, confirmed. **Primary relationship type:** S_W, confirmed. **All relationships:** S_W, confirmed. **Compared document roles:** REPORT main article Table 2 vs REPORT main article abstract and narrative, confirmed. The decisive comparator is the interval versus P within Table 2; abstract and narrative repeat its interval. All belong to one report document. No protocol or second report is a conflicting comparator, so neither P_R nor S_C is added. This concerns numerical inference, not uncertain outcome attribution, so report_internal_inconsistency is not the domain. **Classification ambiguity:** None concerning roles, relationship type or domain. Unrounded output uncertainty is an evidence limit rather than a role ambiguity.

### Observations, alternatives and human question

**Direct observation:** Exact same-row values have the printed null-status comparison above; repeated intervals agree.

**Inferred explanation:** A below-null unrounded upper endpoint could account for the printed pairing. Different interval/test procedures could also account for it. Neither mechanism is demonstrated by the supplied output, and this recheck does not assert mathematical incompatibility of every possible underlying model.

**Source-grounded alternative interpretation:** Ordinary two-decimal CI formatting permits an upper endpoint just below 1 to display as 1.00. The results methods identify cause-specific Cox regression for ICU duration, but do not print the exact numerical inferential output needed to establish that explanation.

**Exact remaining human question:** What are the unrounded ICU HR confidence limits and P value, and which exact interval and test procedures produced the printed 0.93 (0.88–1.00), P=.04 combination?

## C003 — Original primary-power correlation assumptions differ between SAP and report

**Candidate:** Original primary-power correlation assumptions differ between SAP and report.

**Evidence state: reproduced.** Fresh source renders confirm SAP lower ICC extreme 0.001 and native supplied-source text confirms main lower within-cluster/within-period correlation 0.01. Their display-precision intervals remain separated beyond the scope's relative threshold. The compared statements occur in the original one-day power rationale, before the separately marked after-completion rationale. No actual calculated power failure is claimed.

### Exact locations and matched source content

Every row is **location found: yes; source printed value/text matched: yes; comparator matched: yes**.

| Source location | Role by content | Exact confirmed inputs/context and method |
|---|---|---|
| [Main PDF p.3, Sample Size Calculation, bottom-right paragraph](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=3) | REPORT: retrospective original-power rationale | TARGET summary data, eight clusters, four periods and cluster-period size at least 60 begin the passage continued on p.4. Native source output confirms this continuity. |
| [Main PDF p.4, Sample Size Calculation continuation](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=4) | REPORT: stated power inputs | At least 60/80 per cluster-period for 80%/90% power to detect one day; within-cluster/within-period correlation 0.01–0.05, base 0.02; cluster autocorrelation 0.64–0.96, base 0.8; cluster-size CV 0.5. The subsequent sentence explicitly begins the after-completion four-cluster/two-day rationale. Native source output matches the lower bound and distinction. |
| [SAP PDF p.13, lines 301–308](../../../joi250040supp2_prod_1753124024.37799.pdf#page=13) | PLAN: sample-size specification | Shiny Cluster Randomized Trial Calculator, prior SD 11.3 days; exchangeable correlation; cluster-size CV 0.5; eight ICUs, mean 160 per period, 95% CI 80–240; ICC 0.02 with lower extreme 0.001 and upper 0.1. Fresh source render confirms especially all decimal places in the extremes. |
| [SAP PDF p.14, lines 309–321](../../../joi250040supp2_prod_1753124024.37799.pdf#page=14) | PLAN: original and post-completion sample-size rationales | 60–65 per period/cluster gives 80%, about 80 gives 90% for a one-day mean difference; 2560/eight clusters and 15% inflation to approximately 3000 are discussed. The later passage expressly begins after trial completion and describes four clusters per sequence and >80% for two days. Fresh render confirms these separate rationales. |
| [Protocol PDF p.20, lines 651–665](../../../joi250040supp1_prod_1753124024.37199.pdf#page=20) | PLAN: corroborating prospective power description | SD 11.3, CV 0.5 and ICC 0.02 with lower 0.001/upper 0.1; original 60–65/about 80 per-period rationale and later eight-ICU recruitment description. Fresh source render confirms the lower/upper bounds. Its earlier six-ICU bracket is not used to infer a numerical power discrepancy here. |

**Comparator matched:** Yes. The main .01–.05 range is introduced before its explicitly after-completion paragraph; it is not labeled solely as an input to the later two-day calculation. The SAP .001–.1 range similarly precedes the original 80%/90% one-day rationale. This matches the rationale and the shared base .02/CV .5 without silently declaring the covariance parameterizations identical.

### Rule, calculation, display precision and inputs

**Consistency rule applicable:** Focus D, Route B. B1: original primary sample-size/power inputs are in focus. B2: the supplied passages do not map exchangeable ICC/extremes to within-cluster/within-period correlation and added autocorrelation, or identify .01–.05 as a separate sensitivity subset. B3: an extractor or reader reproducing the original primary power rationale would record distinct lower correlation bounds and possibly distinct covariance specifications. This is an unresolved report/plan power-input comparison, not a calculation of actual power.

**Calculation reproduced:** Printed SAP lower .001 versus report lower .01. PLAN interval [0.0005,0.0015], REPORT interval [0.005,0.015]. Minimum gap = 0.005−0.0015 = 0.0035. Using the reported value .01 as reference, relative discrepancy = .0035/.01 = .35 > .05. If the SAP value were instead the reference, the relative gap would be 3.5; the threshold result does not depend on that choice.

**Display-precision interval check for the upper bound:** SAP .1 gives [.05,.15], report .05 gives [.045,.055]. They overlap on [.05,.055], so gap and relative discrepancy are zero. The upper bound alone is not a reproduced numeric discrepancy under the scope. Shared base .02 gives identical [.015,.025] intervals. The added autocorrelation range is context for the correlation-specification question, not a separately registered omission.

**Necessary inputs available:** Both directly printed lower and upper ranges, shared base/CV, distinct covariance terminology, original power targets, original cluster/period rationale and expressly separated later rationale. These suffice for the printed-bound comparison.

**Exact missing inputs or definitions:** A mapping between exchangeable ICC and the report's within-period correlation/cluster autocorrelation; whether .01–.05 was an additional or refined sensitivity subset; saved calculator configuration/version and selected design/covariance settings; exact power formula and alpha for the original power calculation. The SAP names a calculator but does not supply its complete saved settings. These inputs would be needed to establish which calculation generated the stated original 80%/90% power; this recheck does not assume a formula.

### Classification confirmation

**Review domain:** protocol_report, confirmed. **Primary relationship type:** P_R, confirmed. **All relationships:** P_R, confirmed. **Compared document roles:** PLAN SAP vs REPORT main article, confirmed. Corroborating protocol is PLAN by prospective sample-size content and supports the SAP lower/upper range. It does not introduce a conflicting P_P relationship. Main pp.3–4 are contiguous, not conflicting report copies; no S_W or S_C is established. **Precedence:** P_R alone is highest. **Classification ambiguity:** Report could describe refined or additional sensitivity calculations using a different covariance parameterization; no supplied statement identifies that mapping. No classification correction is proposed.

### Observations, alternatives and human question

**Direct observation:** Direct-source lower bounds differ beyond display precision, the base and CV match, covariance descriptions differ, and the original versus after-completion rationales are explicitly separated.

**Inferred explanation:** The report may summarize a refined covariance formulation or a narrower sensitivity subset inside the broader SAP range. That is plausible but not established. Neither a reduced actual power nor a changed clinical conclusion follows from the printed range comparison.

**Source-grounded alternative interpretation:** The report explicitly supplies within-period correlation and a cluster autocorrelation parameter; this could identify a more detailed/additional calculation rather than the exchangeable calculation summarized in the SAP. The absence of a mapping leaves that interpretation to human clarification; the candidate concerns which assumptions support the quoted original power.

**Exact remaining human question:** Which covariance structure, sensitivity bounds and calculator settings produced the original one-day 80%/90% power figures, and is the report's .01–.05 plus autocorrelation specification a refinement/additional calculation or a replacement of the supplied SAP assumptions?

## Classification handoff and completion

| ID | Evidence state | Review domain | Primary relationship | All relationships after recheck | Role confirmation | Proposed ledger change |
|---|---|---|---|---|---|---|
| C001 | reproduced | protocol_report | P_R | P_R, S_C | PLAN protocol/SAP vs REPORT main/results | Add S_C for main SAP-concordance assertion versus separate results-supplement explicit replacement; retain primary P_R and domain. Add corroborating repeated result on main p.5 to affected locations. |
| C002 | reproduced | statistical_results | S_W | S_W | REPORT main vs itself | Evidence state only; no classification change. |
| C003 | reproduced | protocol_report | P_R | P_R | PLAN SAP vs REPORT main; protocol corroborates PLAN side | Evidence state only; no classification change. |

Three assigned IDs covered individually; all registered exact locations found. No registered numeric transcription or page correction was necessary. The coordinator owns ledger/screening updates; neither was modified here. Remaining questions are the named missing analysis output/amendment, unrounded ICU inference output, and original-power covariance/calculator mapping. They are evidence limitations, not source-location coverage omissions or AI dispositions.

## Derivative provenance

All paths below are relative to review_1_6_2. Every derivative uses **PyMuPDF 1.26.4, CPU**. Native `--layout` uses PyMuPDF sorted reading order; it is not Poppler's geometric layout extraction. Source inputs are untouched. The exact command for each table row is the prefix below followed by the row's complete argument string:

`.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py`

| Source/page scope | Derivative | Exact command arguments |
|---|---|---|
| Main PDF pp.1–9 | preprocessing/recheck/main-1-9.txt | text jama_summers_2025_oi_250040_1753124024.36498.pdf --first 1 --last 9 .ai_paper_validation/review_1_6_2/preprocessing/recheck/main-1-9.txt --layout |
| Main PDF p.10 | preprocessing/recheck/main-10.txt | text jama_summers_2025_oi_250040_1753124024.36498.pdf --first 10 --last 10 .ai_paper_validation/review_1_6_2/preprocessing/recheck/main-10.txt --layout |
| Results PDF pp.1–21 | preprocessing/recheck/results-1-21.txt | text joi250040supp3_prod_1753124024.38098.pdf --first 1 --last 21 .ai_paper_validation/review_1_6_2/preprocessing/recheck/results-1-21.txt --layout |
| Results PDF pp.22–34 | preprocessing/recheck/results-22-34.txt | text joi250040supp3_prod_1753124024.38098.pdf --first 22 --last 34 .ai_paper_validation/review_1_6_2/preprocessing/recheck/results-22-34.txt --layout |
| SAP PDF pp.13–18, encoded unusable native text | preprocessing/recheck/sap-13-18.txt | text joi250040supp2_prod_1753124024.37799.pdf --first 13 --last 18 .ai_paper_validation/review_1_6_2/preprocessing/recheck/sap-13-18.txt --layout |
| SAP PDF p.28, encoded unusable native text | preprocessing/recheck/sap-28.txt | text joi250040supp2_prod_1753124024.37799.pdf --first 28 --last 28 .ai_paper_validation/review_1_6_2/preprocessing/recheck/sap-28.txt --layout |
| Protocol PDF pp.20–21, encoded unusable native text | preprocessing/recheck/protocol-20-21.txt | text joi250040supp1_prod_1753124024.37199.pdf --first 20 --last 21 .ai_paper_validation/review_1_6_2/preprocessing/recheck/protocol-20-21.txt --layout |
| Main PDF p.7, 200 dpi | preprocessing/recheck/main-p7.png | render jama_summers_2025_oi_250040_1753124024.36498.pdf --page 7 .ai_paper_validation/review_1_6_2/preprocessing/recheck/main-p7.png |
| SAP PDF p.6, 200 dpi | preprocessing/recheck/sap-p6.png | render joi250040supp2_prod_1753124024.37799.pdf --page 6 .ai_paper_validation/review_1_6_2/preprocessing/recheck/sap-p6.png |
| SAP PDF p.13, 200 dpi | preprocessing/recheck/sap-p13.png | render joi250040supp2_prod_1753124024.37799.pdf --page 13 .ai_paper_validation/review_1_6_2/preprocessing/recheck/sap-p13.png |
| SAP PDF p.14, 200 dpi | preprocessing/recheck/sap-p14.png | render joi250040supp2_prod_1753124024.37799.pdf --page 14 .ai_paper_validation/review_1_6_2/preprocessing/recheck/sap-p14.png |
| SAP PDF p.18, 200 dpi | preprocessing/recheck/sap-p18.png | render joi250040supp2_prod_1753124024.37799.pdf --page 18 .ai_paper_validation/review_1_6_2/preprocessing/recheck/sap-p18.png |
| SAP PDF p.28, 200 dpi | preprocessing/recheck/sap-p28.png | render joi250040supp2_prod_1753124024.37799.pdf --page 28 .ai_paper_validation/review_1_6_2/preprocessing/recheck/sap-p28.png |
| Protocol PDF p.20, 200 dpi | preprocessing/recheck/protocol-p20.png | render joi250040supp1_prod_1753124024.37199.pdf --page 20 .ai_paper_validation/review_1_6_2/preprocessing/recheck/protocol-p20.png |
| Protocol PDF p.21, 200 dpi | preprocessing/recheck/protocol-p21.png | render joi250040supp1_prod_1753124024.37199.pdf --page 21 .ai_paper_validation/review_1_6_2/preprocessing/recheck/protocol-p21.png |
| Results PDF p.23, 120 dpi | preprocessing/recheck/results-p23.png | render joi250040supp3_prod_1753124024.38098.pdf --page 23 .ai_paper_validation/review_1_6_2/preprocessing/recheck/results-p23.png --dpi 120 |
| Results PDF p.24, 120 dpi | preprocessing/recheck/results-p24.png | render joi250040supp3_prod_1753124024.38098.pdf --page 24 .ai_paper_validation/review_1_6_2/preprocessing/recheck/results-p24.png --dpi 120 |
| Results PDF p.25, 120 dpi | preprocessing/recheck/results-p25.png | render joi250040supp3_prod_1753124024.38098.pdf --page 25 .ai_paper_validation/review_1_6_2/preprocessing/recheck/results-p25.png --dpi 120 |
| Results PDF p.26, 120 dpi | preprocessing/recheck/results-p26.png | render joi250040supp3_prod_1753124024.38098.pdf --page 26 .ai_paper_validation/review_1_6_2/preprocessing/recheck/results-p26.png --dpi 120 |
| Results PDF p.27, 120 dpi | preprocessing/recheck/results-p27.png | render joi250040supp3_prod_1753124024.38098.pdf --page 27 .ai_paper_validation/review_1_6_2/preprocessing/recheck/results-p27.png --dpi 120 |
| Results PDF p.28, 120 dpi | preprocessing/recheck/results-p28.png | render joi250040supp3_prod_1753124024.38098.pdf --page 28 .ai_paper_validation/review_1_6_2/preprocessing/recheck/results-p28.png --dpi 120 |
| Results PDF p.29, 120 dpi | preprocessing/recheck/results-p29.png | render joi250040supp3_prod_1753124024.38098.pdf --page 29 .ai_paper_validation/review_1_6_2/preprocessing/recheck/results-p29.png --dpi 120 |
| Results PDF p.30, 120 dpi | preprocessing/recheck/results-p30.png | render joi250040supp3_prod_1753124024.38098.pdf --page 30 .ai_paper_validation/review_1_6_2/preprocessing/recheck/results-p30.png --dpi 120 |
| Results PDF p.31, 120 dpi | preprocessing/recheck/results-p31.png | render joi250040supp3_prod_1753124024.38098.pdf --page 31 .ai_paper_validation/review_1_6_2/preprocessing/recheck/results-p31.png --dpi 120 |
| Results PDF p.32, 120 dpi | preprocessing/recheck/results-p32.png | render joi250040supp3_prod_1753124024.38098.pdf --page 32 .ai_paper_validation/review_1_6_2/preprocessing/recheck/results-p32.png --dpi 120 |

Twenty-five new derivatives: seven native text files and eighteen source-page renders. Reusable OCR/text locations in the current source maps and screen served as locators only. Reusable image locators recorded there include review_1_5_1/preprocessing/protocol_images/page-020.png, page-021.png; sap_images/page-006.png, page-013.png, page-014.png, page-018.png, page-028.png; and main-001/page-007.png. These are existing curator-inventoried assets, not new derivative outputs and not final transcription authority in this recheck. Each decisive image was freshly rendered from its exact supplied PDF. The final inventory/hash and tool-environment removal remain coordinator responsibilities.
