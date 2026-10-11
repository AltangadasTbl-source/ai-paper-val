# Statistical pass 1 — REPORT checker

Runtime ID: root/statistical_pass_1; fresh gpt-6.1-sol/high. Exact scope: all DOC-001 REPORT pp.1–10 and DOC-003 REPORT pp.1–17 inferential/method relationships; DOC-004 p.1 no applicable inferential result. All 105 S records S001–S105 are PASS_1_COMPLETE in statistics/parts/report_relationship_inventory.md. PLAN-only scope is disjoint and belongs to the separate fresh PLAN shard. Scope, contract and tooling were read completely. Findings below are observations for independent inclusion screening, not candidates or adjudications. No expected finding count was used.

All source evidence below is supplied REPORT material. Main PDF pp.5–8 and supplement p.5 were visually inspected using source-linked, unchanged reusable PNGs; current-source-matched native/layout text located methods/code. Direct PDF remains final authority at mechanical recheck. Exact raw participant-by-period measurements, paired availability subsets, subgroup inferential degrees of freedom and posterior draws are absent. CPU, historical rendering versions unrecorded; no web, unapproved Python, prior audit conclusions or preferred analysis used.

Numerical calculations use ordinary arithmetic and labeled t-distribution diagnostics. For a stated dependent t test, the mean-difference CI has half-width h=t(.975, df)*SE; statistic t=estimate/SE and two-sided P=2 Pr(T_df≥abs(t)). Where N=27 is used, df=26 is derived from a paired t on 27 complete participant pairs, not inferred from mixed-model convention. Sensitivity to 31 sets/df 30 is explicitly diagnostic, not a claim that sets were the analysis units. Numerical t integrals were evaluated in JavaScript in the tool orchestration cell, not by Python scientific orchestration.

## Findings

### F-ST1-001

**Title:** First-attempt handgrip placebo mean is outside its printed interval and endpoints descend.

**Relationships:** S071. **Locations and roles:** REPORT DOC-001 [PDF p.7 Table2, handgrip action myotonia First attempt, Change Placebo Period](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=7). REPORT DOC-001 p.8 footnotes a/h describes secondary dependent t tests and relaxation-time quantity.

**Printed values:** Placebo change 0.46 seconds, 95% CI −0.30 to−1.23; baseline 3.33(SD 5.00), mexiletine −2.39(−4.22 to−0.55), effect −2.85(−5.28 to−0.42), P=.02.

**Rule and calculation:** Ordered limits require L≤U: −0.30>−1.23. Even sorting gives [−1.23,−0.30], excluding mean +.46. Half-unit intervals for mean[.455,.465], first limit[−.305,−.295], second limit[−1.235,−1.225] cannot restore order/containment; smallest point-to-upper gap=.455−(−.295)=.750. Relative gap=.750/.46=1.6304. Route A category 1 does not permit a rounding exclusion.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 1.
**Affected result or extracted value:** Placebo first-attempt handgrip mean change and its 95% CI.
**Why context does not resolve it:** Point outside interval is an always-register category; reversing endpoint order alone still excludes the point.
**Alternatives / missing definition:** A sign on 1.23 may differ from the intended bound; this is a source-grounded reconstruction possibility, not a correction. No distinct interval estimand is stated.
**Human question:** Which 95% CI belongs to the printed placebo mean change+.46 seconds?

### F-ST1-002

**Title:** Mean Timed Up&Go placebo change exceeds its printed upper confidence limit.

**Relationships:** S082. **Locations and roles:** REPORT DOC-001 [p.7 Table2, Timed Up&Go Mean, Change Placebo Period](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=7); REPORT p.8 footnotes a/i.

**Printed values:** Placebo +.07 seconds(95% CI −.67 to+.01), mexiletine −1.05(−1.48 to−.62), effect −1.12(−2.07 to−.18), P=.02.
**Rule and calculation:** .07>.01, so point lies outside 95% CI. Mean rounding interval[.065,.075] and upper-bound interval[.005,.015] leave gap≥.050, relative gap=.050/.07=.7143. Ordered limits themselves reconcile; containment does not. The display-precision rule does not screen category 1.
**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 1.
**Affected result or extracted value:** Placebo mean Timed Up&Go change and 95% CI.
**Why context does not resolve it:** Printed point outside interval is always-register even though an intended symmetric endpoint might be reconstructed.
**Alternatives / missing definition:** A different upper limit or a differently attributed mean is possible; source specifies neither.
**Human question:** Which 95% CI is associated with the placebo +.07 second mean change?

### F-ST1-003

**Title:** SCN4A fifth-attempt handgrip interval includes zero but its P value is significant.

**Relationships:** S074. **Locations and roles:** REPORT DOC-001 [p.7 Table2, Handgrip action myotonia Fifth attempt SCN4A](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=7), [p.8 narrative repeated effect/CI and footnotes](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=8); REPORT p.4 two-sided P and significance P<.05.
**Printed values:** Effect −1.96 seconds, 95% CI −3.41 to+.51, P=.009; narrative repeats−1.96(−3.41 to+.51), separate interaction P=.04.
**Rule and calculation:** −3.41<0<+.51 while .009<.05. Every half-unit bound leaves CI crossing 0; P remains[.0085,.0095]. No covariance, df or choice between subgroup t/mixed inference is required. The printed interval midpoint−1.45 also differs from−1.96; this corroborates the reading but is not a second issue.
**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 1.
**Affected result or extracted value:** Within-SCN4A fifth-attempt handgrip treatment effect and significance.
**Why context does not resolve it:** Interval-versus-P conflict is always-register. The interaction P is a separate row and cannot substitute for subgroup P.
**Alternatives / missing definition:** Upper endpoint sign could differ; P and CI could come from distinct analyses. Neither definition is supplied for this row; a distinct-analysis alternative does not remove category 1.
**Human question:** Which interval and which two-sided test belong to the SCN4A effect −1.96 seconds?

### F-ST1-004

**Title:** SCN4A fifth-attempt transient-paresis interval includes zero but P=.02.

**Relationships:** S092. **Locations and roles:** REPORT DOC-001 [p.7 Table2, transient paresis Fifth attempt SCN4A](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=7); [p.6 narrative repeats13.71(−1.96 to25.47)](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=6); REPORT p.4 significance and p.8 method/scale footnotes.
**Printed values:** Effect 13.71 percentage points, 95% CI −1.96 to 25.47, P=.02; interaction P<.001 is a distinct row.
**Rule and calculation:** CI contains 0 but .02<.05. Rounding limits remain negative/positive and P[.015,.025] remains significant. CI midpoint 11.755 is not 13.71; df is not assumed for the primary contradiction.
**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 1.
**Affected result or extracted value:** SCN4A fifth-attempt transient-paresis effect, 95% CI and significance.
**Why context does not resolve it:** Always-register interval/P conflict; interaction does not determine the within-subgroup test.
**Alternatives / missing definition:** Lower endpoint sign could differ, or CI/P may be from distinct analyses; source does not define that mapping.
**Human question:** Which CI and P represent the SCN4A 13.71 percentage-point effect?

### F-ST1-005

**Title:** SF-36 mental treatment CI does not yield printed P=.001 under stated paired t inference.

**Relationships:** S069. **Locations and roles:** REPORT DOC-001 [p.7 Table2 SF-36 Mental component](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=7); REPORT [p.3 Frequentist Analysis](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=3), p.4 two-sided testing and [p.8 footnote a](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=8).
**Printed values:** Effect 6.78, 95% CI 1.64–11.92, P=.001, total N 27. Methods say dependent t tests calculated total-group mean effects, significance and confidence intervals; footnote a contrasts IVR mixed model with dependent t tests for other measures.
**Rule and calculation:** h=(11.92−1.64)/2=5.14. Under stated paired t on 27 pairs, df 26, tcrit 2.055529, SE 5.14/2.055529=2.500572, t 6.78/2.500572=2.711379, two-sided P=.0117149. Allowing half-unit rounding of all inputs yields diagnostic P[.0115883,.0118425], disjoint from printed P[.0005,.0015]. Minimum gap=.0100883 relative to .001=10.0883. Category 1 is never screened as rounding. Diagnostic df 30 for 31 sets gives P=.0114515; large-df diagnostic P≈.00973 remains distinct. Other total rows reproduce the t relation, e.g. peak-force Mean P≈.008863 rounds .009 and INQoL P≈.009789 rounds .01.
**Focus area:** B, C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 1.
**Affected result or extracted value:** SF-36 mental treatment P, statistical evidence and CI/test identity.
**Why context does not resolve it:** Printed P cannot belong to the printed effect/CI under the analysis stated for this outcome; always-register category 1.
**Alternatives / missing definition:** A distinct test or interval analysis, different linked effect, or unreported paired-subset mapping is possible. Missing exact analysis mapping/df must be named rather than inferred.
**Human question:** Which analysis and associated CI generated P=.001 for the 6.78-point mental-component effect?

### F-ST1-006

**Title:** Needle-EMG effect/CI does not yield P<.001 under stated paired t inference.

**Relationships:** S098. **Locations and roles:** REPORT DOC-001 [p.8 Table2 continuation, needle EMG grading and footnotes a/m](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=8); REPORT p.3 dependent-t methods, p.4 two-sided testing.
**Printed values:** Placebo 2.52(SD.89), mexiletine 1.85(SD 1.13), effect .67, 95% CI.23–1.11, P<.001, total N 27.
**Rule and calculation:** Difference 2.52−1.85=.67; h=.44. Paired-t on 27 pairs, df 26, SE.44/2.055529=.2140568, t=.67/.2140568=3.130011, two-sided P=.00428275. Half-unit inputs yield diagnostic P[.00369665,.00494118], entirely above .001. Gap to asserted upper bound .001≥.00269665. Since P is an inequality there is no unique printed P denominator for a relative discrepancy; normalized gap to .001=2.69665. Diagnostic df 30 gives P=.0040810; large-df diagnostic≈.002844 also exceeds .001.
**Focus area:** B, C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 1.
**Affected result or extracted value:** EMG-grading treatment P and compatibility with its reported 95% CI.
**Why context does not resolve it:** Always-register test / interval numerical incompatibility even though both suggest a positive treatment effect at .05.
**Alternatives / missing definition:** A distinct test generating P<.001, interval convention, or effect mapping might apply; none is stated for this row.
**Human question:** Which two-sided analysis generated P<.001 and which associated CI belongs to the .67-grade effect?

### F-ST1-007

**Title:** First-attempt eyelid interval excludes zero but printed P=.05 fails the stated strict significance rule.

**Relationships:** S077. **Locations and roles:** REPORT DOC-001 [p.7 Table2 Eyelid closure First attempt](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=7); REPORT p.4 explicitly P<.05 and two-sided tests, p.8 footnotes.
**Printed values:** Effect −4.25 seconds, 95% CI −8.45 to−.05, P=.05.
**Rule and calculation:** Upper bound−.05 excludes 0; printed .05 is not<.05. The upper bound half-unit interval[−.055,−.045] still excludes 0. P rounding interval[.045,.055] includes latent values on both sides of .05, but scope category 1 expressly excludes display-precision screening. A paired-t diagnostic with N 27 gives P=.0475236 and provides a plausible rounded P alternative.
**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 1.
**Affected result or extracted value:** First-attempt eyelid effect's significance at the stated strict .05 rule.
**Why context does not resolve it:** The scope requires registering a printed interval/test conflict irrespective of a rounding interpretation.
**Alternatives / missing definition:** Unrounded P≈.0475 would reconcile the interval and underlying strict significance decision; the report prints only .05.
**Human question:** What unrounded P and significance classification belong to this 95% CI?

### F-ST1-008

**Title:** Lower Table2 contrast header reverses the direction represented by period changes and effects.

**Relationships:** S068–S082,S086–S092,S094–S096; repeated pattern consolidated. **Locations and roles:** REPORT DOC-001 [p.7 Table2 lower-section header and non-IVR outcome rows](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=7); REPORT [p.8 footnotes d,f–l](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=8).
**Printed values:** Effect header “Placebo-Mexiletine”. SF-36 physical placebo +1.04, mexiletine +8.66, effect +7.81; INQoL placebo −7.22, mexiletine −21.44, effect −14.22; handgrip First placebo +.46, mexiletine −2.39, effect −2.85. The majority of subsequent non-IVR rows follow mexiletine-minus-placebo sign, including handgrip Fifth/Mean, eyelid First/Fifth/Mean, Timed Up&Go First/Fifth/Mean, peak force First/Fifth/Mean, transient paresis First/Fifth/Mean and both genotype rows for transient Fifth/Mean. Footnote d says all significant findings favor mexiletine; higher SF-36/peak force and lower INQoL/times/paresis are beneficial by supplied scale definitions.
**Rule and calculation:** Header subtraction SF-36 physical 1.04−8.66=−7.62, versus printed+7.81; INQoL−7.22−(−21.44)=+14.22, versus−14.22; handgrip First .46−(−2.39)=+2.85, versus−2.85. INQoL recomputed half-unit interval[14.21, 14.23], printed[−14.225,−14.215], gap 28.425/14.22=1.9989. Header therefore changes reference/direction rather than only typography. Same opposite-sign pattern across named rows is one issue; F-ST1-009 separately concerns magnitude/paired subset after allowing the observed operative M−P direction.
**Focus area:** B, C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 2.
**Affected result or extracted value:** Sign and reference orientation of non-IVR effect estimates for extraction/synthesis.
**Why context does not resolve it:** Numeric-sign/reference reversal falls in always-register category 2 even though source scale/narrative suggests benefit.
**Alternatives / missing definition:** Effects may use mexiletine-minus-placebo while header names the reverse; outcome-specific changes or a different contrast definition could apply but are not stated.
**Human question:** Which subtraction/reference group does each lower-section treatment-effect column represent?

### F-ST1-009

**Title:** Several non-IVR treatment effects do not reproduce the period mean difference under the stated dependent-t method.

**Relationships:** S073,S083,S085,S086,S087,S088,S089,S090,S092,S094,S096. **Locations and roles:** REPORT DOC-001 [p.7 Table2 exact named rows below](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=7); REPORT p.3 dependent-t methods, p.4 all available data and missing outcomes,[p.8 footnote a](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=8). All locations REPORT.
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

### F-ST1-010

**Title:** Baseline “Other” antimyotonic-medication P does not reproduce the binary comparison that matches adjacent rows.

**Relationships:** S011. **Locations and roles:** REPORT DOC-001 [p.5 Table1 Men and Pretrial medication rows with footnote a](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=5). All REPORT.
**Printed values:** CLCN1 N 16,SCN4A N 11; Other 7(44%) versus 5(46%), P=.62; adjacent Men 13 versus 7, P=.39; Mexiletine 2 versus 0, P=.50. Footnotea identifies Mann–Whitney U.
**Rule and calculation:** A binary rank comparison with tied 0/1 values has U centered at n1*n2/2=88, observed U=88+(11*7−16*5)/2=86.5. Exact two-sided permutation probability of abs(U−88) at least 1.5 is 1.000: every possible allocation of 12 yes values is at least that far from 88. The same exact absolute-U permutation tail gives .391304 for Men and .498575 for Mexiletine, reproducing .39/.50. Tie-adjusted asymptotic diagnostic var(U)=16*11*12*15/(4*26)=304.6154,|z|1.5/sqrt(var)=.08594, normal P≈.9315; continuity adjustment increases P. Integer counts are exact; exact recomputed P=1, printed P interval[.615,.625], gap.375/.62=.60484, above 5%.
**Focus area:** B, C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 4.
**Affected result or extracted value:** Baseline Other-medication subgroup comparison P and which variable was tested.
**Why context does not resolve it:** A reproducing exact binary rank method matches adjacent rows yet does not reproduce this row; unstated tested variable is the human question.
**Alternatives / missing definition:** P may test drug categories or doses instead of binary Other-medication use; a different tested variable or sample could be intended. Neither is labeled in the display.
**Human question:** Which variable, sample and Mann–Whitney procedure generated P=.62 for 7/16 versus 5/11?

### F-ST1-011

**Title:** Primary patient 21 stiffness credible interval differs between Figure2 and eTable3.

**Relationships:** S051,S099. **Locations and roles:** REPORT DOC-001 [p.5 Figure2 patient21](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=5); REPORT DOC-003 [p.5 eTable3 patient21](../../../../joi180136supp2_prod.pdf#page=5). All REPORT.
**Printed/graphical values:** eTable3 SCN4A patient 21 mean 4.41, 95% CrI 3.80–5.0, posterior 100%, one interim. Figure2 patient 21 marker approximately 4.4, whisker lower approximately 3.3, upper approximately 5.5; caption says mean and 95% CrI for each patient and cross-references eTable3.
**Rule and calculation:** Source graph coordinates are unprinted; conservative visual uncertainty±.1 gives lower[3.2, 3.4], upper[5.4, 5.6]. eTable lower half-unit[3.795, 3.805], upper printed one-decimal[4.95, 5.05]. Minimum gaps lower 3.795−3.4=.395, relative .395/3.80=.10395; upper 5.4−5.05=.35, relative .35/5.0=.07. Both exceed 5% even under conservative visual intervals. Mean agrees; interval does not. This is a graphical comparison, not a digitized exact estimate.
**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_C. **Qualifying route:** Route B.
**Affected result or extracted value:** Patient 21 primary individual stiffness 95% credible interval.
**Why context does not resolve it:** B1: primary result interval; B2: caption links displays to the same patient/result without defining distinct analyses; B3: a reader could extract different individual uncertainty for the primary outcome.
**Alternatives / missing definition:** eTable 3 is individual interim analysis while Figure 2 might use a hierarchical individual estimate; group caption states genotypes informed by all patients, but does not define this distinction for individual markers. Distinct model/time point could reconcile values if confirmed. Exact Figure 2 underlying bounds/analysis not supplied.
**Human question:** Does Figure 2 patient 21 use the same individual posterior as eTable 3, and which 95% CrI should be extracted?

### F-ST1-012

**Title:** SF-36 physical placebo change/CI is not centered under the interval method reproducing other period rows.

**Relationships:** S068. **Locations and roles:** REPORT DOC-001 [p.7 Table2,SF-36 Physical,ChangePlaceboPeriod](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=7); REPORT p.3 secondary analysis, p.8 footnote a.
**Printed values:** Placebo change 1.04, 95% CI −.60 to 2.96. Other periods: SF-36 mental placebo −1.85(−4.81, 1.11); SF-36 physical mexiletine 8.66(5.94, 11.38); eyelid First placebo −.74(−2.49, 1.01).
**Rule and calculation:** Symmetric mean intervals reproduce the other named rows: respective endpoint midpoints−1.85, 8.66,−.74. Physical placebo midpoint(−.60+2.96)/2=1.18. Rounding midpoint interval[1.175, 1.185], printed mean[1.035, 1.045], gap.130/1.04=.125, above 5%. The mean is contained; issue is reproduction under the same-display interval method, not point containment.
**Focus area:** B, C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Qualifying route:** Route A, category 4.
**Affected result or extracted value:** SF-36 physical placebo change mean and 95% CI analysis identity.
**Why context does not resolve it:** Category 4 allows a reproducing method that matches other rows of the display; an unstated interval convention is a human question.
**Alternatives / missing definition:** An asymmetric interval procedure or different mean/interval subset could apply; source dependent t test description clearly covers mean effects but does not separately name the period CI engine. No asymmetric method is asserted.
**Human question:** Which method and sample generated−.60 to 2.96, and does it belong to the printed 1.04 placebo mean?

## Excluded observations

These are apparent issues deliberately not emitted; reconciling checks are in S records and are not exclusions. Each row has exactly one reason code.

| Location | Observation | Reason code |
|---|---|---|
| DOC-001 pp.1,4,7 Bayesian 3.06 versus frequentist 3.12 and arm-summary differences | Distinct labeled hierarchical/mixed analyses need not equal crude estimates or each other; no conflicting shared estimand is claimed. | MODEL_VERSUS_CRUDE |
| DOC-001 p.5 Figure2 CLCN1 group marker versus p.4 printed 3.84/5.16 | Visual coordinates about 3.55/4.8 with ±.1–.2 uncertainty leave remaining relative gaps at most .05; unprinted numbers are not treated as exact. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 p.6 Figure3C terminal SCN4A about 88% versus text 93% | Conservative visual interval [87,89] and text [92.5,93.5] leave gap 3.5/93=.0376; the precision threshold screens it. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 p.5 eTable3 patient11; main p.4 nonresponse | Posterior 38% lies outside the below-20% rule, but the footnote explicitly explains zero stiffness in both arms, prior influence and the decision to stop and discontinue. The exception is disclosed. | CONTEXT_RESOLVES |
| DOC-003 p.5 eTable3 patients8,20 | Printed 80% versus strict above-80% can represent unrounded 80.0–80.5% above the criterion; no exact boundary violation is reproduced. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 pp.11–14 eMethods2/3 glossary | Swapped mex/plac descriptions and the CLCN1-difference glossary's SCN4A name are immediately resolved by explicit observation loops, effect equations and genotype code. No result-attribution ambiguity remains. | TERMINOLOGY_OR_WORDING |
| DOC-003 pp.15–17 eMethods4 pointers | Numbered individual/group references are offset relative to actual section titles, but named individual/group model roles and code identify the analysis at once. No new reported-number conflict is present. | CONTEXT_RESOLVES |
| DOC-003 p.10 eMethods1 loops1:30 | Actual missing/shorter observation-vector handling is not provided. Without a conflicting printed result, an unreported implementation detail alone is not a finding. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 pp.15–17 simulation inputs | Full random-baseline/variance-generating distributions and posterior replicates are absent. Numeric power/bias counts reconcile, and missing inputs for rerunning are not independent findings. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 p.7 Table2 SF-36 mental Mexiletine period | Mean4.77 versus interval midpoint4.575 leaves gap.190/4.77=.03983, at most .05; screened for precision and not an F-ST1-012 location. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 p.7 Table2 other lower-section near-differences | SF-36 physical effect7.81 versus M−P7.62, mental6.78 versus6.62, CLCN1 transient Fifth−23.85 versus−23.06, CLCN1 transient Mean−12.37 versus−12.79 and tiny relaxation Fifth−.01 versus−.02 all have overlap or remaining relative gap at most .05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 p.7 Table2 Timed Up&Go Fifth / dynamometry relaxation Mean P diagnostics | Central paired-t diagnostics .0543 versus printed .06 and .8779 versus .91 can reconcile under half-unit estimate/CI rounding; neither has a CI/P null-classification conflict. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 p.5 Figure2 patient11 | No visibly wide whisker is not an exact printed zero-width CI. The eTable3 footnoted zero data and prior-based interval allow different presentation; absence alone cannot reproduce a quantitative CI-endpoint comparison. | CONDITIONAL_OR_UNREPORTED |

## Completion and limitations

REPORT pass1: 105 relationships, 12 findings, 13 excluded-observation rows. Complete assigned inferential/method scope includes all 14 Table1 rows, 38 Table2 outcome/interaction rows, 27 individual graph markers, all three Figure3 panels, all seven main method records, all seven results-supplement method/decision relationships and all matching report narratives. Source units without an applicable statistical result were inspected; none were omitted.

Exact raw data, posterior draws, period-CI engine, paired available-case subsets, repeated-set weights and subgroup inferential degrees of freedom are absent. Diagnostic calculations do not substitute for unreported methods. These limitations do not remove printed containment, interval/P, contrast or category4 reproduction findings. Independent inclusion screen and evidence recheck remain required. Canonical shard merge must preserve all finding and S IDs. Every candidate, if registered later, remains Pending Human Adjudication.
