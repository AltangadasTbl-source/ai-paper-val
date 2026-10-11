# Mechanical evidence recheck — Workflow 1.6.2

Assigned scope: every stable ID C001–C014 in the current candidate ledger, including every affected occurrence of each consolidated pattern. Status: COMPLETE. Rechecker runtime: `/root/evidence_rechecker`; run model: `gpt-6.1-sol`; reasoning effort: `high`. This document records evidence facts and classification facts; every stable ID remains Pending Human Adjudication.

The recheck read `QUALITY_CONTROL_SCOPE.md` and `workflow_1_6_2/review_contract.md`, the current ledger and initial screening record, the source inventory, and the tooling record. Only supplied package evidence was used. DOC-001 is REPORT content: the published article and its actual results. DOC-002 is PLAN content: Protocol 2014-0213, August 23, 2023, with prospective design and analysis commitments. DOC-003 is REPORT content: supplementary methods and actual results supporting the article. Its descriptions of anticipated distributions do not turn the retrospective results supplement into a separate PLAN document.

Authority and engines: fresh direct Poppler `pdftotext -layout` extraction from all three supplied PDFs, with direct-source page renders to confirm the compared printed readings, mathematical signs, decimals, formulas, beta parameters, and cell alignment. Current-source renders from `main_mapper`, `support_mapper`, `plan_mapper`, and `statistical_pass1` were inspected; they were used with the supplied PDFs and independent direct extraction, not as autonomous transcription authority. Additional direct Poppler `pdftoppm` renders covered REPORT supplement pp.5–6, PLAN pp.7,24–25, and main p.8. Rendering was CPU, using the recorded Poppler 26.01.0 tooling; no OCR, fallback, or GPU was needed. New derivatives are confined to `preprocessing/evidence_rechecker/`: `main-direct-layout.txt`, `plan-direct-layout.txt`, `support-direct-layout.txt`, the six additional page PNGs, `calculations.R`, and `calculations.txt`. R 4.5.2 independently reproduced qbeta/pbeta, qnorm/exp, and count/percentage interval arithmetic. No source or reused artifact was modified.

All links below use physical PDF page numbers. The three source paths are [main article](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1), [protocol](../../../joi240036supp1_prod_1716416466.00349.pdf#page=1), and [results supplement](../../../joi240036supp2_prod_1716416466.01349.pdf#page=1). Numeric precision checks allow half of the last displayed unit to each input and each compared number; interval gaps are divided by the absolute reference printed value. Gaps above 0.05 reproduce under the scope rule. Integer counts are also given conservative half-unit intervals; their being discrete would not reconcile the findings. Route A category 1 containment/test conflicts are independent of this rounding rule. No Bayesian benefit probability was interpreted as a frequentist P value, and model probabilities were not replaced with crude event fractions.

## Final classification and evidence-state table

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state |
|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | PLAN prospective second-stage assignment/analysis vs REPORT assigned-continuation primary populations | reproduced |
| C002 | statistical_results | S_C | S_C, S_W | REPORT main actual assigned-continuation population and IPW claim vs REPORT supplement per-observation weight specification | reproduced |
| C003 | statistical_results | S_W | S_W | REPORT main abstract counts/percentages and flow counts | reproduced |
| C004 | statistical_results | S_C | S_C, S_W | REPORT main abstract/body CNRT contrasts vs REPORT supplement eTable 4 | reproduced |
| C005 | statistical_results | S_C | S_C, S_W | REPORT main abstract/body/figure direction and contrast vs REPORT supplement eTable 4 sign | reproduced |
| C006 | protocol_report | P_R | P_R | PLAN selected posterior advancement criterion vs REPORT asserted prespecified confirmation criterion | reproduced |
| C007 | protocol_report | P_R | P_R | PLAN general analytic-strategy robustness commitments vs complete supplied REPORT scope | reproduced |
| C008 | statistical_results | S_C | S_C, S_W | REPORT main/supplement narrative VAR continuation size vs REPORT supplement eFigure 2 size | reproduced |
| C009 | statistical_results | S_C | S_C, S_W | REPORT main/supplement six-month CNRT summary vs REPORT supplement detailed probabilities/figure/table | reproduced |
| C010 | plan_material | P_P | P_P, S_W | PLAN distribution definition vs PLAN Figure 2; REPORT distribution definition vs REPORT eFigure 1 | reproduced |
| C011 | statistical_results | S_W | S_W | REPORT supplement normal variance definition vs its claimed 95% prior odds limits | reproduced |
| C012 | statistical_results | S_W | S_W | REPORT supplement seven EOT+30 narrative occurrences vs matched eFigure 2/eTables 9–11 | reproduced |
| C013 | statistical_results | S_W | S_W | REPORT supplement six-month responder narrative credible limits vs eTable 11 | reproduced |
| C014 | report_internal_inconsistency | S_C | S_C, S_W | REPORT supplement anticipated CNRT+ dose vs REPORT main/supplement regimen definitions | reproduced_after_transcription_correction |

No document-role, primary relationship, all-relationship, or domain change is required from the ledger. Specific classification reasoning and any bounded ambiguity are recorded separately for every ID. Final audited evidence-state counts: reproduced 13; reproduced_after_transcription_correction 1; not_reproduced 0. C014's pp.15–16 comparator caption specificity was corrected after direct visual audit; its focal discrepancy remains reproduced. Arithmetic-envelope refinements below do not change a transcribed source value or source location.

## C001 — Planned and reported primary continuation populations

**Location found; source value/text matched:** PLAN [p.7, Participants](../../../joi240036supp1_prod_1716416466.00349.pdf#page=7) specifies rerandomization of patients failing abstinence to continuation, switching, or augmentation. PLAN [p.24, final pharmacotherapy paragraph](../../../joi240036supp1_prod_1716416466.00349.pdf#page=24) repeats a second randomization for week-6 smokers; [p.25, first paragraph](../../../joi240036supp1_prod_1716416466.00349.pdf#page=25) describes their subsequent medication. PLAN [p.28, general strategy and coding/model](../../../joi240036supp1_prod_1716416466.00349.pdf#page=28), [p.29, Aims 2–3](../../../joi240036supp1_prod_1716416466.00349.pdf#page=29), and [p.30, continuing Aim 3 contrasts](../../../joi240036supp1_prod_1716416466.00349.pdf#page=30) use second-stage continuation as the reference. The missing-observations-as-smoking and intention-to-treat commitments are explicitly present on p.28.

**Comparator matched:** REPORT [main p.1, both Results paragraphs](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1) adds 40 CNRT and 35 VAR nonreturners to continuation. [Main p.4, Results/flow prose](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4) states assignment for phase-2 analyses and all-participant primary intention-to-treat analysis. [Main p.6, Figure 2 and footnote c](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6) explicitly shows 50 randomized plus 40 assigned CNRT continuers, and 42 randomized plus 35 assigned VAR continuers, with primary-analysis totals 90 and 77. [Main p.8, first limitation](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=8) explains assignment because those participants were exposed to one strategy. REPORT [supplement p.6, phase-II weighting/coding](../../../joi240036supp2_prod_1716416466.01349.pdf#page=6) specifies the rerandomized-nonresponder pathway.

**Consistency rule applicable; comparison reproduced:** Focus D, route A category 5: a primary analysis-population/strategy specification differs between PLAN and REPORT. Exact counts give 90 = 50 + 40, 77 = 42 + 35, and 75 = 40 + 35. This is a comparison of documented membership policies, not a claim that the plan printed sample sizes 50 or 42. Intention-to-treat imputation of an outcome as smoking does not itself specify assignment of a second-stage treatment. Display precision is not applicable to the logical policy comparison; counts reconcile internally.

**Necessary inputs available:** Prospective second-stage design and contrasts; reported deterministic additions and analyzed totals. **Exact missing inputs or definitions:** A prospective rule or disclosed amendment assigning nonreturners to second-stage continuation, and any separate rerandomized-only primary result. The complete plan text was searched for nonreturner/assigned-continuation policies; the cited plan sections supply no such rule.

**Source-grounded alternative interpretation:** The plan's broad intention-to-treat commitment could have been implemented through continuation assignment, consistent with the report's explanation, or an additional amendment could have specified it. Neither supplies the absent explicit second-stage policy in this package.

**Direct observation versus inferred explanation:** Planned rerandomization and actual assigned additions are observed. Whether assignment was a planned implementation, later decision, or amendment is not established.

**Classification rationale:** Retain PLAN/REPORT, primary/all P_R, protocol_report: the compared issue is prospective versus actual primary-analysis membership, not a conflict between the mutually consistent report counts. **Classification ambiguity:** Possible additional amendment or interpretation of the broad intention-to-treat policy; no content-role ambiguity.

**Evidence state:** reproduced. **Determining recheck fact:** The actual primary continuation populations explicitly include 40/35 participants who did not undergo the planned second randomization, without an explicit supplied prospective assignment rule.

**Exact human question:** Which prospective rule or amendment specified assigning the 40 CNRT and 35 VAR nonreturners to the primary second-stage continuation reference populations, rather than only imputing their outcomes as smoking?

## C002 — Weight mapping for 75 assigned continuation participants

**Location found; source value/text matched:** REPORT [main p.1, assigned counts](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1), [p.4, statistical methods and participant flow](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4), and [p.6, Figure 2/footnote c](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6) establish 75 deterministically assigned nonreturners and IPW primary analyses. The resulting reference groups are also explicitly displayed at [main p.7, Figure 3](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7): 7/90 CNRT, 8% (6%–10%), and 2/77 VAR, 3% (1%–4%).

**Comparator matched:** REPORT [supplement p.5, opening eAppendix 3](../../../joi240036supp2_prod_1716416466.01349.pdf#page=5) calls randomization probabilities known fixed design quantities. [P.6, first two paragraphs and coding](../../../joi240036supp2_prod_1716416466.01349.pdf#page=6) states first-stage p = 0.5, responder continuation p = 1, nonresponder rerandomization p = 0.33; weights 2 and 6.06; and multiplication of each observation's log-posterior contribution by its corresponding weight. Its formula explicitly describes nonresponders who were rerandomized. [Supplement p.19, eTable 3 headings](../../../joi240036supp2_prod_1716416466.01349.pdf#page=19) confirms 90/77 continuation cells.

**Consistency rule applicable; calculation reproduced:** Focus C, route B: a necessary mapping step is absent for an explicitly included nonrandomized pathway. 1/0.5 = 2; 1/(0.5 × 1) = 2; 1/(0.5 × 0.33) = 6.060606, consistent with printed 6.06. Allowing p = 0.5 ± 0.05 and p = 0.33 ± 0.005 gives a conservative rerandomized-weight range [5.4274,6.8376], overlapping 6.06 ± 0.005. Thus the numerical formula reconciles; the reproduced issue is the mapping for 40 + 35 assigned observations, which is not a rounding comparison and does not determine their implemented weight.

**Necessary inputs available:** Actual analyzed membership; fixed probability formulas; per-observation implementation statement. **Exact missing inputs or definitions:** The assigned nonreturners' weight, probability basis, coding, likelihood inclusion/imputation convention, and any model code confirming their treatment.

**Source-grounded alternative interpretation:** Assigned observations may share a nonresponder design weight, receive another weight, or enter through an imputation/augmentation convention. The separately reported post hoc GEE/data augmentation analysis on supplement pp.12–13 does not identify the primary Bayesian assigned-pathway mapping.

**Direct observation versus inferred explanation:** Presence of assigned participants and the restricted explicit weight formulas are observed; no numerical bias, actual weight, or consequence for posterior estimates is inferred.

**Classification rationale:** Retain REPORT/REPORT, S_C primary, all S_C and S_W, statistical_results. Cross-document population/method mapping is focal; the main report internally combines all-participant analysis with the design-IPW description, and the supplement pairs that method with 90/77 cell membership. The plan does not establish this implementation conflict. **Classification ambiguity:** Implemented weight/coding are absent; source roles are clear.

**Evidence state:** reproduced. **Determining recheck fact:** The reported model includes a documented 75-person nonrerandomized pathway that the explicit randomization-based weight mapping does not identify.

**Exact human question:** What weight, probability basis, coding, and likelihood/imputation treatment were used for each of the 40 CNRT and 35 VAR assigned nonreturners in the reported primary Bayesian model?

## C003 — Mixed denominators in abstract allocation percentages

**Location found; source value/text matched:** REPORT [main p.1, CNRT and VAR Results paragraphs](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1) prints, among 191 CNRT nonabstainers, 90 (47%) continuation, 50 (33%) increase, and 51 (34%) switch; among 157 VAR nonabstainers, 77 (49%) continuation, 39 (32%) increase, and 41 (34%) switch.

**Comparator matched:** REPORT [main p.6, Figure 2 branches](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6) reproduces every count and distinguishes rerandomized totals 151 and 122 from full nonabstainer totals 191 and 157. Within the abstract, the common population descriptions and continuation percentages provide the denominator comparator.

**Consistency rule applicable; calculation and precision reproduced:** Focus A, route A category 3. All four affected percentages are preserved below. Conservative half-unit count/denominator envelopes are used.

| Population; count; printed percentage | Recomputed percentage interval | Printed interval | Relative remaining gap |
|---|---|---|---:|
| CNRT 191; increase 50; 33% | [25.848564,26.509186]% | [32.5,33.5]% | 0.181540 |
| CNRT 191; switch 51; 34% | [26.370757,27.034121]% | [33.5,34.5]% | 0.190173 |
| VAR 157; increase 39; 32% | [24.444444,25.239617]% | [31.5,32.5]% | 0.195637 |
| VAR 157; switch 41; 34% | [25.714286,26.517572]% | [33.5,34.5]% | 0.205366 |

Exact counts sum: 90 + 50 + 51 = 191; 77 + 39 + 41 = 157. Continuation fractions 90/191 and 77/157 reproduce 47% and 49%. The rescue percentages instead reproduce using 151 and 122: 50/151 = 33.1126%, 51/151 = 33.7748%, 39/122 = 31.9672%, 41/122 = 33.6066%. All four common-denominator gaps exceed 0.05.

**Necessary inputs available:** Every count, common population size, and printed percentage. **Exact missing inputs or definitions:** Explicit per-percentage denominator labels distinguishing full nonabstainers from rerandomized participants.

**Source-grounded alternative interpretation:** Continuation percentages use all nonabstainers, while rescue percentages deliberately use rerandomized participants; Figure 2 supplies these two possible denominators.

**Direct observation versus inferred explanation:** Printed percentages and denominator populations are observed; deliberate mixing versus production mechanism is inferred and unresolved.

**Classification rationale:** Retain REPORT/REPORT within main, S_W only, statistical_results; the relevant rule concerns counts within one display. **Classification ambiguity:** None in roles/relationships; denominator intent remains the human question.

**Evidence state:** reproduced. **Determining recheck fact:** Four count/percentage pairs do not reconcile with the abstract's stated 191/157-person populations beyond display precision, while continuation pairs do.

**Exact human question:** Should the four rescue allocation percentages be extracted using 191/157 full nonabstainers or 151/122 rerandomized participants, and which denominator is intended for each printed allocation percentage?

## C004 — Primary CNRT lower credible limit differs across locations

**Location found; source value/text matched:** REPORT [main p.1, CNRT Results](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1) assigns both rescue strategies an absolute RD 6%, 95% CrI 6%–11%. REPORT [main p.5, Smoking Cessation End of Phase 2, CNRT paragraph](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5) prints RD 6%, CrI 2%–11%, for both switching and dose increase.

**Comparator matched:** REPORT [supplement p.21, eTable 4](../../../joi240036supp2_prod_1716416466.01349.pdf#page=21) has CNRT increase-minus-stay 6% (2%–11%) and switch-minus-stay 6% (2%–10%). Both affected contrast rows were confirmed, not just the increase row.

**Consistency rule applicable; calculation and precision reproduced:** Focus B, route A category 2, matched primary interval-limit copies. Lower-limit intervals [5.5,6.5]% and [1.5,2.5]% leave gap 3 percentage points; relative gap to abstract 6% is 0.50. The 10%/11% upper-limit copies have touching [9.5,10.5]/[10.5,11.5] intervals, gap zero; that comparison does not add an issue.

**Necessary inputs available:** Time point, primary endpoint, baseline treatment, rescue contrasts, RD, credible level, and all compared limits. **Exact missing inputs or definitions:** Any different pooled posterior/interval calculation specifically intended by the combined abstract statement; posterior draws are absent but unnecessary to establish printed-copy disagreement.

**Source-grounded alternative interpretation:** The abstract may summarize a separately pooled rescue contrast or use a different interval construction. No such distinction is stated; the body and two table rows supply the alternative 2% lower limits.

**Direct observation versus inferred explanation:** The lower-limit disagreement is directly observed; a substituted digit or distinct posterior is an explanation, not an established mechanism.

**Classification rationale:** Retain S_C primary, all S_C/S_W, statistical_results: main-to-supplement and abstract-to-body interval comparisons concern numeric inference. **Classification ambiguity:** Different combined-versus-individual contrast construction is possible but undisclosed; all compared locations are REPORT.

**Evidence state:** reproduced. **Determining recheck fact:** Abstract lower limit 6% does not overlap or fall within 5% relative precision of the matched body/table lower limit 2%.

**Exact human question:** Which lower 95% credible limit applies to each primary CNRT rescue-versus-continuation RD, and was the abstract's 6%–11% interval produced from a distinct combined contrast?

## C005 — Primary varenicline-to-CNRT direction, sign, and attribution

**Location found; source value/text matched:** REPORT [main p.1, VAR Results](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1) prints RD −3% (−4% to −1%), followed by wording that continuation was worse than switching to a higher dosage; a separate next sentence assigns increased dosage RD 18%. REPORT [main p.5, VAR nonabstainer paragraph](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5) explicitly attaches −3% (−4% to −1%) to switching from VAR to CNRT relative to VAR continuation, but says continuing was worse than switching.

**Comparator matched:** REPORT [main p.7, Figure 3 VAR nonabstainer rows](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7) prints switch 0% (0%–0%), continuation 3% (1%–4%), and increase 20% (16%–26%). REPORT [supplement p.21, eTable 4 VAR switch-CNRT versus VAR-stay row](../../../joi240036supp2_prod_1716416466.01349.pdf#page=21) prints +3% (+1%–+4%) for the explicitly labeled switch-versus-stay contrast. [Main p.8, Discussion](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=8) additionally describes a 3% decrement between continuation 3% and switching 0%, corroborating the modeled direction rather than creating another candidate.

**Consistency rule applicable; comparison and precision reproduced:** Focus B, route A category 2. Signed point intervals [−3.5,−2.5]% and [2.5,3.5]% have gap 5, relative 5/3 = 1.666667. The negative body interval and positive table interval cannot share the same signed contrast convention. The displayed model switch and continuation probabilities order switch below continuation; the body benefit-direction sentence reverses that order. This uses printed model ordering, not a crude event fraction. The higher-dose abstract attribution is separately checked against the adjacent 18% higher-dose result.

**Necessary inputs available:** Explicit contrast labels, primary time point, signed effects/limits, group probabilities, and direction statements. **Exact missing inputs or definitions:** Table signed-versus-absolute ARD convention and the treatment/contrast intended by the abstract −3% sentence.

**Source-grounded alternative interpretation:** eTable 4 may present an unsigned magnitude or reversed subtraction, despite its switch-versus-stay label. The abstract may intend its later higher-dose contrast while attaching the −3% result. Neither supplies one coherent direction and contrast for all printed locations.

**Direct observation versus inferred explanation:** Signs, labels, group order, and narrative benefit direction are observed; missing-sign production and reversed-contrast convention remain explanations.

**Classification rationale:** Retain S_C primary, all S_C/S_W, statistical_results: signed numerical effects and their direction are focal even though the abstract also changes attribution. All compared content is REPORT. **Classification ambiguity:** Undefined unsigned/reversed ARD convention; no role ambiguity.

**Evidence state:** reproduced. **Determining recheck fact:** Matched switch-versus-continuation point estimates have opposite printed signs, and body benefit wording conflicts with its modeled ordering.

**Exact human question:** What signed contrast and treatment strategy does the primary −3% result denote, and is the +3% eTable 4 value a signed switch-minus-continuation effect, reversed contrast, or unsigned magnitude?

## C006 — Reported prespecified posterior criterion differs from plan

**Location found; source value/text matched:** PLAN [p.31, paragraph preceding Data Simulation Model](../../../joi240036supp1_prod_1716416466.00349.pdf#page=31) selects posterior probability ≥0.90 for sufficient evidence to advance to further evaluation; its inline formula uses >0.90. [Plan p.33, power prose](../../../joi240036supp1_prod_1716416466.00349.pdf#page=33) refers to detecting 0.90 benefit probability, and [p.34, Table 3](../../../joi240036supp1_prod_1716416466.00349.pdf#page=34) tabulates 0.80, 0.85, 0.90, and 0.95 options.

**Comparator matched:** REPORT [main p.4, Sample Size Determination and Statistical Analysis Plan](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4) describes more than 80% posterior probability as prespecified and sufficient to confirm hypotheses. REPORT [supplement p.9, first paragraph](../../../joi240036supp2_prod_1716416466.01349.pdf#page=9) calls ≥0.80 a prespecified confirmation criterion for clinical decisions/future trials, with >0.80 in the formula. REPORT [supplement p.18, eTable 2](../../../joi240036supp2_prod_1716416466.01349.pdf#page=18) also tabulates multiple cutoffs and mentions 0.90 in power prose; it does not separately select a prospective 0.80 rule.

**Consistency rule applicable; precision reproduced:** Focus D, route A category 5: analysis described as prespecified does not match the selected supplied plan rule. At common hundredth precision, intervals [0.895,0.905] and [0.795,0.805] have gap 0.09; relative to plan 0.90, 0.10 >0.05. The criterion is a design definition, so equality comparator glyphs are not used as an independent numeric issue. Searching the complete plan finds tabulated 0.80 scenarios but no separately selected 0.80 confirmation decision.

**Necessary inputs available:** Selected numeric cutoffs, their stated uses, and complete supplied plan. **Exact missing inputs or definitions:** An amendment or prospective distinction between 0.80 confirmation and 0.90 advancement decisions.

**Source-grounded alternative interpretation:** Confirmation in this study and advancement to a later confirmatory trial could be distinct decisions. Both supplied descriptions mention further evaluation/future trials, leaving that distinction unstated.

**Direct observation versus inferred explanation:** The selected cutoffs and prespecification claims are observed; a changed rule versus separate intended decisions is unresolved.

**Classification rationale:** Retain PLAN/REPORT, P_R only, protocol_report. Corroborating cutoff scenarios and matching power-table copies do not create additional within-report or plan relationships. **Classification ambiguity:** Distinct decision targets or an additional amendment may explain the comparison; roles are clear.

**Evidence state:** reproduced. **Determining recheck fact:** The report calls 0.80 prespecified, while the supplied plan explicitly selects 0.90 and contains no separate prospective 0.80 selection for the stated confirmation use.

**Exact human question:** Was the prespecified confirmation/future-evaluation cutoff 0.80 or 0.90, or did a prospective amendment define distinct confirmation and advancement decisions?

## C007 — Planned primary-model robustness analyses absent from reports

**Location found; source value/text matched:** PLAN [p.28, general analytic strategy and prior paragraphs](../../../joi240036supp1_prod_1716416466.00349.pdf#page=28) states that primary analyses use intention-to-treat with missing outcomes imputed as smoking; secondary analyses implement joint modeling of observed outcomes/missing data; sensitivity analyses evaluate robustness to missing data; nonignorable patterns are addressed through pattern-mixture methods; and optimistic and pessimistic/skeptical prior sensitivity analyses evaluate prior assumptions. These are prospective commitments in the strategy governing the abstinence model. Joint missing-data modeling and the robustness/prior analysis commitments are not qualified by baseline-covariate imbalance. The pattern-mixture component concerns nonignorable patterns if relevant; the recheck does not assume such patterns occurred.

**Comparator matched, including complete absence scope:** The entire supplied REPORT scope was examined in direct extraction: main physical pp.1–10 and supplement pp.1–36, not only selected search hits. Main [p.4, methods/intent-to-treat](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4), [p.7, secondary outcomes](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7), and [p.8, post hoc analyses/limitations](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=8) describe reported primary, secondary, and GEE pathway analyses. Supplement [pp.1–3, complete contents](../../../joi240036supp2_prod_1716416466.01349.pdf#page=1), [p.5](../../../joi240036supp2_prod_1716416466.01349.pdf#page=5), [p.6](../../../joi240036supp2_prod_1716416466.01349.pdf#page=6), [p.7](../../../joi240036supp2_prod_1716416466.01349.pdf#page=7), [p.8](../../../joi240036supp2_prod_1716416466.01349.pdf#page=8), [p.9](../../../joi240036supp2_prod_1716416466.01349.pdf#page=9), [p.10](../../../joi240036supp2_prod_1716416466.01349.pdf#page=10), [p.11](../../../joi240036supp2_prod_1716416466.01349.pdf#page=11), [p.12](../../../joi240036supp2_prod_1716416466.01349.pdf#page=12), and [p.13](../../../joi240036supp2_prod_1716416466.01349.pdf#page=13) cover all statistical method/results appendices. Supplement pp.14–18 contain design/outcome figures and simulation tables; pp.19–21 baseline/primary contrasts; pp.22–30 adverse events; pp.31–32 visit/medication compliance; pp.33–35 secondary contrasts and GEE pathways; p.36 references. None supplies results for the promised joint missing-data modeling, missingness robustness, or optimistic/pessimistic/skeptical prior sensitivity families. Full-scope searches for sensitivity, pattern-mixture, missingness, optimism/pessimism, skepticism, and robustness were followed by reading the methods, contents, and result-display identities, so this is not a search-only absence claim.

**Consistency rule applicable; logical comparison reproduced:** Focus D, route A category 5: prespecified primary-model robustness analyses are not reported in the supplied REPORT documents. Missing = smoking is the base analysis, not the promised joint-model/sensitivity result. The intercept-prior change on supplement p.8 is expressly to obtain convergence, and posterior predictive checking assesses fit; neither is identified as an optimistic/pessimistic/skeptical prior sensitivity comparison. The GEE pathways are expressly post hoc and estimate another quantity. Display precision does not apply to this analysis-status comparison.

**Necessary inputs available:** Prospective commitments and complete supplied report scope. **Exact missing inputs or definitions:** The named sensitivity/joint-model results, a disclosed replacement/amendment, and any condition under which the promised analyses were not applicable. No missing participant-level data are needed to establish that the supplied reports do not contain the results.

**Source-grounded alternative interpretation:** These analyses may have been performed but omitted, supplied elsewhere, or replaced by an amendment. The package establishes report absence only; it cannot establish whether they were performed. The general-strategy wording rather than a separate primary-endpoint sensitivity heading is retained as scope context.

**Direct observation versus inferred explanation:** Prospective commitments and absence of their results from the 46 supplied REPORT pages are observed. Nonperformance, effect on conclusions, and causes of omission are not inferred.

**Classification rationale:** Retain PLAN/REPORT, P_R only, protocol_report: this is a planned-versus-reported analysis-status comparison. It is not a method preference or an inferred failure of fitted results. **Classification ambiguity:** Additional outputs or amendments outside this supplied package are unknown; the pattern-mixture promise should not be described as evidence that nonignorable missingness occurred.

**Evidence state:** reproduced. **Determining recheck fact:** The unconditional robustness/joint-model/prior-analysis commitments are present, but their specified analysis results or disclosed replacement are absent from the complete supplied reports.

**Exact human question:** Where are the planned joint observed/missing-outcome analysis and missing-data and optimistic/pessimistic/skeptical-prior robustness results for the abstinence model, or what disclosed amendment or applicability condition explains their replacement or omission?

## C008 — EOT plus 30-day varenicline continuation denominator

**Location found; source value/text matched:** REPORT [main p.7, Secondary Outcomes of Abstinence](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7) describes among 157 phase-1 VAR nonabstainers the EOT+30 continuation result as 0%; n = 42. REPORT [supplement p.10, opening continuation of summarized analysis](../../../joi240036supp2_prod_1716416466.01349.pdf#page=10) repeats 0%; n = 42 for the same result.

**Comparator matched:** REPORT [supplement p.15, eFigure 2 final VAR nonabstainer-to-VAR row](../../../joi240036supp2_prod_1716416466.01349.pdf#page=15) prints 0/77, 0% (0%–0%); its caption calls the right-hand counts cell sample size. REPORT [main p.6, VAR continuation branch](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6) establishes 42 rerandomized plus 35 assigned = 77 primary continuers.

**Consistency rule applicable; precision reproduced:** Focus A, route B; matched secondary-result analysis-population size escapes the peripheral count exclusion. Half-unit size intervals [41.5,42.5] and [76.5,77.5] have gap 34; relative to narrative 42, 34/42 = 0.809524. Zero probability copies themselves reconcile and are not treated as an independent display-zero issue.

**Necessary inputs available:** Matched time point, treatment pathway, result and explicit narrative/figure sizes. **Exact missing inputs or definitions:** Whether n = 42 identifies the actually analyzed result population, only randomized members of a 77-person population, or a separate secondary analysis.

**Source-grounded alternative interpretation:** The narrative may list rerandomized participants while the figure includes assigned nonreturners. Main Figure 2 shows precisely these nested groups, but neither matched EOT+30 location explains that denominator convention or a switch of analysis population.

**Direct observation versus inferred explanation:** The 42/77 printed population-size comparison is observed; which population generated the reported posterior is not inferred.

**Classification rationale:** Retain REPORT/REPORT, S_C primary, all S_C/S_W, statistical_results: main-to-supplement and supplement-summary-to-figure population-size comparisons both occur. **Classification ambiguity:** The figure may show a full assigned cell while the prose reports only rerandomized membership; no source-role ambiguity.

**Evidence state:** reproduced. **Determining recheck fact:** The same EOT+30 VAR continuation result has two explicit extractable sample sizes, 42 and 77, without a stated secondary population distinction.

**Exact human question:** Was the EOT+30 VAR continuation posterior based on 42 rerandomized or 77 randomized-plus-assigned participants, and what does the narrative n = 42 represent if 77 was analyzed?

## C009 — Six-month CNRT summary probabilities and risk difference

**Location found; source value/text matched:** REPORT [main p.7, six-month Secondary Outcomes sentence](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7) describes CNRT dose increase (3%) and VAR dose increase (2%) providing benefit over continuation (0%) in both groups. REPORT [supplement p.10, six-month summarized analysis](../../../joi240036supp2_prod_1716416466.01349.pdf#page=10) repeats the CNRT+ 3%/continuation 0% reading. [Main p.1, final Results sentence](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1) designates six-month continuous abstinence as a reported secondary outcome.

**Comparator matched:** REPORT [supplement p.11, six-month CNRT detailed paragraph](../../../joi240036supp2_prod_1716416466.01349.pdf#page=11) prints switch 4%, increase 6%, continuation 3%, and increase-minus-continuation ARD 3% with 96% benefit probability. [Supplement p.16, eFigure 3 matched CNRT rows](../../../joi240036supp2_prod_1716416466.01349.pdf#page=16) confirms increase 3/50, 6% (4%–9%), and continuation 3/90, 3% (2%–5%). [Supplement p.33, eTable 9 six-month CNRT+ contrast](../../../joi240036supp2_prod_1716416466.01349.pdf#page=33) prints RD 3% (0%–6%) and benefit probability 96%.

**Consistency rule applicable; precision reproduced:** Focus B, route A category 2: the printed arm probabilities/readings differ in magnitude for a key secondary result. For increase, 3% ± 0.5 versus 6% ± 0.5 gives gap 2, relative 2/3 = 0.666667. For CNRT continuation, 0% ± 0.5 versus 3% ± 0.5 gives gap 2 against printed zero, reproducing under the zero-value rule. This compares matched model summaries rather than recomputing crude rates. If the summary percentages denote RDs, 3% can instead match eTable 9, but that changes the extracted quantity represented by those parenthetical percentages.

**Necessary inputs available:** Reported time point, model arm probabilities, summary labels, contrast RD and benefit probability. **Exact missing inputs or definitions:** Whether summary percentages represent arm probabilities, RDs, or mixed quantities, and whether continuation 0% refers only to VAR rather than both initial treatments.

**Source-grounded alternative interpretation:** The summary may express benefit magnitude above a zero reference, making CNRT 3% an RD; continuation 0% may intend only VAR. The neighboring VAR 2% can serve either probability or RD because its continuation is zero, while the CNRT distinction cannot be resolved numerically without defining the summary quantity.

**Direct observation versus inferred explanation:** Both sets of printed values/labels are observed. Conflation of RD with arm probability is an explanation, not established intent.

**Classification rationale:** Retain S_C primary, all S_C/S_W, statistical_results: the numeric probability/RD identity is focal, rather than merely wording. Both locations are REPORT; six months qualifies as key secondary because it appears in the abstract. **Classification ambiguity:** Summary quantity and continuation scope are undefined.

**Evidence state:** reproduced. **Determining recheck fact:** The summary's CNRT 3%/continuation 0% arm readings do not reconcile with detailed/figure 6%/3%; interpreting 3% as RD requires a different quantity definition.

**Exact human question:** Do the six-month summary percentages denote treatment-arm abstinence probabilities or risk differences, and does the 0% continuation statement apply to VAR alone or also to CNRT?

## C010 — Week-6 design intervals and generating beta distributions

**Location found; source value/text matched:** PLAN [p.31, Data Simulation Model](../../../joi240036supp1_prod_1716416466.00349.pdf#page=31) defines Figure 2 point estimates and 95% credible intervals as corresponding to its beta distributions. PLAN [p.32, Figure 2](../../../joi240036supp1_prod_1716416466.00349.pdf#page=32) prints CNRT week-6 0.48, 0.38–0.58, Beta(193,210); VAR week-6 0.50, 0.40–0.60, Beta(785,869).

**Comparator matched; every repeated and comparator box:** REPORT [supplement p.5, eFigure 1 description](../../../joi240036supp2_prod_1716416466.01349.pdf#page=5) gives the same distribution-to-summary definition. REPORT [supplement p.14, eFigure 1](../../../joi240036supp2_prod_1716416466.01349.pdf#page=14) repeats both affected week-6 boxes and all eight week-12 boxes. Every one of these ten boxes was read in both figures. The eight same-method comparator boxes, shown below, occur on both PLAN p.32 and REPORT p.14; ordering differs for two CNRT rescue rows but treatment labels match.

**Consistency rule applicable; calculation and precision reproduced:** Focus D for PLAN and C for REPORT, route A category 4: printed intervals do not reproduce under the distribution method that reproduces the other boxes. Exact qbeta(.025,.975) gives CNRT [0.430320464,0.527694225] and VAR [0.450581241,0.498690952]. Allowing each integer beta shape ±0.5 gives:

| Affected box | Recomputed lower envelope | Printed lower interval | Relative gap | Recomputed upper envelope | Printed upper interval | Relative gap |
|---|---|---|---:|---|---|---:|
| CNRT week 6 | [0.429090867,0.431550363] | [0.375,0.385] | 0.116029 | [0.526454098,0.528934051] | [0.575,0.585] | 0.079424 |
| VAR week 6 | [0.450280035,0.450882456] | [0.395,0.405] | 0.113200 | [0.498388256,0.498993640] | [0.595,0.605] | 0.160011 |

All four endpoint gaps exceed 0.05. Independent pbeta coverage of printed week-6 ranges is 0.9999500444 for CNRT and 0.9999999996 for VAR, not 0.95. Equal-tail convention is independently supported by the eight comparison boxes; no empirical simulation realization is substituted for the stated beta inputs.

| Week-12 comparator box, in both figures | Printed point; limits; beta shapes | Exact qbeta lower/upper | Relative remaining lower/upper gaps after each input's displayed precision |
|---|---|---|---|
| CNRT responder continuation | 0.50; 0.40–0.60; (47.3,47.3) | 0.400000185 / 0.599999815 | 0 / 0 |
| CNRT nonresponder continuation | 0.02; 0.0007–0.0978; (1.02,35.48) | 0.000773798 / 0.099786534 | 0.011878 / 0.017019 |
| CNRT nonresponder switch to VAR | 0.40; 0.25–0.57; (14.4,21.5) | 0.249238653 / 0.563431726 | 0 / 0.000277 |
| CNRT nonresponder increase | 0.20; 0.10–0.34; (8.90,34.6) | 0.099982998 / 0.334863059 | 0 / 0 |
| VAR responder continuation | 0.75; 0.65–0.83; (62.2,21.0) | 0.649542760 / 0.834381659 | 0 / 0 |
| VAR nonresponder continuation | 0.15; 0.05–0.30; (4.35,23.1) | 0.050067649 / 0.313547295 | 0 / 0.026139 |
| VAR nonresponder switch to CNRT | 0.20; 0.15–0.26; (42.8,170.0) | 0.150159095 / 0.257414844 | 0 / 0 |
| VAR nonresponder increase | 0.40; 0.26–0.55; (17.3,25.7) | 0.262529872 / 0.550732379 | 0 / 0 |

The complete half-unit envelopes, including median envelopes, are preserved in `preprocessing/evidence_rechecker/calculations.txt`. All eight comparator point estimates reconcile with their qbeta medians within display precision. The week-6 VAR median 0.4745968 versus point 0.50 leaves a relative precision gap about 0.0402, at most 0.05; it is not an additional reproduced point discrepancy. The earlier 0.0285 VAR-continuation-upper calculation uses fixed exact shapes; allowing their displayed half-unit intervals gives the more conservative 0.026139 above, with the same precision conclusion.

**Necessary inputs available:** Explicit distribution family/shapes, 95% interval claim, exact box labels, and eight supporting method comparisons. **Exact missing inputs or definitions:** Whether the two week-6 intervals came from other beta shapes, a different uncertainty distribution, or a separate summary construction; the exact realized simulation inputs/code are absent. A new power value cannot be computed from these checks alone.

**Source-grounded alternative interpretation:** Week-6 boxes may combine historical anticipated ranges with separately selected simulation shapes. Both texts instead state correspondence, so that distinction requires clarification.

**Direct observation versus inferred explanation:** Printed beta shapes/limits and qbeta/pbeta incompatibility are observed. Which parameters were used in power simulations and any replacement power result are not inferred.

**Classification rationale:** Retain primary P_P, all P_P/S_W, plan_material. There is a distribution-to-summary inconsistency within the plan, repeated within the report; agreement between the two documents does not create P_R or S_C. P_P precedes S_W. **Classification ambiguity:** The supplement remains REPORT by content; an unstated historical-range/simulation-shape distinction is possible.

**Evidence state:** reproduced. **Determining recheck fact:** Both week-6 boxes, on both source pages, retain four endpoint gaps above 0.05, while all eight same-method comparator boxes reconcile under the specified precision rule.

**Exact human question:** Which beta inputs or separate interval construction generated the two week-6 95% design intervals, and which of the printed distributions/ranges were used in the primary sample-size/power simulations?

## C011 — Revised normal prior variance and printed odds interval

**Location found; source value/text matched:** REPORT [supplement p.7, initial coefficient-prior paragraph](../../../joi240036supp2_prod_1716416466.01349.pdf#page=7) and [p.8, first prior paragraph](../../../joi240036supp2_prod_1716416466.01349.pdf#page=8) define the original Normal(mean 0, variance 1 × 10^6) and approximate 95% log limits −1960 to 1960. P.8's model-fitting paragraph changes the intercept to Normal(mean 0, variance 10) on the log scale.

**Comparator matched:** The same [p.8 model-fitting paragraph](../../../joi240036supp2_prod_1716416466.01349.pdf#page=8) claims the revised 95% prior interval for intercept odds is 3.07 × 10^−9 to 325,215,956, and explains that treatment-coefficient priors remained unchanged and posterior predictive checking indicated fit.

**Consistency rule applicable; calculation and precision reproduced:** Focus C, route B: the defined prior does not generate its stated interval. The original variance gives qnorm(.975) × 1000 = 1959.963984, consistent with ±1960. Revised variance 10 gives exp(±1.959963984 × sqrt(10)) = [0.002033594579,491.7400991]. Allowing variance [9.5,10.5] gives lower envelope [0.001744985241,0.002379143534] and upper [420.3193232,573.0707494]. The printed lower interval is [3.065,3.075] × 10^−9; upper [325215955.5,325215956.5]. Relative remaining lower gap exceeds 568000; upper gap is about 0.99999824. Even additionally allowing printed mean 0 a conservative half-unit interval [−0.5,0.5] gives lower [0.00105838705,0.00392254455] and upper [254.9365564,944.8339342]; remaining relative gaps still exceed 344000 and 0.99999709. Thus interpreting zero as an exact defined prior center is unnecessary to the conclusion.

An SD of 10 gives exact odds [3.075987511 × 10^−9,325098849.2]; the approximation ±1.96 × 10 gives about [3.07488 × 10^−9,325215956.1]. This supplies a bounded alternative specification, not an assigned replacement prior.

**Necessary inputs available:** Distribution, log scale, mean/variance, 95% level, and stated exponentiation mapping. **Exact missing inputs or definitions:** Whether the implemented intercept normal prior used variance 10, SD 10/variance 100, or another parameter convention; fitted code is absent.

**Source-grounded alternative interpretation:** The numerical odds limits are consistent within scope precision with an SD near 10 rather than variance 10. A different prior parameterization may have been intended. The reported convergence-driven revision does not select which numeric convention was implemented.

**Direct observation versus inferred explanation:** The variance-to-odds interval inconsistency is observed; a variance/SD parameter mix and any effect on posterior results are not established.

**Classification rationale:** Retain REPORT/REPORT within supplement, S_W only, statistical_results. The plan's historical original prior merely corroborates original context and does not create P_R. **Classification ambiguity:** Implemented variance-versus-SD convention is absent; document role is clear.

**Evidence state:** reproduced. **Determining recheck fact:** Normal variance 10 cannot generate either stated odds endpoint, even with conservative half-unit variance and mean allowances.

**Exact human question:** Did the implemented revised intercept prior use variance 10, SD 10, or another convention, and which definition generated the stated 95% prior odds interval?

## C012 — Repeated EOT plus 30-day decimal-scale discrepancies

**Location found; source value/text matched; every comparator matched:** All seven affected occurrences were read visually and in fresh direct extraction. Every paired result matches treatment pathway, EOT+30 time point, probability-versus-ARD identity, and contrast.

| Occurrence | Direct REPORT narrative location and printed reading | Direct REPORT comparator and printed reading |
|---|---|---|
| 1 | [Supplement p.10, CNRT nonabstainer switch probability](../../../joi240036supp2_prod_1716416466.01349.pdf#page=10): 1.0% (7.0%–1.3%) | [P.15, eFigure 2 CNRT nonabstainer→VAR](../../../joi240036supp2_prod_1716416466.01349.pdf#page=15): 10% (7%–13%); p.9 summarized narrative also prints 10% |
| 2 | [P.10, same CNRT probability sentence, increase](../../../joi240036supp2_prod_1716416466.01349.pdf#page=10): 8.0% (5.0%–1.1%) | [P.15, eFigure 2 CNRT nonabstainer→CNRT+](../../../joi240036supp2_prod_1716416466.01349.pdf#page=15): 8% (5%–11%) |
| 3 | [P.10, CNRT switch-minus-continuation ARD](../../../joi240036supp2_prod_1716416466.01349.pdf#page=10): 6.0% (3.0%–1.0%) | [P.33, eTable 9 EOT+30 CNRT VAR-switch column](../../../joi240036supp2_prod_1716416466.01349.pdf#page=33): 6% (3%–10%) |
| 4 | [P.10, final VAR nonabstainer probability sentence, increase](../../../joi240036supp2_prod_1716416466.01349.pdf#page=10): 8.0% (5.0%–1.1%) | [P.15, eFigure 2 VAR nonabstainer→VAR+](../../../joi240036supp2_prod_1716416466.01349.pdf#page=15): 8% (5%–11%) |
| 5 | [P.11, first paragraph, VAR increase-minus-continuation ARD](../../../joi240036supp2_prod_1716416466.01349.pdf#page=11): 8.0% (5.0%–1.1%) | [P.33, eTable 9 EOT+30 VAR+ column](../../../joi240036supp2_prod_1716416466.01349.pdf#page=33): 8% (5%–11%) |
| 6 | [P.11, second paragraph, VAR increase-minus-switch ARD](../../../joi240036supp2_prod_1716416466.01349.pdf#page=11): 8.0% (5.0%–1.1%) | [P.34, eTable 10 EOT+30 VAR column](../../../joi240036supp2_prod_1716416466.01349.pdf#page=34): 8% (5%–11%) |
| 7 | [P.11, phase-1 abstainers paragraph, CNRT versus VAR ARD](../../../joi240036supp2_prod_1716416466.01349.pdf#page=11): 1.1% (−1.0%–22%) | [P.35, eTable 11 EOT+30 row](../../../joi240036supp2_prod_1716416466.01349.pdf#page=35): 11% (−1%–22%), probability 97% |

**Consistency rule applicable; calculation and precision reproduced:** Focus B, route A categories 1 and 2. Occurrences 1–6 have reversed endpoint order; their points lie outside even the numerically ordered printed endpoint range. For occurrence 1, [1.3,7.0] cannot contain 1.0; for occurrences 2/4/5/6, [1.1,5.0] cannot contain 8.0; for occurrence 3, [1.0,3.0] cannot contain 6.0. These containment observations are independent of rounding. Printed-copy gaps also reproduce:

| Compared numeric copies, percentage points | Reference interval | Comparator interval | Gap | Relative gap | Occurrences |
|---|---|---|---:|---:|---|
| 1.0 vs 10 | [0.95,1.05] | [9.5,10.5] | 8.45 | 8.45 | 1 point; 3 upper limit |
| 1.3 vs 13 | [1.25,1.35] | [12.5,13.5] | 11.15 | 8.576923 | 1 upper limit |
| 1.1 vs 11 | [1.05,1.15] | [10.5,11.5] | 9.35 | 8.50 | 2/4/5/6 upper limits; 7 point |

All other matched point/limit copies in these rows overlap within their own displayed precision: e.g., 8.0/8, 5.0/5, 6.0/6, 3.0/3, −1.0/−1 and 22/22. They are not additional differences.

**Necessary inputs available:** All printed points/limits, matching figure/table values, credible level, and contrast labels. **Exact missing inputs or definitions:** Intended narrative scales and any separately fitted narrative analysis. No such distinct model is disclosed for these copies; posterior draws are absent but unnecessary for the printed containment/copy comparisons.

**Source-grounded alternative interpretation:** The figure/table readings provide a plausible alternative decimal scale for every affected value. A distinct narrative model could explain some cross-location values, but would not reconcile the narrative's own endpoint ordering/containment.

**Direct observation versus inferred explanation:** Seven numeric and six containment/order discrepancies are observed; a shared decimal-production mechanism is inferred, not established. The six-month responder interval in overlapping F-XS-003/F-ST1-003 provenance remains separately represented by C013, with its own rule and question rather than being silently omitted.

**Classification rationale:** Retain S_W only, statistical_results: every focal numeric comparison and containment check occurs in one REPORT supplement. The main's summarized counterparts merely corroborate some comparator values and are not required conflicting relationships. **Classification ambiguity:** None in content roles or relationship identity; intended scale/model remains undefined.

**Evidence state:** reproduced. **Determining recheck fact:** All seven registered printed occurrences are present; each has at least one matched-copy gap above 0.05, and the first six additionally fail printed interval ordering/containment.

**Exact human question:** For all seven EOT+30 narrative occurrences, which printed point estimates and credible limits are intended, and do the narrative, eFigure 2 and eTables 9–11 represent the same model/contrast outputs?

## C013 — Six-month responder credible limits differ across locations

**Location found; source value/text matched:** REPORT [supplement p.12, Continuous Abstinence at 6 months for Abstainers](../../../joi240036supp2_prod_1716416466.01349.pdf#page=12) prints CNRT/VAR arm probabilities 39%/40%; difference probability 55%; ARD 1.0% (−1.3%–1.1%), with wording of a small VAR benefit.

**Comparator matched:** REPORT [supplement p.35, eTable 11 six-month Continuous Abstinence row](../../../joi240036supp2_prod_1716416466.01349.pdf#page=35) prints ARD 1% (−11%–12%), probability 56%, under the column heading ARD for CNRT vs VAR. [P.16, eFigure 3 responder rows](../../../joi240036supp2_prod_1716416466.01349.pdf#page=16) confirms the same six-month responder arm identities and 39%/40% probabilities. The p.12/p.35 component of F-XS-003/F-ST1-003 is retained as additional provenance to canonical F-NUM-007.

**Consistency rule applicable; precision reproduced:** Focus B, route A category 2, matched credible-limit magnitudes. Lower intervals [−1.35,−1.25]% and [−11.5,−10.5]% leave gap 9.15, relative to 1.3 is 7.038462. Upper intervals [1.05,1.15]% and [11.5,12.5]% leave gap 10.35, relative to 1.1 is 9.409091. The point copies 1.0/1 overlap, and probability intervals 55 ±0.5 and 56 ±0.5 touch; they have zero gap. This occurrence has ordered limits and an in-interval point, so containment is not its determining rule. Multiplying the narrative limits by ten gives −13/+11, not the table −11/+12; sign reversal alone also fails to reconcile their widths.

**Necessary inputs available:** Six-month responder population, matched ARD, credible limits, and probability values. **Exact missing inputs or definitions:** Which credible interval and contrast orientation are intended; whether distinct posterior models or interval constructions generated the two displays.

**Source-grounded alternative interpretation:** A distinct analysis, summary definition, or contrast orientation may apply. Different direction wording is present, but cannot by itself explain the order-of-magnitude width comparison.

**Direct observation versus inferred explanation:** Limit magnitudes/widths are observed; the EOT+30 production explanation is not assumed for this distinct occurrence.

**Classification rationale:** Retain REPORT/REPORT within supplement, S_W only, statistical_results: credible-limit extraction is focal. Figure p.16 supplies population context without adding a different document relationship. **Classification ambiguity:** Contrast direction and interval construction are unstated.

**Evidence state:** reproduced. **Determining recheck fact:** Both credible-limit pairs differ beyond 0.05 under half-unit intervals, independently of the point/probability copies that reconcile within precision.

**Exact human question:** Which 95% credible interval and subtraction direction apply to the six-month CNRT-versus-VAR responder contrast, and did the narrative and eTable 11 use different models or interval constructions?

## C014 — Augmented-CNRT dose attached to the primary-design input

**Location found; source value/text matched:** REPORT [supplement p.14, eFigure 1 caption and CNRT+ week-12 cell](../../../joi240036supp2_prod_1716416466.01349.pdf#page=14) defines dose increase as two 21-mg patches plus 4-mg lozenges, attaching CNRT+ to the anticipated primary-outcome input 0.20, interval 0.10–0.34, Beta(8.90,34.6).

**Comparator matched; every cited regimen location:** REPORT [supplement p.17, eTable 1 caption](../../../joi240036supp2_prod_1716416466.01349.pdf#page=17) defines CNRT+ as two 21-mg patches plus 2-mg lozenges for the simulation results. [Supplement p.18, eTable 2 caption](../../../joi240036supp2_prod_1716416466.01349.pdf#page=18) repeats the 2-mg simulation-table definition. [P.15, eFigure 2 caption](../../../joi240036supp2_prod_1716416466.01349.pdf#page=15) and [p.16, eFigure 3 caption](../../../joi240036supp2_prod_1716416466.01349.pdf#page=16) define the two-patch plus lozenge pathway without specifying lozenge mg; they provide pathway context only. REPORT [main p.4, first medication paragraph](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4) explicitly continues 2-mg phase-1 lozenges with increased patches; [main p.7, Figure 3 caption](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7) repeats 2 mg. [Main p.8, second limitation](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=8) states that use of 2-mg rather than 4-mg lozenges was a practical choice. PLAN [p.25, medication paragraph](../../../joi240036supp1_prod_1716416466.00349.pdf#page=25) corroborates purchase/use of 2-mg lozenges; it does not supply a conflicting planned design input for this candidate. This caption-specific clarification follows the independent audit's direct visual reread; the focal 4-mg and explicit 2-mg comparators remain reproduced.

**Consistency rule applicable; precision reproduced:** Focus D/C-related primary-design intervention identity, route B. Integer printed dose intervals [3.5,4.5] mg and [1.5,2.5] mg have gap 1 mg; relative to the focal 4-mg copy, 1/4 = 0.25 >0.05. The comparison concerns which intervention the primary-design probability/distribution denotes, not matching anticipated 0.20 to an observed outcome or inferring a dose-dependent power change.

**Necessary inputs available:** Numeric caption dose, same CNRT+ pathway/cell identity, simulation-table regimen definitions, and actual report regimen. **Exact missing inputs or definitions:** Whether the anticipated design distribution assumed 4-mg lozenges historically or 2-mg lozenges as defined in the simulation tables, and any disclosed change relating those assumptions.

**Source-grounded alternative interpretation:** The anticipated figure could retain a historical 4-mg regimen while the trial and other simulation displays use 2 mg. The main limitation establishes the actual 2-mg choice, but neither resolves which regimen the anticipated beta input represents.

**Direct observation versus inferred explanation:** Caption/table dose readings are observed; a historical-dose assumption or carryover mechanism is not established. No change in effect or power is inferred.

**Classification rationale:** Retain S_C primary, all S_C/S_W, report_internal_inconsistency: the numerical dose assigns a primary-design value to a different intervention identity across REPORT locations. The plan only corroborates one side, so P_R does not apply. **Classification ambiguity:** Historical anticipated dose versus implemented trial/simulation-table dose is possible; the supplement remains REPORT by content.

**Evidence state:** reproduced_after_transcription_correction. **Determining recheck fact:** eFigure 1 attaches 4-mg lozenges to the CNRT+ design input, while its matched simulation-table and trial regimen definitions specify 2 mg beyond display precision.

**Exact human question:** Did the CNRT+ anticipated probability 0.20 and Beta(8.90,34.6) design input assume 4-mg or 2-mg lozenges, and how does that assumption relate to the 2-mg regimen in the simulation tables and trial?

## Completion and remaining supplied-input limits

All 14 assigned IDs have a separately recorded location/value/comparator/rule/calculation/precision/input/alternative/observation/question record, exactly one evidence state, and content-grounded classification. No assigned repeated location remains unexamined. The complete 46-page REPORT scope was used for C007; the complete PLAN text was also searched for the prospective assignment/decision definitions relevant to C001/C006. At initial recheck handoff no transcription change was recorded; the subsequent independent audit corrected C014 comparator-caption specificity on supplement pp.15–16 as documented above. Its evidence state is reproduced_after_transcription_correction. Extra corroborating locations are explicitly distinguished from relationships.

Remaining human inputs are issue-specific: prospective assignment/amendment policy (C001); assigned-observation model weights/coding (C002); allocation denominator definitions (C003); primary interval construction (C004); signed contrast convention/attribution (C005); selected decision/amendment rule (C006); robustness outputs/applicability/amendment (C007); secondary analysis-population convention (C008); summary probability/RD identity (C009); beta-summary construction and simulation inputs (C010); implemented prior parameter convention (C011); intended EOT+30 narrative scales/model identity (C012); six-month interval/contrast construction (C013); anticipated CNRT+ lozenge-dose assumption (C014). Fitted model code, posterior draws, participant-level data, and additional amendments are not supplied. Their absence does not prevent reproducing the recorded printed/logical comparisons, but prevents choosing among the bounded alternatives. No severity, validity, disposition, or final corrected value is assigned.
