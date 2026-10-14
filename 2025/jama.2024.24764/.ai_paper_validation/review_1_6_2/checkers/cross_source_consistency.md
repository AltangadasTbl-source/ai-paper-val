# Cross-source consistency review

Runtime agent: `/root/cross_checker`. Fresh mandatory cross-source stage; model `gpt-6.1-sol`, reasoning effort `medium`. Ownership: this checker artifact. Scientific inputs were supplied sources, eligible source-linked extractions, and current-run maps; no prior scientific conclusions or external evidence were used.

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely. Reviewed source/evidence inventories and complete source coverage, main map M001–M137, SAP/results map U001–U034, and protocol map P001–P034. Exact scope: all matched trial relationships across DOC-001 REPORT pp.1–11, DOC-003 REPORT pp.1–9, DOC-002 PLAN pp.1–46, and DOC-004 PLAN pp.1–48. All 114 source pages are mapped upstream; this stage reviewed their cross-location and planned-versus-reported relationships. Numerical arithmetic within individual displays and inferential compatibility receive separate mandatory checker review; all relevant cross-source matches remain covered here.

Five findings and ten excluded observations are recorded. No candidate IDs or adjudications are assigned.

## Evidence access and derivative provenance

Preferred reused assets were the complete main/results native text and geometric layout companions, full SAP/protocol layout blocks, and source-matched page images identified in evidence_asset_inventory.md. Eligible extractions are transcription aids; findings below cite supplied PDFs. Fresh direct-source text confirmation used the recorded fallback PyMuPDF 1.26.4 through `workflow_1_6_2/scripts/pdf_tools.py text` on main p4 and p8, SAP pp23–26, and protocol p17. Outputs are `preprocessing/cross_source/main-p4.txt`, `main-p8.txt`, `sap-p23-26.txt`, and `protocol-p17.txt` under this run directory. The command form was `.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py text SOURCE --first N --last M OUTPUT`. No rendering or OCR was performed by this checker; no GPU inference is claimed. New derivatives are current-run assets, outside reused-asset hashes.

## Complete comparison record

| Relationship family | Compared locations and matching keys | Review outcome |
|---|---|---|
| Primary randomized/retained/analysis population | Main abstract, Key Points, Figure1, recruitment narrative, Table3, Figure2; M002–M003, M009–M014, M022, M136 | 840 randomized; 19 removed before trial data, 821 retained; further primary exclusions give 788 analyzed, 394 each arm. Abstract 52 postrandomization exclusions includes both stages. Population labels distinguished before matching. |
| Primary SSI counts, estimate, interval and P | Main pp1,2,6,8,9; supplement pp6,8; M003/M085/U033/U034 | 112/394 versus108/394; RR1.03, CI0.83–1.28, P=.78 match. Supplement source-time rows overlap; exclusive additions give109+0+3=112 and107+1+0=108. No mismatched primary estimate or direction found. |
| Abstract demographics | Main pp1,5,6; M004/M023/M024/M127 | Age63.8 and female52% match retained population after rounding; no population reassignment. |
| LOS abstract/narrative/Table3 | Main pp1,4,6,8; SAP pp7,18,25,42; protocol pp24,38–39 | Combined-country8[6–14] versus9[6–14.5], ratio0.96[0.88–1.06], P=.21 agree within REPORT. UK9[7–15] versus11[7–16], ratio0.91[0.82–1.02], P=.12 are a different population. Planned versus reported analysis retained as F-XS-002. |
| Quality-of-life matched results | Main pp4,6,8; supplement pp3–4; SAP pp20–23,26,42–43; protocol pp25,29,38–39 | Day30 PCS/MCS descriptive means and modeled contrasts match after precision allowance. All EQ/SF component time points, reference group, baseline adjustment, treatment×time specification and scale directions matched. Covariance discrepancy retained as F-XS-003; missing post-death index rule considered separately below. |
| Quality-of-life significance narrative | Main pp1,6 versus supplement eTable3 p4 | Unqualified no-difference statement versus day7 EQ index P=.02 retained as F-XS-005; interaction P=.10 and later-time tests distinguished as alternative hypotheses. |
| Pain, acceptability and outcome hierarchy | Main pp1,4,6,8; supplement contents; SAP pp7,26–27,42,44; protocol pp2,8,16,24–25,27 | Pain addition disclosed in protocol amendment; day7/day30 times and 1–10 endpoints match. Main day7 mean difference−0.41, CI−0.70 to−0.12, P=.01 agrees with narrative lower pain by0.4 points. Acceptability remains secondary in Table3. Outcome-status and unreported non-key analyses screened below. |
| Wound complication/readmission/SAE | Main pp4,6,8; supplement p5; SAP pp19–20,24–27,41,45; protocol pp24–25,31–33,47–48 | Matched 30-day binary definition, wound complications excluding SSI, wound-related readmission components, patient/event distinction, grading and secondary status. Supplement grade totals84/83 count complication types; main73/71 count participants and grades reflect participant-level categories. |
| Intervention | Main pp1–4,6; supplement p3; SAP pp6,12,14,38; protocol pp8,21–24 | Randomized PICO7 −80mmHg, seven days or earlier discharge, replacement permitted; simple control excludes active silver/honey/iodine dressings. Receipt and three-day PP rule distinguished from intended seven-day exposure and feasibility24-hour adherence. No conflicting randomized dose/duration found. |
| Eligibility, consent and criterion lists | Main pp2–3,10; SAP pp6,13,31; protocol pp8,17–20 | Compared item by item: emergency operation; incision≥5cm; primary skin closure; UK≥16/Australia≥18; consent/capacity arrangements; ability for day30 follow-up; prior abdominal surgery3months; planned reopening30days. Report-only survival criterion retained as F-XS-001. Separate fascia description and conversion-boundary wording do not establish changed realized analysis membership. |
| Primary model, covariates and hypothesis | Main p4/Table3; SAP pp8–9,12,15,18,25,40; protocol pp23–24,38 | Individual randomization/minimization; center random, stoma/contamination fixed; log-binomial RR and identity-link RD; control reference; superiority/two-sided95% CI/5% convention reconcile. Convergence fallback is permitted, not a demonstrated change. No noninferiority/equivalence margin applies. |
| Complete cases, withdrawal, death and sensitivities | Main pp3–4,6; supplement pp8–9; SAP pp12–15,18,23,29; protocol pp24,30,39 | Initial received/available primary data, retained earlier SSI after dropout/death, missing absent SSI with no day30 form, PP≥3days/earlier discharge, early-form and30–44-day exclusions, diary-only and return-to-theatre exclusions, both extreme-case assignments all matched. Six supplement sensitivity definitions exhaust mandatory SAP list. Tipping point is explicitly post hoc; no claim of prespecification conflict. |
| Primary subgroup inventory | Main pp4,9; SAP pp16–17,28,46; protocol p39 | All nine SAP subgroups represented: contamination4, stoma2, operative group3, incision2, prep3, country2, BMI4, assessment method3, UK pandemic date2. Each Figure2 interaction P and arm event counts mapped. Assessment/pandemic additions are in supplied SAP, despite shorter protocol list. Numeric incision boundary mismatch inside SAP retained as F-XS-004. |
| Sample size/power | Main p4; SAP p9; protocol p38 | Control25%, intervention15%, absolute10points/relative40%, power90%, alpha.05,336/arm before20% attrition,420/arm recruited,840 total reconcile across documents. Separate statistical checker performs numeric reproduction. |
| Interim, feasibility, stopping and multiplicity | Main pp2,4; SAP pp9–12; protocol pp15,38–41 | Annual/discretionary DMC; approximate P<.001 proof-beyond-reasonable-doubt stopping guide; final.05; no multiple-testing correction; feasibility green/amber/red criteria and all-green continuation statements match. No report statement contradicts a planned decision; unprinted interim results/charter cannot establish a mismatch. |
| Economic plan and other supplied structure | SAP p29; protocol pp39–40; main scope | Economic analyses expressly documented separately; no economic estimate/result is attributed in this report. No independent workbook/CSV/Office scientific source supplied. Prospective shells were never treated as observed results. |

## Findings

### F-XS-001

**Title:** Reported 30-day survival eligibility exclusion is absent from the supplied protocol criterion list.

**Compared locations and document roles:** REPORT [main eligibility, PDF p2](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=2) and [mortality interpretation, p10](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=10); PLAN [protocol eligibility §5.1–5.2, p17](../../../joi240145supp4_prod_1741627844.90412.pdf#page=17), corroborated by [protocol summary, p8](../../../joi240145supp4_prod_1741627844.90412.pdf#page=8). Amendment context: PLAN [protocol p2](../../../joi240145supp4_prod_1741627844.90412.pdf#page=2).

**Printed statements:** The report excludes patients “not expected to survive beyond 30 days” and later explains the low mortality by the study not including patients unlikely to survive30days. The protocol's exclusion list contains only abdominal surgery during the previous3months and expected reopening within30days. Its inclusion list includes willing/able day30 follow-up and consent/capacity criteria; it does not list predicted30-day survival. Current protocol version4.0 and its supplied amendment summaries do not disclose this added criterion.

**Comparison logic:** Compare the full prospective inclusion/exclusion list item by item with the reported population definition. Predicted survival is a distinct criterion from incision, consent and ability to attend follow-up. The discrepancy is the presence versus absence of an explicitly reported exclusion, not an assertion that an observed death violates eligibility. It can change the population to which the reported primary treatment contrast is said to apply. Display-precision intervals/relative discrepancy: not applicable to categorical criterion presence;30days is an exact eligibility horizon, not a rounded estimate.

**Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed relationship type:** `P_R`. **All relationships:** `P_R`.

**Qualifying route:** Route B.

**Affected result or extracted value:** Primary SSI RR1.03 (95%CI0.83–1.28) and the population description accompanying this estimate; mortality within30days and its eligibility-based interpretation.

**Why context does not resolve it:** The report affirmatively attributes a restriction to the study, while the complete supplied current plan criterion list does not contain that restriction. A reader cannot identify whether the target population was prospectively restricted by predicted survival or whether this is a later description of recruitment practice. No number of excluded people or unsupported clinical judgment is inferred.

**Supported alternatives and classification ambiguity:** A separate operational/amended eligibility document may have added this criterion but is not supplied. Alternatively, the report could describe pragmatic clinical selection rather than a formal protocol exclusion. Willingness/ability for day30 follow-up may explain some overlap, but does not establish the same explicit survival threshold. Sources remain PLAN versus REPORT under either interpretation.

**Human question:** Was predicted survival beyond30days a formal prespecified eligibility criterion, and which supplied amendment or operational definition establishes the population restriction described in the report?

### F-XS-002

**Title:** Prespecified hospital-stay difference analysis is replaced by geometric-mean ratios, with a pooled-country result foregrounded.

**Compared locations and document roles:** PLAN [SAP §9.2, p15](../../../joi240145supp1_prod_1741627844.87412.pdf#page=15), [§9.6, p25](../../../joi240145supp1_prod_1741627844.87412.pdf#page=25), [planned LOS display, p42](../../../joi240145supp1_prod_1741627844.87412.pdf#page=42); PLAN [protocol §14.2.2, pp38–39](../../../joi240145supp4_prod_1741627844.90412.pdf#page=39), [UK-only outcome definition, p24](../../../joi240145supp4_prod_1741627844.90412.pdf#page=24). REPORT [abstract p1](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=1), [method p4](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=4), [secondary-results narrative p6](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=6), [Table3 and footnote c p8](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=8).

**Printed statements/values:** SAP specifies UK patients only, continuous mixed-effects linear regression producing an adjusted mean difference and95%CI. Its general distributional rule says to follow the proposed primary method first and examine transformations/nonparametric alternatives through sensitivity analysis. Protocol specifies an adjusted mean difference or, if skewed, an unadjusted difference in medians. Report instead log-transforms before fitting and exponentiates to adjusted geometric-mean ratios: UK0.91 (0.82–1.02), P=.12, and UK+Australia0.96 (0.88–1.06), P=.21. The latter accompanies medians8 versus9days in the abstract. No planned adjusted arithmetic-mean difference or unadjusted median-difference estimate/interval is supplied in the complete article/results supplement.

**Comparison logic:** Match LOS by index surgery-to-discharge definition, then distinguish UK versus pooled population and arithmetic/median difference versus geometric ratio. These are different estimands; the report correctly labels its ratios, so this is not a crude-versus-modeled calculation issue. The prespecified UK difference analysis is not reported; the transformed analysis takes its place. The pooled analysis is additional to the planned UK-only specification. One finding consolidates this replacement/presentation pattern. Display-precision intervals/relative discrepancy: not applicable; an estimand and population specification cannot be reconciled by rounding.

**Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed relationship type:** `P_R`. **All relationships:** `P_R`.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The abstract's key-secondary hospital-stay estimate0.96 (95%CI0.88–1.06) and the UK hospital-stay estimate0.91 (0.82–1.02), including whether either represents the prespecified analysis.

**Why context does not resolve it:** Route A category5 applies because the planned key-secondary difference analysis is absent. The report explains skewness and clearly defines the transformation, but does not identify a reported planned difference analysis or a documented replacement of the SAP's first-analysis rule. The alternative analysis rationale does not supply the absent prespecified estimate.

**Supported alternatives and classification ambiguity:** An approved revised analysis specification may have replaced the mean/median difference with a log-scale model and expanded the population; no such populated SAP amendment is supplied. The ratios could have been intended as permitted transformation sensitivities, but the planned first analysis is not shown. Protocol and SAP differ in their skewness contingencies; both planned difference estimands are absent, so no separate plan-internal finding is inferred from their order/version relationship.

**Human question:** Which supplied amendment establishes the geometric-ratio/pooled-country LOS analysis as the reported analysis, and where is the planned UK mean- or median-difference result and interval?

### F-XS-003

**Title:** Repeated-measures quality-of-life covariance specification differs between SAP and report.

**Compared locations and document roles:** PLAN [SAP §9.6, p26](../../../joi240145supp1_prod_1741627844.87412.pdf#page=26); REPORT [main Statistical Analysis, p4](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=4), [Table3 SF-12 results, p8](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=8), [supplement eTable2 p3](../../../joi240145supp3_prod_1741627844.89412.pdf#page=3), and [eTables3–4 p4](../../../joi240145supp3_prod_1741627844.89412.pdf#page=4).

**Printed statements:** SAP specifies a general “unstructured” covariance structure for repeated SF-12 PCS/MCS; EQ-5D index/health uses the same analysis methods. It also specifies robust sandwich standard errors. The main report says the longitudinal SF-12/EQ-5D model assumed an “independent covariance structure.” Both specify a treatment×time interaction and adjustment for minimization variables; baseline adjustment is generally described. Supplement model footnotes repeat center random effects and treatment×time but do not name a different covariance structure.

**Comparison logic:** Match outcome components, repeated time points, treatment contrast and fixed/random adjustments before comparing covariance assumptions. Unstructured and independent are different covariance specifications: independent sets cross-time residual covariance to zero, while unstructured permits unconstrained covariance parameters. This is a positive printed method conflict, not an inference from omission of an unspecified model detail. Display-precision intervals/relative discrepancy: not applicable to the method labels. No claim is made about the size of any resulting numerical change or about superiority of either model.

**Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed relationship type:** `P_R`. **All relationships:** `P_R`.

**Qualifying route:** Route B.

**Affected result or extracted value:** Time-specific PCS/MCS and EQ index/health adjusted mean differences and confidence intervals, including day30 PCS−0.861 (−2.829 to1.106), MCS−1.904 (−4.276 to0.469), and all treatment×time interaction tests in eTables2–4.

**Why context does not resolve it:** A reader cannot identify which covariance specification generated the printed quality-of-life estimates and intervals, or whether a change from the supplied SAP was adopted. The same outcome/time interaction description does not make independence and an unstructured repeated covariance identical.

**Supported alternatives and classification ambiguity:** The article may be describing a working covariance while robust inference was retained, or the model may have been revised for fitting/convergence reasons. Alternatively, its covariance description may refer to a different model level than the SAP repeated structure. No supplied printed explanation establishes one of these alternatives. Absence of an explicit robust-SE statement is not itself a finding.

**Human question:** Which repeated-measures covariance and variance estimator generated each SF-12/EQ-5D result, and was the SAP's unstructured specification replaced by independence under a documented analysis amendment?

### F-XS-004

**Title:** SAP incision-length subgroup boundaries assign exactly15cm to different groups.

**Compared locations and document roles:** PLAN [SAP data grouping §9.4, p17](../../../joi240145supp1_prod_1741627844.87412.pdf#page=17), [planned subgroups §9.9, p28](../../../joi240145supp1_prod_1741627844.87412.pdf#page=28), versus PLAN [AppendixD9 primary subgroup shell, p46](../../../joi240145supp1_prod_1741627844.87412.pdf#page=46). REPORT [Figure2 p9](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=9) corroborates the detailed-plan labels only.

**Printed statements/values:** Both substantive SAP sections define groups `<15cm` and `≥15cm`; AppendixD9 defines `≤15cm` and `>15cm`. Main Figure2 prints `<15` and `≥15`, with SSI event counts21/22 and90/81 and RR1.28 (0.76–2.16) and1.01 (0.79–1.29), interaction P=.42.

**Comparison logic:** Apply the printed inclusion criteria to an incision length exactly15cm. Detailed sections assign it to the second category; the reporting shell assigns it to the first. This is an analysis-group boundary, not merely another name for the same population. It is a repeated occurrence of one plan-internal grouping issue. Display-precision intervals/relative discrepancy: not applicable; subgroup cutpoints and their inclusion operators are exact rules, not rounded estimates. No number of exactly15cm participants is inferred.

**Focus area:** D. **Proposed review domain:** `plan_material`. **Proposed relationship type:** `P_P`. **All relationships:** `P_P`.

**Qualifying route:** Route B.

**Affected result or extracted value:** The primary SSI treatment effects by incision-length subgroup, and which participants are intended to contribute to each subgroup.

**Why context does not resolve it:** The shell is expressly the template for the prespecified primary subgroup analysis, yet it partitions exactly15cm differently from the accompanying analysis specification. The report follows the detailed-plan labels but cannot establish whether the implemented grouping followed those labels or the supplied template rule. This is a quantity-changing subgroup membership rule, not a symbol difference with invariant membership.

**Supported alternatives and classification ambiguity:** AppendixD9 may contain an outdated boundary and the substantive sections may have governed the analysis. Alternatively, the implementation could have used the template boundary while retaining detailed labels. Report Figure2 is corroborative evidence only; it is not needed to establish the PLAN-versus-PLAN conflict, so `P_R` is not added solely because of corroboration.

**Human question:** Which boundary was implemented for exactly15cm incisions, and which SAP specification governs the primary-outcome subgroup allocation?

### F-XS-005

**Title:** Unqualified no-difference quality-of-life narrative does not reconcile with the reported day7 EQ index test.

**Compared locations and document roles:** REPORT [main abstract p1](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=1), [Secondary Outcomes p6](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=6), versus REPORT [supplement eTable3 day7 and interaction result, p4](../../../joi240145supp3_prod_1741627844.89412.pdf#page=4). Confidence/significance conventions are stated in PLAN [SAP p12](../../../joi240145supp1_prod_1741627844.87412.pdf#page=12); this location corroborates the convention and does not introduce a PLAN-versus-REPORT conflict.

**Printed values/statements:** Abstract says six of seven secondary outcomes showed no significant difference, including quality of life. Main p6 says “There were no differences in quality of life between the 2 groups” and cites eTables2–4. eTable3 day7 EQ index prints adjusted mean difference−0.057 and P=.02, with the interval string `(-0.104 -0.010)`. Its treatment×time interaction P=.10. The other EQ index time-specific P values are.37,.49,.78; these do not erase the day7 test.

**Comparison logic:** Match the same EQ index component, randomized treatment contrast and included day7 timepoint to the broad statement explicitly referring to the complete quality-of-life tables. At the supplied two-sided significance level.05, day7 P=.02 is significant: its half-unit display interval [.015,.025] is wholly below.05. The narrative's no-significant-difference claim is unqualified by component, timepoint or hypothesis. The interaction P=.10 answers whether effects vary over time, not whether the time-specific day7 contrast equals zero. The ambiguous printed interval separator/sign is preserved; this finding rests on the unambiguous P=.02 and narrative, without selecting a sign interpretation. Display-precision relative discrepancy is not applicable to this significance-test conflict; Route A category1 is never rounding.

**Focus area:** B. **Proposed review domain:** `statistical_results`. **Proposed relationship type:** `S_C`. **All relationships:** `S_C`.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** Day7 EQ-5D index difference−0.057 and P=.02, and its classification as a secondary quality-of-life finding when extracted from the abstract/body versus eTable3.

**Why context does not resolve it:** Route A category1 applies to the printed significance-test conflict. Neither narrative location restricts its claim to a particular timepoint or an overall test. Their immediate reference includes the table containing the day7 contrast. The different-hypothesis interpretation is retained below for human review rather than used to suppress the observation.

**Supported alternatives and classification ambiguity:** The narrative may have intended an overall quality-of-life conclusion or the nonsignificant interaction rather than every component/time contrast. A planned omnibus treatment test could also have produced a nonsignificant result, but no such clearly labeled overall test is tied to this narrative. An isolated time-specific finding is not asserted to establish an overall longitudinal effect. The statistical checker may independently identify the same narrative/test issue; it should be consolidated at screening with all locations retained.

**Human question:** Does the no-difference quality-of-life statement refer to a specific overall hypothesis, the interaction, or all reported component/time contrasts, and how should the printed day7 EQ index P=.02 be represented in that statement?

## Excluded observations

Only apparent discrepancies considered and not emitted are listed. Reconciled checks are documented above, not counted as excluded observations.

| Location | Observation | Reason code |
|---|---|---|
| SAP p23; main p4; supplement p4 | SAP assigns zero to EQ index after death; main's available-case/no-imputation statement is phrased for “primary analyses.” No EQ-specific printed assertion establishes that planned post-death coding was omitted. A claim of changed EQ missingness would depend on unreported implementation. | CONDITIONAL_OR_UNREPORTED |
| Protocol pp24–25; SAP pp7,27; main Table3 p8 | Wound complication/readmission move under the heading “Secondary safety outcomes”; the heading retains secondary status, the same definitions and treatment contrasts, and is a safety subdivision rather than a demonstrable move out of the secondary hierarchy. | TERMINOLOGY_OR_WORDING |
| SAP pp26–27,44; protocol pp25,27; main p8 | Patient acceptability is described without its planned inferential contrast and the professional survey is absent. Neither is abstract-reported or designated key secondary; absent non-key analysis detail alone does not meet the planned-primary/key-secondary nonreporting category. | CONDITIONAL_OR_UNREPORTED |
| Protocol pp39–40; SAP p29; main report | Health-economic results are absent from the clinical report, but SAP expressly says the economic analysis is documented separately. No economic result or claimed economic conclusion conflicts. | CONTEXT_RESOLVES |
| Main pp4,6,8; protocol p2; SAP pp7,26 | Pain described as visual analogue, Likert, or a10-point scale; amendment records collection-tool terminology clarification and endpoints/time points agree. No treatment estimate is assigned to a different scale/time. | TERMINOLOGY_OR_WORDING |
| Main pp4,8; supplement p3 | PCS day30−0.86 versus−0.861 and MCS−1.90 versus−1.904, and their CI limits, are the same modeled quantities at different precision. Half-unit intervals overlap (e.g.−0.86 spans−0.865 to−0.855, encompassing the−0.861 interval); gap0, relative discrepancy0. | ROUNDING_OR_DISPLAY_PRECISION |
| Main p4; protocol pp2,25–29; SAP p13 and schedule p32 | Early assessment7–10days versus amended allowable5–10day window differs in described target versus permissible range. Disclosed relaxation and sensitivity-window treatment preserve the30-day event definition and explain the difference. | CONTEXT_RESOLVES |
| Protocol p17 inclusion list and conversion prose | Incision eligibility≥5cm versus converted-open prose>5cm is a plan-internal procedural boundary wording difference; no changed primary/key-secondary outcome, realized analysis-population size, or statistical decision rule is established. | PERIPHERAL_COMPARISON |
| Protocol p39; SAP p28; main pp4,9 | Protocol's shorter subgroup list versus expanded SAP list, including skin/BMI/incision/assessment/pandemic date. Protocol expressly delegates detailed methods to SAP, which contains every reported prespecified subgroup; no unsupported prespecification claim remains. | CONTEXT_RESOLVES |
| Main Table3 p8; supplement eTable5 p5 | Main participant-level wound grade totals differ from supplementary complication-type grade totals. Supplement explicitly permits multiple complication types per participant, so they are different counted quantities. | CONTEXT_RESOLVES |

## Limitations and completion

Cross-source coverage is complete for all supplied mapped source units and relationships. No raw participant data, execution output, populated analysis-deviation log, dated/approved SAP amendment, or DMC charter is supplied. These omissions limit attribution of implementation and numerical impact; they do not justify assuming an unreported method or omitting supplied evidence. Reused extraction engine versions are partly unavailable, but exact source text confirmation was obtained for the principal method/population conflicts, and independent mechanical evidence recheck must confirm every included finding. Intermediate tipping-point values are not printed and were not invented. No scientific-coverage gap, fresh OCR need, or external evidence use occurred in this stage.
