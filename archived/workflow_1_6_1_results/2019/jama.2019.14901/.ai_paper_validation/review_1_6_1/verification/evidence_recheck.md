# Mechanical evidence and classification recheck

Fresh runtime `01a128ec-690f-7e03-a5dc-029f8535c3c2`; configured role `qc161_evidence_rechecker`, model `gpt-6.1-sol`, reasoning effort `high`, `FRESH_SPAWN`. Exact stable-ID scope: C001, C002, C003, C004, C005, including every affected occurrence of the registered patterns. The current ledger, initial inclusion screen, scope, complete review contract, current maps and cited checker passages were read. Prior scientific conclusions and external evidence were not used. Every ID remains Pending Human Adjudication. Evidence states below are mechanical facts, with no disposition.

Source confirmation used direct supplied-PDF native/layout reads and visual reading of current-run images rendered from those PDFs. Reusable text/maps were locators, not final authority. PDF page numbers below are physical PDF pages. Source content establishes the main article and results supplement as REPORT and the prospective version-4 clinical protocol as PLAN. The one-page data-sharing statement is administrative REPORT content and supplies no additional result, SAP or amendment.

## Confirmation tooling and derivatives

Direct CPU tools recorded in tooling_record.md were used: Poppler 26.01.0 `pdftotext -layout` and `pdftoppm`; no fallback, OCR, GPU, Office conversion or Python extraction was needed. Existing source-derived images were visually read without modification: `preprocessing/cross_source/main-p1.png`, `main-p4.png`, `main-p6.png`, `main-p8.png`, `protocol-p31.png`, `protocol-p34.png`, `results-p2.png`, and `preprocessing/statistics_pass1/results-p07.png`. Their current-run source/render provenance is recorded by those checkers; the direct extractions in this stage agree with the printed values in those images.

New unique derivatives, all under `preprocessing/evidence_recheck/`, are:

| Relative derivative path | Supplied source and exact scope | Engine and command pattern |
|---|---|---|
| preprocessing/evidence_recheck/main-all-layout.txt | jama_thille_2019_oi_190108.pdf pp.1–11 | Poppler 26.01.0 CPU, pdftotext -layout source output |
| preprocessing/evidence_recheck/results-all-layout.txt | joi190108supp2_prod.pdf pp.1–9 | Poppler 26.01.0 CPU, pdftotext -layout source output |
| preprocessing/evidence_recheck/protocol-p30-p34-layout.txt | joi190108supp1_prod.pdf pp.30–34 | Poppler 26.01.0 CPU, pdftotext -layout -f 30 -l 34 source output |
| preprocessing/evidence_recheck/data-sharing-p1-layout.txt | joi190108supp3_prod.pdf p.1 | Poppler 26.01.0 CPU, pdftotext -layout source output |
| preprocessing/evidence_recheck/protocol-p30.png | joi190108supp1_prod.pdf p.30 | Poppler 26.01.0 CPU, pdftoppm -f 30 -l 30 -r 110 -singlefile -png source output-stem |
| preprocessing/evidence_recheck/main-p7.png | jama_thille_2019_oi_190108.pdf p.7 | Poppler 26.01.0 CPU, pdftoppm -f 7 -l 7 -r 110 -singlefile -png source output-stem |
| preprocessing/evidence_recheck/results-p6.png | joi190108supp2_prod.pdf p.6 | Poppler 26.01.0 CPU, pdftoppm -f 6 -l 6 -r 110 -singlefile -png source output-stem |
| preprocessing/evidence_recheck/results-p9.png | joi190108supp2_prod.pdf p.9 | Poppler 26.01.0 CPU, pdftoppm -f 9 -l 9 -r 110 -singlefile -png source output-stem |

Every new image was visually inspected. Full direct main and results text was searched for subgroup, disease, weaning, mortality, log-rank, Cox and analysis-plan references; all relevant contexts and complete results-supplement contents/table inventory were inspected. The current complete evidence maps were cross-checked against that direct inventory when assessing supplied-result absence. The survival figure's numeric P value is visually confirmed because its native extraction is sparse. No supplied source or reusable asset was changed.

## Stable-ID classification and evidence facts

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Classification change |
|---|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT main abstract/narrative versus REPORT same-main Table 2 | reproduced | None |
| C002 | protocol_report | P_R | P_R | PLAN prospective severe-reintubation rule versus REPORT applied-rule description | reproduced | None |
| C003 | protocol_report | P_R | P_R | PLAN ICU mortality treatment-comparison specification versus REPORT ICU mortality analysis/result | reproduced | None |
| C004 | protocol_report | P_R | P_R | PLAN primary subgroup commitments versus REPORT supplied subgroup analysis set | reproduced | None |
| C005 | statistical_results | S_W | S_W | REPORT eTable 4 arm headings/counts versus REPORT same-table mortality difference | reproduced | None |

## C001 — Day-7 respiratory-failure absolute difference differs within the main report

**Registered scope:** Overall day-7 postextubation respiratory-failure absolute treatment difference, an abstract-reported secondary result. The repeated conflicting values are in three main-article locations; supplementary values only corroborate counts/populations. The already screened P-value subpart is not part of the inconsistency.

**Location found, source value/text matched, and comparator matched:**

| Exact supplied-source location | Content role | Independently matched printed content | Function in this ID |
|---|---|---|---|
| [Main p.1 abstract Results](../../../jama_thille_2019_oi_190108.pdf#page=1) | REPORT | Day-7 respiratory failure 21% versus 29%; difference −8.7%, 95% CI −15.2% to −1.8%, P=.01 | First affected effect occurrence |
| [Main p.6 Secondary Outcomes](../../../jama_thille_2019_oi_190108.pdf#page=6) | REPORT | Same day-7 endpoint, 21% versus 29%; difference −8.7%, same CI and P=.01 | Second affected effect occurrence |
| [Main p.8 Table 2 headings and respiratory-failure row](../../../jama_thille_2019_oi_190108.pdf#page=8) | REPORT | HFNC-alone n=302, 88 (29); HFNC+NIV n=339, 70 (21); absolute difference −8.5 (−15.2 to −1.8), P=.01 | Matched comparator and third affected occurrence |
| [Main p.4 Outcomes/Statistical Analysis](../../../jama_thille_2019_oi_190108.pdf#page=4) | REPORT | Same day-7 definition; categorical respiratory-failure comparison by chi-square; adjusted logistic descriptions concern primary reintubation | Method/population context |
| [Results p.2 eTable 1](../../../joi190108supp2_prod.pdf#page=2) | REPORT | Same 88/302 versus 70/339; P=.02 | Count corroboration; P subpart remains outside this candidate |
| [Results p.6 eTable 3](../../../joi190108supp2_prod.pdf#page=6) | REPORT | Hypercapnic control n=48, respiratory failure 24; intervention n=63, respiratory failure 14 | Corroborating component counts |
| [Results p.7 eTable 4](../../../joi190108supp2_prod.pdf#page=7) | REPORT | Nonhypercapnic control n=254, respiratory failure 64; intervention n=276, respiratory failure 56 | Corroborating component counts |

**Consistency rule applicable:** Matched overall endpoint, day, population, direction and unqualified absolute effect should agree between locations beyond their display precision. This rule concerns two printed reported effects and does not force an explicitly adjusted effect to equal a crude calculation.

**Calculation/logical comparison reproduced:** The printed −8.7 and −8.5 differ by 0.2 percentage points. Their closed half-unit rounding intervals are [−8.75,−8.65] and [−8.55,−8.45]; the intervals are disjoint, including endpoints. The exact displayed event fractions yield 100 times (70/339 minus 88/302) = −8.4901052961 percentage points, which lies in the Table 2 interval. Supplement component counts add to 24+64=88 and 14+56=70; denominators add to 48+254=302 and 63+276=339. The rounded arm percentages alone have wider intervals, but do not erase the directly conflicting effect intervals for the matched result. For the separate screened P observation, [.005,.015] for .01 and [.015,.025] for .02 overlap at .015; no P inconsistency is carried forward.

**Necessary inputs available:** Both printed effects, all three affected locations, result matching, table population/counts and displayed precision are available. No raw data is needed to reproduce this reported-effect disagreement.

**Exact missing inputs/definitions:** The narrative −8.7 calculation, any distinct narrative estimator or denominator, and exact CI/test settings are not supplied. The method description does not identify the narrative effect as a separate modeled analysis.

**Source-grounded alternative interpretation:** Table counts support its printed −8.5 at one decimal place. A separate unlabelled narrative estimator or a reporting transcription could explain −8.7, but neither explanation is established by the supplied content. The count calculation does not select an authoritative reported value for human review.

**Direct observation versus inferred explanation:** Direct: both −8.7 occurrences and the −8.5 table value, identical endpoint/CI, and disjoint display intervals. Inferred possibilities: an unlabelled calculation or reporting transcription. No change in clinical conclusion is asserted.

**Classification confirmation:** Every conflicting location is REPORT content in the same main document: primary relationship S_W; all relationships S_W; statistical_results because the issue concerns an effect estimate. Supplementary counts corroborate one side and are not a conflict. No S_C or P_R relationship applies; precedence therefore selects S_W. No role ambiguity or classification correction.

**Evidence state:** reproduced. Determining fact: the exact main abstract and narrative print −8.7 while the same-main table prints −8.5 for the matched outcome, with disjoint half-unit intervals. All registered values/locations matched without transcription correction.

**Exact remaining human question:** Which overall day-7 respiratory-failure absolute difference and calculation were intended in the two narrative occurrences and Table 2, and was a distinct estimator or denominator used for either narrative occurrence?

## C002 — Severe-acidosis threshold differs between plan and reported reintubation rule

**Registered scope:** Severe-acidosis component of the at-least-two-component respiratory reintubation rule underlying the primary day-7 endpoint. This is distinct from the less-severe secondary respiratory-failure definition.

**Location found, source value/text matched, and comparator matched:**

| Exact supplied-source location | Content role | Independently matched printed content | Function in this ID |
|---|---|---|---|
| [Protocol p.30 section 5.4 start](../../../joi190108supp1_prod.pdf#page=30) | PLAN | Reintubation respiratory failure requires at least 2 criteria; first component respiratory rate >35/min; separate ARF list above uses pH<7.35 | Start of prospective severe rule and endpoint disambiguation |
| [Protocol p.31 section 5.4 continuation](../../../joi190108supp1_prod.pdf#page=31) | PLAN | Severe-rule acidosis item pH<7.35 units and PaCO2>45 mm Hg; FiO2≥80%/ratio≤100 and other sufficient reintubation categories follow | Compared planned cutoff |
| [Main p.4 Outcomes](../../../jama_thille_2019_oi_190108.pdf#page=4) | REPORT | Severe respiratory failure leading to reintubation requires at least 2 criteria; acidosis pH below 7.25 and PaCO2>45; separate secondary failure uses pH<7.35 | Compared reported cutoff |
| [Main p.8 Table 2 primary row](../../../jama_thille_2019_oi_190108.pdf#page=8) | REPORT | Day-7 reintubation 55/302 versus 40/339, difference −6.4 | Affected primary endpoint context; no count conflict asserted |
| [Results p.2 eTable 1 severe-failure acidosis row](../../../joi190108supp2_prod.pdf#page=2) | REPORT | Severe respiratory-acidosis criterion counts 12 (4%) versus 9 (3%), P=.35 | Corroborating criterion reporting; cutoff not independently defined in the table |

**Consistency rule applicable:** Corresponding prospective and reported operational components of a primary endpoint decision rule differ. Both content contexts expressly describe severe respiratory failure leading to reintubation; comparing the report's severe item against the plan's separate ARF list would be a different comparison and was not done.

**Calculation/logical comparison reproduced:** With PaCO2>45, pH in [7.25,7.35) meets the plan's acidosis component and not the report's. If exactly one other respiratory component is met and no independently sufficient indication is present, the severe-rule eligibility can differ. This is a logical example, not a claim about any observed participant. The thresholds are specified rules, not rounded patient measurements. Even granting a half-unit interval to the two-decimal cutoffs gives [7.345,7.355] versus [7.245,7.255], disjoint by at least .09 pH units, so display precision cannot explain the rule difference. The common PaCO2 cutoff does not resolve it.

**Necessary inputs available:** Both explicit pH/PaCO2 conditions, the two-component requirement, severe-rule context across plan pp.30–31, and affected primary endpoint are available. Participant-level gases are not necessary to establish the textual rule discrepancy.

**Exact missing inputs/definitions:** The applicable dated operational rule/SAP or amendment, which cutoff actually governed ascertainment at each site, patient-level pH and other simultaneous criteria, and any explanation for the changed cutoff. Counts 12 and 9 do not identify the applied threshold or quantify affected participants.

**Source-grounded alternative interpretation:** The prospective protocol is version 4 dated 17 October 2017; the article says analyses followed a predefined SAP. A later applicable amendment or a reporting transcription might explain the cutoff, but the supplied package provides neither an applicable replacement rule nor a cutoff explanation. The separate pH<7.35 secondary failure definition supplies no resolution of the severe-rule comparison.

**Direct observation versus inferred explanation:** Direct: the respective severe thresholds and two-component contexts. Inferred possibilities: later rule change or reporting transcription. No actual reclassification, primary-event count change, or preferred clinical threshold is inferred.

**Classification confirmation:** Protocol pp.30–31 contain prospective operational instructions and are PLAN by content. Main p.4 contains published methods and is REPORT. Primary relationship P_R; all relationships P_R; protocol_report. Report results/criterion counts merely show affected reporting context and do not create S_C/S_W conflicts. Highest-precedence listed relationship is P_R. No role ambiguity or classification correction; an unsupplied amendment remains a human question.

**Evidence state:** reproduced. Determining fact: exact severe reintubation definitions specify pH<7.35 in the plan and pH<7.25 in the report, beyond display precision. No registered value/location required transcription correction.

**Exact remaining human question:** Which dated severe-acidosis cutoff governed primary reintubation decisions, and does an applicable amendment, SAP, or reporting explanation reconcile the plan pH<7.35 with the report pH<7.25?

## C003 — ICU mortality comparison is planned as log-rank and reported as chi-square

**Registered scope:** Planned versus reported treatment-group analysis of abstract-reported ICU mortality. Only the unconditional Kaplan–Meier/log-rank commitment is compared; conditional Cox-model omissions are outside this ID.

**Location found, source value/text matched, and comparator matched:**

| Exact supplied-source location | Content role | Independently matched printed content | Function in this ID |
|---|---|---|---|
| [Protocol p.34 section 6.3 continuation](../../../joi190108supp1_prod.pdf#page=34) | PLAN | Mortality criteria explicitly include ICU, in-hospital, day 28 and day 90; curves from enrollment to death will be compared between two treatment groups by log-rank | Planned ICU method; unconditional sentence precedes conditional Cox passage |
| [Main p.4 Statistical Analysis](../../../jama_thille_2019_oi_190108.pdf#page=4) | REPORT | ICU and hospital mortality rates compared by chi-square; separate extubation-to-death curves compared by log-rank at day 90 | Reported ICU method and separate day-90 method |
| [Main p.1 abstract Results](../../../jama_thille_2019_oi_190108.pdf#page=1) | REPORT | ICU mortality 6% versus 9%, difference −2.4 (−6.7 to 1.7), P=.25 | Establishes abstract-reported key secondary result |
| [Main p.8 Table 2 ICU mortality row/headings](../../../jama_thille_2019_oi_190108.pdf#page=8) | REPORT | Control 26/302 (9%), intervention 21/339 (6%); absolute difference −2.4 (−6.7 to 1.7), P=.25 | Matched ICU result and population |
| [Results p.9 eFigure title/legend/test label](../../../joi190108supp2_prod.pdf#page=9) | REPORT | Overall cumulative survival from extubation to day 90; log-rank P=.37 | Separately identified overall day-90 analysis; does not supply the ICU analysis |
| [Main pp.1–11, methods p.4/results pp.6–8](../../../jama_thille_2019_oi_190108.pdf#page=4), [results pp.1–9, contents p.1](../../../joi190108supp2_prod.pdf#page=1) | REPORT | Supplied figures/tables and matching mortality/log-rank contexts contain no separately identified ICU log-rank output | Availability comparison within complete supplied report inventory |

**Consistency rule applicable:** Explicit prospective treatment-comparison specification for the same key secondary outcome is compared with its stated reported method and available output. Coherent distinct tests do not explain this plan/report specification difference. This is not a claim that chi-square P=.25 cannot follow the ICU counts.

**Calculation/logical comparison reproduced:** Planned method set includes an ICU mortality log-rank comparison; reported ICU method is chi-square. The survival figure is identified as overall day-90 survival, so it does not establish the planned ICU log-rank result. As an arithmetic context check only, 100 times (21/339 minus 26/302) = −2.4145812577 percentage points, within the printed −2.4 interval [−2.45,−2.35]. The ICU P=.25 display interval is [.245,.255]; day-90 P=.37 gives [.365,.375], but those tests concern distinct outcome/window specifications and their non-overlap is not an inconsistency claim. The discrepancy is categorical method identity, to which numerical rounding does not apply. No log-rank statistic or P value is reconstructed from final death counts.

**Necessary inputs available:** Unconditional prospective method sentence, explicit reported ICU method, matched ICU result, endpoint hierarchy by abstract inclusion, and complete supplied output inventory are available.

**Exact missing inputs/definitions:** Applicable SAP/amendment governing ICU mortality, any retained ICU Kaplan–Meier/log-rank output, explanation of the method change, individual death/discharge/follow-up times, censoring rules and time origin for an ICU survival comparison. These missing time-to-event inputs prevent numerical reproduction of a planned log-rank result; they do not prevent the textual specification comparison.

**Source-grounded alternative interpretation:** The source explicitly reports a separate day-90 log-rank analysis; the ICU comparison could have been amended or retained elsewhere without being supplied. The article's statement that analyses followed a predefined SAP makes the applicable SAP relevant, but it is not separately supplied. Neither possibility is asserted to have occurred. The subsequent plan Cox passage has a conditional qualifier and is not appended to this candidate.

**Direct observation versus inferred explanation:** Direct: ICU listed in the planned unconditional log-rank sentence, reported ICU chi-square statement/P=.25, and separate day-90 figure. Inferred possibility: amended or unreported ICU analysis. No test preference, hypothetical ICU log-rank result, or numerical P inconsistency is inferred.

**Classification confirmation:** Prospective statistical commitments are PLAN and published methods/results are REPORT. Primary relationship P_R; all relationships P_R; protocol_report. No S_C relationship arises because main and supplement concern distinguishable mortality windows rather than conflicting ICU results. Precedence selects P_R; no classification correction or role ambiguity.

**Evidence state:** reproduced. Determining fact: exact supplied statements specify log-rank for planned ICU mortality and chi-square for reported ICU mortality, and the separately supplied survival figure identifies only overall day-90 output. No value or location required transcription correction.

**Exact remaining human question:** What applicable analysis specification governed ICU mortality, and where is its planned between-treatment ICU log-rank comparison or a documented explanation/amendment accounting for the reported chi-square analysis?

## C004 — Prespecified disease and weaning-test primary subgroup results are absent

**Registered scope:** One repeated planned-primary-subgroup reporting pattern affecting two explicitly named factor families: underlying cardiac/respiratory disease and T-piece versus minimal pressure-support weaning test. Non-key secondary subgroup omissions are outside this ID.

**Location found, source value/text matched, and comparator matched:**

| Exact supplied-source location | Content role | Independently matched printed content | Function in this ID |
|---|---|---|---|
| [Protocol p.34 section 6.4](../../../joi190108supp1_prod.pdf#page=34) | PLAN | Main and secondary subgroup analyses will be performed by PaCO2; moreover in patients with underlying cardiac or respiratory disease and according to T-piece versus minimal pressure-support weaning test | Both affected prospective primary-subgroup commitments |
| [Main p.4 Statistical Analysis subgroup paragraph](../../../jama_thille_2019_oi_190108.pdf#page=4) | REPORT | Primary/secondary subgroup analysis described according to PaCO2≤45 or >45 with treatment interaction test | Reported subgroup factor set |
| [Main p.7 Subgroup Analysis and Additional Analyses](../../../jama_thille_2019_oi_190108.pdf#page=7) | REPORT | PaCO2 interaction P=.25; hypercapnic day-7 difference −12.9 and nonhypercapnic difference −5.0; adjusted primary OR=.60 with PaCO2/chronic-lung-disease covariates | Supplied subgroup effects; covariate adjustment is not a disease subgroup output |
| [Main p.8 Figure 3 panels/caption](../../../jama_thille_2019_oi_190108.pdf#page=8) | REPORT | Hypercapnic and nonhypercapnic day-7 reintubation curves only, log-rank P=.049 and .11 | Supplied primary subgroup figure set |
| [Results p.1 contents](../../../joi190108supp2_prod.pdf#page=1) | REPORT | Criteria table, PaCO2 baseline table, hypercapnic/nonhypercapnic outcome tables, center table, overall survival eFigure | Complete supplementary results inventory |
| [Results p.6 eTable 3 title/primary row](../../../joi190108supp2_prod.pdf#page=6) | REPORT | Hypercapnic n=48/63, day-7 reintubation 10/5, difference −12.9 (−27.1 to −0.1), P=.0489 | Supplied PaCO2 primary subgroup output |
| [Results p.7 eTable 4 title/primary row](../../../joi190108supp2_prod.pdf#page=7) | REPORT | Nonhypercapnic n=254/276, day-7 reintubation 45/35, difference −5.0 (−11.2 to 1.1), P=.1057 | Supplied PaCO2 primary subgroup output |
| [Complete main pp.1–11, baseline disease p.5/weaning p.6](../../../jama_thille_2019_oi_190108.pdf#page=5), [complete results pp.1–9, baseline pp.3–5](../../../joi190108supp2_prod.pdf#page=3) | REPORT | Disease and weaning descriptors occur in baseline tables; no disease/weaning primary subgroup treatment effects or interaction results supplied | Complete availability assessment for both affected factor families |

**Consistency rule applicable:** A prespecified primary subgroup analysis explicitly committed in the supplied prospective plan can be compared with the supplied reported analysis/result set under focus D. This is not merely an inference that a customary method should have been described. Both factor families share the same absent-planned-primary-output pattern and remain one stable ID.

**Calculation/logical comparison reproduced:** Prospective primary subgroup factor set includes PaCO2, underlying disease and weaning-test mode. Supplied primary subgroup effect/curve set contains PaCO2 only; both additional factor families lack matching supplied outputs or a reporting explanation. Disease adjustment in the overall logistic model is a covariate analysis, not an outcome contrast within the planned disease subgroup. Baseline factor counts also cannot supply those treatment contrasts. Display precision is not applicable to the categorical set membership/availability comparison; allowing any half-unit intervals for displayed PaCO2 effects cannot create absent disease/weaning outputs. The printed −12.9 interval [−12.95,−12.85] and −5.0 interval [−5.05,−4.95] are identifiers of different PaCO2 strata, not compared as conflicting estimates.

**Necessary inputs available:** The explicit prospective promise for the main criterion, both named factor families, complete main/results contents and reported subgroup methods/output inventory are available. These inputs establish absence from the supplied report, not absence from all study work.

**Exact missing inputs/definitions:** Applicable SAP/amendment retaining or removing the two primary subgroup families, their outcome-specific counts/effect estimates/interactions, reporting explanation, and the precise intended disease grouping (cardiac and respiratory separately or combined). The source establishes a disease subgroup commitment but not every proposed disease-subgroup partition. Missing participant cross-classifications prevent reconstructing those outputs from baseline totals.

**Source-grounded alternative interpretation:** The article's predefined SAP might have amended the subgroup set, or the disease/weaning results might exist outside the supplied package. Those possibilities are not established. Chronic-lung-disease adjustment in the supplied model cannot itself be read as the promised subgroup output. No subgroup heterogeneity, numerical result or performed/unperformed status is inferred.

**Direct observation versus inferred explanation:** Direct: both explicit primary subgroup commitments and the PaCO2-only supplied subgroup inventory. Inferred possibilities: omitted reporting or a changed applicable plan. Only supplied-result availability is recorded; actual analysis execution is not determined.

**Classification confirmation:** Prospective section 6.4 is PLAN; main subgroup methods/figures and supplementary results are REPORT by content. Primary relationship P_R; all relationships P_R; protocol_report. The report locations consistently concern PaCO2, so they do not create S_C or S_W conflicts. P_R is the highest-precedence listed relationship. No classification correction; intended disease partition and an unsupplied SAP/amendment remain interpretive limitations, not document-role ambiguity.

**Evidence state:** reproduced. Determining fact: exact protocol p.34 commits primary analyses for both disease and weaning factors, while the complete supplied report inventory supplies PaCO2 subgroup outputs and no matching outputs or explanation for either factor family. No registered value/location required transcription correction.

**Exact remaining human question:** Were the prespecified primary disease and weaning-test subgroup analyses retained in the applicable SAP, what disease partition was intended, and where are their results or an explanation for their absence from the supplied report?

## C005 — Nonhypercapnic day-90 mortality absolute difference does not reconcile

**Registered scope:** The within-row quantity identity of the nonhypercapnic day-90 mortality absolute difference in eTable 4. It does not compare peripheral outcomes across displays or infer a preferred estimator.

**Location found, source value/text matched, and comparator matched:**

| Exact supplied-source location | Content role | Independently matched printed content | Function in this ID |
|---|---|---|---|
| [Results p.7 eTable 4 title and population headings](../../../joi190108supp2_prod.pdf#page=7) | REPORT | Nonhypercapnic PaCO2≤45; HFNC alone n=254; HFNC+NIV n=276; absolute-difference column | Population, direction and quantity identity |
| [Results p.7 final mortality-at-day-90 row](../../../joi190108supp2_prod.pdf#page=7) | REPORT | Control 54 (21%); intervention 50 (18%); absolute difference −3.8 (−9.9 to 3.6), P=.3626 | Compared event values and displayed effect |
| [Results p.7 other binary rows](../../../joi190108supp2_prod.pdf#page=7) | REPORT | Day-7 reintubation 45/254 versus 35/276 gives −5.0; hospital mortality 39/254 versus 46/276 gives 1.3 | Local proportion-difference convention corroboration |
| [Main p.4 Statistical Analysis](../../../jama_thille_2019_oi_190108.pdf#page=4) | REPORT | Categorical rate comparisons; covariate-adjusted logistic models explicitly for primary reintubation; overall day-90 survival analysis separately described | Method context; no identified adjusted nonhypercapnic day-90 risk difference |

**Consistency rule applicable:** For the table's displayed arm-proportion contrast, an absolute percentage-point difference should reconcile with the stated event fractions beyond display precision. The direct table labels, arm headings and neighboring binary effects support this quantity reading. The source does not explicitly label this mortality entry as adjusted or model-based; it also does not explicitly name its absolute-difference estimator. Accordingly the reproducible fact is the mismatch with its displayed proportions, and the exact estimator remains a human question. No explicitly model-based contrast is forced to equal a crude value.

**Calculation/logical comparison reproduced:** 100 times (50/276 minus 54/254) = −3.1439004907 percentage points. Treating integer participant counts/denominators as exact gives the displayed-fraction contrast, which is outside −3.8's rounding interval [−3.85,−3.75]. Even an overly permissive continuous half-unit check allows deaths 49.5–50.5 and 53.5–54.5, intervention denominator 275.5–276.5 and control denominator 253.5–254.5. The extreme minimum is 100 times (49.5/276.5 minus 54.5/253.5) = −3.5966629930; the maximum is 100 times (50.5/275.5 minus 53.5/254.5) = −2.6913024720. This entire interval is disjoint from [−3.85,−3.75]. Coarse displayed percentages alone could yield a difference near −3.8, but the exact reported event fractions supply more precise inputs and cannot. Local binary examples yield −5.0353760128 for day-7 reintubation and 1.3123359580 for hospital mortality, both rounding to their printed −5.0 and 1.3. CI asymmetry and the P value are not used to determine the evidence state.

**Necessary inputs available:** Exact table population headings, mortality counts, unqualified absolute-difference label, displayed effect/precision, neighboring binary convention, and method context are available. Raw participant data are not necessary for the printed-fraction arithmetic.

**Exact missing inputs/definitions:** The exact mortality absolute-difference estimator and its adjustment/censoring treatment, any mortality-specific alternative denominator or analysis population, the source values used to generate −3.8, and exact CI/test settings. In particular a separately specified modeled or survival-based risk contrast is not provided for this row.

**Source-grounded alternative interpretation:** An unlabelled model-based estimate, time-to-event risk estimate, or alternative denominator could reconcile −3.8 if its identity and inputs were established. The report separately contains an overall day-90 Kaplan–Meier analysis, but it does not link that analysis to this subgroup row's absolute-difference entry. A reporting transcription affecting the effect or a count is another possibility. None is established, and no replacement value is prescribed. If a distinct modeled estimator is established, the human can revisit the displayed-fraction comparison accordingly.

**Direct observation versus inferred explanation:** Direct: all source headings/counts/effect, absence of a locally identified distinct estimator, and arithmetic/display-interval non-reconciliation for the printed fractions. Inferred possibilities: unlabelled estimator, denominator or reporting transcription. No raw-data result, changed nonsignificance conclusion, CI-method inconsistency, or causal explanation is asserted.

**Classification confirmation:** Both actual conflicting quantities occur within REPORT eTable 4 in one results document. Primary relationship S_W; all relationships S_W; statistical_results because the issue concerns effect-measure/quantity identity. Main method text is context and does not establish a cross-report conflict. P_R, P_P and S_C are not added; precedence selects S_W. No role ambiguity or classification correction. The unidentified estimator is an evidence limitation, not a role ambiguity.

**Evidence state:** reproduced. Determining fact: direct p.7 shows the registered counts/denominators and −3.8, and their stated arm-proportion reading remains disjoint after exact and conservative half-unit calculations. No registered value/location required transcription correction. This state records that quantity-comparison fact; it does not establish the undisclosed estimator or determine human disposition.

**Exact remaining human question:** Which estimator, population and denominators generated the nonhypercapnic day-90 mortality absolute difference −3.8, and how does that estimate relate to the displayed 54/254 and 50/276 event fractions?

## Completion and limitations

All five stable IDs and every registered affected location were rechecked separately. Evidence states: reproduced=5; reproduced_after_transcription_correction=0; not_reproduced=0. Document roles, primary/all relationships and review domains are unchanged: two statistical_results/S_W candidates and three protocol_report/P_R candidates. No evidence transcription or source-page correction was needed. No stable ID was removed, appended, or reclassified by this stage.

There is no source-confirmation or tool gap. Remaining evidence limitations are named separately above: an applicable separate SAP/amendment is not supplied; the administrative source states data are unavailable; exact narrative/table estimator settings, operational cutoff history, ICU time-to-event output/input data, and disease/weaning subgroup results are not supplied. These limitations do not authorize reconstructed raw outcomes, model assumptions or human dispositions. The coordinator owns ledger updates; this stage changed only its assigned evidence-recheck artifact and unique preprocessing derivatives.
