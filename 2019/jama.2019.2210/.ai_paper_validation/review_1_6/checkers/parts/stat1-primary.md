# Statistical pass 1 — primary scope

- Runtime UUID: 01a12869-5568-7b03-ad14-728b9a27f354.
- Model/effort: gpt-6.1-sol/high; fresh named qc16 statistical agent; current provider retained.
- Exact scope: DOC-001 REPORT pp.1–9; DOC-002 PLAN pp.1–45; DOC-003 REPORT pp.1–6; DOC-004 REPORT p.1 (no applicable inference). DOC-003 REPORT pp.7–41 separately assigned to fresh high agent and excluded from this primary output.
- Primary relationship IDs: S001–S082, each PASS_1_COMPLETE / PASS_2_PENDING in statistics/relationship_inventory.md. Coordinator appends subgroup shard beginning S101; IDs are stable and must not be renumbered.
- Primary candidates: four independent checker-local observations ST1-A through ST1-D, no assigned C IDs, all Pending Human Adjudication.
- Scientific coverage gaps in assigned units: zero. Missing inferential definitions recorded by relationship, not treated as coverage gaps or candidate evidence by themselves.

## Inputs and method

Completely read QUALITY_CONTROL_SCOPE.md, PERFORMANCE_PROFILE.md, workflow_1_6/review_contract.md, workflow_1_6/report_spec.md and workflow_1_6/settings.toml. Read current mapper canonicals, full PLAN page transcriptions and DOC-003pp.1–6 transcriptions; source-linked main definition locators pp.3/4/6 and complete main quantitative bundles M001–M134. Page and bundle coverage used current source map only. No old candidate/queue/report/classification or external literature input. The initial reading of support results map includes pp.7–41 locators, but inferential checking/registration for that disjoint scope belongs to the separate subgroup specialist.

Tooling: tooling_record.md says direct PDF tools available, fallback NOT_NEEDED. Primary text derivative created using direct `pdftotext -f 7 -l 7 -layout jama_urashima_2019_oi_190023.pdf .ai_paper_validation/review_1_6/preprocessing/stat1-main-p7.txt` (Poppler26.01.0, version directly probed). Existing fresh support PLAN derivatives are current Poppler26.01.0. Fresh direct `pdftoppm -f 7 -l 7 -r 130 -singlefile -png jama_urashima_2019_oi_190023.pdf .ai_paper_validation/review_1_6/preprocessing/stat1-main-p7` and analogous PLAN page23 command created stat1-main-p7.png and stat1-plan-p23.png, both visually inspected. These direct page renders confirm Table2 direction, Figure3C risk rows/caption and absent inequality on PLANp.23; designated rechecker still independently confirms every cited location. No OCR, GPU, Python helper, new environment, source edit or reused-asset edit.

All available main and support-table intervals contain their point estimates, have ordered positive endpoints, and agree qualitatively with null/significance narrative. Repeated same-model values match at printed precision. The package supplies Cox/95%CI/two-sided significance, but lacks precise coefficient test/CI construction/variance/covariance; exact P-versus-CI reproduction is therefore unavailable. No conventional Wald test is silently imposed. In particular eTable1 supplementation-adjusted mean20–<30 relapse/death AHR.61 [.37,1.01],P=.05 is not a standalone inconsistency: source significance is strict P<.05, rounded .05 is a boundary, and unrounded/test construction unavailable.

PLAN sample-size log matches report planning inputs, allocation and total arithmetic. Diagnostic only: ln(.75)/ln(.62)≈.6018 agrees printed planning hazard ratio; this does not establish an observed HR or independently reproduce Freedman event/sample-size rounding. Printed120events/400patients is not contradicted by crude expected120.8events because withdrawal/method/rounding implementation is not fully supplied. No replacement test or correction prescribed.

Biomarker medians/IQRs and rounded change-ratio medians cannot reproduce Wilcoxon/Mann–Whitney P values. Main all-patient and baseline-subgroup serum medians are distinct populations. Imputation results repeat complete-case values at printed precision but MI model/pooling differences mean equal rounded outputs alone are not evidence of a contradiction. Unreported PH/stage-adjusted numeric results and unevaluated high-baseline subgroup remain explicit records.

## ST1-A — Table2 effect-direction footnote conflicts with adverse-outcome comparisons

**Candidate statement:** Main Table2 says HR values greater than1 indicate a decreased probability of the outcome; the table's treatment comparison and main adverse-outcome narrative use HR<1 as the favorable direction for vitaminD versus placebo.

**Category:** Measure, label, or scale inconsistency.

**Compared locations and roles:** REPORT DOC-001 p.7 Table2 footnotea versus REPORT DOC-001 pp.3/6 treatment/competing-risk definitions and lower-relapse interpretation; both within one REPORT document. Corroborating Figure3pp.4/7 has lower relapse/death HR.46 with higher RFS85%/71%, but this is not a conflicting PLAN role.

**Exact source locations:** `jama_urashima_2019_oi_190023.pdf#page=7`, Table2 footnotea and all nine effect rows; `jama_urashima_2019_oi_190023.pdf#page=6`, first right-column competing-risk paragraph; `jama_urashima_2019_oi_190023.pdf#page=3`, Statistical Analysis.

**Printed inputs:** Footnote: “Hazard ratio (HR) values greater than 1 indicate that vitamin D supplementation was associated with a decreased probability of the outcome.” Middle-baseline relapse subdistributionHR.44[.21,.89],P=.02; body p.6 says cumulative relapse incidence significantly lower in vitaminD than placebo. Table2 adverse endpoints are relapse, cancer-specific death, noncancer death. Other ratios include1.18/1.09/1.45/1.11 and .75/.78/.70/.39 with the same common direction label.

**Reproducible rule:** Preserve vitaminD/placebo comparison. A ratio<1 is the lower numerator hazard/subdistribution hazard. Printed p.6 interpretation of .44 explicitly establishes vitaminD as lower adverse-outcome direction. The common footnote asserts the opposite direction for greater-than1. Compare direction labels independently of confidence interval/P significance; do not claim hazard ratio directly equals cumulative event probability ratio.

**Calculation/logical comparison:** .44<1 accompanies “lower” relapse incidence; common footnote attaches “decreased probability” toHR>1. Reversing a common reference could reconcile a footnote in isolation but would conflict with source's treatment direction and the p.6 interpretation. Exact test reconstruction is unnecessary for the printed sign-label comparison.

**Direct observation versus diagnostic:** Printed footnote and .44/lower-incidence interpretation are direct transcription. Inferring a typographic inversion is a possible explanation only, not a correction or adjudication.

**Alternative source-grounded interpretation:** Footnote might have intended reciprocal comparison or a favorable survival endpoint; table actually names adverse outcomes and body explicitly compares vitaminD against placebo. No supplied footnote-specific reverse reference is found. HR/probability wording also compresses distinct measures; candidate is framed primarily around direction.

**Human question:** Which comparison/reference and direction was intended by Table2footnotea, and should that direction statement agree with the .44 vitaminD-versus-placebo relapse interpretation? Check original model coding before making a correction.

**Relationship IDs:** S003,S010,S011,S013,S014,S015,S017,S018,S019. Pending Human Adjudication.

## ST1-B — Figure3C printed risk rows conflict with caption absence claim

**Candidate statement:** Figure3caption says panelC numbers at risk are not given because of weighting, while panelC displays two numeric risk sequences.

**Category:** Numeric or arithmetic inconsistency.

**Compared locations and roles:** REPORT DOC-001 p.7 Figure3C risk rows versus REPORT DOC-001 p.7 Figure3caption; same REPORT document. Main model definitions p.3 corroborate standard baseline-subgroup Cox comparison and do not supply weighting details.

**Exact source locations:** `jama_urashima_2019_oi_190023.pdf#page=7`, panelC beneath “Death, baseline25(OH)Dlevel20–40ng/mL”; caption sentence on left below panels.

**Printed inputs:** PanelC Placebo90,88,70,51,34,22,11 and VitaminD142,139,115,88,61,41,20 at years0–6. Caption: “Numbers at risk for panel C are not given because of weighting.” PanelC HR.60[.28,1.30],P=.20.

**Reproducible rule:** Presence of labeled numeric risk rows is directly incompatible with a statement that those panel-specific numbers are not given. Do not reconstruct or challenge numerical weighting without supplied weighting specification.

**Calculation/logical comparison:** PanelC contains14printed integers grouped in two7-value sequences; caption asserts absence. No test statistic, survival conversion or approximate curve reading is required.

**Direct observation versus diagnostic:** Numeric presence and caption statement are direct printed facts. A carried-over caption or intended different panel is a possible explanation only.

**Alternative source-grounded interpretation:** Caption may refer to a different analysis/panel or to weighted effective counts, while rows are unweighted raw subjects; it says panelC numbers are “not given,” and no distinction between raw and weighted rows is explained. Package does not supply weighting method.

**Human question:** Does the caption's panelC sentence refer to another panel or to a different type of at-risk quantity, and what is the intended status of the14printed risk values? Confirm panel identification and original plot output.

**Relationship IDs:** S007; numeric M114/M116 relationships. Pending Human Adjudication.

## ST1-C — PLAN relapse-free survival AND/OR censor definitions disagree

**Candidate statement:** PLAN endpoint sections censor patients who remain relapse-free and alive, whereas reporting sections censor patients who are relapse-free or alive. These logical rules differ for an alive patient who has relapsed and for a relapse-free patient who has died.

**Category:** Measure, label, or scale inconsistency.

**Compared locations and roles:** PLAN DOC-002 p.9 primary outcome versus PLAN DOC-002 p.13 reporting/censor; independently repeated final PLAN DOC-002 p.25 primary outcome versus PLAN DOC-002 p.29 reporting/censor. The bound initial/final plan bundle remains PLAN throughout; REPORT earliest-event definition is corroboration, not a conflicting role.

**Exact source locations:** `joi190023supp1_prod.pdf#page=9`, OutcomeMeasures/Primaryoutcome; `joi190023supp1_prod.pdf#page=13`,7cCensor; `joi190023supp1_prod.pdf#page=25`,OutcomeMeasures/Primaryoutcome; `joi190023supp1_prod.pdf#page=29`,7cCensor.

**Printed inputs:** Endpoint paragraphs: RFS elapsed time from supplementation to earliest relapse or death of any cause; “Participants who do not relapse and remain alive on the day the trial ends are censored.” Reporting paragraphs: “Participants are censored in terms of RFS if they are relapse-free or alive at the end of the trial.”

**Reproducible rule:** For R=relapse-free, A=alive, R AND A and R OR A differ whenever R≠A. Earliest relapse-or-death endpoint requires no event for end-of-trial censor, hence R AND A. The printed OR category includes event-positive patients under the same supplied endpoint definition.

**Calculation:** R=false,A=true: AND=false,OR=true; R=true,A=false: AND=false,OR=true. R=A=true bothtrue; R=A=false bothfalse. This is a logical label/definition mismatch, not an estimate recalculation.

**Direct observation versus diagnostic:** Exact AND/OR wording and earliest-event definition directly observed in current fresh PopplerPLAN page transcription. Implemented event/censor records are absent; no claim trial estimates used OR.

**Alternative source-grounded interpretation:** “or” may be ordinary editorial shorthand for the intended conjunction or copied mistranslation. Endpoint definition itself supplies a coherent intended rule. Initial/final repetition means a version change does not reconcile the two statements within each version.

**Human question:** Which PLAN censor condition was intended, and do the operational definitions/model records confirm censoring only participants both alive and relapse-free? Resolve wording without presuming an implemented analytic error.

**Relationship IDs:** S049. Pending Human Adjudication.

## ST1-D — PLAN high-baseline subgroup boundary label is incomplete

**Candidate statement:** Final PLAN StudyDesign p.23 prints high “(40ng/mL),” while final PLAN SubgroupAnalyses p.31 defines high as “>40ng/mL.” The literal p.23 label is not a disjoint counterpart to middle≥20to≤40.

**Category:** Measure, label, or scale inconsistency.

**Compared locations and roles:** PLAN DOC-002 p.23 final StudyDesign/SpecificAim1 versus PLAN DOC-002 p.31 final SubgroupAnalyses. REPORT baseline cutoffs corroborate p.31's>40 but are not a conflicting REPORT comparison.

**Exact source locations:** `joi190023supp1_prod.pdf#page=23`, lastSpecificAim1sentence; `joi190023supp1_prod.pdf#page=31`,6Subgroupanalyses(i).

**Printed inputs:** p.23 low(<20ng/mL),middle(≥20to≤40ng/mL),high(40ng/mL); p.31 low<20,middle≥20to≤40,high>40. Source transcription retains absent inequality rather than normalizing it.

**Reproducible rule:** Three baseline category definitions should match across occurrences. Literal high=40 overlaps stated middle-inclusive40 and differs from stated high>40. This is an observable cutoff-label mismatch; no participant records are required to identify the missing definition.

**Calculation:** Atx=40ng/mL,p.23middle includesx and literalhigh(40)also namesx; p.31middle includesx whilehigh>40excludesx. Atx=41,p.31highincludesx whileliteral40labeldoesnot define its inclusion.

**Direct observation versus diagnostic:** Direct current page transcription and fresh visually inspected source render both lack “>” in p.23. Independent designated recheck remains required. Missing-symbol editorial explanation is diagnostic, not a prescribed correction.

**Alternative source-grounded interpretation:** “high(40)” may mean “above a40threshold” in prose; p.31andREPORT definitions support that intent. This interpretation resolves intended category but leaves the printed label incomplete.

**Human question:** Does direct page23 inspection confirm absence of an inequality symbol, and is the intended high category strictly>40ng/mL as stated p.31? Determine wording and preserve reported subgroup analyses rather than assume a changed classification.

**Relationship IDs:** S051. Pending Human Adjudication.

## Exclusions and handoff

No candidate assigned solely for missing inferential definitions, unreported adjusted results, qualitative background significance, identical rounded MI/complete-case outputs, changing statistical significance under adjustment, equality of rounded serum/calcium medians, mean-group treatment imbalance, planned-versus-actual accrual totals, or disclosed posthoc competing-risk analysis. No display-zero P is present in this primary scope; coherent display zeros encountered later must be DISPLAY_ZERO_NOT_CANDIDATE.

Four observation records are independent consistency rules and should be merged with other lanes only when same printed values, comparator and rule match. Complete evidence is in this checker and relationship inventory. All C IDs, document-role relationship classification, evidence states and suggested disposition are coordinator/rechecker tasks. Mandatory pass2 must use a different newly spawned gpt-6.1-sol/high agent, read the complete merged inventory/ledger/recheck, and update every S record to PASS_2_COMPLETE.
