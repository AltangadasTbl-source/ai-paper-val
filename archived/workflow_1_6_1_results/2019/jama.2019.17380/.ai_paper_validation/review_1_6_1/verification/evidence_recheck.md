# Mechanical evidence recheck

Scope: every assigned stable ID, C001, C002, C003, C004 and C005, including every registered occurrence of the repeated C004 pattern. All remain Pending Human Adjudication. Evidence states describe source-confirmation facts only. No candidate is removed and no adjudication is supplied.

The complete QUALITY_CONTROL_SCOPE.md, review contract, current initial inclusion screen, current ledger, source inventory, evidence-asset inventory and tooling record were read. Exact supplied-source pages were reread with direct CPU Poppler `pdftotext -layout -f N -l N SOURCE.pdf -`; no text was taken from an earlier scientific review. Current exact-page renders `preprocessing/numeric-main-p8.png`, `numeric-main-p9.png`, `numeric-supp2-p12.png`, `numeric-supp2-p18.png` and `numeric-supp2-p19.png` provided visual confirmation of all graphical and sample-accounting cells. Source-matched reusable plan renders for physical pp. 32–33 were also inspected alongside fresh direct-source extraction. The supplied PDFs, not any derivative, are the evidence authority. Direct Poppler 26.01.0 is recorded as available; no OCR, GPU, persistent new derivative, fallback environment, source modification or reused-artifact modification was needed.

All PDF links below identify physical PDF pages. Both the protocol and its implemented analytic addendum are PLAN by prospective content. The article and supplementary result tables/figures are REPORT by retrospective content. No role depends on a file name.

| ID | Evidence state | Relationship type | All relationships | Review domain | Classification change |
|---|---|---|---|---|---|
| C001 | reproduced | P_R | P_R | protocol_report | None |
| C002 | reproduced | P_R | P_R | protocol_report | None |
| C003 | reproduced | P_R | P_R | protocol_report | None |
| C004 | reproduced | S_C | S_C, S_W | statistical_results | None; all repeated rows confirmed, with independent-comparator limits retained |
| C005 | reproduced | S_W | S_W | statistical_results | None |

## C001 — Planned and reported adherence sensitivity definitions differ

**Location found:** Yes, all registered locations. PLAN [original protocol p. 19, §VI.g](../../../joi190122supp1_prod.pdf#page=19) and [implemented addendum p. 33, §15g](../../../joi190122supp1_prod.pdf#page=33); REPORT [main p. 3, Covariates and Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [main p. 4, adherence and robustness paragraphs](../../../jama_de_boer_2019_oi_190122.pdf#page=4), [eTable 1 p. 6](../../../joi190122supp2_prod.pdf#page=6), [eTable 5 p. 10](../../../joi190122supp2_prod.pdf#page=10) and [eTable 8 p. 13](../../../joi190122supp2_prod.pdf#page=13).

**Source value/text matched:** Yes. Original §VI.g says adherence to at least 80% of study medication. Implemented §15g says continuous adherence to at least 80%. These specify the planned restriction for exploratory analyses of the robustness of null findings.

**Comparator matched:** Yes. Main p. 3 defines highly adherent participants by reporting medication use at least two-thirds of the time and lists adherence-restricted secondary analyses. Main p. 4 attributes similar primary results to participants reporting consistent high adherence. eTable 1 defines each qualifying questionnaire as at least two-thirds use; through year 5 requires at least four of six questionnaires. eTables 5 and 8 repeat at least two-thirds on at least four assessments, explicitly listing 6 months and years 1, 2, 3, 4 and 5, and N=1032 per intervention. eTable 1 partitions these as vitamin-D active 546/placebo 486 and omega-3 active 518/placebo 514. eTable 5 reports five-year eGFR differences 0.89 (−0.74, 2.52), P=.28, and 0.42 (−1.22, 2.06), P=.61. eTable 8 reports ACR ratios 1.02 (0.85, 1.22), P=.87, and 0.99 (0.83, 1.19), P=.94.

**Consistency rule applicable:** Yes. The prospective restriction and reported restriction for the same primary-outcome sensitivity purpose must be compared as membership rules, not as synonymous labels.

**Logical comparison reproduced and precision check:** Yes. Two-thirds is 66.666…%, 13.333… percentage points below 80%. The fraction is an exact operational threshold; even treating 80% as a nearest-integer display gives [79.5%, 80.5%), entirely above two-thirds. Four qualifying assessments out of six does not logically imply continuous qualification. A hypothetical participant reporting 70% use on four assessments illustrates nonequivalence; it is not an assertion about an actual participant. Display intervals for the reported effect estimates do not reconcile these membership definitions and are not the basis of this candidate.

**Necessary inputs available:** Both restriction texts, timing, reported N and affected result tuples are available. **Exact missing inputs or definitions:** Operational meaning of continuous 80% adherence, individual longitudinal adherence, membership and estimates under that restriction, and any later threshold amendment. The planned population size and numerical effect of switching rules cannot be reproduced from supplied aggregate results.

**Source-grounded alternative interpretation:** The questionnaire rule could have been adopted through a later amendment or could operationalize a distinct reported sensitivity analysis. The supplied addendum explicitly retains 80%, and no supplied location establishes equivalence to the questionnaire rule.

**Direct observation versus inferred explanation:** Different printed membership rules and the reported adherence-restricted results are direct observations. An unprovided amendment, actual membership differences, and an effect on conclusions are explanations or consequences not established by the package.

**Classification confirmation:** Each prospective restriction is PLAN; each reported definition or result is REPORT. Primary relationship P_R; all relationships P_R; domain protocol_report, focus D. Original and implemented plans agree on 80%, so no P_P conflict is involved. The report locations agree with one another; no S_C/S_W conflict is added merely for corroboration. No correction. Classification ambiguity: no later adherence amendment is supplied.

**Evidence state:** reproduced. Determining fact: directly confirmed continuous at least 80% and at least two-thirds at four of six assessments are nonequivalent rules for the named primary sensitivity analysis.

**Exact remaining human question:** Which operational adherence rule generated eTable 5, and what supplied or additional amendment connects that rule to §15g's continuous-at-least-80% restriction? If both analyses were performed, which participants and results belong to each?

## C002 — Planned and reported primary covariate specifications differ

**Location found:** Yes. PLAN [addendum p. 32, §15e Equation 2 and conditional sensitivity paragraph](../../../joi190122supp1_prod.pdf#page=32) and [p. 33, its continuation](../../../joi190122supp1_prod.pdf#page=33); REPORT [main p. 3, Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [main p. 8, Table 2 and footnote a](../../../jama_de_boer_2019_oi_190122.pdf#page=8), [eTable 4 p. 9](../../../joi190122supp2_prod.pdf#page=9) and [eTable 5 p. 10](../../../joi190122supp2_prod.pdf#page=10).

**Source value/text matched:** Yes. Equation 2 contains an intercept, treatment, categorical time, treatment-by-time, participant random effect and residual. Its following paragraph puts additional baseline-characteristic terms into sensitivity analyses in the event of imbalance. The p. 33 continuation concerns exploring follow-up medication/laboratory covariates as mediators or attenuators; it does not add routine age, sex or baseline-ACR terms to Equation 2.

**Comparator matched:** Yes. Main p. 3 includes linear age, sex and their time interactions, with baseline urine ACR and its time interaction additionally included for eGFR. Table 2 footnote a explicitly derives primary differences from a mixed model adjusted for age, sex and baseline ACR. Primary five-year tuples are vitamin D 0.9 (−0.7, 2.5), P=.25, and omega-3 0.9 (−0.7, 2.6), P=.27. eTables 4 and 5 corroborate those same adjustment variables for complete-case/adherence sensitivity models.

**Consistency rule applicable:** Yes. Compare the named primary model's fixed-effect specification and the separate conditional sensitivity provision with the applied primary model, without evaluating whether one model is preferable.

**Logical comparison reproduced and precision check:** Yes. The routine report terms age, sex, age-by-time, sex-by-time, baseline ACR and ACR-by-time are absent from the supplied primary Equation 2. The common random intercept, categorical time and treatment-by-time terms do not make the fixed-effect sets identical. No numeric rounding interval can create or remove a model term or change its primary-versus-conditional-sensitivity designation. Reported effect estimates have their ordinary half-unit display intervals, but no effect-size discrepancy is asserted and no crude recomputation is used.

**Necessary inputs available:** Primary equation, conditional adjustment statement, reported model description, primary footnote and result tuples. **Exact missing inputs or definitions:** Implemented formula/code; whether a prespecified imbalance trigger was invoked; any later amendment adopting routine adjustment; and primary result tuples under the literal Equation 2. These prevent quantifying the impact of extra terms, not reproducing the specification comparison.

**Source-grounded alternative interpretation:** A later expanded primary specification may exist, or a conditional sensitivity model may have become the published primary model. The supplied text does not identify such a linkage.

**Direct observation versus inferred explanation:** Different printed model-term sets and analysis designations are direct observations. The reasons for added adjustment, its prospective timing and its effect on estimates are not established.

**Classification confirmation:** Addendum formula/continuation are PLAN; applied methods, Table 2 and sensitivity results are REPORT. Primary relationship P_R; all relationships P_R; domain protocol_report, focus D. Sensitivity footnotes corroborate the report specification and create no additional cross-report conflict. No correction. Classification ambiguity: later formula amendment or conditional-trigger linkage unavailable.

**Evidence state:** reproduced. Determining fact: the explicit supplied primary equation and separately conditional adjustment paragraph do not specify the report's routine primary adjustment terms.

**Exact remaining human question:** Which prospectively designated model formula produced Table 2, and what amendment or conditional-analysis linkage reconciles its routine age, sex and baseline-ACR terms with §15e Equation 2?

## C003 — Planned and reported primary population definitions differ

**Location found:** Yes. PLAN [addendum implementation cover p. 31](../../../joi190122supp1_prod.pdf#page=31) and [p. 32, §15c](../../../joi190122supp1_prod.pdf#page=32); REPORT [main p. 3, primary analysis paragraph](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p. 4, retention and primary results](../../../jama_de_boer_2019_oi_190122.pdf#page=4), [p. 6, Figure 1](../../../jama_de_boer_2019_oi_190122.pdf#page=6) and [p. 8, Table 2](../../../jama_de_boer_2019_oi_190122.pdf#page=8).

**Source value/text matched:** Yes. The cover says the analytic changes were implemented upon funding February 24, 2016. §15c defines intent-to-treat inclusion by all participants who return at least one follow-up biosample, regardless of adherence or other postrandomization characteristics.

**Comparator matched:** Yes. Main p. 3 says all participants were analyzed according to randomized group regardless of adherence or follow-up, calling this the full analytic population. Figure 1 includes all four randomized arms, 370, 333, 289 and 320, in primary analyses. Its follow-up blood boxes are 303, 280, 242 and 265. Main p. 4 gives at least one follow-up blood sample in 1090 and urine sample in 1091, and the primary differences 0.9 (−0.7, 2.5) and 0.9 (−0.7, 2.6). Table 2 footnote b states change was summarized over all participants using imputation; displayed per-time-point N denotes measured contributions and is not an alternative full primary N.

**Consistency rule applicable:** Yes, for the explicit prospective and reported inclusion definitions. A definition that conditions inclusion on biosample return differs from one explicitly irrespective of follow-up. This comparison does not establish a particular numerical decrease in the planned population.

**Calculation/logical comparison reproduced and precision check:** Yes. Primary boxes total 370+333+289+320=1312; any-follow-up-blood boxes total 303+280+242+265=1090; 1312−1090=222 have no follow-up blood sample. The blood/urine union is bounded by 1091 to 1312 from the marginals and the randomized total; it is not determined. All Ns are exact counts, with no rounding tolerance. The membership conditions are categorical, so half-unit display intervals cannot make them identical. This recheck does not call 222 the number without any biosample and does not claim that the plan-eligible union was necessarily smaller than 1312.

**Necessary inputs available:** Implementation status, explicit inclusion texts, randomized/full-primary count, blood and urine marginals and affected primary results. **Exact missing inputs or definitions:** Participant-level blood/urine overlap; meaning of biosample for applying §15c; whether the plan statement was an exhaustive eligibility rule or a minimum inclusion guarantee; and any subsequent population amendment. No exact plan-eligible N or counterfactual effect can be calculated.

**Source-grounded alternative interpretation:** Because §15c says all biosample returners will be included without the word only, it could be read as a minimum inclusion guarantee consistent with including additional randomized participants. Its wording defines what intent-to-treat means in that plan, making a restricted-population reading supportable as well. A later all-randomized amendment could also reconcile the analysis. The package does not expressly settle these interpretations.

**Direct observation versus inferred explanation:** The plan's biosample-qualified inclusion description and report's regardless-of-follow-up description, and inclusion of 1312, are directly observed. An actual numerical difference between any-biosample eligibility and reported population, or a change in effect, is not established.

**Classification confirmation:** Cover and §15c are PLAN; applied methods, flow, retention and Table 2 are REPORT. Primary relationship P_R; all relationships P_R; domain protocol_report, focus D. Report counts corroborate the full-population side and do not create a separate internal count issue. No correction. Classification ambiguity: exact planned eligibility interpretation, blood/urine union and any later population amendment unavailable.

**Evidence state:** reproduced. Determining fact: the directly confirmed primary inclusion descriptions differ explicitly in whether follow-up is named as an inclusion condition; the recheck establishes that definition comparison rather than an unprovided numerical population difference.

**Exact remaining human question:** Does §15c define an exclusive any-follow-up-biosample population or only a minimum inclusion guarantee, and which operative amendment or analysis specification establishes inclusion of all 1312 regardless of follow-up?

## C004 — Forest participant counts do not align with treatment summaries

**Location found:** Yes, all registered locations and all repeated rows: REPORT [main p. 5, Table 1](../../../jama_de_boer_2019_oi_190122.pdf#page=5), [p. 6, Figure 1](../../../jama_de_boer_2019_oi_190122.pdf#page=6), [p. 8, Table 2 and Figure 3](../../../jama_de_boer_2019_oi_190122.pdf#page=8), [p. 9, Figure 4](../../../jama_de_boer_2019_oi_190122.pdf#page=9), [supplement p. 11, eTable 6](../../../joi190122supp2_prod.pdf#page=11), [p. 16, eTable 11, retained corroboration from screening](../../../joi190122supp2_prod.pdf#page=16), [p. 18, eFigure 2](../../../joi190122supp2_prod.pdf#page=18) and [p. 19, eFigure 3](../../../joi190122supp2_prod.pdf#page=19). The two main figures and two supplemental figures were visually read cell by cell. There are 15 vitamin-D rows and 11 omega-3 rows per outcome: 52 displayed row occurrences in total.

**Source value/text matched:** Yes. Figure 1 and Table 1 four-arm headings give D+O 370, D+O-placebo 333, D-placebo+O 289, and both placebos 320. eTable 11 confirms D active/placebo 703/609 and O active/placebo 659/653.

**Comparator matched:** Yes. Table 2 assigns five-year changes −12.3 to D active and −13.1 to D placebo, −12.2 to O active and −13.1 to O placebo. Figure 3 assigns the same means to the same headings but prints N=703 under Placebo and 609 under Vitamin D. Figure 4 likewise has Placebo N=659/mean −13.1 and Omega-3 N=653/mean −12.2. eTable 6 assigns five-year geometric changes 2.97/3.02 to D active/placebo and 2.94/3.05 to O active/placebo. Supplemental forest overall means follow those treatment labels while Ns again have the opposite assignment order.

The following tables record every visually confirmed column pairing. Each N pair is **literal displayed Placebo / Active** and is identical in the two linked figures for that intervention. Both mean(SD) columns are given in that same literal order; they are transcriptions, not proposed replacement cells. D main values are in mL/min/1.73 m² and D/O supplemental values are geometric change ratios. O main values also use mL/min/1.73 m².

| Vitamin-D row: main Figure 3 p. 8 and eFigure 2 p. 18 | N Placebo / Active, both figures | Main Placebo mean(SD) / Active mean(SD) | Supplement Placebo geometric mean(SD) / Active geometric mean(SD) | Independent assignment comparison |
|---|---|---|---|---|
| Overall | 703 / 609 | −13.1(14.4) / −12.3(14.8) | 3.02(4.10) / 2.97(4.50) | Figure 1: active 703, placebo 609 |
| White | 451 / 406 | −12.1(13.7) / −11.7(13.5) | 3.00(3.95) / 3.02(4.60) | Table 1: active 240+211=451, placebo 199+207=406 |
| Black | 148 / 130 | −15.9(16.0) / −14.7(17.1) | 2.90(4.79) / 3.29(4.10) | Table 1: active 73+75=148, placebo 59+71=130 |
| Baseline ACR <30 | 635 / 559 | −12.4(14.2) / −11.8(14.4) | 3.38(3.82) / 3.39(4.23) | Independent arm-stratum counts unavailable |
| Baseline ACR ≥30 | 67 / 50 | −20.4(15.0) / −17.3(17.4) | 0.87(4.90) / 0.86(4.65) | Independent arm-stratum counts unavailable |
| Baseline 25(OH)D <20 | 110 / 85 | −14.6(13.9) / −12.2(17.1) | 2.16(4.36) / 2.32(4.68) | Table 1: active 62+48=110, placebo 41+44=85 |
| Baseline 25(OH)D 20 to <30 | 230 / 203 | −14.7(15.2) / −12.4(14.0) | 3.08(4.28) / 2.80(4.33) | Table 1: active 109+121=230, placebo 87+116=203 |
| Baseline 25(OH)D ≥30 | 332 / 297 | −11.5(13.9) / −12.3(14.6) | 3.28(3.88) / 3.36(4.53) | Table 1: active 184+148=332, placebo 146+151=297 |
| Baseline eGFR ≥60 | 612 / 531 | −14.1(14.4) / −13.7(14.5) | 3.09(3.87) / 3.00(4.17) | Independent arm-stratum counts unavailable |
| Baseline eGFR <60 | 89 / 76 | −5.8(12.4) / −3.0(13.6) | 2.60(5.83) / 2.80(7.09) | 89+76=165 matches main p. 4 total only; arm allocation unavailable |
| BMI <25 | 87 / 87 | −12.9(13.2) / −10.5(11.7) | 3.18(3.67) / 2.60(4.17) | Equal Ns cannot independently establish a count discrepancy |
| BMI 25 to <30 | 228 / 205 | −12.3(14.1) / −12.2(14.4) | 3.32(4.04) / 2.82(4.16) | Independent arm-stratum counts unavailable |
| BMI ≥30 | 364 / 294 | −13.7(15.0) / −12.8(15.7) | 2.78(4.27) / 3.17(4.81) | Independent arm-stratum counts unavailable |
| Omega-3 assignment placebo | 333 / 320 | −13.2(14.9) / −13.0(14.7) | 3.15(4.03) / 2.96(4.29) | Figure 1: D active 333, D placebo 320 |
| Omega-3 assignment active | 370 / 289 | −12.9(13.9) / −11.7(14.9) | 2.89(4.19) / 2.98(4.71) | Figure 1: D active 370, D placebo 289 |

| Omega-3 row: main Figure 4 p. 9 and eFigure 3 p. 19 | N Placebo / Active, both figures | Main Placebo mean(SD) / Active mean(SD) | Supplement Placebo geometric mean(SD) / Active geometric mean(SD) | Independent assignment comparison |
|---|---|---|---|---|
| Overall | 659 / 653 | −13.1(14.8) / −12.2(14.5) | 3.05(4.16) / 2.94(4.48) | Figure 1: active 659, placebo 653 |
| EPA/DHA ≤2.2 | 332 / 347 | −13.3(15.0) / −12.5(14.6) | 2.90(4.39) / 2.95(4.56) | Independent arm-stratum counts unavailable |
| EPA/DHA >2.2 | 308 / 292 | −12.9(14.6) / −11.9(14.4) | 3.21(3.93) / 2.93(4.39) | Independent arm-stratum counts unavailable |
| Baseline ACR <30 | 596 / 598 | −12.6(14.8) / −11.5(13.8) | 3.41(3.95) / 3.36(4.12) | Independent arm-stratum counts unavailable |
| Baseline ACR ≥30 | 62 / 55 | −18.1(14.2) / −19.1(18.3) | 0.92(4.14) / 0.81(5.31) | Independent arm-stratum counts unavailable |
| hsCRP ≤0.2 | 334 / 335 | −12.9(14.3) / −11.5(13.4) | 3.27(4.17) / 2.93(4.16) | Independent arm-stratum counts unavailable |
| hsCRP >0.2 | 323 / 316 | −13.3(15.3) / −13.0(15.5) | 2.82(4.13) / 2.95(4.82) | Independent arm-stratum counts unavailable |
| Fish intake <1.5 servings/week | 354 / 329 | −13.4(15.3) / −11.8(14.7) | 2.94(4.17) / 2.94(4.04) | Independent arm-stratum counts unavailable |
| Fish intake ≥1.5 servings/week | 295 / 310 | −12.9(14.3) / −12.7(14.3) | 3.15(4.15) / 2.94(4.94) | Independent arm-stratum counts unavailable |
| Vitamin-D assignment placebo | 289 / 320 | −13.2(14.9) / −12.9(13.9) | 3.15(4.03) / 2.89(4.19) | Figure 1: O active 289, O placebo 320 |
| Vitamin-D assignment active | 370 / 333 | −13.0(14.7) / −11.7(14.9) | 2.96(4.29) / 2.98(4.71) | Figure 1: O active 370, O placebo 333 |

**Consistency rule applicable:** Yes. A treatment-specific participant N and summary displayed beneath a common treatment heading must be compared with the supplied randomized assignment and matching treatment-specific overall result. This is not a recomputation of modeled treatment differences from crude summaries.

**Calculation reproduced:** D active=370+333=703, D placebo=289+320=609; O active=370+289=659, O placebo=333+320=653. All independent subgroup calculations are written above. Exchanging entire group headings would conflict with the matching overall Table 2/eTable 6 means; retaining all printed cells pairs the N with the other assignment's count. The same literal N orders appear in all four forests. Independent assignment evidence reproduces the reversed order for 8 D rows and 3 O rows in both outcome displays, 22 row occurrences. The other 30 row occurrences are directly confirmed pattern locations, with the lack of an independent assignment-stratum comparator explicitly recorded; no alternative raw-data mapping is invented.

**Display-precision interval check:** Ns are exact integers, not rounded estimates. Even hypothetical nearest-integer intervals for the overall D counts [702.5,703.5) and [608.5,609.5), or O counts [658.5,659.5) and [652.5,653.5), are disjoint. Known independent subgroup Ns differ by 45, 18, 25, 27, 35, 13 or 81 for D and 31 or 37 for O; none can be reconciled by half-unit rounding. The equal 87/87 BMI row is not independently discrepant. Main overall one-decimal mean intervals for D placebo −13.1 versus active −12.3, and O placebo −13.1 versus active −12.2, are disjoint, establishing the matching summary order. Supplemental two-decimal geometric means 3.02 versus 2.97 and 3.05 versus 2.94 have disjoint half-unit intervals of width 0.01. Thus a whole-heading exchange does not reconcile the independently matched overall means. No claim is made that the adjusted difference or P value changes.

**Necessary inputs available:** All printed figure Ns and summary cells, treatment headings, captions, four randomized arms, the available Table 1 strata, and matching overall treatment means. **Exact missing inputs or definitions:** Independent assignment-specific counts for ACR, eGFR, BMI, EPA/DHA, hsCRP and fish strata; participant-level analysis membership; unrounded subgroup outputs; any definition of a special population for the figure N columns; and an explicit intended N-to-mean/SD mapping. These gaps prevent specifying replacement subgroup triplets, not reproducing the supplied overall and independently supported subgroup comparison.

**Source-grounded alternative interpretation:** The N columns may use active/placebo ordering while summary columns use placebo/active ordering. Alternatively Ns might describe a separately defined population; neither caption identifies such a population. The former is an inference supported by the independent count comparators, not a supplied instruction to remap every SD or subgroup result. Equal Ns and equal displayed means in individual rows do not independently support a discrepancy.

**Direct observation versus inferred explanation:** Literal 52-row cell pairings, independently established count mismatches and matching overall summary labels are direct observations. A particular production mechanism, exchange of every subgroup N, or changes to adjusted estimates are not established.

**Classification confirmation:** Every compared location is REPORT. Within-main Figure 1/Table 1 versus Figures 3/4 gives S_W; main assignment counts versus supplemental forests and eTable 11 versus main forests establish S_C, while eTable 11 versus supplemental forests and eTable 6 mean comparisons also support internal-report checks. Primary S_C by precedence over S_W; all relationships S_C, S_W; domain statistical_results, focus A. Counts are the underlying issue even though group attribution is involved. No PLAN comparator exists. No correction. Classification ambiguity: the intended column mapping and several subgroup assignment counts are unavailable.

**Evidence state:** reproduced. Determining fact: direct visual overall N/mean pairings conflict with exact randomized treatment counts while matching treatment-specific overall means in independent result tables; multiple directly supported subgroup rows repeat the pattern. All registered rows have been reread, without asserting unavailable independent subgroup populations.

**Exact remaining human question:** Which treatment-specific N belongs with each displayed five-year eGFR and ACR mean/SD triplet, and does a distinct population or independent column ordering explain the repeated displays? What supplied participant-level counts establish the mapping in the remaining subgroup rows?

## C005 — Complete-case ACR sample-size constructions do not reconcile

**Location found:** Yes. REPORT [supplement p. 12, eTable 7 title, both baseline/year-5 partitions and asterisk footnote](../../../joi190122supp2_prod.pdf#page=12), with REPORT [main p. 4, urine retention](../../../jama_de_boer_2019_oi_190122.pdf#page=4) and [supplement p. 11, eTable 6 year-5 counts](../../../joi190122supp2_prod.pdf#page=11) as corroborating context. eTable 7 was visually inspected, including the explicit included-in-analysis phrase.

**Source value/text matched:** Yes. Title N=944; D baseline and year-5 active/placebo Ns each 504/440; O baseline and year-5 Ns each 477/467. Five-year ratios are D 1.03 (0.86,1.22), P=.77, and O 0.93 (0.78,1.11), P=.44.

**Comparator matched:** Yes. The directly linked asterisk footnote says 1312 enrolled; 1311 donated baseline urine; 991 also donated year-5 urine and were included in this analysis; 320 baseline-but-not-year-5 donors excluded; one without baseline urine excluded. Main p. 4 gives 945 final urine contributors. eTable 6 partitions final contributors as 505+440 and 478+467, both 945.

**Consistency rule applicable:** Yes. An analysis population's title N, both factorial marginal partitions and directly referenced included/excluded accounting should identify the same complete-case population or explicitly distinguish different sets.

**Calculation reproduced and precision check:** Yes. 504+440=944; 477+467=944, each at baseline and year 5. Footnote accounting is 1311−320=991 and 1312−320−1=991. The constructions differ by 991−944=47. To obtain 944 from 1311 would exclude 367 rather than 320 baseline donors. Counts are exact integers. Even hypothetical nearest-integer display intervals [943.5,944.5) and [990.5,991.5) are disjoint; allowing half-unit intervals for the subtraction yields [990,992), still disjoint from the title interval. The result tuples are named to identify the affected sensitivity analysis, not used for an independent statistical contradiction.

**Necessary inputs available:** Title, every repeated partition, full footnote accounting and result tuples. **Exact missing inputs or definitions:** Participant-level eligibility and paired specimen usability; any 47 additional exclusions; whether 991/320 describe a distinct return population or time point; and confirmation of the actual analysis N. Aggregate printed material cannot establish that linkage.

**Source-grounded alternative interpretation:** 991 could describe returned specimens before usability/eligibility exclusions, while 944 are usable paired measurements. The explicit footnote statement that 991 were included in this analysis does not describe that distinction. A different participant/time-point set for the footnote could also explain the competing accounting, but it is not named.

**Direct observation versus inferred explanation:** The two internally coherent but differing analysis-N constructions are direct observations. A 47-person unreported eligibility/usability exclusion, a different specimen pool, or a change in effect estimate is not established. Repeated partitions and neighboring final-urine counts support 944 as one reading without explaining the footnote's 991 inclusion claim.

**Classification confirmation:** All compared content is REPORT. The actual conflicting constructions are within eTable 7 in one results supplement, so primary S_W; all relationships S_W; domain statistical_results, focus A. Main retention and eTable 6 are corroboration and do not add S_C merely because they are cited. No correction. Classification ambiguity: unprovided eligibility/usability linkage.

**Evidence state:** reproduced. Determining fact: the exact title/arm partitions identify 944 while the explicitly included-in-analysis footnote and its arithmetic identify 991; no rounding interval connects them.

**Exact remaining human question:** Did eTable 7 analyze 944 or 991 participants, and what specimen, eligibility or timing accounting connects its four repeated arm partitions to the 991-included/320-excluded footnote?

## Completion and limitations

Covered stable IDs: C001, C002, C003, C004, C005. Evidence-state counts: reproduced 5; reproduced_after_transcription_correction 0; not_reproduced 0. Every cited affected page and all 52 C004 figure-row occurrences were found and reread. No source-confirmation or transcription gap remains for the assigned scope. No classification or location correction was needed. The source does not supply individual adherence, a later amendment, an exhaustive operational interpretation of §15c, the blood/urine union, participant-level subgroup membership, intended forest cell mappings, or eTable 7's reconciliation of inclusion constructions. These limitations are retained as exact human questions; none is converted into a raw-data claim or adjudication.
