# Mechanical evidence recheck — Workflow 1.6.1

Scope: every assigned stable ID in the current candidate ledger, namely C001, including the complete location union retained from F-XS-001, F-ST1-001 and F-ST1-101. This is a fresh evidence recheck, not human adjudication. QUALITY_CONTROL_SCOPE.md and the complete 1.6.1 review contract were read before rechecking. Source files and reusable artifacts were preserved. No external evidence, raw participant data, assumed model parameters or preferred analysis was used.

## C001 — Composite primary endpoint uses different patient and care-opportunity weighting definitions

**Evidence state:** reproduced

**Determining recheck fact:** The exact source statements specify patient-specific fractions calculated and averaged in the main REPORT, and a ratio of total fulfilled to total eligible interventions in the PLAN and the results REPORT supplement. The supplement expressly identifies its endpoint definition with the randomized phase. Independently summing all nine exact Table 2 numerator/denominator pairs gives pooled percentages outside the displayed composite-mean rounding intervals. No registered source transcription or location needed amendment.

### Location found and source value/text matched

Every listed location was found in a fresh, targeted native/layout extraction from the supplied PDF. The key definition locations and every Table 2 count were additionally inspected visually in direct-source page renders. PDF page numbers below are file pages; main article journal pages 245–249 and 251 correspond to PDF pages 1–5 and 7. Each role was confirmed from the compared content.

| Exact supplied-source location | Location found | Source value/text matched | Role confirmed by content | Function in this candidate |
|---|---|---|---|---|
| [Main article PDF p.1, abstract Results](../../../jama_wang_2018_oi_180070.pdf#page=1) | Yes | Composite 88.2% intervention versus 84.8% control; absolute difference 3.54%, 95% CI 0.68% to 6.40%, P=.02. | REPORT: completed randomized-trial results. | Affected result occurrence; values agree with the detailed Results. The abstract does not itself identify the difference as adjusted; that specification is supplied by Methods, detailed Results and Table 2. |
| [Main article PDF p.2, Key Points](../../../jama_wang_2018_oi_180070.pdf#page=2) | Yes | Composite adherence 88.2% versus 84.8% and statistically significant difference; all-or-none contrast described separately. | REPORT: summary of completed trial findings. | Affected result occurrence, not a separately conflicting value. |
| [Main article PDF p.3, Outcomes, final primary-outcome paragraph](../../../jama_wang_2018_oi_180070.pdf#page=3) | Yes | Fulfilled eligible performance measures divided by measures for which a given patient was eligible; the composite was calculated for each patient and then averaged. Nine measures and co-primary outcome status are explicitly stated in the same Outcomes section. | REPORT: describes the endpoint used in the completed trial. | Main definition being compared with PLAN p.16 and results supplement p.2. |
| [Main article PDF p.4, Data Analysis](../../../jama_wang_2018_oi_180070.pdf#page=4) | Yes | Intention-to-treat analysis; comparative absolute differences adjusted for patient/hospital characteristics; GEE accounts for within-hospital correlation. Each eligible care opportunity is a binary met/not-met observation for the composite odds analysis, with effects expressed as population-average odds ratios. The illustrative five-of-seven example is present. | REPORT: describes analyses of completed trial data. | Corroborating model context. Opportunity-level OR analysis is distinct from the patient-average descriptive definition and does not supply another conflict. |
| [Main article PDF p.5, primary adherence Results](../../../jama_wang_2018_oi_180070.pdf#page=5) | Yes | 88.2% versus 84.8%; absolute difference 3.54%, CI 0.68% to 6.40%, P=.02; adjusted ORPA 1.39, CI 1.12 to 1.72, P=.003; ICC .02. The paragraph refers to adjustment for baseline patient/hospital characteristics. | REPORT: primary randomized adherence findings. | Affected result occurrence. The phrase about adjustment does not by itself change Table 2's explicit mean(SD) label or p.3's aggregation rule. |
| [Main article PDF p.7, Table 2 composite row, all nine individual rows and footnote a](../../../jama_wang_2018_oi_180070.pdf#page=7) | Yes | Composite mean(SD) 88.2(15.1) versus 84.8(18.2); difference 3.5, CI 0.7–6.4, P=.02; ORPA 1.39, CI 1.12–1.72, P=.003; nine integer pairs reproduced below. Footnote a identifies adjusted inferential columns. | REPORT: observed adherence summaries and modeled randomized-trial comparisons. | Printed descriptive comparator, exact pooled-calculation inputs and adjustment context. Individual row effects are not separate instances of the candidate. |
| [Protocol PDF p.16, printed lines 216–220](../../../joi180070supp1_prod.pdf#page=16) | Yes | Composite defined as total interventions performed among eligible patients divided by total possible interventions among eligible patients. The all-or-none definition follows separately. | PLAN: prospective protocol endpoint specification in the dated plan. | Conflicting planned primary composite definition. |
| [Protocol PDF p.18, printed lines 266–274](../../../joi180070supp1_prod.pdf#page=18) | Yes | GEE accounting for within-hospital correlation; qualitative variables as population-average odds ratios and quantitative variables as mean differences; composite odds of fulfilling eligible opportunities, with each care opportunity contributing an observation. | PLAN: prospective statistical analysis plan. | Corroborating opportunity-model context, not another conflict. |
| [Protocol PDF p.19, printed lines 275–279](../../../joi180070supp1_prod.pdf#page=19) | Yes | Binary outcome 1 for measure met and 0 for not met; five eligible opportunities with three fulfilled contribute five observations, three ones and two zeros. | PLAN: continuation of prospective analysis specification. | Corroborating opportunity-model context, not another conflict. |
| [Results supplement PDF p.2, eAppendix endpoint-definition paragraph](../../../joi180070supp2_prod.pdf#page=2) | Yes | Baseline survey says it used the same endpoint definition as the randomized phase, immediately followed by total performed interventions among eligible patients divided by total possible interventions among eligible patients. Baseline composite 80.2% versus 79.5% follows separately. | REPORT: description and results of the completed baseline survey, including its assertion about the randomized endpoint; not a prospective plan. | Conflicting REPORT definition expressly attributed to the randomized endpoint. Baseline percentages are context and are not compared with randomized percentages. |

**Comparator printed value/text matched:** Yes. PLAN p.16 and results REPORT supplement p.2 both state the total-interventions ratio, while main REPORT p.3 explicitly states patient averaging. Main p.7 prints the mean(SD) comparator values and all nine inputs needed to calculate the total-interventions ratio. Main pp.1,2,5 repeat the same percentages; those repetitions do not introduce a separate within-report discrepancy. Main p.4 and PLAN pp.18–19 match each other in the separate opportunity-based odds description.

### Consistency rule applicable and calculation reproduced

**Consistency rule applicable:** Yes, for matching the planned and reported primary endpoint definition and the supplement's expressly shared randomized-phase definition. This concerns endpoint aggregation/weighting, not whether adjusted estimates equal crude ratios.

Let a_i be the fulfilled eligible opportunities and b_i the eligible opportunities for patient i, with b_i>0 for the patient fractions being summarized. The explicit main-report descriptive rule is U=(1/n)Σ(a_i/b_i). A literal implementation of the PLAN/supplement total-interventions rule is W=Σa_i/Σb_i=Σ[(b_i/Σb_j)(a_i/b_i)]. U weights patient fractions equally; W weights them in proportion to eligibility. The supplied reports do not establish that the weights are constant or disclose a reconciliation of these definitions. Different rules need not always yield different numerical values; here the printed count sums provide an additional numerical check of the pooled rule.

All entries below were read directly from the exact Table 2 source page and visually matched to its column headers and rows. Repeated patients across measures are intended in this sum: the objects being counted are care opportunities, not unique patients.

| Table 2 measure | Intervention fulfilled/eligible | Control fulfilled/eligible |
|---|---|---|
| Intravenous rtPA | 46/212 | 23/204 |
| Early antithrombotics | 2307/2353 | 2253/2330 |
| Dysphagia screening | 2255/2328 | 2040/2139 |
| DVT prophylaxis | 178/645 | 66/592 |
| Discharge antithrombotics | 2272/2324 | 2141/2305 |
| Anticoagulation for atrial fibrillation | 63/155 | 39/137 |
| Lipid-lowering | 1415/1481 | 1439/1547 |
| Antihypertensive medication | 1510/1838 | 1372/1771 |
| Antidiabetic medication | 653/728 | 557/663 |
| Independently reproduced sums | 10699/12064 | 9930/11688 |

Calculation reproduced with shell awk arithmetic:

- Intervention: 100×10699/12064=88.6853448276%, which displays as 88.7% to one decimal.
- Control: 100×9930/11688=84.9589322382%, which displays as 85.0% to one decimal.
- Pooled descriptive contrast: 3.7264125894 percentage points. This is a diagnostic arithmetic consequence of the total-interventions definition, not an alternative adjusted trial estimate.

**Display-precision interval check:** Reproduced. Reported mean 88.2% allows [88.15%,88.25%) and mean 84.8% allows [84.75%,84.85%) under half-unit rounding at one decimal. The pooled calculations exceed even the upper bounds by 0.4353448276 and 0.1089322382 percentage points, respectively. Endpoint tie conventions cannot bridge either gap. Printed fulfilled/eligible entries are exact integer event and eligibility counts, not rounded percentages; allowing a half-unit display interval around each count still leaves that printed integer as the only possible integer count. No permissible combination changes the pooled totals. The displayed SDs do not widen the rounding interval of the displayed mean.

For an additional deliberately conservative display check, allow every one of the nine printed numerator counts and every one of the nine denominator counts to vary continuously by ±0.5, temporarily disregarding their integer-count meaning. This expands each arm's numerator sum and denominator sum by ±4.5. The minimum percentage uses the smallest numerator and largest denominator; the maximum uses the largest numerator and smallest denominator. Independent awk calculation gives intervention [100×10694.5/12068.5,100×10703.5/12059.5]=[88.6149894353%,88.7557527261%] and control [100×9925.5/11692.5,100×9934.5/11683.5]=[84.8877485568%,85.0301707536%]. Even these conservative lower bounds exceed the corresponding reported-mean upper bounds by 0.3649894353 and 0.0377485568 percentage points. Thus the comparison remains nonoverlapping when a half-unit allowance is propagated through every displayed count input, as well as under exact integer treatment.

The separately reported adjusted difference 3.54 and its CI 0.68–6.40 are compatible with Table 2's one-decimal 3.5 and 0.7–6.4: their respective half-unit intervals overlap. The ORPA, CI and P values match across Results and Table 2. Neither the adjusted difference nor the ORPA is required to equal the pooled crude calculation or a transform of the displayed means. No significance incompatibility is inferred.

### Necessary inputs available and exact missing inputs or definitions

**Necessary inputs available:** Yes for the registered definition comparison, for the pooled count sum, and for the display-precision check. All nine measure counts, eligibility denominators, endpoint statements, arm labels, mean(SD) labels and adjustment labels are supplied and matched.

**Exact missing inputs or definitions:** Participant-level a_i/b_i fractions, their complete joint eligibility distribution and any rule for participants with no eligible opportunity are unavailable, so the numerical patient-average and its SD cannot be independently reconstructed from row totals. The supplied descriptions do not explicitly identify the exact target summary and computational steps of the adjusted composite absolute difference, reconcile pooled endpoint wording with patient averaging, or disclose an endpoint-definition amendment selecting between them. These omissions limit further reconstruction; they are not independent candidates. Neither a changed statistical significance decision nor an adjusted effect under another weighting definition can be calculated from the supplied evidence.

### Alternative interpretation, observation and inference

**Source-grounded alternative interpretation:** The reported descriptive endpoint may be the patient-average score expressly described in the main Outcomes paragraph, with an opportunity-based model for the separately reported odds effect, while the plan describes a pooled endpoint. Alternatively, the PLAN/supplement total-interventions wording may have intended patient averaging without stating that operation. Both are compatible with parts of the supplied text; neither is explicitly selected as the planned-and-used interpretation. A baseline-only explanation does not settle the REPORT-to-REPORT definition comparison because the supplement expressly states that the randomized phase used the same endpoint definition.

**Direct observation:** Three exact source definition locations state the two aggregation operations; the supplement connects its definition to the randomized phase; main Table 2 prints the means and nine integer pairs; main and PLAN model paragraphs describe opportunity-level odds inference. The independently derived pooled percentages lie outside the displayed mean rounding intervals.

**Inferred explanation:** A change of endpoint weighting or shorthand in the plan/supplement could explain the conflicting language, but neither explanation is established by the supplied source locations. The recheck does not attribute a cause or establish which analysis was actually implemented from aggregate counts alone. The patient-average definition within the main REPORT is clear; its correspondence with the PLAN/supplement primary definition remains a human question.

**Affected result or extracted value:** The primary composite 88.2% versus 84.8%, its interpretation as a patient-average score versus a pooled opportunity proportion, and the mapping of the accompanying adjusted absolute difference to the planned endpoint. No paper-level conclusion change is established.

**Exact remaining human question:** Was the prespecified randomized composite adherence summary the unweighted mean of patient-specific fulfilled/eligible fractions or the pooled proportion of fulfilled care opportunities, which aggregation produced the reported 88.2% versus 84.8%, and how does that definition relate to the adjusted absolute-difference analysis and the PLAN/supplement total-interventions wording?

### Classification confirmed from content

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C

**Compared document roles:** REPORT main article p.3 versus PLAN protocol p.16; REPORT main article p.3 versus REPORT results supplement p.2. Every additional source location's role is recorded in the location table.

**Classification rationale:** The actual prospective protocol definition differs from the main REPORT definition, so P_R is a substantive comparison rather than a plan that merely corroborates a within-report value. The results supplement's definition expressly applies to the randomized phase and supplies the same definition comparison between two REPORT documents, so S_C also applies. P_R has precedence over S_C under P_R > P_P > S_C > S_W and requires protocol_report. No P_P is established: PLAN endpoint and odds-model paragraphs are not contradictory summaries of the same descriptive quantity. No S_W is added: repetitions within the main REPORT agree, and its descriptive mean and modeled opportunity odds are separately specified. Corroborating analysis context supplies no additional relationship.

**Classification corrections:** None. The ledger's compared document roles, primary relationship, all relationships and domain are confirmed.

**Classification ambiguity:** No uncertainty about document roles. The intended scope of the pooled language, and any amendment reconciling it with patient averaging, remains unresolved by supplied text. This interpretive question does not establish another relationship or change precedence.

**Human adjudication status:** Pending Human Adjudication. Evidence state is an evidence-record fact, not a disposition.

### Tooling, durable derivatives and completion

Direct installed Poppler pdftotext 25.03.0 supplied fresh layout extraction; direct Poppler pdftoppm supplied fresh CPU-only PNG rendering. No OCR, fallback environment, Python extraction, global installation or GPU was used. Each newly written derivative has a unique path below preprocessing and was generated from an exact supplied PDF range:

| Derivative relative to review_1_6_1 | Engine | Exact direct-source range |
|---|---|---|
| preprocessing/recheck-main-p1-p5-layout.txt | Poppler pdftotext 25.03.0, -layout | jama_wang_2018_oi_180070.pdf, PDF pp.1–5 |
| preprocessing/recheck-main-p7-layout.txt | Poppler pdftotext 25.03.0, -layout | jama_wang_2018_oi_180070.pdf, PDF p.7 |
| preprocessing/recheck-plan-p16-layout.txt | Poppler pdftotext 25.03.0, -layout | joi180070supp1_prod.pdf, PDF p.16 |
| preprocessing/recheck-plan-p18-p19-layout.txt | Poppler pdftotext 25.03.0, -layout | joi180070supp1_prod.pdf, PDF pp.18–19 |
| preprocessing/recheck-report-supp-p2-layout.txt | Poppler pdftotext 25.03.0, -layout | joi180070supp2_prod.pdf, PDF p.2 |
| preprocessing/recheck-main-p7.png | Poppler pdftoppm 25.03.0, -png -singlefile -scale-to 2100 | jama_wang_2018_oi_180070.pdf, PDF p.7 |
| preprocessing/recheck-report-supp-p2.png | Poppler pdftoppm 25.03.0, -png -singlefile -scale-to 2100 | joi180070supp2_prod.pdf, PDF p.2 |

The existing current-run direct-source renders preprocessing/st1-main-p3.png and preprocessing/st1-plan-p16.png were also visually inspected and agree with fresh direct-source extraction. No legacy text, OCR or table asset was treated as final authority. Covered IDs: C001. Covered supplied-source page locations: ten, including every affected repeated occurrence and every model-context location assigned. Unread assigned locations: none. Unresolved reconstruction inputs and definitions are stated above. No stable ID was removed or suppressed, and the ledger was not edited by this specialist.
