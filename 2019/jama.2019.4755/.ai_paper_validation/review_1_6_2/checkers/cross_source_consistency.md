# Cross-source consistency review

## Scope and evidence

Fresh cross-source checker; complete assigned union of the main and support quantitative maps. Sources: DOC-001 main report PDF pp.1–7 (REPORT); DOC-002 protocol v1.5 PDF pp.1–62 (PLAN); DOC-003 SAP PDF pp.1–10 (PLAN); DOC-004 results supplement PDF pp.1–8 (REPORT); DOC-005 availability PDF p.1 (REPORT). All 88 mapped units were covered through the complete current maps and source-linked reusable extraction. Scope comprises N001–N043, N100–N106, N200–N205 and S001–S049, S100–S133, S200–S221. These are grouped relationships, not a restriction on displayed cells. No workbook, CSV, or other structured result source is supplied. No old scientific conclusions or external evidence were used. QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely.

Population, time, contrast, measure, model, analysis set, reference group and precision were matched before comparison. Source native/layout layers were locators; the reproduced finding was confirmed visually against direct CPU renders. Source and reused artifacts were preserved. No scientific coverage limitation.

## Completed matched comparisons

| Relationship scope | Cross-location/source checks and outcome |
|---|---|
| N001–N003, N006–N022 | Abstract, Key Points, results, participant flow and baseline display: randomized 2422=1208+1214; analysis 2134=1075+1059; exclusions 288 reconcile with 77+61+56+94; advanced neoplasms 224=8+216 reconcile with arm findings. Randomized male count 1219 is distinguished from analyzed male count 1075. Abstract screening/diagnostic proportions match nonmissing indication denominators. |
| S001–S018, N024–N033 | All primary and narrative-matched secondary sensitivity/specificity values, differences, intervals, directions and P values match across abstract, Key Points, narrative and Table 2. Primary differences 9.8 (−3.1,22.2), P=.14 and 6.0 (−5.7,17.5), P=.32 retain the same cutoff and analysis set. Sex-specific ranges match their rows without assigning overall results to strata. |
| N023, N202, N204, S038, S045, S209, S219 | Main valid scheduled-day-2 sample counts 1030/1012 quantitative and 974/969 qualitative match eTable 2 and Table 2 totals. Actual-day-2 per-protocol denominators include samples scheduled on other days; eTable 4 matches actual-day totals rather than the scheduled-day-2 column alone. Main male per-protocol differences 23.2 (5.0,39.5) and 22.5 (4.5,38.6) match eTable 4. |
| N034–N037, S019–S036, S046–S047, S211–S215, N203–N205, S218–S220 | Overall PPV/NPV statements match overall rows; women's intervals are not assigned the overall statement. Main and supplementary predictive values belong to intention-to-screen versus per-protocol sets, respectively. Combined-day narrative matches eTable 3's sensitivity increase and specificity decrease. All supplement captions/footnotes and sex/test/cutoff keys were retained; a visible dash is not replaced by a hidden text-layer estimate. |
| S039, S101–S102, S109, S125–S127, S200, S205–S206 | Outcome status and primary-endpoint lists were compared item by item. F-XS-001 below records the differing primary hierarchy. CRC/advanced-adenoma composite matches report and SAP; the colonoscopy category list is distinguished from the composite. |
| N004–N005, N040–N042, N101, N104–N105, S103–S107, S114, S118, S201 | Single oral uncoated 300-mg intervention versus placebo agrees; future 75/100-mg discussion is not a changed intervention. Two tests/eight kits and collection before preparation agree. SAP day-numbering footnote explicitly maps protocol medication day 1/sample day 3 to medication day 0/sample day 2. Delayed collection and optional baseline were matched to scheduled versus actual days. |
| S106, N200–N201 | Protocol §§3.8/6.2, SAP §2.2 and report eTable 1 criteria compared item by item: three inclusion criteria; five endpoint-related disease/symptom exclusions; antithrombotic/ASA/NSAID windows; each current symptom and medical-history criterion; each intended medication; surgery; alcohol, illicit drugs, pregnancy, compliance and other-trial criteria. Thresholds age 40–80, 12-month menopause, two-week/one-week/three-day drug windows, GFR<30, infarction within six months, methotrexate≥15 mg/week agree. Clinical synonyms and expanded G6PD wording do not change a result or population rule. |
| S038, S109, S112, S115–S116, S119, S122, S132–S133, S202–S204, S207, S217 | Efficacy sample/colonoscopy availability and safety randomized-population rules distinguished. SAP §7 explicitly replaces primary per-protocol analysis with intention-to-screen and includes missing timing. Main scheduled-day analysis agrees with that change. No numerical imputation is asserted. Recovered reports versus missing-test exclusion are different operations. |
| S040–S043, S123–S124, S210–S214, S216–S217, S221 | Main adjusted-Wald interval methods match SAP Agresti–Coull/Agresti–Caffo and PropCIs. Interaction GLM matches plan; site random intercept in the report is not the participant random intercept planned for repeated measurements. The report does not claim the site model was prespecified. Absence of some ordinary secondary analyses is evaluated under the primary/key-secondary restriction below. |
| S037, S049, N102, N106, S121, S126, S128–S129, S210, S212 | Power inputs prevalence10%, sensitivity36% versus60%, two-sided .05 and90% agree. Protocol 2400 recruited/2000 analyzable is distinguished from achieved enrollment and valid-test denominators. Sex-specific70% power assumption is not the overall primary60% assumption. Confirmatory primary/exploratory other analyses and no reported multiplicity adjustment do not conflict with a supplied correction rule; none is stated. Recruitment/safety stopping criteria are distinguished from an inferential interim boundary. No noninferiority/equivalence margin or corresponding claim is supplied. |
| N038, S112, S117, S130, S215, DOC-005 | Adverse event totals and serious-event narrative have no competing printed result in plan or supplement; definitions and randomized safety set retained. Availability statement contains no extra data or statistical specification. |

## Findings

### F-XS-001 — Primary outcome hierarchy differs within the protocol and between its broader definition and the report

**Compared locations and roles:** PLAN [DOC-002 p.11 §3.4](../../../joi190039supp1_prod.pdf#page=11) and [p.22 §6.1](../../../joi190039supp1_prod.pdf#page=22), PLAN [p.13 §3.9 continuing p.14](../../../joi190039supp1_prod.pdf#page=13), PLAN [p.28 §§7.1–7.2](../../../joi190039supp1_prod.pdf#page=28), PLAN [DOC-003 p.6 §3.2](../../../joi190039supp2_prod.pdf#page=6), and REPORT [DOC-001 p.3 Outcomes and Statistical Analyses](../../../jama_brenner_2019_oi_190039.pdf#page=3). REPORT [p.1 Main Outcome and Measures](../../../jama_brenner_2019_oi_190039.pdf#page=1) repeats the narrow primary definition.

**Printed statements:** Protocol §§3.4/6.1 identify the primary endpoint as FOBGold sensitivity and explicitly list specificity and ROC AUC as secondary. Its §3.9 parenthesis instead defines the primary endpoint as FOBGold sensitivity, specificity and AUC on day 3. On the same p.28, §7.1 calls FOBGold sensitivity the primary endpoint and says primary endpoints are confirmatory; §7.2 calls sensitivity, specificity and ROC AUC of **two** immunochemical FOBTs the primary endpoint. SAP p.6 calls FOBGold sensitivity primary, and FD Hb/Hp sensitivity, FOBGold AUC and both tests' specificities secondary. Main p.3 calls quantitative sensitivity at two cutoffs primary; specificity and qualitative sensitivity are reported secondary, and AUC is explicitly a secondary outcome not reported in the article. Secondary analyses are described as exploratory.

**Comparison logic:** The same protocol version assigns specificity/AUC to both primary and secondary status; its broader §7.2 definition additionally includes both tests, unlike the FOBGold-only primary definitions. The report follows the narrow definition. This is one repeated hierarchy pattern, with all affected locations retained. The report's secondary designation for specificity/qualitative sensitivity and its omission of AUC have different implications under the broader versus narrower prespecified primary list. No arithmetic reconstruction is required: recomputed interval and relative discrepancy are not applicable to this categorical status comparison. The disclosed SAP §7 changes concern analysis population and missing values, not this outcome hierarchy.

**Focus area:** D.

**Proposed review domain:** protocol_report.

**Provisional relationship type:** P_R.

**All relationships:** P_R, P_P. P_R takes precedence: the report differs from the broad protocol definition; there are also direct plan-internal conflicts, including between protocol sections and SAP. The SAP is not merely corroborating an internal report discrepancy.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Primary/confirmatory versus secondary/exploratory status of quantitative and qualitative specificity, qualitative sensitivity, and ROC AUC; completeness of reported primary outcomes if §7.2 governed.

**Why context does not resolve it:** This is an always-register outcome-status conflict. The narrow endpoint lists support the report, but the broad statements explicitly say “primary endpoint,” including in the power section, and §7.1 assigns confirmatory status to primary endpoints. Choosing one list requires identifying the governing specification rather than reconciling equivalent names. No supplied hierarchy amendment addresses those broad statements.

**Supported alternatives and classification ambiguity:** The endpoint sections/SAP may have governed and the broad synopsis/power descriptions may reflect a retained earlier specification. Alternatively, the broad definition may have governed before an undocumented hierarchy change. The supplied evidence establishes the conflicting status statements, not their production mechanism or which specification governed. Day 3 versus day 2 is disclosed renumbering and is not part of this finding.

**Exact human question:** Which prespecified primary outcome list governed the trial, and what supplied amendment or decision reconciles the protocol's primary specificity/AUC/both-test wording with the narrow FOBGold-sensitivity primary definition and the report's secondary/exploratory status and unreported AUC?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-002 pp.18,21,28; DOC-003 pp.4,9; DOC-001 p.3 | Original protocol excludes first postdose sample delayed by constipation, whereas main uses scheduled-day samples despite timing deviations. Later SAP explicitly changes primary analysis to intention-to-screen; the observed report follows that change. This is distinct from the unresolved hierarchy pattern above. | CONTEXT_RESOLVES |
| DOC-003 pp.7,9; DOC-004 p.4 | Earlier SAP excludes missing collection day; later §7 explicitly includes it. No undisclosed report/plan conflict remains. | CONTEXT_RESOLVES |
| DOC-002 day3 versus DOC-001/DOC-004 day2 | Apparent endpoint-time difference is resolved by DOC-003 p.4 explicit medication-relative renumbering. | TERMINOLOGY_OR_WORDING |
| DOC-003 pp.8–9; DOC-001 pp.3–4; DOC-004 p.8 | Planned repeated-participant model and reported site-effect model have different random-intercept units; no assertion identifies them as the same analysis or says the site model was prespecified. | NOT_REPRODUCED |
| DOC-003 pp.8–9; DOC-001 p.3; DOC-004 pp.5–8 | Total/partial ROC, repeated-day plot/model, age/smoking/BMI and lesion subgroups, delayed-colonoscopy sensitivity analysis, and tests/colonoscopies per detected neoplasm are not supplied as results. Apart from AUC status captured in F-XS-001, these are ordinary secondary analyses, not abstract-reported or prespecified key secondary analyses; absence alone supplies no competing printed result. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 p.9; DOC-001 pp.3,6 | SAP missing-test Fisher assessment and treatment decision have no printed numerical counterpart; main approximately4% sample reduction does not assert a conflicting numerical imputation rule. | CONDITIONAL_OR_UNREPORTED |
| DOC-002 pp.12–13,22–23; DOC-003 pp.4–5; DOC-004 pp.2–3 | Acute gastrointestinal/peptic-ulcer wording, exsiccosis/dehydration, colitis ulcerosa/ulcerative colitis, and expanded drug/enzyme names differ across eligibility lists but do not prevent identification of a criterion or alter a printed threshold. | TERMINOLOGY_OR_WORDING |
| DOC-004 p.7 versus embedded text/native derivatives | Women's PPV point-difference cells visibly show dashes although the embedded layer contains numerical tokens; hidden-layer values are not independently printed competing results. | NOT_REPRODUCED |
| DOC-001 p.5 Table3 Men third row | Blank test label is recoverable immediately from the quantitative/quantitative/qualitative row sequence and matching cutoffs/counts; no competing result attribution is printed. | CONTEXT_RESOLVES |

## Provenance and completion

One finding; nine excluded observations. All assigned matched-result and statistical-design relationships reviewed, without sampling. No scientific coverage gap. Absence of raw data limits reproduction of unprinted models, not the completed supplied-evidence comparison.

Direct confirmation derivatives, all Poppler pdftoppm 26.01.0 on CPU, no OCR: `preprocessing/xs-DOC002-p28.png` (120 dpi), `preprocessing/xs-DOC002-p13.png`, `preprocessing/xs-DOC002-p11.png`, `preprocessing/xs-DOC003-p6.png`, `preprocessing/xs-DOC001-p3.png` (100 dpi). Commands used `pdftoppm -f N -l N -singlefile -r DPI -png SOURCE PREFIX`. Each image was directly viewed. Protocol p.22 duplicates the visually confirmed p.11 hierarchy and was checked against its complete source-linked layout. These derivatives supplement the current map provenance and do not modify reused assets.
