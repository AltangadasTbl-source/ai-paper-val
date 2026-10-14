# Mechanical evidence recheck

Runtime: `agent:/root/evidence_recheck`; fresh `qc162_evidence_rechecker`, run model `gpt-6.1-sol`, high reasoning effort. Assigned stable scope: **C001, C002, C003**. All three IDs remain **Pending Human Adjudication**. This artifact records source and comparison facts; it assigns no human disposition.

The complete role preset, `QUALITY_CONTROL_SCOPE.md`, `workflow_1_6_2/review_contract.md`, current-run candidate ledger and initial inclusion screen were read. Direct supplied PDFs are final authority. Current-run native text and page renders were used to locate and inspect their content; legacy OCR/text and earlier review conclusions were not evidence authorities.

## Source identity, inspection and tooling

Direct `sha256sum` at this stage reproduced the current source-inventory hashes:

| Source | Content role | SHA-256 |
|---|---|---|
| Main article | REPORT: a completed randomized-trial article with observed results, tables and figures | `10ab2f532b03f65d1d84bc8e8a2a3a14e3b24a76f204123acd7049d67f7b73e3` |
| Protocol | PLAN: iSEARCH Protocol V2.1, prospective conduct and analysis specifications | `4d21c2d519df3a518ed23afdba74b221ae035e19222f7230081bb63d6f28221f` |
| SAP | PLAN: prospective statistical-analysis specifications and proposed table shells, with a blinded-preparation declaration | `413d12db69bc43aa875801ea986fb6316a4511874b393ed8a71782ddb000e5b0` |
| Results supplement | REPORT: observed sensitivity, site-specific and side-effect results | `16131dae3f154fd78dc8058b1b4203cdeda5a26f2fe4939365651305e80e6e80` |

Native extraction and rendering used the recorded package-local fallback interpreter `.ai_paper_validation/review_1_6_2/tooling/venv/bin/python`, `workflow_1_6_2/scripts/pdf_tools.py`, PyMuPDF **1.26.4**, **CPU**. Direct PDF extraction/rendering tools are absent according to `tooling_record.md`. That record permits user-approved RapidOCR/CUDA when OCR is needed; readable native text and visual inspection sufficed here, so no OCR was run.

Fresh derivatives owned by this stage, all under `../preprocessing/evidence_recheck/`:

| Derivative | Exact supplied-source scope | Engine/device |
|---|---|---|
| `main-native.txt` | Main PDF pp.1–11, native extraction of every page | PyMuPDF 1.26.4 native text, CPU |
| `results-native.txt` | Results PDF pp.1–6, native extraction of every page | PyMuPDF 1.26.4 native text, CPU |
| `sap1-4-native.txt` | SAP PDF pp.1–4, cover, contents, revision/approval material | PyMuPDF 1.26.4 native text, CPU |
| `protocol22-native.txt` | Protocol PDF p.22, amendment context | PyMuPDF 1.26.4 native text, CPU |
| `main4.png`, `main6.png` | Main PDF pp.4 and 6 | PyMuPDF 1.26.4 render, 150 dpi, CPU |
| `protocol20.png` | Protocol PDF p.20 | PyMuPDF 1.26.4 render, 150 dpi, CPU |
| `sap4.png`, `sap12.png`, `sap13.png`, `sap14.png`, `sap29.png` | SAP PDF pp.4, 12, 13, 14, 29 | PyMuPDF 1.26.4 render, 150 dpi, CPU |

Commands were `pdf_tools.py text SOURCE --first N --last N OUTPUT` and `pdf_tools.py render SOURCE --page N OUTPUT --dpi 150`. The helper returned the engine and selected page/range for every derivative. Eight pages were newly rendered. Current-run 200-dpi CPU renders in `../preprocessing/inclusion_initial/` were also visually inspected: `main3.png`, `main7.png`, `main8.png`, `protocol17.png`, `protocol21.png`, `sap25.png`, `sap26.png`, `results2.png`. Their documented source/page generation matches the current identity; page titles, page numbers, row labels and adjacent text were checked visually. Current-run native/sorted text for protocol pp.17–21 and SAP pp.10–14 and 25–29 served as locators for these directly inspected pages. No source or pre-existing derivative was modified.

## Classification and evidence-state summary

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Classification action and determining recheck fact |
|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | REPORT main article and results supplement versus PLAN protocol and SAP | reproduced | Classification confirmed. SAP specifies a separately prognostic-adjusted primary model, main says it was undertaken, and all supplied REPORT output labels fail to identify its treatment-effect result. |
| C002 | protocol_report | P_R | P_R | REPORT main article versus PLAN protocol and SAP | reproduced | Classification confirmed. Both plans require ten-component adjusted P values; main expressly states no multiple-testing adjustment and Table 3 has no adjusted-P output. |
| C003 | protocol_report | P_R | P_R | REPORT main article versus PLAN protocol; SAP is corroborating PLAN context | reproduced | Classification confirmed. Protocol says one or more previous cesareans; report repeatedly specifies the preceding pregnancy. The later blinded SAP matches the report but supplies no criterion-specific reconciliation. |

No transcribed value or originally cited page required replacement. The additional main p.7 repetition for C003 is retained below. It expands the occurrence list without changing an originally transcribed statement or location. `P_R` is the sole relationship for each bounded registered issue, so precedence `P_R > P_P > S_C > S_W` is satisfied without adding corroborating document pairs as relationships.

## C001 — Planned prognostic-adjusted primary result is not identified

**Evidence state: reproduced.** **Review domain: protocol_report. Relationship type: P_R. All relationships: P_R.** Qualifying route carried by the registration: **Route A, category 5**; focus C/D. Status: **Pending Human Adjudication**.

### Location found; source and comparator matched

Every registered page was found. The following table distinguishes planned inputs, the report's undertaking statement, and the results inspected for the specified output.

| Exact location | Role confirmed from content | Printed text/value matched and its comparison function |
|---|---|---|
| [Protocol PDF p.20, §13.2](../../../joi250034supp1_prod_1750956984.09018.pdf#page=20) | PLAN | Primary analyses will be unadjusted. Where baseline differences between groups might be associated with outcomes, secondary primary-outcome analyses will use multiple log-binomial regression. The conditional clause is retained; this page alone does not establish that its condition occurred. |
| [SAP PDF p.12, §3.2, printed lines 399–401](../../../joi250034supp2_prod_1750956984.11521.pdf#page=12) | PLAN | Secondary analyses of the primary outcome will include adjustment for relevant baseline prognostic factors using multiple log-binomial or robust Poisson regression. No baseline-imbalance condition appears in this SAP commitment. |
| [SAP PDF p.13, §3.9, printed lines 442–450](../../../joi250034supp2_prod_1750956984.11521.pdf#page=13) | PLAN | Multivariable prognostic analysis of the primary endpoint is specified. Variables: small for gestational age, preeclampsia, delivery method for previous pregnancy (no prior delivery, spontaneous vaginal, instrumental vaginal, cesarean), and postnatal fetal anomaly. Robust modified Poisson or another computational method is available on log-binomial nonconvergence; multiple birth is included if a GEE cannot be fitted. |
| [SAP PDF p.26, Table 12, printed lines 542–544](../../../joi250034supp2_prod_1750956984.11521.pdf#page=26) | PLAN | Separate multivariable composite-primary-endpoint shell: treatment and the prognostic rows, including multiple pregnancy, with parameter estimate, RR/95% CI and P-value columns. Footnote: robust Poisson model. It is a proposed table, with no observed fitted values. |
| [Main PDF p.3, Statistical Analysis](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=3) | REPORT | Primary model is GEE log-binomial accounting for multifetal clustering. Separately, secondary primary-outcome analysis “was undertaken,” including prognostic adjustment using robust modified Poisson regression. This is a positive undertaking statement. |
| [Main PDF p.6, Primary and Secondary Outcomes paragraph](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=6) | REPORT | Primary RR 1.02 (95% CI 0.75–1.37) is described as adjusted for multifetal clustering. Missing cord-pH sensitivities: imputed RR 1.01 (0.75–1.36); adjusted-for RR 0.98 (0.73–1.31), expressly referred to eTable 1. The paragraph does not label a prognostic-adjusted result. |
| [Main PDF p.7, Table 3 and outcome paragraphs](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=7) | REPORT | Primary 83/1625 versus 84/1625, RR 1.02 (0.75–1.37), P=.91. Table footnote associates estimates with GEE accounting for multiple births. Component outcomes and site-result narrative follow; no separate prognostic model is identified. |
| [Main PDF p.8, Figure 2 and Table 4](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=8) | REPORT | Figure overall RR 1.02 (0.75–1.37) is GEE log-binomial; subgroup effects are GLM log-binomial. Table 4 contains tertiary outcomes, with infant-level GEE footnote. Neither labels the multivariable primary model in SAP Table 12. |
| [Results PDF p.2, eTable 1, all six analysis families and footnotes](../../../joi250034supp3_prod_1750956984.12018.pdf#page=2) | REPORT | Composite imputed/GEE RR 1.01 (0.75–1.36), P=.943; imputed cord-pH RR 1.62 (0.68–3.85), P=.276; nine-component/GEE RR 0.96 (0.70–1.31), P=.796; ten-component/GLM RR 0.99 (0.74–1.33), P=.937; ten-component/GLM cord-testing-indicator RR 0.98 (0.73–1.31), P=.882; imputed ten-component/GLM cord-testing-indicator RR 0.97 (0.73–1.30), P=.844. Footnotes positively identify log-binomial GEE/GLM and the Cord Artery testing ‘Not Done’ covariate. None identifies the SAP prognostic set or a robust-Poisson result. |

**Complete supplied REPORT absence search:** Fresh native extraction covered main pp.1–11 and results pp.1–6, with readable text on every page. Searches for prognostic/adjusted/adjustment/Poisson/model/regression/sensitivity and result labels were evaluated with their adjacent paragraphs, tables and footnotes, including line-broken “prog-nostic.” Main p.1 contains the abstract's primary effect; p.2 is introduction/early methods; pp.3–4 are analysis methods and flow; p.5 is baseline Table 1; p.6 is Table 2 and primary narrative; p.7 is Table 3 and results/discussion; p.8 is Figure 2/Table 4; p.9 is discussion/limitations/conclusions; pp.10–11 are article information/references. Results p.1 indexes its three eTables; p.2 is the sensitivity table; pp.3–5 contain site-specific outcome results; p.6 contains side effects. All displayed primary-effect model families were compared, rather than relying on a failed search for one word. A bibliography entry for a prognostic-reporting guideline is not current-trial model output. The supplied REPORT scope contains no identified prognostic-adjusted primary treatment RR/CI.

### Rule, logical reproduction and display precision

**Consistency rule applicable:** Match the primary composite, treatment contrast and model/covariates to the separately prespecified prognostic analysis; under Route A category 5, a planned primary analysis whose output is not reported is a registered comparison. Do not identify a model merely because its label contains “adjusted.”

**Logical comparison reproduced:** (1) SAP §§3.2/3.9 and Table 12 establish the distinct planned multivariable analysis. (2) Main p.3 says it was undertaken. (3) Main Table 3 and Figure 2 identify the overall result as the primary GEE, while eTable 1 identifies missing-pH/cord-testing-indicator sensitivities. (4) The remaining REPORT pages contain no output mapping to the separate prognostic model. Thus the registered absence of an identified result remains. The observation does not assert that an undocumented fit omitted a covariate or that the fitted result would differ from the primary GEE.

**Display-precision interval check:** The registered comparison is categorical model/output identification; no printed-versus-recomputed numeric discrepancy is alleged, so a recomputed interval and relative discrepancy are **not applicable**. As a cross-check on numerical locators, the primary RR 1.02 repeated in the main gives [1.015, 1.025] at two-decimal precision; its CI endpoints give [0.745, 0.755] and [1.365, 1.375]. Corresponding printed copies overlap, gap 0, relative discrepancy 0. Main p.6 RR 0.98 and eTable 1's RR 0.98 both give [0.975, 0.985]; CI copies also overlap, gap 0. Rounding cannot establish that the cord-testing-indicator model is the specified prognostic model. No `S_C` or `S_W` numeric conflict follows from these copies.

### Inputs, alternatives, observation and human question

**Necessary inputs available:** The planned outcome, treatment contrast, named prognostic set, conditional fallback structure, proposed output table, undertaking sentence, and complete supplied REPORT output labels are available. They suffice to reproduce output nonidentification.

**Exact missing inputs or definitions:** The actual prognostic-model coefficient/RR, confidence interval, fitted covariate set, fitting/convergence record and a mapping from any printed result to that fitted model are unavailable. An analysis-specific amendment withdrawing or changing this commitment is not identified. These are not inputs needed to establish which outputs the supplied documents identify; they are needed to select an explanation or reproduce the fitted analysis.

**Source-grounded alternatives:** Output may have been omitted after fitting; a supplied but differently labelled result may be intended to represent the model; a prospective change may have altered the analysis. The protocol's baseline-imbalance condition could limit its own adjustment commitment, but it does not condition the SAP commitment and does not reconcile the article's undertaking statement. The SAP's [blinded-development declaration on PDF p.4](../../../joi250034supp2_prod_1750956984.11521.pdf#page=4) supports a prospective-plan interpretation without identifying a change to this model. No alternative is selected.

**Direct observation versus inferred explanation:** Direct observation is the printed plan, the undertaking statement, positively identified alternative model labels, and no identified result for the planned model within the supplied REPORT scope. Any claim about whether fitting occurred, why an output is absent, or how an unpublished model was coded is an inferred explanation and is not made.

**Classification confirmation:** Protocol and SAP locations are PLAN because they specify future analyses/proposed tables; article and results-supplement locations are REPORT because they state analyses undertaken and observed estimates. The substantive comparison is PLAN versus REPORT, so `P_R` and `protocol_report` apply. Concordant report copies and output-label corroboration do not add report/report relationships. No classification replacement is required. **Classification ambiguity:** an unidentified result mapping or analysis-specific amendment could reconcile the comparison, but neither is supplied.

**Exact remaining human question:** Which supplied result, if any, is the treatment RR and confidence interval from the prognostic-adjusted primary analysis stated to have been undertaken, and what model and covariates produced it; if no supplied result represents it, was that prespecified analysis changed or its output omitted?

**Determining evidence-state fact:** Direct inspection finds the unconditioned SAP specification and article undertaking statement, but the complete supplied REPORT scope does not identify the corresponding prognostic-adjusted treatment-effect output. All originally registered locations and decisive values match, determining `reproduced`.

## C002 — Planned component multiplicity adjustment differs from reported rule

**Evidence state: reproduced.** **Review domain: protocol_report. Relationship type: P_R. All relationships: P_R.** Qualifying route carried by the registration: **Route A, category 5**; focus D. Status: **Pending Human Adjudication**.

### Location found; source and comparator matched

| Exact location | Role confirmed from content | Printed text/value matched and its comparison function |
|---|---|---|
| [Protocol PDF p.20, §13.2](../../../joi250034supp1_prod_1750956984.09018.pdf#page=20) | PLAN | Key secondary outcomes are the individual primary-composite components. Adjusted P values for ten comparisons will be derived using the named Benjamin-Hochberg procedure; stated rate is 5%. |
| [Protocol PDF p.21, continuation of §13.2](../../../joi250034supp1_prod_1750956984.09018.pdf#page=21) | PLAN | Continuation calls for context and consideration of false-positive risk for other endpoints, subgroup and sensitivity analyses. This contextual sentence does not revoke the component-family adjustment on p.20. |
| [SAP PDF p.12, §3.2, printed lines 404–408](../../../joi250034supp2_prod_1750956984.11521.pdf#page=12) | PLAN | Repeats the ten-comparison adjusted-P commitment for key secondary individual components; other endpoints/subgroup/sensitivity results receive contextual interpretation. |
| [SAP PDF p.25, Table 11](../../../joi250034supp2_prod_1750956984.11521.pdf#page=25) | PLAN | Composite/components shell contains separate P-value and Adjusted P-Values (Benjamin-Hochberg) columns. Composite row has a dash in the adjustment column; the ten component rows form the specified family. This is a shell, not observed adjusted values. |
| [Main PDF p.3, Trial Outcomes and Statistical Analysis interpretation paragraph](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=3) | REPORT | Names all ten components as secondary outcomes. Says related secondary results are interpreted by their pattern/consistency instead of any single significant result; sentence continues on p.4. |
| [Main PDF p.4, Statistical Analysis](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=4) | REPORT | Continued caution says secondary and subgroup results should not infer definitive treatment effect. Separately prints two-tailed P<.05 and “There was no adjustment for multiple testing.” No family-specific exception is printed. |
| [Main PDF p.7, Table 3](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=7) | REPORT | One P-value column with GEE/multiple-birth footnote, no adjusted-P column or component-adjustment label. Every member of the ten-component family is listed below. |

**All ten affected locations within Main PDF p.7 Table 3, P-value column:**

| Component row | Printed P value matched | Planned family comparator matched |
|---|---:|---|
| Intrapartum stillbirth | NA | SAP Table 11 corresponding component row |
| 28-day neonatal death | NA | SAP Table 11 corresponding component row |
| Apgar score <4 at 5 min | .48 | SAP Table 11 corresponding component row |
| Umbilical cord artery pH <7.0 | .12 | SAP Table 11 corresponding component row |
| Neonatal encephalopathy | .96 | SAP Table 11 corresponding component row |
| Neonatal seizures within 28 d | .61 | SAP Table 11 corresponding component row |
| Neonatal unit admission >48 h | .39 | SAP Table 11 corresponding component row |
| Neonatal respiratory support >4 h | .35 | SAP Table 11 corresponding component row |
| Persistent pulmonary hypertension of the newborn | .34 | SAP Table 11 corresponding component row |
| Meconium aspiration | .29 | SAP Table 11 corresponding component row |

The separate emergency cesarean/instrumental birth row, P=.10, is not one of these ten composite components. It is not added to the adjustment family. Main pp.6–7 summarize the same component effects; their inference is governed by the explicit reported rule, not a separate adjusted-analysis output. The complete REPORT output search described for C001 also found no adjusted-P family output.

### Rule, logical reproduction and display precision

**Consistency rule applicable:** Match the prespecified ten-component key secondary family and its adjustment/output commitment to the reported analysis rule. Route A category 5 covers the prespecified key secondary adjusted analysis whose output is not reported. The candidate concerns this rule, not procedure-name spelling or rate terminology.

**Logical comparison reproduced:** Both plans require adjusted P values for the same ten components. SAP provides a separate output column. Main specifies no multiple-testing adjustment without a component-family exception; Table 3 provides only its P-value column. Therefore the supplied report does not identify the planned adjusted component-family analysis/output. Its caution about related outcomes is contextual interpretation and is not an implementation/output of the stated adjustment.

**Display-precision interval check:** No adjusted P value is printed for numerical comparison or recomputed here. Recomputed interval and relative discrepancy are therefore **not applicable** to this categorical rule difference. The eight numeric P locators, at two-decimal precision, have intervals [.475,.485], [.115,.125], [.955,.965], [.605,.615], [.385,.395], [.345,.355], [.335,.345], [.285,.295], respectively; the two NA cells have no numeric interval. Those rounding intervals cannot reconcile “adjusted P values will be derived” with “no adjustment,” and are not treated as evidence of numerical conflict. The planned 5% rate is not compared numerically with the report's P<.05 significance level: an adjustment rule and an individual threshold are different specifications. No adjusted P values or alternative method are proposed.

### Inputs, alternatives, observation and human question

**Necessary inputs available:** Named family, all ten corresponding table rows, positive adjustment commitment, proposed adjusted-output column, explicit reported no-adjustment statement and report's contextual caveat. They suffice for the logical comparison.

**Exact missing inputs or definitions:** An implemented adjustment specification, adjusted output for the family, any handling of the two zero-event/NA component tests within that family, and an analysis-specific change record are unavailable. These would be necessary to reconstruct an adjusted analysis or decide which rule actually governed its inference; they are not needed to reproduce the printed rule difference. Table 3's raw displayed P precision alone would not identify the complete implemented adjustment.

**Source-grounded alternatives:** Adjusted results may have been generated but omitted; the planned rule may have been changed; or the no-adjustment sentence may have an unstated narrower intended scope. The plans' allowance for contextual interpretation of other outcomes and main's caution are observed, but no supplied sentence confines no-adjustment to a different family or identifies an amendment. No alternative is selected and no claim is made that significance or the overall conclusion would change.

**Direct observation versus inferred explanation:** Direct observation is the two plans' adjusted-P commitment, the table shell, all ten report P entries, and the explicit no-adjustment sentence. Whether adjustment was actually performed and why reporting differs are inferred explanations not established by these sources.

**Classification confirmation:** Prospective specifications/table shell are PLAN; completed analyses and observed component output are REPORT. The conflicting rule is `P_R`, determining `protocol_report`; both plans agree, so no `P_P` is present. Report caveats and the table corroborate the report side rather than establish an additional `S_W` conflict. No classification replacement is required. **Classification ambiguity:** intended scope or an amendment could explain the reported rule, but no supplied family-specific mapping establishes either.

**Exact remaining human question:** Was the prespecified adjusted-P analysis of the ten key secondary composite components performed or prospectively changed, including how the zero-event components were handled, and which adjustment rule applies to the component P values and inference reported in Table 3?

**Determining evidence-state fact:** Visual inspection confirms both plans' positive ten-component adjustment requirement and the article's explicit no-adjustment rule, with no supplied adjusted-family output or exception. Original values and pages match, determining `reproduced`.

## C003 — Prior-cesarean subgroup history window differs from protocol

**Evidence state: reproduced.** **Review domain: protocol_report. Relationship type: P_R. All relationships: P_R.** Qualifying route carried by the registration: **Route B**; focus D. Status: **Pending Human Adjudication**. Assigned issue is exclusively the prior-cesarean criterion; the anomaly wording component remains screening provenance and is not an affected result in this card.

### Location found; source and comparator matched

| Exact location | Role confirmed from content | Printed text/value matched and its comparison function |
|---|---|---|
| [Protocol PDF p.17, §8, subgroup item 4](../../../joi250034supp1_prod_1750956984.09018.pdf#page=17) | PLAN | Six planned primary-effect subgroups include “one or more previous CS.” This specifies any previous cesarean rather than naming only the immediately preceding pregnancy. |
| [Main PDF p.4, prespecified-subgroup paragraph](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=4) | REPORT | States prespecified interaction analyses of the primary composite, including “cesarean delivery in preceding pregnancy.” |
| [Main PDF p.7, subgroup-results paragraph](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=7) | REPORT | Additional occurrence found during recheck: names “preceding pregnancy cesarean delivery” among subgroup results and points to Figure 2. Added to the occurrence list; the original cited locations still match. |
| [Main PDF p.8, Figure 2, cesarean-delivery-in-preceding-pregnancy family and caption](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=8) | REPORT | Label is “Cesarean delivery in preceding pregnancy.” Yes: 4/57 (7.0%) versus 1/71 (1.4%), RR 4.98 (95% CI 0.57–43.35). No: 79/1568 (5.0%) versus 83/1554 (5.3%), RR 0.94 (0.70–1.27). Caption says subgroup interaction tests were not significant (P>.05); subgroup effects used GLM log-binomial. |
| [SAP PDF p.14, §3.11, printed lines 477–488](../../../joi250034supp2_prod_1750956984.11521.pdf#page=14) | PLAN, corroborating report criterion | Subgroup item 4 is “Method of delivery for previous pregnancy CS.” Interaction model and separate models by subgroup levels are specified. No baseline-covariate adjustment is planned in these subgroup models. |
| [SAP PDF p.29, Table 15, preceding-pregnancy-CS row](../../../joi250034supp2_prod_1750956984.11521.pdf#page=29) | PLAN, corroborating report criterion | Proposed subgroup shell says “Preceding pregnancy CS,” with yes/no rows. Proposed RR/CI, P and interaction P columns contain placeholders rather than current-trial results. |
| [SAP PDF p.4, §§1.2 and 1.3.2](../../../joi250034supp2_prod_1750956984.11521.pdf#page=4) | PLAN, amendment/timing context | Revision history: drafts 23 September and 14 October 2024; version 1.2 finalized 25 October 2024 with nonspecific changes. Signed approvals dated 25 October 2024 state the plan was developed completely blinded, without knowledge of intervention effect. No change to the cesarean criterion is specifically named. |
| [Main PDF p.3, opening Statistical Analysis sentence](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=3) | REPORT, amendment/timing context | States analyses were prespecified in protocol and SAP before database lock and unblinding. This supports considering a prospective SAP revision, without identifying the history-window change. |
| [Protocol PDF p.22, §15.3](../../../joi250034supp1_prod_1750956984.09018.pdf#page=22) | PLAN, amendment context | Describes protocol-amendment approval and implementation process. It is a general process, not a record of this particular criterion change. |

The same protocol/SAP/report pages contain fetal-anomaly subgroup wording. It was read as surrounding context and preserved in the screening provenance. This recheck does not extend C003 to that separately screened wording component or assume a different anomaly population.

### Rule, logical reproduction and display precision

**Consistency rule applicable:** Compare the explicit eligibility/history window of a prespecified primary-effect subgroup, which is an eligible planned-versus-reported analysis specification. Route B requires focus, no immediate source reconciliation, and a named interpretation/extraction consequence.

**Logical comparison reproduced:** Let A be women with at least one cesarean in any previous pregnancy; let B be women with a cesarean in the immediately preceding pregnancy. B implies A. A does not imply B: a history with a cesarean followed by a vaginal birth illustrates A without B. This is a logical counterexample showing the criteria differ, not a claim that such a history occurred in this dataset. The protocol names A; report pp.4, 7 and Figure 2 name B; SAP §3.11/Table 15 corroborate B. The source package does not show whether the implemented criterion was A or B, document a specific replacement, or demonstrate that A and B coincided for these participants.

**Display-precision interval check:** The registered inconsistency is a categorical history-window difference, so no recomputed numerical interval or relative discrepancy is **applicable** to that rule. The Figure 2 RRs have half-unit intervals [4.975,4.985] and [.935,.945]; their respective CI endpoints have [.565,.575], [43.345,43.355], [.695,.705], [1.265,1.275]. The protocol provides no numerical subgroup effect to compare against those intervals. The displayed counts are integer observations, not rounded continuous estimates. As a locator check, subgroup totals reconcile: 57+1568=1625 and 71+1554=1625; events 4+79=83 and 1+83=84. This arithmetic neither establishes the implemented history window nor shows identical membership under A and B. No count/RR inconsistency is alleged.

### Inputs, alternatives, observation and human question

**Necessary inputs available:** Exact protocol rule; repeated report rule; complete subgroup yes/no counts, RRs/intervals and model caption; SAP rule and proposed shell; blinded-preparation declaration and generic amendment context. These suffice to reproduce the definition-level discrepancy and identify the effects whose population label is affected.

**Exact missing inputs or definitions:** Operational subgroup coding rule, source variable definition, earlier-pregnancy delivery history needed to identify A outside B, membership cross-tabulation under both criteria, criterion-specific revision/amendment record and its timing relative to lock/unblinding are unavailable. Raw participant membership or the actual number reclassified cannot be inferred from published yes/no totals.

**Source-grounded alternatives:** The blinded SAP may prospectively have revised the protocol criterion; the report label might abbreviate a broader implemented criterion; or the two criteria may happen to select identical participants. The SAP's explicit signed blinded-development statement and main's prespecification-before-lock statement strengthen the prospective-revision alternative. Their nonspecific revision history does not demonstrate that this history window was changed prospectively, and their finalization date alone is not treated as evidence of unblinded development. No alternative is selected.

**Direct observation versus inferred explanation:** Direct observation is the different printed history windows, their three report occurrences, the SAP's corroborating definition and its blinded-preparation statement. Actual reclassification, a protocol violation, motives, or whether the effect estimates would change are not directly observed and are not asserted.

**Interpretation/extraction consequence:** The reader extracting yes RR 4.98 (0.57–43.35) and no RR 0.94 (0.70–1.27), or interpreting their interaction analysis, needs the subgroup population criterion. B1 is met by the prespecified subgroup specification under focus D; B2 by no criterion-specific amendment mapping or membership equivalence; B3 by the different populations that the two printed rules can denote. This does not assert that any actual participant changed category.

**Classification confirmation:** Protocol/SAP specifications are PLAN; article descriptions and Figure 2 are REPORT. The bounded inconsistency compares the protocol criterion with the report criterion, so `P_R` and `protocol_report` apply. SAP only corroborates the report criterion and supplies prospective-plan context; it is not registered here as a separately conflicting plan pair. Under the corroboration rule no `P_P` is added. Repeated report occurrences agree and do not establish `S_W`. No classification replacement is required. **Classification ambiguity:** a prospective SAP revision is plausible and explicitly supported by blinded preparation, but criterion-specific mapping and actual coding are missing.

**Exact remaining human question:** Was the Figure 2 subgroup coded as any previous cesarean or only cesarean in the immediately preceding pregnancy, and does a criterion-specific prospective revision or a membership comparison showing identical groups reconcile it with protocol §8?

**Determining evidence-state fact:** Direct printed-source inspection confirms the any-previous protocol rule and repeated preceding-pregnancy report rule; the corroborating SAP and generic blinded revision statements do not specifically reconcile their criterion difference. Original transcriptions remain accurate, determining `reproduced`.

## Completion and bounded unresolved inputs

Covered IDs: **C001, C002, C003**; 3 of 3 assigned. Evidence states: **reproduced 3**; **reproduced_after_transcription_correction 0**; **not_reproduced 0**. All roles, primary/all relationship codes and review domains match the registered classification. No assigned ID was removed. One additional repeated report occurrence, C003 main p.7, is recorded for coordinator propagation.

There is no unresolved supplied-source page inspection gap in this scope. Unavailable fitted prognostic output/mapping (C001), implemented adjusted-family output/change specification (C002), and subgroup coding/membership/criterion-specific amendment (C003) are precisely bounded human questions above. They are not scientific coverage omissions and do not select a disposition. Sources and reused artifacts were preserved.
