# Statistical Consistency Review — Pass 1

## Scope, evidence, and method

Independent pass-1 review completed for all **53/53** stable inferential relationships in `statistics/relationship_inventory.md`: S001-S027 (DOC-001 main article) and S028-S053 (DOC-002 protocol, DOC-003 SAP, and DOC-004 results supplement). Direct PDFs were the authority; current source-matched native/layout extraction and the relationship shards were used as locators and transcription aids.

For each relationship, two complementary source-grounded checks were applied:

1. Point estimate/interval null containment, endpoint order, sign/direction, effect-measure/scale label, and P-value/test/model compatibility when the source supplied a matching model and inferential definition.
2. Matching cross-location occurrences, denominator and arithmetic implications, duplicate values, population/estimand labels, and narrative interpretation.

`DIAGNOSTIC` below means a rounded or qualitative compatibility check only; it does not substitute for an unreported variance estimator, covariance structure, sidedness, degrees of freedom, or estimand definition. `NO PROPOSAL` does not adjudicate validity. Every record is `PASS_1_COMPLETE`.

## Pass-1 candidate proposals (no stable candidate IDs assigned)

### P-SP1-001 — Multiple-testing statement conflicts with the supplied SAP/protocol plan

- **Proposed category:** Statistical reporting inconsistency.
- **Exact direct observations:** DOC-001 PDF p.4 states, “There was no adjustment for multiple testing.” DOC-003 PDF p.12 states that adjusted P values for the 10 key-secondary-component comparisons “will be derived using the Benjamin-Hochberg procedure”; its proposed Table 11 on p.25 also has an `Adjusted P-values (Benjamin-Hochberg)` column. DOC-002 PDF p.20 likewise states that adjusted P values for the 10 comparisons will be derived.
- **Reproducible comparison:** The main article’s explicit no-adjustment statement is the opposite of the supplied protocol/SAP statements for the same ten component comparisons. The main article also says analyses were prespecified in those documents before database lock and unblinding (DOC-001 PDF p.3).
- **Direct observation versus inference:** Directly observed are the opposing adjustment statements. It is not inferred whether adjusted values were calculated, omitted from the article, superseded in an unprovided amendment, or deliberately not used.
- **Human question:** Which prespecified/approved analysis-plan version governed the component P values, and were Benjamini-Hochberg-adjusted P values derived and, if so, where are they reported?
- **Relationship provenance:** S024, S029, and S038. These are one genuine proposal because they compare the same main-paper statement to the same planned component-P-value procedure, with two supporting locations.

### P-SP1-002 — Protocol’s stated count rationale for the primary composite does not reconcile with its displayed list

- **Proposed category:** Measure, label, or scale inconsistency.
- **Exact direct observations:** DOC-002 PDF p.15 displays ten separate bullets under “A composite of the following adverse perinatal outcomes.” On p.16, its secondary-outcome text calls these the individual components and states, “There are ten items because outcomes (i) and (viii) each contain two individual components.” The immediately preceding displayed list has ten bullets, including separate bullets for intrapartum stillbirth and 28-day neonatal mortality, and one bullet for neonatal-unit admission.
- **Reproducible comparison:** Treating the displayed bullets as the stated ten items, adding two components to each of two listed outcomes would not yield ten individual components. Conversely, if the author intended an eight-item list with two double components, that grouping is not identified consistently in the displayed list.
- **Direct observation versus inference:** This is a text-and-count inconsistency in a supplied endpoint definition. It does not assert that the executed composite, the main-paper ten-component list, or any observed effect estimate is incorrect.
- **Human question:** Which individual events were intended to be counted within outcomes (i) and (viii), and what is the authoritative ten-component definition used for the trial analysis?
- **Relationship provenance:** S034 (primary-composite model and definition context); source definition also supports main-paper S001 and S027.

## Relationship records

| Stable ID | Source-grounded pass-1 checks and result | Status |
|---|---|---|
| S001 | DOC-001 pp.1, 6-8: 83/1625 vs 84/1625, RR 1.02 (0.75-1.37), P=.91, absolute difference -0.1% (-1.6 to 1.5), and GEE twin-clustering label agree across abstract, Table 3, narrative, and Figure 2. RR contains 1; CI and P direction are compatible. | PASS_1_COMPLETE — NO PROPOSAL |
| S002 | DOC-001 p.7 Table 3: 5/1629 vs 3/1637, RR 1.67 (0.40-7.00), P=.48. Point direction, null-containing CI, and non-significant P are compatible under the stated GEE framework. | PASS_1_COMPLETE — NO PROPOSAL |
| S003 | DOC-001 p.7 Table 3: 12/1629 vs 5/1637, RR 2.28 (0.81-6.47), P=.12; footnote defines untested pH as no event. Direction, CI, P, and named missing-data rule agree. | PASS_1_COMPLETE — NO PROPOSAL |
| S004 | DOC-001 p.7: 1/1625 vs 1/1625, RR 0.94 (0.06-14.94), P=.96. Rounded RR/CI/P are compatible with sparse-event uncertainty; no contradictory occurrence. | PASS_1_COMPLETE — NO PROPOSAL |
| S005 | DOC-001 p.7: 2/1625 vs 1/1625, RR 1.87 (0.17-20.62), P=.61. Direction and null-containing CI/P agree. | PASS_1_COMPLETE — NO PROPOSAL |
| S006 | DOC-001 p.7: 50/1629 vs 61/1637, RR 0.85 (0.59-1.23), P=.39. Count direction, RR direction, CI, and P agree. | PASS_1_COMPLETE — NO PROPOSAL |
| S007 | DOC-001 p.7: 37/1629 vs 47/1637, RR 0.81 (0.53-1.25), P=.35. Count direction, RR direction, CI, and P agree. | PASS_1_COMPLETE — NO PROPOSAL |
| S008 | DOC-001 p.7: 1/1629 vs 3/1637, RR 0.33 (0.03-3.22), P=.34. Sparse counts, effect direction, CI, and P are compatible. | PASS_1_COMPLETE — NO PROPOSAL |
| S009 | DOC-001 p.7: 9/1629 vs 5/1637, RR 1.81 (0.61-5.39), P=.29. Direction, null containment, and P agree. | PASS_1_COMPLETE — NO PROPOSAL |
| S010 | DOC-001 pp.1, 6-7: 343/1629 vs 307/1637, RR 1.12 (0.98-1.29), P=.10. Abstract, Table 3, and narrative agree; CI contains 1 and direction agrees with counts. | PASS_1_COMPLETE — NO PROPOSAL |
| S011 | DOC-001 p.6 and DOC-004 p.2: imputed RR 1.01 (0.75-1.36) and Not-Done-adjusted RR 0.98 (0.73-1.31) are repeated consistently. GEE/GLM labels and the pH-missingness rules are supplied in eTable 1. | PASS_1_COMPLETE — NO PROPOSAL |
| S012 | DOC-001 p.8 Figure 2: overall GEE log-binomial RR 1.02 (0.75-1.37); exploratory subgroup GLM effects; all interaction tests P>.05. Figure label, null containment, and narrative interpretation agree. | PASS_1_COMPLETE — NO PROPOSAL |
| S013 | DOC-001 p.8 Figure 2: SGA yes RR .76 (.35-1.66), no 1.03 (.75-1.42). Both CIs contain 1; directions agree with displayed event proportions. | PASS_1_COMPLETE — NO PROPOSAL |
| S014 | DOC-001 p.8: multiple-pregnancy yes RR .36 (.09-1.49), no 1.05 (.77-1.42). CIs, directions, and exploratory-model label agree. | PASS_1_COMPLETE — NO PROPOSAL |
| S015 | DOC-001 p.8: preeclampsia yes RR .74 (.21-2.56), no 1.00 (.74-1.36). Both CI orderings and null containment agree with displayed counts. | PASS_1_COMPLETE — NO PROPOSAL |
| S016 | DOC-001 p.8: prior-cesarean yes RR 4.98 (.57-43.35), no .94 (.70-1.27). Wide intervals contain 1 and align with the sparse displayed counts. | PASS_1_COMPLETE — NO PROPOSAL |
| S017 | DOC-001 p.8: noncephalic yes RR .50 (.06-4.47), no .99 (.73-1.33). Event directions and null-containing CIs agree. | PASS_1_COMPLETE — NO PROPOSAL |
| S018 | DOC-001 p.8: fetal-anomaly yes RR 2.03 (.70-5.87), no .95 (.70-1.29). Direction and intervals agree with counts; no interaction contradiction. | PASS_1_COMPLETE — NO PROPOSAL |
| S019 | DOC-001 pp.7, 9 and DOC-004 p.3: interaction P=.16 in the article and .158 in eTable 2 are compatible rounding for the same site comparison; site counts and directions repeat exactly. | PASS_1_COMPLETE — NO PROPOSAL |
| S020 | DOC-001 p.8 Table 4: four infant-level RRs (1.11, 1.13, 1.14, .83) each have ordered CIs containing 1 and effect directions concordant with counts. Table footnote supplies GEE twin adjustment. | PASS_1_COMPLETE — NO PROPOSAL |
| S021 | DOC-001 p.8 Table 4: operative/factor RRs 1.10, 1.16, 1.04 have CIs containing 1; spontaneous vaginal birth RR .93 (.88-.99) has an ordered CI excluding 1 and agrees with lower sildenafil proportion. No P value is supplied, so none was inferred. | PASS_1_COMPLETE — NO PROPOSAL |
| S022 | DOC-001 p.8: mean differences -0.00 h (-.29 to .28) and -.03 h (-.14 to .07) have correctly ordered CIs containing 0; signs agree with displayed means. | PASS_1_COMPLETE — NO PROPOSAL |
| S023 | DOC-001 p.8: PPH RR 1.29 (1.03-1.60) and absolute difference 2.2% (.2-4.3) agree with 10.1% vs 7.9%; sparse maternal-outcome RRs have CIs containing 1. Narrative labels PPH hypothesis-generating rather than asserting a definitive effect. | PASS_1_COMPLETE — NO PROPOSAL |
| S024 | DOC-001 pp.3-4 states two-tailed P<.05 and no multiplicity adjustment. The threshold is consistent with reported unadjusted P presentation. Its conflict with supplied planned Benjamini-Hochberg adjustment is P-SP1-001. | PASS_1_COMPLETE — P-SP1-001 |
| S025 | DOC-001 p.3: 7.0% to 4.6% is a rounded presentation of the SAP/protocol 7.0% to 4.55%; alpha, power, and interim boundary are planning statements, not a result conflict. | PASS_1_COMPLETE — NO PROPOSAL |
| S026 | DOC-001 p.2 gives prior-trial 18.0% vs 36.7%, RR .49 (.33-.73), described as 51% relative-risk reduction. The arithmetic direction and approximate 1-.49=51% label agree; it is not a duplicate of the phase-3 result. | PASS_1_COMPLETE — NO PROPOSAL |
| S027 | DOC-001 pp.1, 6-7 conclusion of no significant primary/secondary-component effect matches Table 3 null-containing intervals and P values. PPH is separately described as a tertiary hypothesis-generating pattern. | PASS_1_COMPLETE — NO PROPOSAL |
| S028 | DOC-003 p.10: planned 3,200 women, alpha .05, power targets, 10% dropout, and 7% to 4.55% target agree with DOC-002 pp.9-10 and the rounded main-paper planning description. | PASS_1_COMPLETE — NO PROPOSAL |
| S029 | DOC-003 p.12 specifies RR, 95% CI, two-tailed P<.05, GEE log-binomial for neonatal outcomes, and Benjamini-Hochberg adjusted component P values. GEE/RR labels agree with main results; the adjustment statement contributes to P-SP1-001. | PASS_1_COMPLETE — P-SP1-001 |
| S030 | DOC-002 p.21 and DOC-003 pp.10-11: primary nominal P<.001 and mortality P<.0027. DOC-001 p.3’s P<.003 is compatible rounding of .0027; no interim-result claim is made. | PASS_1_COMPLETE — NO PROPOSAL |
| S031 | DOC-003 p.12 defines mITT as subjects with available outcome data and safety as treatment received. DOC-001 reports outcome-available denominators and treatment-received safety. The sources do not supply a final mITT inclusion/exclusion reconciliation sufficient to infer a mismatch. | PASS_1_COMPLETE — NO PROPOSAL; missing final dataset derivation |
| S032 | DOC-003 p.12 names chi-square/trend, t/Wilcoxon, and conditional exact tests. It supplies no matched reported statistic for a mechanical reproduction, and no conflicting test label occurs in results. | PASS_1_COMPLETE — NO PROPOSAL; test selection per endpoint not reported |
| S033 | DOC-003 p.12 specifies GEE exchangeable clustering for twins and independent-baby comparison. DOC-001 Table 3/Figure 2 labels GEE for the relevant neonatal results; no conflicting covariance or analysis-unit label is printed. | PASS_1_COMPLETE — NO PROPOSAL |
| S034 | DOC-003 p.13’s GEE log-binomial, RR/CI, and pH Not-Done-as-no-event plan agree with DOC-001 Table 3 and DOC-004 eTable 1. The protocol’s internally inconsistent ten-item rationale is P-SP1-002. | PASS_1_COMPLETE — P-SP1-002 |
| S035 | DOC-003 pp.13-14 specifies twin-stratified imputation, nine-component, no-cluster, and Not-Done-indicator sensitivities. DOC-004 p.2 reports each corresponding sensitivity with matching model footnotes and coherent CIs/P values. | PASS_1_COMPLETE — NO PROPOSAL |
| S036 | DOC-003 p.13 specifies prognostic covariates and robust-Poisson fallback. Main-paper narrative reports an adjusted primary sensitivity without its covariate coefficient table; the absence of that table does not establish a conflicting implementation. | PASS_1_COMPLETE — NO PROPOSAL; adjustment detail not fully reported |
| S037 | DOC-003 p.14 specifies six interaction log-binomial GLMs, unadjusted, no GEE. DOC-001 Figure 2 presents the same six groups and model label; all interaction P values are reported only as P>.05, with no contrary value supplied. | PASS_1_COMPLETE — NO PROPOSAL |
| S038 | DOC-003 p.25 proposed Table 11 includes a Benjamini-Hochberg adjusted-P column. Actual DOC-001 Table 3 prints unadjusted P values and p.4 says no adjustment; this is the same direct comparison as P-SP1-001. | PASS_1_COMPLETE — P-SP1-001 |
| S039 | DOC-003 p.26 is an unfilled robust-Poisson proposed table. No results-paper row purports to be that table; no point estimate or P value can be compared without inventing an estimand mapping. | PASS_1_COMPLETE — NO PROPOSAL |
| S040 | DOC-003 p.27 proposed GEE sensitivity shell is consistent with populated DOC-004 p.2 eTable 1 labels/results. The shell contains placeholders, not competing estimates. | PASS_1_COMPLETE — NO PROPOSAL |
| S041 | DOC-003 pp.27-28 proposed neonatal GEE and maternal log-binomial/t-test output is consistent with DOC-001 Tables 3-4 model labels. No unreported P value or SE was inferred. | PASS_1_COMPLETE — NO PROPOSAL |
| S042 | DOC-003 p.29 proposed subgroup log-binomial shell matches DOC-001 Figure 2’s exploratory subgroup GLM description. Placeholder cells are not results. | PASS_1_COMPLETE — NO PROPOSAL |
| S043 | DOC-002 p.9 historical phase-2 RR .49 (.33-.73), P=.0004, NNT 5 (3-11), and RR .48 (.31-.75), P=.0009 are compatible with their CIs/directions; main DOC-001 repeats the former RR/CI and 51% reduction. No display-zero P is present. | PASS_1_COMPLETE — NO PROPOSAL |
| S044 | DOC-004 p.2: imputed GEE composite RR 1.01 (.75-1.36), P=.943. CI contains 1, P is compatible, and counts 85/1625 vs 87/1625 support the direction. | PASS_1_COMPLETE — NO PROPOSAL |
| S045 | DOC-004 p.2: imputed pH RR 1.62 (.68-3.85), P=.276; counts 14/1629 vs 8/1637. Direction, CI, P, twin-stratified imputation label, and missingness categories agree. | PASS_1_COMPLETE — NO PROPOSAL |
| S046 | DOC-004 p.2: nine-component GEE RR .96 (.70-1.31), P=.796 and ten-component GLM RR .99 (.74-1.33), P=.937. Each CI/P is compatible and model labels distinguish the analyses. | PASS_1_COMPLETE — NO PROPOSAL |
| S047 | DOC-004 p.2: Not-Done-adjusted GLM RR .98 (.73-1.31), P=.882 and imputed adjusted GLM RR .97 (.73-1.30), P=.844. Both have ordered null-containing CIs; no conflict with stated indicator/imputation labels. | PASS_1_COMPLETE — NO PROPOSAL |
| S048 | DOC-004 p.3: site-primary RRs .67 (.36-1.25), P=.209 and 1.11 (.80-1.55), P=.537; interaction P=.158. Counts, directions, CIs/P values, and main-paper rounded interaction P=.16 agree. | PASS_1_COMPLETE — NO PROPOSAL |
| S049 | DOC-004 p.3: site Apgar, pH, and unit-admission rows have ordered CIs, direction-consistent counts, and interaction P=.676, .315, .931. Sparse cells are labelled with the table’s log-binomial model; no incompatible inference found. | PASS_1_COMPLETE — NO PROPOSAL |
| S050 | DOC-004 p.4: respiratory-support interaction P=.015; Mater RR .30 (.11-.80), P=.016 and other-sites RR 1.07 (.66-1.75), P=.779. CI/P/directions are compatible; this interaction differs from the main paper’s six prespecified subgroups and is not misrepresented there. | PASS_1_COMPLETE — NO PROPOSAL |
| S051 | DOC-004 pp.4-5: all listed secondary/tertiary site interaction P values (.214, .591, .718, .726, .815, .559, .927) correspond to the displayed within-site RRs/counts. No incompatible repeated result was identified. | PASS_1_COMPLETE — NO PROPOSAL |
| S052 | DOC-004 p.5: spontaneous-birth interaction .450 and PPH interaction .036; other-sites PPH RR 1.63 (1.19-2.24), P=.002. Point/CI/P directions are compatible. Other-sites spontaneous-birth RR .91 (.82-1.00), P=.050 is a rounded borderline result, not an endpoint-order conflict. | PASS_1_COMPLETE — NO PROPOSAL |
| S053 | DOC-004 p.6: safety results use Fisher exact tests; printed P=.343, .999, .062, .624, and .999 values accord with the displayed sparse counts. No P=0 or p=.000 display occurs; rows with both groups zero have no P value. | PASS_1_COMPLETE — NO PROPOSAL |

## Cross-location and diagnostic notes

- `DISPLAY_ZERO_NOT_CANDIDATE`: **0** relationships contained a printed `P = 0`, `p = 0.000`, or equivalent. Several rows contain zero event counts and several use P=.999; neither is a display-zero P-value candidate.
- The SAP title page says `Draft Version 1.2`, dated October 25, 2024, while its revision table describes v1.2 as “SAP finalised” on that date (DOC-003 pp.1, 4). DOC-001 p.4 says data were analyzed October 24, 2024 and DOC-001 p.3 says the SAP was prespecified before database lock/unblinding. This is retained as a chronology limitation, not a proposal: the supplied sources do not give database-lock/unblinding time or establish whether “data were analyzed” denotes an unblinded final analysis.
- Protocol/SAP planned-table blanks and omitted result details (for example a full adjusted-model coefficient table, endpoint-specific exact-test choice, NNT, degrees of freedom, and variance estimator) were not treated as contradictions. They constrain mechanical compatibility checks.

## Completion marker

**PASS_1_COMPLETE**

- Stable relationships covered: **53/53** (S001-S053).
- Distinct pass-1 proposals: **2** (P-SP1-001 and P-SP1-002; no stable C IDs assigned).
- Display-zero P-value records: **0**.
- Limitations: no raw model objects, unrounded estimates, SEs, covariance matrices, degrees of freedom, database-lock/unblinding timestamp, endpoint-specific test-selection log, or complete adjusted-model output are supplied. No such quantity was inferred from convention.
