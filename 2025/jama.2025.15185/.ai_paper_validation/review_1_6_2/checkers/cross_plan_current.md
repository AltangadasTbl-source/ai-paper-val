# Current cross-source checker: plan comparisons

## Scope and source authority

This disjoint shard covers every PLAN–REPORT and PLAN–PLAN statistical-design comparison in DOC-002 (protocol bundle, 94 pages) and DOC-003 (SAP, 18 pages), matched to DOC-001 (main report, 10 pages) and DOC-004 (results supplement, 27 pages). REPORT–REPORT comparisons belong to the parent checker and are not emitted here. No structured workbook, CSV, or Office source was supplied. The complete scope and review contract were read. Only current-run fresh factual maps and supplied sources were used; pre-existing 1.6.2 assets and scientific conclusions were excluded.

Current factual maps read completely and separately: fresh_support_protocol_a.md, fresh_support_protocol_b.md, fresh_support_protocol_c.md, fresh_support_sap.md, main_quantitative_evidence.md, and fresh_support_results.md, all in ../extraction/. The maps establish complete page coverage and distinguish protocol 1.1 from 1.4. Comparisons below use the final supplied protocol 1.4 when assessing the report; documented differences from protocol 1.1 are version context, not automatically additional findings.

Direct confirmation for every emitted observation used the exact supplied PDFs, freshly rendered with the pinned package-local interpreter and supplied pdf_tools.py render command (Py Mu PDF 1.26.4, 200 dpi, CPU). Inspected renderings: protocol page 86; SAP pages 4, 5, 6, 7, 8, 9, 10, 11, 12, 15; main pages 3, 4, 5; results page 7. Temporary derivatives are /tmp/cross-plan86.png, /tmp/cross-sap4.png through /tmp/cross-sap12.png, /tmp/cross-sap15.png, /tmp/cross-main3.png through /tmp/cross-main5.png, and /tmp/cross-results7.png. Source-linked current maps, including fresh OCR as locator where needed, support the remaining reconciling comparisons. No source or reused derivative was changed.

Four findings and seven excluded apparent observations are recorded. Numerical result copies are matched by population, time, contrast, model, measure, analysis set, and displayed precision before comparison. These findings concern explicit design or analysis statements; none treats a crude descriptive difference as an adjusted coefficient.

## Complete statistical-design comparison matrix

All protocol and SAP locations in this table have role PLAN; main and results-supplement locations have role REPORT. Page numbers are physical PDF pages. Each list item has an explicit record; grouped scale domains and safety events are individually enumerated below.

| Element or list item | PLAN source and specification | Matched REPORT source and comparison record |
|---|---|---|
| Primary endpoint identity | Protocol pp 54,69; SAP p 5: final FMMA total at Visit 3 | Main pp 1,3,4,6: affected-side FMA total; equivalent clinical scale/name, same final-score endpoint |
| Primary scale and direction | Protocol p 69; SAP p 5: 0–100; items 0/1/2; upper 66, lower 34; higher better | Main p 3 agrees item scoring, total and subscales; no composite redefinition |
| Primary endpoint time and window | Protocol pp 54,59,69,79: 3 months after randomization ±14 days; p 86 also says after treatment onset | SAP p 3 and main p 3 use Visit 3/randomization ±14 days; treatment starts next day. The isolated anchor wording is listed once among exclusions |
| Primary versus change score | Protocol p 69 and SAP pp 5,10 final score adjusted for baseline | Main pp 3–4 final score; results p 14 separately labels change analysis and gives identical adjusted estimate, consistent with SAP p 10 footnote |
| Treatment contrast | Protocol pp 56,68; SAP pp 2,6–9 levodopa plus standardized rehabilitation versus placebo plus same rehabilitation | Main pp 2–3 agrees; randomized assignment retained in all reported estimands |
| Primary model family | Protocol p 86 mixed effects; SAP p 10 linear model | Main p 4 linear regression; F-XS-101 |
| Primary treatment term | Protocol p 86; SAP p 10 two-level randomized treatment fixed effect | Main p 4 agrees treatment term |
| Baseline adjustment | Protocol p 86; SAP p 10 baseline FMMA covariate | Main p 4 agrees baseline FMA total |
| Stroke-type adjustment | Protocol p 86 ischemic/hemorrhagic fixed effect; SAP p 10 does not include this term | Main p 4 does not include it; F-XS-101 |
| Center adjustment | Protocol p 86 center random intercept; SAP p 10 does not include center | Main p 4 does not include it; F-XS-101 |
| Primary confidence and significance | Protocol p 86 two-sided 5%; SAP p 10 two-sided .05 and 95%CI | Main pp 4,6 agrees; no noninferiority/equivalence margin |
| Primary population | Protocol p 86 all randomized FAS/ITT; SAP p 4 all randomized FAS with deaths contributing only death-inclusive estimands | Main pp 4–5 excludes 28 deaths and analyzes 582; F-XS-102 addresses the protocol-to-SAP/report change, rather than FAS terminology |
| Assignment after intercurrent events | Protocol p 86 and SAP pp 6–9 retain randomized treatment | Main p 4 and results p 13 agree randomized assignment |
| Primary survivor missingness | Protocol p 87 MICE generally; SAP pp 4,11 impute missing survivor FMA,100 datasets/Rubin pooling | Main p 4 and results p 7 agree MICE,100 and Rubin pooling |
| Primary missingness unit | SAP p 11 does not prescribe item versus aggregate level | Results p 7 gives item-level FMA imputation; additional detail, no conflicting plan statement |
| Complete-case membership | Protocol p 86 no missing baseline or 3-month FMMA; SAP p 4 complete Visit 3 FMA | Results pp 12–13 complete Visit 3 FMA,n 551. No printed baseline-missing count or conflicting membership is supplied; no additional finding inferred |
| Death-imputed sensitivity | SAP pp 4,7 primary exclusions/death-imputed policy III | Main p 4 and results p 13 estimand 3,n 610,agree specific death-imputation strategy |
| Composite sensitivity: first component | SAP pp 8,11 death before Visit 3 and survival ordering | Results p 13 death/FMA composite,n 610; same death component |
| Composite sensitivity: second component | SAP pp 8,11 surviving patients ordered by Visit 3FMA | Results p 13 uses Visit 3FMA; no changed component is identified |
| Composite win comparison | SAP p 11 all cross-arm pairs; survival beats death; later death beats earlier death; higher survivor FMA wins; treatment wins/placebo wins;1000 bootstrap CIs per imputation | Results p 13 reports win ratio 1.06[0.86,1.26]. No conflicting pair algorithm is stated. Report-side odds-ratio label belongs to parent REPORT–REPORT lane |
| Motor-impairing SAE exclusion | SAP pp 6,8 recurrent stroke/fracture/comparable before Visit 3 | Results pp 13,24 estimand 5 excludes same events,n 545 |
| Medication-only exclusion | SAP pp 6,8–9 excludes< 80%drug | Results p 13 estimand 6 uses same threshold,n 496 |
| Rehabilitation-only exclusion | SAP pp 6,9 at least 1 week< 5 sessions/week over 4 weeks | Results p 13 estimand 7 repeats full rule,n 450 |
| Window exclusion | SAP pp 6,9 excludes Visit 3 out of window | Results p 13 estimand 8 uses same exclusion,n 524; window fixed by schedule |
| Protocol PP: medication criterion | Protocol p 86 ≥ 80%prescribed drug OR justified reduced 1–1–0 dose | Main p 4 labels strict≥ 80%combined-adherence analysis post hoc; exact protocol PP result not identified; F-XS-103 |
| Protocol PP: rehabilitation criterion | Protocol p 86 requires≥ 5 sessions/week in addition to medication criterion | Main p 4 combined-adherence analysis has same nominal session threshold but strict drug criterion; F-XS-103. REPORT conjunction wording belongs to parent |
| Protocol PP: assignment and analysis | Protocol p 86 randomized assignment; repeat primary on PP | Main p 4/results p 14 only combined-adherence post hoc result 0.32[−3.25,3.89],n 395; not explicitly the protocol PP set; F-XS-103 |
| Center sensitivity | Protocol p 86 graphical treatment heterogeneity; SAP p 11 adds center and treatment×center to main model and graph | Main p 5/eFigure 5 results p 25 provides grouped-center plot labeled post hoc; no center-interaction model result; F-XS-103 |
| Stroke-type sensitivity | Protocol p 86 treatment×index-event-type interaction | No matching effect-modification result in supplied report; F-XS-103 |
| Adjusted sensitivity: age | Protocol p 86 includes age | No corresponding multivariable sensitivity result; F-XS-103 |
| Adjusted sensitivity: sex | Protocol p 86 includes sex | Same consolidated absent sensitivity; F-XS-103 |
| Adjusted sensitivity: dementia | Protocol p 86 includes dementia | Same consolidated absent sensitivity; F-XS-103 |
| Adjusted sensitivity: selective hand/wrist movement | Protocol p 86 includes baseline selective movement | Same consolidated absent sensitivity; F-XS-103 |
| Adjusted sensitivity: cortical dysfunction | Protocol p 86 aphasia/neglect/hemianopia | Same consolidated absent sensitivity; F-XS-103 |
| Adjusted sensitivity: fatigue | Protocol p 86 self-reported fatigue | Same consolidated absent sensitivity; F-XS-103 |
| Adjusted sensitivity: SSRI | Protocol p 86 SSRI treatment | Same consolidated absent sensitivity; F-XS-103 |
| Adjusted sensitivity: extrapyramidal symptoms | Protocol p 86 physician-rated mild symptoms | Same consolidated absent sensitivity; F-XS-103 |
| Adjusted sensitivity: reduced impetus | Protocol p 86 physician-rated reduced impetus | Same consolidated absent sensitivity; F-XS-103 |
| SAP subgroup: age | SAP pp 12,15 <median versus≥median; younger greater benefit hypothesized | No age-interaction result or planned forest plot in supplied report; F-XS-103 |
| SAP subgroup: sex | SAP pp 12,15 male/female; no modification expected | No matching result; F-XS-103 |
| SAP subgroup: distal motor | SAP pp 12,15 distal NIHSS0/> 0; no modification expected | Distal item definition supplied results p 9, but no matching interaction result; F-XS-103 |
| SAP subgroup: cortical dysfunction | SAP pp 12,15 Best Language+Extinction/Inattention+Visual 0/> 0; no modification expected | No matching result; F-XS-103 |
| SAP subgroup: baseline SSRI | SAP pp 12,15 yes/no; no modification expected | No matching result; F-XS-103 |
| SAP subgroup: stroke type | SAP pp 12,15 ischemic/intracerebral hemorrhage; no modification expected | No matching result; F-XS-103 |
| SAP subgroup: baseline FMMA severity | SAP pp 12,15 <median/≥median; no modification expected | Main p 5 post hoc≤ 35/> 35 and results p 27 do not implement median cutoffs; F-XS-103 |
| Nonlinearity sensitivity | SAP p 10 permits transformations for model assumptions; no spline/interaction analysis specified | Main pp 5,7 and results p 18 label spline/baseline-treatment analyses post hoc; status coherent |
| Secondary FMMA total times | Protocol p 54; SAP p 5 additional 5 weeks,6 months,12 months | Main p 3 reports 5 weeks and explicitly defers other times; none designated key secondary or abstract result; omission screened as peripheral, once below |
| Secondary FMMA upper and lower | Protocol p 54; SAP p 5 separate subscales at Visits 2–5 | Main pp 3,6/results p 15 report separate 3-month values; other times explicitly outside current report |
| Secondary additional side | SAP pp 5,10 says affected side | Main pp 3,6/results pp 7,15 explicitly identifies unaffected side and discloses wording replacement; excluded once below |
| Secondary NIHSS | Protocol pp 54,70; SAP p 5 | Main pp 3,6/results p 15 same 3-month impairment scale |
| Secondary mRS | Protocol pp 54,70; SAP p 5 | Main pp 3,5,6/results p 15 ordinal analysis, same disability scale; missingness departure F-XS-104 |
| Secondary PROMIS-29 | Protocol p 70 seven domains and pain-intensity item; SAP p 5 names 29 | Main p 3 seven domains/raw ranges; results p 15 aggregate score. No plan statement prescribes a contrasting aggregation; report-side aggregate definition belongs to parent/statistical lanes |
| Secondary PROMIS-10 | Protocol p 70 general-health measure; SAP p 5 names 10 | Main p 3 and results p 15 same named instrument; no contrasting plan aggregation prescribed |
| Secondary patient relevance | Protocol p 70 improvement since previous visit and personal relevance; SAP p 5 PRAI | Main p 3/results p 8 same two-item concept; missingness departure F-XS-104 |
| Secondary RMI continuous | Protocol pp 70–71 0–15; SAP p 6 continuous | Main pp 3,6/results p 15 continuous RMI result; agrees scale |
| Secondary RMI binary | Protocol pp 70,85 RMI≥ 7 independent walking; SAP p 6 explicitly binary analysis | Supplied report provides continuous result only. No key-secondary/abstract designation; peripheral ordinary-secondary omission recorded below |
| Optional selected-center ARAT | Protocol pp 54,71 at 5 weeks/3/6/12 months | Main p 3 explicitly defers other subset motor assessments; no key-secondary designation |
| Optional Box-and-Block | Protocol pp 54,71 same selected-center times;60seconds | Same explicit deferral |
| Optional Jamar | Protocol pp 54,71 affected/unaffected grip | Same explicit deferral |
| Optional Motricity Index | Protocol pp 54,71 upper/lower 0–100 | Same explicit deferral |
| Optional Trunk Control | Protocol pp 54,71 four 0–25items | Same explicit deferral |
| Optional FAC | Protocol pp 54,71 score 0–5 | Same explicit deferral |
| Optional 10-meter walk | Protocol pp 54,71 comfortable/maxspeed,cadence | Same explicit deferral |
| Optional Mo CA | Protocol pp 54,71 score 0–30 | Same subset/other-time deferral; no key-secondary designation |
| Optional sensors | Protocol pp 54,71–72 dailyactivity/armuse | Same subset/other-time deferral |
| Safety outcome status, checked separately | Protocol p 54 includes mortality, recurrent stroke and serious adverse events among secondary outcomes; pp 69,71 explicitly also label them safety objectives/outcomes. SAP pp 5–6 places potential harm under secondary outcomes | Main p 3 calls these measures of harm, and Table 2/results pp 16–17 retain safety classifications. Secondary and safety status coexist in the supplied plan; no tertiary outcome status or categorical reclassification is established |
| Safety endpoint mortality | Protocol p 71; SAP p 6 death all cause through 12 months | Main p 3 defines all cause death; current report gives 28 deaths at 3 months; longer follow-up is explicitly outside the current report |
| Safety endpoint recurrent stroke | Protocol p 71; SAP p 6 anystroke through 12 months | Main p 3 anystroke; current serious-event stroke counts; no altered component |
| Safety endpoint SAE | Protocol pp 71,81–83 SAE through 3 months | Main p 3 and Table 2/results p 16 serious events; same interval |
| Safety selected nonserious events | Protocol p 81; report results p 19 list nausea; vomiting; taste disturbance; drymouth; anorexia; arrhythmias; posturalhypotension; syncope; drowsiness/suddensleep; fatigue; dementia; psychoses; hallucinations; confusion; euphoria; abnormaldreams; insomnia; depression; anxiety; dizziness; dystonia; dyskinesia; chorea | List checked item by item: all 23 entries present in eTable 9. Table 2 prints observed categories rather than asserting every possible category has events |
| Safety monitoring composite | Protocol p 85 death/recurrentstroke/SAE composite for DSMC alerts; threshold in unsupplied charter | Report p 2 safety reviews; no conflicting threshold or final efficacy-composite designation; not a changed efficacy outcome |
| Further biomarker outcomes | Protocol p 72; SAP pp 16–17 Nf L,Tau,hs-troponin T,NT-pro-BNP,GDF15,secretorypanel IL1b/IL6/IL10/MCP1/TNFa/MMP1/osteopontin; rs 1842681,Apo E; othergenetics exploratory | No matching reported result; these are further/exploratory analyses, not missing primary/key secondary results |
| Further registry/rehabilitation/fatigue analyses | Protocol p 69; SAP p 18 registry comparison,rehabilitationdose/type×levodopa,fatigue/depression | No matching reported result; further analyses remain distinct from primary endpoint analysis; no prespecification claim for absent results |
| Secondary model families | Protocol p 87 and SAP p 10 binarylogit/binomial;continuouslinear;ordinalordinal-logistic;baseline adjustment | Main p 5 agrees baseline regressions and ordinalmRS. No binary RMI regression reported, as recorded separately |
| Secondary missingness | SAP p 11 imputes secondary outcomes except harms | Main p 5/results p 7 mRS/PRAI not imputed; F-XS-104 |
| Secondary hierarchy/multiplicity | Protocol labels secondary; SAP p 11 sensitivityresults contextual,no multiplicityadjustment | Main p 3 retains secondary label and calls findings exploratory because multiplecomparisons. This inferential caution is not a categorical outcome-status change; excluded once below |
| Sample size inputs | Protocol pp 56,84–85 SD25,difference 6,power 80%,two-sided 5%,548evaluable,610target,10%dropout; planned ttestwithoutbaselinegain | Main p 3 reproduces all inputs,548/610/549. Numerical power reconstruction belongs to statistical lane; no cross-source input mismatch |
| Walking power | Protocol p 85 45%versus 57%,absolute 12%,relative 27%,80%power,5%,5 weeks | Not repeated as observed result; no report-side contradictory power assumption |
| PROMIS power | Protocol p 85 states 80%power without numeric inputs | No conflicting reported input; missing details alone are not findings |
| Margin/hypothesis/success rule | Protocol pp 72,84 superior direction,6 point planningdifference; SAP p 10 nulltestedtwo-sided.05 | Main pp 3,4,6 same planningdifference and conventional superioritytest;6 points not described as noninferioritymargin or nullboundary |
| Interim rule | Protocol p 87 no interim analysis; DSMC pp 62,85 safety only/no efficacy review | Main p 2 safety reviews 200/400/500; these are not efficacy interimanalyses; scope reconciles |
| Stopping rule | Protocol pp 64,85 no efficacystopping;possible DSMCsafetystop;charterthresholdnot supplied | No reported efficacy stop or conflicting numeric threshold; no inferred boundary |
| Allocation | Protocol p 74; SAP p 3 1:1centerstratified,minimization 80% | Main p 3 agrees 1:1,centerstratum,minimization 80% |
| Intervention dose and duration | Protocol pp 56,73,76; SAP pp 2–3 100/25mg,39 days,day s 1–3once;4–6twice;7–34thrice;35–37twice;38–39once | Main pp 2–3 repeats strength,39 days and all 5phases exactly; no dose/duration change |
| Rehabilitation cointervention | Protocol p 77 standard motor learning,3 sessions/workday,at least 2motor | Main p 3 same standardized active task-oriented care and expectation≥ 3 sessions/day. Adherence≥ 5/week is a separate analysis criterion, not conflicting treatment dose |
| Plan versions | Protocol 1.1 ischemiconly,motorarm+leg;1.4 includeshemorrhage/ataxia/distalparesis | SAP pp 4–5 and report follow 1.4. Explicit version evolution resolves historical population change; final eligibility checked below |

## Eligibility criteria, item by item

Comparators: PLAN final protocol [p 55](../../../joi250066supp1_prod_1761597796.4601.pdf#page=55), [p 68](../../../joi250066supp1_prod_1761597796.4601.pdf#page=68), [p 74](../../../joi250066supp1_prod_1761597796.4601.pdf#page=74); PLAN SAP [p 4](../../../joi250066supp2_prod_1761597796.4701.pdf#page=4) and [p 5](../../../joi250066supp2_prod_1761597796.4701.pdf#page=5); REPORT main [p 2](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=2) and full reported eFigure 1 [results p 20](../../../joi250066supp3_prod_1761597796.4701.pdf#page=20). Main p 2 is abbreviated and points to the full list. Each row below reconciles the complete current lists; these are not exclusions.

| Criterion | Item-level comparison |
|---|---|
| Acute stroke type | Ischemic or intracerebral hemorrhagic; subarachnoid hemorrhage/cerebral venous sinus thrombosis excluded. Report full list matches current protocol/SAP |
| Onset window | ≤ 7 days before randomization in all lists |
| Hemiparesis threshold | Total≥ 3 NIHSSpoints across motorarm,motorleg,limbataxia in all current lists |
| Distal paresis equivalence | Distalarm paresis equivalent to one listeditem in all current lists |
| Reperfusion latency | ≥ 24 hours afterthrombolysis/thrombectomy in all lists |
| Rehabilitation need | Inpatient rehabilitation required in all lists |
| Rehabilitation participation | Capable of standardized rehabilitation in all lists |
| Consent | Patient or next of kin consent in all lists |
| Age exclusion | < 18 years in all lists |
| Parkinson disease | Excluded in all lists |
| Mandatory levodopa | Excluded in all lists |
| Procedure/drug adherence | Inability/unwillingness excluded;oral/NG/PEG route permitted in all lists |
| Severe aphasia | Unable to followtwo-stage commands excluded in all lists |
| Prestroke disability | Basal ADLdependence,mRS> 3 excluded in all lists |
| Pre-existing hemiparesis | Excluded in all lists |
| Hypersensitivity/contraindication | Levodopa/carbidopa hypersensitivity/othercontraindications excluded in all lists |
| Pregnancy/lactation/planned pregnancy | Excluded in all lists;pregnancytest forchildbearingwomen |
| Reliable contraception | Lack of medicallyreliablemethod excluded in all lists |
| Childbearing-potential exceptions | Surgicalsterilization/hysterectomy or postmenopause> 2 years exempt in all lists |

## Findings

### F-XS-101 — Primary model changes from the final protocol to the SAP and report

- **Exact compared locations and roles:** PLAN [final protocol p 86, section 11.4.2 primary model](../../../joi250066supp1_prod_1761597796.4601.pdf#page=86), also PLAN [p 56 synopsis](../../../joi250066supp1_prod_1761597796.4601.pdf#page=56); PLAN [SAP p 10, section 5.2](../../../joi250066supp2_prod_1761597796.4701.pdf#page=10); REPORT [main p 4, Statistical Analyses](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4) and [p 5, SAP/protocol alignment explanation](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5).
- **Printed statements:** The final protocol specifies a mixed-effects primary model with baseline FMMA, treatment, and acute ischemic/hemorrhagic event type as fixed effects and a random intercept for each center. SAP p 10 instead specifies a linear model with baseline FMMA and treatment. Main p 4 reports this latter linear regression specification. Main p 5 describes protocol/SAP differences as statistical terminology related to emerging estimands.
- **Comparison logic and reproduced calculation:** Match primary 3-month FMMA, levodopa–placebo contrast, baseline adjustment and randomized assignment. The random center intercept and stroke-type fixed effect are present in the final protocol and absent from the explicit SAP/report primary model. Changing model terms is an analysis-specification change independently of the use of estimand names. This is categorical model comparison; display-rounding intervals and relative numerical discrepancy are not applicable.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Relationship type:** P_R. **All relationships:** P_R, P_P. The protocol/SAP model disagreement is itself plan-internal; the report implements the SAP side and differs from the final protocol.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Primary adjusted 3-month FMA mean difference−0.90 points,95%CI−3.78 to 1.98,P=.54, and the model specification accompanying its extraction.
- **Why context does not resolve it:** The report identifies the fitted linear model, but the explanation about terminology does not identify a substantive removal of center and stroke-type terms or explain how the final protocol model was superseded. These are distinct fitted analyses, not alternative names for the same quantity.
- **Supported alternatives:** The later SAP may intentionally replace the protocol specification; alternatively a protocol-specified model may have been fitted but not described or reported. The supplied primary-model statements support the first implementation, without supplying a model-change rationale or a matching protocol-model sensitivity result.
- **Missing definition or disclosure:** The operative amendment and reason/date for removing center and stroke-type terms, and whether a protocol-model estimate exists.
- **Classification ambiguity:** A prospective SAP revision may authorize the changed model; this does not erase the supplied protocol-versus-report comparison or imply any conduct judgment.
- **Exact human question:** Was the protocol's primary mixed-effects model with a center random intercept and stroke-type adjustment prospectively replaced by the baseline-and-treatment linear model, and where are that change and any result from the protocol-specified model documented?

### F-XS-102 — The primary analysis excludes deaths after the protocol specifies all randomized patients

- **Exact compared locations and roles:** PLAN [final protocol p 86, sections 11.4.1–11.4.2](../../../joi250066supp1_prod_1761597796.4601.pdf#page=86); PLAN [SAP p 4, section 3.2 and footnote 1](../../../joi250066supp2_prod_1761597796.4701.pdf#page=4), [p 6, primary estimand status](../../../joi250066supp2_prod_1761597796.4701.pdf#page=6), and [p 7, primary policy versus death-imputed policy III](../../../joi250066supp2_prod_1761597796.4701.pdf#page=7); REPORT [main p 4, primary population](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4), [p 5, flow and terminology explanation](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5), and [results pp 12–13, primary estimand population](../../../joi250066supp3_prod_1761597796.4701.pdf#page=12).
- **Printed statements:** The protocol FAS consists of all randomized patients, analyzed as randomized; primary analysis is on that FAS. SAP p 4 preserves the FAS name but explicitly states that deceased patients contribute only to policy III and the composite. The primary policy is distinguished from these supplementary analyses on pp 6–7. The report explicitly excludes deaths before 3 months from the primary analysis:28 deaths leave 582 of 610 randomized participants; policy III and composite separately analyze 610.
- **Comparison logic and reproduced calculation:** Membership is compared item by item: randomized status retained; treatment assignment retained; missing survivor FMA imputed; deceased patients included in the protocol's all-randomized population but explicitly excluded from the reported primary analysis and relegated to supplementary estimands in SAP. 610−28=582 confirms the implemented exclusion. The finding is the categorical population/death-handling change, not a discrepancy between rounded copies of a count; display-precision relative discrepancy is not the criterion applied.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Relationship type:** P_R. **All relationships:** P_R, P_P.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** The target population of the primary−0.90 point adjusted effect and its sample size 582; the separate death-inclusive policy III effect−0.98,n 610,is supplementary.
- **Why context does not resolve it:** The SAP/report make the implemented survivor population clear, but this is a substantive narrowing of the protocol's primary all-randomized analysis, rather than only a change in FAS terminology. No explicit protocol death-exclusion rule or amendment is supplied at the primary-analysis specification.
- **Supported alternatives:** The SAP may be the operative prospective clarification of an endpoint undefined after death; the protocol may have intended survivor-only scoring despite its unqualified all-randomized specification. The death-inclusive sensitivity results are available, but their availability does not make them the reported primary analysis.
- **Missing definition or disclosure:** Whether and when survivor-only primary inference replaced or clarified the protocol's all-randomized primary population.
- **Classification ambiguity:** This concerns substantive membership, not the immediately resolvable use of the FAS name in death-inclusive rows. The later SAP supplies an explicit operational rule and may constitute a prospective amendment.
- **Exact human question:** Was exclusion of patients who died before 3 months from the primary analysis a prospective change or clarification of the protocol's all-randomized primary analysis, and which document records that decision and its timing?

### F-XS-103 — Planned primary-endpoint sensitivity and subgroup analyses are not identified among the reported analyses

- **Exact compared locations and roles:** PLAN [protocol p 86, sections 11.4.1 and 11.4.3](../../../joi250066supp1_prod_1761597796.4601.pdf#page=86); PLAN [SAP p 11, section 7](../../../joi250066supp2_prod_1761597796.4701.pdf#page=11), [p 12, section 7.2](../../../joi250066supp2_prod_1761597796.4701.pdf#page=12), and [p 15, prespecified hypotheses and cutoffs](../../../joi250066supp2_prod_1761597796.4701.pdf#page=15); REPORT [main p 4, post hoc combined adherence analysis](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4), [p 5, post hoc severity/center analyses and prespecified-analysis statement](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5), [p 6, primary/sensitivity result summary](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), and [results p 13, estimands 1–8](../../../joi250066supp3_prod_1761597796.4701.pdf#page=13), [p 14, post hoc estimands](../../../joi250066supp3_prod_1761597796.4701.pdf#page=14), [p 18, regression sensitivity tables](../../../joi250066supp3_prod_1761597796.4701.pdf#page=18), [p 25, center plot](../../../joi250066supp3_prod_1761597796.4701.pdf#page=25), [p 27, post hoc severity plot](../../../joi250066supp3_prod_1761597796.4701.pdf#page=27).
- **Printed statements:** SAP p 12 says the primary estimand will be analyzed with subgroup and treatment×subgroup terms and presented in a forest plot for seven variables: age<median/≥median; male/female; distal motor 0/> 0; cortical NIHSS sum 0/> 0; baseline SSRI yes/no; ischemic/hemorrhagic stroke; baseline FMMA severity, specified as<median/≥median on p 15. SAP p 11 additionally specifies center and treatment×center terms. Protocol p 86 plans a covariate sensitivity including age,sex,dementia,selective hand/wrist movement,cortical dysfunction,fatigue,SSRI,extrapyramidal symptoms,reduced impetus; a stroke-type interaction; and a PP repeat using≥ 80%drug OR justified reduced dose, plus≥ 5rehabilitation sessions/week.
- **Comparison logic and reproduced calculation:** Every supplied report display and narrative was matched to those specifications. The report supplies the eight estimands, complete-case/death-imputed/composite/single-event exclusions, post hoc combined adherence, baseline spline/interaction, grouped-center descriptive plot, and post hoc FMA≤ 35/> 35 severity groups. None is the seven-variable planned interaction forest plot, center-interaction model, or additional-covariate primary sensitivity. The post hoc severity cutoff is not the prespecified median cutoff. The strict combined-adherence criterion does not explicitly retain the protocol's justified-dose-reduction allowance and is labeled post hoc rather than identified as the planned PP repeat. No subgroup-interaction estimate, interval or P value for the other six planned variables appears. This is a logical specification/result inventory comparison; rounding intervals and relative numerical discrepancy are not applicable.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Planned robustness and effect-modification analyses of the primary 3-month FMA effect; the report's description that prespecified analyses were performed and the interpretation of the post hoc severity/adherence/center analyses.
- **Why context does not resolve it:** This is category 5: planned analyses of the primary endpoint are not identified in the report. The explicit deferral of other secondary measures/timepoints does not identify these primary-endpoint analyses as deferred. A different post hoc cutoff or strict adherence rule is not automatically the planned analysis.
- **Supported alternatives:** These analyses may have been performed but omitted or reserved for separate reporting; the SAP may have superseded some protocol sensitivities; the post hoc PP-like and center figures may be intended to implement parts of the plan. The exact differences in cutoff, dose-reduction allowance and fitted interaction terms prevent assuming equivalence.
- **Missing definition or disclosure:** Location/status of every planned primary sensitivity and subgroup result, plus any amendment or explanation for replacement/nonreporting. An absent result is established only within the complete supplied report package, not beyond it.
- **Classification ambiguity:** The consolidated pattern concerns nonreported or differently labeled planned primary-endpoint analyses, not deferred ordinary secondary outcomes. A later approved analysis amendment or separate supplied result could refine the comparison.
- **Exact human question:** Where are the prespecified primary-FMA subgroup interactions, center-interaction model, additional-covariate sensitivity and protocol-defined PP repeat reported, and which were replaced or deferred, particularly the median-based severity subgroup, justified-dose-reduction PP allowance, and planned center analysis now described as post hoc?

### F-XS-104 — Reported secondary missing-data handling departs from the SAP imputation rule

- **Exact compared locations and roles:** PLAN [SAP p 11, section 6](../../../joi250066supp2_prod_1761597796.4701.pdf#page=11), together with [p 5, mRS and patient-relevance secondary outcomes](../../../joi250066supp2_prod_1761597796.4701.pdf#page=5); REPORT [main p 5, secondary methods](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5), [main p 6, secondary results](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), [results p 7, deviations](../../../joi250066supp3_prod_1761597796.4701.pdf#page=7), and [results p 15, eTable 4](../../../joi250066supp3_prod_1761597796.4701.pdf#page=15).
- **Printed statements:** SAP p 11 states that missing secondary outcomes will be imputed as for the primary analysis, except potential-harm outcomes. Main p 5 states that missing mRS and patient-relevance data were not imputed. Results p 7 expressly discloses that deceased participants were assigned mRS6 rather than imputed and missing PRAI was not imputed. eTable 4 uses 596 participants for mRS and 546 for PRAI, compared with 582 for most imputed secondary outcomes.
- **Comparison logic and reproduced calculation:** mRS and PRAI appear explicitly in the SAP's secondary list and are not harms. The SAP's universal secondary-imputation statement therefore covers them; the report's stated exceptions are substantive departures. The comparison is not an attempt to reconstruct model denominators from imputation. Display-rounding intervals and relative discrepancy are not applicable to the categorical missing-data handling.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Three-month mRS odds ratio 0.93[0.69,1.23],n 596,and patient-relevance outcome based on 546 respondents, rather than a secondary analysis following the SAP's general imputation rule.
- **Why context does not resolve it:** Disclosure establishes the methods actually used but does not reconcile them with the planned rule or give the timing/rationale for the secondary exceptions. The choice determines which patients and outcomes contribute to these extracted secondary results.
- **Supported alternatives:** Assigning mRS6 to death follows the stated scale and may intentionally replace imputation; PRAI may intentionally use observed responses. Both are expressly disclosed, so the issue is the planned-versus-reported analysis change and its provenance, not ambiguity about what the report says was done.
- **Missing definition or disclosure:** Rationale/timing of the mRS/PRAI exceptions and whether an updated SAP or amendment specifies them. Main p 5's nonimputation of remaining missingmRS is broader than supplement p 7's explicit death exception.
- **Classification ambiguity:** These are disclosed departures; no inference of an undisclosed action is made.
- **Exact human question:** When and why were mRS and PRAI excluded from the SAP's general secondary-outcome imputation rule, does the mRS exception cover all missingmRS or only deaths, and where is the operative revised specification documented?

## Excluded observations

Only apparent issues not emitted are listed here. Reconciling checks in the matrices are not exclusions. Each row has one reason code.

| Location | Observation | Reason code |
|---|---|---|
| PLAN protocol pp 20,65,86 versus PLAN synopsis/assessment schedule and REPORT main p 3 | Primary-time references vary between poststroke, treatment onset and randomization, but the detailed repeated Visit 3 window is 3 months±14 days after randomization and treatment begins next day. The clinical timing is immediately identifiable; no different reported observation is established. | TERMINOLOGY_OR_WORDING |
| PLAN protocol p 86 final sensitivity paragraph | The last sentence refers to analyses(c,d) rather than the complete-case/PP lettering indicated by the immediately preceding explicit definitions. This isolated pointer does not change the explicitly defined analysis sets or a result. | PERIPHERAL_COMPARISON |
| PLAN SAP pp 5,10 versus REPORT results p 7 and main pp 3,6 | Additional secondary-side wording changes affected to unaffected, expressly explained in the report; affected-side total is already the primary endpoint and the additional side result is explicitly labeled throughout the report. The intended clinical reading is resolved immediately. | TERMINOLOGY_OR_WORDING |
| PLAN protocol/SAP secondary hierarchy versus REPORT main p 3 | Report calls secondary findings exploratory in view of multiple comparisons while retaining the secondary-outcome heading and definitions. This is inferential caution, not a changed categorical outcome status. | TERMINOLOGY_OR_WORDING |
| PLAN protocol pp 54,69–72 and SAP p 5 versus REPORT main p 3 | Ordinary secondary 5 week/subscale and 6/12 month or selected-center motor/cognitive/sensor outcomes are not all presented; the report expressly defers other times/subset assessments, and none is designated key secondary or reported in the abstract. | PERIPHERAL_COMPARISON |
| PLAN SAP p 6 binary RMI≥ 7 versus REPORT main pp 3,6/results p 15 continuous RMI | The binary independent walking representation is planned but not supplied as a result; it is an ordinary secondary endpoint without a key secondary/abstract designation. Its absence does not replace the primary or a key secondary result. | PERIPHERAL_COMPARISON |
| PLAN protocol pp 85,87/SAP p 9 versus REPORT main p 2 | No planned efficacy interim analysis contrasts with safety reviews after 200/400/500 participants; the DSMC's explicit safety only remit distinguishes the procedures. | TERMINOLOGY_OR_WORDING |

## Completion and limitations

All assigned planned statistical-design elements and criterion lists were compared. All 112 PLAN pages are covered through the current fresh maps; every emitted source statement was additionally inspected in a fresh exact-PDF rendering. There is no scientific coverage gap in this shard. Some planned analyses have no supplied result; that is the reproduced scope of F-XS-103, not an assumption about work outside this package. The DSMC charter and numeric safety-alert thresholds are not supplied, so no unpublished boundary was reconstructed. No raw data permit reconstructing subgroup/PP memberships or refitting models; no such raw-data audit was attempted. Historical rendering provenance is unrecorded for mapper assets, but exact fresh renderings independently confirm every emitted observation.
