# Cross-source Consistency Review — Workflow 1.6.2

Runtime agent ID: 01a129b4-ed97-7e21-94ff-d13c39bd4cee. Model: gpt-6.1-sol. Reasoning effort: medium. Start mode: FRESH_SPAWN. Source roles: DOC-001 main REPORT; DOC-002 protocol PLAN; DOC-003 SAP PLAN; DOC-004 results supplement REPORT. English scope and review contract were read completely. Both new evidence maps and their integral page transcripts were read completely. No old review conclusions, external literature, or web sources were used. Every comparison first matched population, outcome, time point, treatment contrast, model, analysis set, effect measure, and displayed precision.

## Exact scope and coverage

All matched results and statistical-design relationships in DOC-001 pp. 1–10, DOC-002 pp. 1–15, DOC-003 p. 1, and DOC-004 pp. 1–15 were reviewed: 41/41 source pages represented. The main map M001–M127 and support keys SUP-P01–SUP-P11/SUP-R01–SUP-R15, including every cell in the integral supplement transcription, were covered. Cover, reference and administrative pages were inspected for additional applicable relationships; none supplies another current-trial result. There is no supplied structured source. Every one of 18 secondary endpoint items was matched individually below. No analysis was inferred from a statistical result merely because a preferred method could have been applied.

Native-source checks used direct Poppler 26.01.0 pdftotext -layout. Exact cited statements were confirmed against source-page images, using curated current-source reusable images for main pp. 3, 6, 7, 8 and result pp. 10–11, and new CPU pdftoppm images for main pp. 2, 4, 9; protocol pp. 8, 12; SAP p. 1; result p. 14. Commands for every new derivative were `pdftoppm -f N -l N -singlefile -scale-to 1800 -png SOURCE OUTPUT_PREFIX`. New derivatives are `preprocessing/cross_source/main-p02.png`, `preprocessing/cross_source/main-p04.png`, `preprocessing/cross_source/main-p09.png`, `preprocessing/cross_source/protocol-p08.png`, `preprocessing/cross_source/protocol-p12.png`, `preprocessing/cross_source/sap-p01.png`, and `preprocessing/cross_source/results-p14.png`, each relative to review_1_6_2. Engine: Poppler 26.01.0; device CPU. No OCR or fallback environment was needed.

| Scope | Matching and completed check | Result |
|---|---|---|
| Primary result, main pp1/2/6/7 and supplement pp2/5 | Same randomized population, 24-week VAS change, same CI and test; original, age-adjusted and imputed sensitivities kept distinct | F-XS-001; otherwise displayed precision reconciles original-result copies |
| Primary endpoint, protocol pp2/6/8/11 and main pp1/3/7 | VAS 0–100, baseline-to-24-week change, index knee; recall wording compared explicitly | F-XS-002 |
| Primary model and conditional baseline adjustment, protocol p12/SAP p1/main pp4/6/7 | Planned change-score linear regression compared with printed mixed longitudinal model and coefficient contrasts | F-XS-003; baseline-imbalance adjustment principle agrees |
| Analysis populations and ≥80% criteria, protocol p12/SAP p1/main pp3/4/7/results pp2/3 | ITT, ≥1 outcome value, ≥1 dose safety set, per-protocol ≥80% intake; full report searched for outcome results in adherent subset | F-XS-004; all randomized participants initiated treatment, so safety criterion does not exclude another randomized subset |
| Missing data, protocol p12/SAP p1/main pp4/6/results pp2/6 | Conditional propensity weighting, available longitudinal observations, age adjustment, imputed sensitivity; primary original and sensitivity results not conflated | Excluded detail-only observations below |
| Sample size/power, protocol p12/main p4 | Adopted pain and effusion assumptions distinguished from explicitly hypothetical historical WOMAC illustration | F-XS-005 |
| Hypothesis, margin, multiplicity, interim and stopping | Primary superiority direction agrees; two-sided .05 agrees; no noninferiority/equivalence margin, prespecified multiplicity adjustment, formal interim or stopping rule printed; protocol explicitly requires no DSMB | No conflict; absent rule not manufactured |
| Intervention, protocol pp6/7/main pp1/2/3/8/9 | Two daily capsules, 2 g/d for 24 weeks agree; report EPA/DHA daily dose agrees with per-softgel composition; printed other omega-3 percentage assessed | F-XS-008 |
| Participant flow, main pp1/3/7 | Screening/randomization totals and primary model totals agree; treatment completion vs follow-up completion assessed separately | Small numerical copy gaps below display threshold; no finding |
| All main Table2 outcomes vs results eTable4 | Every matching 24-week mean/change/CI/P copied result assessed; earlier time points kept distinct; all 62 eTable4 rows inspected | Matched estimates agree; different contributor n are peripheral, documented below |
| Secondary effusion and triglyceride narrative/main Table2/eTable4 | Main p7 effusion 24-week and triglyceride 12-week contrasts matched to their own rows | Agree; exploratory caveat distinguished from hierarchy change |
| Main Figure2 and result eFigure | Raw participant 24-week change distributions vs modeled means, missing-follow-up exclusions, anatomical illustration | No exact numerical group result invented from graphical distributions |
| Exposure/adherence, main pp5/7/8/results pp3/4 | Omega-3 Index and pill-intake frequencies, means and available pill-count populations kept distinct | Index copies agree; small adherence percentage difference below threshold |
| Safety, main pp1/7/8 and results pp10–14 | Aggregate AE counts, individual event types, treatment columns, SAE totals and relatedness | F-XS-006 and F-XS-007; peripheral and small copy gaps separately screened |
| Plan-internal comparisons, protocol pp2/6–12/SAP p1 | Endpoint lists, assessment schedule, analysis, dose, power hypotheses, missingness and criteria compared | SAP reproduces protocol p12; peripheral schedule differences below |

### Item-by-item planned secondary endpoint coverage

Plan locations: [protocol p6](../../../joi240048supp1_prod_1727199125.7845.pdf#page=6) and [p7](../../../joi240048supp1_prod_1727199125.7845.pdf#page=7), all PLAN. Report locations: [main p3](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=3), [p4](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4), [p6](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6), [results p5](../../../joi240048supp3_prod_1727199125.83025.pdf#page=5), [p6](../../../joi240048supp3_prod_1727199125.83025.pdf#page=6), [p8](../../../joi240048supp3_prod_1727199125.83025.pdf#page=8), [p9](../../../joi240048supp3_prod_1727199125.83025.pdf#page=9), [p10](../../../joi240048supp3_prod_1727199125.83025.pdf#page=10), [p14](../../../joi240048supp3_prod_1727199125.83025.pdf#page=14), all REPORT. No outcome is expressly designated key secondary in the supplied plan; none of these secondary outcomes is reported in the abstract. Secondary nonreporting alone therefore does not meet the key-secondary nonreporting category. Changes in prespecified status or composite definitions were nevertheless independently sought.

| Planned item | Definition/time | Report match and check |
|---|---|---|
| 1 | Maximal effusion area AND volume, 24 weeks | Volume main pp3/6/7; maximal area absent. Not represented as a reported maximal-area result; absence considered below |
| 2 | Ordinal knee effusion, 24 weeks | WORMS change results p8; category direction agrees with main MRI definition |
| 3 | BML maximal area, 24 weeks | Main p4 explicitly retains prespecified secondary status but says not assessed for budget; no status change |
| 4 | Ultrasound parameters, 24 weeks | Main p4 explicitly retains secondary status and says not reported for missing data |
| 5 | Knee VAS 4/8/12/16/20 weeks | Results p5 has every planned time point; 24 weeks remains primary |
| 6 | WOMAC total/weight-bearing/non-weight-bearing pain, all time points | Main p6/results p5 preserve all three components and 4/8/12/16/20/24-week contrasts |
| 7 | Hand/back VAS, all time points | Main p6/results pp5–6; six follow-up time points each |
| 8 | Knee function, all time points | WOMAC function main p6/results p5, six time points |
| 9 | OMERACT-OARSI responder, all time points | Main pp3/6/results pp6–7, all six time points; pain/function/global criterion components enumerated in main |
| 10 | hsCRP, 12/24 weeks | Main p6/results p6; original and baseline-adjusted interpretation kept distinct |
| 11 | Blood lipids, 12/24 weeks | HDL/LDL/triglycerides main p6/results p6; 12-week significant triglycerides not compared with 24-week null result |
| 12 | Glucose, 12/24 weeks | Main p6/results p6; schedule matches |
| 13 | Dynamometer leg strength, 12/24 weeks | Main pp4/6/results p6; both-leg description compared with index-limb shorthand |
| 14 | Analgesic use, all time points | Main p4/results p9; descriptive NSAID-change table, with blank preserved rather than forced to zero |
| 15 | AQoL, 'all time points, 12 and 24 weeks' | Protocol schedule p11 baseline12/24 matches results p6; main p4 says all time points; schedule terminology compared below |
| 16 | Study-knee PPT, 24 weeks | Main p4 explicitly says secondary outcome unreported due to missing data; baseline available main p5 |
| 17 | Adverse events, 12/24 weeks | Main pp7/8/results pp10–14; events collected throughout; safety result attribution assessed |
| 18 | Costs, time points TBA | Main p4 retains secondary status but unassessed; protocol p9 economic analysis explicitly conditional on meeting primary endpoints |

### Item-by-item eligibility and analysis-set criteria

Protocol [p7](../../../joi240048supp1_prod_1727199125.7845.pdf#page=7), PLAN, compared with main [p2](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=2), [p3](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=3), [p4](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4), and [p9](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=9), REPORT. These comparisons do not substitute a broad enrollment/design audit for the quantitative scope.

| Criterion | Exact comparison | Scope assessment |
|---|---|---|
| Inclusion 1 age | PLAN >40; REPORT ≥40, observed range starts40 | Enrollment boundary differs; no supplied outcome estimate or analysis-set size attributed differently |
| Inclusion 2 pain | PLAN >40mm most days; REPORT ≥40 at screening | Screening boundary/wording differs; primary recall discrepancy independently F-XS-002 |
| Inclusion 3 MRI effusion | PLAN present; REPORT modified WORMS ≥1 | Same any-effusion criterion expressed operationally |
| Inclusion 4 ACR OA | PLAN ACR clinical confirmed rheumatologist; REPORT symptomatic ACR OA/study physician | Same condition, assessor detail does not change an extracted result |
| Exclusion 1 MRI inability | Both contraindication/inability | Reconciles |
| Exclusion 2 severe OA | Both radiographic grade3 | Reconciles |
| Exclusion 3 medication | Both anticoagulants/high-dose aspirin/NSAIDs | Matches printed exclusion, concomitant-treatment paragraph in both permits NSAIDs; in-plan tension is clinical enrollment wording, not an analysis decision |
| Exclusion 4 fish/krill medication cessation | Both cessation during trial; report30days/minimum4weeks, protocol p9 four weeks | Reconciles practical washout |
| Exclusion 5 seafood | PLAN ≥1 fish/seafood meal/week excluded; REPORT p9 dietary omega-3 unrestricted | Dietary enrollment difference; no quantified changed analysis population supplied |
| Exclusion 6 inflammatory arthritis | Both excluded | Reconciles |
| Exclusion 7 seafood allergy | Both excluded | Reconciles |
| Exclusion 8 injury | PLAN within6months; REPORT injury example/surgery <12months | Clinical screening window differs; not endpoint/analysis-set rule |
| Exclusion 9 surgery | Both surgery <12months, protocol also planned surgery; Figure1 opted surgery exclusion | Reconciles operative enrollment context |
| Exclusion 10 injections | Both steroids3months/hyaluronic6months | Reconciles |
| Exclusion 11 pregnancy/lactation | Both excluded | Reconciles |
| Exclusion 12 investigational product | PLAN30days; report methods does not list | Detail absent; no contradictory number or changed result |
| Exclusion 13 serious illness | PLAN precludes24wk; report Figure1 excludes11 for serious illness | Reconciles |
| Exclusion 14 consent | Both unable consent excluded | Reconciles |
| Analysis ITT | PLAN all outcomes ITT; REPORT randomized with ≥1 corresponding outcome | Primary model contains130/132, all randomized; no demonstrated primary-set size conflict |
| Safety | REPORT ≥1 dose; Figure1 all randomized initiated | Same primary randomized totals available; no new excluded primary population inferred |
| Per protocol | PLAN ≥80% capsule intake; REPORT descriptive intake counts but no subset outcome analysis | F-XS-004 |
| Responder success | Main pain/function/global thresholds itemized; plan names standard responder criteria without altered component list | No reproduced changed composite definition |
| Primary success | PLAN10mm superiority hypothesis, α.05 two-tailed; REPORT no significant superiority using95%CI/.05 | Direction and decision logic agree;10mm target distinguished from15mm MCII |

## Findings

### F-XS-001

Primary VAS point-estimate sign differs between Key Points and matched original-result copies.

- **Compared locations and roles:** REPORT [main p2, Key Points](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=2), versus REPORT [main p1 abstract](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=1), [p6 Table2](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6), [p7 Primary Outcome](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7), and REPORT [results p2 original row](../../../joi240048supp3_prod_1727199125.83025.pdf#page=2), [p5 24-week knee VAS](../../../joi240048supp3_prod_1727199125.83025.pdf#page=5).
- **Printed values:** Key Points mean difference +0.30; abstract/Table2/text/eTable4 −0.3, CI−6.9 to6.4; original sensitivity-table difference−0.27, CI−6.92 to6.38. P=.94 where printed. Same262 randomized participants and 24-week outcome.
- **Comparison logic and reproduction:** Half-unit intervals for +0.30 and−0.3 are [0.295,0.305] and [−0.35,−0.25]; gap0.545; relative gap0.545/0.30=1.817, above.05. The original−0.27 interval [−.275,−.265] corroborates the negative copy. Reversing a contrast would also reverse its CI; Key Points retains the same CI and states no distinct contrast.
- **Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship:** S_C; **all relationships:** S_C, S_W.
- **Qualifying route:** Route A, category 2.
- **Affected result or extracted value:** Sign of the primary 24-week between-group VAS estimate.
- **Why context does not resolve it:** Route A category2 applies to a reproduced printed sign change regardless of the negligible clinical magnitude or unchanged nonsignificant test.
- **Supported alternatives:** Key Points could use an absolute magnitude or opposite contrast, but neither is stated and its CI has not changed direction. All original-result copies could instead share the other sign convention; the source does not identify this.
- **Exact human question:** Which signed treatment contrast is intended for the Key Points primary mean difference, and should it use the same sign and CI orientation as the abstract and original-analysis tables?

### F-XS-002

Planned and reported primary pain outcome use different recall windows.

- **Compared locations and roles:** PLAN [protocol p8 Primary outcome: Pain](../../../joi240048supp1_prod_1727199125.7845.pdf#page=8), with primary24-week outcome on PLAN [p6](../../../joi240048supp1_prod_1727199125.7845.pdf#page=6), versus REPORT [main p3 Primary Outcome](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=3).
- **Printed statements:** Protocol asks how participants rate pain 'today'; main specifies self-reported VAS knee pain 'over the past 7 days'. Both define baseline-to-24-week primary VAS change, 0–100.
- **Comparison logic and reproduction:** A same-day rating and a past-week rating are different specified outcome windows, although the instrument and follow-up visit agree. This is a categorical endpoint-definition comparison; half-unit display rounding is not applicable.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship/all relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Outcome window underlying the primary mean change−19.9/−20.2 and mean difference−0.3 at24weeks.
- **Why context does not resolve it:** Neither the source protocol nor report identifies an amendment or explains whether actual questionnaires rated current pain or the previous week. A reader cannot identify the underlying primary recall period from the two supplied specifications.
- **Supported alternatives:** A later questionnaire amendment may have changed the recall window, or one passage may summarize the collected item differently. No questionnaire text beyond the protocol's question is supplied.
- **Exact human question:** Was the analyzed primary VAS item pain today or pain over the past7days, and what dated plan or amendment documents that outcome window?

### F-XS-003

Reported primary longitudinal model differs from the supplied planned change-score regression.

- **Compared locations and roles:** PLAN [protocol p12 Statistics](../../../joi240048supp1_prod_1727199125.7845.pdf#page=12), PLAN [SAP p1 lines5–7](../../../joi240048supp2_prod_1727199125.8245.pdf#page=1), versus REPORT [main p4 Statistical Analyses](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4) and [p7 methods continuation](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7).
- **Printed statements:** Plan uses linear regression comparing changes in pain, maximal effusion size and function, univariate/multivariable if baseline imbalance. Report evaluates primary and secondary outcomes with linear mixed model including treatment, month, treatment×month; participant and center random intercepts; month random slope; changes and contrasts from linear combinations of coefficients.
- **Comparison logic and reproduction:** A printed regression of change scores and a longitudinal mixed model with specified participant/center/time random effects are distinct stated analysis specifications. Conditional baseline adjustment agrees and is not itself the issue. Categorical comparison; numerical rounding is not applicable.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship/all relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Analysis producing the primary24-week VAS mean difference/CI/P and related effusion/function contrasts.
- **Why context does not resolve it:** Route A category5 applies to a planned primary analysis replaced in the report. The broad fact that both model families are linear does not identify a supplied prespecified longitudinal model.
- **Supported alternatives:** A dated amendment could have replaced the regression specification; alternatively, report may mean the mixed model was an implementation of the original broad regression intention. Neither supplied plan describes these random effects or the treatment×month model.
- **Exact human question:** Which dated analysis specification authorized the reported longitudinal mixed model for the primary result, and was the supplied change-score regression also performed?

### F-XS-004

Planned adherent-subset analysis of the primary outcome is absent from the supplied report.

- **Compared locations and roles:** PLAN [protocol p12 Statistics](../../../joi240048supp1_prod_1727199125.7845.pdf#page=12), PLAN [SAP p1 lines8–9](../../../joi240048supp2_prod_1727199125.8245.pdf#page=1), versus REPORT [main pp4/7 methods and results](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4), [main p7](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7), REPORT [results p2 primary sensitivities](../../../joi240048supp3_prod_1727199125.83025.pdf#page=2) and [p3 adherence](../../../joi240048supp3_prod_1727199125.83025.pdf#page=3). Absence check covers all10main and all15results pages.
- **Printed statements:** Plan says per-protocol analyses will be completed for participants consuming≥80% capsules. Report gives randomized longitudinal analyses; eTable1 gives original, age-adjusted and multiple-imputation primary analyses; eTable2 gives ≥80% intake frequencies, not outcome effects for that set.
- **Comparison logic and reproduction:** The plan's unconditional per-protocol analysis supplements the ITT analysis and includes primary pain. None of the complete supplied results provides a primary effect/CI/P restricted by the≥80% criterion. Descriptive pill adherence does not supply that analysis. Categorical absence comparison; no rounding calculation applies.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship/all relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Prespecified adherent-subset primary24-week knee pain contrast and its relationship to the reported randomized-population contrast.
- **Why context does not resolve it:** Route A category5 explicitly includes an unreported planned primary analysis. High adherence and an available-case primary model do not identify the prescribed adherence subset.
- **Supported alternatives:** Analysis may have been performed but omitted, or amended out of the plan; incomplete pill-count data may have prevented a planned implementation. The supplied report states no such amendment or result.
- **Exact human question:** Where is the prespecified≥80%-capsule per-protocol primary VAS result, or which dated amendment explains its omission?

### F-XS-005

The reported adopted power assumptions do not match the supplied adopted plan.

- **Compared locations and roles:** PLAN [protocol p12 Power calculations](../../../joi240048supp1_prod_1727199125.7845.pdf#page=12), PLAN [protocol p2 secondary hypothesis](../../../joi240048supp1_prod_1727199125.7845.pdf#page=2), versus REPORT [main p4 Power Calculations](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4).
- **Printed values:** Plan pain10mm difference, SD25.5,90%power,.05,234participants inflated10% to260/130perarm. Report pain10points, SD23.8,90%power,.05,130perarm. Plan effusion96%power for20% difference, mean2.24cm² and SDchange1.35; report90%power for4.5mL effusion-volume change. Protocol's later conditional n54WOMAC illustration is explicitly not the adopted basis and is excluded from this comparison.
- **Comparison logic and reproduction:** PainSD intervals [25.45,25.55] versus [23.75,23.85] leave1.60gap; relative to plan25.5, gap=.06275. Printed96% and90%power intervals [95.5,96.5]/[89.5,90.5] leave5percentage-points gap; relative to96, .05208. Both exceed.05. Area in cm² versus volume in mL is a distinct dimensional endpoint, with no supplied conversion allowing the20% area target to become4.5mL. The same nominal130perarm does not reconcile these adopted inputs.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship/all relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Prespecified detectable primary pain effect/dispersion and secondary effusion effect/power underpinning trial size and interpretation of the supplied precision.
- **Why context does not resolve it:** The report cites different trials as its source but does not identify an amendment replacing the supplied prospective power calculation or explain the area-to-volume target. This leaves which calculation governed the design unclear.
- **Supported alternatives:** A revised calculation could have changed the adopted SD and effusion endpoint while retaining130perarm, or report could present a retrospective design summary. A dated amended calculation is not supplied.
- **Exact human question:** Which calculation was prospectively adopted, and what version documents the change from25.5 to23.8 painSD and20% area/96%power to4.5mL volume/90%power?

### F-XS-006

Selected printed adverse-event subrows attribute the counts to opposite treatment groups.

- **Compared locations and roles:** REPORT [main p8 Table3](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=8), versus REPORT [results p10 eTable7 cough](../../../joi240048supp3_prod_1727199125.83025.pdf#page=10) and [p11 eTable7 gastrointestinal rows](../../../joi240048supp3_prod_1727199125.83025.pdf#page=11).
- **Printed values:** Main krill/placebo: cough2/0; gastroesophageal reflux1/3; abdominal discomfort0/3. Supplement krill/placebo: coughblank/2; reflux3/1; abdominal discomfort3/blank. Both tables clearly label krilln130 and placebon132. Blanks are not silently converted to printed zeros; the positive printed count appears under the opposite treatment label.
- **Comparison logic and reproduction:** Same event types and study period. Main placebo cough0 versus supplement placebo2 leaves gap1 between half-unit intervals [−.5,.5] and[1.5,2.5]; reference zero makes any positive gap reproduced. Main krill reflux1 versus supplementkrill3 leaves gap1, relative1/1=1; main placebo reflux3 versus supplementplacebo1 leaves gap1, relative1/3=.333. Main krill abdominal discomfort0 versus supplementkrill3 leaves gap2, reference zero reproduced. Treatment-column headings do not reverse elsewhere in either display. Nasopharyngitis2/1 versus1/2 and diarrhea2/1 versus1/2 are not added to the finding because their literal half-unit intervals touch, as recorded below.
- **Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship/all relationships:** S_C.
- **Qualifying route:** Route A, category 2.
- **Affected result or extracted value:** Treatment-specific cough, reflux and abdominal-discomfort event counts for safety extraction.
- **Why context does not resolve it:** Route A category2 applies to printed substituted treatment-specific counts whose magnitude changes beyond display precision. No table note assigns a different subset or reverses treatment columns for these rows.
- **Supported alternatives:** Individual rows could have treatment-column substitutions, or different event coding/subsets might have been used; the supplied headings and period do not disclose the latter.
- **Exact human question:** Which treatment-specific event counts apply to these three event types, and do the main and supplementary subrows represent the same coding and event population?

### F-XS-007

The stated absence of treatment-related serious events does not reconcile with the supplement's printed relatedness classifications.

- **Compared locations and roles:** REPORT [main p8 Table3 final row, footnote b, and safety paragraph](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=8), versus REPORT [results p14 eTable8](../../../joi240048supp3_prod_1727199125.83025.pdf#page=14).
- **Printed statements:** Main any treatment-related SAE0/0, no related SAE identified by investigators, and all events considered unrelated. Supplement labels one krill transfusion-dependent anaemia event 'Probable'; seven other krill event entries and three placebo entries 'Possible'; krill fracture-fixation/placeboappendicitis 'Unlikely'; two placebo entries 'NA'. SAE totals9krill/6placebo match the main totals.
- **Comparison logic and reproduction:** Same complete SAE display and treatment totals. A printed 'Probable' relation, along with ten 'Possible' entries, is not explicitly mapped to the report's all-unrelated classification. This is an unresolved categorical relation/aggregation rule, not an assumed clinical causality decision. Half-unit numeric precision is inapplicable to the categorical conflict; an integer0-versus1 comparison is not used to bypass its touching half-unit intervals.
- **Focus area:** A/C. **Proposed review domain:** statistical_results. **Proposed relationship/all relationships:** S_C.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Treatment-related SAE classification and count used for safety extraction, particularly the krill anaemia event.
- **Why context does not resolve it:** Neither display states a relatedness threshold or explains whether supplement labels are preliminary assessments subsequently replaced by investigator adjudication. The same events can therefore be extracted as all unrelated or containing a probable treatment relation.
- **Supported alternatives:** Main could summarize a later investigator assessment, while supplement retains earlier possible/probable coding; alternatively, 'treatment-related' could use an unstated threshold. No supplied note identifies either reconciliation.
- **Exact human question:** Which relatedness assessment governs the SAE summary, how are Possible/Probable mapped into treatment-related events, and was the probable anaemia classification subsequently changed?

### F-XS-008

The printed percentage of other omega-3 content in the placebo differs tenfold between report locations.

- **Compared locations and roles:** REPORT [main p2 Interventions, continuing p3](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=2), [main p3](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=3), versus REPORT [main p9 Discussion](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=9).
- **Printed values:** Both passages describe the same placebo oil as containing less than5mg/g of other omega-3 content; Methods gives the parenthetical0.5%, Discussion0.05%.
- **Comparison logic and reproduction:** At1g=1000mg,5mg/g corresponds to0.5%, while0.05% corresponds to0.5mg/g. Printed percentage half-unit intervals[.45,.55] and[.045,.055] leave.395percentage-points gap; relative to Methods.5%, gap=.79, above.05. The two percentages therefore state different upper concentration bounds for the same supplied comparator composition.
- **Focus area:** A/D, percentage extraction and randomized-comparator composition. **Proposed review domain:** statistical_results. **Proposed relationship/all relationships:** S_W.
- **Qualifying route:** Route A, category2.
- **Affected result or extracted value:** Other omega-3 percentage upper bound extracted for placebo exposure when interpreting the knee-pain and effusion contrasts.
- **Why context does not resolve it:** RouteA category2 includes reproduced decimal/percentage changes of magnitude. The intended conversion can be reconstructed, but a reader can still extract either printed percentage; this is a numerical change, rather than merely a missing unit sign.
- **Supported alternatives:** Discussion could have a decimal-position substitution, or a different composition upper bound could have been intended. Both passages retain the same5mg/g value, favoring a single mass-concentration definition without conclusively assigning the intended percentage.
- **Exact human question:** Is the comparator's other omega-3 upper bound5mg/g (0.5%) or0.5mg/g (0.05%), and which printed mass and percentage values represent the supplied placebo?

## Excluded observations

Only apparent issues considered but not emitted are listed; reconciled checks appear in the coverage tables above. Each row has one reason code. There are19 excluded-observation rows.

| Location | Observation | Reason code |
|---|---|---|
| Mainp3 Figure1 vsp1/p7 | Figure completion224/discontinuation38 vs textcompletion222/discontinuation40; paired copies224/222 half-unitgap1 /224=.00446 and38/40 gap1 /38=.02632, both≤.05; placebo21vs23 gap1 /21=.04762 | ROUNDING_OR_DISPLAY_PRECISION |
| Mainp6 vsp7/resultspp5–6 | Contributor n differs between several main24-week cells and supplemental observed24-week rows; these are per-time-point observation counts, with unchanged matched estimates and primary randomized analysis n | PERIPHERAL_COMPARISON |
| Mainp7 vsresultsp3 | Printed95%≥80%adherence vs82+81 out of167 (=97.60%); allowing95±.5%, exactcounts and denominator half-units leaves minimum recomputed96.716%, gap1.216points /95=.01280≤.05 | ROUNDING_OR_DISPLAY_PRECISION |
| Mainp8Table3 vsabstractp1/textp8/resultsp10 | Placebo extremity pain6 vs5; [5.5,6.5]/[4.5,5.5] touch, gap0 under literal printed-copy precision rule | ROUNDING_OR_DISPLAY_PRECISION |
| Mainp8Table3 vsresultspp10–11 | Nasopharyngitis2/1 vs1/2 and diarrhea2/1 vs1/2 have adjacent integer copies; half-unit intervals touch, gap0; nonadjacent reversals independently F-XS-006 | ROUNDING_OR_DISPLAY_PRECISION |
| Mainp8 vsresultspp10–13 | Respiratory/gastrointestinal aggregate categories and individual2-event administrative/safety-copy discrepancies are peripheral secondary displays when not an independently reproduced printed-value slip | PERIPHERAL_COMPARISON |
| Protocolp12/SAPp1 vsmainp4 | Missing data propensity weighting 'as appropriate' vs age-related sensitivity; report does not state weighting was omitted or prohibited, so missing implementation detail alone does not reproduce a changed missing-data rule | CONDITIONAL_OR_UNREPORTED |
| Mainp6/resultsp6 vsresultsp2 | No imputation statements apply to original reported analyses, while separately labeled multiple-imputation sensitivity is distinct; no imputed primary result substituted for original | CONTEXT_RESOLVES |
| Protocolp11 vsmainp4/p6 ICOAP | Prospective questionnaire collection does not specify an ICOAP outcome analysis or its hierarchy; post hoc analysis label cannot alone establish a changed prespecified outcome status | CONDITIONAL_OR_UNREPORTED |
| Protocolpp6–7 vsmainp7 | Main calls these secondary outcomes throughout but says their results should be considered exploratory because of number; an inferential caution does not itself change their prespecified outcome status | TERMINOLOGY_OR_WORDING |
| Protocolp6 vsmainpp3–4/results | Maximal effusion area unreported, but no supplied designation as key secondary and no abstract result; volume reported separately; non-key secondary absence alone does not meet routeA5 | CONDITIONAL_OR_UNREPORTED |
| Protocolpp6–7 vsmainp4 | BML/PPT/ultrasound not reported, but retained as secondary and explicitly disclosed; no supplied key-secondary designation or changed outcome status | CONDITIONAL_OR_UNREPORTED |
| Protocolp9 vsmainp4 | Economic analysis conditional on primary endpoints met; negative primary trial expressly explains unassessed economics | CONTEXT_RESOLVES |
| Protocolpp7/9 vsmainpp2/9 | Eligibility age/pain strictness, injury window, fish-intake restriction and omitted investigational-product criterion are clinical enrollment differences, not a changed numerical primary/key-secondary outcome, quantified analysis-set size or statistical decision rule | OUT_OF_FOCUS |
| Protocolpp7/9/mainp2/p4 | NSAID exclusion versus stable concomitant NSAID use appears in both plan and report; concerns enrollment-medication terminology and contraindication, without a supplied changed primary analysis size or decision | OUT_OF_FOCUS |
| Protocolpp7/9/10/11 | Plan administrative recruitment calendar and anthropometry/blood/PPT schedules vary by description; no primary/key-secondary result or statistical decision changes | PERIPHERAL_COMPARISON |
| Mainp4/results p7 | Both-leg strength measured simultaneously versus index lower-limb shorthand; no changed printed treatment estimate or analysis attribution | TERMINOLOGY_OR_WORDING |
| Mainp7 vsmainp6 | 'No changes in post hoc outcomes' follows between-arm comparisons; it naturally denotes no between-arm benefit, while within-arm changes are tabulated | CONTEXT_RESOLVES |
| Mainpp8–9 vspp6–7 | Broad discussion no-effect wording followed by explicit placebo effusion reduction and chance caveat; same numeric effusion result retained and no changed extractable value | CONTEXT_RESOLVES |

## Closeout

Findings:8 (F-XS-001 through F-XS-008). Excluded observations:19. Primary/key-secondary matched-result hierarchy applied throughout; no candidate quota. All41 supplied pages and all18 planned secondary items covered. No scientific coverage gap. Limitations: supplied material does not contain raw participant linkage, actual VAS questionnaires beyond the protocol item, a later dated plan/amendment, or SAE coding-to-final-assessment mapping. Graphical distributions are not tabulated exact observations; no artificial digitization was used. These are evidence limitations, not omitted source units. Findings are proposals for independent inclusion screening, with no C IDs, adjudications, severity labels, or suggested corrections.
