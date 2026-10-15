# Statistical Relationship Inventory — Main-Paper Pass 1

Runtime agent: /root/stat1_main. Model: gpt-6.1-sol. Reasoning effort: high. Fresh pass-1 primary-main shard only. Scope: DOC-001 REPORT, physical PDF pages1–14; fresh map MAIN001–MAIN116. Sources preserved; no prior review conclusions used. All110 records below are PASS_1_COMPLETE. Statistical pass2 must use a distinct fresh agent.

Methods and inferential outcomes are disjoint records; each outcome contributes three families (group estimates, between-group estimates/test, derived estimates). Every triple lists every tuple in fixed PT/HC/UC or PT–UC/HC–UC/HC–PT order. Total270 estimate–95%CI tuples,30 omnibus tests,27 NNTs,63 SMDs. The outcome records explicitly cover all three times and all contrasts. No result tuple is sampled.

Full exact printed input transcription and source page links: [fresh main map](../../extraction/main_quantitative_evidence.md). Direct pages 9–11 visually inspected; page 7 narrative directly inspected; fresh native PDF text used as locator for all 14 pages. Inferential categories absent from main are recorded in S020.

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


