# Statistical pass 1 — support shard

Runtime agent: `/root/stat1_support`; fresh named statistical reviewer, `gpt-6.1-sol`, reasoning effort `high`. The coordinator records the exact canonical runtime task name returned at spawn using the manifest transport namespace. This artifact is owned only by this support pass-1 agent. Canonical merge must rebase its four-level source links by one level when placing the content directly in `checkers/statistical_pass_1.md`.

Exact assigned scope: S501, S502, S503, S504, S505, S506, S507, S508, S509, S510, S511, S512, S513, S514, S515, S516, S517, S518, S519, S520, S521, S522, S523, S524, S525, S526, S527, S528, S529, S530, S531, S532, S533, S534, S535, S536, S537, S538, S539, S540, S541, S542, S543, S544, S545, S546, S547, S548, S549, S550, S551, S552, S553, S554, S555, S556, S557, S558, S559, S560, S561, S562, S563, S564, S565, S566, S567, S568, S569, S570, S571. This is 71 relationships, disjoint from the main pass-1 shard S001–S092. Supporting count cells in eTables 1–4 and 7 and all eFigure panels were reviewed as implications of these relationships.

Read completely: `QUALITY_CONTROL_SCOPE.md` and `workflow_1_6_2/review_contract.md`. Inputs were the new canonical relationship inventory, current support plan/results evidence maps, main source matching context, tooling record, source inventory, direct-source PDF text and current page images. No earlier candidate, checker, screening, disposition, quality-control report, or external source was used.

## Source authority and calculation boundaries

Roles by content: protocol `joi170166supp1_prod.pdf` and SAP `joi170166supp2_prod.pdf` are PLAN; supplement `joi170166supp3_prod.pdf` pp. 2–16 is PLAN toolkit content, p. 1 and pp. 17–27 are REPORT; the main article is REPORT. Current source-derived images were opened for all results pages 17–24 and 26–27, relevant main methods and SAP subgroup pages, and newly rendered SAP p. 5/protocol p. 9. Native/layout text locates exact source text; cited findings use the exact displayed source values.

Supplemental eTables 1, 2, 5, 6 and 7 state 95% confidence intervals but print no P values, test statistics, standard errors, degrees of freedom, covariance matrices, or variance-estimator definitions. Null values are 0 for differences and residuals and 1 for odds ratios. Point containment, endpoint order and stated direction were checked without inferring model coefficients or sidedness. No noninferiority or equivalence claim/margin is stated. The primary superiority rule is the stated final two-sided .048 level after one interim analysis, not an invented multiplicity rule for all secondary displays. The article's primary nonsignificant result is compatible with this rule.

Fresh auxiliary derivatives use direct Poppler `pdftotext -layout` and `pdftoppm -singlefile -scale-to 1700 -png`, on CPU. Paths: `preprocessing/st1-support/supp3-layout.txt`, `preprocessing/st1-support/main3.txt`, `preprocessing/st1-support/sap5.png`, `preprocessing/st1-support/protocol9.png`. Sources and reused assets were preserved.

## Findings

### F-ST1-501 — LDL difference interval does not reproduce under the calculation reproducing other mean/SD rows

- **Relationships:** S541, with comparison rows S529, S537, S538, S539 and S545.
- **Locations and roles:** REPORT [Supplement 3, physical p. 17, eTable 1](../../../../joi170166supp3_prod.pdf#page=17), LDL cholesterol row, the two group headers, and the age, weight, systolic pressure, heart-rate and hemoglobin rows of the same display.
- **Printed values:** complete follow-up n=21,079, LDL mean 122.4 (SD 40.8) mg/dL; missing follow-up n=295, LDL mean 131.4 (SD 46.0) mg/dL; difference 9.0 with 95% CI 3.2 to 14.8 mg/dL. The table gives no LDL-specific contributor counts or CI-method definition.
- **Rule and calculation:** a pooled two-sample mean-difference calculation has `s_p²=((n_C−1)s_C²+(n_M−1)s_M²)/(n_C+n_M−2)` and `SE=s_p sqrt(1/n_C+1/n_M)`. With a 1.96 multiplier, the LDL SE is 2.39649 and the calculated CI is approximately 4.3029 to 13.6971. This is a reproducing-method calculation, not an assertion that the authors used that method. It gives the same display's age CI −1.9897 to 0.7897, weight −2.0140 to 0.2140, systolic pressure −2.9270 to 3.7270 and heart rate 0.8279 to 5.1721, reproducing their printed endpoints; hemoglobin also overlaps after allowing its printed means and SDs their rounding intervals. A pooled t multiplier using the group counts differs negligibly at these sample sizes and leaves the discrepancy unchanged.
- **Display precision:** allow ±0.05 around each mean/SD and, conservatively, ±0.5 around each group n. LDL's recomputed lower endpoint spans 4.19321–4.41253 and upper endpoint spans 13.58747–13.80679. The printed limits allow 3.15–3.25 and 14.75–14.85. The lower gap is at least 0.94321/3.2=0.29475, and the upper gap is at least 0.94321/14.8=0.06373; both exceed 0.05. These are endpoint discrepancies, not a comparison of a modeled estimate with a crude ratio.
- **Focus area:** B and C. **Proposed review domain:** `statistical_results`. **Proposed relationship type / all relationships:** `S_W` / `S_W`.
- **Qualifying route:** Route A, category 4.
- **Affected result or extracted value:** the 95% confidence interval for the baseline LDL difference between missing and complete follow-up groups.
- **Why context does not resolve it:** the method reproduces the other mean/SD rows of the same display, but not this row; category 4 requires registration even when the producing method is unspecified. The table supplies no alternative contributor counts or LDL-specific CI construction to resolve the printed interval.
- **Alternatives / missing definitions:** LDL could have fewer observed values than the displayed group totals, or a different interval procedure could have been used for LDL. Either could explain the wider interval, but the corresponding counts and procedure are absent. This is not a request to adopt a preferred procedure.
- **Exact human question:** What complete- and missing-follow-up LDL contributor counts and confidence-interval procedure produced 9.0 mg/dL (95% CI, 3.2–14.8), given that the pooled calculation with the displayed group totals reproduces the other mean/SD rows but yields approximately 4.30–13.70 for LDL?

### F-ST1-502 — Reported in-hospital medication composite omits the planned statin component

- **Relationships:** S512 and S521; affected modeled results S554 and S564.
- **Locations and roles:** PLAN [SAP p. 5, §6.1.2, lines 1149–1151](../../../../joi170166supp2_prod.pdf#page=5); REPORT [main article p. 3, Outcomes](../../../../jama_huffman_2018_oi_170166.pdf#page=3), [p. 7, Table 3 optimal in-hospital medication and footnote c](../../../../jama_huffman_2018_oi_170166.pdf#page=7); REPORT [Supplement 3 p. 21, eTable 5 footnote c](../../../../joi170166supp3_prod.pdf#page=21) and [p. 22, eTable 6 footnote b](../../../../joi170166supp3_prod.pdf#page=22).
- **Printed values / statements:** SAP defines optimal in-hospital use by five components: aspirin, ADP receptor antagonist, heparin, statin and beta blocker. Main Outcomes defines four components, aspirin, ADP antagonist, anticoagulant and beta blocker, and explicitly says in-hospital statin was predefined but data were not collected. Table 3 shows 3122 (31.7%) control versus 3878 (35.8%) intervention, primary OR 1.45 (1.28–1.64), for the four-component definition. eTable 5 likewise omits statin; eTable 6 lists aspirin, ADP antagonist, heparin and beta blocker.
- **Rule and logical calculation:** the planned all-component endpoint requires meeting five drug criteria, while the reported endpoint requires four. Removing statin changes both the composite event condition and eligibility to receive every component. The provided report acknowledges the missing collection but does not supply a result for the planned composite. No arithmetic correction or preferred analysis is proposed; display precision is not applicable to this set-membership difference.
- **Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed relationship type / all relationships:** `P_R` / `P_R`.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** the optimal in-hospital medication event rates and adjusted odds ratios, and whether the extracted endpoint includes statin.
- **Why context does not resolve it:** category 5 expressly includes changes in a prespecified composite definition. Disclosure of noncollection explains why one component is absent but does not make the four-component endpoint the same quantity as the planned five-component endpoint.
- **Alternatives / missing definitions:** a prospective amendment could have changed the composite after the supplied SAP; alternatively, the reported definition is a disclosed adaptation caused by noncollection. No supplied amendment establishes its timing or the corresponding eligibility definition.
- **Exact human question:** Was optimal in-hospital medication use prospectively redefined to omit statin, and what amendment and eligibility rule should accompany extraction of the four-component rates and modeled results rather than the five-component endpoint in the supplied SAP?

### F-ST1-503 — Expanded MACE is a planned secondary objective but reported as post hoc

- **Relationships:** S504 and S567, matching main S091.
- **Locations and roles:** PLAN [protocol p. 9, §2.2.3, lines 259–263](../../../../joi170166supp1_prod.pdf#page=9); PLAN [SAP pp. 2–3, §2.1.2, lines 1071–1074](../../../../joi170166supp2_prod.pdf#page=3); REPORT [main p. 3, Outcomes and Statistical Analysis](../../../../jama_huffman_2018_oi_170166.pdf#page=3), [p. 8, Secondary and Post Hoc Analyses](../../../../jama_huffman_2018_oi_170166.pdf#page=8), [p. 9, continuation/discussion](../../../../jama_huffman_2018_oi_170166.pdf#page=9); REPORT [Supplement 3 p. 23, eTable 7 title and first row](../../../../joi170166supp3_prod.pdf#page=23).
- **Printed values / statements:** protocol and SAP place evaluation of intervention effects on in-hospital and 30-day expanded MACE under secondary objectives. The main report calls expansion by incident in-hospital heart failure, cardiogenic shock and cardiac arrest a post hoc analysis. eTable 7 calls it exploratory and reports 919 (9.1%) control versus 795 (7.0%) intervention; primary-model difference −1.34% (−2.72 to 0.04) and OR 0.84 (0.70–1.00).
- **Rule and logical calculation:** the supplied plan contains a secondary expanded-MACE objective before the reported analysis, whereas the report characterizes the expanded-MACE analysis as post hoc. The plan does not define the expanded components; consequently it does not establish whether the report's specific expansion equals the planned expansion or replaces it. This reproduced status/definition contrast must be registered under category 5. Display precision is inapplicable to prespecification status.
- **Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed relationship type / all relationships:** `P_R` / `P_R`.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** prespecification and outcome status for the expanded-MACE counts, risk difference and odds ratio.
- **Why context does not resolve it:** category 5 covers prespecified outcome-status changes. The report's post hoc label and the plan's secondary objective coexist, but the supplied sources do not define the distinction between their expanded composites.
- **Alternatives / missing definitions:** the broad objective may have anticipated a different expanded endpoint and the report's particular component set may truly have been selected post hoc; alternatively, the same endpoint was already planned. The component definition and dated analysis specification are missing from the supplied plan.
- **Exact human question:** Does eTable 7's MACE-plus-heart-failure/shock/arrest composite implement the secondary expanded-MACE objective in the supplied protocol/SAP, or is it a distinct post hoc composite, and what prospective definition and outcome status should be used in extraction?

### F-ST1-504 — The reported prespecified subgroup set differs from the supplied subgroup plan

- **Relationships:** S513 and S520, matching main Figure 3 relationships.
- **Locations and roles:** PLAN [SAP p. 7, §7.5.2, lines 1243–1254](../../../../joi170166supp2_prod.pdf#page=7) and [p. 5, §6.1.3](../../../../joi170166supp2_prod.pdf#page=5); REPORT [main p. 3, Statistical Analysis](../../../../jama_huffman_2018_oi_170166.pdf#page=3) and [p. 9, Figure 3 and accompanying subgroup narrative](../../../../jama_huffman_2018_oi_170166.pdf#page=9). The supplied protocol and complete SAP were searched/read for an additional hospital-type or revised age subgroup specification; none is supplied.
- **Printed values / statements:** SAP lists a priori primary-endpoint subgroups: hospital size, use of toolkit components, age <65 and >65, sex, and STEMI/NSTEMI. The report describes age, sex, STEMI/NSTEMI, hospital size and hospital type as prespecified. Figure 3 instead divides age into <50, 50–69 and ≥70; adds government/nonprofit/private hospital groups with ORs 0.90 (0.61–1.33), 0.91 (0.59–1.40), and 1.16 (0.82–1.64); and supplies no toolkit-use subgroup result. Main p. 3 states the concurrent process evaluation will be reported separately, but does not identify the planned primary-outcome toolkit-use subgroup as deferred.
- **Rule and logical calculation:** compare the explicitly listed prospective subgroup partitions with the reported set called prespecified: the age partition changes, hospital type is added without a corresponding supplied prespecification, and toolkit-use effect heterogeneity is not reported. These form one subgroup-specification pattern. The <65/>65 equality boundary alone is not the observation. Display precision cannot equate the <65/>65 partition with <50/50–69/≥70.
- **Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed relationship type / all relationships:** `P_R` / `P_R`.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** prespecification of the primary MACE age and hospital-type subgroup results, and availability of the planned primary MACE toolkit-use subgroup analysis.
- **Why context does not resolve it:** category 5 always registers an analysis called prespecified that the supplied plan does not contain and a planned primary analysis not reported. An unspecified separate process-evaluation publication does not establish whether these specific primary-outcome subgroup changes were prospective.
- **Alternatives / missing definitions:** a later dated analysis specification may establish the three age bands and hospital type and defer or replace toolkit use. Alternatively, the reported subgroup descriptions may refer to a different prospective source. That source and its timing are not supplied.
- **Exact human question:** Which dated prospective specification establishes Figure 3's age bands and hospital-type subgroup as prespecified, and where is the SAP's primary-MACE subgroup analysis by use of toolkit components reported or documented as replaced/deferred?

### F-ST1-505 — Residual sign definition reverses hospital-rate direction between the index and caption

- **Relationships:** S568 and S569.
- **Locations and roles:** REPORT [Supplement 3 p. 1, eFigure 1A index entry](../../../../joi170166supp3_prod.pdf#page=1), and REPORT [p. 24, eFigure 1A axis/points and final caption sentence](../../../../joi170166supp3_prod.pdf#page=24).
- **Printed values / statements:** index calls the quantity residual of 30-day MACE rate “Expected – Observed.” Figure p. 24 puts negative residuals on the left and positive residuals on the right; caption says the left-hand side depicts hospitals with MACE below the mean and the right-hand side hospitals above the mean. It describes the residuals as hospital-level departures from the mean (residual=0). The plotted axis includes −3, −2, −1, 0, 1 and 2.
- **Rule and logical calculation:** for the printed index contrast `r=Expected−Observed`, a hospital above the expected/mean rate has r<0, whereas the caption assigns above-mean hospitals to the positive right-hand side. Conversely, below-mean observed rates yield r>0 under the index formula but occupy the negative left-hand side under the caption. This is a direction reversal, not a residual magnitude reconstructed from pixels. Rounding cannot reverse the signs of the clearly nonzero plotted points; no imprecise graph digitization is used.
- **Focus area:** B. **Proposed review domain:** `statistical_results`. **Proposed relationship type / all relationships:** `S_W` / `S_W`.
- **Qualifying route:** Route A, category 2.
- **Affected result or extracted value:** the direction of the hospital departures in the MACE residual display and whether a positive residual represents above- or below-expected MACE.
- **Why context does not resolve it:** category 2 covers direction/reference definitions reversing printed values. The index supplies one subtraction order and the caption supplies the opposite association between residual sign and hospital rates. Choosing the caption as authoritative leaves the printed index definition unresolved.
- **Alternatives / missing definitions:** the graph may depict a hospital random effect or predicted-minus-mean residual rather than the expected-minus-observed quantity in the index. Alternatively, the subtraction order may differ from the caption's interpretation. The exact residual formula/scale is not supplied.
- **Exact human question:** What residual formula and subtraction order generated eFigure 1A, and does a positive residual denote higher or lower hospital MACE than expected, given the index's Expected−Observed label and the caption's opposite sign interpretation?

## Relationship completion records

Every row below records the full assigned relationship as `PASS_1_COMPLETE`, including checks for count, denominator, estimate/test, method and matched-source implications wherever applicable. A finding is referenced without assigning adjudication. “No printed conflict” does not claim unavailable model internals were reproduced.

| S ID | Pass 1 status | Checks and source-grounded outcome |
|---|---|---|
| S501 | PASS_1_COMPLETE | Five-cohort stepped-wedge schedule, random hospital effects and fixed periods match reported design. SAP's four-period sentence is separately excluded; no observed allocation or primary analysis conflict is established. |
| S502 | PASS_1_COMPLETE | Primary 30-day MACE components/GUSTO definition match main primary outcome and supplemental clinical labels; death versus all-cause death is resolved by definitions. |
| S503 | PASS_1_COMPLETE | Listed mortality, reinfarction, stroke, GUSTO bleeding and process secondary outcomes match report displays; in-hospital medication component implication is F-ST1-502. |
| S504 | PASS_1_COMPLETE | Expanded-MACE status comparison is F-ST1-503. Substudy outcomes are not identified as key secondary and omitted substudy results alone do not establish a qualifying primary/key-secondary omission. |
| S505 | PASS_1_COMPLETE | Follow-up definitions read including protocol's Discharge Date+30 Days diagram; report does not supply a conflicting explicit admission-versus-discharge follow-up origin. No origin was inferred from convention. |
| S506 | PASS_1_COMPLETE | Adult STEMI/NSTEMI eligibility, consent and analysis-population definitions reviewed; no contradictory report population rule found. |
| S507 | PASS_1_COMPLETE | Withdrawal/loss definitions compared with 295 missing outcomes; 215 not followed and 80 unreachable sum to 295, without inferring cause distributions absent from the plan. |
| S508 | PASS_1_COMPLETE | SAE definitions and expected clinical event capture distinguish safety from primary composite; no printed contradiction in stated surveillance cadence or reported safety decision. |
| S509 | PASS_1_COMPLETE | One one-year safety/efficacy interim and DSMB stop/continue role match article's 12-month interim. No numerical interim result or stopping recommendation is supplied for reproduction. |
| S510 | PASS_1_COMPLETE | Planned 15,000/15,750, ICC .05, alpha .05, power 80%, baseline 10.4%, difference 2.4 percentage points match reported assumptions. Inflation and unavailable per-period inputs appear once in exclusions; no formula was invented. |
| S511 | PASS_1_COMPLETE | Central computer-generated size-stratified randomization matches article. Notification lead-time difference is peripheral; no changed randomized comparison or decision rule established. |
| S512 | PASS_1_COMPLETE | Discharge drug composite matches. Five-component in-hospital definition versus four-component reported definition is F-ST1-502. |
| S513 | PASS_1_COMPLETE | Toolkit measurement/implementation and effect-modification plan reviewed; primary-outcome toolkit-use subgroup implication is F-ST1-504. Process evaluation publication itself is explicitly deferred. |
| S514 | PASS_1_COMPLETE | >80% medication-concordance/2,200 substudy definitions reviewed; no matching published value is supplied and these are not designated key secondary. No inferential mismatch manufactured. |
| S515 | PASS_1_COMPLETE | ITT allocation by randomized exposure and hospital random effects agree with report. Missing follow-up sensitivity descriptions considered jointly with S516; complete/missing 21,079+295=21,374. |
| S516 | PASS_1_COMPLETE | Three-call rule and planned complete-case/multiple-imputation sensitivity agree with report descriptions; report says results similar but supplies no imputed OR for a numerical reproduction. |
| S517 | PASS_1_COMPLETE | All baseline cells and count/percentage pairs in eTables 1, 3, 4 checked; 12, 60 and 36 pairs respectively reconcile with the display-precision rule. No denominator or dispersion conflict established. |
| S518 | PASS_1_COMPLETE | Primary mixed logistic, random hospital, fixed four-month periods match article/eTable 7 primary-model footnote. Supplemental sensitivity models remain separately identified. |
| S519 | PASS_1_COMPLETE | GRACE covariate sensitivity matches main covariate list and all eTable 5 GRACE model rows; creatinine availability does not establish undisclosed imputation in that model. |
| S520 | PASS_1_COMPLETE | All reported subgroup partitions/models compared with explicit SAP set; changes and missing toolkit-use result consolidated in F-ST1-504. |
| S521 | PASS_1_COMPLETE | Mixed-logistic secondary clinical outcome models agree with source labels; medication composite implication is F-ST1-502. Secondary exploratory interpretation does not by itself remove their explicit secondary-outcome labels. |
| S522 | PASS_1_COMPLETE | Substudy and SAE reporting plans read; no specific conflicting reported result, analysis set or decision supplied. General absence of these non-key-secondary results is excluded. |
| S523 | PASS_1_COMPLETE | O'Brien–Fleming interim/final thresholds match article: z2.797/.005 and z1.977/.048. Gaussian conversion differences are within displayed alpha intervals; no incompatible interim or final conclusion supplied. |
| S524 | PASS_1_COMPLETE | Semiannual safety reviews and at-least-annual DSMB plan are compatible with described one-year analysis; no additional inference or stopping result supplied. |
| S525 | PASS_1_COMPLETE | R3M/percentiles/boxplot definitions apply to operational audit examples, not inferential 95% CIs; no trial-result comparison made. |
| S526 | PASS_1_COMPLETE | Opportunity composites have source-defined 11 AMI/STEMI, 8 NSTEMI and 6 discharge items. These are separate operational measures, not the MACE or optimal-drug composite. |
| S527 | PASS_1_COMPLETE | Process timing/eligibility definitions checked against main process outcomes; source allows measure-specific denominators, and no conflicting printed threshold producing a result found. |
| S528 | PASS_1_COMPLETE | Admission/discharge checklist eligibility flags are coherent with excluding contraindications in main process measures; no preferred clinical regimen or method proposed. |
| S529 | PASS_1_COMPLETE | Age difference −.6 within ordered −2.0,.8; pooled mean/SD interval reproduces endpoints; no P printed. |
| S530 | PASS_1_COMPLETE | Male counts 15973/21079 and 210/295 reproduce proportions and −4.5904 percentage-point difference; unpooled binary Wald CI −9.7909,.6101 matches −9.8,.6. |
| S531 | PASS_1_COMPLETE | Tobacco counts/proportions reproduce 11.6 difference and ordered 5.9,17.3 interval; no contradictory test printed. |
| S532 | PASS_1_COMPLETE | Diabetes counts/proportions reproduce .7 difference and ordered −5.0,6.4 interval; null included; no test supplied. |
| S533 | PASS_1_COMPLETE | Transfer counts/proportions reproduce 5.2 difference and ordered −.5,10.9 interval; null included; no test supplied. |
| S534 | PASS_1_COMPLETE | Insurance counts/proportions reproduce 1.9 difference and ordered −3.1,6.9 interval; null included; no test supplied. |
| S535 | PASS_1_COMPLETE | STEMI counts/proportions reproduce −4.8 difference and ordered −10.4,.9 interval; null included; no test supplied. |
| S536 | PASS_1_COMPLETE | Median-based 21 difference can be obtained within 246/266 half-unit intervals; 21 lies in −38,80. No median-interval method inferred from IQRs. |
| S537 | PASS_1_COMPLETE | Weight −.9 within −2.0,.2; pooled mean/SD calculation reproduces CI. |
| S538 | PASS_1_COMPLETE | SBP .4 within −2.9,3.7; pooled mean/SD calculation reproduces CI, unlike an automatically assumed Welch procedure. |
| S539 | PASS_1_COMPLETE | Heart rate 3.0 within .8,5.2; pooled mean/SD interval reproduces. No P supplied; no conflicting statement of nonsignificance specifically tied to this interval. |
| S540 | PASS_1_COMPLETE | Troponin 3.3 within .1,6.5, direction matches missing minus complete medians. Main P<.001 and CI both exclude null at .05; Gaussian quantitative P reconstruction is only a diagnostic and cannot establish equality with an unstated median/rank test. |
| S541 | PASS_1_COMPLETE | LDL estimate 9.0 is inside ordered CI, but printed CI differs from same-display reproducing mean/SD calculation beyond display precision: F-ST1-501. |
| S542 | PASS_1_COMPLETE | Triglyceride medians reproduce 7 difference; ordered −3,17 contains 7; no confidence construction inferred from IQRs. |
| S543 | PASS_1_COMPLETE | Creatinine displayed medians 1.0/1.0 permit .1 difference within half-unit intervals; ordered −.2,.3 contains .1. |
| S544 | PASS_1_COMPLETE | Glucose medians reproduce 1 difference; ordered −6,8 contains 1; no unspecified quantile method reconstructed. |
| S545 | PASS_1_COMPLETE | Hemoglobin 0.0 inside −.3,.2; mean/SD calculation overlaps endpoints after mean rounding; printed unit issue excluded as notation. |
| S546 | PASS_1_COMPLETE | All 17 modeled differences and all 34 arm estimates are inside ordered CIs; direction agrees with marginal intervention-minus-control values after precision. Modeled-versus-crude contrast excluded. No P/test supplied; covariance not invented. |
| S547 | PASS_1_COMPLETE | All four MACE ORs inside ordered CIs, all include 1; matched main primary model distinguished from additional GRACE/transfer/insurance/aspirin adjustments. |
| S548 | PASS_1_COMPLETE | All four 30-day mortality ORs inside ordered CIs including 1; no P or significance conflict. |
| S549 | PASS_1_COMPLETE | All four cardiovascular mortality ORs inside ordered CIs including 1; similarity to all-cause rows alone supplies no contradiction. |
| S550 | PASS_1_COMPLETE | All four in-hospital mortality ORs inside ordered CIs including 1; no test supplied. |
| S551 | PASS_1_COMPLETE | All four reinfarction ORs inside ordered CIs including 1; model contrast consistently intervention/control. |
| S552 | PASS_1_COMPLETE | All four stroke ORs inside ordered CIs including 1; direction changes among adjustment models are allowed by distinct model definitions. |
| S553 | PASS_1_COMPLETE | All four GUSTO bleeding ORs inside ordered CIs including 1; wide intervals alone do not contradict sparse-event model results. |
| S554 | PASS_1_COMPLETE | All four in-hospital medication ORs inside ordered CIs excluding 1 above; no P. Endpoint-component change F-ST1-502. |
| S555 | PASS_1_COMPLETE | All four discharge medication ORs inside ordered CIs excluding 1 above; definition includes statin as planned. |
| S556 | PASS_1_COMPLETE | All four tobacco-advice ORs inside ordered CIs including 1; distinct covariate adjustment explains different point directions without a source conflict. |
| S557 | PASS_1_COMPLETE | MACE OR1.14 inside .76,1.70, null included; time-exposure interaction model distinguished from primary model; no interaction coefficient inferred. |
| S558 | PASS_1_COMPLETE | Mortality OR.98 inside .63,1.52, null included; no P/test supplied. |
| S559 | PASS_1_COMPLETE | Cardiovascular mortality OR1.00 inside .64,1.56; no P/test supplied. |
| S560 | PASS_1_COMPLETE | In-hospital mortality OR1.43 inside .83,2.46; no P/test supplied. |
| S561 | PASS_1_COMPLETE | Reinfarction OR2.81 inside .79,9.94; no P/test supplied. |
| S562 | PASS_1_COMPLETE | Stroke OR2.06 inside .58,7.36; no P/test supplied. |
| S563 | PASS_1_COMPLETE | GUSTO bleeding OR2.53 inside .50,12.94; no P/test supplied. |
| S564 | PASS_1_COMPLETE | In-hospital medication OR.87 inside .70,1.07, null included; different model from eTable 5 so direction not equated; component change F-ST1-502. |
| S565 | PASS_1_COMPLETE | Discharge medication OR1.45 inside 1.12,1.88, null excluded above; no contrary printed significance assertion. |
| S566 | PASS_1_COMPLETE | Tobacco advice OR.99 inside .37,2.66, null included; no P/test supplied. |
| S567 | PASS_1_COMPLETE | All 16 eTable 7 RD/OR point estimates inside ordered intervals; directions match within each stated model; all eight n/% pairs reconcile with 10066/11308. Expanded status F-ST1-503. Cluster OR upper1.00 vs RD upper−.01 has compatible rounding and no P/test, separately excluded. |
| S568 | PASS_1_COMPLETE | All visible hospital points contained in respective ordered bars; stated CI/nonzero rule is coherent. Cross-location residual direction discrepancy consolidated with S569 in F-ST1-505. Exact coefficients/IDs are absent; no decimal digitization substituted. |
| S569 | PASS_1_COMPLETE | Source index Expected−Observed definition compared with eFigure 1A plotted sign and caption: F-ST1-505. |
| S570 | PASS_1_COMPLETE | Every cohort×step MACE panel inspected; points/rates within 0–100%, visible CI segments contain points, open-to-filled crossover matches five-cohort schedule. No exact hospital events/Ns or confidence formula supplied. |
| S571 | PASS_1_COMPLETE | Every cohort×step mortality panel inspected with same checks; rates remain no greater than corresponding graphical MACE rates where recognizable. No exact decimal/statistical test inferred from pixels. |

## Additional reconciliation details

The six binary eTable 1 contrasts reproduce under the unpooled proportion-difference normal formula using their printed integer counts. This differs appropriately from the mean/SD calculation. All count-percent pairs in eTables 1, 3 and 4 reconcile after rounding (12+60+36=108 pairs), and all eight eTable 7 pairs reconcile. eTable 3's control counts sum to 10,066 and intervention counts to 11,308; paired step totals match eTable 4's 2,915, 3,311, 3,516, 3,854, 4,043 and 3,735, totaling 21,374. Every continuous mean/SD and median/IQR cell in eTables 3–4 was checked for nonnegative dispersion and ordered IQRs containing medians. Weighted means may depend on row-specific available observations; none were assumed for clinical measurements. Matching labels establish these tables as descriptive data, whereas eTable 2 explicitly uses marginal effects from logistic/linear/quantile models.

Log-symmetry checks for eTables 5–6 are diagnostics only: the ORs are approximately geometric centers of their CIs, and no point-outside-interval or endpoint reversal appears. No covariance, variance estimator, exact degrees of freedom, exposure coding, or interaction estimand was inferred. eTable 7's RD and OR are separately defined transformations and confidence calculations; null-boundary printing is not a supplied P value or stated test.

## Excluded observations

This table contains only apparent issues considered and not emitted, each once with exactly one reason code. Reconciled routine checks are recorded above instead.

| Location | Observation | Reason code |
|---|---|---|
| PLAN SAP p. 4 §5 vs p. 3 schedule | Randomization text says four time periods, but five switches and five cohorts are explicit in the immediate design/schema; no changed allocation or primary decision rule is shown. | CONTEXT_RESOLVES |
| PLAN SAP p. 4 sample inflation, protocol p. 18 | 15,000 divided by .95 is 15,789.47 rather than 15,750; the ~0.25% difference and displayed 5% input interval fall within the display-precision rule. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN sample-size paragraphs | Exact 80% stepped-wedge power cannot be recomputed without anticipated cluster-by-period sizes, their variability and the calculation implementation; no reproduced conflicting power result is supplied. | CONDITIONAL_OR_UNREPORTED |
| PLAN SAP p. 4 notification vs REPORT main p. 2 | Three-week planned versus two-week reported site notification changes an operational lead time, without a demonstrated outcome, analysis-population or decision-rule implication. | PERIPHERAL_COMPARISON |
| REPORT eTable 1 p. 17 footnote a | Intervention-minus-control terminology is attached to complete/missing follow-up columns; all displayed differences identify missing-minus-complete directly, resolving the intended comparison. | TERMINOLOGY_OR_WORDING |
| REPORT eTable 1 troponin CI and main p. 6 P<.001 | A Gaussian diagnostic from 3.3 and CI .1–6.5 suggests a different numerical P, but no common test or median-CI convention is supplied; both printed summaries exclude the null at .05 and the display does not establish a shared quantitative test. | CONDITIONAL_OR_UNREPORTED |
| REPORT eTables 1–4 hemoglobin unit | The printed mg/dL label for values near 13 is a unit-notation slip whose reading is evident; no numerical blood concentration disagreement is established. | NOTATION_OR_TYPOGRAPHY |
| REPORT eTable 2 p. 18 vs crude main baseline values | Marginal effects adjusted for hospital clustering/time differ from crude descriptive summaries; the source explicitly distinguishes the analyses. | MODEL_VERSUS_CRUDE |
| REPORT eTable 2 p. 18 footnote; eTable 6 p. 22 title | Row-specific model family, covariance construction, and time-exposure interaction coding/estimand are not fully printed; missing details alone do not conflict with a printed value or stated result. | CONDITIONAL_OR_UNREPORTED |
| REPORT eTable 7 p. 23 cluster expanded MACE row | RD CI upper−.01 excludes 0 while OR CI upper1.00 can round from below1; no P/test conflicts, and differently transformed interval boundaries can reconcile within display precision. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p. 3 secondary analyses vs PLAN secondary labels | Report still identifies the same secondary outcomes, while describing their unadjusted-for-multiplicity analyses as exploratory; this is an inferential caveat rather than an observable outcome-hierarchy change. | TERMINOLOGY_OR_WORDING |
| PLAN substudy/concordance/SAE plans vs REPORT | General absence of separate non-key-secondary substudy or safety summaries is not a reproduced conflicting primary/key-secondary result or decision rule; no specific qualifying omission identified. | OUT_OF_FOCUS |
| PLAN SAP p. 8 and REPORT main p. 3 z/alpha boundaries | Diagnostic two-sided Gaussian conversions of z2.797 (~.00516) and z1.977 (~.04804) are inside the printed alpha half-unit intervals; no supplied interim result or final conclusion conflicts. | ROUNDING_OR_DISPLAY_PRECISION |

## Limitations and handoff

All 71 assigned relationships have explicit `PASS_1_COMPLETE` records. Five findings are emitted (F-ST1-501 through F-ST1-505); 13 apparent observations are excluded once. All findings require the independent inclusion screen before candidate registration. No severity, acceptance, correction or adjudication is assigned.

Reproduction is limited by absent row-specific assay contributor counts, unpublished model internals and absence of exact hospital graph numbers/identifiers. Those limitations did not truncate coverage. Method diagnostics are identified as diagnostics or same-display reproducing checks rather than replacements for the reported analysis. No fresh OCR was required; exact candidate pages have usable current native text and direct visual confirmation.
