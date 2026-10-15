# Complete statistical relationship inventory — both passes

All263 registered relationships receive PASS_1_COMPLETE and PASS_2_COMPLETE through fresh distinct agents. Reserved namespace gaps are not missing records. Pass1 records retain their original provenance; active pass2 follows below. The original PLAN pass2 artifact is preserved separately and replaced by three bounded active shards.

<!-- Complete pass1 inventory: main -->

# Statistical Relationship Inventory — Main-Paper Pass 1

Runtime agent: /root/stat1_main. Model: gpt-6.1-sol. Reasoning effort: high. Fresh pass-1 primary-main shard only. Scope: DOC-001 REPORT, physical PDF pages1–14; fresh map MAIN001–MAIN116. Sources preserved; no prior review conclusions used. All110 records below are PASS_1_COMPLETE. Statistical pass2 must use a distinct fresh agent.

Methods and inferential outcomes are disjoint records; each outcome contributes three families (group estimates, between-group estimates/test, derived estimates). Every triple lists every tuple in fixed PT/HC/UC or PT–UC/HC–UC/HC–PT order. Total270 estimate–95%CI tuples,30 omnibus tests,27 NNTs,63 SMDs. The outcome records explicitly cover all three times and all contrasts. No result tuple is sampled.

Full exact printed input transcription and source page links: [fresh main map](../extraction/main_quantitative_evidence.md). Direct pages 9–11 visually inspected; page 7 narrative directly inspected; fresh native PDF text used as locator for all 14 pages. Inferential categories absent from main are recorded in S020.

### S001

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN001/009/014/034; pp.1–5.
- Relationship: Randomization and analysis units.
- Printed inputs/method: Individual 1:1:1 randomized; strata sex, baseline severity, site, rural/underserved; GEE highest-level within-person or health-coach clustering; 12 coaches.
- Pass1 checks and conclusion: Design and correlation units are explicitly distinguished. No independent-samples assumption imposed; no clustering contradiction found.
- Pass2: PENDING

### S002

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN001/003/018/020/027/030–035; pp.1,4,5,8–11.
- Relationship: Analysis population and missingness denominators.
- Printed inputs/method: 2333 allocated minus 2 EHR-ineligible UC =2331 eligible analysis population; 776/778/777; any-follow-up643/690/703; inverse-probability weighting for no follow-up.
- Pass1 checks and conclusion: Counts reconcile with stated eligible ITT principle and weighting. Table model contributor counts differ from target randomized population without a conflict.
- Pass2: PENDING

### S003

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN002/004/005/011/080; pp.1–4,7–9.
- Relationship: Primary outcome definition and decision direction.
- Printed inputs/method: ≥30% decrease from baseline severity, 0–10 higher=worse, 3mo primary; 6/12 secondary. Active-vs-UC RR>1 favors improvement.
- Pass1 checks and conclusion: Scale, threshold, contrast and direction agree; superiority claim checked against all primary RRs. No noninferiority or equivalence rule applies.
- Pass2: PENDING

### S004

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN012/111–113; pp.3–4,7,11.
- Relationship: Secondary outcome construction and direction.
- Printed inputs/method: Intensity4 and interference7 items; PROMIS higher=better; PGIC1–7 higher=worse; all3/6/12mo.
- Pass1 checks and conclusion: Continuous changes and PGIC status-since-start distinguished; coherent stated linear analysis not questioned. Wording about PGIC change is not a new numerical result.
- Pass2: PENDING

### S005

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN013; p.4 Sample Size.
- Relationship: Sample size and power inputs.
- Printed inputs/method: 2331=777×3; 90% power; UC15%, active22.5%=15%+7.5%; RR1.5;80%retention;10000 modified-Poisson simulations; Fisher LSD.
- Pass1 checks and conclusion: 777×3=2331 and .225/.15=1.5 reproduce. Exact simulation power cannot be reconstructed without simulation data-generating specification, seed and fit/gate rules; no contradictory printed sample size established. No preferred method imposed.
- Pass2: PENDING

### S006

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN014/019/110; pp.4,9.
- Relationship: Primary GEE and test method.
- Printed inputs/method: Modified Poisson, independent working correlation, robust sandwich standard error, time/group/interaction; Wald omnibus across3 groups; two-sidedα=.05.
- Pass1 checks and conclusion: Stated model coherent with repeated binary measures and coaching cluster. No printed numeric test statistic or standard error; do not infer degrees of freedom or sandwich corrections.
- Pass2: PENDING

### S007

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN015/017; p.4.
- Relationship: Adjustment and secondary baseline variables.
- Printed inputs/method: Baseline severity, sex, site, rural/underserved, multisite pain, mental health; same structure plus secondary baseline.
- Pass1 checks and conclusion: Reported covariates are defined, model scope coherent. Plan comparisons assigned distinct shard; source does not require replacing adjustment with crude estimates.
- Pass2: PENDING

### S008

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN015/110/111; pp.4,9,11.
- Relationship: Adjusted group predictions and target estimand.
- Printed inputs/method: Covariates centered at mean values across participants; randomized population average effects.
- Pass1 checks and conclusion: All table tuples explicitly model-adjusted; crude ratios not substitute estimators. Predicted binary proportions and RRs reproduce their algebra within precision.
- Pass2: PENDING

### S009

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN017/111; pp.4,11.
- Relationship: Continuous model and contrast method.
- Printed inputs/method: Linear regression/GEE adjusted group mean, differences and SMD at eachtime; group/time/interaction structure.
- Pass1 checks and conclusion: All21 continuous rows checked for additive group contrast consistency with half-unit rounding; no qualifying group-mean/MD discrepancy.
- Pass2: PENDING

### S010

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN017/111; pp.4,11.
- Relationship: SMD definition and shared denominator.
- Printed inputs/method: Each SMD=adjusted MD / SD(change in UC) at the given outcome/time; positive common SD across3 contrasts; SD value unprinted.
- Pass1 checks and conclusion: Check sign and additive contrast identity without inferring SD magnitude; F-ST1-004. All63 SMD intervals checked; containment F-ST1-002, descending order F-ST1-003.
- Pass2: PENDING

### S011

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN016/110; pp.4,9.
- Relationship: NNT definition and interval rule.
- Printed inputs/method: NNT=1/adjusted response-proportion difference; if RD CI includes0, NNT includes infinity and negative NNH branch.
- Pass1 checks and conclusion: All27 points/intervals checked. F-ST1-001 containment; F-ST1-005 reciprocal display discrepancy; F-ST1-006 finite-NNT versus null-containing RR intervals. Exact RD CI method remains unprinted; alternatives retained.
- Pass2: PENDING

### S012

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN018; p.4.
- Relationship: Outcome imputation and weighting.
- Printed inputs/method: Nonignorable pattern-mixture for≥1follow-up; inverse probability missingness weighting for no follow-up; sensitivity analyses planned/conducted.
- Pass1 checks and conclusion: Sequential observation groups defined and nonoverlapping; no logical contradiction found from main. Supplement inferential details assigned report shard.
- Pass2: PENDING

### S013

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN018; p.4.
- Relationship: Missing covariate data.
- Printed inputs/method: Mean imputation stated for missing covariates.
- Pass1 checks and conclusion: Explicit internally coherent choice; categorical encoding details absent without a conflicting number or statement; not a finding.
- Pass2: PENDING

### S014

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN019/110/111; pp.4,9,11.
- Relationship: Confidence, sidedness and significance.
- Printed inputs/method: All tests2-sidedα=.05; 95%CIs; omnibus Wald across3groups.
- Pass1 checks and conclusion: No omnibus P treated as pairwise P; no inferred covariance or degrees of freedom. Each row's null pattern reviewed at stated level.
- Pass2: PENDING

### S015

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN013/019/110/111; pp.4,9,11.
- Relationship: Multiplicity and omnibus gate.
- Printed inputs/method: Fisher least significant difference; pairwise comparisons onlyif omnibusP<.05.
- Pass1 checks and conclusion: All30 row gates reviewed:29 printedP<.05; physical6=.05 has rounding interval[.045,.055], exact gate cannot be determined. No interim/stopping boundary printed in main.
- Pass2: PENDING

### S016

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN002/004/005/080; pp.1–2,7–9.
- Relationship: Abstract and Key Points primary inference.
- Printed inputs/method: HC32.0(29.3–35.0)%, PT26.6(23.4–30.2)%, UC20.8(18.0–24.0)%; RR1.54/1.28/1.20 with95%CIs excluding1.
- Pass1 checks and conclusion: All estimates, CIs, contrast direction and 3mo superiority match; no numerical mismatch between abstract and primary row.
- Pass2: PENDING

### S017

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN006/080–082/114/116; pp.1,7–9,12.
- Relationship: Severity longitudinal inference.
- Printed inputs/method: Bothactive-vs-UC significant at3/6/12; HC-vs-PT3mo significant,6/12not significant.
- Pass1 checks and conclusion: All9RR CIs have asserted null patterns. Figure series/95%CIs agree visually and display no additional printed estimate/test tuples.
- Pass2: PENDING

### S018

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN006/022/089–109/116; pp.1,7–12.
- Relationship: Secondary inference narrative and SMD copies.
- Printed inputs/method: Narrative3mo severity SMD−.26PT/−.36HC vsTable3−.25/−.34. Overallpatterns described significant benefits pain/function.
- Pass1 checks and conclusion: Copy gaps0/.01 relative0/.0294 meet display precision; no finding. Broad overall-pattern wording not read as a universal everycontrast test; excluded wording observation recorded once.
- Pass2: PENDING

### S019

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN035/114; pp.5,8–9.
- Relationship: Figure2 graph and contributor counts.
- Printed inputs/method: 3/6/12 severity adjusted means and95%CIs; UC621/622/639, PT542/547/583, HC635/621/639.
- Pass1 checks and conclusion: Every plotted group/time and whisker compared visually withTable2. Counts agree withFigure1; time-specific observations differ fromany-follow-up counts by definition.
- Pass2: PENDING

### S020

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN007/008/023–079/112/113/115/116; pp.2–8,12–14.
- Relationship: Remaining pages and nonapplicable methods.
- Printed inputs/method: BaselineTable1 has SD/IQR notCIs and noinferential P; adverse outcomes counts/no formaltests; reference-onlypp.13–14.
- Pass1 checks and conclusion: Numeric-only totals delegated numeric checker; no inferential tuples omitted. No HR/OR/rate/person-time, NI/equivalence, numeric interim/stopping, numeric standard error or numeric test statistic in main. BPI missing-item wording screened once.
- Pass2: PENDING

### S021

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN080, Severity 3 mo — group adjusted estimates.
- Printed tuples: 26.6(23.4–30.2) / 32.0(29.3–35.0) / 20.8(18.0–24.0).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S022

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN080, Severity 3 mo — between-group estimates and omnibus test.
- Printed tuples: 1.28(1.06–1.55) / 1.54(1.30–1.82) / 1.20(1.03–1.40).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 RR estimates lies inside its ordered95%CI; RR directions and ratios of adjusted proportions reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S023

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN080, Severity 3 mo — NNT construction and intervals.
- Printed tuples: 18(10–71) / 9(7–14) / 19(11–102).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 NNT tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Reciprocal points reconcile or fall within display precision. No null-containing-RR/finite-NNT pattern requiring further review.
- Pass2: PENDING

### S024

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN081, Severity 6 mo — group adjusted estimates.
- Printed tuples: 32.9(29.5–36.7) / 37.1(34.1–40.5) / 22.9(20.0–26.1).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S025

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN081, Severity 6 mo — between-group estimates and omnibus test.
- Printed tuples: 1.44(1.21–1.70) / 1.62(1.39–1.90) / 1.13(0.98–1.30).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 RR estimates lies inside its ordered95%CI; RR directions and ratios of adjusted proportions reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S026

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN081, Severity 6 mo — NNT construction and intervals.
- Printed tuples: 10(7–19) / 8(6–11) / 24(12–186).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 NNT tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. HC–UC reciprocal point differs beyond half-unit tolerance: F-ST1-005. Finite HC–PT NNT CI accompanies RR CI including1: F-ST1-006; RD interval method remains unspecified.
- Pass2: PENDING

### S027

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN082, Severity 12 mo — group adjusted estimates.
- Printed tuples: 35.9(32.4–39.7) / 38.3(36.8–39.9) / 27.1(24.1–30.5).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S028

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN082, Severity 12 mo — between-group estimates and omnibus test.
- Printed tuples: 1.32(1.13–1.54) / 1.41(1.25–1.59) / 1.07(0.96–1.19).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 RR estimates lies inside its ordered95%CI; RR directions and ratios of adjusted proportions reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S029

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN082, Severity 12 mo — NNT construction and intervals.
- Printed tuples: 12(8–26) / 9(7–13) / 41(17–76).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 NNT tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Reciprocal points reconcile or fall within display precision. Finite HC–PT NNT CI accompanies RR CI including1: F-ST1-006; RD interval method remains unspecified.
- Pass2: PENDING

### S030

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN083, Intensity 3 mo — group adjusted estimates.
- Printed tuples: 24.3(21.2–27.8) / 27.0(24.0–30.5) / 17.7(15.1–20.7).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S031

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN083, Intensity 3 mo — between-group estimates and omnibus test.
- Printed tuples: 1.37(1.12–1.69) / 1.53(1.26–1.86) / 1.11(0.93–1.33).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 RR estimates lies inside its ordered95%CI; RR directions and ratios of adjusted proportions reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S032

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN083, Intensity 3 mo — NNT construction and intervals.
- Printed tuples: 16(10–43) / 11(8–20) / 37(14–57).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 NNT tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Reciprocal points reconcile or fall within display precision. Finite HC–PT NNT CI accompanies RR CI including1: F-ST1-006; RD interval method remains unspecified.
- Pass2: PENDING

### S033

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN084, Intensity 6 mo — group adjusted estimates.
- Printed tuples: 26.9(23.7–30.5) / 31.8(28.3–35.7) / 21.1(18.3–24.3).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S034

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN084, Intensity 6 mo — between-group estimates and omnibus test.
- Printed tuples: 1.27(1.06–1.54) / 1.51(1.26–1.80) / 1.18(1.00–1.40).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 RR estimates lies inside its ordered95%CI; RR directions and ratios of adjusted proportions reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S035

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN084, Intensity 6 mo — NNT construction and intervals.
- Printed tuples: 18(10–76) / 10(7–17) / 21(11–5524).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 NNT tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Reciprocal points reconcile or fall within display precision. No null-containing-RR/finite-NNT pattern requiring further review.
- Pass2: PENDING

### S036

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN085, Intensity 12 mo — group adjusted estimates.
- Printed tuples: 32.1(28.7–35.8) / 33.7(31.2–36.3) / 26.4(23.4–29.8).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S037

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN085, Intensity 12 mo — between-group estimates and omnibus test.
- Printed tuples: 1.21(1.03–1.43) / 1.28(1.11–1.47) / 1.05(0.92–1.20).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 RR estimates lies inside its ordered95%CI; RR directions and ratios of adjusted proportions reconcile allowing printed precision. OmnibusP=.003 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S038

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN085, Intensity 12 mo — NNT construction and intervals.
- Printed tuples: 18(10–106) / 14(9–31) / 63(18–38).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 NNT tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Containment does not reconcile for contrast3: F-ST1-001. Endpoint order reconciles. Reciprocal points reconcile or fall within display precision. Finite HC–PT NNT CI accompanies RR CI including1: F-ST1-006; RD interval method remains unspecified.
- Pass2: PENDING

### S039

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN086, Interference 3 mo — group adjusted estimates.
- Printed tuples: 30.6(27.3–34.4) / 35.6(33.7–37.6) / 23.4(20.5–26.8).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S040

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN086, Interference 3 mo — between-group estimates and omnibus test.
- Printed tuples: 1.31(1.10–1.55) / 1.52(1.32–1.75) / 1.16(1.02–1.32).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 RR estimates lies inside its ordered95%CI; RR directions and ratios of adjusted proportions reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S041

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN086, Interference 3 mo — NNT construction and intervals.
- Printed tuples: 14(9–40) / 9(7–12) / 21(12–100).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 NNT tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Reciprocal points reconcile or fall within display precision. No null-containing-RR/finite-NNT pattern requiring further review.
- Pass2: PENDING

### S042

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN087, Interference 6 mo — group adjusted estimates.
- Printed tuples: 37.0(33.5–40.9) / 40.9(37.0–45.1) / 24.3(21.3–27.6).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S043

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN087, Interference 6 mo — between-group estimates and omnibus test.
- Printed tuples: 1.52(1.30–1.79) / 1.68(1.43–1.98) / 1.10(0.96–1.27).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 RR estimates lies inside its ordered95%CI; RR directions and ratios of adjusted proportions reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S044

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN087, Interference 6 mo — NNT construction and intervals.
- Printed tuples: 8(6–13) / 7(5–9) / 26(11–67).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 NNT tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. HC–UC reciprocal point differs beyond half-unit tolerance: F-ST1-005. Finite HC–PT NNT CI accompanies RR CI including1: F-ST1-006; RD interval method remains unspecified.
- Pass2: PENDING

### S045

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN088, Interference 12 mo — group adjusted estimates.
- Printed tuples: 39.6(36.1–43.5) / 42.3(40.6–44.0) / 30.6(27.4–34.2).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S046

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN088, Interference 12 mo — between-group estimates and omnibus test.
- Printed tuples: 1.29(1.12–1.49) / 1.38(1.23–1.55) / 1.07(0.97–1.18).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 RR estimates lies inside its ordered95%CI; RR directions and ratios of adjusted proportions reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S047

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN088, Interference 12 mo — NNT construction and intervals.
- Printed tuples: 12(8–25) / 9(7–13) / 39(16–79).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 NNT tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Reciprocal points reconcile or fall within display precision. Finite HC–PT NNT CI accompanies RR CI including1: F-ST1-006; RD interval method remains unspecified.
- Pass2: PENDING

### S048

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN089, Severity 3 mo — group adjusted estimates.
- Printed tuples: -1.2(-1.3 to-1.0) / -1.2(-1.3 to-1.1) / -0.8(-0.9 to-0.6).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S049

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN089, Severity 3 mo — between-group estimates and omnibus test.
- Printed tuples: -0.4(-0.6 to-0.2) / -0.4(-0.6 to-0.3) / -0.0(-0.2 to 0.1).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S050

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN089, Severity 3 mo — SMD construction and intervals.
- Printed tuples: -0.25(-0.28 to-0.02) / -0.34(-0.36 to-0.13) / -0.13(-0.15 to 0.08).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING

### S051

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN090, Severity 6 mo — group adjusted estimates.
- Printed tuples: -1.3(-1.4 to-1.1) / -1.4(-1.5 to-1.3) / -0.9(-1.0 to-0.8).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S052

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN090, Severity 6 mo — between-group estimates and omnibus test.
- Printed tuples: -0.4(-0.6 to-0.2) / -0.5(-0.7 to-0.4) / -0.1(-0.3 to 0.1).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S053

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN090, Severity 6 mo — SMD construction and intervals.
- Printed tuples: -0.26(-0.34 to-0.08) / -0.36(-0.43 to-0.19) / -0.12(-0.19 to 0.04).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common-SD/additivity discrepancies fall within display-precision tolerance; excluded row recorded.
- Pass2: PENDING

### S054

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN091, Severity 12 mo — group adjusted estimates.
- Printed tuples: -1.5(-1.6 to-1.3) / -1.4(-1.6 to-1.3) / -1.1(-1.2 to-0.9).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S055

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN091, Severity 12 mo — between-group estimates and omnibus test.
- Printed tuples: -0.4(-0.6 to-0.2) / -0.4(-0.6 to-0.2) / 0.0(-0.2 to 0.2).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S056

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN091, Severity 12 mo — SMD construction and intervals.
- Printed tuples: -0.25(-0.24 to 0.01) / -0.36(-0.35 to-0.12) / -0.11(-0.11 to 0.12).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Containment does not reconcile for contrast1,2: F-ST1-002. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING

### S057

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN092, Intensity 3 mo — group adjusted estimates.
- Printed tuples: -0.9(-1.0 to-0.8) / -0.9(-1.0 to-0.8) / -0.6(-0.7 to-0.5).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S058

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN092, Intensity 3 mo — between-group estimates and omnibus test.
- Printed tuples: -0.3(-0.5 to-0.1) / -0.3(-0.5 to-0.2) / -0.0(-0.2 to 0.2).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S059

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN092, Intensity 3 mo — SMD construction and intervals.
- Printed tuples: -0.21(-0.21 to-0.01) / -0.29(-0.30 to-0.11) / -0.08(-0.09 to 0.09).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING

### S060

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN093, Intensity 6 mo — group adjusted estimates.
- Printed tuples: -1.0(-1.1 to-0.9) / -1.1(-1.2 to-1.0) / -0.7(-0.9 to-0.6).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S061

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN093, Intensity 6 mo — between-group estimates and omnibus test.
- Printed tuples: -0.2(-0.4 to-0.1) / -0.3(-0.5 to-0.2) / -0.1(-0.3 to 0.1).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S062

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN093, Intensity 6 mo — SMD construction and intervals.
- Printed tuples: -0.17(-0.23 to-0.06) / -0.27(-0.32 to-0.17) / -0.04(-0.10 to 0.05).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING

### S063

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN094, Intensity 12 mo — group adjusted estimates.
- Printed tuples: -1.1(-1.3 to-1.0) / -1.1(-1.3 to-1.0) / -0.9(-1.0 to-0.8).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S064

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN094, Intensity 12 mo — between-group estimates and omnibus test.
- Printed tuples: -0.2(-0.4 to-0.1) / -0.2(-0.4 to-0.1) / 0.0(-0.2 to 0.2).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=.01 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S065

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN094, Intensity 12 mo — SMD construction and intervals.
- Printed tuples: -0.16(-0.16 to 0.00) / -0.27(-0.26 to-0.12) / -0.03(-0.03 to 0.11).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Containment does not reconcile for contrast2: F-ST1-002. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING

### S066

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN095, Interference 3 mo — group adjusted estimates.
- Printed tuples: -1.3(-1.4 to-1.1) / -1.4(-1.5 to-1.2) / -0.8(-1.0 to-0.7).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S067

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN095, Interference 3 mo — between-group estimates and omnibus test.
- Printed tuples: -0.5(-0.7 to-0.3) / -0.5(-0.7 to-0.3) / -0.1(-0.3 to 0.2).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S068

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN095, Interference 3 mo — SMD construction and intervals.
- Printed tuples: -0.25(-0.28 to-0.03) / -0.34(-0.37 to-0.13) / -0.13(-0.15 to 0.07).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING

### S069

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN096, Interference 6 mo — group adjusted estimates.
- Printed tuples: -1.5(-1.6 to-1.3) / -1.6(-1.8 to-1.4) / -1.0(-1.1 to-0.8).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S070

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN096, Interference 6 mo — between-group estimates and omnibus test.
- Printed tuples: -0.5(-0.7 to-0.3) / -0.6(-0.8 to-0.4) / -0.1(-0.4 to 0.1).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S071

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN096, Interference 6 mo — SMD construction and intervals.
- Printed tuples: -0.27(-0.34 to-0.08) / -0.37(-0.44 to-0.19) / -0.14(-0.21 to 0.04).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING

### S072

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN097, Interference 12 mo — group adjusted estimates.
- Printed tuples: -1.6(-1.8 to-1.5) / -1.6(-1.8 to-1.5) / -1.2(-1.3 to-1.0).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S073

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN097, Interference 12 mo — between-group estimates and omnibus test.
- Printed tuples: -0.5(-0.7 to-0.3) / -0.5(-0.7 to-0.3) / 0.0(-0.2 to 0.2).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S074

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN097, Interference 12 mo — SMD construction and intervals.
- Printed tuples: -0.26(-0.25 to 0.01) / -0.37(-0.36 to-0.11) / -0.12(-0.12 to 0.12).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Containment does not reconcile for contrast1,2: F-ST1-002. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING

### S075

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN098, Social 3 mo — group adjusted estimates.
- Printed tuples: 1.5(1.0 to 2.1) / 2.2(1.7 to 2.7) / 0.7(0.3 to 1.2).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S076

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN098, Social 3 mo — between-group estimates and omnibus test.
- Printed tuples: 0.8(0.0 to 1.5) / 1.5(0.8 to 2.2) / 0.7(-0.0 to 1.4).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S077

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN098, Social 3 mo — SMD construction and intervals.
- Printed tuples: 0.12(0.23 to 0.11) / 0.01(0.12 to-0.00) / 0.20(0.29 to 0.19).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Printed endpoints descend for contrasts1,2,3: F-ST1-003. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING

### S078

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN099, Social 6 mo — group adjusted estimates.
- Printed tuples: 2.2(1.6 to 2.8) / 2.5(2.0 to 3.1) / 1.0(0.5 to 1.5).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S079

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN099, Social 6 mo — between-group estimates and omnibus test.
- Printed tuples: 1.2(0.4 to 1.9) / 1.5(0.8 to 2.2) / 0.3(-0.4 to 1.1).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S080

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN099, Social 6 mo — SMD construction and intervals.
- Printed tuples: 0.18(0.23 to 0.05) / 0.06(0.11 to-0.06) / 0.26(0.30 to 0.15).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Printed endpoints descend for contrasts1,2,3: F-ST1-003. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING

### S081

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN100, Social 12 mo — group adjusted estimates.
- Printed tuples: 2.6(2.0 to 3.2) / 2.7(2.2 to 3.3) / 1.4(0.8 to 1.9).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S082

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN100, Social 12 mo — between-group estimates and omnibus test.
- Printed tuples: 1.3(0.5 to 2.1) / 1.4(0.6 to 2.1) / 0.1(-0.7 to 0.9).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S083

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN100, Social 12 mo — SMD construction and intervals.
- Printed tuples: 0.19(0.21 to 0.01) / 0.07(0.09 to-0.10) / 0.27(0.28 to 0.12).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Printed endpoints descend for contrasts1,2,3: F-ST1-003. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING

### S084

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN101, Physical 3 mo — group adjusted estimates.
- Printed tuples: 1.4(1.1 to 1.8) / 1.7(1.4 to 2.1) / 1.0(0.7 to 1.4).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S085

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN101, Physical 3 mo — between-group estimates and omnibus test.
- Printed tuples: 0.4(-0.1 to 0.9) / 0.7(0.2 to 1.2) / 0.3(-0.2 to 0.8).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=.02 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S086

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN101, Physical 3 mo — SMD construction and intervals.
- Printed tuples: 0.09(0.16 to 0.07) / -0.02(0.05 to-0.04) / 0.16(0.22 to 0.15).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Printed endpoints descend for contrasts1,2,3: F-ST1-003. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING

### S087

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN102, Physical 6 mo — group adjusted estimates.
- Printed tuples: 2.0(1.6 to 2.4) / 1.8(1.4 to 2.1) / 1.4(1.0 to 1.7).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S088

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN102, Physical 6 mo — between-group estimates and omnibus test.
- Printed tuples: 0.6(0.1 to 1.2) / 0.4(-0.1 to 0.9) / -0.3(-0.8 to 0.3).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=.05 is a3-group Wald test, not a pairwiseP. Printed.05 gate has unresolved rounding, recorded once as excluded display precision. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S089

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN102, Physical 6 mo — SMD construction and intervals.
- Printed tuples: 0.15(0.09 to-0.06) / 0.02(-0.03 to-0.18) / 0.22(0.16 to 0.05).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Containment does not reconcile for contrast1,2,3: F-ST1-002. Printed endpoints descend for contrasts1,2,3: F-ST1-003. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING

### S090

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN103, Physical 12 mo — group adjusted estimates.
- Printed tuples: 2.2(1.8 to 2.7) / 2.1(1.7 to 2.5) / 1.3(0.9 to 1.7).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S091

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN103, Physical 12 mo — between-group estimates and omnibus test.
- Printed tuples: 0.9(0.3 to 1.5) / 0.8(0.2 to 1.4) / -0.1(-0.7 to 0.5).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=.004 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S092

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN103, Physical 12 mo — SMD construction and intervals.
- Printed tuples: 0.20(0.18 to-0.03) / 0.07(0.04 to-0.16) / 0.27(0.25 to 0.09).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Containment does not reconcile for contrast1,2,3: F-ST1-002. Printed endpoints descend for contrasts1,2,3: F-ST1-003. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING

### S093

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN104, PGIC pain 3 mo — group adjusted estimates.
- Printed tuples: 2.2(2.1 to 2.3) / 2.0(1.9 to 2.1) / 2.9(2.8 to 3.0).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S094

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN104, PGIC pain 3 mo — between-group estimates and omnibus test.
- Printed tuples: -0.7(-0.8 to-0.6) / -0.9(-1.0 to-0.8) / -0.2(-0.3 to-0.1).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S095

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN104, PGIC pain 3 mo — SMD construction and intervals.
- Printed tuples: -0.62(-0.81 to-0.19) / -0.62(-0.76 to-0.25) / -0.37(-0.51 to-0.05).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING

### S096

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN105, PGIC pain 6 mo — group adjusted estimates.
- Printed tuples: 2.2(2.1 to 2.3) / 2.1(2.0 to 2.2) / 2.8(2.7 to 2.9).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S097

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN105, PGIC pain 6 mo — between-group estimates and omnibus test.
- Printed tuples: -0.6(-0.8 to-0.5) / -0.7(-0.8 to-0.5) / -0.1(-0.2 to 0.1).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S098

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN105, PGIC pain 6 mo — SMD construction and intervals.
- Printed tuples: -0.54(-0.59 to-0.05) / -0.55(-0.60 to-0.16) / -0.29(-0.33 to 0.06).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING

### S099

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN106, PGIC pain 12 mo — group adjusted estimates.
- Printed tuples: 2.2(2.1 to 2.3) / 2.2(2.1 to 2.4) / 2.8(2.7 to 2.9).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S100

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN106, PGIC pain 12 mo — between-group estimates and omnibus test.
- Printed tuples: -0.6(-0.8 to-0.5) / -0.6(-0.7 to-0.4) / 0.1(-0.1 to 0.2).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S101

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN106, PGIC pain 12 mo — SMD construction and intervals.
- Printed tuples: -0.55(-0.50 to 0.05) / -0.57(-0.54 to-0.08) / -0.29(-0.25 to 0.14).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Containment does not reconcile for contrast1,2,3: F-ST1-002. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING

### S102

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN107, PGIC general 3 mo — group adjusted estimates.
- Printed tuples: 2.0(1.9 to 2.1) / 1.6(1.5 to 1.7) / 2.7(2.6 to 2.8).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S103

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN107, PGIC general 3 mo — between-group estimates and omnibus test.
- Printed tuples: -0.7(-0.8 to-0.6) / -1.1(-1.2 to-1.0) / -0.4(-0.5 to-0.3).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S104

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN107, PGIC general 3 mo — SMD construction and intervals.
- Printed tuples: -0.66(-1.04 to-0.38) / -0.66(-0.98 to-0.42) / -0.40(-0.67 to-0.18).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING

### S105

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN108, PGIC general 6 mo — group adjusted estimates.
- Printed tuples: 2.1(2.0 to 2.2) / 1.8(1.7 to 1.9) / 2.5(2.5 to 2.6).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S106

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN108, PGIC general 6 mo — between-group estimates and omnibus test.
- Printed tuples: -0.5(-0.6 to-0.3) / -0.7(-0.9 to-0.6) / -0.2(-0.4 to-0.1).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S107

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN108, PGIC general 6 mo — SMD construction and intervals.
- Printed tuples: -0.46(-0.69 to-0.24) / -0.50(-0.70 to-0.32) / -0.24(-0.41 to-0.07).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING

### S108

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN109, PGIC general 12 mo — group adjusted estimates.
- Printed tuples: 2.0(1.9 to 2.1) / 1.9(1.8 to 2.0) / 2.6(2.5 to 2.7).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING

### S109

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN109, PGIC general 12 mo — between-group estimates and omnibus test.
- Printed tuples: -0.6(-0.7 to-0.4) / -0.7(-0.8 to-0.5) / -0.1(-0.3 to 0.0).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING

### S110

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN109, PGIC general 12 mo — SMD construction and intervals.
- Printed tuples: -0.53(-0.64 to-0.11) / -0.58(-0.67 to-0.22) / -0.28(-0.36 to 0.03).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING




<!-- Complete pass1 inventory: reports -->

# Statistical relationship inventory — report-supplement pass-1 shard

Fresh runtime agent: /root/stat1_reports; configured run model gpt-6.1-sol; reasoning effort high; stage statistics_pass_1; fresh spawn. Exact assigned scope: DOC-005 PDF pages1–16 and19,eTables1–10,eFigures1–2; DOC-004 PDFpages1–7 andDOC-006 eTable 3 A1:J115 for any inferential/method relationships. DOC-005 PDF17–18/eTable11 is excluded from this shard and belongs to the raw-score statistical peer. MAIN inference rows and PLAN-internal relationships belong to separate peers. Every location in this artifact is REPORT; matching main methods were read only for shared definitions (all tests2-sidedα=.05,95%CIs,GEEclustering), not assigned MAIN results.

Scientific inputs: exact sources, current fresh map extraction/parts/reports_restart.md, selective current main-method definitions. No prior Workflow1.6.2 artifact or old finding/report was a scientific input. Quantitative source authority: fresh PyMuPDF1.26.4 CPU renders in preprocessing/stat1_reports, current mapper's source-confirmed complete transcriptions; direct permitted Office helper extract_office_source.py for all 525 populated workbook cells. No web or external literature. No other Python used.

This shard contains 63 stable relationship records, S201–S263. Families carry every printed row/tuple explicitly, not a selected subset. Findings: F-ST1-201–F-ST1-206. Each record is PASS_1_COMPLETE; a fresh separate pass-2 agent must revisit every record. Missing definitions are named as limitations, not filled from convention. Counts/descriptive values without inferential content remain mapped by the numeric peer; they are retained here when needed to identify a statistical population.

## S201 — Outcome definitions, thresholds and directions

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.2](../../../joi250046supp4_prod_1755300121.15587.pdf#page=2)
- **Finding links:** None

**Printed values and method:**

```text
### SUP-RESULTS-P02 — DOC-005 PDF p2

[Exact source page](../../../joi250046supp4_prod_1755300121.15587.pdf#page=2)


OUTCOME MEASURES
Pain Severity Score: Based on modified 11-item version of the Brief Pain Inventory – Short Form (BPI-
SF). Score is calculated mean of all 11 items; range 0-10 with a higher score = worse pain severity

Pain Intensity Score: Based on 4-item subscale of the Brief Pain Inventory – Short Form (BPI-SF). Score
is calculated mean of all 4 items; range 0-10 with a higher score = worse pain intensity

Pain-related Interference Score: Based on 7-item subscale of the Brief Pain Inventory – Short Form (BPI-
SF). Score is calculated mean of 7 items; range 0-10 with a higher score = worse pain-related interference

Minimal clinically important difference (MCID) is defined as ≥30% decrease in pain score from baseline
(i.e., improvement; pain score range 0-10 with a higher score = worse pain severity, intensity or related
interference)

8-Item Patient Health Questionnaire Depression Scale (PHQ-8): Sum of 8 items related to depressive
symptoms (each item response 0-3) with total scale range=0-24; higher score = greater severity of
depressive symptoms. Cut points= 10 (moderate), 15 (moderately severe) and 20 (severe depression).

The Generalized Anxiety Disorder 7-item Scale (GAD-7): Sum of 7 items related to anxiety symptoms
(each item response 0-3) with total scale range=0-21; higher score = greater severity of anxiety
symptoms. Cut points= 5 (mild), 10 (moderate) and 15 (severe) levels of anxiety.

PROMIS (Patient-Reported Outcomes Measurement Information System) Sleep Disturbance – Short
Form 6a: Score by summing the 6 items (each item response 1-5) and then converting raw score to
standardized T-score, using the HealthMeasures Scoring Service, with mean of 50 and standard deviation
of 10. Higher T-score= worse sleep disturbance. Score ≥60 indicates moderate (60-70) to severe (>70)
sleep disturbance.

PROMIS Ability to Participate in Social Roles and Activities – Short Form 4a: Score by summing the 4
items (each item response 1-5) and then converting raw score to standardized T-score, using the
HealthMeasures Scoring Service, with mean of 50 and standard deviation of 10. Higher T-score= better
ability to participate in social roles and activities. Score ≤40 indicates moderate (40-30) to severe (< 30)
limitations in ability to participate.

PROMIS Physical Function – Short Form 6b: Score by summing the 6 items (each item response 1-5) and
then converting raw score to standardized T-score, using the HealthMeasures Scoring Service, with mean
of 50 and standard deviation of 10. Higher T-score= better physical functioning. Score ≤40 indicates
moderate (40-30) to severe (< 30) limitations in physical functioning.




© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.
```

**Pass-1 checks and result:** Means of 11/4/7 BPI items span0–10, higher worse; MCID≥30% decrease,3-month primary. PHQ8sum0–24; GAD7sum0–21; PROMIS T-score references50/10, sleep higher worse/social and physical higher better. Ranges, item counts, thresholds and direction definitions were read; no internal inferential conflict. These definitions anchor all outcome rows below.

## S202 — Primary response completeness and missingness decision

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.4](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [DOC-005 PDF p.7](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7)
- **Finding links:** None

**Printed values and method:**

```text
### SUP-RESULTS-P07 — DOC-005 PDF p7

[Exact source page](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7)


eTable 1. Primary outcome follow-up rates and patterns overall and by arm.
                                            Usual Care
                             OVERALL           plus    painTRAINER Health Coach
                             N    %          N      %    N     %     N      %
Randomized                  2331            777         776         778
Follow-up
 3 months                   1798    77.1     621    79.9   542     69.8    635     81.6
 6 months                   1790    76.8     622    80.1   547     70.5    621     79.8
 12 months                  1861    79.8     639    82.2   583     75.1    639     82.1
At least 1 follow-up        2036    87.3     703    90.5   643     82.9    690     88.7
No follow-up                 295    12.7      74     9.5   133     17.1     88     11.3
One observed follow-up       188     8.1      64     8.2    77      9.9     47      6.0
Two observed follow-ups      283    12.1      99    12.7   103     13.3     81     10.4
Three observed follow-ups   1568    67.3     540    69.5   464     59.8    564     72.5
```

**Pass-1 checks and result:** 3M missingness100−77.1=22.9%>15%: branch triggered; arm completeness79.9/69.8/81.6 differs. Counts and percentages agree within display precision. Pattern counts188+283+1568=2039 versus2036; PT644vs643 andHC692vs690; implied observed visits5458vs5449. All remaining relative gaps<.05, one exclusion. Base complete visits1798+1790+1861=5449.

## S203 — Additional predictor selection and analysis attribution

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.4](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [DOC-005 PDF p.5](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5), [DOC-005 PDF p.7](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7)
- **Finding links:** F-ST1-203, F-ST1-204

**Printed values and method:**

```text
P<.10 in both adjusted3M-MCID modified Poisson and3M-missingness logistic models selects additional imputation/estimation predictors. Weight model selects variables associated with3M-MCID and any follow-up in corresponding separate adjustedmodels. Base set: arm, baseline severity, age, sex, site, rural, multisite pain,mentalhealth. eTable2 final imputation/estimation adds education(anycollege vsHSorless),unemployment; weight addsPEG,PHQ8,GAD7,anynegativeSDOH,education.
```

**Pass-1 checks and result:** The stated dual-selection rule is coherent. Applied covariate identity/coding is not fully aligned with model coefficient displays; seeS261/S262. No preference for a different selection method is proposed.

## S204 — Pattern-mixture imputation design and response construction

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.4](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [DOC-005 PDF p.5](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5)
- **Finding links:** None

**Printed values and method:**

```text
Imputation (MNAR): Implementation of the MNAR imputation approach for GEE2 requires the specification and
execution of a two-step modeling process. The first step is to impute missing outcome data using a pattern-mixture
approach with reasonable choices for included missing patterns given the amount of missing data. To classify
patterns of missing data in this study, among those with any observed follow-up measure we created a categorical
variable indicating whether each participant had one (8.1%), two (12.1 %) or three (67.3%) follow-up observations
recorded. The full imputation model was specified as follows:


         𝐸𝐸(𝑌𝑌𝑖𝑖𝑖𝑖 |𝑋𝑋𝑖𝑖 , 𝒁𝒁𝑖𝑖 ) = 𝛼𝛼 + 𝛽𝛽𝑃𝑃𝑃𝑃 𝐼𝐼(𝑋𝑋𝑖𝑖 = 𝑃𝑃𝑃𝑃) + 𝛽𝛽𝐻𝐻𝐻𝐻 𝐼𝐼(𝑋𝑋𝑖𝑖 = 𝐻𝐻𝐻𝐻) + 𝜷𝜷𝑧𝑧 𝒁𝒁𝑖𝑖 + 𝛽𝛽6 𝐼𝐼(𝑚𝑚 = 6) + 𝛽𝛽12 𝐼𝐼(𝑚𝑚 = 12)
                                 + 𝛾𝛾𝑃𝑃𝑃𝑃,6 𝐼𝐼(𝑋𝑋𝑖𝑖 = 𝑃𝑃𝑃𝑃)𝐼𝐼(𝑚𝑚 = 6) + 𝛾𝛾𝑃𝑃𝑃𝑃,12 𝐼𝐼(𝑋𝑋i = 𝑃𝑃𝑃𝑃)𝐼𝐼(𝑚𝑚 = 12)

                                 +𝛾𝛾𝐻𝐻𝐻𝐻,6 𝐼𝐼(Xi = 𝐻𝐻𝐻𝐻)𝐼𝐼(𝑚𝑚 = 6) + 𝛾𝛾𝐻𝐻𝐻𝐻,12 𝐼𝐼(Xi = 𝐻𝐻𝐻𝐻)𝐼𝐼(𝑚𝑚 = 12)

                                                  +𝜂𝜂1 𝐼𝐼(𝑂𝑂𝑂𝑂𝑂𝑂𝑖𝑖 = 1) + 𝜂𝜂2 𝐼𝐼(𝑂𝑂𝑂𝑂𝑂𝑂𝑖𝑖 = 2)

                               +𝜂𝜂𝑃𝑃𝑃𝑃,1 𝐼𝐼(𝑋𝑋i = 𝑃𝑃𝑃𝑃)𝐼𝐼(𝑂𝑂𝑂𝑂𝑂𝑂𝑖𝑖 = 1) + 𝜂𝜂𝐻𝐻𝐻𝐻,1 𝐼𝐼(𝑋𝑋i = 𝐻𝐻𝐻𝐻)𝐼𝐼(𝑂𝑂𝑂𝑂𝑂𝑂𝑖𝑖 = 1)

                               +𝜂𝜂𝑃𝑃𝑃𝑃,2 𝐼𝐼(𝑋𝑋i = 𝑃𝑃𝑃𝑃)𝐼𝐼(𝑂𝑂𝑂𝑂𝑂𝑂𝑖𝑖 = 2) + 𝜂𝜂𝐻𝐻𝐻𝐻,2 𝐼𝐼(𝑋𝑋i = 𝐻𝐻𝐻𝐻)𝐼𝐼(𝑂𝑂𝑂𝑂𝑂𝑂𝑖𝑖 = 2)


© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.


where 𝑌𝑌𝑖𝑖𝑖𝑖 is the change in pain severity for individual i at time point 𝑚𝑚, 𝑋𝑋𝑖𝑖 is the intervention group (UC, PT, and
UC), 𝑚𝑚 is the number of months post randomization, and 𝒁𝒁𝑖𝑖 is the vector of baseline covariates. Further, 𝑂𝑂𝑂𝑂𝑂𝑂𝑖𝑖 is a
variable that indicates the pattern of observed outcomes present. In this case, 𝑂𝑂𝑂𝑂𝑂𝑂𝑖𝑖 takes on the values 1, 2 or 3
depending on whether 1, 2 or 3 of the follow-up measures are observed for a randomized person. The 𝒁𝒁𝑖𝑖 include all
adjustment variables as specified previously. We fit this assuming a modified linear model using GEE with
independent working correlation and robust standard errors, accounting for clustering of participants within health
coaches and multiple observations per person. The fitted imputation model was then used to replace missing
outcomes data with predicted values from the model. The binary MCID outcome variable was then calculated using
the change outcome with imputed data and the baseline value of pain severity.
```

**Pass-1 checks and result:** Linear GEE, independence, robust clustering byperson/coach; arm × time and arm × observed pattern terms printed; referenceOBS3,UC,3M; missing change replaced by predicted values; binary MCID computed from change/baseline. Formula and coefficient structural families align. No unstated covariance, finite-sample test or change-sign convention inferred.

## S205 — Imputation population, observed visits and missing values

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.7](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7), [DOC-005 PDF p.8](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8)
- **Finding links:** None

**Printed values and method:**

```text
eTable3 observations6108,persons2036,missingvalues659; eTable1 observed visits1798+1790+1861=5449; no follow-up295.
```

**Pass-1 checks and result:** 2036×3=6108;6108−5449=659;2331−295=2036. Participant-level and visit-level sample sizes reconcile. The minute observed-pattern discrepancy isS202's display precision exclusion.

## S206 — Primary estimation functional form, variance and clustering

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.5](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5)
- **Finding links:** None

**Printed values and method:**

```text
In the second step, the following estimation model was fit to the full imputed data with the binary MCID outcome
now represented as 𝑌𝑌�𝑖𝑖𝑖𝑖 and using the following pre-specified functional form from the statistical analysis plan:

      𝑙𝑙𝑙𝑙𝑙𝑙(𝐸𝐸�𝑌𝑌�𝑖𝑖𝑖𝑖 �𝑋𝑋𝑖𝑖 , 𝒁𝒁𝑖𝑖 )) = 𝛼𝛼 + 𝛽𝛽𝑃𝑃𝑃𝑃 𝐼𝐼(𝑋𝑋𝑖𝑖 = 𝑃𝑃𝑃𝑃) + 𝛽𝛽𝐻𝐻𝐻𝐻 𝐼𝐼(𝑋𝑋𝑖𝑖 = 𝐻𝐻𝐻𝐻) + 𝜷𝜷𝑧𝑧 𝒁𝒁𝑖𝑖 + 𝛽𝛽6 𝐼𝐼(𝑚𝑚 = 6) + 𝛽𝛽12 𝐼𝐼(𝑚𝑚 = 12)

                                   + 𝛾𝛾𝑃𝑃𝑃𝑃,6 𝐼𝐼(𝑋𝑋𝑖𝑖 = 𝑃𝑃𝑃𝑃)𝐼𝐼(𝑚𝑚 = 6) + 𝛾𝛾𝑃𝑃𝑃𝑃,12 𝐼𝐼(𝑋𝑋i = 𝑃𝑃𝑃𝑃)𝐼𝐼(𝑚𝑚 = 12)

                                   +𝛾𝛾𝐻𝐻𝐻𝐻,6 𝐼𝐼(Xi = 𝐻𝐻𝐻𝐻)𝐼𝐼(𝑚𝑚 = 6) + 𝛾𝛾𝐻𝐻𝐻𝐻,12 𝐼𝐼(Xi = 𝐻𝐻𝐻𝐻)𝐼𝐼(𝑚𝑚 = 12).


The model was fit with GEE assuming Poisson errors and using robust sandwich standard errors to account for
clustering within provider and individual.1 Parameter estimates are taken directly from the solution to the second
step GEE model above and the variance-covariance matrix for the joint imputation and analysis model are calculated
as described in Wang and Fitzmaurice.2 Summaries of the fitted imputation and estimation models are provided in
eTable 3 and eTable 4.
```

**Pass-1 checks and result:** Log-mean binary MCID Poisson GEE witharm, time,arm × time; robust provider/person sandwich and joint imputation/analysis variance referenced. Form reproduces coefficient/time-contrast families; no individual test statistic, degrees of freedom or numeric standard error supplied.

## S207 — Nonresponse weighting and baseline missing covariates

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.5](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5), [DOC-005 PDF p.6](../../../joi250046supp4_prod_1755300121.15587.pdf#page=6), [DOC-005 PDF p.10](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10)
- **Finding links:** None

**Printed values and method:**

```text
As a final note on imputation, there were a small number of cases where baseline covariates contained a limited
number of missing values. To keep the entire randomized cohort intact for all analyses, these missing baseline values
were imputed with their corresponding population means estimated from all available baseline data.3

Non-Response Weighting: The imputation approach assuming data are MNAR was used to impute missing data for
those that had at least one observation, but we observed a higher-than-expected number of participants with all
outcome time points missing (12.7%) and a differential by study arm: 9.5% for Usual care plus, 17.1% for
painTRAINER, and 11.3% for health coach (eTable 1).To be able to estimate an average treatment effect (ATE)
amongst all randomized, and due to concern about differential missingness, we added non-response weighting which
we formally incorporated into the SAP.

For the primary weighted analysis, to estimate the non-response weights, we fit a logistic regression model to the
entire randomized population, with an indicator of at least one observed follow-up as the outcome. Predictor
variables included study arm, baseline pain severity, age, sex, clinical site, rural/medically underserved residency,
multisite pain, and co-occurring mental health conditions and additional variables that were associated both with the
3-month MCID in pain severity outcome and with having any follow-up at 3, 6 or 12 months (Supplement 5). As
detailed above for adjustment variables, additional variables for the weight model were evaluated one-at-a-time by
fitting a sequence of separate models for 3-month MCID in pain severity (modified Poisson regression) and for any
follow-up (logistic regression). Those baseline covariates that, when included in models with study arm and the base
set of adjustment variables, reached statistical significance at the 0.10 level in model for MCID and in the model for
any follow-up (Supplement 5) were added to the weight model.

The final model for the non-response weights took the following form:

                          𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙(𝐸𝐸(𝑅𝑅𝑖𝑖 |𝑋𝑋𝑖𝑖 , 𝒁𝒁𝑖𝑖 )) = 𝛽𝛽0 + 𝛽𝛽𝑃𝑃𝑃𝑃 𝐼𝐼(𝑋𝑋𝑖𝑖 = 𝑃𝑃𝑃𝑃) + 𝛽𝛽𝐻𝐻𝐻𝐻 𝐼𝐼(𝑋𝑋𝑖𝑖 = 𝐻𝐻𝐻𝐻) + 𝜷𝜷𝑧𝑧 𝒁𝒁𝑖𝑖 ,

where 𝑅𝑅𝑖𝑖 indicates having at least one observed follow-up measurement. Predictions, 𝑝𝑝𝑖𝑖 , from this model are used to
                         1
calculate weights 𝑤𝑤𝑖𝑖 = . The 𝑤𝑤𝑖𝑖 were then scaled to the study sample size and included as weights in the GEE
                            𝑝𝑝𝑖𝑖



© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.


### SUP-RESULTS-P06 — DOC-005 PDF p6

[Exact source page](../../../joi250046supp4_prod_1755300121.15587.pdf#page=6)


estimation model described in the imputation section (step 2). The fitted weight model is presented in eTable 5, and
eTable 6 and eFigure 1 provide summaries of the predicted probabilities and corresponding weights.




© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.
```

**Pass-1 checks and result:** Entire2331 response-logistic fit;w=1/p scaled for analytic2036 persons, table4 visitweightssum6108=3×2036. Baseline missing means imputed fromavailablebaseline cohort. Conditional response distribution is not an outcome model; no raw/imputed equivalence assumed.

## S208 — Complete linear imputation coefficient/interval/P family

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.8](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8)
- **Finding links:** F-ST1-201

**Printed values and method:**

```text
### SUP-RESULTS-P08 — DOC-005 PDF p8

[Exact source page](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8)


eTable 3. Imputation step 1: Summary of fitted imputation model for primary
analysis.
 Step 1. Imputation Model (Linear)
 Outcome: Change in pain severity        Overall      N
 Number of observations used               6108    2036
 Number of missing values                   659

 Variable                                 Est.         95% CI      p-value
 Intercept                               -1.24     -1.42   -1.06    <.001
 painTRAINER (vs. Usual Care plus)       0.49       0.39    0.59    <.001
 Health Coach (vs. Usual Care plus)      0.45       0.36    0.54    <.001
 Time: 6M                                0.13       0.07    0.19    0.025
 Time: 12M                               0.31       0.24    0.38    <.001
 Pattern: 2 observed follow-ups          -0.28     -0.47   -0.08    0.150
 Pattern: 1 observed follow-up           -0.20     -0.36   -0.03    0.226
 painTRAINER | Time 6M                   0.02      -0.07    0.11    0.853
 painTRAINER | Time 12M                  0.01      -0.09    0.12    0.916
 Health Coach | Time 6M                  0.08      -0.01    0.17    0.351
 Health Coach | Time 12M                 -0.06     -0.16    0.04    0.535
 Pattern 2 | painTRAINER                 -0.30     -0.58   -0.02    0.280
 Pattern 1 | painTRAINER                 -0.21     -0.45    0.02    0.368
 Pattern 2 | Health Coach                -0.47     -0.74   -0.19    0.090
 Pattern 1 | Health Coach                0.18      -0.07    0.44    0.468
 Sex: Male                               -0.22     -0.29   -0.14    0.003
 Age >=65                                0.19       0.12    0.27    0.013
 Site 2                                  0.07      -0.03    0.17    0.479
 Site 3                                  0.19       0.08    0.29    0.069
 Site 4                                  0.15       0.05    0.24    0.124
 Residence:Urban                         0.07       0.00    0.15    0.306
 1+ musculoskeletal pain conditions      -0.22     -0.30   -0.14    0.004
 No Mental health diagnosis EHR          0.26       0.19    0.33    <.001
 Pain severity                           0.36       0.33    0.38    <.001
 Education:AA degree (ref = High         -0.02     -0.11    0.08    0.866
 school or less)
 Education:AA degree (ref = High         0.16      0.07    0.25     0.077
 school or less)
 Education:Graduate degree (ref = High   0.39      0.29    0.49    <.001
 school or less)
 Not employed                            -0.55     -0.62   -0.47   <.001




© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.
```

**Pass-1 checks and result:** All 28 printed coefficient tuples: point containment and endpoint order hold; seven95%CI-excludes0/P>.05 conflicts consolidated F-ST1-201. Remaining null/significance statuses agree. Numeric Wald reconstruction is diagnostic only because coefficient test/df/interval construction not named. Time6, sex,age,etc diagnostics cannot establish a further contradiction beyond the seven null conflicts.

## S209 — Complete weighted primary RR/interval/P family

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.9](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9)
- **Finding links:** F-ST1-202, F-ST1-204

**Printed values and method:**

```text
### SUP-RESULTS-P09 — DOC-005 PDF p9

[Exact source page](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9)


eTable 4. Imputation step 2: Summary of primary estimation model fit to imputed
data with weighting.
Step 2. Estimation Model (Poisson) –
Imputation with Weights.
                                              Overall Persons
Outcome: Binary 30% improvement in pain
severity.
Number of Observations Used                    6108    2036
Sum of Weights                                 6108
Variable                                        RR         95% CI      p-value
painTRAINER (vs. Usual Care plus)              1.28    1.06     1.55     0.010
Health Coach (vs. Usual care plus)             1.54     1.3     1.82     <.001
Health Coach vs. painTRAINER 3M                 1.2    1.03      1.4     0.019
painTRAINER vs. Usual Care plus 6M             1.44    1.21      1.7    <0.001
painTRAINER vs. Usual Care plus 12M            1.32    1.13     1.54    <0.001
Health Coach vs. Usual Care plus 6M            1.62    1.39      1.9    <0.001
Health Coach vs. Usual Care plus 12M           1.41    1.25     1.59    <0.001
Health Coach vs. painTRAINER 3M                 1.2    1.03      1.4     0.019
Health Coach vs. painTRAINER 6M                1.13    0.98      1.3     0.086
Health Coach vs. painTRAINER 12M               1.07    0.96     1.19     0.215
Sex: Male (vs. Female)                          0.8    0.71     0.91    <0.001
Age >=65 (vs. <65)                             1.15      1      1.33     0.046
Site                                           1.07    0.89     1.28     0.498
Site                                           1.15    0.97     1.37     0.102
Site                                           1.17    1.02     1.34     0.028
Residence: Urban (vs. Rural)                   1.07    0.96     1.19     0.226
1+ musculoskeletal pain conditions (vs. 1)     0.87    0.78     0.97     0.014
Mental health diagnosis EHR (vs. None)         1.15    1.04     1.27     0.008
Pain severity                                  0.99    0.96     1.02     0.451
Education: AA degree (vs. HS or less)          0.97    0.82     1.16     0.770
Education: AA degree (ref vs. HS or less)      1.16      1      1.33     0.046
Education: Graduate degree (vs. HS or less)    1.35    1.13     1.61    <0.001
Not employed (vs. Employed)                    0.72    0.64      0.8    <0.001




© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.
```

**Pass-1 checks and result:** All 23 printed rows including identicalHC/PT3M repetition: containment/order hold; directions and multiplicative contrast closure fit display precision. Age and secondAA education lowerCI1/P.046 conflict consolidated withPEG upperCI1/P.037 inF-ST1-202. Duplicate 3M row reconciles, not an excluded observation. Educationcoding/attribution addressedS261.

## S210 — Complete response-logistic OR/interval/P family

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.10](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10)
- **Finding links:** F-ST1-202, F-ST1-203

**Printed values and method:**

```text
### SUP-RESULTS-P10 — DOC-005 PDF p10

[Exact source page](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10)


 eTable 5. Summary of logistic weighting model for any observed follow-up.
Variable                                                    OR*              95% CI           P-value
Usual Care plus (vs. painTRAINER)                           2.05         1.50      2.79        <0.001
Health Coach (vs. painTRAINER)                              1.68         1.25      2.26        <0.001
Male Sex                                                    0.76         0.57      1.00         0.053
Age >=65                                                    0.97         0.70      1.35         0.859
Site                                                        2.93         1.97      4.36        <0.001
Site                                                        3.43         2.27      5.18        <0.001
Site                                                        2.48         1.70      3.61        <0.001
Residence Urban                                             0.67         0.49      0.90         0.009
>1 Musculoskeletal Pain Condition                           0.97         0.72      1.29         0.812
No Mental Health Diagnosis                                  1.21         0.92      1.59         0.165
Pain Severity                                               1.05         0.93      1.18         0.417
Not employed                                                1.49         1.11      2.00         0.008
No Negative Social Determinant of Health                    1.34         1.01      1.77         0.042
PEG score                                                   0.96         0.92      1.00         0.037
PHQ-8                                                       0.97         0.94      1.01         0.125
GAD-7                                                       0.99         0.96      1.02         0.524
c-statistic                                                0.679
* OR = Odds Ratio
Health care site information has been excluded.
```

**Pass-1 checks and result:** All 16 OR95%CI/P tuples and c-statistic. Containment/order and referencegroup direction hold;male upper1,P.053 agrees. PEG upper1,P.037 belongsF-ST1-202. ORlabel is coherent forlogistic response model. Covariate membership discrepancy isS262; no odds-versus-risk relabeling.

## S211 — Response-probability and analytic weight summaries

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.10](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10)
- **Finding links:** None

**Printed values and method:**

```text
eTable 6. Summary of estimated weights.
                                                  Sum    Mean      SD   Min.   P25    P50    P75        Max.
  Estimated probability of having at
  least 1 follow-up.                               --    0.88   0.07    0.50   0.85   0.90   0.93       0.98
  Calculated weight used for
  analysis.                                       2036   1.00   0.09    0.89   0.94   0.97   1.03       1.75
```

**Pass-1 checks and result:** Probability[min.50,max.98],quartiles.85/.90/.93,mean.88,SD.07; weight[min.89,max1.75],quartiles.94/.97/1.03,mean1,SD.09,sum2036. Quantiles ordered and means inside extrema; reciprocal scaled range ratios are compatible within display precision. Mean reciprocal is not reciprocal mean; no such inference made.

## S212 — Complete-case sensitivity method and multiplicity rule

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.11](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11)
- **Finding links:** None

**Printed values and method:**

```text
### SUP-RESULTS-P11 — DOC-005 PDF p11

[Exact source page](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11)


SENSITIVITY ANALYSES
Missing Data Analyses: Sensitivity analysis results for different missing data assumptions for the MCID on pain severity primary outcome are presented in
eTable 7 below. eTable 7 provides results for different models assumptions for missing data that were pre-specified in the SAP including: a) complete-case
analysis (missing outcomes removed) adjusting for baseline pain severity, age, sex, clinical site, rural/medically underserved residency, multisite pain, and co-
occurring mental health conditions; b) worst case/best case analysis (missing outcomes for participants randomized to PT or HC are assumed 0 (worst case) and
missing outcomes for participants randomized to UC are 1 (best case)) adjusting for baseline pain severity, age, sex, clinical site, rural/medically underserved
residency, multisite pain, and co-occurring mental health conditions.


a Primary timepoint
b Adjusted mean % and adjusted RR were calculated from a modified Poisson regression model fit using generalized estimating equations (GEE) for each

binary outcome. Adjusted mean % assumes the mean of the covariate distribution to calculate randomized population average effects. Adjustment variables:
Sex, age, site, rural vs. urban residence, more than 1 musculoskeletal pain condition, presence of mental health diagnoses, and pain severity at baseline.
c Omnibus P value is the Wald Test to assess if there is any difference between the three groups. To control for multiple compairsons between-group

comparisons should only be compared if the Omnibus P value<0.05 following the least significant difference approach.
d Adjusted Number needed to treat (NNT) to gain one additional 30% improvement, i.e., one over the difference in the adjusted percent with an 30%

improvement or greater.
e If CIs for the absolute risk difference contain zero the NNT confidence limits appear non-sensical due to division by zero. The NNT estimate is interpreted as

being consistent with a NNT from the lower limit (positive number) to infinity, and a number needed to harm (NNH) from the upper limit (negative number) to
negative infinity.




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar
technologies.
```

**Pass-1 checks and result:** No imputation/weighting,seven baseline covariates,1798observed3Mpersons=621+542+635; modified Poisson GEE estimates standardized proportions, RR andNNT. OmnibusWaldacross3arms gates pairwiseinterpretation atP<.05, all 3 rows pass. Test is omnibus, not a pairwise P.

## S213 — Worst/best-case sensitivity method and population

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.11](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11)
- **Finding links:** None

**Printed values and method:**

```text
Missingactive(PT/HC)outcomes set0;missingUCoutcomes set1;all2331(UC777,PT776,HC778),seven baseline covariates;modified Poisson GEE. Table notes define NNT=100/(percentage difference) and disjoint infinity-containing branches when risk-difference CI crosses0.
```

**Pass-1 checks and result:** 777+776+778=2331; deliberately unfavorable active direction is coherent withmethod. All omnibusP<.001 passgate. NNT branch order is explicitly defined; do not treat positive/negative displayed endpoints as a conventional finite interval.

## S214 — eTable7 complete-case 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.11](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa 32.2 (28.5, 36.3) 35.5 (32.0, 39.3) 24.0 (20.9, 27.6) 1.34 (1.12, 1.61) 1.48 (1.24, 1.75) 1.10 (0.94, 1.29) <0.001 13 (8, 33)             9 (7, 15)      31 (13, -60)
```

**Pass-1 checks and result:** All three group95%CIs,three RR95%CIs,omnibusP andthree NNT95%limits reviewed. Containment/order/directions hold, treating disjoint NNT limits according tofootnote. RR point estimates consistent with standardized proportion ratios; omnibus differs frompairwise null tests; no implication thatall three pairwise contrasts significant. NNT reciprocals checked with half-unit precision; any remaining gaps≤.05 relative. RD variance absent: NNT limits cannot be derived from marginal group CIs alone.

## S215 — eTable7 complete-case 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.11](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11)
- **Finding links:** None

**Printed values and method:**

```text
6 months 40.1 (36.3, 44.3) 41.1 (37.4, 45.1) 26.6 (23.4, 30.3) 1.51 (1.28, 1.77) 1.54 (1.32, 1.81) 1.02 (0.90, 1.17) <0.001 8 (6, 13) 7 (6, 11) 101 (16, -22)
```

**Pass-1 checks and result:** All three group95%CIs,three RR95%CIs,omnibusP andthree NNT95%limits reviewed. Containment/order/directions hold, treating disjoint NNT limits according tofootnote. RR point estimates consistent with standardized proportion ratios; omnibus differs frompairwise null tests; no implication thatall three pairwise contrasts significant. NNT reciprocals checked with half-unit precision; any remaining gaps≤.05 relative. RD variance absent: NNT limits cannot be derived from marginal group CIs alone.

## S216 — eTable7 complete-case 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.11](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11)
- **Finding links:** None

**Printed values and method:**

```text
12 months 41.0 (37.3, 45.1) 41.5 (37.9, 45.4) 30.5 (27.2, 34.3) 1.34 (1.16, 1.56) 1.36 (1.17, 1.57) 1.01 (0.89, 1.15) <0.001 10 (7, 20) 10 (7, 15) 217 (22, -28)
```

**Pass-1 checks and result:** All three group95%CIs,three RR95%CIs,omnibusP andthree NNT95%limits reviewed. Containment/order/directions hold, treating disjoint NNT limits according tofootnote. RR point estimates consistent with standardized proportion ratios; omnibus differs frompairwise null tests; no implication thatall three pairwise contrasts significant. NNT reciprocals checked with half-unit precision; any remaining gaps≤.05 relative. RD variance absent: NNT limits cannot be derived from marginal group CIs alone.

## S217 — eTable7 worst/best-case 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.11](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa 22.7 (20.0, 25.8) 29.3 (26.3, 32.6) 39.4 (36.1, 43.0) 0.58 (0.49, 0.67) 0.74 (0.65, 0.85) 1.29 (1.09, 1.52) <0.001 -6 (-9, -5) -10 (-18, -7) 16 (10, 40)
```

**Pass-1 checks and result:** All three group95%CIs,three RR95%CIs,omnibusP andthree NNT95%limits reviewed. Containment/order/directions hold, treating disjoint NNT limits according tofootnote. RR point estimates consistent with standardized proportion ratios; omnibus differs frompairwise null tests; no implication thatall three pairwise contrasts significant. NNT reciprocals checked with half-unit precision; any remaining gaps≤.05 relative. RD variance absent: NNT limits cannot be derived from marginal group CIs alone.

## S218 — eTable7 worst/best-case 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.11](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11)
- **Finding links:** None

**Printed values and method:**

```text
6 months 28.6 (25.6, 31.9) 33.1 (30.0, 36.5) 41.3 (38.0, 44.9) 0.69 (0.60, 0.79) 0.80 (0.70, 0.91) 1.16 (1.00, 1.34) <0.001 -8 (-13, -6) -13 (-26, -8) 23 (12, 227)
```

**Pass-1 checks and result:** All three group95%CIs,three RR95%CIs,omnibusP andthree NNT95%limits reviewed. Containment/order/directions hold, treating disjoint NNT limits according tofootnote. RR point estimates consistent with standardized proportion ratios; omnibus differs frompairwise null tests; no implication thatall three pairwise contrasts significant. NNT reciprocals checked with half-unit precision; any remaining gaps≤.05 relative. RD variance absent: NNT limits cannot be derived from marginal group CIs alone.

## S219 — eTable7 worst/best-case 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.11](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11)
- **Finding links:** None

**Printed values and method:**

```text
12 months 31.3 (28.2, 34.6) 34.4 (31.2, 37.8) 43.0 (39.6, 46.7) 0.73 (0.64, 0.83) 0.80 (0.70, 0.91) 1.10 (0.96, 1.26) <0.001 -9 (-15, -7) -12 (-21, -8) 33 (15, -194)
```

**Pass-1 checks and result:** All three group95%CIs,three RR95%CIs,omnibusP andthree NNT95%limits reviewed. Containment/order/directions hold, treating disjoint NNT limits according tofootnote. RR point estimates consistent with standardized proportion ratios; omnibus differs frompairwise null tests; no implication thatall three pairwise contrasts significant. NNT reciprocals checked with half-unit precision; any remaining gaps≤.05 relative. RD variance absent: NNT limits cannot be derived from marginal group CIs alone.

## S220 — Protocol-change subset definitions, sample populations and adjustment

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.13](../../../joi250046supp4_prod_1755300121.15587.pdf#page=13), [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14), [DOC-005 PDF p.7](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7)
- **Finding links:** F-ST1-205

**Printed values and method:**

```text
### SUP-RESULTS-P13 — DOC-005 PDF p13

[Exact source page](../../../joi250046supp4_prod_1755300121.15587.pdf#page=13)


Protocol Change Subset Analyses: Sensitivity analysis results for different protocol changes for the primary outcome MCID on pain severity are presented in
eTable 8. The results in eTable 8 shows the results of the primary analysis restricting to subsets of the randomized population after the following protocol
changes were made: a) enhancement to the painTRAINER engagement activities (restricts to those randomized after 8/9/2021) and b) reminder letter sent to all
participants prior to follow-up survey reach out (restrict to those randomized after 3/31/2022). Specifically, to improve engagement in the painTRAINER
intervention the study team added motivational interviewing-based language to the onboarding script for those randomized to the online program. This change
was implemented on 8/9/2021 after 454 patients were enrolled in the study. This sensitivity analysis was pre-specified in the SAP to evaluate whether the
“enhanced” painTRAINER engagement activities improved the effect of the painTRAINER intervention. The follow-up letter analysis was not pre-specified in
the SAP, but we have added this post-hoc analysis after observing large improvements in follow-up rates (82.7% overall at 3 months and 90.1% with at least one
follow-up measure) after the study added a reminder letter, mailed to all participants before the due date of their follow-up survey, to remind them to expect an
email or a call (depending on participant preference) from the study team, and encouraged participants to complete the survey when contacted.




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar
technologies.


Before8/9/2021:N454,any follow-up366,3MPT149/HC153/UC152;after:N1877,any1670,3MUC512/PT448/HC527;after3/31/2022:N1038,any935,3MUC296/PT262/HC300. p13 callsresults primaryanalysis restrictedtosubsets; p14 covariate listcontainssevenbase variables.
```

**Pass-1 checks and result:** 454+1877=2331;366+1670=2036;letters858/1038=82.659%=82.7and935/1038=90.077%=90.1. Before3M149+153+152=454 label is randomized arm population rather thanobservedcounts; noadditional claimedresponse rate. Primaryvsbase subset covariates differ F-ST1-205. Prespecifiedenhancement/posthocletters status retained forcross-sourcechecker.

## S221 — eTable8 pre-enhancement 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa 20.5 (14.2, 29.6) 28.5 (23.4, 34.8) 21.3 (15.2, 29.8) 0.96 (0.59, 1.57) 1.34 (0.92, 1.95) 1.39 (0.92, 2.10) 0.138 -120 (11, -10) 14 (7, -67) 13 (6, -84)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.

## S222 — eTable8 pre-enhancement 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
6 months 32.9 (25.1, 43.0) 32.4 (27.8, 37.7) 25.2 (18.5, 34.2) 1.31 (0.88, 1.95) 1.29 (0.92, 1.80) 0.98 (0.73, 1.33) 0.313 13 (6, -27) 14 (7, -56) -185 (11, -10)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.

## S223 — eTable8 pre-enhancement 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
12 months 32.6 (25.0, 42.5) 37.7 (32.2, 44.3) 20.5 (14.7, 28.6) 1.59 (1.05, 2.41) 1.84 (1.29, 2.63) 1.16 (0.85, 1.57) 0.003     9 (5, 75)   6 (4, 12)   20 (7, -20)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.

## S224 — eTable8 post-enhancement 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa 28.0 (24.4, 32.0) 32.7 (29.5, 36.2) 20.4 (17.4, 23.9) 1.37 (1.11, 1.69) 1.60 (1.33, 1.93) 1.17 (0.99, 1.38) <0.001 14 (8, 39) 9 (6, 14) 22 (11, -327)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.

## S225 — eTable8 post-enhancement 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
6 months 33.8 (30.1, 38.1) 38.2 (34.5, 42.3) 22.2 (19.1, 25.7) 1.53 (1.27, 1.84) 1.72 (1.44, 2.06) 1.13 (0.97, 1.32) <0.001     9 (6, 16)   7 (5, 10)   24 (11, -88)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.

## S226 — eTable8 post-enhancement 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
12 months 36.9 (33.1, 41.2) 38.1 (36.0, 40.3) 28.6 (25.2, 32.5) 1.29 (1.09, 1.52) 1.33 (1.16, 1.52) 1.03 (0.92, 1.16) <0.001   13 (8, 34)   11 (8, 19) 86 (18, -31)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.

## S227 — eTable8 reminder-letter 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa 31.6 (26.7, 37.3) 34.1 (29.5, 39.5) 20.5 (16.6, 25.3) 1.54 (1.18, 2.01) 1.67 (1.30, 2.14) 1.08 (0.87, 1.34) <0.001 9 (6, 23) 8 (5, 14)   40 (11, -23)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.

## S228 — eTable8 reminder-letter 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** F-ST1-206

**Printed values and method:**

```text
6 months 35.6 (30.6, 41.4) 40.6 (35.8, 46.1) 21.3 (17.5, 26.1) 1.67 (1.30, 2.14) 1.90 (1.50, 2.41) 1.14 (0.94, 1.39) <0.001 8 (5, 14)  6 (4, 8)    20 (9, -43)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.

## S229 — eTable8 reminder-letter 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
12 months 38.2 (33.1, 44.0) 38.9 (35.6, 42.5) 26.1 (21.9, 31.2) 1.46 (1.17, 1.83) 1.49 (1.23, 1.80) 1.02 (0.87, 1.20) <0.001 9 (6, 21) 8 (6, 14) 133 (15, -19)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.

## S230 — Unadjusted binary analysis method and effect identity

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
Narrative:no adjustment,weightingorimputation. Footnote:modified Poisson GEE forbinaryoutcome without adjustment. Heading:unadjusted n/N(%),RelativeRisk(95%CI); titlecontains'adjusted relative risk'. PT/HC/UC groups; contrastsPT/UC,HC/UC,HC/PT.
```

**Pass-1 checks and result:** Repeated definitionsmakeunadjustedstatus immediately identifiable; title wording screened once. Unadjusted crudeproportion ratios provide a diagnosticpoint-estimate check supportedbyexplicitmethod; all 27 RRs agree withratioswithinprecision. No crude-SE-based CI orassumedwithinperson/coach covariance imposed.

## S231 — eTable9 pain severity 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa     179/542 (33.0) 229/635 (36.1) 151/621 (24.3) 1.36 (1.13, 1.63) 1.48 (1.26, 1.75) 1.09 (0.94, 1.27)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.

## S232 — eTable9 pain severity 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
6 months      225/547 (41.1) 259/621 (41.7) 167/622 (26.8) 1.53 (1.30, 1.80) 1.55 (1.32, 1.83) 1.01 (0.88, 1.17)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.

## S233 — eTable9 pain severity 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
12 months 246/583 (42.2) 269/639 (42.1) 197/639 (30.8) 1.37 (1.18, 1.59) 1.37 (1.21, 1.54) 1.00 (0.90, 1.10)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.

## S234 — eTable9 pain intensity 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa     164/543 (30.2) 192/635 (30.2) 129/621 (20.8) 1.46 (1.19, 1.78) 1.46 (1.18, 1.79) 1.00 (0.83, 1.21)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.

## S235 — eTable9 pain intensity 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
6 months      183/548 (33.4) 222/622 (35.7) 153/623 (24.6) 1.36 (1.13, 1.63) 1.45 (1.20, 1.74) 1.06 (0.90, 1.26)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.

## S236 — eTable9 pain intensity 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
12 months 218/583 (37.4) 238/641 (37.1) 191/639 (29.9) 1.25 (1.07, 1.47) 1.24 (1.08, 1.42) 0.99 (0.87, 1.12)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.

## S237 — eTable9 pain-related interference 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa     206/543 (37.9) 249/635 (39.2) 169/620 (27.3) 1.39 (1.17, 1.64) 1.44 (1.25, 1.65) 1.03 (0.92, 1.17)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.

## S238 — eTable9 pain-related interference 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
6 months      249/546 (45.6) 277/620 (44.7) 176/621 (28.3) 1.61 (1.38, 1.88) 1.58 (1.35, 1.85) 0.98 (0.86, 1.12)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.

## S239 — eTable9 pain-related interference 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
12 months 267/583 (45.8) 293/638 (45.9) 221/638 (34.6) 1.32 (1.15, 1.52) 1.33 (1.18, 1.48) 1.00 (0.91, 1.10)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.

## S240 — Unadjusted continuous-change descriptive/inferential method

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
Medians(25%-tile,75%tile) forchanges frombaseline; between-groupMEANdifferences95%CIs fromlinear regression GEE;15outcome/timepointrows;omnibusP acrossarms.
```

**Pass-1 checks and result:** Median differences neednot equalmean model differences. Direction is coherent withhigher worsepainandhigher betterfunction. Footnote'meanchange' andmedianheader do not changeeffect-column meaning; screened context observationonce. P is omnibus;pairwise nonsignificanceHC/PT doesnotconflictwithsignificant overall test.

## S241 — eTable10 pain severity 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa    -1.1 (-2.1, -0.1)     -1.1 (-2.3, -0.1)    -0.6 (-1.6, 0.2)   -0.4 (-0.6, -0.3) -0.4 (-0.6, -0.3) 0.0 (-0.2, 0.2)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S242 — eTable10 pain severity 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
6 months     -1.3 (-2.5, -0.1)     -1.4 (-2.5, -0.2)    -0.8 (-1.8, 0.2)   -0.4 (-0.7, -0.2) -0.5 (-0.8, -0.3) -0.1 (-0.3, 0.1)    <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S243 — eTable10 pain severity 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
12 months    -1.3 (-2.5, -0.3)     -1.4 (-2.5, -0.2)    -0.8 (-2.2, 0.1)   -0.4 (-0.7, -0.2) -0.4 (-0.6, -0.2) 0.0 (-0.1, 0.2)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S244 — eTable10 pain intensity 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa       -0.8 (-1.8, 0.0)   -0.8 (-2.0, 0.0)     -0.5 (-1.5, 0.2)   -0.3 (-0.5, -0.2) -0.3 (-0.5, -0.1) 0.0 (-0.1, 0.2)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S245 — eTable10 pain intensity 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
6 months        -1.0 (-2.0, 0.0)   -1.0 (-2.2, 0.0)     -0.8 (-1.5, 0.2)   -0.3 (-0.5, -0.1) -0.3 (-0.5, -0.2) -0.1 (-0.3, 0.1)    <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S246 — eTable10 pain intensity 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
12 months       -1.0 (-2.2, 0.0)   -1.0 (-2.2, 0.0)     -0.8 (-2.0, 0.2)   -0.3 (-0.5, -0.1) -0.2 (-0.4, -0.1) 0.0 (-0.1, 0.2)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S247 — eTable10 pain-related interference 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa    -1.3 (-2.4, -0.1)     -1.3 (-2.6, 0.0)     -0.7 (-1.9, 0.1)   -0.5 (-0.7, -0.3) -0.5 (-0.7, -0.3) 0.0 (-0.2, 0.2)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S248 — eTable10 pain-related interference 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
6 months        -1.4 (-2.9, 0.0)   -1.6 (-2.9, -0.1)    -0.9 (-2.1, 0.1)   -0.6 (-0.8, -0.3) -0.6 (-0.9, -0.4) -0.1 (-0.4, 0.2)    <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S249 — eTable10 pain-related interference 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
12 months    -1.6 (-3.0, -0.1)     -1.6 (-3.0, -0.1)    -1.0 (-2.6, 0.1)   -0.5 (-0.8, -0.3) -0.5 (-0.7, -0.3) 0.0 (-0.2, 0.3)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S250 — eTable10 social role functioning 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa        1.8 (-2.0, 5.8)   1.9 (-1.9, 6.0)      0.0 (-2.2, 4.3)     0.9 (0.1, 1.7)    1.5 (0.7, 2.2)   0.5 (-0.2, 1.3)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S251 — eTable10 social role functioning 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
6 months         1.9 (-1.9, 6.5)   1.9 (-1.9, 7.4)      1.5 (-3.2, 5.5)     1.3 (0.4, 2.2)    1.7 (0.9, 2.6)   0.4 (-0.5, 1.4)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S252 — eTable10 social role functioning 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
12 months        1.9 (-1.9, 7.5)   2.0 (-1.7, 7.7)      0.0 (-3.2, 5.8)     1.4 (0.4, 2.3)    1.4 (0.8, 2.1)   0.1 (-0.7, 0.8)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S253 — eTable10 physical functioning 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa        1.6 (-0.8, 3.6)   1.2 (-0.8, 3.8)      0.9 (-1.4, 3.2)     0.6 (0.1, 1.1)    0.8 (0.3, 1.2)   0.1 (-0.3, 0.6)     0.002
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S254 — eTable10 physical functioning 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
6 months         1.7 (-0.8, 4.4)   1.2 (-0.9, 4.4)      1.0 (-1.0, 3.6)     0.8 (0.3, 1.4)    0.5 (0.1, 0.9)   -0.3 (-0.8, 0.2)    <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S255 — eTable10 physical functioning 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
12 months        1.9 (-0.9, 5.0)   1.3 (-1.2, 4.6)      0.9 (-1.7, 3.6)     1.1 (0.5, 1.7)    0.8 (0.2, 1.5)   -0.3 (-0.9, 0.4)    <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S256 — Complete workbook model-selection P-value family

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-006 worksheet eTable 3](../../../joi250046supp5_prod_1755300121.16087.xlsx), H2:J108; A114
- **Finding links:** None

**Printed values and method:**

```text
Outcome/MissingAll/Missing3M selection headers H/I/J. FootnoteA114 boldmeansP<.10inbothprimary3M-MCIDandatleastonemissingnessmodelafterbase adjustment. All32 populated P cells:

| Cell | Stored value | Formula |
|---|---|---|
| H12 | 1.5599999999999999E-2 |  |
| J12 | 0.05 |  |
| H18 | <0.001 |  |
| I18 | 2.2800000000000001E-2 |  |
| J18 | 5.91E-2 |  |
| H20 | 1.8599999999999998E-2 |  |
| H39 | 6.3600000000000004E-2 |  |
| I39 | 1.9599999999999999E-2 |  |
| H41 | 5.2499999999999998E-2 |  |
| H43 | 5.7599999999999998E-2 |  |
| H45 | 3.0800000000000001E-2 |  |
| I47 | 2.0000000000000001E-4 |  |
| I51 | 1E-3 |  |
| H52 | 7.4099999999999999E-2 |  |
| H54 | 5.1000000000000004E-3 |  |
| H58 | 6.1499999999999999E-2 |  |
| H60 | 1.6999999999999999E-3 |  |
| H66 | 3.2300000000000002E-2 |  |
| H68 | 0.01 |  |
| H72 | <0.001 |  |
| H74 | <0.001 |  |
| H81 | <0.001 |  |
| I81 | 9.4999999999999998E-3 |  |
| H84 | 3.27E-2 |  |
| I84 | 3.3099999999999997E-2 |  |
| H87 | 1.0800000000000001E-2 |  |
| H100 | 4.9200000000000001E-2 |  |
| H101 | 4.9200000000000001E-2 |  |
| H102 | <.0001 |  |
| H105 | <.0001 |  |
| H108 | 2.4500000000000001E-2 |  |
| I108 | 4.0500000000000001E-2 |  |
```

**Pass-1 checks and result:** All populated Pvalues lie0–1or are valid upper bounds; H/I/J aredistinctselection tests, nottreatmentcomparisons. EmploymentH18<.001,I18=.0228,J18=.0591,PHQ8H81<.001/I81=.0095,GAD7H84=.0327/I84=.0331,SDOHH39=.0636/I39=.0196,PEGH108=.0245/I108=.0405meetdual weight selector. EducationH12=.0156,J12=.05 butI12blank; no numeric P asserted for a blank. Selectedweightmembership examinedS262. No estimate, SE, CI,test statisticprinted for these selection tests; no testreconstruction possible.

## S257 — Workbook completeness groups and sample implications

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-006 worksheet eTable 3](../../../joi250046supp5_prod_1755300121.16087.xlsx), B3:E3; A110; DOC-005 eTable1 [DOC-005 PDF p.7](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7)
- **Finding links:** None

**Printed values and method:**

```text
Overall2331;MissingAll295;Missing1or2 468;AllObserved1568. FootnoteA110 excludesmissing from percentdenominator. Complete workbook descriptives mapped inreports_restart.
```

**Pass-1 checks and result:** 295+468+1568=2331;468+1568=2036. This agreesanalyticcohortandvisitrows; eTable1 correspondingone+two471differs3,screenedonceasdisplay precision withS202. Baselinecount-percentage checks are assigned to the numeric checker,not duplicated here. Prespecified adjustment flags G4,G10,G11,G38,G54,G80 anchorsbase variables.

## S258 — Adherence histogram method and direction

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.3](../../../joi250046supp4_prod_1755300121.15587.pdf#page=3)
- **Finding links:** None

**Printed values and method:**

```text
PT/VirtualCoach8-sessionhistograms;xticks0,2,4,6,8; proportions0,.2,.4,.6,.8,1.0. Unlabeledbars; visuallyapproximatePTfirst/last .38/.38,VC .18/.63.
```

**Pass-1 checks and result:** No P,CI ormodelclaim. Histogram definition and arms match the intervention dose; exact counts not recoverable without labels. Visualapproximationscannotbeusedasprinted valuesforquantitativediscrepancy. VC/HC terminology is resolved by context, one exclusion.

## S259 — Probability/weight diagnostic figure

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.10](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10)
- **Finding links:** None

**Printed values and method:**

```text
eFigure2 observed≥1followupgreenversusnoobservedfollowupsorange;leftestimatedresponseprobability,rightweight;unlabeled barsandfittedsmoothcurves.
```

**Pass-1 checks and result:** Observedresponsegroup higher predicted probability andlower weight coherently matchesinverseprobability weighting. Figureincludesnonsampledresponsegroup fordiagnostics; onlyany follow-upanalysiscontributesfinalweightsum2036. No exact bar counts or bin probabilitiesprinted; no inferential comparison claimed.

## S260 — TIDieR sampling, fidelity and intervention definitions

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-004 PDF pp.2–6](../../../joi250046supp3_prod_1755300121.15087.pdf#page=2)
- **Finding links:** None

**Printed values and method:**

```text
HC12providers;8sessions45–60min/12weeks;PT8sessions30–45min/12weeks;fidelityplannedrandom5%first12months,onepercoach/6monthslater,thresholds100%content/80%CBT. Reviewed299=193training+89first12months+17later;8/2992.7%,11/2993.7%. Outreach356/77645.9%;extensionn14.
```

**Pass-1 checks and result:** All DOC-004 pages1–7read in the assigned fresh map. No inferential P, CI,statistical model,power calculationorstatistical stopping ruleinTIDieR. The fidelity sampling rule is descriptive protocol administration, not a trial decision rule; percentages reconcile. Intervention definitions support histogram identity; broadclinical or procedure auditnot performed.

## S261 — Education coding and coefficient attribution

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.7](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7), [DOC-005 PDF p.8](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8), [DOC-005 PDF p.9](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9)
- **Finding links:** F-ST1-204

**Printed values and method:**

```text
eTable2 selectededucation'anycollegevsHSdegreeorless';eTable3 printsAA−.02(−.11,.08),P.866;secondAA .16(.07,.25),P.077;graduate .39(.29,.49),P<.001;eTable4printsAA .97(.82,1.16),P.770;secondAA1.16(1,1.33),P.046;graduate1.35(1.13,1.61),P<.001.
```

**Pass-1 checks and result:** Onebinaryeducationfactorversusthreecategorycontrastsdoesnotidentifytheapplied model. Duplicated AA labels preventmatchingthetwo differentprinted estimates toonecategory, eventhoughworkbookdistinguishesassociate/college/graduate. Source-groundedRouteBobservationconsolidatedwithcoding discrepancy.

## S262 — Weight-model applied covariates versus final selected list

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.4](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [DOC-005 PDF p.5](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5), [DOC-005 PDF p.7](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7), [DOC-005 PDF p.10](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10)
- **Finding links:** F-ST1-203

**Printed values and method:**

```text
eTable2 finalweightadditionPEG,PHQ8,GAD7,SDOH,education;allmodelbase variableslistdoesnotcontainemployment; eTable5weightcoefficientsincludeNotemployed1.49(1.11,2.00),P.008 andnoeducationrow.
```

**Pass-1 checks and result:** Explicitlistandcompletefitdisplaydisagreeonwhichadditional predictorsgeneratedtheweights. Different reference armUC/HCversusPTcan reparameterize the logistic model and is not a finding;the membership difference cannot be resolved by reference choice.

## S263 — Subset analysis model attribution

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.13](../../../joi250046supp4_prod_1755300121.15587.pdf#page=13), [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14), [DOC-005 PDF p.4](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [DOC-005 PDF p.7](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7)
- **Finding links:** F-ST1-205

**Printed values and method:**

```text
Subsetnarrative'results oftheprimaryanalysisrestrictingtosubsets';primaryselectionstateseducationandemploymentaddedtoimputation/estimation;subsetfootnotelistsexclusivelysex,age,site, rural,morethan1condition,mentalhealth,baselineseverity.
```

**Pass-1 checks and result:** Subset point estimates are explicitly reported, but method mapping is unclear because the primary restricted fit and printed base set are different adjustments. This doesnot inferanythingfromabsenceofweightorimputationterms;onlytheexplicitcovariate lists compared.

## Scope limitations and no-applicable checks

No superiority decision based on an individual pairwise P outside the gated omnibus rule is reported in these assigned units. No noninferiority/equivalence margin, statistical interim/stopping boundary, power calculation, numeric standard error or numeric test statistic appears in the assigned supplement results. The source states two-sided tests and 95% CIs, but the coefficient-test family, degrees of freedom, coefficient-CI construction and full variance-covariance matrix are not provided: exact numeric P/statistic/SE reconstruction is not asserted. This does not limit CI-null/P-level or point-containment checks. Figures have unlabeled bars; no exact bin counts were extracted. Office conversion is unavailable, but direct cell structure provided exact stable locations. Scientific source-unit coverage gap: none; assigned source pages and workbook were completely mapped by the current fresh mapper and all result-relevant relationships were reviewed here.





<!-- Complete pass1 inventory: plans -->

# Statistical relationship inventory — PLAN shard, pass 1

Runtime task: `/root/stat1_plans`; fresh gpt-6.1-sol/high statistical pass-1 shard. The coordinator holds the tool-returned runtime agent ID for the execution manifest. Exact disjoint scope: every inferential/statistical/method/design relationship in DOC-002 protocol physical PDF pp.1–77 and DOC-003 SAP physical PDF pp.1–29. This inventory uses only current fresh maps, supplied sources, and current source renders. Main REPORT p.4 was read selectively to establish the stated sample-size simulation and reported-analysis dependence; its inferential result rows belong to the main shard. Cross-source outcome/status/omission findings belong to the cross-source checker.

The full four source-map parts were read. All 106 PLAN pages are covered by the current complete maps, including administrative pages, references, covers and histories; no extra relationship is invented for a unit without an applicable relationship. Families below enumerate their outcomes, times, contrasts and input tuples. Every record has PASS_1_COMPLETE. Pass 2 must revisit every ID using the complete ledger, screening log and mechanical recheck; this fresh pass-1 agent is not a pass-2 agent.

Source abbreviations: P = DOC-002, `joi250046supp1_prod_1755300121.14087.pdf`, role PLAN; A = DOC-003, `joi250046supp2_prod_1755300121.15087.pdf`, role PLAN. Physical PDF pages govern all locations. HC = coach-led CBT-CP, PT = painTRAINER, UC = usual care. Source links: [P, p.1](../../../joi250046supp1_prod_1755300121.14087.pdf#page=1), [A, p.1](../../../joi250046supp2_prod_1755300121.15087.pdf#page=1). Comparisons within these sources are P_P when an observation qualifies; no P_R classification is inferred merely from report corroboration.

## Complete relationship records

| S ID | Exact locations and roles | Explicit relationship family and source quantities | Pass-1 check, result and missing definitions | Pass 1 | Pass 2 |
|---|---|---|---|---|---|
| S401 | PLAN P pp.1,3–7; PLAN A pp.1–4,10 | Protocol5.0 November2022; SAP6.0 July2024 based on that protocol; amendments, masking of assignment/outcomes, SAP precedence and pre-unblinding approval | Historical amended and current specifications kept distinct. SAP explicitly takes analytical precedence; no inferred undeclared amendment. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S402 | PLAN P pp.13–15,29–31; PLAN A pp.8–9 | Individual phaseIII parallel3-arm trial; HC, PT, UC; two active/UC primary contrasts; all arms unrestricted usual care | Individual unit and parallel contrasts agree. Neither NI nor equivalence design/margin printed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S403 | PLAN P pp.29–30; PLAN A p.18 | Equal1:1:1 allocation; variable permuted blocks3,6,9; baseline-before-randomization | All block sizes divisible by3; equal allocation and individual randomization reconcile. No outcome-based allocation rule stated. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S404 | PLAN P pp.3,29; PLAN A pp.2,18 | Randomization strata: EHR sex male/female-or-other; baseline BPI severity<7/≥7; four sites; rural/MUA | Current source definitions agree; EHR stratification sex distinguished from self-reported moderator sex. No inferred extra stratum. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S405 | PLAN P pp.6–7,14,34,55; PLAN A pp.9,16,26 | Randomized2331/777 per arm, analyzed1863/621 per arm; enrolled approximately2500, may exceed; four sites595–625 | 3 × 777=2331 and3 × 621=1863. Enrollment and randomized targets explicitly different; site targets approximate. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S406 | PLAN P p.55; PLAN A p.16 | Retention80%, analyzed1863, randomized2331 | Point diagnostic1863/.8=2328.75; retention half-unit interval79.5–80.5% and randomized2330.5–2331.5 yield expected retained1852.7475–1876.8575, overlapping1862.5–1863.5. Arithmetic reconciles under display precision. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S407 | PLAN P p.55; PLAN A p.16 | Primary MCID30% at3-months; UC15%, active22.5%, difference7.5percentage points, printed ratio150%; power90%; two-sided.05 | 22.5−15=7.5;22.5/15=1.5. Independent-proportion/Fisher-LSD gate stated. No exact simulation inputs, covariance or joint-power definition supplied; diagnostics are not exact reproduction. REPORT p.4 explicitly supplies10,000 modified-Poisson simulations. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S408 | PLAN P p.55; PLAN A p.16 | Subgroup row372(20%of1863), UC15.0%, active31.0%, difference16.0%, ratio206.7%, power80% | 372/1863=19.9678%;31−15=16;100×31/15=206.6667%. Display intervals overlap all recomputations. N is total three-arm subgroup, not per-arm. Exact power engine absent. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S409 | PLAN P p.55; PLAN A p.16 | Subgroup row558(30%), UC15.0%, active27.7%, difference12.7%, ratio184.7%, power80% | 558/1863=29.9517%;27.7−15=12.7;100×27.7/15=184.6667%. Display intervals overlap. Exact power engine absent. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S410 | PLAN P p.55; PLAN A p.16 | Subgroup row744(40%), UC15.0%, active25.8%, difference10.8%, ratio172.0%, power80% | 744/1863=39.9356%;25.8−15=10.8;100×25.8/15=172%. Display intervals overlap. Exact power engine absent. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S411 | PLAN P pp.34,55–56; PLAN A p.16 | Subgroup prevalence20–40%, sex/mood≥40%, rural/MUA≥20%, SDOH unknown/exploratory; table is detectable active/UC difference | Source distinguishes within-subgroup pairwise power from the planned interaction model. No interaction-test power is claimed numerically; do not replace it with a preferred calculation. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S412 | PLAN P pp.55–56; PLAN A pp.16,19 | Fisher LSD: omnibus Wald any difference among3 groups at.05, then pairwise two-sided.05 only if gate significant | Planned sequence internally coherent; no alpha-spending/Bonferroni assumption. No realized omnibus or pairwise test statistic in PLAN. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S413 | PLAN P pp.56–57; PLAN A pp.19–21 | Confidence intervals/Pvalues two-sided, significance.05; secondary three-group comparisons similar gate; no safety multiplicity | No confidence level numerically supplied in PLAN beyond general two-sided description; REPORT uses95%. No claim of a cross-endpoint alpha allocation is inferred. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S414 | PLAN P pp.19,22,55–56; PLAN A pp.8,11,20 | Primary binary severity responder≥30% baseline reduction, modified11-item BPI-SF,3-months; HC/UC,PT/UC | Outcome, direction, primary time and response threshold agree; larger response risk favorable. No PLAN fitted estimate/CI/P tuple. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S415 | PLAN P pp.16,22–23,56; PLAN A pp.8,11,20–21 | Severity MCID at6and12-months secondary; both active/UC at3,6,12 | All three time indicators belong to one longitudinal model; later-time status distinct from single3-month primary endpoint. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S416 | PLAN P pp.22–23,57; PLAN A pp.11,21 | Binary intensity30%4-item responder and binary interference30%7-item responder at3,6,12; active/UC | Binary response definitions and model families agree. Measurement-cell omission of3-months is paired with explicit3-month timeframe in same table; intensity word in interference description is resolved by row/subscale. Exclusions recorded once. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S417 | PLAN P pp.23,57; PLAN A pp.11,21 | Continuous severity11-items=4intensity+7interference, continuous intensity4-items, continuous interference7-items;3,6,12; active/UC | Item arithmetic4+7=11; continuous versus responder outcomes distinguished. Three-month primary time for secondary outcomes does not change their secondary status. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S418 | PLAN P pp.13,19,23,57; PLAN A pp.8,12,21 | Secondary social roles PROMIS4A4-items and physical function6b6 items; baseline3,6,12; active/UC | Instruments/status/times and continuous linear models reconcile. Neither fitted value nor a scale-to-estimand conflict printed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S419 | PLAN P pp.23,57; PLAN A pp.4,12,21 | Secondary PGIC1item each pain/overall status, follow-up3,6,12; active/UC | July2024 amendment explicitly changes descriptive item count to2 and says actual assessments unchanged. Binary cutpoint not printed in PLAN; no inferential value can be calculated from it. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S420 | PLAN P pp.25,59; PLAN A pp.12,23 | Exploratory opioid continuous≥60-day supply in prior90 days, EHR quarterly; baseline and3,6,9,12 definitions; analysis3,6,12 | Windows contain90 days;9month measurement need not be a distinct analysis. Baseline day0 versus day1 origin retained and not assumed interchangeable data. No reported opioid estimate assigned here. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S421 | PLAN P pp.13,19,25,59; PLAN A pp.8,12–13,23 | Exploratory PHQ8, GAD7, PROMIS sleep6a, HICP/graded pain; baseline/3/6/12; active/UC | Explicit exploratory/tertiary status and same secondary-model approach mapped. HICP scoring thresholds absent here; no conflicting result printed. P_R outcome-status/omission review handed off. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S422 | PLAN P pp.56–57; PLAN A pp.20–21 | Primary modified Poisson GEE binary responders; Poisson log link, RR interest, robust sandwich, independent working correlation | Binary data with Poisson mean and robust variance explicitly described; do not substitute logistic/crude estimates or reject internally coherent choice. No coefficients/SE/test values printed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S423 | PLAN P p.56; PLAN A pp.20–21 | Primary covariates: baseline severity, sex/site/rural-MUA strata, multisite pain, mental-health condition | Text and Z-vector mean equation agree. Categories defined in outcome/strata tables. No unreported covariate coding is inferred. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S424 | PLAN A pp.20–21; PLAN P p.56 | Equation β0+β1Int1+β2Int2+β3T6+β4T12+β5Int1T6+β6Int2T6+β7Int1T12+β8Int2T12+βzZ; UC/3-month refs | log RR at3-months β1,β2;6-months β1+β5,β2+β6;12-months β1+β7,β2+β8. Equation has ordered explicit time coding; numerical covariance unavailable so no contrast SE inferred. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S425 | PLAN A pp.2,20–21; PLAN P pp.56–57 | Independent working correlation; robust sandwich accounts for within-person and within-health-coach dependence | Explicit accounting exists; finest implementation/cluster IDs absent but no printed claim conflicts. Main p.4 states highest-level clustering. Coherent nesting is not replaced by assumed covariance. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S426 | PLAN P p.57; PLAN A p.21 | Secondary longitudinal GEE linear continuous/Poisson binary/count; independent working correlation; intervention×time; baseline severity/all strata | Outcomes/models fit stated data structure; adjustment list differs in scope from primary predictors because secondary paragraph is its own specification. P_R reported prespecification review assigned crosschecker. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S427 | PLAN P pp.41,56; PLAN A pp.18,21 | Effectiveness ITT eligible as randomized; no modifiedITT; all randomized regardless exposure/engagement | Eligibility qualification, intervention discontinuation and study withdrawal distinguished. No plan-internal conflict with adherence-based selection; as-treated is a separate conditional sample. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S428 | PLAN A pp.18,25–26; PLAN P pp.49–50 | Primary safety all randomized; secondary excludes intervention ineligibility preventing continuation | Primary and secondary safety samples explicitly distinguished. No silent denominator mapping assumed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S429 | PLAN A p.18; PLAN P pp.33,46 | As-treated/per-protocol considered only if>10%UC outside-CBT crossover; otherwise unrestricted after enrollment | Conditional plan is internally coherent; no assertion trigger occurred. Reported counterpart review belongs crosschecker. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S430 | PLAN P pp.19,42–45; PLAN A pp.9,18 | Adherence≥6of8=75%; programs8 sessions approximatelyweekly8 weeks, intended max12 weeks with documented exceptions | Threshold6/8=.75; extensions, online availability and treatment intention distinguish dose/period. No inferential per-protocol estimate stated here. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S431 | PLAN P pp.3,16,47; PLAN A pp.8,11–13 | Follow-up3/6/12-months; protocol windows80–140/170–230/350–410days; notification after randomization | Windows ordered and distinct; baseline/randomization precede follow-up. Prespecified measurement windows separate from nominal time labels. No actual outcome-window discordance assigned here. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S432 | PLAN A pp.4,19; PLAN P pp.41,56 | Observed-follow-up primary, MAR given covariates; trigger>15%3-month or differential missingness;12.1%all-time missing at amendment | Missing-all count is amendment rationale, not current result denominator. Follow-up availability versus all-randomized estimand/sensitivity distinguished by explicit missing-data methods. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S433 | PLAN A p.19 | Pattern-mixture relaxing MAR conditioned on patterns among≥1follow-up; IPW for missing all follow-ups | Two disjoint availability patterns explicitly covered; numeric imputation count, IPW covariate model/truncation and pattern parameters absent. Missing detail alone is not a conflict; report matching delegated. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S434 | PLAN A p.19 | Extreme sensitivity missing active=nonresponse, missing UC=response at each missingtime | Directions minimize favorable active-vsUC response difference as stated. No fitted sensitivity output or CI/P conflict in PLAN. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S435 | PLAN A p.21; PLAN P p.43 | Enhanced PT onboarding8/9/2021 after~140enrolled; primary analysis repeat randomized after date; ITT retained | Date specifies subset independently of approximate historical enrollment count. REPORT subset/date/counterpart numerical review delegated; no alternative date inferred. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S436 | PLAN A pp.19–20; PLAN P p.56 | Descriptives arm-specific means/SD/median/range/count/percentage; no survey outlier changes; economic99th-percentile Winsor sensitivity | Plan uses outcome-type-specific descriptive and sensitivity rules. No printed outlier treatment/result contradiction. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S437 | PLAN P pp.25–26,57–58; PLAN A pp.14,20–22 | Moderator sex male/female-other; EHRstrata sex separate; age<65/≥65; race WhiteNH/BlackNH/Hispanic/Other | All explicit subgroup partitions mapped; self-report moderator versus EHRstrata source difference is stated, not a conflict. No subgroup fitted coefficients printed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S438 | PLAN P pp.26,34,57–58; PLAN A pp.14,20–22 | Urban versus rural/MUA; RUCA4–10 rural; MUAHRSA geography/highneeds shortage area | Source definitions and model target match; urban RUCA1–3 distinct from MUA rule. No inferred exclusive count decomposition. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S439 | PLAN P pp.26,57–58; PLAN A pp.14,20–22 | Single versus>1pain cluster; prior360 days; back,neck,limb/joint/arthritis,fibromyalgia,headache,orofacial/TMJ,chest,general pain | Eight named clusters; SAP list numbering1,3–9 retained. Numbering alone does not change the named operational categories or imply a missing outcome value. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S440 | PLAN P pp.26,57–58; PLAN A pp.14,20–22 | Mood: ICDdepression/anxiety prior360 days; SDOH≥1needs domain, itemcounts1+2+2+3 | Group definitions and planned interactions explicitly map; domain endorsement rather than item sum is classifier. No confusion with PHQ/GAD exploratory thresholds inferred. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S441 | PLAN P pp.25,57–58; PLAN A pp.14,20–22 | Seven separate moderators; main moderator plus moderator×arm×time; primary interaction contrasts3-months; protocoltable says6-months | Interaction structure can generate time-specific effects3/6/12. Protocoltable/analysis time-point observation is plan-internal ancillary scope without reported subgroup result in current REPORT map; exclusion recorded. Omission evaluation belongs crosschecker. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S442 | PLAN P pp.13,19,57–58; PLAN A pp.8,21–22 | Directional moderation hypothesis HC better than PT for complex/mood/multisite/rural-MUA/socialneed groups | This directional prospective hypothesis differs from the model's omnibus/moderator interaction tests without constituting a printed result reversal. No completed subgroup claim supplied here. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S443 | PLAN P pp.27,47,58; PLAN A pp.15,22–23 | Mediation: catastrophizing6 items/self-efficacy5 items baseline→3-month; perceivedsupport2 items notification→3-month;6-month severityMCID | Mediator antecedence to6-month outcome coherent; notification is explicitly perceived-support baseline, not prereandomization assessment. Ancillary mediation result absent here. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S444 | PLAN P p.58; PLAN A p.22 | Separate active/UC mediation; only intervention significant6-month outcome; primary6-month severityMCID/explanatory other6-month outcomes | Stated selection/framework mapped without preferred causal-method critique. No NI/equivalence or unprinted significance criterion invented. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S445 | PLAN A p.22 | MediationStep1 logE(Y)=β0+β1Int+βzZ,6-month binary; association required | Model matches defined binary responder and active/UC contrast; Z baseline adjustment vector supplied. No fitted estimate/SE/CI/P. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S446 | PLAN A pp.22–23 | Step2 E(M)=βM0+βM1Int+βMzZ, linear mediator change; include if either armP<.10 | Selection level.10 distinct from main testing.05; continuous change model fits defined measures. No observed selected mediators or selection Pvalues printed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S447 | PLAN A p.23 | Step3a logistic treatment on selected mediators; prose adjusting baseline confounders; equationβW0+βWMMsub withoutZ | Exact text/equation discrepancy retained; it is an ancillary plan method with no reported mediation result in current main map. Excluded as peripheral, not an assumed fitted-number reconciliation. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S448 | PLAN A p.23 | Weight active1/expit(η), UC1/[1−expit(η)],η=βW0+βWMMsub | Formula matches assigned-group inverse probability, positive for finiteη. No actual coefficients, mediator covariance, weights or truncation threshold supplied; no numeric check inferred. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S449 | PLAN A p.23 | Step3weighted6-month response model same mean asStep1; weighted/unweighted effects compare mediation; each mediator independently | Models and weights linked explicitly; decomposition algorithm beyond the multivariate/independent wording not numerically printed. No completed mediation number to attach a method finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S450 | PLAN P pp.24,58–59; PLAN A pp.13,23–24 | Economic12-month additional30%severityresponders and QALY, EQ5D5Lbaseline3/6/12; active eachother/UC | Cost-effectiveness outcome and times reconcile across plans; Aim2 separately prospective. No reported ICER/QALY input, fitted economic result or status change decided here. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S451 | PLAN P pp.58–59; PLAN A pp.23–24 | Health-plan perspective; KP administrative data; Essentia contingent on data comprehensiveness; process/training/delivery/care costs | Conditional site inclusion in SAP distinguishes eligibility for economic ancillary analysis from effectiveness population. No actual economic denominator supplied. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S452 | PLAN P pp.58–59; PLAN A p.24 | Netbenefit nb=λeffect−cost; CEAC,WTP$30000–100000/QALY examples | Formula units/cost-effect direction agree: increasing effect increases netbenefit atpositiveλ. Example WTP range is not stopping or significance margin. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S453 | PLAN P p.59; PLAN A pp.19,24 | Economic GEE appropriate links, costs overall/pain-specific; settings/replication/scale sensitivity;99th-percentile Winsor | Exact links/distributions not stated; no conflicting fitted result. No preferred cost model introduced. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S454 | PLAN P p.59; PLAN A pp.24–25 | Empty cost table pain-related/total columns; pharmacy,primarycare,PT/OT/physiatry,painclinic,mentalhealth/addiction,ER,other,inpatient | Empty cells are prospective placeholders, not zero counts. Footnotes partition categories as described; no total arithmetic possible. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S455 | PLAN P pp.49–51; PLAN A pp.25–26 | SAEdeath/inpatienthospitalization activeparticipation; pre-enrollmentplanned hospitalization excluded; EHR6-monthly,selfreport | Definition/window/source mapped; event counts and subjects are distinct summary quantities. No observed counts printed except historical rationale. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S456 | PLAN P p.50; PLAN A pp.3,26 | Protocol routine death/hospitalization physician review; SAP amendment removes routine hospitalization review, all deaths reviewed | Explicit October2020 amendment and SAPprecedence resolve hospital-review difference. It does not change the defined SAE event or primary decision rule. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S457 | PLAN P pp.49–51; PLAN A pp.25–26 | AE unequalcontact, not uniformlysolicited; no meaningful betweenarmAE tests; SAEdescriptives no formaltests/no safetyNI | Safety tests intentionally absent, internally coherent. Distinguish systematicSAE from unsolicitedAE. No NI margin or safety superiority claim supplied in PLAN. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S458 | PLAN P pp.50–51; PLAN A pp.25–26 | Related/possiblyrelated/notrelated; mild/moderate/severe; expectedness; frequency/subjects/timing byarm | Categories have explicit definitions; no aggregation/distribution values to reconcile. No mediator/result labels inferred from safety categories. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S459 | PLAN P pp.53,59–60; PLAN A pp.25–27 | DSMBtwiceyearly; unexpectedANDrelatedSAE notification; temporary suspension recommendations; no numeric efficacy/futility boundary | Safety monitoring and operational halting are distinct from formal efficacy interim tests. No unsupported alpha-spending/stopping calculation. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S460 | PLAN P p.60; PLAN A p.27 | No planned primary/secondary interim analysis; safety-requested effectiveness estimates permitted; noformal efficacy/futility analyses | Statements reconcile; requested estimates do not assert prespecified sequential testing. No reported interim conclusion in PLAN. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S461 | PLAN P pp.3–5,32–33,37,66; PLAN A pp.2–3,17–18 | Age≥18; English;360-dayhealthsystem/painlookback;KP≥2 encounters>60 days,Essentia≥1; surgery60 days; cancer≥2 encounters60 days; no hospice360 days/OUDKPWA | Currenteligibility thresholds mapped; protocolhistory30-dayversuscurrent60-day apparent difference retained as peripheral history comparison; SAPhistory/current60-day agrees. Actual eligibility/population comparison assigned crosschecker. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S462 | PLAN P pp.32–33,37; PLAN A pp.17–18 | HICPmost/everydaypainANDlimitation3-months; PEG≥12; CBTprior6-months/current/nextmonth excluded; substancecare current/nextmonth; planned painsurgery12-months | Operational eligibility rules coherent; PEGthreshold distinct from BPIseveritystratum7 and MCID30%outcome. No threshold substitution. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S463 | PLAN P pp.27–28,35–36,47–48,61–62; PLAN A p.9 | Qualitative purposeful sampling response/site/arm/residence; approximately120 patients,20 stakeholders,12 staff; reach denominatorsapproached/eligible; noSAPqualitative tests | Ancillaryqualitative/context scope inspected; no numeric effectiveness estimate or inferential test. RE-AIM/TFAframeworkcount wording outside quantitative result/design scope. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S464 | PLAN P pp.30–31,49,65–77; PLAN A pp.5–7,28–29 | Historical feasibility d.43/.33; historicalOR5.0(95%CI2.0–12.5),OR5.4(2.3–12.8); PPACT850,12deaths,287hospitalizations=116+171; remaining admin/references | HistoricalORpoints contained and endpointsordered; historicalhospitalizations116+171=287. No source result from references inferred; remainingpages notapplicable to inferential review. Clinical/background interpretation and administrative framework comparisons not findings. | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Diagnostic calculations and mechanical limits

For power only, a labelled diagnostic normal approximation for two independent proportions used n=[z(.975)√(2p̄(1−p̄))+z(power)√(p0(1−p0)+p1(1−p1))]^2/(p1−p0)^2. With printed primary probabilities it yields567.072/arm; adding the standard continuity-correction diagnostic n/4[1+√(1+4/(nΔ))]^2 yields593.439/arm. For the three printed subgroup tuples it yields uncorrected107.410,162.244,217.359/arm or continuity-corrected119.583,177.643,235.513/arm, compared with printed124,186,248/arm. These are diagnostics, not source-established algorithms or fitted-result reproduction. No one unspecified routine is asserted to reproduce other rows exactly. The primary report explicitly describes10,000 modified-Poisson simulations; dependence/covariate/cluster-generation inputs, exact omnibus gate simulation and definition of successful detection are unavailable. These approximations do not establish a reporting issue under the stated-method rule.

All arithmetic tuple checks used half-unit rounding intervals. Subgroup differences can range respectively15.9–16.1,12.6–12.8,10.7–10.9percentagepoints; ratio intervals respectively205.648–207.692,183.721–185.619,171.096–172.910%, each overlapping printed16.0/12.7/10.8and206.7/184.7/172.0 half-unit intervals. Subgroup-size percentages computed from integer half-unit intervals similarly overlap the printed20/30/40% intervals. Gap zero, relative discrepancy zero for each reconciled tuple. No point-estimate/CI/P/test tuple from the actual trial is printed in PLAN. No priors, NI/equivalence margin, fittedSE, df, covariance matrix, interim efficacy boundary or stopping-test outcome is supplied. Their absence is precisely recorded and never converted into an assumed contradiction.

## Source confirmation provenance and limitations

Critical sources were independently read visually from current fresh PyMuPDF1.26.4 CPU renders: protocol p.25, p.55, p.58 and SAP pp.11, 14, 15, 16, 18, 19, 20, 21, 22, 23. Source images control the printed relationships; new maps serve as locators. Main p.4 current source render was independently read for the simulation/method description only. No new OCR, Python review orchestration, external literature or web used. PLAN native/layout glyph encoding remains a derivative limitation, covered by the complete current visual maps and targeted source confirmation. No scientific coverage gap in the assigned 106 PLAN pages. This shard emits0 findings and 10 excluded observations; exclusions are in checkers/parts/stat1_plans.md. Fitted REPORT relationships and cross-source status/omission judgments remain with their assigned peers.


<!-- Complete pass1 inventory: raw -->

# Statistical relationship inventory — raw-score shard, pass 1

Runtime task: `/root/stat1_raw`; fresh `gpt-6.1-sol` / `high`. Exact scope: REPORT DOC-005 physical PDF pp.17–18, eTable11, all21 outcome/timepoint rows, every raw-score summary, unadjusted mean difference/95%CI, omnibus P, title/column header and both notes. Context only: REPORT DOC-005 pp.2,4–5,15; REPORT DOC-001 pp.4,11 definitions/methods. Other results displays are outside this shard.

Direct authority: [eTable11](../../../joi250046supp4_prod_1755300121.15587.pdf#page=17) and [notes](../../../joi250046supp4_prod_1755300121.15587.pdf#page=18). Columns below follow printed headings exactly: raw PT;HC;UC, and differences PT−UC;HC−UC;HC−PT. Descriptive summaries are labeled median (25th,75th percentile); inferential entries are GEE unadjusted means/95%CI. No SMD column occurs. Omnibus P is distinct from pairwise P. No standard-error or test-statistic values are printed. Three-month footnote means primary timepoint, not a change of outcome status.

Every row received estimate containment, endpoint order, descriptive quantile order, additive contrast, null/omnibus level, scale/direction and method checks. All63 model point estimates lie within ordered intervals; all63 raw centers lie inside ordered reported percentile bounds. Rounded contrast additivity is feasible for all21 rows. No pairwise P is printed, so omnibus-versus-single-contrast significance is not treated as the same test. Physical3 has all pairwise CIs including zero with nonsignificant omnibusP; all other rows have at least one CI excluding zero with significant omnibusP. Unrounded exact Wald compatibility requires test/CI/variance definitions not expressly assigned to eTable11; seeS625. Pain/PGIC negative contrasts favor the first named group, social/physical positive contrasts favor it, under supplied scale direction; group summaries cannot alone establish model mean direction.

| S ID | Exact REPORT location, outcome/month | Printed raw PT;HC;UC summaries | Printed unadjusted differences/95%CIs PT−UC;HC−UC;HC−PT | Omnibus P | Pass1 outcome | Pass1 status |
|---|---|---|---|---|---|---|
| S601 | DOC-005 p17, eTable11 Pain Severity, 3 months | 5.1 (4.9, 5.2); 4.6 (4.4, 4.7); 4.6 (4.5, 4.7) | −0.5 (−0.7, −0.3); −0.5 (−0.7, −0.3); 0.0 (−0.2, 0.2) | <0.001 | Common tuple checks complete; no direct containment/order/additivity/null-level conflict. | PASS_1_COMPLETE |
| S602 | DOC-005 p17, eTable11 Pain Severity, 6 months | 5.0 (4.8, 5.1); 4.4 (4.2, 4.6); 4.4 (4.2, 4.5) | −0.6 (−0.8, −0.3); −0.6 (−0.8, −0.3); −0.0 (−0.2, 0.2) | <0.001 | Common tuple checks complete; no direct containment/order/additivity/null-level conflict. | PASS_1_COMPLETE |
| S603 | DOC-005 p17, eTable11 Pain Severity, 12 months | 4.8 (4.6, 4.9); 4.2 (4.1, 4.4); 4.3 (4.2, 4.5) | −0.5 (−0.8, −0.3); −0.4 (−0.6, −0.2); 0.1 (−0.1, 0.3) | <0.001 | Common tuple checks complete; no direct containment/order/additivity/null-level conflict. | PASS_1_COMPLETE |
| S604 | DOC-005 p17, eTable11 Pain Intensity, 3 months | 4.9 (4.7, 5.0); 4.5 (4.3, 4.6); 4.5 (4.4, 4.6) | −0.4 (−0.6, −0.2); −0.3 (−0.5, −0.1); 0.0 (−0.2, 0.2) | <0.001 | Common tuple checks complete; no direct containment/order/additivity/null-level conflict. | PASS_1_COMPLETE |
| S605 | DOC-005 p17, eTable11 Pain Intensity, 6 months | 4.8 (4.6, 4.9); 4.4 (4.2, 4.5); 4.4 (4.3, 4.5) | −0.4 (−0.6, −0.2); −0.4 (−0.6, −0.2); −0.0 (−0.2, 0.2) | <0.001 | Common tuple checks complete; no direct containment/order/additivity/null-level conflict. | PASS_1_COMPLETE |
| S606 | DOC-005 p17, eTable11 Pain Intensity, 12 months | 4.6 (4.4, 4.7); 4.2 (4.1, 4.4); 4.3 (4.2, 4.4) | −0.3 (−0.6, −0.1); −0.2 (−0.4, −0.1); 0.1 (−0.1, 0.3) | <0.001 | Common tuple checks complete; no direct containment/order/additivity/null-level conflict. | PASS_1_COMPLETE |
| S607 | DOC-005 p17, eTable11 Pain-related Interference, 3 months | 5.2 (5.0, 5.3); 4.6 (4.4, 4.8); 4.6 (4.5, 4.7) | −0.6 (−0.8, −0.3); −0.6 (−0.8, −0.4); 0.0 (−0.2, 0.2) | <0.001 | Common tuple checks complete; no direct containment/order/additivity/null-level conflict. | PASS_1_COMPLETE |
| S608 | DOC-005 p17, eTable11 Pain-related Interference, 6 months | 5.1 (4.9, 5.2); 4.4 (4.2, 4.6); 4.4 (4.2, 4.6) | −0.7 (−0.9, −0.4); −0.7 (−0.9, −0.4); −0.0 (−0.3, 0.2) | <0.001 | Common tuple checks complete; no direct containment/order/additivity/null-level conflict. | PASS_1_COMPLETE |
| S609 | DOC-005 p17, eTable11 Pain-related Interference, 12 months | 4.9 (4.7, 5.1); 4.2 (4.0, 4.4); 4.3 (4.2, 4.5) | −0.6 (−0.9, −0.4); −0.5 (−0.8, −0.3); 0.1 (−0.1, 0.3) | <0.001 | Common tuple checks complete; no direct containment/order/additivity/null-level conflict. | PASS_1_COMPLETE |
| S610 | DOC-005 p17, eTable11 Social Role Functioning, 3 months | 43.4 (42.8, 44.0); 44.6 (43.9, 45.3); 44.8 (44.4, 45.2) | 1.2 (0.3, 2.1); 1.4 (0.7, 2.2); 0.2 (−0.5, 1.0) | 0.001 | Common tuple checks complete; no direct containment/order/additivity/null-level conflict. | PASS_1_COMPLETE |
| S611 | DOC-005 p17, eTable11 Social Role Functioning, 6 months | 43.6 (42.9, 44.2); 45.4 (44.7, 46.0); 45.1 (44.7, 45.4) | 1.8 (0.9, 2.7); 1.5 (0.8, 2.2); −0.3 (−1.0, 0.4) | <0.001 | Common tuple checks complete; no direct containment/order/additivity/null-level conflict. | PASS_1_COMPLETE |
| S612 | DOC-005 p17, eTable11 Social Role Functioning, 12 months | 43.9 (43.3, 44.6); 45.8 (45.1, 46.5); 45.3 (44.8, 45.8) | 1.8 (0.9, 2.8); 1.4 (0.5, 2.2); −0.5 (−1.3, 0.3) | <0.001 | Common tuple checks complete; no direct containment/order/additivity/null-level conflict. | PASS_1_COMPLETE |
| S613 | DOC-005 p17, eTable11 Physical Functioning, 3 months | 37.7 (37.1, 38.2); 38.2 (37.7, 38.8); 38.2 (37.7, 38.8) | 0.6 (−0.2, 1.3); 0.6 (−0.2, 1.3); 0.0 (−0.8, 0.8) | 0.212 | Common tuple checks complete; no direct containment/order/additivity/null-level conflict. | PASS_1_COMPLETE |
| S614 | DOC-005 p17, eTable11 Physical Functioning, 6 months | 37.9 (37.3, 38.4); 38.9 (38.4, 39.5); 38.3 (37.8, 38.8) | 1.1 (0.3, 1.9); 0.4 (−0.3, 1.1); −0.6 (−1.4, 0.1) | 0.005 | Common tuple checks complete; no direct containment/order/additivity/null-level conflict. | PASS_1_COMPLETE |
| S615 | DOC-005 p17, eTable11 Physical Functioning, 12 months | 37.9 (37.3, 38.4); 39.1 (38.5, 39.7); 38.8 (38.1, 39.4) | 1.2 (0.4, 2.0); 0.9 (0.0, 1.8); −0.3 (−1.2, 0.6) | 0.001 | Common tuple checks complete; no direct containment/order/additivity/null-level conflict. | PASS_1_COMPLETE |
| S616 | DOC-005 p17, eTable11 PGIC – Pain, 3 months | 2.9 (2.8, 2.9); 2.0 (1.0, 3.0); 1.9 (1.9, 2.0) | −0.8 (−0.9, −0.6); −0.9 (−1.0, −0.8); −0.2 (−0.3, −0.0) | <0.001 | Common tuple checks complete; no direct containment/order/additivity/null-level conflict. | PASS_1_COMPLETE |
| S617 | DOC-005 p17, eTable11 PGIC – Pain, 6 months | 2.8 (2.7, 2.9); 2.1 (2.0, 2.2); 2.1 (2.0, 2.2) | −0.7 (−0.8, −0.5); −0.7 (−0.8, −0.5); −0.0 (−0.2, 0.1) | <0.001 | Common tuple checks complete; PGIC statistic identity linked to F-ST1-601. | PASS_1_COMPLETE |
| S618 | DOC-005 p17, eTable11 PGIC – Pain, 12 months | 2.8 (2.7, 2.9); 2.1 (2.0, 2.2); 2.2 (2.1, 2.3) | −0.7 (−0.8, −0.5); −0.6 (−0.7, −0.4); 0.1 (−0.1, 0.2) | <0.001 | Common tuple checks complete; PGIC statistic identity linked to F-ST1-601. | PASS_1_COMPLETE |
| S619 | DOC-005 p17, eTable11 PGIC – General, 3 months | 2.7 (2.6, 2.7); 2.0 (1.0, 2.0); 1.6 (1.5, 1.6) | −0.8 (−0.9, −0.6); −1.1 (−1.2, −1.0); −0.3 (−0.5, −0.2) | <0.001 | Common tuple checks complete; PGIC statistic identity linked to F-ST1-601. | PASS_1_COMPLETE |
| S620 | DOC-005 p17, eTable11 PGIC – General, 6 months | 2.5 (2.4, 2.6); 2.0 (1.9, 2.1); 1.8 (1.7, 1.9) | −0.6 (−0.7, −0.4); −0.8 (−0.9, −0.6); −0.2 (−0.3, −0.0) | <0.001 | Common tuple checks complete; PGIC statistic identity linked to F-ST1-601. | PASS_1_COMPLETE |
| S621 | DOC-005 p17, eTable11 PGIC – General, 12 months | 2.6 (2.4, 2.7); 1.9 (1.8, 2.1); 1.9 (1.7, 2.0) | −0.6 (−0.8, −0.4); −0.7 (−0.8, −0.5); −0.1 (−0.2, 0.1) | <0.001 | Common tuple checks complete; no direct containment/order/additivity/null-level conflict. | PASS_1_COMPLETE |

| S ID | Method/relationship scope | Source-grounded check and outcome | Pass1 status |
|---|---|---|---|
| S622 | eTable11 method/population; DOC005p15,17–18; DOC001p4 | P15 specifies no adjustment, weighting or imputation; p18 specifies unadjusted linear GEE for continuous outcomes. Individual repeated outcomes and HC clustering are described in main methods; no statement contradicts design. Exact eTable11 sample sizes, per-outcome missing-data denominators, working correlation and variance implementation are not supplied; absence alone is not a finding. | PASS_1_COMPLETE |
| S623 | Quantity/scale identity; DOC005p2,15,17; DOC001p11 footnotesf–i | PROMIS transformed T scores permit noninteger raw summaries; pain is item-average scale. PGIC is a single seven-category item. Five raw PGIC centers labeled medians remain outside the eligible ordinary median set beyond display precision; F-ST1-601. Other PGIC fractional centers are considered once in excluded observations. No external scoring definition used. | PASS_1_COMPLETE |
| S624 | Raw central values versus GEE contrasts; all21 eTable11 rows | Under the source medians-versus-means distinction, raw subtraction is not an authoritative mean-difference reproduction. Diagnostic permutation raw columns UC;PT;HC instead of printed PT;HC;UC makes all21 row contrast triples compatible with one-decimal rounding; it identifies an alternative requiring a statistic/arm-order definition, not an independently reproduced mismatch. | PASS_1_COMPLETE |
| S625 | eTable11 omnibus Ps, especially social3 and physical3/6/12 | Direct .05-level logic reconciles. A diagnostic normal-Wald, two-independent-contrast reconstruction can match social3 P=.001 and physical3 P=.212 within rounding but produces physical6 approxP=.015–.040 and physical12 approxP=.0036–.020 instead of .005/.001. Neither eTable11 CI reference distribution nor its omnibus test degrees of freedom/covariance/variance mapping is explicitly supplied. No exact inferential conflict is established without those assumptions; excluded conditional diagnostic. | PASS_1_COMPLETE |
| S626 | Multiplicity, superiority and decision logic; DOC001p11 footnotec, DOC005p17–18 | Main Table3 describes Fisher LSD gating by omnibusP<.05. No eTable11 narrative declares pairwise superiority for physical3 (omnibus .212). No noninferiority/equivalence margin, interim or stopping claim occurs in assigned display; no implied margin/test introduced. Sample-size reproduction is outside this raw-score scope. | PASS_1_COMPLETE |

## Tooling and limitations

Fresh CPU render engine: recorded fallback PyMuPDF1.26.4 via allowed workflow_1_6_2/scripts/pdf_tools.py,200dpi. Fresh source images preprocessing/stat1_raw/doc005_p017.png,doc005_p018.png,doc005_p015.png,main_p011.png. Fresh text engine same pinned PyMuPDF native extraction: main_p004.txt,main_p011.txt,doc005_p015.txt. Existing current source map was a transcription aid; p17/18 and finding source contexts were visually confirmed. No raw observations are supplied. Unknown exact GEE/CI/test implementation is named rather than inferred. No scientific source-unit coverage gap exists for assigned pp17–18; all21 tuples explicit. SAP is not needed to settle any assigned raw-score definition or arithmetic; no plan-versus-report result is emitted here.

Counts:26 stable S records(S601–S626);21 row-tuples with63 raw summaries,63 inferential estimate/CI tuples and21 omnibus Ps;1 consolidated finding subject to independent screening; excluded-observation count appears in the checker artifact. Pass2 is reserved for a different fresh agent and must revisit every listed S ID.



# Active pass2 records

<!-- Active complete pass2 inventory: main_early -->

# Statistical pass 2 relationship update — main early

Fresh agent: `/root/stat2_main_early`, gpt-6.1-sol/high, FRESH_SPAWN. Assigned scope: S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055. This part is owned by this agent; the coordinator performs the canonical merge.

Each record below uses the complete current `candidate_ledger.md` (C001–C017), `screening/inclusion_screen.md` (26 initial decisions), `verification/evidence_recheck.md` (17 facts), and `review_packets/checker_exclusions.md` (47 original rows), plus `review_packets/pass2_main_early_input.md`. Scope and contract read completely. These inputs are current-run evidence only. REPORT main is DOC-001; prospective protocol/SAP roles are PLAN; intervention/results/workbook roles are REPORT.

Direct sources: [main methods p.4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), [main binary results p.9](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), [main continuous results p.10](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), [continuation and definitions p.11](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11). Other exact locations are named individually below. Current native text is a locator; directly inspected current exact-source renders control the comparisons. Visual pages: DOC-001 1,3,4,5,7,8,9,10,11,12; native text covers remaining main pages and reference-only material. Five fresh main renders use pinned PyMuPDF1.26.4,200dpi,CPU; their engine record is `preprocessing/stat2_main_early/engine_record.md`. Other renders are current-run exact-source derivatives and were only read.

Checks in every applicable tuple: point containment; endpoint order; scale/reference-group direction; matching count and denominator meaning; estimate construction; stated 95% confidence/two-sided .05 level; omnibus versus pairwise test identity; Fisher-LSD gate; report/plan and cross-report candidate implications. Precision uses every displayed input/output half-unit and remaining gap/absolute printed value≤.05 as the screen, except category1. No SE, degrees of freedom, covariance, exact Wald reference distribution, estimand mapping or interval algorithm is supplied by convention. No NI/equivalence rule applies and no numerical interim/stopping boundary is stated in these main relationships.

### S001

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S001; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main pp.3–5: individual allocation, twelve coaches and highest-level GEE clustering reread; randomization unit and correlation unit are different explicitly stated quantities.
- Independent pass-2 calculation/logic: No additional count/model inconsistency. Coach count is not a cluster-randomization claim.
- Existing candidate and cross-lane implications: None.
- Unresolved definitions and limits: Exact cluster implementation/finite-sample sandwich correction not supplied; no numeric claim depends on importing either.
- New finding: None; no previously screened finding re-emitted.

### S002

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S002; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main pp.1,4,5,9–11: allocation/eligible/any-follow-up/model contributor headers compared.
- Independent pass-2 calculation/logic: 2333−2=2331;776+778+777=2331;643+690+703=2036. Observed-at-time totals are subsets of any-follow-up and need not equal weighted target population.
- Existing candidate and cross-lane implications: C002 affects therapeutic adherence percentage only; C007 affects primary missing-data hierarchy; C015 concerns supplementary subset count convention, not these full-trial denominators.
- Unresolved definitions and limits: Actual weight/model matrices unavailable; different denominator types are explicitly defined and not substituted.
- New finding: None; no previously screened finding re-emitted.

### S003

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S003; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main pp.1,3,7,9: primary severity threshold, baseline-to-three-month window and Table2 read.
- Independent pass-2 calculation/logic: ≥30% decrease on higher-worse scale means improvement; active/UC RR>1 favors active. Three primary intervals exclude1; stated superiority direction reconciles.
- Existing candidate and cross-lane implications: None beyond linked method candidates C005/C007; no new endpoint/status difference.
- Unresolved definitions and limits: No NI/equivalence margin applies.
- New finding: None; no previously screened finding re-emitted.

### S004

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S004; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main pp.3,4,7,11: intensity/interference, PROMIS and both one-item PGIC scale footnotes read.
- Independent pass-2 calculation/logic: Pain decreases, functioning increases and PGIC lower scores denote benefit. Since-start PGIC item is identifiable from adjacent footnotes; no competing numerical assignment established.
- Existing candidate and cross-lane implications: C006 preserves planned/reported secondary adjustment; C016 addresses supplementary raw-summary identity.
- Unresolved definitions and limits: PGIC has no prerandomization change-impression baseline. Outcome-specific baseline adjustment applicability is retained in C006 rather than assumed.
- New finding: None; no previously screened finding re-emitted.

### S005

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S005; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 sample-size paragraph read.
- Independent pass-2 calculation/logic: 777×3=2331;15%+7.5 percentage points=22.5%;.225/.15=1.5. Source states10000 modified-Poisson simulations/Fisher LSD, so a normal two-proportion calculation is diagnostic only.
- Existing candidate and cross-lane implications: No additional candidate; original simulation exclusion retained.
- Unresolved definitions and limits: Full data-generating specification, random seed, joint gate/success criterion and simulation fit details absent;90% exact power cannot be independently rebuilt.
- New finding: None; no previously screened finding re-emitted.

### S006

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S006; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 model description and p.9 footnotes read.
- Independent pass-2 calculation/logic: Modified Poisson/GEE, independence working correlation and robust highest-level sandwich structure are explicitly coherent with repeated measures and coach clustering. Omnibus Wald differs from pairwise CI contrasts.
- Existing candidate and cross-lane implications: C005/C007 concern specification/primary-role comparisons, without changing this source-stated model family.
- Unresolved definitions and limits: No numerical standard error, test statistic, exact reference distribution, df or covariance supplied; none inferred.
- New finding: None; no previously screened finding re-emitted.

### S007

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S007; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 primary/secondary covariate descriptions reread, matched to complete ledger/recheck.
- Independent pass-2 calculation/logic: Six stated main factors plus secondary baseline adjustment are identified. Do not substitute crude ratios.
- Existing candidate and cross-lane implications: C005: prespecified age differs in report/plan/full supplement sets; C006: per-outcome baseline addition differs from explicit plan wording. Both remain present, without re-emission.
- Unresolved definitions and limits: Final per-outcome design matrices and prospective expanded specification absent; primary-factor inheritance is a source-grounded alternative.
- New finding: None; no previously screened finding re-emitted.

### S008

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S008; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 and Table2/3 footnotes pp.9/11 reread.
- Independent pass-2 calculation/logic: Covariates centered at means; model-adjusted predictions/contrasts target randomized population. Each Table2 RR point agrees with corresponding adjusted percentage ratio under half-unit bounds.
- Existing candidate and cross-lane implications: C005/C007 concern covariate and missing-data mapping; existing estimate construction observations C003/C004 retain their local arithmetic.
- Unresolved definitions and limits: Unrounded predictors/predictions absent. Model-based quantities are not equated with crude counts.
- New finding: None; no previously screened finding re-emitted.

### S009

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S009; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 linear GEE and pp.10–11 adjusted mean/MD headings reread.
- Independent pass-2 calculation/logic: One-decimal group means and MDs can satisfy additive contrasts within their rounding intervals. Positive/negative effect direction follows each scale; no independent-samples analysis imported.
- Existing candidate and cross-lane implications: C003/C010 concern SMD construction/containment, distinct from the compatible adjusted mean/MD displays; C006 adjustment mapping retained.
- Unresolved definitions and limits: Fitted linear-model covariance/unrounded means not supplied; no exact omnibus P reconstructed.
- New finding: None; no previously screened finding re-emitted.

### S010

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S010; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 common UC-change SD definition; pp.10–11 SMD columns/footnote d reread.
- Independent pass-2 calculation/logic: Positive common denominator requires sign preservation and a+c=b. Severity3 gap .025/.34=.073529; severity6 HC−PT gap .005/.12=.041667 when recomputing from other two SMDs. Direct interval containment and ordering reviewed separately.
- Existing candidate and cross-lane implications: C003 retains twenty construction rows; C010 retains fourteen outside-interval tuples. F-ST1-003 descending-order-only observation already screened CONTEXT_RESOLVES and is not re-emitted.
- Unresolved definitions and limits: Exact UC-change SDs, unrounded contrasts and CI construction absent. No separate fitted contrast assignment or covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S011

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S011; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 reciprocal definition and p.9 all27 NNT tuples/footnotes read.
- Independent pass-2 calculation/logic: NNT=100/percentage-point difference. All points/endpoints ordered except existing containment63(18–38). Two local reciprocal gaps remain>.05; six matched RR/NNT null readings remain different.
- Existing candidate and cross-lane implications: C004 reciprocal points; C008 RR/NNT null-coverage ambiguity; C009 point containment. Distinct rules retained; no duplicate new finding.
- Unresolved definitions and limits: Risk-difference CI method/endpoints, integer convention, common covariance and parameter-specific analysis mapping absent. Different interval constructions remain alternatives.
- New finding: None; no previously screened finding re-emitted.

### S012

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S012; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 imputation/weighting paragraph read.
- Independent pass-2 calculation/logic: ≥1 follow-up pattern-mixture group and no-follow-up inverse-probability weighting group partition observation categories; weighting does not create direct raw observations.
- Existing candidate and cross-lane implications: C007 retains role hierarchy against SAP; C012/C013/C014 supplementary primary missing-data model membership/coding/test implications read in full recheck.
- Unresolved definitions and limits: Imputation/weight model matrices not supplied. Plan amendment support for current approach remains explicit alternative.
- New finding: None; no previously screened finding re-emitted.

### S013

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S013; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 missing-covariate sentence read.
- Independent pass-2 calculation/logic: Mean imputation is expressly stated and internally coherent. Encoding choices alone do not create a reproduced numeric or method contradiction.
- Existing candidate and cross-lane implications: No additional candidate.
- Unresolved definitions and limits: Categorical covariate coding under mean imputation unprinted; do not infer an encoding or propose a different method.
- New finding: None; no previously screened finding re-emitted.

### S014

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S014; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 and pp.9/11 inference footnotes read.
- Independent pass-2 calculation/logic: Two-sidedα=.05,95%CIs and three-group omnibus Wald explicitly identified. Pairwise intervals not treated as identical to omnibus P; no source-level pairwise P supplied.
- Existing candidate and cross-lane implications: C008/C009/C010 retain interval implications; C014 current supplementary interval/P conflicts read, not added to unrelated main rows.
- Unresolved definitions and limits: Exact df/covariance/test statistics/standard errors absent; pairwise P values not reconstructed.
- New finding: None; no previously screened finding re-emitted.

### S015

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S015; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 sample-size multiplicity and pp.9/11 Fisher-LSD footnotes; physical6 P=.05 on p.10 read.
- Independent pass-2 calculation/logic: All30 omnibus gates checked at printed precision;29<.05. Physical6 P interval[.045,.055] permits P<.05, so no reproduced gate breach. Omnibus and pairwise null patterns need not match.
- Existing candidate and cross-lane implications: No new multiplicity candidate; screened rounding observation retained.
- Unresolved definitions and limits: Unrounded physical6 omnibus P unavailable. No numeric interim/stopping boundary or NI/equivalence rule printed here.
- New finding: None; no previously screened finding re-emitted.

### S016

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S016; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.1 abstract, p.2 Key Points and p.9 primary row matched.
- Independent pass-2 calculation/logic: 32.0/26.6/20.8 and RR1.54/1.28/1.20 with their95%CIs match corresponding body estimates/contrasts; each primary RR CI excludes1.
- Existing candidate and cross-lane implications: No additional copy/significance issue; C005/C007 method-specification implications remain distinct.
- Unresolved definitions and limits: Pairwise P values are not supplied; absence does not conflict with CI-based superiority statements.
- New finding: None; no previously screened finding re-emitted.

### S017

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S017; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main pp.1,7–9,12 longitudinal narrative, Figure2 and Table2 severity rows read.
- Independent pass-2 calculation/logic: All six active/UC CIs exclude1; HC/PT3 excludes1,6/12 include1. Narrative uses corresponding primary-response inferential direction; no equivalence conclusion asserted.
- Existing candidate and cross-lane implications: C008 preserves finite NNT/null-containing HC/PT intervals at6/12; this does not alter correctly matched RR narrative.
- Unresolved definitions and limits: Figure has no extra printed test tuple; no covariance inferred from graph.
- New finding: None; no previously screened finding re-emitted.

### S018

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S018; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.7 narrative SMD−.26/−.36 and p.10 severity3−.25/−.34 read; pp.1,7–12 overall benefit text read.
- Independent pass-2 calculation/logic: Half-unit copy intervals touch/overlap forPT;HC gap.01/.34=.029412≤.05. Overall-pattern wording is not an explicit every-contrast significance claim.
- Existing candidate and cross-lane implications: C003 concerns within-Table3 construction, independently of these screened copy differences. No new narrative finding.
- Unresolved definitions and limits: Wording scope is not resolved by assuming a universal claim; wording doubt screened as specified.
- New finding: None; no previously screened finding re-emitted.

### S019

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S019; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.5 Figure1, p.8 Figure2 and p.9 Table2 matched.
- Independent pass-2 calculation/logic: All nine adjusted severity points/95%whiskers visually agree with Table2; contributor counts UC621/622/639,PT542/547/583,HC635/621/639 match Figure1. Time-specific observed counts differ by definition from any-follow-up.
- Existing candidate and cross-lane implications: No new count/figure issue. C015 pertains a different supplementary subgroup header.
- Unresolved definitions and limits: No numerical graph-only CI endpoint printed; visual agreement is not a pixel-derived exact test.
- New finding: None; no previously screened finding re-emitted.

### S020

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S020; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main pp.2–8,11–14 baseline/adverse results/scoring/remaining material revisited through native text and relevant renders.
- Independent pass-2 calculation/logic: Baseline SD/IQR labels distinct from inferential CIs; adverse events are descriptive. No HR/OR/rate/person-time, NI/equivalence or numerical SE/test-statistic/stopping tuple introduced in remaining main material.
- Existing candidate and cross-lane implications: C002 count/percentage issue retained; no additional inferential relationship hidden in baseline/reference material.
- Unresolved definitions and limits: All11-item versus minimum-item wording is identifiable instrument-scoring context; no reported score contradiction established.
- New finding: None; no previously screened finding re-emitted.

### S021

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S021; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Severity3 group adjusted percentages inPT/HC/UC order: 26.6(23.4–30.2),32.0(29.3–35.0),20.8(18.0–24.0); direct render reread.
- Independent pass-2 calculation/logic: Each point is contained, all endpoints ordered, rates in[0,100]. Source model-adjusted prediction definition preserved; count denominator is not substituted.
- Existing candidate and cross-lane implications: C005/C007 concern specification/analysis role; no new tuple-specific inconsistency.
- Unresolved definitions and limits: Unrounded adjusted predictions absent; no exact SE or raw-count identity imposed.
- New finding: None; no previously screened finding re-emitted.

### S022

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S022; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Severity3 PT/UC,HC/UC,HC/PTRRs: 1.28(1.06–1.55),1.54(1.30–1.82),1.20(1.03–1.40); omnibusP<.001; direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered; adjusted rate ratios reconcile within half-unit precision. All3 exclude1. OmnibusP passes the Fisher-LSD gate and is a3-group test, not a pairwiseP.
- Existing candidate and cross-lane implications: No additional tuple-specific candidate.
- Unresolved definitions and limits: No pairwiseP, covariance, df or exact contrast SE supplied; these are not inferred.
- New finding: None; no previously screened finding re-emitted.

### S023

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S023; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Severity3 PT/UC,HC/UC,HC/PTNNTs: 18(10–71),9(7–14),19(11–102); p.4 reciprocal rule/direct renders reread.
- Independent pass-2 calculation/logic: Every tuple's point containment, endpoint order, direction and reciprocal point checked with percentage±.05/integer±.5; findings are only existing implications below. Other reciprocal gaps≤.05 screened as one precision pattern.
- Existing candidate and cross-lane implications: None; point/interval checks reconcile.
- Unresolved definitions and limits: RD interval endpoints/construction, integer convention and any separate RR/RD mapping unprinted. Different parameter-specific interval methods retained; no joint covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S024

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S024; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Severity6 group adjusted percentages inPT/HC/UC order: 32.9(29.5–36.7),37.1(34.1–40.5),22.9(20.0–26.1); direct render reread.
- Independent pass-2 calculation/logic: Each point is contained, all endpoints ordered, rates in[0,100]. Source model-adjusted prediction definition preserved; count denominator is not substituted.
- Existing candidate and cross-lane implications: C005/C007 concern specification/analysis role; no new tuple-specific inconsistency.
- Unresolved definitions and limits: Unrounded adjusted predictions absent; no exact SE or raw-count identity imposed.
- New finding: None; no previously screened finding re-emitted.

### S025

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S025; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Severity6 PT/UC,HC/UC,HC/PTRRs: 1.44(1.21–1.70),1.62(1.39–1.90),1.13(.98–1.30); omnibusP<.001; direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered; adjusted rate ratios reconcile within half-unit precision. active/UC exclude1;HC/PT includes1. OmnibusP passes the Fisher-LSD gate and is a3-group test, not a pairwiseP.
- Existing candidate and cross-lane implications: C008 retains corresponding RR/NNT null-coverage ambiguity; no new RR/P assertion.
- Unresolved definitions and limits: No pairwiseP, covariance, df or exact contrast SE supplied; these are not inferred.
- New finding: None; no previously screened finding re-emitted.

### S026

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S026; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Severity6 PT/UC,HC/UC,HC/PTNNTs: 10(7–19),8(6–11),24(12–186); p.4 reciprocal rule/direct renders reread.
- Independent pass-2 calculation/logic: Every tuple's point containment, endpoint order, direction and reciprocal point checked with percentage±.05/integer±.5; findings are only existing implications below. Other reciprocal gaps≤.05 screened as one precision pattern.
- Existing candidate and cross-lane implications: C004: HC/UC37.1−22.9→NNT[6.993007,7.092199] versus8[7.5,8.5],gap.407801/8=.050975; C008:HC/PT finite interval vsRR including1.
- Unresolved definitions and limits: RD interval endpoints/construction, integer convention and any separate RR/RD mapping unprinted. Different parameter-specific interval methods retained; no joint covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S027

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S027; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Severity12 group adjusted percentages inPT/HC/UC order: 35.9(32.4–39.7),38.3(36.8–39.9),27.1(24.1–30.5); direct render reread.
- Independent pass-2 calculation/logic: Each point is contained, all endpoints ordered, rates in[0,100]. Source model-adjusted prediction definition preserved; count denominator is not substituted.
- Existing candidate and cross-lane implications: C005/C007 concern specification/analysis role; no new tuple-specific inconsistency.
- Unresolved definitions and limits: Unrounded adjusted predictions absent; no exact SE or raw-count identity imposed.
- New finding: None; no previously screened finding re-emitted.

### S028

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S028; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Severity12 PT/UC,HC/UC,HC/PTRRs: 1.32(1.13–1.54),1.41(1.25–1.59),1.07(.96–1.19); omnibusP<.001; direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered; adjusted rate ratios reconcile within half-unit precision. active/UC exclude1;HC/PT includes1. OmnibusP passes the Fisher-LSD gate and is a3-group test, not a pairwiseP.
- Existing candidate and cross-lane implications: C008 retains corresponding RR/NNT null-coverage ambiguity; no new RR/P assertion.
- Unresolved definitions and limits: No pairwiseP, covariance, df or exact contrast SE supplied; these are not inferred.
- New finding: None; no previously screened finding re-emitted.

### S029

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S029; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Severity12 PT/UC,HC/UC,HC/PTNNTs: 12(8–26),9(7–13),41(17–76); p.4 reciprocal rule/direct renders reread.
- Independent pass-2 calculation/logic: Every tuple's point containment, endpoint order, direction and reciprocal point checked with percentage±.05/integer±.5; findings are only existing implications below. Other reciprocal gaps≤.05 screened as one precision pattern.
- Existing candidate and cross-lane implications: C008:HC/PT finite interval vsRR including1.
- Unresolved definitions and limits: RD interval endpoints/construction, integer convention and any separate RR/RD mapping unprinted. Different parameter-specific interval methods retained; no joint covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S030

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S030; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Intensity3 group adjusted percentages inPT/HC/UC order: 24.3(21.2–27.8),27.0(24.0–30.5),17.7(15.1–20.7); direct render reread.
- Independent pass-2 calculation/logic: Each point is contained, all endpoints ordered, rates in[0,100]. Source model-adjusted prediction definition preserved; count denominator is not substituted.
- Existing candidate and cross-lane implications: C005/C007 concern specification/analysis role; no new tuple-specific inconsistency.
- Unresolved definitions and limits: Unrounded adjusted predictions absent; no exact SE or raw-count identity imposed.
- New finding: None; no previously screened finding re-emitted.

### S031

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S031; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Intensity3 PT/UC,HC/UC,HC/PTRRs: 1.37(1.12–1.69),1.53(1.26–1.86),1.11(.93–1.33); omnibusP<.001; direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered; adjusted rate ratios reconcile within half-unit precision. active/UC exclude1;HC/PT includes1. OmnibusP passes the Fisher-LSD gate and is a3-group test, not a pairwiseP.
- Existing candidate and cross-lane implications: C008 retains corresponding RR/NNT null-coverage ambiguity; no new RR/P assertion.
- Unresolved definitions and limits: No pairwiseP, covariance, df or exact contrast SE supplied; these are not inferred.
- New finding: None; no previously screened finding re-emitted.

### S032

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S032; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Intensity3 PT/UC,HC/UC,HC/PTNNTs: 16(10–43),11(8–20),37(14–57); p.4 reciprocal rule/direct renders reread.
- Independent pass-2 calculation/logic: Every tuple's point containment, endpoint order, direction and reciprocal point checked with percentage±.05/integer±.5; findings are only existing implications below. Other reciprocal gaps≤.05 screened as one precision pattern.
- Existing candidate and cross-lane implications: C008:HC/PT finite interval vsRR including1;PT/UC reciprocal gap.115385/16=.007212 screens out.
- Unresolved definitions and limits: RD interval endpoints/construction, integer convention and any separate RR/RD mapping unprinted. Different parameter-specific interval methods retained; no joint covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S033

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S033; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Intensity6 group adjusted percentages inPT/HC/UC order: 26.9(23.7–30.5),31.8(28.3–35.7),21.1(18.3–24.3); direct render reread.
- Independent pass-2 calculation/logic: Each point is contained, all endpoints ordered, rates in[0,100]. Source model-adjusted prediction definition preserved; count denominator is not substituted.
- Existing candidate and cross-lane implications: C005/C007 concern specification/analysis role; no new tuple-specific inconsistency.
- Unresolved definitions and limits: Unrounded adjusted predictions absent; no exact SE or raw-count identity imposed.
- New finding: None; no previously screened finding re-emitted.

### S034

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S034; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Intensity6 PT/UC,HC/UC,HC/PTRRs: 1.27(1.06–1.54),1.51(1.26–1.80),1.18(1.00–1.40); omnibusP<.001; direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered; adjusted rate ratios reconcile within half-unit precision. active/UC exclude1;HC/PT lower endpoint is printed1.00. OmnibusP passes the Fisher-LSD gate and is a3-group test, not a pairwiseP.
- Existing candidate and cross-lane implications: No additional tuple-specific candidate.
- Unresolved definitions and limits: No pairwiseP, covariance, df or exact contrast SE supplied; these are not inferred.
- New finding: None; no previously screened finding re-emitted.

### S035

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S035; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Intensity6 PT/UC,HC/UC,HC/PTNNTs: 18(10–76),10(7–17),21(11–5524); p.4 reciprocal rule/direct renders reread.
- Independent pass-2 calculation/logic: Every tuple's point containment, endpoint order, direction and reciprocal point checked with percentage±.05/integer±.5; findings are only existing implications below. Other reciprocal gaps≤.05 screened as one precision pattern.
- Existing candidate and cross-lane implications: None additional; HC/PT RR lower1.00 is rounded boundary and no pairwiseP printed. Finite NNT large upper limit is not itself a conflicting test.
- Unresolved definitions and limits: RD interval endpoints/construction, integer convention and any separate RR/RD mapping unprinted. Different parameter-specific interval methods retained; no joint covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S036

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S036; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Intensity12 group adjusted percentages inPT/HC/UC order: 32.1(28.7–35.8),33.7(31.2–36.3),26.4(23.4–29.8); direct render reread.
- Independent pass-2 calculation/logic: Each point is contained, all endpoints ordered, rates in[0,100]. Source model-adjusted prediction definition preserved; count denominator is not substituted.
- Existing candidate and cross-lane implications: C005/C007 concern specification/analysis role; no new tuple-specific inconsistency.
- Unresolved definitions and limits: Unrounded adjusted predictions absent; no exact SE or raw-count identity imposed.
- New finding: None; no previously screened finding re-emitted.

### S037

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S037; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Intensity12 PT/UC,HC/UC,HC/PTRRs: 1.21(1.03–1.43),1.28(1.11–1.47),1.05(.92–1.20); omnibusP.003; direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered; adjusted rate ratios reconcile within half-unit precision. active/UC exclude1;HC/PT includes1. OmnibusP passes the Fisher-LSD gate and is a3-group test, not a pairwiseP.
- Existing candidate and cross-lane implications: C008 retains corresponding RR/NNT null-coverage ambiguity; no new RR/P assertion.
- Unresolved definitions and limits: No pairwiseP, covariance, df or exact contrast SE supplied; these are not inferred.
- New finding: None; no previously screened finding re-emitted.

### S038

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S038; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Intensity12 PT/UC,HC/UC,HC/PTNNTs: 18(10–106),14(9–31),63(18–38); p.4 reciprocal rule/direct renders reread.
- Independent pass-2 calculation/logic: Every tuple's point containment, endpoint order, direction and reciprocal point checked with percentage±.05/integer±.5; findings are only existing implications below. Other reciprocal gaps≤.05 screened as one precision pattern.
- Existing candidate and cross-lane implications: C009:63>38;C008:HC/PT finite interval vsRR including1.
- Unresolved definitions and limits: RD interval endpoints/construction, integer convention and any separate RR/RD mapping unprinted. Different parameter-specific interval methods retained; no joint covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S039

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S039; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Interference3 group adjusted percentages inPT/HC/UC order: 30.6(27.3–34.4),35.6(33.7–37.6),23.4(20.5–26.8); direct render reread.
- Independent pass-2 calculation/logic: Each point is contained, all endpoints ordered, rates in[0,100]. Source model-adjusted prediction definition preserved; count denominator is not substituted.
- Existing candidate and cross-lane implications: C005/C007 concern specification/analysis role; no new tuple-specific inconsistency.
- Unresolved definitions and limits: Unrounded adjusted predictions absent; no exact SE or raw-count identity imposed.
- New finding: None; no previously screened finding re-emitted.

### S040

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S040; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Interference3 PT/UC,HC/UC,HC/PTRRs: 1.31(1.10–1.55),1.52(1.32–1.75),1.16(1.02–1.32); omnibusP<.001; direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered; adjusted rate ratios reconcile within half-unit precision. All3 exclude1. OmnibusP passes the Fisher-LSD gate and is a3-group test, not a pairwiseP.
- Existing candidate and cross-lane implications: No additional tuple-specific candidate.
- Unresolved definitions and limits: No pairwiseP, covariance, df or exact contrast SE supplied; these are not inferred.
- New finding: None; no previously screened finding re-emitted.

### S041

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S041; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Interference3 PT/UC,HC/UC,HC/PTNNTs: 14(9–40),9(7–12),21(12–100); p.4 reciprocal rule/direct renders reread.
- Independent pass-2 calculation/logic: Every tuple's point containment, endpoint order, direction and reciprocal point checked with percentage±.05/integer±.5; findings are only existing implications below. Other reciprocal gaps≤.05 screened as one precision pattern.
- Existing candidate and cross-lane implications: None; point/interval checks reconcile.
- Unresolved definitions and limits: RD interval endpoints/construction, integer convention and any separate RR/RD mapping unprinted. Different parameter-specific interval methods retained; no joint covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S042

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S042; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Interference6 group adjusted percentages inPT/HC/UC order: 37.0(33.5–40.9),40.9(37.0–45.1),24.3(21.3–27.6); direct render reread.
- Independent pass-2 calculation/logic: Each point is contained, all endpoints ordered, rates in[0,100]. Source model-adjusted prediction definition preserved; count denominator is not substituted.
- Existing candidate and cross-lane implications: C005/C007 concern specification/analysis role; no new tuple-specific inconsistency.
- Unresolved definitions and limits: Unrounded adjusted predictions absent; no exact SE or raw-count identity imposed.
- New finding: None; no previously screened finding re-emitted.

### S043

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S043; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Interference6 PT/UC,HC/UC,HC/PTRRs: 1.52(1.30–1.79),1.68(1.43–1.98),1.10(.96–1.27); omnibusP<.001; direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered; adjusted rate ratios reconcile within half-unit precision. active/UC exclude1;HC/PT includes1. OmnibusP passes the Fisher-LSD gate and is a3-group test, not a pairwiseP.
- Existing candidate and cross-lane implications: C008 retains corresponding RR/NNT null-coverage ambiguity; no new RR/P assertion.
- Unresolved definitions and limits: No pairwiseP, covariance, df or exact contrast SE supplied; these are not inferred.
- New finding: None; no previously screened finding re-emitted.

### S044

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S044; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Interference6 PT/UC,HC/UC,HC/PTNNTs: 8(6–13),7(5–9),26(11–67); p.4 reciprocal rule/direct renders reread.
- Independent pass-2 calculation/logic: Every tuple's point containment, endpoint order, direction and reciprocal point checked with percentage±.05/integer±.5; findings are only existing implications below. Other reciprocal gaps≤.05 screened as one precision pattern.
- Existing candidate and cross-lane implications: C004:HC/UC40.9−24.3→NNT[5.988024,6.060606] versus7[6.5,7.5],gap.439394/7=.062771;C008:HC/PT finite interval vsRR including1.
- Unresolved definitions and limits: RD interval endpoints/construction, integer convention and any separate RR/RD mapping unprinted. Different parameter-specific interval methods retained; no joint covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S045

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S045; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Interference12 group adjusted percentages inPT/HC/UC order: 39.6(36.1–43.5),42.3(40.6–44.0),30.6(27.4–34.2); direct render reread.
- Independent pass-2 calculation/logic: Each point is contained, all endpoints ordered, rates in[0,100]. Source model-adjusted prediction definition preserved; count denominator is not substituted.
- Existing candidate and cross-lane implications: C005/C007 concern specification/analysis role; no new tuple-specific inconsistency.
- Unresolved definitions and limits: Unrounded adjusted predictions absent; no exact SE or raw-count identity imposed.
- New finding: None; no previously screened finding re-emitted.

### S046

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S046; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Interference12 PT/UC,HC/UC,HC/PTRRs: 1.29(1.12–1.49),1.38(1.23–1.55),1.07(.97–1.18); omnibusP<.001; direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered; adjusted rate ratios reconcile within half-unit precision. active/UC exclude1;HC/PT includes1. OmnibusP passes the Fisher-LSD gate and is a3-group test, not a pairwiseP.
- Existing candidate and cross-lane implications: C008 retains corresponding RR/NNT null-coverage ambiguity; no new RR/P assertion.
- Unresolved definitions and limits: No pairwiseP, covariance, df or exact contrast SE supplied; these are not inferred.
- New finding: None; no previously screened finding re-emitted.

### S047

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S047; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Interference12 PT/UC,HC/UC,HC/PTNNTs: 12(8–25),9(7–13),39(16–79); p.4 reciprocal rule/direct renders reread.
- Independent pass-2 calculation/logic: Every tuple's point containment, endpoint order, direction and reciprocal point checked with percentage±.05/integer±.5; findings are only existing implications below. Other reciprocal gaps≤.05 screened as one precision pattern.
- Existing candidate and cross-lane implications: C008:HC/PT finite interval vsRR including1.
- Unresolved definitions and limits: RD interval endpoints/construction, integer convention and any separate RR/RD mapping unprinted. Different parameter-specific interval methods retained; no joint covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S048

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S048; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.10 severity3 adjustedPT−1.2(−1.3,−1.0),HC−1.2(−1.3,−1.1),UC−.8(−.9,−.6); direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered, lower-worse pain decreases indicate benefit; one-decimal mean/MD arithmetic compatible.
- Existing candidate and cross-lane implications: No new group tuple issue; C006 adjustment specification applies.
- Unresolved definitions and limits: Unrounded adjusted means/covariance absent.
- New finding: None; no previously screened finding re-emitted.

### S049

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S049; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.10 severity3 MDPT/UC−.4(−.6,−.2),HC/UC−.4(−.6,−.3),HC/PT−0.0(−.2,.1),omnibusP<.001;direct render reread.
- Independent pass-2 calculation/logic: Contained,ordered, directions agree. Group mean differences andMDs have overlapping rounding intervals. Active/UC CIs exclude0;HC/PT includes0;omnibus gate met.
- Existing candidate and cross-lane implications: No newMD/test candidate;C003 concerns paired SMDs.
- Unresolved definitions and limits: Exact df,covariance,SE andpairwiseP unprinted; not inferred.
- New finding: None; no previously screened finding re-emitted.

### S050

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S050; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.10 severity3 SMD−.25(−.28,−.02),−.34(−.36,−.13),−.13(−.15,.08),contrastPT/UC,HC/UC,HC/PT;direct render reread.
- Independent pass-2 calculation/logic: Contained/ordered;contrast signs follow pain reduction. Common-SD identityHC/UC=PT/UC+HC/PT predicts[−.390,−.370]vsprinted[−.345,−.335],gap.025/.34=.073529.
- Existing candidate and cross-lane implications: ExistingC003 includes this exact row; no re-emission.
- Unresolved definitions and limits: Actual UC-changeSD/unroundedMD/SMD/interval construction absent.
- New finding: None; no previously screened finding re-emitted.

### S051

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S051; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.10 severity6 adjustedPT−1.3(−1.4,−1.1),HC−1.4(−1.5,−1.3),UC−.9(−1.0,−.8);direct render reread.
- Independent pass-2 calculation/logic: Contained,ordered, higher-worse pain reduction direction coherent. Group mean/contrast rounding feasible.
- Existing candidate and cross-lane implications: No newgroup tuple issue;C006 applies.
- Unresolved definitions and limits: Unrounded adjustedmeans/covariance absent.
- New finding: None; no previously screened finding re-emitted.

### S052

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S052; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.10 severity6 MD−.4(−.6,−.2),−.5(−.7,−.4),−.1(−.3,.1),omnibusP<.001;direct render reread.
- Independent pass-2 calculation/logic: Contained,ordered;groupmeancontrast roundingfeasible. Active/UC exclude0;HC/PT includes0;three-group omnibusgate met.
- Existing candidate and cross-lane implications: No newMD/testcandidate;C003 reference row construction checked inS053.
- Unresolved definitions and limits: Exact SE/df/covariance/pairwiseP absent;not inferred.
- New finding: None; no previously screened finding re-emitted.

### S053

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S053; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.10 severity6 SMD−.26(−.34,−.08),−.36(−.43,−.19),−.12(−.19,.04);direct render reread.
- Independent pass-2 calculation/logic: Contained,ordered;additiveHC/PT fromotherSMDs[−.110,−.090]vs[−.125,−.115],gap.005/.12=.041667≤.05. MD/SMDscalingHC/PT gap.001429/.12=.011905≤.05. This row is precision-compatible.
- Existing candidate and cross-lane implications: C003 uses this reproducing reference row; original exclusionretained. No newcandidate.
- Unresolved definitions and limits: AbsoluteUC-changeSD unavailable; only scale-independent identities checked.
- New finding: None; no previously screened finding re-emitted.

### S054

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S054; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.10 severity12 adjustedPT−1.5(−1.6,−1.3),HC−1.4(−1.6,−1.3),UC−1.1(−1.2,−.9);direct render reread.
- Independent pass-2 calculation/logic: Contained,ordered;mean/MD roundingfeasible. Source pain direction coherent.
- Existing candidate and cross-lane implications: No newgroup issue;C003/C010 affectSMDcolumns in thisrow, assigned nextshard.
- Unresolved definitions and limits: Unroundedadjustedmeans/covariance absent.
- New finding: None; no previously screened finding re-emitted.

### S055

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S055; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.10 severity12 MD−.4(−.6,−.2),−.4(−.6,−.2),0.0(−.2,.2),omnibusP<.001;direct render reread.
- Independent pass-2 calculation/logic: Contained,ordered;groups/MDcontrast roundingfeasible. Active/UC exclude0;HC/PT includes0;omnibusgate met. MatchedSMDPT/UC CIincludes0 whereasMDCIexcludes0; this is an interval-scaling implication ofexistingSMDpattern.
- Existing candidate and cross-lane implications: ExistingC003/C010 preserve the SMDconstruction/containment. Coordinator alerted to maintain cross-columnCI implication; no duplicatefinding emitted.
- Unresolved definitions and limits: SMDinterval construction and jointMD/SMDcovariance unavailable; do not assume identicalconfidence construction.
- New finding: None; no previously screened finding re-emitted.

Completion: 55/55 assigned relationships explicitly PASS_2_COMPLETE. New findings0. The checker part separately records the seven consolidated apparent observations screened during this shard and the complete47-row original-exclusion revisit.



<!-- Active complete pass2 inventory: main_late -->

# Statistical relationship inventory — pass 2 main-late shard

Fresh runtime agent: `/root/stat2_main_late`; model gpt-6.1-sol, reasoning effort high. Assigned exactly55 relationships S056–S110; each is completed below. This part preserves the complete pass1 source tuples and records independent pass2 checks. No shared canonical artifact was edited.

Direct-source authority: visually reread current pinned PyMuPDF1.26.4 CPU renders of REPORT main physical PDF pp.4,10,11, plus REPORT results pp.17,18 for cross-lane PGIC context. Source links: [main methods](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), [Table3](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), [Table3 continuation and definitions](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11). Current native source text independently reread for the narrative and footnotes; OCR/text serve as locators. Complete current ledger17 IDs, screening26 decisions, evidence-recheck17 cards and original47 excluded rows were read. No legacy scientific record, web source or new Python helper was used.

Common checks: source uses adjusted linear GEE, randomized-population predictions, 95%CIs, two-sided alpha.05, Wald three-group omnibus test and least-significant-difference gate P<.05. The source does not supply row-specific SEs, test statistics or covariance/reference degrees of freedom. A jointP is never treated as a same-contrast pairwiseP. Point containment is compared with numerical interval endpoints; category1 is never removed for precision. Common positive UC-change SD imposes point-contrast scaling and additivity; C003 records its repeated failures. C010 records all14 containment tuples. No noninferiority/equivalence margin, interim or stopping decision applies to these rows. Same-direction model-based group means are not compared with crude sample summaries.

Cross-lane method implications: C005 concerns age prespecification, C006 concerns secondary baseline adjustment, C007 retains the disclosed MNAR/IPW amendment and competing primary-analysis labels. C011–C015 concern distinct supplementary primary models/counts/coefficient tests, not new copies of these adjusted secondary rows. C004/C008/C009 concern binary NNT construction/null coverage/containment and do not instantiate in these continuous rows. C016 is S_W for supplementary raw-summary identity, with main PGIC scale context only corroborating. C002/C017 are distinct adherence/workbook arithmetic. No already-screened observation is re-emitted.

### S056

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN091, Severity 12 mo — SMD construction and intervals.
- Printed tuples: -0.25(-0.24 to 0.01) / -0.36(-0.35 to-0.12) / -0.11(-0.11 to 0.12).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Containment does not reconcile for contrast1,2: F-ST1-002. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Both severity12 PT/UC and HC/UC points are below their printed lower endpoints; retain C010. The zero HC/PT MD with nonzero SMD fails the common positive-SD construction; retain C003.
- Named pass2 limitations: Actual UC change SDs, unrounded standardized contrasts, intended contrast/time mapping and exact SMD interval construction are absent. These limit reconstruction of replacement values; they do not remove C003/C010 source comparisons.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S057

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN092, Intensity 3 mo — group adjusted estimates.
- Printed tuples: -0.9(-1.0 to-0.8) / -0.9(-1.0 to-0.8) / -0.6(-0.7 to-0.5).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Intensity3: all three adjusted group points lie within ordered CIs and have improvement direction. Counts643/690/703 identify contributors, total2036; they are not the randomized target2331.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S058

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN092, Intensity 3 mo — between-group estimates and omnibus test.
- Printed tuples: -0.3(-0.5 to-0.1) / -0.3(-0.5 to-0.2) / -0.0(-0.2 to 0.2).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Intensity3: all three MD points are contained; PT/UC and HC/UC CIs exclude0, HC/PT contains0. OmnibusP<.001 passes the stated gate; no pairwise P is supplied. Group-mean subtraction and MD additivity are feasible after one-decimal precision.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S059

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN092, Intensity 3 mo — SMD construction and intervals.
- Printed tuples: -0.21(-0.21 to-0.01) / -0.29(-0.30 to-0.11) / -0.08(-0.09 to 0.09).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Intensity3: all SMD points are contained with ascending bounds; common scaling cannot produce HC/PT−.08 from MD−0.0 given PT/UC−.3 and SMD−.21. Recomputed HC/PT[−.043,.043] versus[−.085,−.075], relativegap.400; retain C003.
- Named pass2 limitations: Actual UC change SDs, unrounded standardized contrasts, intended contrast/time mapping and exact SMD interval construction are absent. These limit reconstruction of replacement values; they do not remove C003/C010 source comparisons.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S060

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN093, Intensity 6 mo — group adjusted estimates.
- Printed tuples: -1.0(-1.1 to-0.9) / -1.1(-1.2 to-1.0) / -0.7(-0.9 to-0.6).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Intensity6: all three group points are contained with improvement direction; contributor counts643/690/703 total2036. Adjusted group estimates are not crude means.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S061

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN093, Intensity 6 mo — between-group estimates and omnibus test.
- Printed tuples: -0.2(-0.4 to-0.1) / -0.3(-0.5 to-0.2) / -0.1(-0.3 to 0.1).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Intensity6: all MD points are contained and ascending; active/UC CIs exclude0, HC/PT contains0. OmnibusP<.001 passes gate; mean subtraction and MD additivity remain feasible after ±.05 input/output bounds.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S062

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN093, Intensity 6 mo — SMD construction and intervals.
- Printed tuples: -0.17(-0.23 to-0.06) / -0.27(-0.32 to-0.17) / -0.04(-0.10 to 0.05).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Intensity6: all SMD points are contained. Additivity predicts HC/UC[−.220,−.200] versus printed[−.275,−.265]; gap.045/.27=.166667. Retain C003; no unreported SE or covariance is reconstructed.
- Named pass2 limitations: Actual UC change SDs, unrounded standardized contrasts, intended contrast/time mapping and exact SMD interval construction are absent. These limit reconstruction of replacement values; they do not remove C003/C010 source comparisons.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S063

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN094, Intensity 12 mo — group adjusted estimates.
- Printed tuples: -1.1(-1.3 to-1.0) / -1.1(-1.3 to-1.0) / -0.9(-1.0 to-0.8).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Intensity12: all group points are contained with ordered CIs and lower-is-better direction. Counts643/690/703 total2036; follow-up contribution and randomized estimand are distinct.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S064

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN094, Intensity 12 mo — between-group estimates and omnibus test.
- Printed tuples: -0.2(-0.4 to-0.1) / -0.2(-0.4 to-0.1) / 0.0(-0.2 to 0.2).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=.01 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Intensity12: all MD points are contained; both active/UC intervals exclude0 and HC/PT includes0. OmnibusP=.01 passes gate. MD−.2/−.2/0.0 and adjusted group means reconcile within precision.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S065

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN094, Intensity 12 mo — SMD construction and intervals.
- Printed tuples: -0.16(-0.16 to 0.00) / -0.27(-0.26 to-0.12) / -0.03(-0.03 to 0.11).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Containment does not reconcile for contrast2: F-ST1-002. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Intensity12: HC/UC SMD−.27 is below lower limit−.26, retain C010. Additivity predicts HC/UC[−.200,−.180] versus[−.275,−.265]; relativegap.240741, retain C003.
- Named pass2 limitations: Actual UC change SDs, unrounded standardized contrasts, intended contrast/time mapping and exact SMD interval construction are absent. These limit reconstruction of replacement values; they do not remove C003/C010 source comparisons.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S066

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN095, Interference 3 mo — group adjusted estimates.
- Printed tuples: -1.3(-1.4 to-1.1) / -1.4(-1.5 to-1.2) / -0.8(-1.0 to-0.7).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Interference3: three group points are contained with ordered CIs and lower-is-better direction. Contributor counts643/690/703 total2036.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S067

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN095, Interference 3 mo — between-group estimates and omnibus test.
- Printed tuples: -0.5(-0.7 to-0.3) / -0.5(-0.7 to-0.3) / -0.1(-0.3 to 0.2).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Interference3: all MD points are contained; active/UC intervals exclude0, HC/PT contains0. OmnibusP<.001 passes gate. Group mean differences and additive MD triples are feasible under displayed precision.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S068

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN095, Interference 3 mo — SMD construction and intervals.
- Printed tuples: -0.25(-0.28 to-0.03) / -0.34(-0.37 to-0.13) / -0.13(-0.15 to 0.07).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Interference3: all SMD points are contained. Additivity predicts HC/UC[−.390,−.370] versus[−.345,−.335]; gap.025/.34=.073529. Retain C003.
- Named pass2 limitations: Actual UC change SDs, unrounded standardized contrasts, intended contrast/time mapping and exact SMD interval construction are absent. These limit reconstruction of replacement values; they do not remove C003/C010 source comparisons.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S069

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN096, Interference 6 mo — group adjusted estimates.
- Printed tuples: -1.5(-1.6 to-1.3) / -1.6(-1.8 to-1.4) / -1.0(-1.1 to-0.8).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Interference6: all adjusted group points are contained and improvement direction agrees with scale. Counts643/690/703 total2036; estimates are adjusted predictions.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S070

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN096, Interference 6 mo — between-group estimates and omnibus test.
- Printed tuples: -0.5(-0.7 to-0.3) / -0.6(-0.8 to-0.4) / -0.1(-0.4 to 0.1).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Interference6: all MD points are contained; active/UC intervals exclude0, HC/PT contains0. OmnibusP<.001 passes gate. Group-mean subtraction and MD−.5/−.6/−.1 additivity reconcile within precision.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S071

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN096, Interference 6 mo — SMD construction and intervals.
- Printed tuples: -0.27(-0.34 to-0.08) / -0.37(-0.44 to-0.19) / -0.14(-0.21 to 0.04).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Interference6: all SMD points are contained. Additivity predicts HC/UC[−.420,−.400] versus[−.375,−.365]; gap.025/.37=.067568. Retain C003.
- Named pass2 limitations: Actual UC change SDs, unrounded standardized contrasts, intended contrast/time mapping and exact SMD interval construction are absent. These limit reconstruction of replacement values; they do not remove C003/C010 source comparisons.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S072

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN097, Interference 12 mo — group adjusted estimates.
- Printed tuples: -1.6(-1.8 to-1.5) / -1.6(-1.8 to-1.5) / -1.2(-1.3 to-1.0).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Interference12: all three adjusted points are contained in ascending CIs and lower-is-better direction is coherent. Counts643/690/703 total2036.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S073

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN097, Interference 12 mo — between-group estimates and omnibus test.
- Printed tuples: -0.5(-0.7 to-0.3) / -0.5(-0.7 to-0.3) / 0.0(-0.2 to 0.2).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Interference12: MD−.5/−.5/0.0 points are contained; active/UC intervals exclude0, HC/PT contains0. OmnibusP<.001 passes gate; group means and MDs reconcile within precision.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S074

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN097, Interference 12 mo — SMD construction and intervals.
- Printed tuples: -0.26(-0.25 to 0.01) / -0.37(-0.36 to-0.11) / -0.12(-0.12 to 0.12).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Containment does not reconcile for contrast1,2: F-ST1-002. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Interference12: PT/UC−.26 is below−.25 and HC/UC−.37 below−.36; retain C010. Common scaling of HC/PT0.0 predicts[−.029444,.029444] versus SMD[−.125,−.115], relativegap.712963; retain C003.
- Named pass2 limitations: Actual UC change SDs, unrounded standardized contrasts, intended contrast/time mapping and exact SMD interval construction are absent. These limit reconstruction of replacement values; they do not remove C003/C010 source comparisons.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S075

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN098, Social 3 mo — group adjusted estimates.
- Printed tuples: 1.5(1.0 to 2.1) / 2.2(1.7 to 2.7) / 0.7(0.3 to 1.2).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Social3: all group points are contained with ordered CIs and higher-is-better direction. Counts636/683/696 sum2015; this outcome-specific count differs from severity contributors without a contrary denominator statement.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S076

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN098, Social 3 mo — between-group estimates and omnibus test.
- Printed tuples: 0.8(0.0 to 1.5) / 1.5(0.8 to 2.2) / 0.7(-0.0 to 1.4).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Social3: all MD points are contained. PT/UC lower endpoint0.0 and HC/PT−0.0 are null-adjacent; HC/UC CI excludes0. OmnibusP<.001 is a joint test and passes gate. No pairwise P is supplied; MD and group means reconcile within precision.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S077

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN098, Social 3 mo — SMD construction and intervals.
- Printed tuples: 0.12(0.23 to 0.11) / 0.01(0.12 to-0.00) / 0.20(0.29 to 0.19).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Printed endpoints descend for contrasts1,2,3: F-ST1-003. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Social3: each SMD is within the interval's numerical min/max despite descending printed bounds. Order-only observation is already screened F-ST1-003; no re-emission. HC/UC additivity predicts[.310,.330] versus[.005,.015], relativegap29.5; retain C003.
- Named pass2 limitations: Actual UC change SDs, unrounded standardized contrasts, intended contrast/time mapping and exact SMD interval construction are absent. These limit reconstruction of replacement values; they do not remove C003/C010 source comparisons.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S078

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN099, Social 6 mo — group adjusted estimates.
- Printed tuples: 2.2(1.6 to 2.8) / 2.5(2.0 to 3.1) / 1.0(0.5 to 1.5).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Social6: group points are contained in ascending CIs, higher-is-better. Counts636/683/696 sum2015; adjusted means are not raw medians.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S079

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN099, Social 6 mo — between-group estimates and omnibus test.
- Printed tuples: 1.2(0.4 to 1.9) / 1.5(0.8 to 2.2) / 0.3(-0.4 to 1.1).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Social6: all MD points are contained; active/UC CIs exclude0 and HC/PT includes0. OmnibusP<.001 passes gate. Pairwise mean subtraction and additivity are feasible under ±.05 precision.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S080

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN099, Social 6 mo — SMD construction and intervals.
- Printed tuples: 0.18(0.23 to 0.05) / 0.06(0.11 to-0.06) / 0.26(0.30 to 0.15).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Printed endpoints descend for contrasts1,2,3: F-ST1-003. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Social6: all SMD points are contained after sorting bounds. Descending order is the already-screened order-only pattern. Additivity predicts HC/UC[.430,.450] versus[.055,.065], relativegap6.083333; retain C003.
- Named pass2 limitations: Actual UC change SDs, unrounded standardized contrasts, intended contrast/time mapping and exact SMD interval construction are absent. These limit reconstruction of replacement values; they do not remove C003/C010 source comparisons.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S081

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN100, Social 12 mo — group adjusted estimates.
- Printed tuples: 2.6(2.0 to 3.2) / 2.7(2.2 to 3.3) / 1.4(0.8 to 1.9).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Social12: all group points lie in ascending CIs and higher-is-better direction is coherent. Counts636/683/696 sum2015.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S082

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN100, Social 12 mo — between-group estimates and omnibus test.
- Printed tuples: 1.3(0.5 to 2.1) / 1.4(0.6 to 2.1) / 0.1(-0.7 to 0.9).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Social12: all MD points lie inside ascending CIs; active/UC exclude0, HC/PT includes0. OmnibusP=.001 passes gate. Group means and contrast additivity reconcile within precision.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S083

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN100, Social 12 mo — SMD construction and intervals.
- Printed tuples: 0.19(0.21 to 0.01) / 0.07(0.09 to-0.10) / 0.27(0.28 to 0.12).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Printed endpoints descend for contrasts1,2,3: F-ST1-003. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Social12: all SMD points are contained in numerically sorted intervals; descending bounds are previously screened. Additivity predicts HC/UC[.450,.470] versus[.065,.075], relativegap5.357143; retain C003.
- Named pass2 limitations: Actual UC change SDs, unrounded standardized contrasts, intended contrast/time mapping and exact SMD interval construction are absent. These limit reconstruction of replacement values; they do not remove C003/C010 source comparisons.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S084

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN101, Physical 3 mo — group adjusted estimates.
- Printed tuples: 1.4(1.1 to 1.8) / 1.7(1.4 to 2.1) / 1.0(0.7 to 1.4).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Physical3: all group points lie inside ascending CIs and larger changes indicate better functioning. Counts639/684/699 sum2022.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S085

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN101, Physical 3 mo — between-group estimates and omnibus test.
- Printed tuples: 0.4(-0.1 to 0.9) / 0.7(0.2 to 1.2) / 0.3(-0.2 to 0.8).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=.02 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Physical3: all MD points are contained; PT/UC and HC/PT include0, HC/UC excludes0. Joint omnibusP=.02 passes gate; no equivalence conclusion follows from nonsignificant individual comparisons. Group differences reconcile within precision.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S086

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN101, Physical 3 mo — SMD construction and intervals.
- Printed tuples: 0.09(0.16 to 0.07) / -0.02(0.05 to-0.04) / 0.16(0.22 to 0.15).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Printed endpoints descend for contrasts1,2,3: F-ST1-003. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Physical3: all SMD points are contained after sorting endpoints; order-only pattern already screened. HC/UC MD.7 and SMD−.02 have opposite signs under a positive SD; additivity predicts[.240,.260] versus[−.025,−.015], relativegap12.75. Retain C003.
- Named pass2 limitations: Actual UC change SDs, unrounded standardized contrasts, intended contrast/time mapping and exact SMD interval construction are absent. These limit reconstruction of replacement values; they do not remove C003/C010 source comparisons.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S087

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN102, Physical 6 mo — group adjusted estimates.
- Printed tuples: 2.0(1.6 to 2.4) / 1.8(1.4 to 2.1) / 1.4(1.0 to 1.7).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Physical6: group points are contained in ascending CIs and higher-is-better direction is coherent. Counts639/684/699 sum2022.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S088

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN102, Physical 6 mo — between-group estimates and omnibus test.
- Printed tuples: 0.6(0.1 to 1.2) / 0.4(-0.1 to 0.9) / -0.3(-0.8 to 0.3).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=.05 is a3-group Wald test, not a pairwiseP. Printed.05 gate has unresolved rounding, recorded once as excluded display precision. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Physical6: all MD points are contained; PT/UC CI[.1,1.2] excludes0 while other two include0. JointP=.05 is not the PT/UC pairwise test. Its rounding interval[.045,.055] spans the source's strict<.05 gate, so the gate implementation is not reproduced as a new conflict. MD−.3 HC/PT versus group difference−.2 is feasible under half-unit precision.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S089

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN102, Physical 6 mo — SMD construction and intervals.
- Printed tuples: 0.15(0.09 to-0.06) / 0.02(-0.03 to-0.18) / 0.22(0.16 to 0.05).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Containment does not reconcile for contrast1,2,3: F-ST1-002. Printed endpoints descend for contrasts1,2,3: F-ST1-003. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Physical6: all three SMD points exceed the numerical maximum of their intervals; retain C010 even after sorting descending endpoints. HC/PT MD−.3 versus SMD.22 reverses sign; additivity predicts HC/UC[.360,.380] versus[.015,.025], relativegap16.75. Retain C003.
- Named pass2 limitations: Actual UC change SDs, unrounded standardized contrasts, intended contrast/time mapping and exact SMD interval construction are absent. These limit reconstruction of replacement values; they do not remove C003/C010 source comparisons.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S090

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN103, Physical 12 mo — group adjusted estimates.
- Printed tuples: 2.2(1.8 to 2.7) / 2.1(1.7 to 2.5) / 1.3(0.9 to 1.7).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Physical12: all three group points lie within ascending CIs and improvement direction is coherent. Counts639/684/699 sum2022.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S091

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN103, Physical 12 mo — between-group estimates and omnibus test.
- Printed tuples: 0.9(0.3 to 1.5) / 0.8(0.2 to 1.4) / -0.1(-0.7 to 0.5).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=.004 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Physical12: all MD points are contained; both active/UC CIs exclude0, HC/PT includes0. OmnibusP=.004 passes gate. MD.9/.8/−.1 agrees with adjusted group means after precision.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S092

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN103, Physical 12 mo — SMD construction and intervals.
- Printed tuples: 0.20(0.18 to-0.03) / 0.07(0.04 to-0.16) / 0.27(0.25 to 0.09).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Containment does not reconcile for contrast1,2,3: F-ST1-002. Printed endpoints descend for contrasts1,2,3: F-ST1-003. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: Physical12: all SMD points exceed sorted interval maxima; retain C010. HC/PT MD−.1 versus SMD.27 reverses sign; common-SD additivity predicts HC/UC[.460,.480] versus[.065,.075], relativegap5.5. Retain C003.
- Named pass2 limitations: Actual UC change SDs, unrounded standardized contrasts, intended contrast/time mapping and exact SMD interval construction are absent. These limit reconstruction of replacement values; they do not remove C003/C010 source comparisons.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S093

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN104, PGIC pain 3 mo — group adjusted estimates.
- Printed tuples: 2.2(2.1 to 2.3) / 2.0(1.9 to 2.1) / 2.9(2.8 to 3.0).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: PGIC-pain3: three adjusted group points are contained with ascending bounds; 1–7 one-item scale defines lower as better. Counts637/687/702 sum2026. These adjusted values are not the unadjusted raw summaries in eTable11/C016.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S094

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN104, PGIC pain 3 mo — between-group estimates and omnibus test.
- Printed tuples: -0.7(-0.8 to-0.6) / -0.9(-1.0 to-0.8) / -0.2(-0.3 to-0.1).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: PGIC-pain3: all MD points are contained and all three intervals exclude0 with improvement direction. OmnibusP<.001 passes gate. MD−.7/−.9/−.2 and group means reconcile.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S095

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN104, PGIC pain 3 mo — SMD construction and intervals.
- Printed tuples: -0.62(-0.81 to-0.19) / -0.62(-0.76 to-0.25) / -0.37(-0.51 to-0.05).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: PGIC-pain3: all SMD points are contained and bounds ascend. Common-SD additivity predicts HC/UC[−1.000,−.980] versus[−.625,−.615], relativegap.572581. Retain C003.
- Named pass2 limitations: Actual UC change SDs, unrounded standardized contrasts, intended contrast/time mapping and exact SMD interval construction are absent. These limit reconstruction of replacement values; they do not remove C003/C010 source comparisons.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S096

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN105, PGIC pain 6 mo — group adjusted estimates.
- Printed tuples: 2.2(2.1 to 2.3) / 2.1(2.0 to 2.2) / 2.8(2.7 to 2.9).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: PGIC-pain6: all group points are contained in ascending CIs; lower-is-better direction agrees with source scale. Counts637/687/702 sum2026. Raw-score median/mean uncertainty C016 does not change this adjusted-model quantity.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S097

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN105, PGIC pain 6 mo — between-group estimates and omnibus test.
- Printed tuples: -0.6(-0.8 to-0.5) / -0.7(-0.8 to-0.5) / -0.1(-0.2 to 0.1).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: PGIC-pain6: all MD points are contained; active/UC intervals exclude0, HC/PT contains0. OmnibusP<.001 passes gate. Group differences and MD−.6/−.7/−.1 reconcile within precision.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S098

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN105, PGIC pain 6 mo — SMD construction and intervals.
- Printed tuples: -0.54(-0.59 to-0.05) / -0.55(-0.60 to-0.16) / -0.29(-0.33 to 0.06).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: PGIC-pain6: all SMD points lie within ordered CIs. Additivity predicts HC/UC[−.840,−.820] versus[−.555,−.545], relativegap.481818. Retain C003.
- Named pass2 limitations: Actual UC change SDs, unrounded standardized contrasts, intended contrast/time mapping and exact SMD interval construction are absent. These limit reconstruction of replacement values; they do not remove C003/C010 source comparisons.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S099

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN106, PGIC pain 12 mo — group adjusted estimates.
- Printed tuples: 2.2(2.1 to 2.3) / 2.2(2.1 to 2.4) / 2.8(2.7 to 2.9).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: PGIC-pain12: all group points are contained with ascending CIs; lower-is-better. Counts637/687/702 sum2026; target population and outcome-contributor counts remain distinct.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S100

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN106, PGIC pain 12 mo — between-group estimates and omnibus test.
- Printed tuples: -0.6(-0.8 to-0.5) / -0.6(-0.7 to-0.4) / 0.1(-0.1 to 0.2).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: PGIC-pain12: all MD points are contained; active/UC intervals exclude0, HC/PT includes0. OmnibusP<.001 passes gate. HC/PT.1 with equal rounded2.2 arm centers is feasible because difference-input bounds span[−.1,.1] and printed point bounds[.05,.15] overlap.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S101

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN106, PGIC pain 12 mo — SMD construction and intervals.
- Printed tuples: -0.55(-0.50 to 0.05) / -0.57(-0.54 to-0.08) / -0.29(-0.25 to 0.14).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Containment does not reconcile for contrast1,2,3: F-ST1-002. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: PGIC-pain12: all three SMD points are below their lower endpoints; retain C010. Additivity predicts HC/UC[−.850,−.830] versus[−.575,−.565], relativegap.447368. HC/PT MD.1 versus SMD−.29 also reverses sign; retain C003.
- Named pass2 limitations: Actual UC change SDs, unrounded standardized contrasts, intended contrast/time mapping and exact SMD interval construction are absent. These limit reconstruction of replacement values; they do not remove C003/C010 source comparisons.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S102

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN107, PGIC general 3 mo — group adjusted estimates.
- Printed tuples: 2.0(1.9 to 2.1) / 1.6(1.5 to 1.7) / 2.7(2.6 to 2.8).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: PGIC-general3: all group points are contained in ascending CIs; lower indicates better overall status. Counts640/687/702 sum2029. Adjusted predictions and eTable11 raw summaries are distinct analyses.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S103

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN107, PGIC general 3 mo — between-group estimates and omnibus test.
- Printed tuples: -0.7(-0.8 to-0.6) / -1.1(-1.2 to-1.0) / -0.4(-0.5 to-0.3).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: PGIC-general3: all MD points are contained and all three CIs exclude0 with improvement direction. OmnibusP<.001 passes gate; MD−.7/−1.1/−.4 reconciles with group predictions.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S104

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN107, PGIC general 3 mo — SMD construction and intervals.
- Printed tuples: -0.66(-1.04 to-0.38) / -0.66(-0.98 to-0.42) / -0.40(-0.67 to-0.18).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: PGIC-general3: all SMD points are contained with ascending endpoints. Additivity predicts HC/UC[−1.070,−1.050] versus[−.665,−.655], relativegap.583333. Retain C003.
- Named pass2 limitations: Actual UC change SDs, unrounded standardized contrasts, intended contrast/time mapping and exact SMD interval construction are absent. These limit reconstruction of replacement values; they do not remove C003/C010 source comparisons.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S105

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN108, PGIC general 6 mo — group adjusted estimates.
- Printed tuples: 2.1(2.0 to 2.2) / 1.8(1.7 to 1.9) / 2.5(2.5 to 2.6).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: PGIC-general6: all group points are contained; UC point2.5 coincides with lower endpoint2.5, which satisfies containment. Lower-is-better direction is coherent. Counts640/687/702 sum2029.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S106

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN108, PGIC general 6 mo — between-group estimates and omnibus test.
- Printed tuples: -0.5(-0.6 to-0.3) / -0.7(-0.9 to-0.6) / -0.2(-0.4 to-0.1).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: PGIC-general6: all MD points are contained and all three CIs exclude0. OmnibusP<.001 passes gate. Rounded group difference PT/UC−.4 versus MD−.5 and HC/PT−.3 versus MD−.2 both have overlapping recomputed/printed bounds; no numeric finding.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S107

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN108, PGIC general 6 mo — SMD construction and intervals.
- Printed tuples: -0.46(-0.69 to-0.24) / -0.50(-0.70 to-0.32) / -0.24(-0.41 to-0.07).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: PGIC-general6: all SMD points are contained with ascending CIs. Additivity predicts HC/UC[−.710,−.690] versus[−.505,−.495], relativegap.370000. Retain C003.
- Named pass2 limitations: Actual UC change SDs, unrounded standardized contrasts, intended contrast/time mapping and exact SMD interval construction are absent. These limit reconstruction of replacement values; they do not remove C003/C010 source comparisons.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S108

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN109, PGIC general 12 mo — group adjusted estimates.
- Printed tuples: 2.0(1.9 to 2.1) / 1.9(1.8 to 2.0) / 2.6(2.5 to 2.7).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: PGIC-general12: all group points are contained with ascending bounds; lower-is-better. Counts640/687/702 sum2029. C016 addresses the separately labeled unadjusted raw summaries.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S109

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN109, PGIC general 12 mo — between-group estimates and omnibus test.
- Printed tuples: -0.6(-0.7 to-0.4) / -0.7(-0.8 to-0.5) / -0.1(-0.3 to 0.0).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: PGIC-general12: all MD points are contained; active/UC intervals exclude0 and HC/PT ends at0.0. OmnibusP<.001 is not a pairwise HC/PT P. Group differences and MD−.6/−.7/−.1 reconcile.
- Named pass2 limitations: Unrounded fitted values, row-specific covariance, SE/test statistics and test reference degrees of freedom are absent. Outcome-specific covariate vectors and PGIC baseline handling remain the named C006 method question; contributor count versus randomized estimand does not establish an extra numerical conflict.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

### S110

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.11, MAIN109, PGIC general 12 mo — SMD construction and intervals.
- Printed tuples: -0.53(-0.64 to-0.11) / -0.58(-0.67 to-0.22) / -0.28(-0.36 to 0.03).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PASS_2_COMPLETE
- Independent pass2 source facts and rule result: PGIC-general12: all SMD points are contained with ascending endpoints. Additivity predicts HC/UC[−.820,−.800] versus[−.585,−.575], relativegap.370690. Retain C003.
- Named pass2 limitations: Actual UC change SDs, unrounded standardized contrasts, intended contrast/time mapping and exact SMD interval construction are absent. These limit reconstruction of replacement values; they do not remove C003/C010 source comparisons.
- New finding: None; any reproduced issue above is already mapped to the named stable candidate.

## Completion

PASS_2_COMPLETE:55/55 assigned S IDs. New findings:0. No uncovered assigned source row. The named statistical inputs are not supplied; no exact omnibus or interval recomputation is asserted from convention. Calculation alignment for existing recheck prose: severity6 reference SMD−.26/−.36/−.12 has gap.005/.12=.041667 when predicting HC/PT, rather than a zero additive gap; this remains precision-compatible and creates no source candidate.



<!-- Active complete pass2 inventory: reports_early -->

# Statistical relationship inventory — pass 2, REPORT early shard

Fresh runtime: `/root/stat2_reports_early`; gpt-6.1-sol/high; FRESH_SPAWN. Exact assigned set: S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220. This part updates those existing stable records without replacing their pass-1 provenance. All source locations below are physical PDF pages. REPORT supplement is DOC-005; PLAN protocol/SAP are DOC-002/DOC-003. Main DOC-001 is REPORT. Source links use this part's four-level relative depth.

Complete inputs read: QUALITY_CONTROL_SCOPE.md, the 1.6.2 contract, performance profile, report specification/settings, assigned pass-1 packet, entire current 17-ID candidate ledger, all 26 initial screening decisions, all 17 mechanical recheck cards and all 47 original checker exclusion rows. No prior-run conclusions or web evidence used. Current source images were visually read; source/OCR authority and engine details are in the checker part.

## S201 — Outcome definitions, thresholds and directions

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.2, Outcome Measures](../../../joi250046supp4_prod_1755300121.15587.pdf#page=2).
- **Pass-2 check:** Severity is the mean of 11 BPI items, intensity of four, interference of seven, all 0–10 and higher worse. MCID is at least 30% decrease from baseline, so favorable response is an increase in the responder probability and RR above 1 for active versus UC. PHQ-8 sum 0–24 and GAD-7 sum 0–21 agree with eight/seven items each 0–3. PROMIS sleep is higher worse, social/physical higher better, with reference T mean 50/SD10 and the stated 60/40 thresholds. Item totals, scale ranges and directions reconcile with the assigned response rows; no superiority margin, noninferiority or equivalence rule is supplied for this relationship.
- **Named definition limits:** Raw PROMIS conversion tables and item-level scoring are absent; no reconstruction is needed for a printed conflict. Main scoring wording is considered in the prior-exclusion audit, without inventing an alternative score.
- **Finding/cross-lane implication:** No new finding.

## S202 — Primary response completeness and missingness decision

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.4, Missing Data](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [p.7, eTable1](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); PLAN [DOC-003 p.19, section11](../../../joi250046supp2_prod_1755300121.15087.pdf#page=19).
- **Pass-2 check:** Randomized 2331=777+776+778. Observed 3-month 1798=621+542+635, 77.1%; missing 22.9% exceeds the stated 15% branch. Arm 79.9%,69.8%,81.6% completeness also establishes differential missingness. Any follow-up 2036=703+643+690 and none 295=74+133+88; 2036+295=2331. The pattern counts sum 2039 rather than 2036; implied visits 5458 rather than 5449. Half-unit gaps 1/2036=.000491 and 4.5/5449=.000826 are at most .05. This is one display-precision observation, not an always-register category3 reproduction above the threshold.
- **Named definition limits:** Exact corrected pattern classification cannot be identified from supplied aggregate counts. That limit does not change whether the missingness branch is triggered.
- **Finding/cross-lane implication:** No new finding; C007 already records the primary/sensitivity role comparison, including the disclosed amendment and conditional branch.

## S203 — Additional predictor selection and analysis attribution

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.4, Adjustment](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [p.5, Non-Response Weighting](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5), [p.7, eTable2](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7), [p.8](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8), [p.9](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9), [p.10](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10); PLAN [DOC-002 p.56](../../../joi250046supp1_prod_1755300121.14087.pdf#page=56), [DOC-003 p.20](../../../joi250046supp2_prod_1755300121.15087.pdf#page=20).
- **Pass-2 check:** The dual P<.10 selection rule uses adjusted 3-month MCID and 3-month missingness models for imputation/estimation, and MCID plus any-follow-up models for weights. These are distinct tests and response definitions, so one selection P is not a fitted-model coefficient P. Age's prespecified-base attribution, binary education versus three coefficients, and education versus employment in the weight set are already C005, C013 and C012. Their recheck facts remain source-supported and are not re-emitted.
- **Named definition limits:** Final covariate design matrices, selection-versus-final-fit coding and prospective age specification are absent. No preferred selection method is proposed.
- **Finding/cross-lane implication:** C005, C012, C013; no new finding.

## S204 — Pattern-mixture imputation design and response construction

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.4, equation](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [p.5, imputation continuation](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5).
- **Pass-2 check:** The conditional change model contains arm, time6/time12, arm×time, observed-pattern1/pattern2 and arm×pattern terms; reference cells are UC,3months,pattern3. It is fitted among participants with at least one observation using linear GEE, independence and robust person/coach clustering; predictions replace missing changes and MCID uses those changes plus baseline severity. These stated steps identify the linear-change versus binary-response analyses. The formula includes the listed term families shown in eTable3. The duplicated UC name in the arm definition is identifiable from the equation's PT/HC indicators and three-arm context; it does not alter a printed coefficient.
- **Named definition limits:** Exact change sign, individual predictions, truncation and joint covariance are not numerically supplied. The positive conditional PT/HC coefficients alone do not establish a direction reversal of marginal treatment response.
- **Finding/cross-lane implication:** Existing C013 coding question retained; no additional method conflict or new finding.

## S205 — Imputation population, observed visits and missing values

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.7, eTable1](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7), [p.8, eTable3 header](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8).
- **Pass-2 check:** 2331−295=2036 any-follow-up persons; 2036×3=6108 full imputed visits; observed visits 1798+1790+1861=5449; 6108−5449=659 missing values. All reproduce exactly. The estimated target population of all randomized is distinguished from contributing imputation persons and visits; it is not an assertion that all2331 supplied observations.
- **Named definition limits:** Individual pattern assignment is absent; S202's small aggregate discrepancy remains below the precision threshold.
- **Finding/cross-lane implication:** No new finding.

## S206 — Primary estimation functional form, variance and clustering

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.5, second-step equation/method](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5), [p.9, eTable4](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); REPORT [DOC-001 p.4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); PLAN [DOC-003 p.20](../../../joi250046supp2_prod_1755300121.15087.pdf#page=20).
- **Pass-2 check:** Log mean of binary MCID, Poisson GEE, arm/time/arm×time and robust provider/person sandwich are explicitly stated. Joint imputation/analysis variance is described by a supplied citation without numeric matrix. The form generates the treatment/time contrast families in eTable4. Main explicitly says tests are two-sided at .05; this is read, not inferred. Repeated observations/person and provider clustering are addressed in the printed description; no independent-samples method is asserted. Generic Poisson use for binary outcomes is internally coherent with the stated robust variance.
- **Named definition limits:** Numeric covariance, exact coefficient-test reference distribution, degrees of freedom and CI construction are not supplied. Exact coefficient P reconstruction therefore cannot be asserted from a normal approximation.
- **Finding/cross-lane implication:** C005/C007/C013/C014 remain the relevant recorded specification/test comparisons; no new finding.

## S207 — Nonresponse weighting and baseline missing covariates

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.5](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5), [p.6](../../../joi250046supp4_prod_1755300121.15587.pdf#page=6), [p.10, eTables5–6](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10); PLAN [DOC-003 p.4 amendment](../../../joi250046supp2_prod_1755300121.15087.pdf#page=4), [p.19](../../../joi250046supp2_prod_1755300121.15087.pdf#page=19).
- **Pass-2 check:** Logistic response is at least one follow-up in all randomized; raw weights1/p are scaled then applied to second-step estimation. Imputation handles intermittent missingness among2036 contributors; nonresponse weights represent those with none. Baseline means are imputed from available baseline data, which is distinct from outcome pattern-mixture imputation. Weight sum2036 persons and6108 visits identifies the contributor normalization in context; all-randomized estimand2331 is a distinct quantity. The July2024 SAP amendment expressly supplies IPW support; no absence of disclosure is claimed.
- **Named definition limits:** Individual probabilities and applied weight-model vector are absent; C012 addresses explicit predictor membership. C007 retains the final hierarchy question rather than asserting the amendment is absent.
- **Finding/cross-lane implication:** C007/C012; no new finding.

## S208 — Complete linear imputation coefficient/interval/P family

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.8, every eTable3 coefficient row](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8); REPORT [DOC-001 p.4, two-sided .05](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4).
- **Pass-2 check:** All28 printed tuples have ordered endpoints and contained points. The seven direct95%CI-null/P conflicts are Pattern2 −.28(−.47,−.08),P.150; Pattern1 −.20(−.36,−.03),P.226; Pattern2×PT −.30(−.58,−.02),P.280; Pattern2×HC −.47(−.74,−.19),P.090; Site3 .19(.08,.29),P.069; Site4 .15(.05,.24),P.124; secondAA .16(.07,.25),P.077. Each remains C014/F-ST1-201; category1 has no rounding removal. Remaining rows have matching printed null/significance statuses. For Time6 .13(.07,.19),P.025, a normal-Wald diagnostic SE=.12/3.92=.030612,z4.2467 yields about.000022; this is not an exact reported test reproduction because its distribution/CI construction are absent. It does not become a further finding by assuming normal tests.
- **Named definition limits:** Numeric SEs, reference distribution/df, exact CI/test construction and unrounded values absent. Education mapping belongs C013; conditional direction belongs S204.
- **Finding/cross-lane implication:** C013/C014; no new finding.

## S209 — Complete weighted primary RR/interval/P family

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.9, every eTable4 row](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9).
- **Pass-2 check:** All23 printed rows, including identical HC/PT3M repetition, have contained points and ordered endpoints. PT/UC1.28(1.06,1.55),P.010; HC/UC1.54(1.3,1.82),P<.001; HC/PT1.2(1.03,1.4),P.019 show favorable active responder directions. Ratio closure1.54/1.28=1.203125 is compatible with1.2;6M1.62/1.44=1.125 with1.13;12M1.41/1.32=1.06818 with1.07 under half-units. Age1.15(1,1.33),P.046 and secondAA1.16(1,1.33),P.046 are already C014/F-ST1-202; printed null endpoints are retained regardless of unrounded alternatives. Other tuples' null/P statuses agree. The duplicate3M row agrees exactly and is not an exclusion.
- **Named definition limits:** Joint covariance/CI-test construction and unrounded null-adjacent endpoints absent; repeated site labels carry intentional healthcare-site suppression context. No crude-ratio comparison is made.
- **Finding/cross-lane implication:** C013/C014; no new finding.

## S210 — Complete response-logistic OR/interval/P family

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.10, every eTable5 coefficient](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10).
- **Pass-2 check:** All16OR tuples have ordered endpoints and contained points. UC/PT2.05(1.50,2.79),P<.001 and HC/PT1.68(1.25,2.26),P<.001 agree with higher follow-up odds outside PT; these are response odds, not pain-response risks. Male.76(.57,1.00),P.053 has null/P agreement. PEG.96(.92,1.00),P.037 repeats C014/F-ST1-202 and remains under category1. All remaining printed null/P statuses agree. c-statistic.679 is not a regression coefficient or an interval-bearing treatment effect; no numeric uncertainty is supplied.
- **Named definition limits:** Numeric logistic test statistics, SEs, df, exact interval construction and final predictor vector absent. OR versus RR labels are coherent with the stated different outcomes/models.
- **Finding/cross-lane implication:** C012/C014; no new finding.

## S211 — Response-probability and analytic weight summaries

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.10, eTable6](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10).
- **Pass-2 check:** Response probabilities mean.88,SD.07,min.50,P25.85,P50.90,P75.93,max.98 are ordered and bounded. Weights sum2036,mean1.00,SD.09,min.89,P25.94,P50.97,P751.03,max1.75 are ordered, and2036×1=2036. Reversed quantile pair products .50×1.75=.875, .85×1.03=.8755,.90×.97=.873,.93×.94=.8742,.98×.89=.8722 support a common positive scaling factor under half-unit intervals. The transformations are reciprocals before scaling; mean(1/p) is not set equal to1/mean(p).
- **Named definition limits:** Individual weight normalization and probability sample membership beyond the analytic context are not supplied numerically. No significance test or stopping rule applies to these descriptive summaries.
- **Finding/cross-lane implication:** No new finding.

## S212 — Complete-case sensitivity method and multiplicity rule

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.11, eTable7 introduction/header/notesb–e](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11); PLAN [DOC-003 p.19, sections10–11](../../../joi250046supp2_prod_1755300121.15087.pdf#page=19).
- **Pass-2 check:** Complete case removes missing outcomes, no imputation or weighting;3M1798=621+542+635. Seven listed baseline factors produce modified-Poisson GEE adjusted percentages, RRs and reciprocal NNTs. The omnibus Wald P is a three-arm test; pairwise comparisons are interpreted only when omnibusP<.05. All three complete-case omnibusPs<.001 satisfy the rule. Omnibus significance does not imply that HC/PT is significant. The adjusted versus full-primary results are distinct analyses and should not be compared as copies.
- **Named definition limits:** Exact pairwise covariance/RD intervals, omnibus statistic and df are absent. C007 records sensitivity/primary hierarchy; the provided complete-case result is not absent from the package.
- **Finding/cross-lane implication:** C005/C007 background; no new finding.

## S213 — Worst/best-case sensitivity method and population

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.11, worst/best-case block and notes](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11); PLAN [DOC-003 p.19](../../../joi250046supp2_prod_1755300121.15087.pdf#page=19).
- **Pass-2 check:** Missing PT/HC outcomes set0 and missingUC set1, yielding all2331=777+776+778. This deliberately unfavorable active direction matches the plan's supplied second sensitivity approach. The same seven-factor adjustment and GEE method are explicit. All three omnibusPs<.001 pass the stated gate. NNT notes describe disconnected positive-to-infinity and negative-to-negative-infinity branches when RD crosses0; a positive then negative endpoint is not treated as a finite conventional interval.
- **Named definition limits:** Per-person assignments, RD covariance and exact pairwise CI method absent; no superiority conclusion for the primary analysis is inferred from this different sensitivity analysis.
- **Finding/cross-lane implication:** No new finding.

## S214 — eTable7 complete-case3-month tuple

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.11, complete-case3M row](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11).
- **Printed tuple:** PT32.2(28.5,36.3),HC35.5(32.0,39.3),UC24.0(20.9,27.6); RR PT/UC1.34(1.12,1.61),HC/UC1.48(1.24,1.75),HC/PT1.10(.94,1.29); omnibusP<.001; NNT13(8,33),9(7,15),31(13,−60).
- **Pass-2 check:** All group/RR points contained, endpoints ordered; RR points agree with corresponding adjusted proportions after half-unit arithmetic. NNT point intervals from100/(rate difference) are [12.048193,12.345679],[8.620690,8.771930],[29.411765,31.250000]. Printed13 has expanded[12.5,13.5],gap.154321/13=.011871; the other two overlap. HC/PT RR includes1 and NNT's two branches include infinity, matching the footnote's null interpretation. Omnibus gate passes without claiming every pair differs.
- **Named definition limits:** RD CI and covariance absent; marginal group CIs cannot reproduce NNT limits without them.
- **Finding/cross-lane implication:** No new finding; precision pattern in checker exclusions.

## S215 — eTable7 complete-case6-month tuple

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.11, complete-case6M row](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11).
- **Printed tuple:** PT40.1(36.3,44.3),HC41.1(37.4,45.1),UC26.6(23.4,30.3); RR1.51(1.28,1.77),1.54(1.32,1.81),1.02(.90,1.17); omnibusP<.001; NNT8(6,13),7(6,11),101(16,−22).
- **Pass-2 check:** Group/RR containment, endpoint order and favorable active directions hold. RR ratios agree under printed precision. Reciprocal NNT point intervals [7.352941,7.462687],[6.849315,6.944444],[90.909091,111.111111] give PT gap7.5−7.462687=.037313/8=.004664 and overlap for the other two. HC/PT RR-null and disconnected NNT-null interpretation agree; omnibus gate passes.
- **Named definition limits:** RD interval covariance/construction absent; no pairwise P is supplied and none is inferred from omnibusP.
- **Finding/cross-lane implication:** No new finding.

## S216 — eTable7 complete-case12-month tuple

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.11, complete-case12M row](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11).
- **Printed tuple:** PT41.0(37.3,45.1),HC41.5(37.9,45.4),UC30.5(27.2,34.3); RR1.34(1.16,1.56),1.36(1.17,1.57),1.01(.89,1.15); omnibusP<.001; NNT10(7,20),10(7,15),217(22,−28).
- **Pass-2 check:** Group/RR containment/order/direction and ratio reproduction hold. NNT point intervals [9.433962,9.615385],[9.009009,9.174312],[166.666667,250.000000] give second point gap9.5−9.174312=.325688/10=.032569; first/third overlap. Thus no above-.05 reciprocal discrepancy. HC/PT's RR and disconnected NNT agree in their null interpretation, and omnibus gate passes.
- **Named definition limits:** Same RD covariance/CI and exact pairwise tests absent as S214/S215.
- **Finding/cross-lane implication:** No new finding.

## S217 — eTable7 worst/best-case3-month tuple

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.11, worst/best-case3M row](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11).
- **Printed tuple:** PT22.7(20.0,25.8),HC29.3(26.3,32.6),UC39.4(36.1,43.0); RR.58(.49,.67),.74(.65,.85),1.29(1.09,1.52); omnibusP<.001; NNT−6(−9,−5),−10(−18,−7),16(10,40).
- **Pass-2 check:** Ordered/contained group andRR intervals; active-versusUC RRs below1 and negative NNTs agree with this unfavorable sensitivity assignment. HC/PT benefit direction agrees. Reciprocal NNT intervals [−6.024096,−5.952381],[−10.000000,−9.803922],[14.925373,15.384615] overlap first/second printed points; third gap15.5−15.384615=.115385/16=.007212. Gate passes. No NI/equivalence or stopping conclusion is made.
- **Named definition limits:** Exact RD covariance/CI construction absent; independent marginal CI subtraction is not used.
- **Finding/cross-lane implication:** No new finding.

## S218 — eTable7 worst/best-case6-month tuple

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.11, worst/best-case6M row](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11).
- **Printed tuple:** PT28.6(25.6,31.9),HC33.1(30.0,36.5),UC41.3(38.0,44.9); RR.69(.60,.79),.80(.70,.91),1.16(1.00,1.34); omnibusP<.001; NNT−8(−13,−6),−13(−26,−8),23(12,227).
- **Pass-2 check:** Group/RR containment/order, ratio points and directions hold. NNT point intervals [−7.936508,−7.812500],[−12.345679,−12.048193],[21.739130,22.727273] give middle gap.154321/13=.011871 and overlap otherwise. Gate passes. HC/PT printed RR includes1, while finite positive NNT23(12,227) reciprocally implies RD[1/227,1/12]=[.004405,.083333]. The proposed C008 source expansion was independently screened out as ROUNDING_OR_DISPLAY_PRECISION: the printed lower RR1.00 permits true lower endpoints above1 within [.995,1.005], and P<.001 is omnibus, not a pairwise interval/P conflict. The existing C008 affected locations are unchanged.
- **Named definition limits:** Parameter-specific RR/RD CI methods, unrounded lowerRR endpoint and joint covariance absent; distinct constructions can yield distinct null coverage.
- **Finding/cross-lane implication:** Proposed C008 source expansion excluded independently as ROUNDING_OR_DISPLAY_PRECISION; no new finding.

## S219 — eTable7 worst/best-case12-month tuple

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.11, worst/best-case12M row](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11).
- **Printed tuple:** PT31.3(28.2,34.6),HC34.4(31.2,37.8),UC43.0(39.6,46.7); RR.73(.64,.83),.80(.70,.91),1.10(.96,1.26); omnibusP<.001; NNT−9(−15,−7),−12(−21,−8),33(15,−194).
- **Pass-2 check:** Group/RR containment/order, ratio reproduction and unfavorable active-versusUC direction hold. Reciprocal point intervals [−8.620690,−8.474576],[−11.764706,−11.494253],[31.250000,33.333333] all overlap printed half-unit points. HC/PT RR straddles1 and NNT uses the footnote's infinity-reaching disconnected branches, so the null readings agree. Omnibus gate passes; no pairwise P is inferred.
- **Named definition limits:** RD covariance/CI construction and exact tests absent; this is not a primary-analysis result copy.
- **Finding/cross-lane implication:** No new finding.

## S220 — Protocol-change subset definitions, populations and adjustment

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.13, Protocol Change Subset Analyses](../../../joi250046supp4_prod_1755300121.15587.pdf#page=13), [p.14, eTable8 headers/notes](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14), [p.7, eTable1/eTable2](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7).
- **Pass-2 check:** Randomized pre/post454+1877=2331; any-follow-up366+1670=2036. Letters858 observed3M/1038=.82659 and935 any/1038=.90077 reproduce82.7%/90.1%. The enhancement boundary8/9/2021 is explicit; reminder-letter3/31/2022 analysis is explicitly post hoc. Seven-variable subset adjustment versus full selected education/employment primary adjustment remains C011, already screened. First header's PT149+HC153+UC152=454 at3months exceeds366 any-follow-up: minimum half-unit excess86/366=.234973. Pass1's proposed randomized-population interpretation is retained as an alternative, but cross-lane C015's RouteA3 observation is not removed as context or labeling. These dates describe retrospectively reported subsets, so these locations are REPORT.
- **Named definition limits:** First-header count convention and implemented subset covariate vectors absent. No missing weighting/imputation is inferred from the abbreviated footnote.
- **Finding/cross-lane implication:** C011/C015; no new finding. C004's reciprocal NNT occurrence is in the same table but assigned to later row relationships.

## Shard completion

20/20 assigned relationships explicitly PASS_2_COMPLETE. New finding headings:0. All count, denominator, estimate/test, method, multiplicity and cross-source implications relevant to these relationships were revisited. Existing C005,C007,C011,C012,C013,C014,C015 are cross-referenced rather than re-emitted; S218 was independently screened as a precision-compatible source expansion, excluded from C008. No scientific source-reading gap in the assigned scope. Missing exact covariance/test/CI/weight/model definitions remain bounded per relationship. No raw-data reanalysis or preferred-method recommendation was made.


<!-- Active complete pass2 inventory: reports_late -->

# Statistical relationship inventory — pass 2 REPORT-late shard

Fresh runtime agent: `/root/stat2_reports_late`, gpt-6.1-sol/high, FRESH_SPAWN. Exact assigned scope: S221 through S263,43 relationships. Complete current ledger, screening log, mechanical recheck and all47 original checker exclusions were read; full QUALITY_CONTROL_SCOPE.md and review contract were read. Original pass1 records below are retained from the assigned current-run packet and augmented after direct-source review. Source roles are REPORT at every assigned compared location; PLAN documents appear only in cross-lane context. No shared canonical artifact was changed.

Direct authority: supplied PDF page renders from the current run and supplied workbook XML/shared strings freshly obtained by unzip. Existing extraction is a locator. Source/engine provenance is in preprocessing/stat2_reports_late/engine_record.md.

Complete assigned pass1 records. Read the complete ledger, screening log, mechanical recheck and all checker exclusions as cross-lane inputs.

## S221 — eTable8 pre-enhancement 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa 20.5 (14.2, 29.6) 28.5 (23.4, 34.8) 21.3 (15.2, 29.8) 0.96 (0.59, 1.57) 1.34 (0.92, 1.95) 1.39 (0.92, 2.10) 0.138 -120 (11, -10) 14 (7, -67) 13 (6, -84)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct source p.14 confirms percentages20.5/28.5/21.3, RR .96/1.34/1.39 and omnibus .138. Ordered 95% group and RR endpoints contain their points. RR equality null and the three disjoint NNT confidence branches agree in interpretation under local note e; negative NNT−120 belongs to the negative branch. The .138 omnibus does not open the stated <.05 pairwise gate. NNT reciprocal point intervals [−142.857143,−111.111111], [13.698630,14.084507], [12.345679,12.658228] overlap displayed integer intervals. C011 retains the subset model-definition issue; C015 retains the first-header population issue. No pairwise P or covariance is inferred.

## S222 — eTable8 pre-enhancement 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
6 months 32.9 (25.1, 43.0) 32.4 (27.8, 37.7) 25.2 (18.5, 34.2) 1.31 (0.88, 1.95) 1.29 (0.92, 1.80) 0.98 (0.73, 1.33) 0.313 13 (6, -27) 14 (7, -56) -185 (11, -10)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct source p.14 confirms32.9/32.4/25.2, RRs1.31/1.29/.98 and omnibus .313. All percentage and RR points are contained in ordered 95% endpoints. All RRs include1 and all NNT confidence sets use the source's infinity/negative branch rule. Omnibus .313 keeps the pairwise gate closed. Recomputed NNT intervals [12.820513,13.157895], [13.698630,14.084507], [−250,−166.666667] overlap displayed13/14/−185. C011/C015 apply to common model/header interpretation.

## S223 — eTable8 pre-enhancement 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
12 months 32.6 (25.0, 42.5) 37.7 (32.2, 44.3) 20.5 (14.7, 28.6) 1.59 (1.05, 2.41) 1.84 (1.29, 2.63) 1.16 (0.85, 1.57) 0.003     9 (5, 75)   6 (4, 12)   20 (7, -20)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.14 confirms32.6/37.7/20.5, RRs1.59/1.84/1.16, omnibus .003. All points lie inside ordered percentage/RR CIs; active/UC RRs exclude1 and corresponding NNTs are finite positive; HC/PT includes1 and has a two-branch NNT confidence set. Omnibus .003 opens the local gate. NNT reciprocal PT/UC[8.196721,8.333333] versus9[8.5,9.5] has gap .166667/9=.018519; HC/UC[5.780347,5.847953] and HC/PT[19.230769,20] overlap6/20. No new above-threshold point discrepancy. C011/C015 retained.

## S224 — eTable8 post-enhancement 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa 28.0 (24.4, 32.0) 32.7 (29.5, 36.2) 20.4 (17.4, 23.9) 1.37 (1.11, 1.69) 1.60 (1.33, 1.93) 1.17 (0.99, 1.38) <0.001 14 (8, 39) 9 (6, 14) 22 (11, -327)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.14 confirms28.0/32.7/20.4, RRs1.37/1.60/1.17 and omnibus<.001. Ordered percentage/RR CIs contain every point. Active/UC RRs exclude1 with finite positive NNT confidence intervals; HC/PT includes1 and printed22(11,−327) is interpreted as a confidence set using note e. Reciprocal NNT14 versus[12.987013,13.333333] has relative gap .011905;9 versus[8.064516,8.196721] has .033698;22 overlaps[20.833333,21.739130]. All are at most .05. C011 retains model mapping.

## S225 — eTable8 post-enhancement 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
6 months 33.8 (30.1, 38.1) 38.2 (34.5, 42.3) 22.2 (19.1, 25.7) 1.53 (1.27, 1.84) 1.72 (1.44, 2.06) 1.13 (0.97, 1.32) <0.001     9 (6, 16)   7 (5, 10)   24 (11, -88)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.14 confirms33.8/38.2/22.2, RRs1.53/1.72/1.13 and omnibus<.001. Ordered percentage/RR CIs contain every point; active/UC exclude1 while HC/PT includes1 and NNT24(11,−88) uses disjoint branches. Recomputed NNT9 overlaps[8.547009,8.695652];7 versus[6.211180,6.289308] has relative gap .030099;24 versus[22.222222,23.255814] has .010174. All at most .05. C011 remains the adjustment question.

## S226 — eTable8 post-enhancement 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
12 months 36.9 (33.1, 41.2) 38.1 (36.0, 40.3) 28.6 (25.2, 32.5) 1.29 (1.09, 1.52) 1.33 (1.16, 1.52) 1.03 (0.92, 1.16) <0.001   13 (8, 34)   11 (8, 19) 86 (18, -31)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.14 confirms36.9/38.1/28.6, RRs1.29/1.33/1.03 and omnibus<.001. Ordered percentage/RR CIs contain points; active/UC exclude1 while HC/PT includes1 and NNT86(18,−31) uses the source's branch rule. NNT13 versus reciprocal[11.904762,12.195122] has relative gap .023452;11 overlaps[10.416667,10.638298];86 overlaps[76.923077,90.909091]. None exceeds .05. C011 retained.

## S227 — eTable8 reminder-letter 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa 31.6 (26.7, 37.3) 34.1 (29.5, 39.5) 20.5 (16.6, 25.3) 1.54 (1.18, 2.01) 1.67 (1.30, 2.14) 1.08 (0.87, 1.34) <0.001 9 (6, 23) 8 (5, 14)   40 (11, -23)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.14 confirms31.6/34.1/20.5, RRs1.54/1.67/1.08 and omnibus<.001. Containment, endpoint order and active/UC benefit direction agree. HC/PT null-containing RR and NNT40(11,−23) consistently represent a two-branch confidence set. Reciprocal NNT9 overlaps[8.928571,9.090909];8 versus[7.299270,7.407407] has relative gap .011574;40 overlaps[38.461538,41.666667]. C011 retained; the p.13 reminder subset is explicitly post hoc, so no prespecification conflict is invented.

## S228 — eTable8 reminder-letter 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** F-ST1-206

**Printed values and method:**

```text
6 months 35.6 (30.6, 41.4) 40.6 (35.8, 46.1) 21.3 (17.5, 26.1) 1.67 (1.30, 2.14) 1.90 (1.50, 2.41) 1.14 (0.94, 1.39) <0.001 8 (5, 14)  6 (4, 8)    20 (9, -43)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.14 confirms35.6/40.6/21.3, RRs1.67/1.90/1.14 and omnibus<.001. Every group/RR point is contained in its ordered interval. Active/UC null readings and finite NNT CIs agree; HC/PT includes1 and NNT20(9,−43) uses the branch rule. PT/UC difference interval[14.2,14.4] gives NNT[6.944444,7.042254] versus8[7.5,8.5], relative gap .057218; this exact issue is already C004/F-NUM-005 with F-ST1-206 recorded as duplicate. HC/UC NNT6 versus[5.154639,5.208333] leaves .291667/6=.048611 and remains screened by precision. HC/PT20 overlaps[19.607843,20.408163]. C011 retained; no re-emission.

## S229 — eTable8 reminder-letter 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
12 months 38.2 (33.1, 44.0) 38.9 (35.6, 42.5) 26.1 (21.9, 31.2) 1.46 (1.17, 1.83) 1.49 (1.23, 1.80) 1.02 (0.87, 1.20) <0.001 9 (6, 21) 8 (6, 14) 133 (15, -19)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.14 confirms38.2/38.9/26.1, RRs1.46/1.49/1.02 and omnibus<.001. Percentage/RR containment and order hold; active/UC exclude1 while HC/PT includes1 and NNT133(15,−19) follows the branch rule. PT/UC NNT9 versus[8.196721,8.333333] has relative gap .018519;8 overlaps[7.751938,7.874016];133 overlaps[125,166.666667]. C011 retained.

## S230 — Unadjusted binary analysis method and effect identity

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
Narrative:no adjustment,weightingorimputation. Footnote:modified Poisson GEE forbinaryoutcome without adjustment. Heading:unadjusted n/N(%),RelativeRisk(95%CI); titlecontains'adjusted relative risk'. PT/HC/UC groups; contrastsPT/UC,HC/UC,HC/PT.
```

**Pass-1 checks and result:** Repeated definitionsmakeunadjustedstatus immediately identifiable; title wording screened once. Unadjusted crudeproportion ratios provide a diagnosticpoint-estimate check supportedbyexplicitmethod; all 27 RRs agree withratioswithinprecision. No crude-SE-based CI orassumedwithinperson/coach covariance imposed.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.15 introduction, heading and footnote b establish no adjustment, weighting or imputation and modified Poisson GEE for binary outcomes. The title's adjusted word does not identify a different fitted result in this immediate context; prior exclusion retained. All27 displayed RRs have the same direction as the stated contrasts and reconcile with unadjusted proportion ratios under precision. No independent-binomial CI, covariance or test is substituted for GEE.

## S231 — eTable9 pain severity 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa     179/542 (33.0) 229/635 (36.1) 151/621 (24.3) 1.36 (1.13, 1.63) 1.48 (1.26, 1.75) 1.09 (0.94, 1.27)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.15 severity3 row and footnote reread. Recomputed PT/HC/UC percentages 33.025830/36.062992/24.315620 match printed one-decimal values under half-unit intervals. Crude ratio diagnostics PT/UC,HC/UC,HC/PT are 1.358215/1.483120/1.091963; every displayed RR lies within or at most .05 relative gap from its rounding-aware ratio interval. All three RR points lie inside ordered 95% CIs; active/UC intervals exclude1 and HC/PT includes1, with directions matching the group rates. No P/test statistic/SE is printed; modified-Poisson GEE covariance is unspecified, so ordinary independent-binomial SEs are not imposed. Outcome-specific observed denominators are matched to that outcome, not equated with severity counts. No existing candidate applies to the row's values.

## S232 — eTable9 pain severity 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
6 months      225/547 (41.1) 259/621 (41.7) 167/622 (26.8) 1.53 (1.30, 1.80) 1.55 (1.32, 1.83) 1.01 (0.88, 1.17)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.15 severity6 row and footnote reread. Recomputed PT/HC/UC percentages 41.133455/41.706924/26.848875 match printed one-decimal values under half-unit intervals. Crude ratio diagnostics PT/UC,HC/UC,HC/PT are 1.532036/1.553396/1.013942; every displayed RR lies within or at most .05 relative gap from its rounding-aware ratio interval. All three RR points lie inside ordered 95% CIs; active/UC intervals exclude1 and HC/PT includes1, with directions matching the group rates. No P/test statistic/SE is printed; modified-Poisson GEE covariance is unspecified, so ordinary independent-binomial SEs are not imposed. Outcome-specific observed denominators are matched to that outcome, not equated with severity counts. No existing candidate applies to the row's values.

## S233 — eTable9 pain severity 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
12 months 246/583 (42.2) 269/639 (42.1) 197/639 (30.8) 1.37 (1.18, 1.59) 1.37 (1.21, 1.54) 1.00 (0.90, 1.10)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.15 severity12 row and footnote reread. Recomputed PT/HC/UC percentages 42.195540/42.097027/30.829421 match printed one-decimal values under half-unit intervals. Crude ratio diagnostics PT/UC,HC/UC,HC/PT are 1.368678/1.365482/0.997665; every displayed RR lies within or at most .05 relative gap from its rounding-aware ratio interval. All three RR points lie inside ordered 95% CIs; active/UC intervals exclude1 and HC/PT includes1, with directions matching the group rates. No P/test statistic/SE is printed; modified-Poisson GEE covariance is unspecified, so ordinary independent-binomial SEs are not imposed. Outcome-specific observed denominators are matched to that outcome, not equated with severity counts. No existing candidate applies to the row's values.

## S234 — eTable9 pain intensity 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa     164/543 (30.2) 192/635 (30.2) 129/621 (20.8) 1.46 (1.19, 1.78) 1.46 (1.18, 1.79) 1.00 (0.83, 1.21)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.15 intensity3 row and footnote reread. Recomputed PT/HC/UC percentages 30.202578/30.236220/20.772947 match printed one-decimal values under half-unit intervals. Crude ratio diagnostics PT/UC,HC/UC,HC/PT are 1.453938/1.455558/1.001114; every displayed RR lies within or at most .05 relative gap from its rounding-aware ratio interval. All three RR points lie inside ordered 95% CIs; active/UC intervals exclude1 and HC/PT includes1, with directions matching the group rates. No P/test statistic/SE is printed; modified-Poisson GEE covariance is unspecified, so ordinary independent-binomial SEs are not imposed. Outcome-specific observed denominators are matched to that outcome, not equated with severity counts. No existing candidate applies to the row's values.

## S235 — eTable9 pain intensity 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
6 months      183/548 (33.4) 222/622 (35.7) 153/623 (24.6) 1.36 (1.13, 1.63) 1.45 (1.20, 1.74) 1.06 (0.90, 1.26)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.15 intensity6 row and footnote reread. Recomputed PT/HC/UC percentages 33.394161/35.691318/24.558587 match printed one-decimal values under half-unit intervals. Crude ratio diagnostics PT/UC,HC/UC,HC/PT are 1.359775/1.453313/1.068789; every displayed RR lies within or at most .05 relative gap from its rounding-aware ratio interval. All three RR points lie inside ordered 95% CIs; active/UC intervals exclude1 and HC/PT includes1, with directions matching the group rates. No P/test statistic/SE is printed; modified-Poisson GEE covariance is unspecified, so ordinary independent-binomial SEs are not imposed. Outcome-specific observed denominators are matched to that outcome, not equated with severity counts. No existing candidate applies to the row's values.

## S236 — eTable9 pain intensity 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
12 months 218/583 (37.4) 238/641 (37.1) 191/639 (29.9) 1.25 (1.07, 1.47) 1.24 (1.08, 1.42) 0.99 (0.87, 1.12)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.15 intensity12 row and footnote reread. Recomputed PT/HC/UC percentages 37.392796/37.129485/29.890454 match printed one-decimal values under half-unit intervals. Crude ratio diagnostics PT/UC,HC/UC,HC/PT are 1.250995/1.242185/0.992958; every displayed RR lies within or at most .05 relative gap from its rounding-aware ratio interval. All three RR points lie inside ordered 95% CIs; active/UC intervals exclude1 and HC/PT includes1, with directions matching the group rates. No P/test statistic/SE is printed; modified-Poisson GEE covariance is unspecified, so ordinary independent-binomial SEs are not imposed. Outcome-specific observed denominators are matched to that outcome, not equated with severity counts. No existing candidate applies to the row's values.

## S237 — eTable9 pain-related interference 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa     206/543 (37.9) 249/635 (39.2) 169/620 (27.3) 1.39 (1.17, 1.64) 1.44 (1.25, 1.65) 1.03 (0.92, 1.17)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.15 interference3 row and footnote reread. Recomputed PT/HC/UC percentages 37.937385/39.212598/27.258065 match printed one-decimal values under half-unit intervals. Crude ratio diagnostics PT/UC,HC/UC,HC/PT are 1.391786/1.438569/1.033614; every displayed RR lies within or at most .05 relative gap from its rounding-aware ratio interval. All three RR points lie inside ordered 95% CIs; active/UC intervals exclude1 and HC/PT includes1, with directions matching the group rates. No P/test statistic/SE is printed; modified-Poisson GEE covariance is unspecified, so ordinary independent-binomial SEs are not imposed. Outcome-specific observed denominators are matched to that outcome, not equated with severity counts. No existing candidate applies to the row's values.

## S238 — eTable9 pain-related interference 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
6 months      249/546 (45.6) 277/620 (44.7) 176/621 (28.3) 1.61 (1.38, 1.88) 1.58 (1.35, 1.85) 0.98 (0.86, 1.12)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.15 interference6 row and footnote reread. Recomputed PT/HC/UC percentages 45.604396/44.677419/28.341385 match printed one-decimal values under half-unit intervals. Crude ratio diagnostics PT/UC,HC/UC,HC/PT are 1.609110/1.576402/0.979674; every displayed RR lies within or at most .05 relative gap from its rounding-aware ratio interval. All three RR points lie inside ordered 95% CIs; active/UC intervals exclude1 and HC/PT includes1, with directions matching the group rates. No P/test statistic/SE is printed; modified-Poisson GEE covariance is unspecified, so ordinary independent-binomial SEs are not imposed. Outcome-specific observed denominators are matched to that outcome, not equated with severity counts. No existing candidate applies to the row's values.

## S239 — eTable9 pain-related interference 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
12 months 267/583 (45.8) 293/638 (45.9) 221/638 (34.6) 1.32 (1.15, 1.52) 1.33 (1.18, 1.48) 1.00 (0.91, 1.10)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.15 interference12 row and footnote reread. Recomputed PT/HC/UC percentages 45.797599/45.924765/34.639498 match printed one-decimal values under half-unit intervals. Crude ratio diagnostics PT/UC,HC/UC,HC/PT are 1.322121/1.325792/1.002777; every displayed RR lies within or at most .05 relative gap from its rounding-aware ratio interval. All three RR points lie inside ordered 95% CIs; active/UC intervals exclude1 and HC/PT includes1, with directions matching the group rates. No P/test statistic/SE is printed; modified-Poisson GEE covariance is unspecified, so ordinary independent-binomial SEs are not imposed. Outcome-specific observed denominators are matched to that outcome, not equated with severity counts. No existing candidate applies to the row's values.

## S240 — Unadjusted continuous-change descriptive/inferential method

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
Medians(25%-tile,75%tile) forchanges frombaseline; between-groupMEANdifferences95%CIs fromlinear regression GEE;15outcome/timepointrows;omnibusP acrossarms.
```

**Pass-1 checks and result:** Median differences neednot equalmean model differences. Direction is coherent withhigher worsepainandhigher betterfunction. Footnote'meanchange' andmedianheader do not changeeffect-column meaning; screened context observationonce. P is omnibus;pairwise nonsignificanceHC/PT doesnotconflictwithsignificant overall test.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.16 title/header names change medians with25th/75th percentiles, while its effect columns separately name unadjusted between-group mean differences and95% CIs; note b gives linear GEE. Every descriptive center lies inside ordered quartiles. Group-median subtraction is not a method for reproducing GEE means and supplies no route-A category4 premise. Fifteen MD triples satisfy additive closure within their ±.05 intervals; all points are contained in ordered CIs. Omnibus P is joint across three arms, so a null-containing HC/PT interval is not a P conflict.

## S241 — eTable10 pain severity 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa    -1.1 (-2.1, -0.1)     -1.1 (-2.3, -0.1)    -0.6 (-1.6, 0.2)   -0.4 (-0.6, -0.3) -0.4 (-0.6, -0.3) 0.0 (-0.2, 0.2)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.16 severity3; active/UC−.4/−.4,HC/PT0.0; omnibus<.001 row and common linear-GEE footnote reread. All three group change medians are contained in ordered quartiles. All three mean-difference points are contained in ordered 95% CIs, both active/UC CIs exclude0 and HC/PT CI contains0. Additive mean contrasts HC−PT=(HC−UC)−(PT−UC) are feasible within each one-decimal half-unit interval, including central differences that round differently. Direction is consistent with pain improvement for negative pain differences and improved function for positive active/UC differences. Significant omnibus is a joint three-arm test and does not claim significant HC/PT. Group median differences are not equated with model mean differences. Exact omnibus variance/df/CI construction remains unstated; no conventional test is assumed. No existing candidate applies to these displayed tuples.

## S242 — eTable10 pain severity 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
6 months     -1.3 (-2.5, -0.1)     -1.4 (-2.5, -0.2)    -0.8 (-1.8, 0.2)   -0.4 (-0.7, -0.2) -0.5 (-0.8, -0.3) -0.1 (-0.3, 0.1)    <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.16 severity6; active/UC−.4/−.5,HC/PT−.1; omnibus<.001 row and common linear-GEE footnote reread. All three group change medians are contained in ordered quartiles. All three mean-difference points are contained in ordered 95% CIs, both active/UC CIs exclude0 and HC/PT CI contains0. Additive mean contrasts HC−PT=(HC−UC)−(PT−UC) are feasible within each one-decimal half-unit interval, including central differences that round differently. Direction is consistent with pain improvement for negative pain differences and improved function for positive active/UC differences. Significant omnibus is a joint three-arm test and does not claim significant HC/PT. Group median differences are not equated with model mean differences. Exact omnibus variance/df/CI construction remains unstated; no conventional test is assumed. No existing candidate applies to these displayed tuples.

## S243 — eTable10 pain severity 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
12 months    -1.3 (-2.5, -0.3)     -1.4 (-2.5, -0.2)    -0.8 (-2.2, 0.1)   -0.4 (-0.7, -0.2) -0.4 (-0.6, -0.2) 0.0 (-0.1, 0.2)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.16 severity12; active/UC−.4/−.4,HC/PT0.0; omnibus<.001 row and common linear-GEE footnote reread. All three group change medians are contained in ordered quartiles. All three mean-difference points are contained in ordered 95% CIs, both active/UC CIs exclude0 and HC/PT CI contains0. Additive mean contrasts HC−PT=(HC−UC)−(PT−UC) are feasible within each one-decimal half-unit interval, including central differences that round differently. Direction is consistent with pain improvement for negative pain differences and improved function for positive active/UC differences. Significant omnibus is a joint three-arm test and does not claim significant HC/PT. Group median differences are not equated with model mean differences. Exact omnibus variance/df/CI construction remains unstated; no conventional test is assumed. No existing candidate applies to these displayed tuples.

## S244 — eTable10 pain intensity 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa       -0.8 (-1.8, 0.0)   -0.8 (-2.0, 0.0)     -0.5 (-1.5, 0.2)   -0.3 (-0.5, -0.2) -0.3 (-0.5, -0.1) 0.0 (-0.1, 0.2)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.16 intensity3; active/UC−.3/−.3,HC/PT0.0; omnibus<.001 row and common linear-GEE footnote reread. All three group change medians are contained in ordered quartiles. All three mean-difference points are contained in ordered 95% CIs, both active/UC CIs exclude0 and HC/PT CI contains0. Additive mean contrasts HC−PT=(HC−UC)−(PT−UC) are feasible within each one-decimal half-unit interval, including central differences that round differently. Direction is consistent with pain improvement for negative pain differences and improved function for positive active/UC differences. Significant omnibus is a joint three-arm test and does not claim significant HC/PT. Group median differences are not equated with model mean differences. Exact omnibus variance/df/CI construction remains unstated; no conventional test is assumed. No existing candidate applies to these displayed tuples.

## S245 — eTable10 pain intensity 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
6 months        -1.0 (-2.0, 0.0)   -1.0 (-2.2, 0.0)     -0.8 (-1.5, 0.2)   -0.3 (-0.5, -0.1) -0.3 (-0.5, -0.2) -0.1 (-0.3, 0.1)    <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.16 intensity6; active/UC−.3/−.3,HC/PT−.1; omnibus<.001 row and common linear-GEE footnote reread. All three group change medians are contained in ordered quartiles. All three mean-difference points are contained in ordered 95% CIs, both active/UC CIs exclude0 and HC/PT CI contains0. Additive mean contrasts HC−PT=(HC−UC)−(PT−UC) are feasible within each one-decimal half-unit interval, including central differences that round differently. Direction is consistent with pain improvement for negative pain differences and improved function for positive active/UC differences. Significant omnibus is a joint three-arm test and does not claim significant HC/PT. Group median differences are not equated with model mean differences. Exact omnibus variance/df/CI construction remains unstated; no conventional test is assumed. No existing candidate applies to these displayed tuples.

## S246 — eTable10 pain intensity 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
12 months       -1.0 (-2.2, 0.0)   -1.0 (-2.2, 0.0)     -0.8 (-2.0, 0.2)   -0.3 (-0.5, -0.1) -0.2 (-0.4, -0.1) 0.0 (-0.1, 0.2)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.16 intensity12; active/UC−.3/−.2,HC/PT0.0; omnibus<.001 row and common linear-GEE footnote reread. All three group change medians are contained in ordered quartiles. All three mean-difference points are contained in ordered 95% CIs, both active/UC CIs exclude0 and HC/PT CI contains0. Additive mean contrasts HC−PT=(HC−UC)−(PT−UC) are feasible within each one-decimal half-unit interval, including central differences that round differently. Direction is consistent with pain improvement for negative pain differences and improved function for positive active/UC differences. Significant omnibus is a joint three-arm test and does not claim significant HC/PT. Group median differences are not equated with model mean differences. Exact omnibus variance/df/CI construction remains unstated; no conventional test is assumed. No existing candidate applies to these displayed tuples.

## S247 — eTable10 pain-related interference 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa    -1.3 (-2.4, -0.1)     -1.3 (-2.6, 0.0)     -0.7 (-1.9, 0.1)   -0.5 (-0.7, -0.3) -0.5 (-0.7, -0.3) 0.0 (-0.2, 0.2)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.16 interference3; active/UC−.5/−.5,HC/PT0.0; omnibus<.001 row and common linear-GEE footnote reread. All three group change medians are contained in ordered quartiles. All three mean-difference points are contained in ordered 95% CIs, both active/UC CIs exclude0 and HC/PT CI contains0. Additive mean contrasts HC−PT=(HC−UC)−(PT−UC) are feasible within each one-decimal half-unit interval, including central differences that round differently. Direction is consistent with pain improvement for negative pain differences and improved function for positive active/UC differences. Significant omnibus is a joint three-arm test and does not claim significant HC/PT. Group median differences are not equated with model mean differences. Exact omnibus variance/df/CI construction remains unstated; no conventional test is assumed. No existing candidate applies to these displayed tuples.

## S248 — eTable10 pain-related interference 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
6 months        -1.4 (-2.9, 0.0)   -1.6 (-2.9, -0.1)    -0.9 (-2.1, 0.1)   -0.6 (-0.8, -0.3) -0.6 (-0.9, -0.4) -0.1 (-0.4, 0.2)    <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.16 interference6; active/UC−.6/−.6,HC/PT−.1; omnibus<.001 row and common linear-GEE footnote reread. All three group change medians are contained in ordered quartiles. All three mean-difference points are contained in ordered 95% CIs, both active/UC CIs exclude0 and HC/PT CI contains0. Additive mean contrasts HC−PT=(HC−UC)−(PT−UC) are feasible within each one-decimal half-unit interval, including central differences that round differently. Direction is consistent with pain improvement for negative pain differences and improved function for positive active/UC differences. Significant omnibus is a joint three-arm test and does not claim significant HC/PT. Group median differences are not equated with model mean differences. Exact omnibus variance/df/CI construction remains unstated; no conventional test is assumed. No existing candidate applies to these displayed tuples.

## S249 — eTable10 pain-related interference 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
12 months    -1.6 (-3.0, -0.1)     -1.6 (-3.0, -0.1)    -1.0 (-2.6, 0.1)   -0.5 (-0.8, -0.3) -0.5 (-0.7, -0.3) 0.0 (-0.2, 0.3)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.16 interference12; active/UC−.5/−.5,HC/PT0.0; omnibus<.001 row and common linear-GEE footnote reread. All three group change medians are contained in ordered quartiles. All three mean-difference points are contained in ordered 95% CIs, both active/UC CIs exclude0 and HC/PT CI contains0. Additive mean contrasts HC−PT=(HC−UC)−(PT−UC) are feasible within each one-decimal half-unit interval, including central differences that round differently. Direction is consistent with pain improvement for negative pain differences and improved function for positive active/UC differences. Significant omnibus is a joint three-arm test and does not claim significant HC/PT. Group median differences are not equated with model mean differences. Exact omnibus variance/df/CI construction remains unstated; no conventional test is assumed. No existing candidate applies to these displayed tuples.

## S250 — eTable10 social role functioning 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa        1.8 (-2.0, 5.8)   1.9 (-1.9, 6.0)      0.0 (-2.2, 4.3)     0.9 (0.1, 1.7)    1.5 (0.7, 2.2)   0.5 (-0.2, 1.3)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.16 social3; active/UC.9/1.5,HC/PT.5; omnibus<.001 row and common linear-GEE footnote reread. All three group change medians are contained in ordered quartiles. All three mean-difference points are contained in ordered 95% CIs, both active/UC CIs exclude0 and HC/PT CI contains0. Additive mean contrasts HC−PT=(HC−UC)−(PT−UC) are feasible within each one-decimal half-unit interval, including central differences that round differently. Direction is consistent with pain improvement for negative pain differences and improved function for positive active/UC differences. Significant omnibus is a joint three-arm test and does not claim significant HC/PT. Group median differences are not equated with model mean differences. Exact omnibus variance/df/CI construction remains unstated; no conventional test is assumed. No existing candidate applies to these displayed tuples.

## S251 — eTable10 social role functioning 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
6 months         1.9 (-1.9, 6.5)   1.9 (-1.9, 7.4)      1.5 (-3.2, 5.5)     1.3 (0.4, 2.2)    1.7 (0.9, 2.6)   0.4 (-0.5, 1.4)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.16 social6; active/UC1.3/1.7,HC/PT.4; omnibus<.001 row and common linear-GEE footnote reread. All three group change medians are contained in ordered quartiles. All three mean-difference points are contained in ordered 95% CIs, both active/UC CIs exclude0 and HC/PT CI contains0. Additive mean contrasts HC−PT=(HC−UC)−(PT−UC) are feasible within each one-decimal half-unit interval, including central differences that round differently. Direction is consistent with pain improvement for negative pain differences and improved function for positive active/UC differences. Significant omnibus is a joint three-arm test and does not claim significant HC/PT. Group median differences are not equated with model mean differences. Exact omnibus variance/df/CI construction remains unstated; no conventional test is assumed. No existing candidate applies to these displayed tuples.

## S252 — eTable10 social role functioning 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
12 months        1.9 (-1.9, 7.5)   2.0 (-1.7, 7.7)      0.0 (-3.2, 5.8)     1.4 (0.4, 2.3)    1.4 (0.8, 2.1)   0.1 (-0.7, 0.8)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.16 social12; active/UC1.4/1.4,HC/PT.1; omnibus<.001 row and common linear-GEE footnote reread. All three group change medians are contained in ordered quartiles. All three mean-difference points are contained in ordered 95% CIs, both active/UC CIs exclude0 and HC/PT CI contains0. Additive mean contrasts HC−PT=(HC−UC)−(PT−UC) are feasible within each one-decimal half-unit interval, including central differences that round differently. Direction is consistent with pain improvement for negative pain differences and improved function for positive active/UC differences. Significant omnibus is a joint three-arm test and does not claim significant HC/PT. Group median differences are not equated with model mean differences. Exact omnibus variance/df/CI construction remains unstated; no conventional test is assumed. No existing candidate applies to these displayed tuples.

## S253 — eTable10 physical functioning 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa        1.6 (-0.8, 3.6)   1.2 (-0.8, 3.8)      0.9 (-1.4, 3.2)     0.6 (0.1, 1.1)    0.8 (0.3, 1.2)   0.1 (-0.3, 0.6)     0.002
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.16 physical3; active/UC.6/.8,HC/PT.1; omnibus.002 row and common linear-GEE footnote reread. All three group change medians are contained in ordered quartiles. All three mean-difference points are contained in ordered 95% CIs, both active/UC CIs exclude0 and HC/PT CI contains0. Additive mean contrasts HC−PT=(HC−UC)−(PT−UC) are feasible within each one-decimal half-unit interval, including central differences that round differently. Direction is consistent with pain improvement for negative pain differences and improved function for positive active/UC differences. Significant omnibus is a joint three-arm test and does not claim significant HC/PT. Group median differences are not equated with model mean differences. Exact omnibus variance/df/CI construction remains unstated; no conventional test is assumed. No existing candidate applies to these displayed tuples. A labeled diagnostic allowing all source half-unit bounds, additive contrasts, common covariance, symmetric normal95%CIs and chi-square2-reference Wald gives feasible P ranges [.000356,.013254]; the printed P reading is feasible under that diagnostic, so it supplies no additional reporting observation.

## S254 — eTable10 physical functioning 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
6 months         1.7 (-0.8, 4.4)   1.2 (-0.9, 4.4)      1.0 (-1.0, 3.6)     0.8 (0.3, 1.4)    0.5 (0.1, 0.9)   -0.3 (-0.8, 0.2)    <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.16 physical6; active/UC.8/.5,HC/PT−.3; omnibus<.001 row and common linear-GEE footnote reread. All three group change medians are contained in ordered quartiles. All three mean-difference points are contained in ordered 95% CIs, both active/UC CIs exclude0 and HC/PT CI contains0. Additive mean contrasts HC−PT=(HC−UC)−(PT−UC) are feasible within each one-decimal half-unit interval, including central differences that round differently. Direction is consistent with pain improvement for negative pain differences and improved function for positive active/UC differences. Significant omnibus is a joint three-arm test and does not claim significant HC/PT. Group median differences are not equated with model mean differences. Exact omnibus variance/df/CI construction remains unstated; no conventional test is assumed. No existing candidate applies to these displayed tuples. A labeled diagnostic allowing all source half-unit bounds, additive contrasts, common covariance, symmetric normal95%CIs and chi-square2-reference Wald gives feasible P ranges [.000678,.016573]; the printed P reading is feasible under that diagnostic, so it supplies no additional reporting observation.

## S255 — eTable10 physical functioning 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
12 months        1.9 (-0.9, 5.0)   1.3 (-1.2, 4.6)      0.9 (-1.7, 3.6)     1.1 (0.5, 1.7)    0.8 (0.2, 1.5)   -0.3 (-0.9, 0.4)    <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.16 physical12; active/UC1.1/.8,HC/PT−.3; omnibus<.001 row and common linear-GEE footnote reread. All three group change medians are contained in ordered quartiles. All three mean-difference points are contained in ordered 95% CIs, both active/UC CIs exclude0 and HC/PT CI contains0. Additive mean contrasts HC−PT=(HC−UC)−(PT−UC) are feasible within each one-decimal half-unit interval, including central differences that round differently. Direction is consistent with pain improvement for negative pain differences and improved function for positive active/UC differences. Significant omnibus is a joint three-arm test and does not claim significant HC/PT. Group median differences are not equated with model mean differences. Exact omnibus variance/df/CI construction remains unstated; no conventional test is assumed. No existing candidate applies to these displayed tuples. A labeled diagnostic allowing all source half-unit bounds, additive contrasts, common covariance, symmetric normal95%CIs and chi-square2-reference Wald gives feasible P ranges [.0000887,.003671]; the printed P reading is feasible under that diagnostic, so it supplies no additional reporting observation.

## S256 — Complete workbook model-selection P-value family

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-006 worksheet eTable 3](../../../joi250046supp5_prod_1755300121.16087.xlsx), H2:J108; A114
- **Finding links:** None

**Printed values and method:**

```text
Outcome/MissingAll/Missing3M selection headers H/I/J. FootnoteA114 boldmeansP<.10inbothprimary3M-MCIDandatleastonemissingnessmodelafterbase adjustment. All32 populated P cells:

| Cell | Stored value | Formula |
|---|---|---|
| H12 | 1.5599999999999999E-2 |  |
| J12 | 0.05 |  |
| H18 | <0.001 |  |
| I18 | 2.2800000000000001E-2 |  |
| J18 | 5.91E-2 |  |
| H20 | 1.8599999999999998E-2 |  |
| H39 | 6.3600000000000004E-2 |  |
| I39 | 1.9599999999999999E-2 |  |
| H41 | 5.2499999999999998E-2 |  |
| H43 | 5.7599999999999998E-2 |  |
| H45 | 3.0800000000000001E-2 |  |
| I47 | 2.0000000000000001E-4 |  |
| I51 | 1E-3 |  |
| H52 | 7.4099999999999999E-2 |  |
| H54 | 5.1000000000000004E-3 |  |
| H58 | 6.1499999999999999E-2 |  |
| H60 | 1.6999999999999999E-3 |  |
| H66 | 3.2300000000000002E-2 |  |
| H68 | 0.01 |  |
| H72 | <0.001 |  |
| H74 | <0.001 |  |
| H81 | <0.001 |  |
| I81 | 9.4999999999999998E-3 |  |
| H84 | 3.27E-2 |  |
| I84 | 3.3099999999999997E-2 |  |
| H87 | 1.0800000000000001E-2 |  |
| H100 | 4.9200000000000001E-2 |  |
| H101 | 4.9200000000000001E-2 |  |
| H102 | <.0001 |  |
| H105 | <.0001 |  |
| H108 | 2.4500000000000001E-2 |  |
| I108 | 4.0500000000000001E-2 |  |
```

**Pass-1 checks and result:** All populated Pvalues lie0–1or are valid upper bounds; H/I/J aredistinctselection tests, nottreatmentcomparisons. EmploymentH18<.001,I18=.0228,J18=.0591,PHQ8H81<.001/I81=.0095,GAD7H84=.0327/I84=.0331,SDOHH39=.0636/I39=.0196,PEGH108=.0245/I108=.0405meetdual weight selector. EducationH12=.0156,J12=.05 butI12blank; no numeric P asserted for a blank. Selectedweightmembership examinedS262. No estimate, SE, CI,test statisticprinted for these selection tests; no testreconstruction possible.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct supplied workbook ZIP was reread through worksheet XML/shared strings; exact sheet name eTable3 confirmed. H2/I2/J2 separately define primary MCID/overall nonresponse/3-month missingness tests. All32 populated cells listed in this S record exactly match stored values/strings and lie in[0,1] or give valid upper bounds. No numeric test statistic, SE or CI accompanies them. A114 says bold indicates outcome association and missingness at either3months or allpoints, not that each P is a treatment contrast. Education H12=.0156,J12=.05,I12 blank qualifies the either-missingness descriptive flag but the blank does not provide a numeric overall-nonresponse test. Final-weight predictor mismatch remains C012; no blank-to-P conversion is made.

## S257 — Workbook completeness groups and sample implications

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-006 worksheet eTable 3](../../../joi250046supp5_prod_1755300121.16087.xlsx), B3:E3; A110; DOC-005 eTable1 [DOC-005 PDF p.7](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7)
- **Finding links:** None

**Printed values and method:**

```text
Overall2331;MissingAll295;Missing1or2 468;AllObserved1568. FootnoteA110 excludesmissing from percentdenominator. Complete workbook descriptives mapped inreports_restart.
```

**Pass-1 checks and result:** 295+468+1568=2331;468+1568=2036. This agreesanalyticcohortandvisitrows; eTable1 correspondingone+two471differs3,screenedonceasdisplay precision withS202. Baselinecount-percentage checks are assigned to the numeric checker,not duplicated here. Prespecified adjustment flags G4,G10,G11,G38,G54,G80 anchorsbase variables.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct workbook eTable3 B3:E3 confirms2331/295/468/1568;295+468+1568=2331 and468+1568=2036. Source eTable1 p.7 confirms188/283/1568 and2036. Its alternative completeness subtotal2039 and weighted visit subtotal5458 versus5449 remain below precision: half-unit gaps1/2036=.000491 and4.5/5449=.000826; workbook468 versus471 gives1.5/468=.003205. No population-size inference overrides source2036. C017 independently retains E82 depression numerator/percentage/denominator discrepancy; it is not removed by the completeness reconciliation.

## S258 — Adherence histogram method and direction

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.3](../../../joi250046supp4_prod_1755300121.15587.pdf#page=3)
- **Finding links:** None

**Printed values and method:**

```text
PT/VirtualCoach8-sessionhistograms;xticks0,2,4,6,8; proportions0,.2,.4,.6,.8,1.0. Unlabeledbars; visuallyapproximatePTfirst/last .38/.38,VC .18/.63.
```

**Pass-1 checks and result:** No P,CI ormodelclaim. Histogram definition and arms match the intervention dose; exact counts not recoverable without labels. Visualapproximationscannotbeusedasprinted valuesforquantitativediscrepancy. VC/HC terminology is resolved by context, one exclusion.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.3 eFigure1 visually reread. Both histograms describe sessions completed among randomized PT or Virtual Health Coach participants, x-range0–8. The unlabeled bar heights are qualitative visual information, not exact printed counts/percentages. The eight-session intervention identity is coherent with TIDieR. VC/HC wording remains a context-resolved prior exclusion; no CI, test, statistical model or decision assertion is present.

## S259 — Probability/weight diagnostic figure

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.10](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10)
- **Finding links:** None

**Printed values and method:**

```text
eFigure2 observed≥1followupgreenversusnoobservedfollowupsorange;leftestimatedresponseprobability,rightweight;unlabeled barsandfittedsmoothcurves.
```

**Pass-1 checks and result:** Observedresponsegroup higher predicted probability andlower weight coherently matchesinverseprobability weighting. Figureincludesnonsampledresponsegroup fordiagnostics; onlyany follow-upanalysiscontributesfinalweightsum2036. No exact bar counts or bin probabilitiesprinted; no inferential comparison claimed.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.10 eFigure2 and local model/table context reread. Participants with any follow-up have generally higher predicted response probability and lower inverse-probability weights than those without followup. Both groups appear in a diagnostic figure; only the observed-followup analysis weight sum2036 is asserted. No exact bar counts, bins, inferential comparison or common unconditional denominator is supplied. No test or discrepancy is inferred from curve shapes.

## S260 — TIDieR sampling, fidelity and intervention definitions

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-004 PDF pp.2–6](../../../joi250046supp3_prod_1755300121.15087.pdf#page=2)
- **Finding links:** None

**Printed values and method:**

```text
HC12providers;8 sessions45–60min/12 weeks;PT8 sessions30–45min/12 weeks;fidelityplannedrandom5%first12months,onepercoach/6monthslater,thresholds100% content/80% CBT. Reviewed299=193training+89first12months+17later;8/2992.7%,11/2993.7%. Outreach356/77645.9%;extensionn14.
```

**Pass-1 checks and result:** All DOC-004 pages1–7read in the assigned fresh map. No inferential P, CI,statistical model,power calculationorstatistical stopping ruleinTIDieR. The fidelity sampling rule is descriptive protocol administration, not a trial decision rule; percentages reconcile. Intervention definitions support histogram identity; broadclinical or procedure auditnot performed.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct TIDieR pp.2–6 reread visually.12 coaches,8 sessions,12 weeks,online30–45 andcoach45–60minutes,extension 14 andoutreach 356/77645.9% are source-confirmed.299=193+89+17;299/4626=6.463%,89/1791=4.969%,8/299=2.676%,11/299=3.679%,356/776=45.876% reconcile with printed6.5/5/2.7/3.7/45.9 within precision. Fidelity thresholds100% content/80% CBT and5%/one-per-coach-per6months sampling describe administration, not an inferential trial stopping boundary.4626−1791−2350=485 does not conflict because total training sessions are unspecified. C001 retains planned/report online-session-duration comparison; no additional fitted statistical claim is present.

## S261 — Education coding and coefficient attribution

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.7](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7), [DOC-005 PDF p.8](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8), [DOC-005 PDF p.9](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9)
- **Finding links:** F-ST1-204

**Printed values and method:**

```text
eTable2 selectededucation'anycollegevsHSdegreeorless';eTable3 printsAA−.02(−.11,.08),P.866;secondAA .16(.07,.25),P.077;graduate .39(.29,.49),P<.001;eTable4printsAA .97(.82,1.16),P.770;secondAA1.16(1,1.33),P.046;graduate1.35(1.13,1.61),P<.001.
```

**Pass-1 checks and result:** Onebinaryeducationfactorversusthreecategorycontrastsdoesnotidentifytheapplied model. Duplicated AA labels preventmatchingthetwo differentprinted estimates toonecategory, eventhoughworkbookdistinguishesassociate/college/graduate. Source-groundedRouteBobservationconsolidatedwithcoding discrepancy.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.7 selected binary education description and pp.8–9 three education coefficients/reference labels reread; direct workbook A12:A16 confirms four named categories. C013/F-XS-006 already retains binary-versus-three-parameter coding and both repeatedAA labels; F-ST1-204 is screened as duplicate. C014 separately retains the secondAA coefficient CI/P conflicts. No category is assigned to a repeated label by inference. Missing definition remains final education design matrix/category-to-row mapping, including whether selection and fitting used different coding.

## S262 — Weight-model applied covariates versus final selected list

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.4](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [DOC-005 PDF p.5](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5), [DOC-005 PDF p.7](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7), [DOC-005 PDF p.10](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10)
- **Finding links:** F-ST1-203

**Printed values and method:**

```text
eTable2 finalweightadditionPEG,PHQ8,GAD7,SDOH,education;allmodelbase variableslistdoesnotcontainemployment; eTable5weightcoefficientsincludeNot employed1.49(1.11,2.00),P.008 andno educationrow.
```

**Pass-1 checks and result:** Explicitlistandcompletefitdisplaydisagreeonwhichadditional predictorsgeneratedtheweights. Different reference armUC/HCversusPTcan reparameterize the logistic model and is not a finding;the membership difference cannot be resolved by reference choice.


**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct pp.4–5 selection/weight method, p.7 final additions and p.10 fitted weighting table reread. Final list names education; complete fit showsNot employed1.49(1.11,2.00),P=.008 and no education coefficient. Workbook employment H18<.001/I18=.0228/J18=.0591 supports its possible selection without explaining final education membership. C012/F-XS-007 already retains the whole issue and F-ST1-203 is duplicate. A changed reference arm only reparameterizes and does not resolve predictor membership. C014 retainsPEG.96(.92,1.00),P=.037. Actual fitted predictor vector remains undefined.

## S263 — Subset analysis model attribution

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.13](../../../joi250046supp4_prod_1755300121.15587.pdf#page=13), [DOC-005 PDF p.14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14), [DOC-005 PDF p.4](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [DOC-005 PDF p.7](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7)
- **Finding links:** F-ST1-205

**Printed values and method:**

```text
Subsetnarrative'results oftheprimaryanalysisrestrictingtosubsets';primaryselectionstateseducationandemploymentaddedtoimputation/estimation;subsetfootnotelistsexclusivelysex,age,site, rural,morethan1condition,mentalhealth,baselineseverity.
```

**Pass-1 checks and result:** Subset point estimates are explicitly reported, but method mapping is unclear because the primary restricted fit and printed base set are different adjustments. This doesnot inferanythingfromabsenceofweightorimputationterms;onlytheexplicitcovariate lists compared.

**Pass 2 status:** PASS_2_COMPLETE

**Pass-2 source checks and reconciliation:** Direct p.13 restricted-primary narrative, p.14 explicit base-only covariate footnote and pp.4/7 full-primary selected factors reread. Allnine eTable8 subsets share the footnote, omitting education/employment from the full primary set despite primary-analysis attribution. C011/F-ST1-205 already contains every row and the exact model question; source alternatively permits an abbreviated footnote or deliberately refitted base-only models but identifies neither. No absent weighting/imputation term is inferred from silence. C015/C004 remain independent header/point-rule issues; source populations and posthoc/prespecified subset status were matched before any cross-source numeric comparison.


## Scope limitations and no-applicable checks

No superiority decision based on an individual pairwise P outside the gated omnibus rule is reported in these assigned units. No noninferiority/equivalence margin, statistical interim/stopping boundary, power calculation, numeric standard error or numeric test statistic appears in the assigned supplement results. The source states two-sided tests and 95% CIs, but the coefficient-test family, degrees of freedom, coefficient-CI construction and full variance-covariance matrix are not provided: exact numeric P/statistic/SE reconstruction is not asserted. This does not limit CI-null/P-level or point-containment checks. Figures have unlabeled bars; no exact bin counts were extracted. Office conversion is unavailable, but direct cell structure provided exact stable locations. Scientific source-unit coverage gap: none; assigned source pages and workbook were completely mapped by the current fresh mapper and all result-relevant relationships were reviewed here.




## Pass-2 completion and precision rule

43/43 assigned S records receive PASS_2_COMPLETE. No new finding is emitted in this shard. Existing C004/C011/C012/C013/C014/C015/C017 implications are retained without duplicate candidate registration. Every interval-versus-P or point-containment observation remains independent of the .05 display-precision screen; this shard does not screen out C014. All27 eTable8 reciprocal points and all27 eTable9 proportion/RR comparisons were revisited. eTable10 has15 complete outcome/time tuples. Noninferiority/equivalence/interim/statistical-stopping checks have no applicable assertion or margin in the assigned source units. No population-level sample-size/power calculation is supplied here. The unlabeled histograms do not permit exact bin-count extraction. Missing covariance, coefficient-test/CI construction, unrounded risks and final model vectors are named limitations; no unresolved source-reading or assigned-relationship coverage gap remains. Companion RAW pass2 F-ST2-1001 reclaims the prior eTable11 omnibus diagnostic exclusion and is cross-referenced in the checker shard rather than duplicated here.



<!-- Active complete pass2 inventory: plan_a_repair -->

# Statistical pass 2 — bounded PLAN A replacement

Fresh runtime agent: `/root/stat2_plan_a_repair`; model `gpt-6.1-sol`; reasoning effort `high`; start mode `FRESH_SPAWN`. This is a new pass-2 review, disjoint from PLAN B and C replacements. It does not reuse the first-pass agent. It replaces the active S401–S422 portion of the original PLAN pass-2 shard while preserving that shard as provenance.

Exact assigned relationships: S401, S402, S403, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419, S420, S421, S422.

The complete current ledger C001–C018, single screening table with27 finding decisions, mechanical recheck C001–C017, literal47 original checker exclusions, assigned relationship packet, complete scope and complete review contract were read. C018 was already included in the screening log; its appended mechanical recheck was pending when this shard began. No C018 recheck fact is invented. Named gaps in inferential definitions remain explicit. No prior-run conclusions, other-package evidence or web material were used.

## Input and visual bounds

Unique scientific text read:161125 characters by `wc -m` for the five scientific input files (ledger49971, screen12915, recheck69360, exclusions21057, assigned packet7822); the normative scope/review contract and tooling controls are separate workflow instructions. No complete PLAN map or previous PLAN-pass2 output was loaded. Only31 distinct rendered pages were viewed, within the32-page bound. All were current-run exact-source CPU renders from pinned PyMuPDF1.26.4; no new render/OCR derivative was necessary.

| Source and role | Exact distinct physical PDF pages visually reread | Count | Current-run image paths |
|---|---|---:|---|
| DOC-003 SAP, PLAN | 1,2,3,4,8,9,10,11,12,13,16,18,19,20,21,23 | 16 | preprocessing/sap_restart/page-N.png |
| DOC-002 protocol, PLAN | 22,23,25,29,30 | 5 | preprocessing/protocol_a_restart/page-N.png |
| DOC-002 protocol, PLAN | 55,56,57,59 | 4 | preprocessing/protocol_b_restart/page-N.png |
| DOC-001 main, REPORT | 4,10 | 2 | preprocessing/numeric_review/main_p004.png and main_p010.png |
| DOC-005 results, REPORT | 8,15 | 2 | preprocessing/stat1_reports/doc005_p8.png and doc005_p15.png |
| DOC-005 results, REPORT | 17,18 | 2 | preprocessing/stat1_raw/doc005_p017.png and doc005_p018.png |

Administrative/background occurrences in the original locator list were not additional inferential values requiring duplicate visual visits. Their current quantitative specification is directly confirmed at the authoritative SAP and protocol analysis/outcome pages below. All assigned relationships receive a substantive pass2 record; there is no source-reading gap in this assigned inferential scope.

Source links: [SAP title/version](../../../joi250046supp2_prod_1755300121.15087.pdf#page=1), [SAP amendments](../../../joi250046supp2_prod_1755300121.15087.pdf#page=4), [SAP precedence](../../../joi250046supp2_prod_1755300121.15087.pdf#page=10), [SAP sample size](../../../joi250046supp2_prod_1755300121.15087.pdf#page=16), [SAP randomization](../../../joi250046supp2_prod_1755300121.15087.pdf#page=18), [SAP gate/missingness](../../../joi250046supp2_prod_1755300121.15087.pdf#page=19), [SAP primary model](../../../joi250046supp2_prod_1755300121.15087.pdf#page=20), [SAP secondary model](../../../joi250046supp2_prod_1755300121.15087.pdf#page=21), [protocol outcome table](../../../joi250046supp1_prod_1755300121.14087.pdf#page=22), [protocol power](../../../joi250046supp1_prod_1755300121.14087.pdf#page=55), [protocol primary](../../../joi250046supp1_prod_1755300121.14087.pdf#page=56), [protocol secondary](../../../joi250046supp1_prod_1755300121.14087.pdf#page=57), [main simulations/methods](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4).

## Explicit relationship records

P denotes DOC-002 protocol PLAN; A denotes DOC-003 SAP PLAN. M denotes DOC-001 main REPORT. Original pass1 stable IDs and scope are retained. Each record checks count/denominator, estimate/test, method and cross-source implications as applicable; PLAN records have no fitted point/CI/P tuples, so containment and null-test calculations are inapplicable rather than skipped inferential evidence.

| S ID | Status | Direct-source pass2 facts and reconciliation | Missing definitions and current-ledger implications |
|---|---|---|---|
| S401 | PASS_2_COMPLETE | A1: version6.0,18July2024 based on protocol5.0,10November2022. A2–4 identify amendments; A4 describes current pattern-mixture approach plus IPW and masked-outcome rationale. A10 assigns SAP analytical precedence and pre-unblinding approval. A19 retains primary/MAR wording. Historical and current wording remain separate. | Exact final clause hierarchy is the question in C007, not a new finding. Do not claim IPW was undisclosed or assume unchanged historical specifications. |
| S402 | PASS_2_COMPLETE | P29 and A8–9 identify individual parallel three-arm comparative-effectiveness design; PT and HC compared with UC; A9 permits unrestricted pharmacologic/nonpharmacologic care in all arms. No noninferiority/equivalence margin or hypothesis is printed. | No NI/equivalence/stopping conclusion can be reconstructed from an absent rule. No contradiction or preferred design is proposed. |
| S403 | PASS_2_COMPLETE | P29–30 and A18: individual equal allocation after baseline; variable permuted block sizes3,6,9. Each is divisible by3, permitting equal arm allocations. | Exact realized block sequence is unavailable and unnecessary for the stated allocation check. |
| S404 | PASS_2_COMPLETE | P29 and A18 directly agree on EHR sex male versus female/other, BPI severity<7 versus≥7, four clinical sites and rural/medically underserved strata. A2 explicitly changes stratification sex to EHR. | Self-reported sex in a moderator table is another role, not a competing randomization stratum. No additional stratum is assumed. |
| S405 | PASS_2_COMPLETE | A9/16 and P55 state randomized2331=3×777 and analyzed1863=3×621. Targets are analysis versus randomized populations, not interchangeable denominators. Approximate recruitment/site targets in original locator context do not replace these explicit analysis targets. | Actual enrolled count is a separate report quantity. No count-within-display conflict is reproduced. |
| S406 | PASS_2_COMPLETE | P55/A16 retain80% retention. Diagnostic1863/.8=2328.75. Allowing retention[.795,.805] and randomized[2330.5,2331.5] gives retained[1852.7475,1876.8575], overlapping[1862.5,1863.5]. | The small central difference is display precision; no exact retention fraction is supplied. This is reconciled arithmetic, not a new exclusion. |
| S407 | PASS_2_COMPLETE | P55/A16 state primary30% improvement at3months, UC15%, intervention22.5%, difference7.5points, two-sided.05,90% power and Fisher LSD gate.22.5−15=7.5;22.5/15=1.5. M4 states10,000 modified-Poisson simulations. | Full simulation specification, joint-success criterion and dependence are absent. Normal two-proportion calculations remain diagnostics; no stated-method sample-size conflict is established. |
| S408 | PASS_2_COMPLETE | P55/A16 subgroup row372(20%of1863),UC15,active31,difference16,ratio206.7%,80% power.372/1863×100=19.967794%;31−15=16;100×31/15=206.666667. Each displayed interval admits recomputation. |372 is total three-arm subgroup N, not N per arm. Exact gated power calculation is unspecified. |
| S409 | PASS_2_COMPLETE | Same displays:558(30%),UC15,active27.7,difference12.7,ratio184.7%,80% power.558/1863×100=29.951691%;27.7−15=12.7;100×27.7/15=184.666667. Precision-compatible. | Exact gated power algorithm and simulation inputs remain absent. No invented per-arm denominator. |
| S410 | PASS_2_COMPLETE | Same displays:744(40%),UC15,active25.8,difference10.8,ratio172%,80% power.744/1863×100=39.935588%;25.8−15=10.8;100×25.8/15=172. Precision-compatible. | No exact simulation engine or alternative power definition inferred. |
| S411 | PASS_2_COMPLETE | P55–56/A16 explicitly use20–40% subgroup prevalence, sex/mood at least40%, rural/MUA target at least20% and unknown SDOH prevalence. Table quantifies detectable intervention–UC differences. P57/A21 separately introduce moderation. | Within-subgroup pairwise power is not a printed interaction-test power. No preferred interaction calculation or discrepancy is inferred. |
| S412 | PASS_2_COMPLETE | P55/A16/19 specify omnibus Wald any difference among three groups at alpha.05, then each two-sided pairwise comparison at.05 only if the omnibus gate is significant. | No alpha-spending, Bonferroni rule or realized PLAN test statistic is supplied. Report physical6 P=.05 spans gate-satisfying unrounded values; existing precision exclusion stands. |
| S413 | PASS_2_COMPLETE | P56 says all intervals and Pvalues two-sided and significance.05. A19 uses analogous gate for secondary analyses and no safety multiplicity because safety is descriptive/unpowered. | Numeric confidence level is not explicitly supplied in these PLAN clauses; REPORT gives95%. No unreported cross-endpoint adjustment is inferred. |
| S414 | PASS_2_COMPLETE | P22/A11 define binary primary severity MCID≥30% baseline decrease on modified11-item BPI-SF at3months; A20 specifies active/UC primary contrasts. Larger responder risk is favorable. | No PLAN fitted estimate/CI/P is printed. Current report primary threshold/direction is concordant. |
| S415 | PASS_2_COMPLETE | P22/P56 and A11/A20 label severity MCID6/12months secondary and model three follow-up indicators jointly. Primary comparison remains3months; follow-up effects are time-specific. | No numerical results are attributed to a different endpoint/time. |
| S416 | PASS_2_COMPLETE | P22/A11 define30% intensity reduction on4items and interference reduction on7items. Same rows explicitly give3months in adjacent timeframe despite measurement lists baseline/6/12; P57/A21 analyze3/6/12. | The intensity word in interference description and omitted measurement-cell3months resolve immediately by subscale and neighboring timeframe. No outcome-status change is established; exclusions retained. |
| S417 | PASS_2_COMPLETE | P23/A11 define continuous severity11=4intensity+7interference; continuous subscales4 and7; baseline/3/6/12. P57/A21 label these secondary outcomes with3months their primary assessment time. | Primary time within a secondary-outcome family does not convert that outcome to trial primary status. C006 retains separate explicit covariate difference; no new outcome-status finding. |
| S418 | PASS_2_COMPLETE | P23/A12 specify secondary PROMIS social-role4A4items and physical-function6b6items, baseline/3/6/12; A21/P57 give continuous linear modeling. | No PLAN tuple or scale-to-estimand conflict exists. Report physical-function inferential compatibility is separately C018, not a PLAN method critique. |
| S419 | PASS_2_COMPLETE | P23/A12 specify one PGIC item each for pain and overall status at3/6/12. A4 amendment explicitly supplies two items and says actual assessments unchanged. | No binary cutpoint is printed in PLAN. Item-count history is disclosed, not a changed outcome. C016 concerns REPORT summary identity, not PLAN scale inconsistency. |
| S420 | PASS_2_COMPLETE | P25/A12 define continuous≥60-day opioid supply within preceding90days, EHR quarterly. P25 baseline day0 and A12 baseline day1 are distinct stated origins;3/6/9/12 quarterly extraction and3/6/12 analysis can coexist. | No reported opioid estimate or decision uses the day-origin difference here; preserve origin instead of silently normalizing it. |
| S421 | PASS_2_COMPLETE | P25/P59 and A12–13/A23 identify PHQ8,GAD7,PROMIS sleep6a,high-impact/graded pain as exploratory/tertiary, baseline/3/6/12, same approach as secondary models. | No reported ancillary tuple, changed outcome status or claimed complete ancillary report is supplied. No new omission finding. |
| S422 | PASS_2_COMPLETE | P56 and A20–21 explicitly specify binary-responder modified Poisson log-link GEE, RR estimand, independent working correlation and robust sandwich accounting for person/health-coach correlation and binary mean–variance mismatch. | Model choice is stated and coherent. No crude/logistic substitute, coefficient-test distribution, covariance or degrees of freedom is inferred. C005/C006 concern covariate specification, not the stated link/model family. |

## Cross-lane ledger/recheck implications

All18 registered cards were considered. C005's age prespecification remains distinguishable from A20's broad baseline candidate list; C006's outcome-specific baseline addition remains distinct from inherited primary factors; C007 retains both amendment support and unconditional MAR wording, without alleging absent IPW authorization or missing complete-case results. C001's session-duration issue lies outside the assigned inferential comparison list and remains on the ledger without being re-emitted. C002–C004,C008–C018 concern reported arithmetic, estimands, intervals, summaries or model attribution; none licenses importing their unreported covariance/test conventions into PLAN records. C018 already records the raw physical-function exclusion's reopening; its facts are not counted as a new finding of this replacement shard.

The independent review of all47 literal exclusions is recorded row by row in checkers/parts/stat2_plan_a_repair.md. Forty-six retain their exclusion treatment; the remaining physical-function test observation is already included as C018. New findings:0. Every assigned relationship is PASS_2_COMPLETE. No evidence state, inclusion-audit classification or human disposition was changed by this statistical shard.


<!-- Active complete pass2 inventory: plan_b_repair -->

# Statistical pass 2 — bounded PLAN-B replacement

Fresh runtime agent: `/root/stat2_plan_b_repair`; model gpt-6.1-sol; effort high. This active replacement covers exactly S423, S424, S425, S426, S427, S428, S429, S430, S431, S432, S433, S434, S435, S436, S437, S438, S439, S440, S441, S442, S443, S444, S445, S446, S447, S448, S449. No relationship from another shard is assigned here. Every assigned relationship is PASS_2_COMPLETE. Findings: 0 new. The supplied plan pages contain specifications, not fitted estimate/CI/P tuples; numeric inferential checks are therefore applied to reported counterparts through the complete current ledger/recheck without inventing plan coefficients.

Read completely: QUALITY_CONTROL_SCOPE.md, workflow_1_6_2/review_contract.md, tooling_record.md, current candidate_ledger.md (C001–C018), screening/inclusion_screen.md (27 decisions), verification/evidence_recheck.md (17 completed initial cards, appended C018 pending at assignment), review_packets/checker_exclusions.md (47 original exclusions), and only the assigned relationship packet review_packets/pass2_plan_b_repair.md. Additional scientific text was restricted to protocol OCR pages13,16,19. Scientific text input measured with `wc -m`:169649 characters across those eight scientific artifacts, below200000. No full PLAN map or prior PLAN pass-2 conclusions were loaded. No web or new scientific Python was used. Sources and reused derivatives were not modified.

## Source inspection and exact visual budget

Exactly32 distinct source-page images were viewed: PLAN DOC-002 protocol physical PDF pp.16,25,26,27,33,34,41,43,46,47,49,50,56,57,58 (15); PLAN DOC-003 SAP physical PDF pp.2,4,8,9,11,12,13,14,15,18,19,20,21,22,23,25,26 (17). No other page image was viewed or rendered in this shard.

SAP images are current-run `preprocessing/sap_restart/page-N.png`; protocol pp.25–27 are current-run `preprocessing/protocol_a_restart/page-N.png`, protocol pp.33 onward are current-run `preprocessing/protocol_b_restart/page-N.png`. Those current-source renders were produced by pinned PyMuPDF1.26.4 CPU as recorded in tooling. Protocol p.16 is the eligible immutable original earlier-workflow image `.ai_paper_validation/review_1_5_1/preprocessing/doc002_render/p016.png`, original renderer unversioned, visually inspected as an evidence aid linked to the supplied protocol; it is not an old scientific conclusion. No new derivative was created. Current protocol OCR pp.13,16,19 uses the recorded pinned RapidOCR1.3.24 CPU. Exact supplied PDFs remain authority; OCR was used only for redundant synopsis/time/dose locators, and p.16's critical schedule was visually confirmed.

Source links: P denotes PLAN [supplied protocol](../../../joi250046supp1_prod_1755300121.14087.pdf#page=56); A denotes PLAN [supplied SAP](../../../joi250046supp2_prod_1755300121.15087.pdf#page=20). REPORT comparator facts below refer to the current mechanical cards, not a claim that additional REPORT images were opened here.

## Complete relationship records

| S ID | Exact source locations and roles | Pass-2 source-grounded checks, cross-lane implications and missing definitions | Pass 1 | Pass 2 |
|---|---|---|---|---|
| S423 | PLAN P p.56; PLAN A p.20 | Both explicit primary covariate sets name baseline severity, sex, clinical site, rural/MUA residence, multisite pain and co-occurring mental-health condition. A§13 also lists age among candidate baseline variables, distinct from the fixed primary vector. C005 retains reported age-as-prespecified membership; neither C005's direct comparison nor its possible generic-selection interpretation changes. Exact final fitted vector/coding and additional prospective specification are unavailable. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S424 | PLAN A pp.20–21; PLAN P p.56 | Equation uses log E(Y), Int1/Int2, T6/T12, four arm×time terms and βzZ, with UC and3months references. Algebra gives log RR β1/β2 at3, β1+β5/β2+β6 at6, β1+β7/β2+β8 at12. At each time the active/active contrast is the difference of corresponding active/UC log contrasts. No coefficient covariance, numerical coefficients or contrast SEs supplied; none inferred. Explicit coding is coherent. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S425 | PLAN A pp.2,20–21; PLAN P pp.56–57 | SAP explicitly describes Poisson log-link for nonrare binary outcomes and robust sandwich treatment of within-person and within-health-coach dependence with working independence. Amendment p.2 records coach clustering. Working independence and robust dependence accounting are distinct steps, so they do not contradict. Complete cluster IDs, software call, sandwich small-sample details unavailable; mere absence is not a finding. Current main recheck supplies corresponding highest-level clustering context. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S426 | PLAN P p.57; PLAN A p.21; REPORT main method in C006 | Secondary continuous outcomes use linear regression, binary/count outcomes Poisson, longitudinal GEE, intervention×time,3months primary time. Explicit covariates are baseline severity and strata; same-proposed-approach language can inherit primary factors. C006 already retains the report's outcome-specific baseline adjustment difference, with inheritance ambiguity. Do not re-emit or assert multisite/mood necessarily excluded from PLAN. Exact per-outcome implemented vectors, including PGIC baseline handling, unavailable. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S427 | PLAN P pp.41,56; PLAN A pp.18,21 | A§6.2 says eligible subjects are analyzed as assigned, no modifiedITT; A p.21 and P p.56 retain everyone randomized regardless intervention engagement/exposure. P p.41 distinguishes intervention cessation, withdrawal and continued assessment outreach. Conditional as-treated sensitivity is separate, so no adherence restriction is inferred for effectiveness. Participant-level eligibility/withdrawal records unavailable; C007 separately retains follow-up-contributor versus target-population analysis-role ambiguity. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S428 | PLAN A pp.18,25–26; PLAN P pp.49–50 | Primary safety set includes all randomized; secondary safety set excludes intervention participants deemed ineligible after randomization and unable to continue. Safety outcomes are deaths/hospitalizations, summarized descriptively; no formal test or NI comparison is promised. Primary/secondary samples explicitly distinguish denominators. Actual participant-level allocations and secondary safety counts unavailable; no unstated denominator mapping inferred. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S429 | PLAN A p.18; PLAN P pp.33,46 | Enrollment excludes recent/current pain CBT; after enrollment other treatment is unrestricted and measured. Per-protocol/as-treated sample is considered if UC crossover to outside CBT exceeds10%. These are temporally different rules. No source shows the trigger occurred or prints an as-treated estimate; no omission is inferred. Exact crossover percentage and implemented conditional decision absent. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S430 | PLAN A pp.9,18; PLAN P pp.16,43 | Adherence threshold is≥6of8 sessions,6/8=.75. Eight sessions weekly and intended8weeks/max12weeks are compatible with flexible completion; maximum schedule is directly confirmed p.16. P p.43 describes pause/resume self-paced sessions. The randomized online denominator/percentage discrepancy remains C002; planned versus reported session duration remains C001. No new dose threshold conflict. Patient-level adherence and any extension allocation unavailable. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S431 | PLAN P pp.16,47; PLAN A pp.8,11–13 | Exact schedule windows80–140,170–230,350–410days are ordered and disjoint; nominal3/6/12months do not replace those windows. Baseline/randomization precedes notification and follow-up; perceived-support notification is separately defined. Binary secondary table measurement cells omit3months but adjacent primary timeframe and A p.21 explicitly include3months, so no absent endpoint inferred. Actual per-person dates absent. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S432 | PLAN A pp.4,19; PLAN P pp.41,56; REPORT C007 | A p.19 retains primary-follow-up/MAR wording and a trigger>15% at3months or differential missingness. A p.4 amendment gives12.1% missing all follow-up as rationale for adding IPW and calls pattern mixture the current approach. These denominators are not equal and12.1 does not refute the trigger. C007 retains competing primary/sensitivity labels with disclosed amendment/first-approach support. Exact final hierarchy and observed trigger details unavailable; IPW authorization is directly supplied. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S433 | PLAN A p.19; PLAN A p.4; REPORT C007 | Pattern-mixture imputation is conditioned on missingness patterns among those with≥1follow-up; IPW represents those with no follow-up. These disjoint availability patterns are explicitly described and p.4 amendment broadens interpretation to all randomized. C007's source-grounded amendment alternative is retained. Actual imputation count/parameters, covariance, covariate vector/truncation and final primary-versus-sensitivity hierarchy absent; no numeric mechanism inferred. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S434 | PLAN A p.19 | Extreme sensitivity assigns every missing active outcome to no MCID and missing UC outcome to MCID at each missing time. This lowers favorable active-versus-UC response differences, agreeing with the stated worst/best-case direction. Current recheck confirms complete-case sensitivity is present; extreme sensitivity has no PLAN fitted CI/P to reconcile. Exact observed missingness inputs and fitting output unavailable here, so no quantitative replacement or counterfactual outcome inferred. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S435 | PLAN A p.21; PLAN P p.43; REPORT C011/C015 context | A p.21 names8/9/2021 after~140enrolled; P p.43 names the same date for revised MI-based onboarding. The date defines the planned postchange analysis subset independently of approximate historical enrollment. C011 retains restricted-model vector and C015 the displayed contributor-count convention; neither turns~140 into an actual analytic denominator. Date/count observation remains peripheral because the date and reported454/1877 subset definitions agree. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S436 | PLAN A pp.19–20; PLAN P p.56 | Descriptives expressly permit mean,median,SD,min,max,count,percentage by arm; survey outlier changes are not planned while economic99th-percentile Winsor sensitivity is. Different outcome classes do not create inconsistent outlier rules. C016's unresolved mean-versus-median raw report labels are independent of the plan's allowance for both. Actual economic outliers/percentiles and fitted survey records unavailable; no preferred processing proposed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S437 | PLAN P pp.25–26,57–58; PLAN A pp.14,20–22 | Moderator sex is self-reported male vs female/other; randomization sex from EHR is separate. Age<65/≥65 and four race/ethnicity categories are explicitly stated; no overlap or absent age segment. No subgroup fitted estimates/SEs/CI/Ps supplied in PLAN. Source-specific measurements are not silently equated; exact realized subgroup counts/coding absent. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S438 | PLAN P pp.26,34,57–58; PLAN A pp.14,20–22 | Rural uses RUCA4–10, urban1–3; MUA is an additional geography/high-needs shortage criterion, so no exclusive three-way count partition assumed. Planned moderation/residence adjustment targets same named groups. No source count contradicts these definitions. EHR geocodes and individual MUA classifications unavailable. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S439 | PLAN P pp.26,57–58; PLAN A pp.14,20–22 | Eight named pain clusters are back,neck,limb/joint/arthritic,fibromyalgia,headache,orofacial/ear/TMJ,chest,general. P numbers1–8; A numbers1,3–9 but names the same eight. Single vs>1cluster and prior360days are supplied. Numbering omission changes no cluster identity or extractable outcome; screen notation only. Individual diagnosis mapping and observed moderator estimates absent. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S440 | PLAN P pp.26,57–58; PLAN A pp.14–15,20–22 | Mood uses ICD depression/anxiety during prior360days. SDOH is≥1endorsed need domain among financial1item,food2,transport2,housing3;1+2+2+3=8items across4domains. Definition is domain endorsement, not threshold on total score. PHQ/GAD exploratory measures are separately identified. No conflicting fitted moderator result; realized ICD/domain classifications unavailable. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S441 | PLAN P pp.25,57–58; PLAN A pp.20–22 | Seven moderators enter separate main plus moderator×arm×time models; P table says6months, P analytic text/A p.22 primary interaction3months. Model can generate all3/6/12time contrasts. Direct ancillary plan-time difference is retained as PERIPHERAL_COMPARISON because no supplied reported subgroup result or primary/key-secondary decision rule relies on it. Do not call it rounding or suppress a reported outcome-status change; none supplied here. Exact fitted moderator results absent. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S442 | PLAN P p.57; PLAN A pp.8,21–22 | Prospective prediction favors HC over PT for complex/mood/multisite/rural-MUA/socialneed participants. This is a directional hypothesis, while the model assesses heterogeneity with intervention interactions; it is not a completed superiority/NI/equivalence claim. No observed subgroup P, margin or opposite result printed. Outcome-specific subgroup findings and interaction df absent. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S443 | PLAN P pp.27,47,58; PLAN A pp.15,22–23 | Catastrophizing6items and self-efficacy5items assessed baseline→3months; support2items at notification→3months. P p.47 explicitly designates notification survey as baseline for support.6month severityMCID follows mediator assessment. The generalized baseline-change prose is immediately reconciled by the explicit measure-specific origin; no rerandomization/preassignment measurement is inferred. Participant-level mediator values/results absent. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S444 | PLAN P p.58; PLAN A p.22 | Separate active/UC mediation analyses occur only for interventions with significant6month outcome effects; primary mediation target severityMCID6months and explanatory secondary targets are explicit. Source coherently states its selection framework; no alternative causal method proposed. No fitted selected arm/mediator result, mediation significance threshold beyond text, or decomposition covariance printed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S445 | PLAN A p.22 | Step1 log E(Y)=β0+β1Int+βzZ for6month binary MCID. Z supplied as baseline adjustment vector, active indicator and response scale defined. It describes a response-probability log-mean comparison, not an odds ratio. No numerical coefficient/SE/CI/P or final Z vector supplied; no fitted effect reconstructed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S446 | PLAN A pp.22–23 | Step2 E(M)=βM0+βM1Int+βMzZ models continuous baseline→3month change, fitting each mediator. Selection P<.10 for association with either intervention is expressly distinct from primary testing.05 and need not match it. No selection P or mediator fit printed. Exact moderator correlations, selected mediators and numerical baseline vectors unavailable. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S447 | PLAN A p.23 | Step3a prose specifies baseline-confounder adjustment but equation βW0+βWMMsub omits Z. This is a directly read ancillary mediation specification difference, with no reported fitted mediation result attached. PERIPHERAL_COMPARISON applies because it does not alter an available primary/key-secondary analysis or decision rule. No claim the implemented model omitted confounders. Actual treatment-model vector and mediation output absent. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S448 | PLAN A p.23 | Weights are1/expit(η) for Int1 and1/[1−expit(η)] for Int0, η=βW0+βWMMsub. Both are positive for finite η and match probability of the person's assigned group. They are mediator-rebalancing weights, distinct from no-follow-up response weights in C007/C012. No realized coefficients/weights/truncation, mediator covariance or unreported positivity outcome inferred. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S449 | PLAN A p.23 | Step3 uses the same binary6month mean model asStep1 with Step3a weights, then compares weighted and unweighted intervention effects. Source also describes each mediator independently after multivariate weighting. No quantitative direct/indirect decomposition or reported mediation number exists here, so no method preference or unprinted algorithm is imposed. Exact decomposition/link-scale conventions and fitted outputs absent. | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Cross-lane and exclusion reconciliation

Every initial stable candidate and appended C018 was read as context. C001/C002 connect dose and adherence, C005/C006 adjustment, C007 missing-data hierarchy, C011 restricted-model attribution, C012/C013 response-weight/coding membership and C015 contributor counts. C003/C004/C008–C010/C014/C016–C018 concern printed REPORT tuples and remain with their already assigned exact locations and methods; no PLAN coefficient is substituted for those tuples. C017 is an exact workbook arithmetic comparison and is unaffected by PLAN descriptive permissions. No interval-versus-P, point-containment, printed value, count or planned/reported candidate was removed through a wording/context/conditional rationale.

All47 original checker excluded observations were reread independently against Route A and half-unit precision. The companion checker artifact records one row per original exclusion and the explicit C018 reopening. It does not add another F-ST2 ID for the already-screened C018. Missing definitions for ordinary approximate power diagnostics and unconstrained imputation-coefficient test reconstruction remain missing; they do not constitute a new contradiction. No scientific coverage gap remains for these27 assigned specifications.


<!-- Active complete pass2 inventory: plan_c_repair -->

# Fresh bounded PLAN statistical pass 2 — replacement C

Runtime agent: `/root/stat2_plan_c_repair`; model `gpt-6.1-sol`; reasoning effort `high`; start mode `FRESH_SPAWN`. Exact disjoint scope: S450, S451, S452, S453, S454, S455, S456, S457, S458, S459, S460, S461, S462, S463, S464. All fifteen records receive PASS_2_COMPLETE. This stage replaces the corresponding active PLAN pass-2 scope; it does not delete the earlier stage's provenance.

The scope and review contract were read completely. The complete current eighteen-candidate ledger, twenty-seven-decision screening log, mechanical recheck for C001–C017, all forty-seven original checker exclusions and the assigned fifteen-record packet were read. C018 had an included independent screen and complete registration facts but its fresh mechanical recheck was pending at this stage. Its observation is already registered and is not emitted again. Scientific-record input is 159184 characters using the recorded file lengths; normative instructions and tooling metadata are separate controls. No complete PLAN extraction map or other PLAN statistical packet was loaded.

Exact-source critical-page inspection used thirty-two distinct rendered pages, including all report context pages (none were needed): DOC-002 physical PDF pages **5, 24, 27, 28, 30, 31, 32, 33, 37, 47, 48, 49, 50, 51, 53, 58, 59, 60, 61, 62**; DOC-003 pages **3, 9, 10, 13, 17, 18, 19, 23, 24, 25, 26, 27**. Current-run pages are pinned PyMuPDF1.26.4 CPU renders at preprocessing/protocol_a_restart, protocol_b_restart and sap_restart. Protocol p5 is the eligible earlier-workflow page image at `.ai_paper_validation/review_1_5_1/preprocessing/doc002_render/p005.png`; only that source image was consulted, with no earlier scientific conclusions. No fresh OCR/rendering, new Python helper, web input, source modification or reused-asset modification occurred. Administrative/reference pages represented by S464 were revisited through the complete assigned source-linked record; no inferential tuple was invented for bibliography entries.

P denotes PLAN [DOC-002 protocol](../../../joi250046supp1_prod_1755300121.14087.pdf#page=24); A denotes PLAN [DOC-003 SAP](../../../joi250046supp2_prod_1755300121.15087.pdf#page=13). Roles follow prospective content. A source cited as corroboration does not create a conflicting relationship.

| S ID | Exact source locations and directly checked facts | Count, estimate/test, method and cross-source pass-2 reasoning | Precisely missing definition/input and ledger implication | Pass 2 |
|---|---|---|---|---|
| S450 | P24,58–59; A13,23–24: additional patient achieving 30% severity reduction at12months and QALY; EQ-5D-5L at baseline,3,6,12months; active interventions compared with each other/UC | Economic outcome/time and units agree. Twelve-month ancillary economic outcome does not replace the trial's three-month primary severity response. No fitted economic estimate, CI or test appears in the assigned source record; no containment or null calculation applies. | Economic fitted result, utility-conversion implementation and economic analysis denominator absent. Ancillary absence alone does not establish changed primary/key-secondary outcome status. No new candidate. | PASS_2_COMPLETE |
| S451 | P58–59; A23–24: health-plan perspective, KP administrative capture, Essentia inclusion contingent on exploratory data-completeness assessment; implementation/training/delivery/utilization costs | Conditional economic-site inclusion concerns cost-data availability rather than the effectiveness analysis population. Cost components and perspective match. No printed economic denominator is available to recompute. | Actual economic sites/participants, resource quantities and costing inputs absent. This absence alone supplies no observable conflict with a reported economic result. | PASS_2_COMPLETE |
| S452 | P58–59; A24: nb_i=λ×effect_i−cost_i; willingness-to-pay example $30000–100000 per QALY; CEAC | Both formulas have monetary net-benefit units when λ is cost/effect; positive λ makes larger benefit increase net benefit. The example willingness-to-pay range is an economic sensitivity axis, not a superiority, noninferiority, multiplicity or stopping margin. No reported CEAC probability needs reconciliation. | λ grid, fitted coefficients, covariance and CEAC probabilities absent. No distribution or sidedness inferred. | PASS_2_COMPLETE |
| S453 | P59; A19,24: health-care costs overall and pain-specific, GEE with appropriate link functions, applicability/replication/scale sensitivity; economic outliers Winsorized to99th percentile | Economic outlier handling is explicitly distinguished from bounded questionnaire outcomes. These prospective choices are internally coherent; no preference for another cost model is introduced. No fitted cost number conflicts with its description. | Exact link/distribution, fitted cost covariance, outlier values and sensitivity outputs absent; absence alone is not a reporting issue. | PASS_2_COMPLETE |
| S454 | P59; A24–25: pain-related/total table with medication, primary-care, PT/OT/physiatry, pain clinic, mental-health/addiction, ER, other specialty and inpatient categories; empty result cells | Prospective blank cells are placeholders, not observed zero counts. Notes identify pain-linked diagnostic/medication coding and exclude already-listed services from other specialty care. There are no values from which to compute a total or compare an interval/test. | Cost-category amounts and aggregation outputs absent. Do not turn empty planning cells into reported zeros. | PASS_2_COMPLETE |
| S455 | P49–51; A25–26: death and inpatient hospitalization during active participation, excluding hospitalization scheduled before enrollment; six-monthly EHR ascertainment and self-report | Definitions and ascertainment windows match. An event frequency and number of participants with events are distinct summary quantities. P49's850 participants/12deaths/287hospitalizations describe historical PPACT, not RESOLVE observed safety counts. | Actual RESOLVE safety event counts and exposure-specific denominators not supplied in this assigned PLAN family. No fabricated event-rate calculation. | PASS_2_COMPLETE |
| S456 | P50; A3,10,26: protocol physician review of each death/hospitalization; October19,2020 SAP amendment removes routine hospitalization review; current SAP reviews all deaths and selected hospitalizations if relatedness is suggested | The disclosed amendment, current text and explicit SAP precedence reconcile the procedural update. SAE death/hospitalization definitions remain the same. This is not an absent or substituted primary/key-secondary analysis under RouteA5. | No additional input is needed to read the amendment. Actual safety classifications cannot be reconstructed without event records. Original exclusion retained as CONTEXT_RESOLVES. | PASS_2_COMPLETE |
| S457 | P49–51; A25–26: unequal intervention-contact opportunities for unsolicited AE reports; no meaningful between-arm AE comparison; SAE descriptive summaries and no formal tests, explicitly no powered safety noninferiority | The source states a coherent descriptive strategy and differentiates AE and SAE ascertainment. Neither formal safety superiority nor a noninferiority claim is supplied here; no margin or null test can be imported. | No safety test statistic, P value, NI margin or inferential safety claim supplied. Their absence is consistent with the stated strategy. | PASS_2_COMPLETE |
| S458 | P50–51; A26: related/possibly related/not related; mild/moderate/severe AE categories; expectedness; SAE frequency/subjects/timing by arm | Category definitions and summary units are explicit. Relatedness classifications are not treatment-effect estimates or mediator coefficients. No printed category distribution must sum to a reported total. | Observed category totals and participant-level classifications absent. No quantitative inconsistency follows from definitions alone. | PASS_2_COMPLETE |
| S459 | P53,59–60; A25–27: twice-yearly DSMB; notify chair for unexpected AND related SAE; recommendations for temporary recruitment/procedure suspension and ad-hoc meeting | Safety review cadence and operational suspension authority are consistent with no formal efficacy/futility interim test. No numerical alpha-spending, efficacy boundary or stopping conclusion is supplied. | DSMB charter details and actual stopping decision not supplied; no assumed decision threshold. | PASS_2_COMPLETE |
| S460 | P60; A27: no planned primary/secondary interim analysis; safety-requested interim effectiveness estimates permitted; no formal efficacy/futility analysis | Requested descriptive effectiveness estimates do not assert a planned sequential inferential decision. The two plans repeat the same language, with no conflict between permission and prohibition of formal efficacy/futility testing. | Actual request, interim estimates and sequential test statistic absent. No candidate solely for an unreported request. | PASS_2_COMPLETE |
| S461 | P5,32–33,37; A3,17–18: age≥18,English,360-day enrollment/pain lookback; KP≥2 encounters>60days apart/Essentia≥1; surgery60days,cancer≥2 encounters60days,no hospice360days/KPWA OUD; protocol amendment history says30days | Current protocol and SAP eligibility agree. Historical30-day wording differs from the current60-day rule, but this plan-history comparison does not supply a changed primary/key-secondary result, effectiveness analysis-population size or decision rule. Severe cognitive impairment/OUD absent from a condensed report list does not affirmatively establish included participants. F-XS-001 already has its independent terminology screen; do not re-emit. | Actual enrollment ascertainment record needed to establish a population change. History comparison remains PERIPHERAL_COMPARISON; absent condensed criteria remain CONDITIONAL_OR_UNREPORTED. | PASS_2_COMPLETE |
| S462 | P32–33,37; A17–18: most/everyday pain AND limitations over3months, PEG≥12; CBT past6months/current/nextmonth and substance-care current/nextmonth exclusions; planned pain surgery12months | Eligibility PEG threshold12 is a three-item summed screening rule, distinct from BPI severity randomization stratum7 and response threshold30%. All plan exclusion windows match. No printed threshold substitutes for another outcome definition. | No participant screening values supplied for count reproduction; no inferential test applies to eligibility definitions alone. | PASS_2_COMPLETE |
| S463 | P27–28,47–48,61–62; A9: qualitative purposive sampling by response/site/arm/residence; approximately100 completers plus20 noncompleters, approximately12staff; reach approached/eligible denominators; SAP states Aim3 uses no statistical analyses | Approximately120patients is a prospective sampling target, not an effectiveness denominator. Outcome/site/response sampling is explicitly purposeful; no probability-sample test inferred. Framework descriptions name counts that are outside quantitative-result/design focus. No primary/key-secondary numeric outcome is reassigned. | Actual ancillary interview totals, coded qualitative outcomes and reach rates absent. A framework-count wording observation remains OUT_OF_FOCUS. Stakeholder target and other administrative locations retain assigned source-linked record provenance rather than a claim of individually viewed extra pages. | PASS_2_COMPLETE |
| S464 | P30–31,49; remaining P65–77/A5–7,28–29 are administrative/references in assigned record: historicald=.43/.33; OR5.0(2.0–12.5),OR5.4(2.3–12.8); PPACT850,12deaths,287hospitalizations=116+171 | Historical OR points are contained in ordered positive intervals excluding1, consistent with the nearby historical significance description. No exact P is supplied to reconstruct. Hospitalization116+171=287 reconciles; these are events, not necessarily unique patients. Historical standardized effects have no accompanying tests. Bibliographic citation numbers do not become trial counts or inferred source-study results. | Historical covariance/test family/unrounded tuples absent, without a conflicting printed test. References are not followed externally. No fresh candidate or scientific coverage limitation in the assigned relationship family. | PASS_2_COMPLETE |

All C001–C018 implications were considered: C001–C017 source/recheck facts remain as screened; C018's same-display physical-function reconstruction is a REPORT inferential question and remains registered with its inferential alternatives. This PLAN subset supplies no new contradiction or replacement value for those candidates. Economic/safety/administrative ancillary detail is not promoted to a primary-result issue solely because it is unreported. Companion shards cover the disjoint remaining PLAN relationships and registered primary covariate/missing-data comparisons.

Limitations are named in each record. There is no missing assigned S record. No source family in this shard supplies an unexamined reported superiority/NI/equivalence/multiplicity/interim/stopping conclusion. Counts:15relationships,15PASS_2_COMPLETE,0new findings; all47 original exclusions reread in the checker companion artifact.


<!-- Active complete pass2 inventory: raw -->

# Statistical relationship inventory — RAW-score shard, pass 2

Fresh runtime `/root/stat2_raw`, gpt-6.1-sol/high, distinct from pass1 `/root/stat1_raw`. Exact scope: REPORT DOC-005 pp17–18, eTable11, all 21 rows and five method/statistical families. Stable assigned IDs: S601,S602,S603,S604,S605,S606,S607,S608,S609,S610,S611,S612,S613,S614,S615,S616,S617,S618,S619,S620,S621,S622,S623,S624,S625,S626. This unique part is for canonical merge by the coordinator; no other agent's artifacts were changed.

Authority: [DOC-005 p17 eTable11](../../../joi250046supp4_prod_1755300121.15587.pdf#page=17), [p18 notes](../../../joi250046supp4_prod_1755300121.15587.pdf#page=18), and source-method contexts [p15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15), [mainp4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), [mainp11](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11). All assigned rows and both notes were visually reread from exact current-source CPU/PyMuPDF1.26.4 renders. Text/OCR was only a locator.

All 21 rows were revisited after reading the complete ledger, screen and mechanical recheck. Every row's three estimates lie in ordered printed95%CIs; all three raw centers lie inside ordered printed25th/75th-percentile bounds; rounded contrast additivity is feasible. Pain/PGIC negative effects favor the first named arm; PROMIS-function positive effects favor it under exact supplied scoring directions. This says nothing about crude median subtraction or unreported means. All 21 rows have correct .05-level omnibus/pairwise-null pattern: physical3 has no null-excluding CI andP=.212; all others have at least one null-excluding CI andP<.05. An omnibus is not a pairwise test. All raw cells were reread exactly and remain retained under original pass1 transcriptions and C016 recheck; no source/OCR discrepancy was found.

Common limitations for every row: no reported standard error or test statistic; no pairwiseP; exact per-outcome eTable11 n, missingness denominators, variance implementation, confidence reference distribution and exact omnibus-to-CI mapping are unspecified. A diagnostic normal95%CI/common-covariance/two-dimensional Wald family reproduces19 rows; this is empirical same-display support, not inferred author definitions. Detailed precision witnesses and conservative nonreproduction bounds are in `preprocessing/stat2_raw/calculation_record.md`. F-ST2-1001 covers the other2rows. Existing C016 is cross-referenced rather than re-emitted.

| S ID | Exact REPORT p17 row, month | Printed MD95%CIs PT−UC;HC−UC;HC−PT | Printed omnibusP | Source-grounded pass2 facts | Diagnostic same-display check | Pass1 status | Pass2 status |
|---|---|---|---|---|---|---|---|
| S601 | eTable11 Pain Severity 3 months | -0.5 (-0.7, -0.3); -0.5 (-0.7, -0.3); 0.0 (-0.2, 0.2) | <.001 | All three means negative/nonpositive; PT/UC andHC/UC CIs exclude0,HC/PT includes0. Common limits above apply. | Precision-feasible witness; no new finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S602 | eTable11 Pain Severity 6 months | -0.6 (-0.8, -0.3); -0.6 (-0.8, -0.3); -0.0 (-0.2, 0.2) | <.001 | Two negative active/UC means; active comparison displayed−0.0 includes0. Common limits above apply. | Precision-feasible witness; no new finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S603 | eTable11 Pain Severity 12 months | -0.5 (-0.8, -0.3); -0.4 (-0.6, -0.2); 0.1 (-0.1, 0.3) | <.001 | Negative active/UC means with CIs excluding0;HC/PT .1 includes0. Common limits above apply. | Precision-feasible witness; no new finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S604 | eTable11 Pain Intensity 3 months | -0.4 (-0.6, -0.2); -0.3 (-0.5, -0.1); 0.0 (-0.2, 0.2) | <.001 | Two negative active/UC means exclude0;HC/PT0.0 includes0; rounded additivity feasible. Common limits above apply. | Precision-feasible witness; no new finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S605 | eTable11 Pain Intensity 6 months | -0.4 (-0.6, -0.2); -0.4 (-0.6, -0.2); -0.0 (-0.2, 0.2) | <.001 | Both active/UC negative exclude0;HC/PT−0.0 includes0. Common limits above apply. | Precision-feasible witness; no new finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S606 | eTable11 Pain Intensity 12 months | -0.3 (-0.6, -0.1); -0.2 (-0.4, -0.1); 0.1 (-0.1, 0.3) | <.001 | Both active/UC negative exclude0;HC/PT .1 includes0. Common limits above apply. | Precision-feasible witness; no new finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S607 | eTable11 Pain-related Interference 3 months | -0.6 (-0.8, -0.3); -0.6 (-0.8, -0.4); 0.0 (-0.2, 0.2) | <.001 | Both active/UC negative exclude0;HC/PT0.0 includes0. Common limits above apply. | Precision-feasible witness; no new finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S608 | eTable11 Pain-related Interference 6 months | -0.7 (-0.9, -0.4); -0.7 (-0.9, -0.4); -0.0 (-0.3, 0.2) | <.001 | Both active/UC negative exclude0;HC/PT−0.0 includes0; symmetric true CI possible despite printed−.3/.2. Common limits above apply. | Precision-feasible witness; no new finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S609 | eTable11 Pain-related Interference 12 months | -0.6 (-0.9, -0.4); -0.5 (-0.8, -0.3); 0.1 (-0.1, 0.3) | <.001 | Both active/UC negative exclude0;HC/PT .1 includes0. Common limits above apply. | Precision-feasible witness; no new finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S610 | eTable11 Social Role Functioning 3 months | 1.2 (0.3, 2.1); 1.4 (0.7, 2.2); 0.2 (-0.5, 1.0) | 0.001 | Both active/UC positive exclude0;HC/PT .2 includes0; rounded asymmetry of the latter CI feasible. Common limits above apply. | Precision-feasible witness; no new finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S611 | eTable11 Social Role Functioning 6 months | 1.8 (0.9, 2.7); 1.5 (0.8, 2.2); -0.3 (-1.0, 0.4) | <.001 | Both active/UC positive exclude0;HC/PT−.3 includes0. Common limits above apply. | Precision-feasible witness; no new finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S612 | eTable11 Social Role Functioning 12 months | 1.8 (0.9, 2.8); 1.4 (0.5, 2.2); -0.5 (-1.3, 0.3) | <.001 | Both active/UC positive exclude0;HC/PT−.5 includes0; additive true estimates feasible despite rounded point sum. Common limits above apply. | Precision-feasible witness; no new finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S613 | eTable11 Physical Functioning 3 months | 0.6 (-0.2, 1.3); 0.6 (-0.2, 1.3); 0.0 (-0.8, 0.8) | 0.212 | All three CIs contain0; no pairwise superiority claimed; omnibus.212 agrees at.05. Common limits above apply. | Precision-feasible witness; no new finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S614 | eTable11 Physical Functioning 6 months | 1.1 (0.3, 1.9); 0.4 (-0.3, 1.1); -0.6 (-1.4, 0.1) | 0.005 | PT/UC positive excludes0;HC/UC andHC/PT include0; omnibus.005 agrees at.05 but fails same-display diagnostic; F-ST2-1001. Common limits above apply. | Conservative bound does not reproduce printedP; F-ST2-1001. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S615 | eTable11 Physical Functioning 12 months | 1.2 (0.4, 2.0); 0.9 (0.0, 1.8); -0.3 (-1.2, 0.6) | 0.001 | PT/UC positive excludes0;HC/UC endpoint0.0 andHC/PT include0; omnibus.001 agrees at.05 but fails same-display diagnostic; F-ST2-1001. Common limits above apply. | Conservative bound does not reproduce printedP; F-ST2-1001. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S616 | eTable11 PGIC–Pain 3 months | -0.8 (-0.9, -0.6); -0.9 (-1.0, -0.8); -0.2 (-0.3, -0.0) | <.001 | Negative active/UC contrasts; HC/PT−.2 upper−0.0 is a rounded null-adjacent endpoint, with no pairwiseP to conflict; raw HC3 wide bounds retained under C016. Common limits above apply. | Precision-feasible witness; no new finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S617 | eTable11 PGIC–Pain 6 months | -0.7 (-0.8, -0.5); -0.7 (-0.8, -0.5); -0.0 (-0.2, 0.1) | <.001 | Both active/UC negative exclude0;HC/PT−0.0 includes0; rawPT2.8 median-identity issue alreadyC016. Common limits above apply. | Precision-feasible witness; no new finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S618 | eTable11 PGIC–Pain 12 months | -0.7 (-0.8, -0.5); -0.6 (-0.7, -0.4); 0.1 (-0.1, 0.2) | <.001 | Both active/UC negative exclude0;HC/PT .1 includes0; rawPT2.8/UC2.2 issue alreadyC016. Common limits above apply. | Precision-feasible witness; no new finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S619 | eTable11 PGIC–General 3 months | -0.8 (-0.9, -0.6); -1.1 (-1.2, -1.0); -0.3 (-0.5, -0.2) | <.001 | All three negative CIs exclude0; rawPT2.7 andHC3 wide bounds alreadyC016. Common limits above apply. | Precision-feasible witness; no new finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S620 | eTable11 PGIC–General 6 months | -0.6 (-0.7, -0.4); -0.8 (-0.9, -0.6); -0.2 (-0.3, -0.0) | <.001 | Negative active/UC CIs exclude0;HC/PT−.2 upper−0.0 null-adjacent, no pairwiseP; rawUC1.8 issue alreadyC016. Common limits above apply. | Precision-feasible witness; no new finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S621 | eTable11 PGIC–General 12 months | -0.6 (-0.8, -0.4); -0.7 (-0.8, -0.5); -0.1 (-0.2, 0.1) | <.001 | Negative active/UC CIs exclude0;HC/PT−.1 includes0; remaining fractional raw medians below precision threshold. Common limits above apply. | Precision-feasible witness; no new finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |

| S ID | Exact method/relationship source scope | Source-grounded pass2 facts and ledger/recheck implications | Missing definitions / limit | Pass1 status | Pass2 status |
|---|---|---|---|---|---|
| S622 | REPORT DOC005pp15,17–18;DOC001p4 | P15 explicitly no adjustment, weighting or imputation; p18 linearGEE for each continuous outcome. Main describes working independence, robustsandwich and clustering at highest person/coach level; no supplied text says eTable11 violates those design structures. Weighted/imputed adjusted and restricted-model candidatesC005–C007/C011–C014 are not numerically matched to this unadjusted display. | Exact per-outcome sample sizes, missing-data denominators and eTable11 working/variance implementation not specified; absence alone is not emitted. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S623 | REPORT DOC005pp2,15,17–18;DOC001p11f–i | Pain item averages and transformed PROMIS T scores support fractional summaries. PGIC is one categorical item1–7. Mean-narrative/median-quartile-header and five ordinary-median grid discrepancies alreadyC016; recheck confirms S_W/statistical_results, main scale source corroboration only. Other fractional centers have gap≤.05 and excluded once. | Exact raw-arm central statistic and bound convention; empirical/interpolated/weighted/set-valued median definition and mixed-summary intent remain C016 human question. No alternative is assigned as established. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S624 | REPORT DOC005p17 all 21 rows,p15intro,p18note | Model contrast addition is precision-feasible for every row. Under printed raw-median headings, subtraction is not a reproducing GEE mean method. Alternative raw-arm permutation UC/PT/HC fits the21 contrast triples but does not establish arm assignment; median-vs-mean premise remains absent. C016 retains unresolved raw-summary identity. | No equality between raw medians and fitted means, actual means or source arm-order amendment supplied. Conditional permutation excluded once. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S625 | REPORT DOC005p17 all 21omnibusPs,p18note;p15replication;DOC001p11Walddefinition | Reread all original47 exclusions. OriginalRAWphysical6/12 exclusion reopened: same-table diagnostic reproduces19 rows, yet conservative rounded feasible-region bounds requireP≥.01386977/.00215371 versus.005/.001; F-ST2-1001. All .05-level null patterns reconcile; no pairwiseP invented. | Diagnostic normal95%CI, common covariance andchi-square2 mapping are explicitly assumptions tested by same-display reproduction, not author definitions. Actual CI critical value, omnibus distribution/df, variance and estimand mapping remain exact human questions; alternatives retained. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S626 | REPORT DOC001p4,p11notec;DOC005pp15,17–18 | Main Wald/FisherLSD rule permits between-group comparisons only if omnibusP<.05. No eTable11 physical3 superiority claim violates its.212 gate; other row gates are below.05. No noninferiority/equivalence/interim/stopping margin or decision appears. Three-month primary-timepoint note does not change endpoint status. Sample-size simulation exclusions reread, but no same-display sample-size reproducing method established; assigned raw scope contains no sample-size calculation. | No unrounded boundaryP or new margin/test imported. No sample-size simulation specification or output was added to raw scope. | PASS_1_COMPLETE | PASS_2_COMPLETE |

Counts:26/26 S IDs explicitly PASS_2_COMPLETE;21 row triples/63 modeltuples,63 raw summaries,21omnibusPs and5method families. New finding1; excluded observations3; original exclusions47 reread,46retained and1reopened. Full checker findings, excluded table and47-row rereview record: `checkers/parts/stat2_raw.md`. No scientific coverage gap in assigned pages. Supplied sources and every existing artifact were preserved.
