# Statistical pass 1: independent design and method shard

- Agent task/runtime reference: `/root/statistics_1_design`; parent records the fresh spawn runtime ID.
- Model and effort contract: gpt-6.1-sol / high; FRESH_SPAWN.
- Exact scope: S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120, S121, S122, S123, S124, S125, S126, S127, S128, S129.
- Counts: 29 relationships reviewed; 1 finding; 15 excluded observations. Every assigned relationship is PASS_1_COMPLETE. Canonical inventory and checker remain owned by the coordinator/main statistical agent.

Read QUALITY_CONTROL_SCOPE.md, the complete 1.6.1 review contract, and tooling_record.md. Reviewed only assigned inventory rows and their source-linked evidence. Source authority: direct pdftotext native/layout output from supplied PDFs, with visual source-page confirmation of the primary composite definitions using rendered main p. 3, PLAN p. 16, and supplementary REPORT p. 2. Sources and pre-existing derivatives were preserved. Direct pdftotext 25.03.0; no fallback environment, OCR, Python extraction, web, or legacy conclusions used. Methods and numerical conclusions were checked against the statements actually supplied, with no inferred covariance, variance estimator, degrees of freedom, sample-size formula, or estimand mapping.

## Relationship completion records

| S ID | Source-grounded check and result | Pass 1 |
|---|---|---|
| S101 | Main p. 3 and PLAN p. 7 describe 1:1 stratified hospital randomization; main p. 4 describes GEE within-hospital correlation. Forty clusters and 2400 patients per arm agree; no contradictory required covariance specification. | PASS_1_COMPLETE |
| S102 | Main p. 3 defines patient fractions averaged; PLAN p. 16 defines a ratio of totals. Supplementary REPORT p. 2 repeats the ratio of totals and says the randomized phase used the same definition. See F-ST1-101. | PASS_1_COMPLETE |
| S103 | Main p. 3 and PLAN p. 16 all-or-none definition applies all interventions for which each patient is eligible; eligibility context reconciles compact wording. | PASS_1_COMPLETE |
| S104 | Main p. 4 and PLAN pp. 18–19 explicitly model each eligible care opportunity as a binary observation for ORPA. The 5-of-7 example is illustrative and does not replace the nine trial measures. | PASS_1_COMPLETE |
| S105 | Main p. 4 logistic/GEE analysis of binary all-or-none aligns with PLAN pp. 18–19 qualitative population-average odds ratios and within-hospital correlation. | PASS_1_COMPLETE |
| S106 | Main pp. 4 and 8 explicitly describe a binary-link mixed model for disability; logistic regression is compatible with a binary-link model. PLAN pp. 18–19 gives general correlation-aware modeling, without a contradictory disability-specific fixed method. | PASS_1_COMPLETE |
| S107 | Main p. 4 and PLAN p. 19 specify time-to-event vascular events/mortality, Kaplan–Meier and multivariable Cox models. Cluster variance/frailty details are not supplied; their absence does not establish a contradiction. | PASS_1_COMPLETE |
| S108 | Main p. 4 states cumulative incidences and absolute differences adjusted for patient/hospital baseline characteristics; PLAN p. 18 allows quantitative mean differences. Exact difference-generation steps are absent, without a reproduced incompatibility. | PASS_1_COMPLETE |
| S109 | Main pp. 4, 7–8 list consistent patient/hospital covariates. PLAN p. 18 permits identifying possible control variables and supplies no conflicting mandatory fixed list. | PASS_1_COMPLETE |
| S110 | Main p. 4 identifies 4800 in primary analysis and main p. 7 uses 2400/arm for adherence. Main p. 5 flow boxes follow loss to 12-month follow-up; 2003+1977=3980 completers. Immediate adjacent boxes identify those counts. | PASS_1_COMPLETE |
| S111 | Main p. 8 disability denominators at 12 months: 1852+1798=3650; deaths:139+160=299; 3650+299=3949 matches available one-year mRS in supplementary REPORT p. 5. Follow-up completers 3980 exceed available mRS 3949 by 31, without a contradiction in endpoint availability. | PASS_1_COMPLETE |
| S112 | Main p. 4 states mode/median covariate imputation, 1.42% smoking missing and one NIHSS imputed 3. Main p. 6 reports group NIHSS medians 4, supplementary REPORT p. 5 medians 3; supplied text does not identify the distribution used for imputation. No result-level consequence is established by the comparison. | PASS_1_COMPLETE |
| S113 | Main p. 4 uses median(IQR), Wilcoxon and chi-square; PLAN p. 18 allows median(IQR)/Mann–Whitney for skewed distributions. No source-established normality assumption contradicts reported choice. | PASS_1_COMPLETE |
| S114 | Supplementary REPORT p. 5 gives 3949/851 mRS availability groups and ten baseline P values. A named table-specific estimator/adjustment is not supplied, so no exact Pearson/cluster-adjusted mapping is inferred. | PASS_1_COMPLETE |
| S115 | Main p. 4 and PLAN p. 17 agree baseline 80%, detectable 5%, power 80%, alpha 5%, ICC .02, 40 clusters, 120 per cluster, 4800 total. Cluster/patient arithmetic 40×120=4800 and 2×2400=4800 reproduces. Score variance and calculation formula absent; a binary-proportion sample-size reconstruction would be conditional. | PASS_1_COMPLETE |
| S116 | Main p. 4 enrollment stopping at 2400/group agrees main pp. 5,7 and PLAN p. 17 target 4800. No efficacy stopping rule or numerical interim conclusion is reported. | PASS_1_COMPLETE |
| S117 | PLAN p. 20 committee authority to terminate/modify/continue does not supply a numerical efficacy boundary; REPORT supplies no actual interim decision to compare. | PASS_1_COMPLETE |
| S118 | Main pp. 3–4 explicitly says either co-primary significant makes study positive, no multiplicity adjustment, two-sided P<.05. Composite P=.02/.003 and all-or-none P=.06/.31 support main p. 5 statements under that stated rule. No contradictory PLAN decision threshold. | PASS_1_COMPLETE |
| S119 | Main p. 4 labels secondary analyses exploratory. Main pp. 5,8 vascular/disability claims use nominal P<.05; no external multiplicity requirement is substituted for this coherent stated rule. | PASS_1_COMPLETE |
| S120 | Main pp. 3,7; PLAN pp. 13–16; supplementary REPORT pp. 3–4 give nine measures and eligibility. rtPA arrival≤2 hours and treatment≤3 hours reconcile labels. LDL>100 versus≥100 is clarified by detailed measure definition and does not establish a changed primary result. | PASS_1_COMPLETE |
| S121 | Main p. 3 and PLAN p. 16 specify 3/6/12 months after symptom onset. Main p. 5 isolated discharge wording contrasts with main p. 8 explicit onset footnote and axis. Source context makes the displayed follow-up origin immediately identifiable. | PASS_1_COMPLETE |
| S122 | Main p. 4 and PLAN p. 19 specify sensitivity inclusion of contraindications. Supplementary REPORT pp. 8–9 denominators reflect each measure's indication, not universal eligibility for all 4800; adjusted effects are not crude ratios. | PASS_1_COMPLETE |
| S123 | Main p. 3 and PLAN pp. 8–13 match four components, 2-day training, daily first 7 days/discharge and weekly monitoring. Three feedback cycles follow enrollment batches; no competing randomized intervention duration established. | PASS_1_COMPLETE |
| S124 | Main p. 3/PLAN p. 7 strata and main p. 4 adjustment list differ in purpose. No supplied promise requires all strata appear verbatim in the model list. | PASS_1_COMPLETE |
| S125 | Main p. 3, PLAN pp. 13–16 match co-primary adherence and clinical secondary identities/hierarchy. Composite weighting issue consolidated under S102, rather than emitted twice. | PASS_1_COMPLETE |
| S126 | Supplementary REPORT p. 2 describes 20/cluster; main p. 6 displays 801 survey participants across 40 clusters. The difference does not change randomized 4800, power assumptions, or planned decision rule. | PASS_1_COMPLETE |
| S127 | Main p. 5 safety 1/46 versus 2/23, P=.26 and main p. 4 definition identify symptomatic hemorrhage. No named safety test/variance mapping supplied; exact test incompatibility not inferred. | PASS_1_COMPLETE |
| S128 | Supplementary REPORT pp. 6–7 explicitly allows a patient to have different vascular-event types. Sum of component counts need not equal the main p. 8 count of patients with any event; PLAN p. 16 composite definition is coherent. | PASS_1_COMPLETE |
| S129 | PLAN p. 18 qualitatively labels ORPA and quantitatively mean difference; main pp. 4,7–8 labels adjusted absolute differences, ORPA, HR, OR. No printed identity requires crude RR reconstruction. | PASS_1_COMPLETE |

## Findings

### F-ST1-101

Primary composite adherence has patient-level and pooled care-opportunity weighting definitions across REPORT and PLAN.

**Locations and document roles:**

- REPORT: [main article PDF p. 3, Outcomes, final primary-outcome paragraph](../../../../jama_wang_2018_oi_180070.pdf#page=3), and [PDF p. 7, Table 2 composite row](../../../../jama_wang_2018_oi_180070.pdf#page=7).
- PLAN: [protocol PDF p. 16, lines 216–220](../../../../joi180070supp1_prod.pdf#page=16).
- REPORT: [results supplement PDF p. 2, eAppendix composite definition and randomized-phase statement](../../../../joi180070supp2_prod.pdf#page=2).
- Analysis context: REPORT [main PDF p. 4, opportunity-level ORPA analysis](../../../../jama_wang_2018_oi_180070.pdf#page=4) and PLAN [protocol pp. 18–19, opportunity-level analysis](../../../../joi180070supp1_prod.pdf#page=18).

**Printed values/statements:** Main p. 3 defines performed eligible measures divided by eligible measures for a given patient, calculated for each patient and then averaged. Table 2 labels the composite mean (SD), 88.2(15.1) versus 84.8(18.2), adjusted difference 3.5(95% CI 0.7–6.4), P=.02; modeled ORPA 1.39(1.12–1.72), P=.003. PLAN p. 16 instead defines total interventions performed among eligible patients divided by total possible interventions among eligible patients. Supplementary REPORT p. 2 repeats that ratio-of-totals definition and explicitly says the same endpoint definition was used in the randomized phase.

**Rule and calculation:** Write fulfilled opportunities for patient i as a_i and eligible opportunities as b_i. Main's descriptive definition is U=(1/n)Σ(a_i/b_i). The pooled definition is W=(Σa_i)/(Σb_i)=Σ[b_i/Σb_j](a_i/b_i). The definitions assign different weights when b_i vary. This is an algebraic distinction, independent of printed decimal rounding. Diagnostic illustration only, not trial-data reconstruction: with 1/1 and 0/3, U=.5 and W=.25. Source measure-specific denominators differ, and neither source claims all patients have the same number of eligible measures. Opportunity-level modeled ORPA is explicitly a separate result; no crude-versus-modeled comparison is used to support the observation.

**Focus area:** D, planned versus reported primary endpoint definition; additionally C for matching the primary descriptive quantity across REPORT locations.

**Proposed review domain:** protocol_report.

**Proposed relationship type:** P_R. **All relationships:** P_R,S_C. The supplement repeats the pooled definition for the randomized phase; it therefore supplies a separate REPORT-to-REPORT endpoint-definition comparison. No plan-internal contradiction is asserted.

**Affected result or extracted value:** The primary composite adherence scores 88.2% versus 84.8% and the interpretation of the reported composite improvement are described using distinct weighting definitions. This concerns the primary endpoint, rather than merely baseline survey percentages. The supplied evidence does not determine the numeric size of any weighting effect in this trial or establish a change in statistical significance.

**Why context does not resolve it:** A per-patient mean and a pooled proportion are both plausible composite measures. Main text explicitly distinguishes its patient averaging while the protocol states pooled weighting, and the supplement says its pooled definition was used in the randomized phase. The opportunity-level ORPA paragraph specifies how that modeled effect was obtained, but does not state which endpoint definition governs each displayed descriptive score or disclose a change from the planned definition. The immediate context thus supplies competing definitions rather than a single intended meaning.

**Source-grounded alternatives and missing definitions:** The randomized descriptive score may be the main-text patient mean with a disclosed or undisclosed change from the pooled plan; alternatively, pooled wording may abbreviate patient-level aggregation, or different definitions may govern baseline versus randomized descriptive summaries. The supplementary claim of the same randomized endpoint prevents assuming the last explanation. The missing clarification is the exact aggregation/weighting used for each randomized composite score and its relation to the planned primary definition. No preferred analysis is proposed.

**Exact human question:** Was the randomized primary composite score calculated as an unweighted mean of individual patients' eligible-measure fractions or as the pooled proportion of all eligible care opportunities fulfilled, and how should the main-text definition be reconciled with the protocol and supplement's stated randomized-phase definition?

**Self-screen:** Source wording visually confirmed; primary endpoint in focus; weighting distinction is substantive; no numerical correction, severity, validity, or disposition assigned. Consolidates S102/S125 manifestations into one finding. The coordinator should consolidate with any independently emitted finding describing this same weighting pattern.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| Main p. 3; PLAN p. 16; S103 | All-or-none wording omits “for which eligible” in one compact phrase, while surrounding specifications define eligible patients/measures. | TERMINOLOGY_OR_WORDING |
| Main p. 4; PLAN pp. 18–19; S104 | The 5-of-7 example appears beside a trial with 9 measures; it is explicitly an example explaining per-opportunity observations. | CONTEXT_RESOLVES |
| Main pp. 4,8; PLAN pp. 18–19; S106 | Logistic description and binary-link mixed model are not source-established mutually exclusive analyses. Table 3 names the disability model. | CONTEXT_RESOLVES |
| Main p. 4; PLAN pp. 18–19; S107,S108 | Exact clinical cluster variance/frailty and adjusted absolute-difference-generation steps are not reported; absent detail alone does not reproduce an inconsistency. | CONDITIONAL_OR_UNREPORTED |
| Main pp. 3–4; PLAN pp. 7,18; S109,S124 | Requiring all randomization strata verbatim in adjustment would impose an unstated preferred model. | OUT_OF_FOCUS |
| Main pp. 4–5,7; S110 | Flow diagram's 2003/1977 labels follow 12-month attrition boxes; text and Table 2 identify 4800 adherence participants at once. | CONTEXT_RESOLVES |
| Main pp. 4,6; supplementary REPORT p. 5; S112 | NIHSS imputation 3 versus group medians 4 does not establish the distribution used for imputation; impact on a named result is not supplied. | CONDITIONAL_OR_UNREPORTED |
| Main p. 4; PLAN p. 18; S113 | Difference in permitted summaries/tests depends on unreported normality and does not contradict the plan's skewed-distribution option. | CONDITIONAL_OR_UNREPORTED |
| Supplementary REPORT p. 5; S114 | Baseline mRS-availability P values do not supply a table-specific model/estimator, precluding an exact assumed Pearson/cluster test comparison. | CONDITIONAL_OR_UNREPORTED |
| Main p. 4; PLAN p. 17; S115 | A sample-size reconstruction using a binary-score variance would assume an unstated distribution/formula for the composite; stated allocation arithmetic agrees. | CONDITIONAL_OR_UNREPORTED |
| PLAN p. 20; main p. 4; S117 | Committee stopping authority without a reported quantitative interim decision does not establish a failed numerical boundary. | CONDITIONAL_OR_UNREPORTED |
| Main p. 3; PLAN pp. 14–16; supplementary REPORT pp. 3–4; S120 | Compact rtPA timing and LDL>100/≥100 wording are resolved by detailed eligibility specifications, with no identified changed primary value. | CONTEXT_RESOLVES |
| Main pp. 3,5,8; PLAN p. 16; S121 | Isolated discharge origin wording is immediately resolved by explicit onset definition, Table 3 footnote and Figure 2 axis. | CONTEXT_RESOLVES |
| Main p. 6; supplementary REPORT p. 2; S126 | 20 survey patients per cluster versus 801 observed across 40 clusters is baseline descriptive and does not change randomized population or planned power rule. | PERIPHERAL_COMPARISON |
| Main p. 5; S127 | Safety P=.26 has no named test/variance mapping; selecting an exact test by convention would make incompatibility conditional. | CONDITIONAL_OR_UNREPORTED |

## Limits

No scientific coverage gap within this shard. Exact reproduction of power/sample-size and several table-specific tests remains unavailable because named necessary definitions are absent, as recorded above. Diagnostic algebra illustrates distinct weights only; it does not estimate trial-level change. Covariance, repeated-measure/random-effect structure, clinical-event variance estimation and marginalization were not inferred. The complete inferential-results universe S001–S100 is owned by the parallel pass-1 agent and is outside this artifact's scope.
