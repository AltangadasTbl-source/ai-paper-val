# Workflow 1.6.2 Candidate Ledger

Pending Human Adjudication. Twenty-one distinct issues were registered after the initial independent screen completed all 34 findings. C022 was appended after a different fresh screener included the new pass-2 finding; no earlier ID was renumbered. Source order uses the earliest substantive REPORT location, then its display order, followed by PLAN-only source locations; supporting method locations do not reorder a result card. Every repeated pattern preserves all affected rows and locations. Duplicate finding provenance remains attached, while the classification Finding IDs column contains only INCLUDE findings.

## Classification table

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT main abstract p.1 vs REPORT main enrolled counts p.4 | reproduced | CONFIRMED | F-NUM-001 |
| C002 | protocol_report | P_R | P_R | PLAN protocol pp.12,40-41 vs REPORT main pp.3-4,6 and results supplement pp.10-14 | reproduced | CONFIRMED | F-XS-002 |
| C003 | protocol_report | P_R | P_R | PLAN protocol pp.7,31,40 vs REPORT main pp.3-4,7-8 | reproduced | CONFIRMED | F-XS-003 |
| C004 | protocol_report | P_R | P_R | PLAN protocol pp.32-33 vs REPORT main pp.3,5,7-8 | reproduced | CONFIRMED | F-XS-004 |
| C005 | protocol_report | P_R | P_R | PLAN protocol p.35 vs REPORT main pp.3-4,8 and results supplement p.5 | reproduced | CONFIRMED | F-XS-005 |
| C006 | protocol_report | P_R | P_R | PLAN protocol p.40 vs REPORT main pp.3-4 and results supplement pp.11-14 | reproduced | CONFIRMED | F-ST1-207 |
| C007 | statistical_results | S_C | S_C, S_W | REPORT main stopping rule p.3 and response statement p.4 vs REPORT results supplement p.5 | reproduced | CONFIRMED | F-XS-007 |
| C008 | statistical_results | S_W | S_W | REPORT main Table 1 row and scale footnote p.5; corroborating Table 2 scale footnote p.8 | reproduced | CONFIRMED | F-NUM-004 |
| C009 | statistical_results | S_W | S_W | REPORT main Table 1 medication and sex rows plus test footnote p.5 | reproduced | CONFIRMED | F-ST1-010 |
| C010 | statistical_results | S_W | S_W | REPORT main repeated narrative p.6 vs Table 2 subgroup row p.7 and test rule p.4 | reproduced | CONFIRMED | F-ST1-004 |
| C011 | statistical_results | S_W | S_W | REPORT main Table 2 lower header and repeated outcome rows p.7 with direction footnotes p.8 | reproduced | CONFIRMED | F-ST1-008 |
| C012 | statistical_results | S_W | S_W | REPORT main Table 2 physical SF-36 period row and comparator rows p.7; methods pp.3,8 | reproduced | CONFIRMED | F-ST1-012 |
| C013 | statistical_results | S_W | S_W | REPORT main Table 2 mental SF-36 row p.7 vs dependent-test methods pp.3-4,8 | reproduced | CONFIRMED | F-ST1-005 |
| C014 | statistical_results | S_W | S_W | REPORT main Table 2 first-handgrip placebo mean and interval p.7; scale and method footnotes p.8 | reproduced | CONFIRMED | F-ST1-001 |
| C015 | statistical_results | S_W | S_W | REPORT main Table 2 eleven named non-IVR rows p.7 vs dependent-test and availability methods pp.3-4,8 | reproduced | CONFIRMED | F-ST1-009 |
| C016 | statistical_results | S_W | S_W | REPORT main Table 2 fifth-handgrip SCN4A row p.7 and repeated narrative p.8; rule p.4 | reproduced | CONFIRMED | F-ST1-003 |
| C017 | statistical_results | S_W | S_W | REPORT main Table 2 first-eyelid row p.7 vs strict significance rule p.4 and method footnotes p.8 | reproduced | CONFIRMED | F-ST1-007 |
| C018 | statistical_results | S_W | S_W | REPORT main Table 2 mean Timed Up and Go placebo point and interval p.7; footnotes p.8 | reproduced | CONFIRMED | F-ST1-002 |
| C019 | statistical_results | S_W | S_W | REPORT main Table 2 needle-EMG row p.8 vs dependent-test and two-sided methods pp.3-4 | reproduced | CONFIRMED | F-ST1-006 |
| C020 | plan_material | P_P | P_P | PLAN protocol DSMB text p.38 vs PLAN protocol safety diagram p.39 | reproduced | CONFIRMED | F-XS-009 |
| C021 | plan_material | P_P | P_P | PLAN protocol noninformative-only interim text p.42 vs PLAN protocol informative-prior arrows p.43 | reproduced | CONFIRMED | F-XS-008 |
| C022 | statistical_results | S_W | S_W | REPORT main Table 2 total and genotype baseline means p.7 with nominal genotype counts and baseline footnote p.8; available-data context p.4 | reproduced | CONFIRMED | F-ST2-001 |

## C001 — Abstract male percentage differs from the enrolled sex counts

Pending Human Adjudication.

**Qualifying route:** Route A, category 2
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main abstract p.1 vs REPORT main enrolled counts p.4
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-NUM-001
**Checker provenance:** F-NUM-001, F-XS-001
**Classification rationale:** The conflicting numbers, interval, label or test appear within one REPORT document. Plan material does not supply a conflicting comparator.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-NUM-001 — INCLUDE:** Route A, category 2 applies because the abstract's printed 22% men among 30 enrolled participants does not reconcile with the body count of 22 men under the full half-unit rule and changes the abstract demographic value taken for extraction.

Locations: REPORT [DOC-001 abstract p.1](../../jama_stunnenberg_2018_oi_180136.pdf#page=1) versus REPORT [DOC-001 Baseline Data p.4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4); REPORT [DOC-003 eTable 2 p.3](../../joi180136supp2_prod.pdf#page=3) and [p.4](../../joi180136supp2_prod.pdf#page=4) corroborate the body without creating a separate conflicting relationship. Recomputed interval is 100×[21.5/30.5,22.5/29.5]=[70.491803,76.271186]%; printed percentage interval [21.5,22.5]%; gap 47.991803, relative gap 2.181446 >0.05. Relationship S_W; review domain statistical_results. The reading that 22 was intended as a count remains an alternative, not a replacement of the printed percentage. Consolidate F-XS-001 here and preserve its corroborating locations.


### Source-linked checker evidence

#### F-NUM-001

**Title:** Abstract male percentage does not reconcile with enrolled male count.

**Relationships:** N003; N060. **Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W; DOC-003 merely corroborates the body count and is not a separate conflicting relationship.

**Compared locations and document roles:** REPORT [main PDF p.1 abstract Results](../../jama_stunnenberg_2018_oi_180136.pdf#page=1), REPORT [main PDF p.4 Baseline Data](../../jama_stunnenberg_2018_oi_180136.pdf#page=4). Corroborating REPORT [results supplement pp.3–4 eTable 2](../../joi180136supp2_prod.pdf#page=3).

**Printed inputs:** Abstract: “30 patients enrolled” and “22% men.” Body: 22 men and 8 women among 30 enrolled. eTable 2 contains 22 male and 8 female rows.

**Rule and calculation:** Sex percentage = 100 × male count / enrolled count. Counts exact: 100×22/30 = 73.333333%. Recomputed interval [73.333333,73.333333]; abstract whole-percentage interval [21.5,22.5]. Gap = 50.833333 percentage points; relative discrepancy = 50.833333/22 = 2.310606, above .05. Enrolled counts 22+8=30 reconcile.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** Male percentage of the enrolled analysis population as taken from the abstract.

**Why context does not resolve it:** Route A category 2 applies to a printed percentage whose magnitude changes the reading; reconstructing 73.3% from the body does not remove the conflicting abstract number.

**Alternatives and missing definitions:** The abstract “22%” may have been intended as the count 22 rather than a percentage. No alternative enrolled denominator is stated that yields 22%.

**Exact human question:** What male percentage or male count should be extracted for the 30 enrolled participants, and how should the abstract “22% men” be read?


#### F-XS-001 — Abstract enrolled male proportion does not reconcile with enrolled sex counts

- **Locations and roles:** [DOC-001 abstract Results p.1](../../jama_stunnenberg_2018_oi_180136.pdf#page=1), REPORT; [DOC-001 Baseline Data p.4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), REPORT. Supplement [DOC-003 eTable 2 pp.3–4](../../joi180136supp2_prod.pdf#page=3) corroborates enrolled sex identities; it is REPORT and does not create a separate conflict.
- **Printed statements:** Abstract: 30 enrolled, “22% men.” Body: “Twenty-two men and 8 women” enrolled.
- **Comparison logic/calculation:** Same enrolled population. 22/30×100=73.333%, versus 22%. Conservatively allowing half-unit intervals for both count inputs yields 100×[21.5/30.5,22.5/29.5]=[70.492,76.271]%; abstract percentage interval [21.5,22.5]%; gap 47.992 percentage points; relative discrepancy 47.992/22=2.1815 (>0.05). Exact integer counts strengthen the discrepancy.
- **Focus area:** A. **Proposed review domain:** statistical_results. **Relationship:** S_W.
- **Qualifying route:** Route A, category 2.
- **Affected result or extracted value:** Enrolled sample male percentage extracted from the abstract.
- **Why context does not resolve it:** Route A printed percentage changes the sample reading despite body counts permitting reconstruction.
- **Supported alternatives:** “22” may refer to the male count rather than percentage; no normalization is imposed.
- **Human question:** Which enrolled male proportion should be retained, and what does the abstract's 22% represent?



## C002 — Planned primary priors and robustness analyses differ from the supplied implementation

Pending Human Adjudication.

**Qualifying route:** Route A, category 5
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN protocol pp.12,40-41 vs REPORT main pp.3-4,6 and results supplement pp.10-14
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-002
**Checker provenance:** F-XS-002, F-ST1-201, F-ST1-202
**Classification rationale:** The conflicting comparison concerns prospective PLAN content and REPORT analysis or endpoint content; report code corroborates the reported side. P_R takes precedence.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-XS-002 — INCLUDE:** Route A, category 5 applies because the supplied plan promises observed primary analyses under elicited clinical priors and their noninformative-prior robustness comparison, while the reported primary implementation specifies different priors and supplies no corresponding clinical-prior robustness result.

Consolidated primary-prior specification/robustness pattern includes F-ST1-201 and F-ST1-202. Retain PLAN [DOC-002 study design p.12](../../joi180136supp1_prod.pdf#page=12), [multivariate/prior specification p.40](../../joi180136supp1_prod.pdf#page=40), [variance prior/clinical prior/robustness p.41](../../joi180136supp1_prod.pdf#page=41); REPORT [DOC-001 Bayesian method p.3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [primary result p.4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), [Figure 3 p.6](../../jama_stunnenberg_2018_oi_180136.pdf#page=6); REPORT [DOC-003 individual code p.10](../../joi180136supp2_prod.pdf#page=10), [group code p.11](../../joi180136supp2_prod.pdf#page=11), [group glossary p.12](../../joi180136supp2_prod.pdf#page=12), [subgroup code p.13](../../joi180136supp2_prod.pdf#page=13), [subgroup encoding p.14](../../joi180136supp2_prod.pdf#page=14). Plan inverse-gamma variation priors with shape/scale0.001 differ from code uniform SD(0.01,10); clinical effect prior N(1.75,0.89²) differs from code arm means dnorm(4,0.001) and subgroup coefficients dnorm(0,0.01). Uniform-SD implies a variance density proportional to variance^−1/2 on(0.0001,100), not the planned inverse-gamma distribution. The variance-family difference additionally meets Route B. Wide individual-interim priors are allowed by PLAN p.42 and are not a separate conflicting analysis; p.10 remains contextual evidence. Searches of the complete current-source report texts found no observed informative/noninformative primary comparison; prospective and post hoc simulations answer different questions. The named result is overall stiffness3.06(95%CrI1.96–4.15) and genotype posterior effects/probabilities. An unsupplied revision remains an alternative. P_R; protocol_report.


### Source-linked checker evidence

#### F-XS-002 — Planned primary clinical-prior and robustness analyses are replaced by different printed priors without their results

- **Locations and roles:** [DOC-002 Study Design p.12](../../joi180136supp1_prod.pdf#page=12), [§9.1 pp.40–41](../../joi180136supp1_prod.pdf#page=40), PLAN; [DOC-001 Bayesian Analysis p.3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), REPORT; [DOC-003 eMethods 2 pp.11–12](../../joi180136supp2_prod.pdf#page=11) and [eMethods 3 pp.13–14](../../joi180136supp2_prod.pdf#page=13), REPORT.
- **Printed statements:** Plan requires clinical priors for individual treatment effects and overall mean effect, almost noninformative remaining parameters, inverse-gamma variance priors with shape/scale 0.001; elicited overall effect prior normal mean 1.75/SD 0.89. It explicitly promises robustness comparison replacing elicited priors with noninformative priors. Implemented group code instead specifies independent arm means `dnorm(4,0.001)`, subgroup coefficients `dnorm(0,0.01)` and each SD `dunif(0.01,10)`. The complete main article/results supplement reports no paired clinical-prior/noninformative-prior primary results.
- **Comparison logic:** The supplied implemented primary group/subgroup code contains a different prior specification and no elicited effect prior; neither report document supplies the prospective primary sensitivity comparison. This finding combines the primary-prior replacement and its omitted planned robustness counterpart, rather than treating every prior line as a separate issue. Numeric rounding is inapplicable to distribution-family/analysis-presence differences.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Overall primary stiffness effect 3.06 (95% CrI 1.96–4.15), clinically meaningful probability 100%, and genotype estimates/probabilities, whose planned robustness under clinical priors is not reported.
- **Why context does not resolve it:** Route A covers a planned primary analysis that is replaced or not reported. The reported post hoc sample-size simulation is not an analysis of observed efficacy under alternative priors.
- **Supported alternatives:** A later amendment may have selected the printed priors; clinical-prior sensitivity may exist outside the supplied package. Neither is supplied. The vague individual interim prior is separately allowed by plan §9.2 and is not itself this issue.
- **Human question:** Was the observed primary analysis under elicited clinical priors and its planned prior-sensitivity comparison conducted, and which specification/amendment generated the reported posterior results?


#### F-ST1-201 — Primary variance priors differ from the prospective specification

- **Relationships:** S223, S226. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R; all relationships P_R.
- **Exact locations/document roles:** PLAN [DOC-002 p.40 §9.1 prior section](../../joi180136supp1_prod.pdf#page=40) and [p.41 prior distributions](../../joi180136supp1_prod.pdf#page=41); REPORT [DOC-003 p.10 eMethods1](../../joi180136supp2_prod.pdf#page=10), [p.11 eMethods2](../../joi180136supp2_prod.pdf#page=11), [p.13 eMethods3](../../joi180136supp2_prod.pdf#page=13); REPORT [DOC-001 p.3 Bayesian Analysis](../../jama_stunnenberg_2018_oi_180136.pdf#page=3) and [p.4 primary result](../../jama_stunnenberg_2018_oi_180136.pdf#page=4).
- **Printed statements:** PLAN p.41: “For the variation parameters we will use inverse gamma distributions with both shape and scale parameters equal to0.001.” REPORT primary group/subgroup code instead has sigma.within,sigma.mex,sigma.plac~dunif(0.01,10) and tau=1/sigma². Planned clinical versus noninformative treatment-effect priors are tracked separately asF-ST1-202; PLAN p.42 explicitly permits noninformative-only individual interim analyses, so their wide mean priors are not treated as a conflicting side here.
- **Rule/calculation:** The printed primary variance-prior family is inverse gamma on variance in the plan versus uniform on SD in reported code. IfSD~Uniform(0.01,10), variance has support0.0001–100 and density proportional to1/sqrt(variance), which is not inverse gamma(shape0.001,scale0.001) with support positive real numbers. This elementary transformation identifies a specification difference without calculating or assuming a changed posterior. Display rounding cannot turn one prior family/support into the other; numeric discrepancy intervals are not applicable to different distributions/parameters.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Bayesian primary total effect3.06 (95%CrI1.96–4.15) and genotype effects/probabilities.
- **Why context does not resolve it:** Both versions explicitly specify the variation prior family; the report references the supplied protocol but supplies no amendment or explanation linking inverse-gamma variance priors to uniform-SD priors. Calling both noninformative does not identify the same distribution. B1 concerns primary analysis priors, B2 lacks source reconciliation, B3 bears on the posterior results' model interpretation.
- **Alternatives/missing definitions:** The report may intentionally implement revised noninformative variance priors. The supplied code may represent only one of additional model implementations. Posterior sensitivity cannot be quantified without data and model execution. No preferred prior is proposed.
- **Exact human question:** Which variance/SD priors produced the reported primary posterior results, and what supplied amendment or analysis record reconciles the inverse-gamma variance specification with the uniform-SD implementation?


#### F-ST1-202 — Planned primary informative-prior robustness analysis has no supplied result

- **Relationships:** S205. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R; all relationships P_R.
- **Exact locations/document roles:** PLAN [DOC-002 p.12 study design](../../joi180136supp1_prod.pdf#page=12), [p.41 robustness paragraph](../../joi180136supp1_prod.pdf#page=41); REPORT [DOC-001 p.3 primary Bayesian method](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [p.4 primary result](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), [p.6 Figure3](../../jama_stunnenberg_2018_oi_180136.pdf#page=6); REPORT [DOC-003 pp.10–14 implemented primary models](../../joi180136supp2_prod.pdf#page=10). Complete supplied report/supplement maps were searched for the counterpart.
- **Printed statements:** PLAN p.12: “we will test robustness of the method, by comparing results when using noninformative or informative priors”; p.41: “we will also replace the elicited prior distributions with non-informative priors in our analyses.” REPORT provides one noninformative-prior primary posterior analysis and associated effects/probabilities, without an informative versus noninformative primary result comparison. PLAN p.21's0.817/0.821 versus0.782/0.784 are prospective simulation outputs, not analyses of observed trial data.
- **Rule/calculation:** A prespecified primary sensitivity/robustness analysis must have an identifiable reported result or an explanation of its status; none is supplied. This is an absence of a named planned primary analysis, confirmed over complete report units, not inference from one paragraph. No rounding arithmetic applies.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Robustness of the primary stiffness posterior effect and probability of benefit>0.75 to the elicited versus noninformative priors.
- **Why context does not resolve it:** Category5 always registers an unreported planned primary analysis. The prospective simulation and post hoc stopping simulation answer different questions and do not supply this observed-data prior sensitivity comparison.
- **Alternatives/missing definitions:** A revision may have intentionally removed the analysis; it may have been run but not supplied. This finding concerns its reporting status and is distinct from F-ST1-201's actual prior specification.
- **Exact human question:** Where is the planned observed-data informative-versus-noninformative primary robustness analysis, or the documented change to its prespecified status?



## C003 — Non-IVR secondary analysis specification differs from the plan

Pending Human Adjudication.

**Qualifying route:** Route B
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Final support qualification:** Formal secondary labels are retained by the report. The retained reporting issue is the concrete planned Bayesian versus reported dependent-t specification for non-IVR secondary endpoints, qualifying by Route B. Earlier checker/screen status-language interpretations below are provenance, not the final candidate assertion.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN protocol pp.7,31,40 vs REPORT main pp.3-4,7-8
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-003
**Checker provenance:** F-XS-003
**Classification rationale:** The conflicting comparison concerns prospective PLAN content and REPORT analysis or endpoint content; report code corroborates the reported side. P_R takes precedence.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-XS-003 — INCLUDE:** Route A, category 5 applies conservatively to the printed contrast between planned secondary outcome status and reported exploratory interpretation, with the concrete replacement of planned Bayesian secondary analyses by dependent-t analyses retained in the same secondary-analysis pattern for human clarification.

Locations: PLAN [DOC-002 summary p.7](../../joi180136supp1_prod.pdf#page=7), [secondary endpoints p.31](../../joi180136supp1_prod.pdf#page=31), [secondary-analysis statement p.40](../../joi180136supp1_prod.pdf#page=40); REPORT [DOC-001 outcomes/analysis p.3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [exploratory interpretation p.4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), [Table 2 p.7](../../jama_stunnenberg_2018_oi_180136.pdf#page=7) and [methods footnote p.8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8). The report continues to label these outcomes secondary and explains exploratory interpretation by lack of multiplicity adjustment; this is a strong alternative reading that formal status did not change, retained explicitly rather than silently asserting formal reassignment. The plan states secondary endpoints will be analyzed in the same way after its Bayesian primary specification, whereas the report identifies dependent t tests for non-IVR outcomes. Human question concerns intended outcome status and supplied analysis specification for the named secondary IVR, quality-of-life and objective Table 2 effects. No key-secondary designation or unreported nonkey outcome alone is used to qualify this issue. P_R; protocol_report.


### Source-linked checker evidence

#### F-XS-003 — Prespecified secondary outcomes are described as exploratory and non-IVR Bayesian analyses are replaced by frequentist results

- **Locations and roles:** [DOC-002 summary p.7](../../joi180136supp1_prod.pdf#page=7), [§7.1.2 p.31](../../joi180136supp1_prod.pdf#page=31), [§9.1 p.40](../../joi180136supp1_prod.pdf#page=40), PLAN; [DOC-001 secondary definitions/frequentist methods p.3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [Statistical Analysis p.4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), [Table 2 pp.7–8](../../jama_stunnenberg_2018_oi_180136.pdf#page=7), REPORT.
- **Printed statements:** Plan lists IVR pain, weakness/fatigue, clinical myotonia, quantitative grip, INQoL, SF-36, plasma, biceps force and needle EMG as secondary and states “The secondary endpoints will be analyzed in the same way” following its hierarchical Bayesian model. Report explicitly says secondary measures “should be interpreted as exploratory,” owing to no multiple-testing adjustment, and describes dependent t tests for other normally distributed secondary outcomes. Observed Bayesian results are supplied for IVR pain/weakness/tiredness, while Table 2 reports frequentist estimates/CIs/P values for non-IVR endpoints.
- **Comparison logic:** Prespecified secondary status versus explicitly exploratory interpretation is a status change under the required Route A rule. In the same changed secondary-analysis pattern, the printed prospective model is replaced for non-IVR endpoints by frequentist tests. No amendment or clarification limiting the plan's secondary-model promise is supplied. No numerical recomputation applies.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship:** P_R.
- **Qualifying route:** Route A, category 5 (status change); Route B additionally supports the printed planned-versus-reported secondary model conflict.
- **Affected result or extracted value:** Secondary IVR and objective/quality-of-life outcome status and the analysis interpretation of Table 2 non-IVR treatment effects.
- **Why context does not resolve it:** Route A requires registration of reproduced status changes. Calling P values exploratory explains the report's inferential caution, but does not supply the prospective-to-reported hierarchy/analysis reconciliation.
- **Supported alternatives:** “Exploratory” might refer only to interpretation of unadjusted tests, while outcomes retain formal secondary status; a methodological amendment may have replaced non-IVR models. Human review can distinguish these readings.
- **Human question:** What formal outcome status and prospective analysis specification apply to each listed secondary outcome, and where is the change from the plan's Bayesian specification documented?



## C004 — Myotonia measurement definitions differ between the plan and report

Pending Human Adjudication.

**Qualifying route:** Route B
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN protocol pp.32-33 vs REPORT main pp.3,5,7-8
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-004
**Checker provenance:** F-XS-004, F-XS-010, F-ST1-204
**Classification rationale:** The conflicting comparison concerns prospective PLAN content and REPORT analysis or endpoint content; report code corroborates the reported side. P_R takes precedence.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-XS-004 — INCLUDE:** Route B applies to the consolidated myotonia endpoint-definition pattern because planned3-second bedside contractions and90%→10/50/75% quantitative relaxation thresholds differ from reported5-second contractions and90%→5% relaxation, changing the measurement definition attached to the named Table 2 treatment effects without a supplied reconciliation.

Consolidate F-XS-010 and F-ST1-204 here; retain PLAN [DOC-002 bedside/quantitative procedure p.32](../../joi180136supp1_prod.pdf#page=32) and [quantitative thresholds p.33](../../joi180136supp1_prod.pdf#page=33); REPORT [DOC-001 outcome definitions p.3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [baseline footnote d p.5](../../jama_stunnenberg_2018_oi_180136.pdf#page=5), [handgrip/eyelid/dynamometry rows p.7](../../jama_stunnenberg_2018_oi_180136.pdf#page=7), [footnotes h/j p.8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8). These are endpoint design constants; even treating them as rounded leaves3-versus5 interval gap1/5=0.20 and10-versus5 gap4/5=0.80. Same number of repeated contractions does not make durations/thresholds identical. A revised measurement specification or earlier protocol version remains possible; no clinical consequence or preferred procedure is inferred. P_R; protocol_report.


### Source-linked checker evidence

#### F-XS-004 — Reported quantitative-grip relaxation endpoint differs from all three planned cutoffs

- **Locations and roles:** [DOC-002 Quantitative grip myotonia pp.32–33](../../joi180136supp1_prod.pdf#page=33), PLAN; [DOC-001 Outcomes p.3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [Table 2 relaxation rows p.7](../../jama_stunnenberg_2018_oi_180136.pdf#page=7), [footnote j p.8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8), REPORT.
- **Printed statements:** Plan measures three relaxation durations: 90%→10%, 90%→50%, 90%→75% MVIC. Report defines and labels relaxation as 90%→5%, with first/fifth/mean dynamometry results.
- **Comparison logic:** The lower force threshold is 5% rather than any prospectively specified 10%, 50% or 75%; this changes the measured relaxation-time quantity. These are exact endpoint thresholds, not interchangeable descriptions or rounded outcome estimates. Display precision therefore cannot reconcile the endpoint-definition change.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Table 2 dynamometry relaxation treatment differences, including mean −0.02 seconds (95% CI −0.28–0.25), and the endpoint definition a reviewer would extract.
- **Why context does not resolve it:** A reader cannot assume that 90%→5% is one of the three specified cutoffs; reaching 5% represents a different portion of relaxation. The report does not describe a threshold amendment.
- **Supported alternatives:** A later measurement specification may have selected the 5% cutoff; the historical study description in plan p.26 mentions a 90%→5% endpoint but does not amend the current protocol's operative pp.32–33 measurements.
- **Human question:** Which quantitative-grip endpoint was prospectively specified and implemented, and how do the 90%→5% results relate to the three planned relaxation outcomes?


#### F-XS-010 — Reported bedside relaxation measurements use a different preceding contraction duration

- **Locations and roles:** [DOC-002 Clinical Myotonia test p.32](../../joi180136supp1_prod.pdf#page=32), PLAN; [DOC-001 Outcomes p.3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [Table 1 footnote d p.5](../../jama_stunnenberg_2018_oi_180136.pdf#page=5), [Table 2 footnote h p.8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8), REPORT.
- **Printed statements:** Plan instructs eye closure tightly for three seconds and fist closure forcefully for three seconds, each repeated five times with relaxation timed. Report defines both eyelid and handgrip relaxation after forceful contraction for five seconds, repeated five times.
- **Comparison logic:** Both sources specify the preceding contraction duration as part of the same secondary relaxation-time endpoint. Exact three-second versus five-second instructions differ; this is not different terminology for one test and cannot be equated by rounding. The finding is about the prospective/report endpoint specification, without assuming any clinical effect of the duration change.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Table 2 first/fifth/mean handgrip and eyelid action-myotonia treatment differences and the measurement definition for extraction.
- **Why context does not resolve it:** Report footnotes repeat five seconds, whereas the operative protocol repeats three seconds for both assessments; no supplied amendment identifies the performed duration or equates the two definitions.
- **Supported alternatives:** Actual assessments may have adopted a revised five-second specification, or one document may summarize another protocol version. Neither is supplied.
- **Human question:** Were the bedside relaxation times collected after three-second or five-second contractions, and where is the endpoint-specification change documented?


#### F-ST1-204 — Reported myotonia measurements use different contraction and relaxation definitions

- **Relationships:** S215, S216; consolidated pattern of prospective versus reported quantitative myotonia endpoint definitions. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R; all relationships P_R.
- **Exact locations/document roles:** PLAN [DOC-002 p.32 clinical action myotonia](../../joi180136supp1_prod.pdf#page=32), [p.33 quantitative grip](../../joi180136supp1_prod.pdf#page=33); REPORT [DOC-001 p.3 Outcomes](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [p.7 Table2 myotonia rows](../../jama_stunnenberg_2018_oi_180136.pdf#page=7), [p.8 Table2 footnotes h,j](../../jama_stunnenberg_2018_oi_180136.pdf#page=8).
- **Printed statements:** PLAN eyes/fist closed forcefully3seconds then opening/extension; quantitative relaxation measured90%→10%,90%→50%,90%→75%MVIC. REPORT eye/hand action times follow5seconds forceful contraction; quantitative grip relaxation90%→5%MVIC. Both use five repeated contractions, which agrees and does not resolve the differing duration/cutoffs.
- **Rule/calculation:** Matched outcome definitions must identify the same experimental contraction duration and relaxation endpoint.3seconds versus5seconds and10/50/75% versus5% specify different measurement tasks/endpoints. These are design definitions, not rounded estimates; taking5% as the reported reference, even nearest-integer percent intervals for10% and5% leave4percentage-point gap/5=0.8>0.05. For3 versus5seconds the nearest-integer intervals leave1second gap/5=0.20>0.05. Definitions are actually scheduled quantities, so these intervals are conservative diagnostic checks.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Clinical handgrip/eyelid relaxation treatment effects and handgrip dynamometry90%–5% relaxation effects in Table2; extraction as originally planned endpoints versus revised measurement definitions.
- **Why context does not resolve it:** The printed report consistently names5seconds and90%–5%, while the protocol consistently provides3seconds andthree different relaxation cutoffs. No supplied amendment, alternate matched endpoint result or explanation states which definition was implemented for these results. This is not merely a synonym for myotonia.
- **Alternatives/missing definitions:** Measurements may have been deliberately harmonized to the comparison RCT, or the protocol may be an earlier specification. The article's similarity-to-RCT statement does not supply the actual amendment/history or reconcile the numerical definitions.
- **Exact human question:** Which contraction durations and relaxation thresholds generated the reported Table2 myotonia results, and how are these reconciled with the supplied prospective definitions?



## C005 — Primary-data eligibility differs from the planned withdrawal-data rule

Pending Human Adjudication.

**Qualifying route:** Route B
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN protocol p.35 vs REPORT main pp.3-4,8 and results supplement p.5
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-005
**Checker provenance:** F-XS-005, F-ST1-203
**Classification rationale:** The conflicting comparison concerns prospective PLAN content and REPORT analysis or endpoint content; report code corroborates the reported side. P_R takes precedence.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-XS-005 — INCLUDE:** Route B applies because the plan's primary-data inclusion rule permits pretermination data except consent withdrawal whereas the report requires completion of at least one period and analyzes27 completers, leaving the prespecified eligibility predicate attached to the named primary effects unresolved.

Consolidate F-ST1-203 here. Retain PLAN [DOC-002 withdrawal-data rule p.35](../../joi180136supp1_prod.pdf#page=35); REPORT [DOC-001 aggregation criterion p.3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [flow/Numbers Analyzed p.4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), [SAE exclusion p.8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8); REPORT [DOC-003 individual outcomes/dropout footnote p.5](../../joi180136supp2_prod.pdf#page=5). Count arithmetic30−3=27 reconciles; the issue is different printed inclusion predicates, not an assumed missing-data effect. The27-patient Bayesian3.06 and frequentist3.12 estimates have clear reported denominators but unresolved prospective population mapping. Withdrawals may have no eligible outcome-window data or may have withdrawn consent; these unavailable facts could reconcile actual exclusions and remain alternatives. P_R; protocol_report.


### Source-linked checker evidence

#### F-XS-005 — Completer-based primary analysis conflicts with planned inclusion of pretermination data

- **Locations and roles:** [DOC-002 §7.5 p.35](../../joi180136supp1_prod.pdf#page=35), PLAN; [DOC-001 Bayesian Analysis p.3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [Figure 1/Numbers Analyzed p.4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), REPORT; [DOC-003 eTable 3 p.5](../../joi180136supp2_prod.pdf#page=5), REPORT.
- **Printed statements:** Plan: intent-to-treat, “All data acquired prior to termination ... included in the primary analysis unless patient withdraws consent.” Report restricts aggregate inclusion to completion of at least one treatment period, and analyzed results/flow include exactly 27 completers with 31 sets. Patients 3,6,7 dropped out and are absent from individual primary-result table; patient 7 discontinued for an adverse reaction, not described as withdrawal of consent.
- **Comparison logic:** Prospective inclusion of all acquired pretermination data uses consent withdrawal as the exception; reported completion-based inclusion uses a different criterion. This concerns the stated analysis population, not a claim that unseen withdrawal data must change the estimate. No raw early data or consent records are supplied, so numerical effect recalculation is unavailable.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Primary Bayesian stiffness analysis population n=27 and overall treatment effect 3.06.
- **Why context does not resolve it:** The report's “all available data” applies within the completion-defined population and does not state whether pretermination data from excluded patients were unavailable, withdrawn, or omitted under an amended rule.
- **Supported alternatives:** Dropouts may have no evaluable postbaseline primary data, or may have withdrawn consent. The package does not establish either; the observed finding is the different printed population rules.
- **Human question:** Were pretermination primary data from patients 3,6,7 included or unavailable/withdrawn, and what reconciles the reported completion criterion with the planned intent-to-treat criterion?


#### F-ST1-203 — Primary analysis eligibility differs from the planned withdrawal-data rule

- **Relationships:** S219. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R; all relationships P_R.
- **Exact locations/document roles:** PLAN [DOC-002 p.35 §7.5](../../joi180136supp1_prod.pdf#page=35); REPORT [DOC-001 p.3 Bayesian Analysis](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [p.4 Figure1/Numbers Analyzed](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), [p.8 SAE exclusion](../../jama_stunnenberg_2018_oi_180136.pdf#page=8).
- **Printed statements:** PLAN: “An intent-to-treat approach will be used. All data acquired prior to termination ... will be included in the primary analysis unless patient withdraws consent.” REPORT: “All patients who completed at least1 treatment period were included within the aggregated analysis, with inclusion of all available data”;30 randomized,3 did not complete,27 completers analyzed, with31 sets. One patient excluded after mexiletine-related SAE.
- **Rule/calculation:** Compare inclusion predicates: any acquired pretermination data except consent withdrawal versus completion of≥1 period and the displayed27-completer population. These are distinct eligibility rules.30−3=27 reconciles report flow arithmetically; the finding is not a count-total discrepancy. No display rounding applies to categorical inclusion rules. No raw-data availability or treatment-effect impact is assumed.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** The analysis population attached to primary Bayesian3.06-point effect and frequentist3.12-point estimate, both based on27 patients.
- **Why context does not resolve it:** The report supplies neither a consent-withdrawal explanation nor a reconciliation of the planned rule with its completed-period eligibility. A reader can identify27 analyzed but cannot determine whether this is the prespecified population or a revised primary eligibility rule. This satisfiesB1 analysis population,B2 unresolved specification,B3 interpretation of the primary population.
- **Alternatives/missing definitions:** All three withdrawals may have contributed no eligible treatment-window measurements, or consent withdrawal may explain exclusions; no such facts are supplied. The report may operationalize “all data” as only analyzable treatment-period data. This could reconcile actual exclusions and requires human confirmation; it does not make the printed rules identical.
- **Exact human question:** How did the completed-period eligibility rule implement the protocol's all-pretermination-data primary rule, and did any withdrawn patient's eligible primary measurements or consent status account for the30-to27 restriction?



## C006 — Planned primary treatment interactions have no identifiable reported result

Pending Human Adjudication.

**Qualifying route:** Route A, category 5
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN protocol p.40 vs REPORT main pp.3-4 and results supplement pp.11-14
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-ST1-207
**Checker provenance:** F-ST1-207
**Classification rationale:** The conflicting comparison concerns prospective PLAN content and REPORT analysis or endpoint content; report code corroborates the reported side. P_R takes precedence.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-ST1-207 — INCLUDE:** Route A, category 5 applies because the plan promises primary treatment×pair and treatment×order interaction checks, whereas the report identifies only order/period covariate main effects and genotype×treatment interaction, with no identifiable supplied result for the two planned interactions.

Locations: PLAN [DOC-002 primary model p.40](../../joi180136supp1_prod.pdf#page=40); REPORT [DOC-001 primary frequentist model p.3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [primary results/orderP=.85/periodP=.22 p.4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4); REPORT [DOC-003 model code pp.11](../../joi180136supp2_prod.pdf#page=11), [12](../../joi180136supp2_prod.pdf#page=12), [13](../../joi180136supp2_prod.pdf#page=13), [14](../../joi180136supp2_prod.pdf#page=14). A main-effect order/period term is not a treatment interaction. The P values might summarize intended interaction tests, but neither the printed model nor code establishes that interpretation. The named result is primary stiffness effect stability across pair/order. An unreported term definition or revision remains the human question. P_R; protocol_report.


### Source-linked checker evidence

#### F-ST1-207 — Planned primary treatment-by-pair/order interactions have no identifiable reported counterpart

- **Relationships:** S224. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R; all relationships P_R.
- **Exact locations/document roles:** PLAN [DOC-002 p.40 §9.1](../../joi180136supp1_prod.pdf#page=40); REPORT [DOC-001 p.3 Frequentist Analysis](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [p.4 primary results](../../jama_stunnenberg_2018_oi_180136.pdf#page=4); REPORT [DOC-003 pp.11–14 primary Bayesian models](../../joi180136supp2_prod.pdf#page=11).
- **Printed statements:** PLAN: “We will also investigate whether we find evidence for interactions between treatment effect and treatment pair, and between treatment effect and treatment order.” REPORT candidates are treatment,genotype,baselineIVR,randomization order,period effect, with genotype×treatment specified as the fixed interaction; order/period excluded from final model usingP<.10. Results state orderP=.85 andperiodP=.22. Printed Bayesian model code has no treatment-pair/order variables or interactions.
- **Rule/calculation:** A main-effect order/period covariate and its P value do not identify a treatment×order or treatment×pair interaction. The report names the genotype interaction explicitly but not either planned interaction. Nodegrees of freedom/test-term identity is assumed. These planned primary-analysis interaction checks have no identifiable supplied result. No numeric rounding applies to distinct model terms.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Primary IVR stiffness treatment effect and its stability across treatment pair and order.
- **Why context does not resolve it:** Category5 registers an unreported planned primary analysis. The supplied order/periodP values may be intended counterparts, but the printed model specification does not say they are treatment interactions; that alternative does not establish a matched result.
- **Alternatives/missing definitions:** P=.85/.22 may summarize interaction tests rather than the named covariate main effects; additional omitted interaction models may have been fitted; planned checks may have been revised. The missing definition is which exact model term/test eachP value represents.
- **Exact human question:** Were the prespecified treatment-by-pair and treatment-by-order interactions analyzed, and doP=.85/.22 represent those interactions or the report's order/period covariate main effects?



## C007 — Three clinical nonresponders are attributed to a Bayesian rule met by two

Pending Human Adjudication.

**Qualifying route:** Route B
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** statistical_results
**Relationship type:** S_C
**All relationships:** S_C, S_W
**Compared document roles:** REPORT main stopping rule p.3 and response statement p.4 vs REPORT results supplement p.5
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-007
**Checker provenance:** F-XS-007
**Classification rationale:** The response classification compares two REPORT documents and also an internal main-report criterion; S_C takes precedence over S_W.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-XS-007 — INCLUDE:** Route B applies because the report attributes all3 nonresponders to predefined Bayesian ineffectiveness but patient11 has38% probability against its below20% criterion, changing the named number classified by that criterion even though a clinical override is disclosed.

Locations: REPORT [DOC-001 stopping rule p.3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [primary response classification p.4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), REPORT [DOC-003 eTable 3 patient11/criterion/override footnote p.5](../../joi180136supp2_prod.pdf#page=5). Probability interval [37.5,38.5]% cannot be below20%; patients13/22 at2%/1% meet the numerical rule. The same-display footnote explains why patient11's zero observed stiffness led to clinical discontinuation but does not make38% satisfy the printed Bayesian criterion. Retain the distinction between2 numerical-rule classifications and3 clinical nonresponders; do not question the clinical decision. S_C primary, all relationships S_C, S_W; statistical_results.


### Source-linked checker evidence

#### F-XS-007 — All three nonresponders are described as meeting predefined Bayesian ineffectiveness although patient 11's probability is 38%

- **Locations and roles:** [DOC-001 Primary Outcome Measure p.4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), [Bayesian stopping rule p.3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), REPORT; [DOC-003 eTable 3 patient 11 and footnote p.5](../../joi180136supp2_prod.pdf#page=5), REPORT.
- **Printed statements:** Main: “In 3 patients (11%), Bayesian analysis showed the predefined clinical ineffectiveness”; lower than 20% probability is its ineffectiveness stopping rule. Supplement labels patients 11,13,22 nonresponders and defines nonresponse <20%, but patient 11 is 38%; footnote explains zero observed stiffness, influential flat prior and clinical discontinuation after one set. Other two probabilities are 2% and 1%.
- **Comparison logic:** Patient 11's 38% is in the 20–80% continuation interval, not below20%. Rounding [37.5,38.5]% cannot place it below20%; this is decision-rule classification rather than a recomputed outcome estimate. Two patients meet the printed probabilistic nonresponse criterion; a third received a clinical override disclosed in the footnote.
- **Focus area:** B/C. **Proposed review domain:** statistical_results. **Relationship:** S_C; **All relationships:** S_C, S_W.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Number/proportion classified as Bayesian predefined ineffective (3/27, 11%) and the distinction between posterior criterion failure and clinical discontinuation.
- **Why context does not resolve it:** The footnote explains a clinical decision, but does not make 38% satisfy the stated Bayesian cutoff. Main explicitly attributes all three classifications to predefined Bayesian ineffectiveness.
- **Supported alternatives:** Patient 11 can reasonably be a clinical nonresponder because observed stiffness was absent; a clinical override may have been intended. This is distinct from the printed probabilistic criterion.
- **Human question:** Should the three nonresponders be described as two meeting the predefined probability rule plus one clinical override, or was another prespecified ineffectiveness rule used?



## C008 — INQoL baseline upper quartiles exceed the stated scale range

Pending Human Adjudication.

**Qualifying route:** Route B
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main Table 1 row and scale footnote p.5; corroborating Table 2 scale footnote p.8
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-NUM-004
**Checker provenance:** F-NUM-004
**Classification rationale:** The conflicting numbers, interval, label or test appear within one REPORT document. Plan material does not supply a conflicting comparator.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-NUM-004 — INCLUDE:** Route B applies because INQoL upper quartiles 110.3 and120.0 exceed the same table's stated0–100 scale beyond display precision, leaving the scale and baseline distributions a data extractor should retain unclear.

Locations: REPORT [DOC-001 Table 1 INQoL row/footnote f p.5](../../jama_stunnenberg_2018_oi_180136.pdf#page=5), corroborating REPORT [Table 2 footnote g p.8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8). The scale definition supplies an upper bound100; quartile intervals [110.25,110.35] and [119.95,120.05] leave relative gaps10.25/110.3=0.092928 and19.95/120=0.16625. Even conservatively allowing upper bound100.5 leaves both above0.05. No scoring formula resolves whether a summed or transformed score is represented. S_W; statistical_results.


### Source-linked checker evidence

#### F-NUM-004

**Title:** INQoL displayed baseline quartiles exceed the stated composite-score range.

**Relationships:** N010, N034, N046. **Focus area:** C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W.

**Compared locations and document roles:** REPORT [main p.5 Table 1 INQoL row and footnote f](../../jama_stunnenberg_2018_oi_180136.pdf#page=5); corroborating REPORT [main p.8 Table 2 footnote g](../../jama_stunnenberg_2018_oi_180136.pdf#page=8).

**Printed inputs:** INQoL composite score: CLCN1 median84.0(IQR74.5–110.3); SCN4A median98.0(IQR56.0–120.0). Footnote f: “Scale,0 to100; a higher score indicates greater disease severity.” Table2 footnote g repeats0–100 for INQoL.

**Rule and calculation:** A quartile of a variable bounded0–100 must lie within0–100. Scale endpoints define exact bounds. Upper quartile110.3 has display interval[110.25,110.35]; gap from maximal attainable100 =10.25; relative discrepancy10.25/110.3=.092928>.05. Upper quartile120.0 has interval[119.95,120.05]; gap19.95; relative19.95/120=.16625>.05. Both median and lower-quartile readings are preserved; only upper quartiles violate the described bound.

**Qualifying route:** Route B.

**Affected result or extracted value:** Baseline INQoL composite distributions, including whether the displayed values use the stated0–100 composite or a different aggregate scale.

**Why context does not resolve it:** The table and its adjacent footnote give incompatible numeric units/ranges. No summation, transformed score, or alternative upper bound is specified, so the reader cannot identify which score scale produced the displayed quartiles.

**Alternatives and missing definitions:** The values may represent a sum or another transformation while the footnote describes a normalized composite; alternatively one or more printed quartiles may refer to a different scale. The supplied report/protocol does not give a formula that chooses between them.

**Exact human question:** What INQoL scoring range and aggregation produced upper quartiles110.3 and120.0, and which scale should a data extractor attach to the Table1 distributions?



## C009 — Other-medication P does not reproduce the adjacent-row binary comparison

Pending Human Adjudication.

**Qualifying route:** Route A, category 4
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main Table 1 medication and sex rows plus test footnote p.5
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-ST1-010
**Checker provenance:** F-ST1-010
**Classification rationale:** The conflicting numbers, interval, label or test appear within one REPORT document. Plan material does not supply a conflicting comparator.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-ST1-010 — INCLUDE:** Route A, category 4 applies because a binary Mann–Whitney permutation calculation reproduces the adjacent Men and Mexiletine rows but givesP=1 for Other7/16 versus5/11, distinct from printedP=.62.

Location: REPORT [DOC-001 Table 1 medication/sex rows and Mann–Whitney footnote a p.5](../../jama_stunnenberg_2018_oi_180136.pdf#page=5). Independent combinatorial calculation sums hypergeometric allocation probabilities with absolute-U tail: Other1.000000, Men.3913043478, Mexiletine.4985754986, reproducing the latter two printedP values. The method's integer sample counts and binary allocations are fixed by any admissible integer values in their half-unit intervals; P=1 compared with [.615,.625] leaves gap.375/.62=.604839. Tie-adjusted asymptoticP≈.9315 is also distinct. A multi-category/dose variable rather than binary Other use might have been tested; the display does not identify that different variable, and category4 preserves this as the human question. S_W; statistical_results.


### Source-linked checker evidence

#### F-ST1-010

**Title:** Baseline “Other” antimyotonic-medication P does not reproduce the binary comparison that matches adjacent rows.

**Relationships:** S011. **Locations and roles:** REPORT DOC-001 [p.5 Table1 Men and Pretrial medication rows with footnote a](../../jama_stunnenberg_2018_oi_180136.pdf#page=5). All REPORT.
**Printed values:** CLCN1 N 16,SCN4A N 11; Other 7(44%) versus 5(46%), P=.62; adjacent Men 13 versus 7, P=.39; Mexiletine 2 versus 0, P=.50. Footnotea identifies Mann–Whitney U.
**Rule and calculation:** A binary rank comparison with tied 0/1 values has U centered at n1*n2/2=88, observed U=88+(11*7−16*5)/2=86.5. Exact two-sided permutation probability of abs(U−88) at least 1.5 is 1.000: every possible allocation of 12 yes values is at least that far from 88. The same exact absolute-U permutation tail gives .391304 for Men and .498575 for Mexiletine, reproducing .39/.50. Tie-adjusted asymptotic diagnostic var(U)=16*11*12*15/(4*26)=304.6154,|z|1.5/sqrt(var)=.08594, normal P≈.9315; continuity adjustment increases P. Integer counts are exact; exact recomputed P=1, printed P interval[.615,.625], gap.375/.62=.60484, above 5%.
**Focus area:** B, C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 4.
**Affected result or extracted value:** Baseline Other-medication subgroup comparison P and which variable was tested.
**Why context does not resolve it:** A reproducing exact binary rank method matches adjacent rows yet does not reproduce this row; unstated tested variable is the human question.
**Alternatives / missing definition:** P may test drug categories or doses instead of binary Other-medication use; a different tested variable or sample could be intended. Neither is labeled in the display.
**Human question:** Which variable, sample and Mann–Whitney procedure generated P=.62 for 7/16 versus 5/11?



## C010 — SCN4A transient-paresis interval crosses zero while its P is significant

Pending Human Adjudication.

**Qualifying route:** Route A, category 1
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main repeated narrative p.6 vs Table 2 subgroup row p.7 and test rule p.4
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-ST1-004
**Checker provenance:** F-ST1-004
**Classification rationale:** The conflicting numbers, interval, label or test appear within one REPORT document. Plan material does not supply a conflicting comparator.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-ST1-004 — INCLUDE:** Route A, category 1 applies because SCN4A fifth-transient-paresis effect13.71 has95%CI−1.96 to25.47 including zero but printedP=.02 indicates significance under the report's.05 rule.

Locations: REPORT [DOC-001 Table 2 SCN4A fifth paresis p.7](../../jama_stunnenberg_2018_oi_180136.pdf#page=7), [repeated narrative p.6](../../jama_stunnenberg_2018_oi_180136.pdf#page=6), [significance p.4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), [method/scale footnotes p.8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8). P [.015,.025] remains significant and rounded endpoints retain opposite signs. InteractionP<.001 is a distinct comparison. Different analyses or an intended endpoint sign remain alternatives. S_W; statistical_results.


### Source-linked checker evidence

#### F-ST1-004

**Title:** SCN4A fifth-attempt transient-paresis interval includes zero but P=.02.

**Relationships:** S092. **Locations and roles:** REPORT DOC-001 [p.7 Table2, transient paresis Fifth attempt SCN4A](../../jama_stunnenberg_2018_oi_180136.pdf#page=7); [p.6 narrative repeats13.71(−1.96 to25.47)](../../jama_stunnenberg_2018_oi_180136.pdf#page=6); REPORT p.4 significance and p.8 method/scale footnotes.
**Printed values:** Effect 13.71 percentage points, 95% CI −1.96 to 25.47, P=.02; interaction P<.001 is a distinct row.
**Rule and calculation:** CI contains 0 but .02<.05. Rounding limits remain negative/positive and P[.015,.025] remains significant. CI midpoint 11.755 is not 13.71; df is not assumed for the primary contradiction.
**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 1.
**Affected result or extracted value:** SCN4A fifth-attempt transient-paresis effect, 95% CI and significance.
**Why context does not resolve it:** Always-register interval/P conflict; interaction does not determine the within-subgroup test.
**Alternatives / missing definition:** Lower endpoint sign could differ, or CI/P may be from distinct analyses; source does not define that mapping.
**Human question:** Which CI and P represent the SCN4A 13.71 percentage-point effect?



## C011 — Lower Table 2 contrast header reverses the represented effect direction

Pending Human Adjudication.

**Final pattern qualification:** All 27 lower-section rows were inspected. Twenty-four show the reversed sign orientation; three are explicit exceptions: handgrip Fifth CLCN1, relaxation First, and relaxation Mean. Their individual row facts remain in the recheck; magnitude comparisons are separately tracked in C015. The final statement does not claim all 27 rows independently reverse direction.

**Qualifying route:** Route A, category 2
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main Table 2 lower header and repeated outcome rows p.7 with direction footnotes p.8
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-ST1-008
**Checker provenance:** F-ST1-008
**Classification rationale:** The conflicting numbers, interval, label or test appear within one REPORT document. Plan material does not supply a conflicting comparator.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-ST1-008 — INCLUDE:** Route A, category 2 applies because Table 2's lower-section Placebo−Mexiletine header reverses the subtraction direction represented by repeated non-IVR treatment-effect signs, changing the extracted reference orientation.

Locations: REPORT [DOC-001 Table 2 lower header/non-IVR rows p.7](../../jama_stunnenberg_2018_oi_180136.pdf#page=7), [scale/benefit/method footnotes d/f–l p.8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8). Preserve all affected lower-section rows: SF-36 physical and mental; INQoL; handgrip First/Fifth/CLCN1/SCN4A/Mean; eyelid First/Fifth/Mean; Timed Up&Go First/Fifth/Mean; relaxation First/Fifth/Mean; peak force First/Fifth/Mean; paresis First/Fifth/CLCN1/SCN4A/Mean/CLCN1/SCN4A. Sign demonstration: INQoL placebo−7.22 minus mexiletine−21.44 gives+[14.21,14.23], versus printed−14.22 interval [−14.225,−14.215], relative gap28.425/14.22=1.998945; first handgrip header subtraction+2.85 versus printed−2.85; higher physical SF-36 also follows reversed orientation. The printed signs, outcome scales and benefit footnote permit reconstructing the likely direction, but always-register sign/reference conflicts retain the printed header for adjudication. S_W; statistical_results.


### Source-linked checker evidence

#### F-ST1-008

**Title:** Lower Table2 contrast header reverses the direction represented by period changes and effects.

**Relationships:** S068–S082,S086–S092,S094–S096; repeated pattern consolidated. **Locations and roles:** REPORT DOC-001 [p.7 Table2 lower-section header and non-IVR outcome rows](../../jama_stunnenberg_2018_oi_180136.pdf#page=7); REPORT [p.8 footnotes d,f–l](../../jama_stunnenberg_2018_oi_180136.pdf#page=8).
**Printed values:** Effect header “Placebo-Mexiletine”. SF-36 physical placebo +1.04, mexiletine +8.66, effect +7.81; INQoL placebo −7.22, mexiletine −21.44, effect −14.22; handgrip First placebo +.46, mexiletine −2.39, effect −2.85. The majority of subsequent non-IVR rows follow mexiletine-minus-placebo sign, including handgrip Fifth/Mean, eyelid First/Fifth/Mean, Timed Up&Go First/Fifth/Mean, peak force First/Fifth/Mean, transient paresis First/Fifth/Mean and both genotype rows for transient Fifth/Mean. Footnote d says all significant findings favor mexiletine; higher SF-36/peak force and lower INQoL/times/paresis are beneficial by supplied scale definitions.
**Rule and calculation:** Header subtraction SF-36 physical 1.04−8.66=−7.62, versus printed+7.81; INQoL−7.22−(−21.44)=+14.22, versus−14.22; handgrip First .46−(−2.39)=+2.85, versus−2.85. INQoL recomputed half-unit interval[14.21, 14.23], printed[−14.225,−14.215], gap 28.425/14.22=1.9989. Header therefore changes reference/direction rather than only typography. Same opposite-sign pattern across named rows is one issue; F-ST1-009 separately concerns magnitude/paired subset after allowing the observed operative M−P direction.
**Focus area:** B, C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 2.
**Affected result or extracted value:** Sign and reference orientation of non-IVR effect estimates for extraction/synthesis.
**Why context does not resolve it:** Numeric-sign/reference reversal falls in always-register category 2 even though source scale/narrative suggests benefit.
**Alternatives / missing definition:** Effects may use mexiletine-minus-placebo while header names the reverse; outcome-specific changes or a different contrast definition could apply but are not stated.
**Human question:** Which subtraction/reference group does each lower-section treatment-effect column represent?



## C012 — Physical SF-36 placebo interval does not center on its printed mean

Pending Human Adjudication.

**Qualifying route:** Route A, category 4
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main Table 2 physical SF-36 period row and comparator rows p.7; methods pp.3,8
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-ST1-012
**Checker provenance:** F-ST1-012
**Classification rationale:** The conflicting numbers, interval, label or test appear within one REPORT document. Plan material does not supply a conflicting comparator.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-ST1-012 — INCLUDE:** Route A, category 4 applies because the symmetric period-mean interval method reproduces adjacent rows but yields midpoint[1.175,1.185] for physical SF-36 placebo CI−.60–2.96, distinct from mean1.04 interval[1.035,1.045] by relative gap.125.

Locations: REPORT [DOC-001 Table 2 physical SF-36 placebo p.7](../../jama_stunnenberg_2018_oi_180136.pdf#page=7), [dependent-t method p.3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [method footnote a p.8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8). Adjacent mental-placebo, physical-mexiletine and first-eyelid-placebo interval midpoints exactly reproduce their−1.85,8.66 and−.74 printed means. Period-CI engine and a possible distinct/asymmetric interval or availability subset are not separately specified; category4 permits this missing method to remain a human question. S_W; statistical_results.


### Source-linked checker evidence

#### F-ST1-012

**Title:** SF-36 physical placebo change/CI is not centered under the interval method reproducing other period rows.

**Relationships:** S068. **Locations and roles:** REPORT DOC-001 [p.7 Table2,SF-36 Physical,ChangePlaceboPeriod](../../jama_stunnenberg_2018_oi_180136.pdf#page=7); REPORT p.3 secondary analysis, p.8 footnote a.
**Printed values:** Placebo change 1.04, 95% CI −.60 to 2.96. Other periods: SF-36 mental placebo −1.85(−4.81, 1.11); SF-36 physical mexiletine 8.66(5.94, 11.38); eyelid First placebo −.74(−2.49, 1.01).
**Rule and calculation:** Symmetric mean intervals reproduce the other named rows: respective endpoint midpoints−1.85, 8.66,−.74. Physical placebo midpoint(−.60+2.96)/2=1.18. Rounding midpoint interval[1.175, 1.185], printed mean[1.035, 1.045], gap.130/1.04=.125, above 5%. The mean is contained; issue is reproduction under the same-display interval method, not point containment.
**Focus area:** B, C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 4.
**Affected result or extracted value:** SF-36 physical placebo change mean and 95% CI analysis identity.
**Why context does not resolve it:** Category 4 allows a reproducing method that matches other rows of the display; an unstated interval convention is a human question.
**Alternatives / missing definition:** An asymmetric interval procedure or different mean/interval subset could apply; source dependent t test description clearly covers mean effects but does not separately name the period CI engine. No asymmetric method is asserted.
**Human question:** Which method and sample generated−.60 to 2.96, and does it belong to the printed 1.04 placebo mean?



## C013 — Mental SF-36 estimate and interval do not yield the printed P under the stated test

Pending Human Adjudication.

**Qualifying route:** Route A, category 1
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main Table 2 mental SF-36 row p.7 vs dependent-test methods pp.3-4,8
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-ST1-005
**Checker provenance:** F-ST1-005
**Classification rationale:** The conflicting numbers, interval, label or test appear within one REPORT document. Plan material does not supply a conflicting comparator.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-ST1-005 — INCLUDE:** Route A, category 1 applies because the stated paired-t analysis associates effect6.78 and95%CI1.64–11.92 with two-sidedP≈.0117149, whereas the source printsP=.001 for the SF-36 mental result.

Locations: REPORT [DOC-001 Table 2 mental component p.7](../../jama_stunnenberg_2018_oi_180136.pdf#page=7), [dependent-t method p.3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [two-sided testing p.4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), [method footnote a p.8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8). Independent diagnostic calculation for27 pairs: halfwidth5.14, tcrit26=2.0555294386, t=2.7113792984, P=.0117148867. Full input-rounding diagnostic [.0115883,.0118425] is distinct from [.0005,.0015]; even a large-df normal diagnostic remains about.00973. Exact paired availability/df or different interval/test mapping is not supplied and remains the human question. S_W; statistical_results.


### Source-linked checker evidence

#### F-ST1-005

**Title:** SF-36 mental treatment CI does not yield printed P=.001 under stated paired t inference.

**Relationships:** S069. **Locations and roles:** REPORT DOC-001 [p.7 Table2 SF-36 Mental component](../../jama_stunnenberg_2018_oi_180136.pdf#page=7); REPORT [p.3 Frequentist Analysis](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), p.4 two-sided testing and [p.8 footnote a](../../jama_stunnenberg_2018_oi_180136.pdf#page=8).
**Printed values:** Effect 6.78, 95% CI 1.64–11.92, P=.001, total N 27. Methods say dependent t tests calculated total-group mean effects, significance and confidence intervals; footnote a contrasts IVR mixed model with dependent t tests for other measures.
**Rule and calculation:** h=(11.92−1.64)/2=5.14. Under stated paired t on 27 pairs, df 26, tcrit 2.055529, SE 5.14/2.055529=2.500572, t 6.78/2.500572=2.711379, two-sided P=.0117149. Allowing half-unit rounding of all inputs yields diagnostic P[.0115883,.0118425], disjoint from printed P[.0005,.0015]. Minimum gap=.0100883 relative to .001=10.0883. Category 1 is never screened as rounding. Diagnostic df 30 for 31 sets gives P=.0114515; large-df diagnostic P≈.00973 remains distinct. Other total rows reproduce the t relation, e.g. peak-force Mean P≈.008863 rounds .009 and INQoL P≈.009789 rounds .01.
**Focus area:** B, C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 1.
**Affected result or extracted value:** SF-36 mental treatment P, statistical evidence and CI/test identity.
**Why context does not resolve it:** Printed P cannot belong to the printed effect/CI under the analysis stated for this outcome; always-register category 1.
**Alternatives / missing definition:** A distinct test or interval analysis, different linked effect, or unreported paired-subset mapping is possible. Missing exact analysis mapping/df must be named rather than inferred.
**Human question:** Which analysis and associated CI generated P=.001 for the 6.78-point mental-component effect?



## C014 — Placebo first-handgrip mean lies outside its descending interval

Pending Human Adjudication.

**Qualifying route:** Route A, category 1
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main Table 2 first-handgrip placebo mean and interval p.7; scale and method footnotes p.8
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-ST1-001
**Checker provenance:** F-ST1-001
**Classification rationale:** The conflicting numbers, interval, label or test appear within one REPORT document. Plan material does not supply a conflicting comparator.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-ST1-001 — INCLUDE:** Route A, category 1 applies because placebo first-handgrip mean+.46 is outside the printed−.30 to−1.23 interval even after sorting its descending limits, so the mean/interval pair cannot be extracted coherently.

Locations: REPORT [DOC-001 Table 2 first handgrip placebo p.7](../../jama_stunnenberg_2018_oi_180136.pdf#page=7), [methods/scale footnotes p.8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8). Source image and direct text both contain the minus sign before1.23; estimate [.455,.465] versus the larger negative endpoint [−.305,−.295] leaves minimum gap.750. A sign change is a reconstruction possibility, not an assigned correction. S_W; statistical_results.


### Source-linked checker evidence

#### F-ST1-001

**Title:** First-attempt handgrip placebo mean is outside its printed interval and endpoints descend.

**Relationships:** S071. **Locations and roles:** REPORT DOC-001 [PDF p.7 Table2, handgrip action myotonia First attempt, Change Placebo Period](../../jama_stunnenberg_2018_oi_180136.pdf#page=7). REPORT DOC-001 p.8 footnotes a/h describes secondary dependent t tests and relaxation-time quantity.

**Printed values:** Placebo change 0.46 seconds, 95% CI −0.30 to−1.23; baseline 3.33(SD 5.00), mexiletine −2.39(−4.22 to−0.55), effect −2.85(−5.28 to−0.42), P=.02.

**Rule and calculation:** Ordered limits require L≤U: −0.30>−1.23. Even sorting gives [−1.23,−0.30], excluding mean +.46. Half-unit intervals for mean[.455,.465], first limit[−.305,−.295], second limit[−1.235,−1.225] cannot restore order/containment; smallest point-to-upper gap=.455−(−.295)=.750. Relative gap=.750/.46=1.6304. Route A category 1 does not permit a rounding exclusion.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 1.
**Affected result or extracted value:** Placebo first-attempt handgrip mean change and its 95% CI.
**Why context does not resolve it:** Point outside interval is an always-register category; reversing endpoint order alone still excludes the point.
**Alternatives / missing definition:** A sign on 1.23 may differ from the intended bound; this is a source-grounded reconstruction possibility, not a correction. No distinct interval estimand is stated.
**Human question:** Which 95% CI belongs to the printed placebo mean change+.46 seconds?



## C015 — Eleven non-IVR effects do not reproduce the period-mean difference pattern

Pending Human Adjudication.

**Qualifying route:** Route A, category 4
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main Table 2 eleven named non-IVR rows p.7 vs dependent-test and availability methods pp.3-4,8
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-ST1-009
**Checker provenance:** F-ST1-009
**Classification rationale:** The conflicting numbers, interval, label or test appear within one REPORT document. Plan material does not supply a conflicting comparator.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-ST1-009 — INCLUDE:** Route A, category 4 applies because the paired-mean difference identity reproduces multiple adjacent non-IVR Table 2 rows but does not reproduce the11 specified treatment effects beyond full input display precision, leaving the observations/weights behind those extracted effects unresolved.

Locations: REPORT [DOC-001 Table 2 p.7](../../jama_stunnenberg_2018_oi_180136.pdf#page=7), [dependent-t method p.3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [missing/available data p.4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), [method/subgroup footnotes a/c p.8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8). Retain every affected row and its recomputation: handgrip Fifth CLCN1 recomputed [−.300,−.280] versus+.04 relative gap7.875; relaxation First [−.010,.010] versus−.02 gap.25; relaxation Mean [.010,.030] versus−.02 gap1.25; peak-force First [26.720,26.740] versus32.92 gap.1876, Fifth [21.800,21.820] versus24.08 gap.0936, Mean [33.740,33.760] versus37.23 gap.0931; paresis First [−3.145,−3.035] versus−3.7 gap.1365, Fifth total [−9.300,−9.280] versus−12.25 gap.2404, Fifth SCN4A [14.550,14.570] versus13.71 gap.0609, Mean total [−6.310,−6.290] versus−7.34 gap.1396, Mean SCN4A [4.940,4.960] versus4.46 gap.1065. All gaps above.05. Identity uses observed Mexiletine−Placebo orientation independently of the header finding. Missing available-case pairing,27 participants versus31 sets, weighting or subgroup mixed-model mapping are explicit source-grounded alternatives, not assumed absent; source footnote c mentions mixed-model interaction and does not define each subgroup effect's method. IVR model-based effects are excluded from this crude recomputation. S_W; statistical_results.


### Source-linked checker evidence

#### F-ST1-009

**Title:** Several non-IVR treatment effects do not reproduce the period mean difference under the stated dependent-t method.

**Relationships:** S073,S083,S085,S086,S087,S088,S089,S090,S092,S094,S096. **Locations and roles:** REPORT DOC-001 [p.7 Table2 exact named rows below](../../jama_stunnenberg_2018_oi_180136.pdf#page=7); REPORT p.3 dependent-t methods, p.4 all available data and missing outcomes,[p.8 footnote a](../../jama_stunnenberg_2018_oi_180136.pdf#page=8). All locations REPORT.
**Printed values and calculation:** For a paired-difference mean, mean(M−P)=mean(M)−mean(P) when the same paired observations/weights contribute. Allow the operative M−P direction because F-ST1-008 independently covers the printed opposite header. This method reproduces handgrip First−2.85, Fifth−.97, eyelid First−4.25, Fifth−.95, Mean −2.11, Timed Up&Go Mean −1.12, and other rows within precision. The following named rows do not reproduce beyond 5% after rounding:

| Exact Table2 row | Placebo change | Mexiletine change | Printed effect | Recomputed M−P interval | Interval gap | Relative gap |
|---|---:|---:|---:|---|---:|---:|
| Handgrip fifth CLCN1 | -0.01 | -0.30 | 0.04 | [-0.300,-0.280] | 0.315 | 7.8750 |
| Relaxation first | -0.10 | -0.10 | -0.02 | [-0.010, 0.010] | 0.005 | 0.2500 |
| Relaxation mean | -0.07 | -0.05 | -0.02 | [0.010, 0.030] | 0.025 | 1.2500 |
| Peak force first | -7.81 | 18.92 | 32.92 | [26.720, 26.740] | 6.175 | 0.1876 |
| Peak force fifth | 6.15 | 27.96 | 24.08 | [21.800, 21.820] | 2.255 | 0.0936 |
| Peak force mean | -3.85 | 29.90 | 37.23 | [33.740, 33.760] | 3.465 | 0.0931 |
| Transient first | 0.69 | -2.4 | -3.7 | [-3.145,-3.035] | 0.505 | 0.1365 |
| Transient fifth total | 0.73 | -8.56 | -12.25 | [-9.300,-9.280] | 2.945 | 0.2404 |
| Transient fifth SCN4A | -5.00 | 9.56 | 13.71 | [14.550, 14.570] | 0.835 | 0.0609 |
| Transient mean total | -0.08 | -6.38 | -7.34 | [-6.310,-6.290] | 1.025 | 0.1396 |
| Transient mean SCN4A | -2.64 | 2.31 | 4.46 | [4.940, 4.960] | 0.475 | 0.1065 |

**Rule:** Same paired-difference identity and half-unit intervals applied uniformly; no model-versus-crude comparison is made for IVR mixed-model results. The source explicitly describes dependent t tests for these non-IVR outcomes. A reproducing method for other rows is enough under category 4; missing case/weight mapping is the human question.
**Focus area:** A, C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 4.
**Affected result or extracted value:** Listed non-IVR mean treatment effects, particularly handgripCLCN1+.04, peak force 32.92/24.08/37.23 and transient-paresis−12.25/−7.34.
**Why context does not resolve it:** Always-registercategory 4; the unknown exact paired subset cannot substitute for a supplied mapping.
**Alternatives / missing definition:** Period columns may use different available-case observations from paired-effect tests;31 sets may be weighted differently from 27 participants; subgroup effects may use an additional mixed model despite footnote a. These alternatives are grounded in stated missing outcomes, multiple sets and interaction analysis, but the source does not specify which applies to each listed estimate. Exact paired denominators, weights and outcome/model mapping are missing.
**Human question:** Which observations, weights and analysis generated each listed effect, and do its displayed treatment-period means use the same paired sample?



## C016 — SCN4A fifth-handgrip interval crosses zero while its P is significant

Pending Human Adjudication.

**Qualifying route:** Route A, category 1
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main Table 2 fifth-handgrip SCN4A row p.7 and repeated narrative p.8; rule p.4
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-ST1-003
**Checker provenance:** F-ST1-003
**Classification rationale:** The conflicting numbers, interval, label or test appear within one REPORT document. Plan material does not supply a conflicting comparator.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-ST1-003 — INCLUDE:** Route A, category 1 applies because the SCN4A fifth-handgrip95%CI−3.41 to+.51 includes zero while its printed two-sidedP=.009 is significant under the report's.05 rule.

Locations: REPORT [DOC-001 Table 2 SCN4A fifth handgrip p.7](../../jama_stunnenberg_2018_oi_180136.pdf#page=7), [repeated narrative p.8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8), [significance rule p.4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4). Effect−1.96; P interval [.0085,.0095] remains significant, CI rounding still crosses zero. Separate interactionP=.04 is not substituted for the within-SCN4A test. Different CI/test analyses remain an alternative without removing category1. S_W; statistical_results.


### Source-linked checker evidence

#### F-ST1-003

**Title:** SCN4A fifth-attempt handgrip interval includes zero but its P value is significant.

**Relationships:** S074. **Locations and roles:** REPORT DOC-001 [p.7 Table2, Handgrip action myotonia Fifth attempt SCN4A](../../jama_stunnenberg_2018_oi_180136.pdf#page=7), [p.8 narrative repeated effect/CI and footnotes](../../jama_stunnenberg_2018_oi_180136.pdf#page=8); REPORT p.4 two-sided P and significance P<.05.
**Printed values:** Effect −1.96 seconds, 95% CI −3.41 to+.51, P=.009; narrative repeats−1.96(−3.41 to+.51), separate interaction P=.04.
**Rule and calculation:** −3.41<0<+.51 while .009<.05. Every half-unit bound leaves CI crossing 0; P remains[.0085,.0095]. No covariance, df or choice between subgroup t/mixed inference is required. The printed interval midpoint−1.45 also differs from−1.96; this corroborates the reading but is not a second issue.
**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 1.
**Affected result or extracted value:** Within-SCN4A fifth-attempt handgrip treatment effect and significance.
**Why context does not resolve it:** Interval-versus-P conflict is always-register. The interaction P is a separate row and cannot substitute for subgroup P.
**Alternatives / missing definition:** Upper endpoint sign could differ; P and CI could come from distinct analyses. Neither definition is supplied for this row; a distinct-analysis alternative does not remove category 1.
**Human question:** Which interval and which two-sided test belong to the SCN4A effect −1.96 seconds?



## C017 — First-eyelid interval excludes zero while printed P equals the strict threshold

Pending Human Adjudication.

**Qualifying route:** Route A, category 1
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main Table 2 first-eyelid row p.7 vs strict significance rule p.4 and method footnotes p.8
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-ST1-007
**Checker provenance:** F-ST1-007
**Classification rationale:** The conflicting numbers, interval, label or test appear within one REPORT document. Plan material does not supply a conflicting comparator.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-ST1-007 — INCLUDE:** Route A, category 1 applies because first-eyelid effect−4.25 has95%CI−8.45 to−.05 excluding zero while printedP=.05 does not meet the source's strictP<.05 significance rule.

Locations: REPORT [DOC-001 Table 2 first eyelid p.7](../../jama_stunnenberg_2018_oi_180136.pdf#page=7), [strict rule p.4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), [method footnotes p.8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8). Independent paired-t diagnosticP=.0475236183 is a plausible latent roundedP; preserve this explicit alternative, but category1 is excluded from the display-precision screen. CI upper-limit interval [−.055,−.045] remains negative. S_W; statistical_results.


### Source-linked checker evidence

#### F-ST1-007

**Title:** First-attempt eyelid interval excludes zero but printed P=.05 fails the stated strict significance rule.

**Relationships:** S077. **Locations and roles:** REPORT DOC-001 [p.7 Table2 Eyelid closure First attempt](../../jama_stunnenberg_2018_oi_180136.pdf#page=7); REPORT p.4 explicitly P<.05 and two-sided tests, p.8 footnotes.
**Printed values:** Effect −4.25 seconds, 95% CI −8.45 to−.05, P=.05.
**Rule and calculation:** Upper bound−.05 excludes 0; printed .05 is not<.05. The upper bound half-unit interval[−.055,−.045] still excludes 0. P rounding interval[.045,.055] includes latent values on both sides of .05, but scope category 1 expressly excludes display-precision screening. A paired-t diagnostic with N 27 gives P=.0475236 and provides a plausible rounded P alternative.
**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 1.
**Affected result or extracted value:** First-attempt eyelid effect's significance at the stated strict .05 rule.
**Why context does not resolve it:** The scope requires registering a printed interval/test conflict irrespective of a rounding interpretation.
**Alternatives / missing definition:** Unrounded P≈.0475 would reconcile the interval and underlying strict significance decision; the report prints only .05.
**Human question:** What unrounded P and significance classification belong to this 95% CI?



## C018 — Placebo mean Timed Up and Go change exceeds its interval upper bound

Pending Human Adjudication.

**Qualifying route:** Route A, category 1
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main Table 2 mean Timed Up and Go placebo point and interval p.7; footnotes p.8
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-ST1-002
**Checker provenance:** F-ST1-002
**Classification rationale:** The conflicting numbers, interval, label or test appear within one REPORT document. Plan material does not supply a conflicting comparator.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-ST1-002 — INCLUDE:** Route A, category 1 applies because the mean Timed Up&Go placebo change+.07 exceeds its printed95%CI upper bound+.01, leaving an incompatible printed point/interval pair.

Locations: REPORT [DOC-001 Table 2 Timed Up&Go Mean placebo p.7](../../jama_stunnenberg_2018_oi_180136.pdf#page=7), [footnotes a/i p.8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8). Estimate [.065,.075], upper bound [.005,.015], minimum gap.050; printed lower bound−.67 is retained. An alternative upper endpoint or estimand is unspecified. S_W; statistical_results.


### Source-linked checker evidence

#### F-ST1-002

**Title:** Mean Timed Up&Go placebo change exceeds its printed upper confidence limit.

**Relationships:** S082. **Locations and roles:** REPORT DOC-001 [p.7 Table2, Timed Up&Go Mean, Change Placebo Period](../../jama_stunnenberg_2018_oi_180136.pdf#page=7); REPORT p.8 footnotes a/i.

**Printed values:** Placebo +.07 seconds(95% CI −.67 to+.01), mexiletine −1.05(−1.48 to−.62), effect −1.12(−2.07 to−.18), P=.02.
**Rule and calculation:** .07>.01, so point lies outside 95% CI. Mean rounding interval[.065,.075] and upper-bound interval[.005,.015] leave gap≥.050, relative gap=.050/.07=.7143. Ordered limits themselves reconcile; containment does not. The display-precision rule does not screen category 1.
**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 1.
**Affected result or extracted value:** Placebo mean Timed Up&Go change and 95% CI.
**Why context does not resolve it:** Printed point outside interval is always-register even though an intended symmetric endpoint might be reconstructed.
**Alternatives / missing definition:** A different upper limit or a differently attributed mean is possible; source specifies neither.
**Human question:** Which 95% CI is associated with the placebo +.07 second mean change?



## C019 — Needle-EMG estimate and interval do not yield the printed P under the stated test

Pending Human Adjudication.

**Qualifying route:** Route A, category 1
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main Table 2 needle-EMG row p.8 vs dependent-test and two-sided methods pp.3-4
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-ST1-006
**Checker provenance:** F-ST1-006
**Classification rationale:** The conflicting numbers, interval, label or test appear within one REPORT document. Plan material does not supply a conflicting comparator.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-ST1-006 — INCLUDE:** Route A, category 1 applies because the stated paired-t analysis associates needle-EMG effect.67 and95%CI.23–1.11 with two-sidedP≈.00428275, which cannot satisfy the printedP<.001.

Locations: REPORT [DOC-001 Table 2 needle EMG/footnotes a/m p.8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8), [dependent-t method p.3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [two-sided testing p.4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4). Independent diagnostic for27 pairs: halfwidth.44, t=3.1300107361, P=.0042827529; input-rounding diagnostic [.00369665,.00494118] stays above.001, and large-df diagnostic≈.002844 also does. A distinct test, interval convention or paired-subset mapping remains possible; both quantities being significant at.05 does not remove a numerical test/interval conflict. S_W; statistical_results.


### Source-linked checker evidence

#### F-ST1-006

**Title:** Needle-EMG effect/CI does not yield P<.001 under stated paired t inference.

**Relationships:** S098. **Locations and roles:** REPORT DOC-001 [p.8 Table2 continuation, needle EMG grading and footnotes a/m](../../jama_stunnenberg_2018_oi_180136.pdf#page=8); REPORT p.3 dependent-t methods, p.4 two-sided testing.
**Printed values:** Placebo 2.52(SD.89), mexiletine 1.85(SD 1.13), effect .67, 95% CI.23–1.11, P<.001, total N 27.
**Rule and calculation:** Difference 2.52−1.85=.67; h=.44. Paired-t on 27 pairs, df 26, SE.44/2.055529=.2140568, t=.67/.2140568=3.130011, two-sided P=.00428275. Half-unit inputs yield diagnostic P[.00369665,.00494118], entirely above .001. Gap to asserted upper bound .001≥.00269665. Since P is an inequality there is no unique printed P denominator for a relative discrepancy; normalized gap to .001=2.69665. Diagnostic df 30 gives P=.0040810; large-df diagnostic≈.002844 also exceeds .001.
**Focus area:** B, C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 1.
**Affected result or extracted value:** EMG-grading treatment P and compatibility with its reported 95% CI.
**Why context does not resolve it:** Always-register test / interval numerical incompatibility even though both suggest a positive treatment effect at .05.
**Alternatives / missing definition:** A distinct test generating P<.001, interval convention, or effect mapping might apply; none is stated for this row.
**Human question:** Which two-sided analysis generated P<.001 and which associated CI belongs to the .67-grade effect?



## C020 — Plan text and diagram specify different DSMB review triggers

Pending Human Adjudication.

**Qualifying route:** Route B
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** plan_material
**Relationship type:** P_P
**All relationships:** P_P
**Compared document roles:** PLAN protocol DSMB text p.38 vs PLAN protocol safety diagram p.39
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-009
**Checker provenance:** F-XS-009, F-ST1-206
**Classification rationale:** Both conflicting specifications belong to the prospective PLAN bundle. Report material only corroborates implementation and creates no additional relationship.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-XS-009 — INCLUDE:** Route B applies because the plan's population DSMB trigger differs in event set and inclusive/strict10% boundary between text and diagram, changing the planned continuation/stopping review rule rather than an administrative comparison.

Consolidate F-ST1-206 here. Retain PLAN [DOC-002 DSMB text p.38](../../joi180136supp1_prod.pdf#page=38) and [DSMB diagram p.39](../../joi180136supp1_prod.pdf#page=39). Text uses study-related SAEs at least10%(three patients); diagram uses cardiac AE/SAEs more than10%(three patients), alongside the common two-same-cardiac-event trigger. At target30,3/30=10%,4/30>10%; the parenthetical suggests the inclusive boundary but does not reconcile different qualifying event sets. Possible complementary triggers or a schematic summary remain alternatives; threshold attainment in actual trial is not claimed. P_P; plan_material.


### Source-linked checker evidence

#### F-XS-009 — Plan text and safety diagram define different study-level DSMB review triggers

- **Locations and roles:** [DOC-002 §8.4 p.38](../../joi180136supp1_prod.pdf#page=38), [Figure 3 p.39](../../joi180136supp1_prod.pdf#page=39), both PLAN. Source-linked full-page p.39 image was visually inspected.
- **Printed statements:** Text: accumulated serious adverse events related to study “equal to or more than 10% (three patients)” or two or more same cardiac AE/SAE triggers review. Diagram: cardiac events AE/SAE in “more than 10% (three patients)” or two or more same cardiac event triggers review.
- **Comparison logic:** First trigger differs in event category (all study-related SAEs versus cardiac AE/SAE) and boundary (≥10% versus >10%). With planned n=30, three patients=10%; ≥10% includes three and >10% first includes four, while diagram itself says three. Parenthetical three does not resolve the differing event sets. Percent threshold is a decision rule, so display rounding cannot replace its inequality.
- **Focus area:** D. **Proposed review domain:** plan_material. **Relationship:** P_P.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Prespecified safety-dependent study continuation/stopping review rule underlying the observed safety evaluation.
- **Why context does not resolve it:** Three noncardiac study-related SAEs and three varied cardiac AEs would activate different printed versions; no precedence instruction identifies the operative trigger.
- **Supported alternatives:** Diagram may summarize only cardiac surveillance while text retains a broader SAE rule; “more than” may have intended ≥. Both alternatives require clarifying which rule governed decisions.
- **Human question:** Did three study-related SAEs of any type, three cardiac AE/SAEs, or more than three cardiac events trigger DSMB review, and which text/diagram rule governed?


#### F-ST1-206 — Text and diagram give different DSMB population review triggers

- **Relationships:** S222. **Focus area:** D. **Proposed review domain:** plan_material. **Proposed relationship type:** P_P; all relationships P_P.
- **Exact locations/document roles:** PLAN [DOC-002 p.38 §8.4 final paragraph](../../joi180136supp1_prod.pdf#page=38) versus PLAN [p.39 Figure3 adverse reactions/events item2](../../joi180136supp1_prod.pdf#page=39). Both are prospective safety continuation/stopping rules. REPORT safety results establish that this monitored trial actually used the planned safety framework, without claiming threshold attainment.
- **Printed statements:** Text: accumulated study-related serious adverse events “equal to or more than10%(three patients)” or≥2 same cardiac AE/SAE. Figure: cardiac events(AE/SAE) “in more than10%(three patients)” or≥2 same cardiac events. Figure's individual-stop and population-review arrows are distinct and retained.
- **Rule/calculation:** At plannedN30,3/30=0.10,4/30=0.1333. Thus≥10% includesthree affected patients while>10% would first includefour; figure's parenthetical “three patients” itself does not implement its strict inequality. The event sets also differ: study-related SAE of any organ system versus cardiac AE/SAE. These are categorical decision rules; display precision is inapplicable to their stated strict/inclusive operators and event definitions. No observation of trial threshold attainment is inferred.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Planned rule for DSMB review and possible continuation/stopping of the study, needed to interpret the supplied safety analysis/stopping framework.
- **Why context does not resolve it:** The protocol explicitly identifies the diagram as detailed DSMB guidelines, yet three-patient boundary and qualifying event class differ from its text. These are planned decision inputs, not administrative counts or a preference for another safety policy.
- **Alternatives/missing definitions:** A broader text criterion and narrower cardiac-specific diagram could be separate complementary triggers, but neither source states that hierarchy. The figure's parenthetical may intend inclusive10%; the event-class distinction would remain.
- **Exact human question:** Which event class and inclusive/strict10% threshold governed population-level DSMB convening and continuation/stopping review?



## C021 — Plan interim text and diagram specify different prior information

Pending Human Adjudication.

**Qualifying route:** Route B
**Mechanical evidence recheck:** reproduced; all affected source locations confirmed in [the complete recheck](verification/evidence_recheck.md).

**Review domain:** plan_material
**Relationship type:** P_P
**All relationships:** P_P
**Compared document roles:** PLAN protocol noninformative-only interim text p.42 vs PLAN protocol informative-prior arrows p.43
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-008
**Checker provenance:** F-XS-008, F-ST1-205
**Classification rationale:** Both conflicting specifications belong to the prospective PLAN bundle. Report material only corroborates implementation and creates no additional relationship.
**Classification ambiguity:** None; source-grounded interpretation alternatives are retained below.

### Independent inclusion facts

**F-XS-008 — INCLUDE:** Route B applies because operative noninformative-only interim text and informative-prior arrows entering the plan's stopping/effectiveness paths specify different inputs to the primary-response stopping rule the reported N-of-1 analysis relies on.

Consolidate F-ST1-205 here. Retain PLAN [DOC-002 interim-prior text p.42](../../joi180136supp1_prod.pdf#page=42) and [decision diagram p.43](../../joi180136supp1_prod.pdf#page=43). The directly inspected arrows feed LR1's discontinuation-criteria and LR2's effectiveness paths; they are not merely a figure pointer. Caption does not identify a separate informative-prior procedure. Optional later clinical-decision support or an earlier diagram remains possible. REPORT [DOC-003 individual code p.10](../../joi180136supp2_prod.pdf#page=10) corroborates wide implemented priors and does not create P_R. P_P; plan_material.


### Source-linked checker evidence

#### F-XS-008 — Plan's interim diagram adds informative priors where its operative text permits only noninformative priors

- **Locations and roles:** [DOC-002 §9.2 p.42](../../joi180136supp1_prod.pdf#page=42), [Figure 4 p.43](../../joi180136supp1_prod.pdf#page=43), both PLAN. Source-linked full-page image p.43 was visually inspected.
- **Printed statements:** Text: “For our interim analyses we will use non-informative priors only,” to prevent elicited priors driving stopping advice. Figure prints “+informative priors” arrows into the LR1 discontinuation-criteria path and LR2 effectiveness decision.
- **Comparison logic:** The diagram labels adding informative priors on paths that produce continuation/discontinuation and treatment advice, while adjacent operative text rules them out. This changes primary-outcome interim computation, rather than a peripheral figure pointer. No arithmetic or display-precision calculation applies.
- **Focus area:** D. **Proposed review domain:** plan_material. **Relationship:** P_P.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Prospective prior specification for individual posterior efficacy advice used to stop primary N-of-1 observation.
- **Why context does not resolve it:** Caption/diagram supplies no separation of informative-prior treatment decisions from noninformative-prior stopping calculations; one arrow visibly feeds the “discontinuation criteria met?” branch.
- **Supported alternatives:** Informative priors may have been intended only for subsequent clinical decisions or as a schematic optional analysis; text may supersede an earlier illustration. The binding decision path is not identified.
- **Human question:** Which prior specification governed each diagrammed interim decision, and should the informative-prior arrows be read as separate clinical decision support?


#### F-ST1-205 — Interim prior text and decision diagram specify different information inputs

- **Relationships:** S228. **Focus area:** D. **Proposed review domain:** plan_material. **Proposed relationship type:** P_P; all relationships P_P.
- **Exact locations/document roles:** PLAN [DOC-002 p.42 §9.2](../../joi180136supp1_prod.pdf#page=42) versus PLAN [p.43 Figure4 first/second decision paths](../../joi180136supp1_prod.pdf#page=43). REPORT [DOC-003 p.10 eMethods1](../../joi180136supp2_prod.pdf#page=10) corroborates implemented wide priors only; it is not a conflicting side and does not addP_R.
- **Printed statements:** PLAN text: “For our interim analyses we will use non-informative priors only,” specifically because elicited priors could influence stopping advice. Figure4 has “+informative priors” arrows into the LR1 discontinuation decision and LR2 effectiveness decision paths. Direct source render confirms arrows, not OCR alone.
- **Rule/calculation:** Decision input “non-informative priors only” excludes added informative priors; diagram includes that addition in the paths that determine stopping/treatment advice. No numeric LR or posterior formula is supplied by the diagram; no numerical calculation or rounding rule can reconcile these categorical inputs.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** The individual posterior benefit probabilities and response-dependent stopping rule used to determine number of treatment pairs and subsequent regular mexiletine treatment.
- **Why context does not resolve it:** The explicit exclusivity in text and informative-prior decision arrows belong to the same prospective interim procedure, a statistical design element the report relies on. Figure4 is not labeled as an informative-prior alternative procedure. The LR terminology is not the basis of the finding.
- **Alternatives/missing definitions:** Dashed arrows may illustrate an optional or later clinical decision after the noninformative computation, or the diagram may reflect an earlier procedure. The relationship between dashed input arrows and interim posterior advice is not defined.
- **Exact human question:** Do informative priors enter either depicted interim stopping/effectiveness decision, and how should Figure4 be reconciled with the noninformative-only rule?



## C022 — Two baseline total means do not reconcile with displayed genotype aggregation

Pending Human Adjudication.

**Qualifying route:** Route A, category 4
**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main Table 2 total and genotype baseline means p.7 with nominal genotype counts and baseline footnote p.8; available-data context p.4
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-ST2-001
**Checker provenance:** F-ST2-001, fresh independent inclusion_screener_pass_2.
**Classification rationale:** Both total and subgroup mean summaries, group-count labels and baseline definitions occur within the main REPORT. No plan comparator supplies this conflict.
**Classification ambiguity:** None; outcome-specific sample membership and weighting are unavailable.

### Independent inclusion facts

The fresh screen confirmed both rows beyond the prescribed full-input half-unit rule, including continuous count intervals. Fifth-handgrip total 1.36 seconds has relative gap .105414439; fifth transient-paresis total 20.30% has relative gap .057667999. The same weighted identity reproduces the displayed stiffness baseline within precision. Missing row-specific available-case sample sizes or weights remain explicit alternatives. This baseline aggregation comparison is distinct from C015's period-mean treatment-effect comparison.

### Source-linked checker evidence

#### F-ST2-001

**Title:** Two Table 2 baseline total means do not reproduce the displayed genotype-group aggregation.

**Exact locations and document roles:** REPORT [main Table 2 baseline fifth handgrip, fifth transient paresis and comparator stiffness p.7](../../jama_stunnenberg_2018_oi_180136.pdf#page=7); REPORT [Table 2 footnotes a/b, genotype n=16/11 and visit-1 baseline definition p.8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8); REPORT [Numbers Analyzed and available-data statement p.4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4). Every location belongs to the published report. No PLAN comparison is needed.

**Printed values:** Total Table 2 N=27; genotype n=16 CLCN1 and n=11 SCN4A. Baseline fifth-handgrip mean: total 1.36 seconds, CLCN1 .93, SCN4A 2.59. Baseline fifth transient-paresis mean: total 20.30%, CLCN1 24.35%, SCN4A 9.12%. Comparator baseline stiffness: total 5.65, CLCN1 6.45, SCN4A 4.34. Non-IVR baseline measurements are explicitly from visit 1, start of the first treatment period; these baseline values are not the adjusted treatment-effect estimates.

**Rule and calculation:** For a total formed from two disjoint genotype groups, the aggregate mean is (nC×meanC+nS×meanS)/N. This calculation gives stiffness 5.590370, which reconciles with 5.65 under full display precision. It gives fifth-handgrip 1.606296 and fifth transient paresis 18.145185, each distinct from the printed total. The same-display reproducing method is used to locate the unavailable denominator/weight mapping rather than impose a preferred analysis.

Allow every displayed count its continuous half-unit interval: nC=[15.5,16.5], nS=[10.5,11.5], N=[26.5,27.5]; allow every displayed mean ±.005. Even using independently varying counts, a conservative interval wider than enforcing nC+nS=N, yields:

| Baseline row | Recomputed mean interval | Printed total interval | Interval gap | Relative gap |
|---|---|---|---:|---:|
| Fifth handgrip | [1.508363636,1.708301887] | [1.355,1.365] | .143363636 | .105414439 |
| Fifth transient paresis | [17.202000000,19.124339623] | [20.295,20.305] | 1.170660377 | .057667999 |
| Comparator stiffness | [5.287818182,5.904716981] | [5.645,5.655] | 0 | 0 |

Each affected row exceeds the relative .05 criterion even with conservative full-input precision. Aggregate mean transient paresis was also checked but is excluded below because its conservative interval gap is within .05. Integer-only count arithmetic was not substituted for the normative continuous display rule.

**Focus area:** C, statistical method logic and reported estimate aggregation.

**Proposed review domain:** statistical_results. **Provisional relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route A, category 4.

**Affected result or extracted value:** The baseline fifth-handgrip total mean of 1.36 seconds and fifth transient-paresis total mean of 20.30%, including the total versus genotype population/weight interpretation a data extractor attaches to those values. These are within-display aggregation relationships, not peripheral copies across baseline tables.

**Why context does not resolve it:** Category 4 applies: the aggregate mean identity reproduces another baseline row of the same display but does not reproduce these two rows after full display precision. The source does not provide outcome-specific baseline denominators or weights explaining which total and subgroup observations were summarized. The all-available-data statement identifies a possible mechanism but does not identify those baseline subsets. The printed Table 2 treatment-effect methods do not describe these baseline means as adjusted model estimates.

**Source-grounded alternatives and exact missing definitions:** Different available-case baseline subsets or weights may underlie the total and genotype summaries; reported missing outcome assessments make such subsets possible. The subgroup n=16/11 may indicate nominal trial group sizes rather than each row's actual baseline denominators. The reported 31 treatment sets do not themselves establish baseline replication because footnote b identifies only visit 1. Outcome-specific baseline n, total-versus-subgroup sample membership, weighting, and exact summary mapping are unavailable. No participant data are reconstructed and no consequence for a treatment effect is asserted.

**Exact human question:** Which baseline observations, denominators and weights produced the total and genotype means for fifth handgrip and fifth transient paresis, and how do those mappings reconcile the two printed total means with the displayed n=16/11 groups?



**Appended mechanical evidence recheck:** C022 is reproduced against main PDF pp.4,5,7,8; REPORT/S_W/statistical_results is confirmed. Nominal n16/11 is printed in an effect-related footnote; actual baseline denominators and weights are unavailable. Hypothetical available-case subsets can reconcile the means under the precision rule and remain diagnostic alternatives, not observed participant counts. Full evidence facts are in verification/parts/evidence_recheck_C022.md and the canonical recheck.
