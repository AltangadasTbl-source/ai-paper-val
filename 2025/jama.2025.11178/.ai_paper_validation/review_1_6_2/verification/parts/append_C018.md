# Appended-candidate mechanical evidence recheck

Fresh runtime: /root/recheck_c018; model gpt-6.1-sol; reasoning effort high. Assigned stable ID: C018 only. The complete quantitative scope and review contract were read. Exact current-source render inspection, independently transcribed source tuples and separate JavaScript calculations were used; no web, legacy conclusions, source modification or new Python helper was used.

Source scope: DOC-005 physical PDF pages 15,17,18; DOC-001 physical PDF pages 4,11. Five distinct source pages visually inspected, below the 32-page shard bound. Existing current-run renders use pinned PyMuPDF1.26.4, CPU, as recorded in tooling_record.md. No new extraction/OCR/render derivative was required. Scientific text read remained below 200000 characters.

## C018 — Physical-function omnibus P values and contrast intervals
**Candidate statement:** The eTable 11 physical-function six- and twelve-month omnibus P values do not reconcile with their three mean-difference/95%CI tuples under the normal-CI/common-covariance/chi-square2 Wald reconstruction that is precision-feasible for the other 19 rows of that display.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 11 omnibus P values versus REPORT results supplement eTable 11 mean-difference/95%CI contrasts and method context. Main article REPORT methods are corroboration only.

**Evidence state:** reproduced

**Finding IDs:** F-ST2-1001

**Qualifying route:** Route A, category 1

### Exact-source location and transcription facts

| Exact supplied-source location | Location found | Source value/text matched | Comparator matched | Content role |
|---|---|---|---|---|
| [Results supplement PDF p17, eTable 11 Physical Functioning 6 months](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=17) | Yes; every affected contrast and P cell visually read | PT−UC 1.1 (0.3,1.9); HC−UC 0.4 (−0.3,1.1); HC−PT −0.6 (−1.4,0.1) | Omnibus P=0.005 in the same six-month row | REPORT |
| [Results supplement PDF p17, eTable 11 Physical Functioning 12 months](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=17) | Yes; every affected contrast and P cell visually read | PT−UC 1.2 (0.4,2.0); HC−UC 0.9 (0.0,1.8); HC−PT −0.3 (−1.2,0.6) | Omnibus P=0.001 in the same twelve-month row | REPORT |
| [Results supplement PDF p17, all other 19 eTable 11 outcome/time rows](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=17) | Yes; all 57 corroborating mean-difference/CI tuples and 19 Ps visually read | Complete transcription appears below | All 19 feasible witnesses independently recalculated against their own exact printed tuples, not against the target rows | REPORT, same-display corroboration |
| [Results supplement PDF p18, eTable 11 note b](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=18) | Yes | Unadjusted between-group mean differences and 95% confidence intervals were calculated with a linear regression model fit using generalized estimating equations for each continuous outcome | Matches the inferential-column identity of eTable 11; no explicit normal critical value, covariance, omnibus distribution or df supplied | REPORT |
| [Results supplement PDF p15, Additional Unadjusted Data and Analyses](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=15) | Yes | Tables 2 and 3 replicated with no adjustment, weighting or imputation; eTable 10 gives unadjusted mean change and eTable 11 gives unadjusted mean secondary outcomes | Supplies broad replicated-analysis context, not an explicit statement that every inferential implementation is identical | REPORT |
| [Main article PDF p11, Table 3 note c](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11) | Yes | Omnibus P value is the Wald test assessing any difference among the three groups; between-group comparisons follow omnibus P<.05 using the least significant difference approach | Corroborates a three-group Wald family for the main adjusted display; not an exact supplement df/covariance declaration | REPORT, corroboration only |
| [Main article PDF p4, Statistical Analysis](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4) | Yes | GEE with working-independence correlation and robust sandwich standard errors; linear GEE for continuous secondary outcomes; all tests two-sided with alpha=.05 | Corroborates the broad fitted family and confidence/testing context; exact eTable 11 inferential distributions remain absent | REPORT, corroboration only |

The rendered p17 heading is unadjusted between-group mean differences (95%CI), with PT vs UC, HC vs UC and HC vs PT columns and a separately named omnibus P column. No pairwise P value is printed. The comparison does not equate raw medians with fitted means, and does not equate a single pairwise null with the omnibus null.

### Independent source transcription, including every corroborating row

All entries below were reread visually from the exact supplied-source p17 render. The 19 remaining rows support a reproducible numerical family; only physical six/twelve months are affected locations of this candidate.

| Relationship | Outcome/time | PT−UC estimate (95%CI) | HC−UC estimate (95%CI) | HC−PT estimate (95%CI) | Omnibus P |
|---|---|---|---|---|---|
| S601 | Pain severity 3 months | -0.5 (-0.7, -0.3) | -0.5 (-0.7, -0.3) | 0 (-0.2, 0.2) | <.001 |
| S602 | Pain severity 6 months | -0.6 (-0.8, -0.3) | -0.6 (-0.8, -0.3) | 0 (-0.2, 0.2) | <.001 |
| S603 | Pain severity 12 months | -0.5 (-0.8, -0.3) | -0.4 (-0.6, -0.2) | 0.1 (-0.1, 0.3) | <.001 |
| S604 | Pain intensity 3 months | -0.4 (-0.6, -0.2) | -0.3 (-0.5, -0.1) | 0 (-0.2, 0.2) | <.001 |
| S605 | Pain intensity 6 months | -0.4 (-0.6, -0.2) | -0.4 (-0.6, -0.2) | 0 (-0.2, 0.2) | <.001 |
| S606 | Pain intensity 12 months | -0.3 (-0.6, -0.1) | -0.2 (-0.4, -0.1) | 0.1 (-0.1, 0.3) | <.001 |
| S607 | Pain-related interference 3 months | -0.6 (-0.8, -0.3) | -0.6 (-0.8, -0.4) | 0 (-0.2, 0.2) | <.001 |
| S608 | Pain-related interference 6 months | -0.7 (-0.9, -0.4) | -0.7 (-0.9, -0.4) | 0 (-0.3, 0.2) | <.001 |
| S609 | Pain-related interference 12 months | -0.6 (-0.9, -0.4) | -0.5 (-0.8, -0.3) | 0.1 (-0.1, 0.3) | <.001 |
| S610 | Social functioning 3 months | 1.2 (0.3, 2.1) | 1.4 (0.7, 2.2) | 0.2 (-0.5, 1) | 0.001 |
| S611 | Social functioning 6 months | 1.8 (0.9, 2.7) | 1.5 (0.8, 2.2) | -0.3 (-1, 0.4) | <.001 |
| S612 | Social functioning 12 months | 1.8 (0.9, 2.8) | 1.4 (0.5, 2.2) | -0.5 (-1.3, 0.3) | <.001 |
| S613 | Physical functioning 3 months | 0.6 (-0.2, 1.3) | 0.6 (-0.2, 1.3) | 0 (-0.8, 0.8) | 0.212 |
| S614 | Physical functioning 6 months | 1.1 (0.3, 1.9) | 0.4 (-0.3, 1.1) | -0.6 (-1.4, 0.1) | 0.005 |
| S615 | Physical functioning 12 months | 1.2 (0.4, 2) | 0.9 (0, 1.8) | -0.3 (-1.2, 0.6) | 0.001 |
| S616 | PGIC pain 3 months | -0.8 (-0.9, -0.6) | -0.9 (-1, -0.8) | -0.2 (-0.3, 0) | <.001 |
| S617 | PGIC pain 6 months | -0.7 (-0.8, -0.5) | -0.7 (-0.8, -0.5) | 0 (-0.2, 0.1) | <.001 |
| S618 | PGIC pain 12 months | -0.7 (-0.8, -0.5) | -0.6 (-0.7, -0.4) | 0.1 (-0.1, 0.2) | <.001 |
| S619 | PGIC general 3 months | -0.8 (-0.9, -0.6) | -1.1 (-1.2, -1) | -0.3 (-0.5, -0.2) | <.001 |
| S620 | PGIC general 6 months | -0.6 (-0.7, -0.4) | -0.8 (-0.9, -0.6) | -0.2 (-0.3, 0) | <.001 |
| S621 | PGIC general 12 months | -0.6 (-0.8, -0.4) | -0.7 (-0.8, -0.5) | -0.1 (-0.2, 0.1) | <.001 |

### Consistency rule and independently reproduced calculation

**Rule applicable:** Yes, as an explicitly labeled diagnostic reconstruction supported by the same display. Let a=PT−UC, b=HC−UC and c=HC−PT=b−a. Under symmetric normal95% intervals use z=1.959963984540054, interval halfwidths h_j, variances v_j=(h_j/z)^2 and covariance u=(v_a+v_b−v_c)/2. The two-dimensional joint Wald statistic is

Q=(v_b a²+v_a b²−2uab)/(v_a v_b−u²),

with diagnostic chi-square2 tail P=exp(−Q/2). This reconstructed covariance is algebra within the tested family; it is not a claim about the authors' actual fitted covariance.

For every witness below I checked additive contrast identity, positive determinant, each point and both symmetric endpoints against the corresponding source number ±.05, and the computed tail against numeric P±.0005 or printed <.001. Arithmetic tolerance 1e−12 only accommodates floating-point endpoints. All 19 pass. These witnesses prove feasibility for these rows under this diagnostic family, not the actual undisclosed fitted implementation.

| Relationship | Witness (a,b,c) | Witness halfwidths | Diagnostic Q | Diagnostic P | Largest point/endpoint gap | All witness constraints met |
|---|---|---|---:|---:|---:|---|
| S601 | (-0.549, -0.549, 0) | (0.199, 0.199, 0.15) | 34.077570344 | 3.9824434849e-8 | 0.050000 | Yes |
| S602 | (-0.6, -0.6, 0) | (0.25, 0.25, 0.15) | 24.315167920 | 0.0000052484174757 | 0.050000 | Yes |
| S603 | (-0.549, -0.449, 0.1) | (0.201, 0.199, 0.15) | 29.340551305 | 4.2538310425e-7 | 0.050000 | Yes |
| S604 | (-0.398, -0.349, 0.049) | (0.152, 0.199, 0.199) | 28.892830604 | 5.3211015956e-7 | 0.050000 | Yes |
| S605 | (-0.449, -0.449, 0) | (0.199, 0.199, 0.15) | 22.793793846 | 0.000011230279251 | 0.050000 | Yes |
| S606 | (-0.349, -0.249, 0.1) | (0.201, 0.101, 0.15) | 23.354754552 | 0.0000084835863752 | 0.050000 | Yes |
| S607 | (-0.6, -0.649, -0.049) | (0.25, 0.199, 0.199) | 41.641881462 | 9.0694370878e-10 | 0.050000 | Yes |
| S608 | (-0.7, -0.7, 0) | (0.25, 0.25, 0.25) | 40.156049539 | 1.9064465561e-9 | 0.050000 | Yes |
| S609 | (-0.649, -0.549, 0.1) | (0.201, 0.201, 0.15) | 41.341524438 | 1.0539063750e-9 | 0.050000 | Yes |
| S610 | (1.151, 1.4, 0.249) | (0.899, 0.75, 0.701) | 13.411989543 | 0.0012235549409 | 0.050000 | Yes |
| S611 | (1.751, 1.451, -0.3) | (0.899, 0.699, 0.65) | 18.441295422 | 0.000098974559956 | 0.050000 | Yes |
| S612 | (1.802, 1.351, -0.451) | (0.948, 0.801, 0.799) | 15.726369532 | 0.00038464690825 | 0.050000 | Yes |
| S613 | (0.551, 0.552, 0.001) | (0.701, 0.798, 0.849) | 3.101587512 | 0.21207956755 | 0.050000 | Yes |
| S616 | (-0.798, -0.949, -0.151) | (0.148, 0.099, 0.101) | 375.441268582 | 2.9782722021e-82 | 0.050000 | Yes |
| S617 | (-0.7, -0.7, 0) | (0.15, 0.15, 0.15) | 111.544582053 | 6.0034619739e-25 | 0.050000 | Yes |
| S618 | (-0.7, -0.6, 0.1) | (0.15, 0.15, 0.15) | 97.886061801 | 5.5502398618e-22 | 0.050000 | Yes |
| S619 | (-0.8, -1.149, -0.349) | (0.15, 0.099, 0.101) | 611.340829900 | 1.7742936821e-133 | 0.050000 | Yes |
| S620 | (-0.6, -0.8, -0.2) | (0.15, 0.15, 0.15) | 118.373842178 | 1.9744528631e-26 | 0.050000 | Yes |
| S621 | (-0.649, -0.7, -0.051) | (0.199, 0.15, 0.101) | 93.615347054 | 4.6955414279e-21 | 0.050000 | Yes |

In particular social three months produces .001223554941 within [.0005,.0015], physical three months .21207956755 within [.2115,.2125], and all other 17 witnesses produce P<.001. The witnesses match source printed values and demonstrate same-display numerical support; no witness is offered as an author estimate.

### Exhaustive conservative display-precision check for both affected rows

Each displayed target point and CI endpoint receives ±.05. Numeric omnibus P receives ±.0005. Full feasible point/endpoint coupling is conservatively relaxed when forming the following bounding domains.

For physical six months: a∈[1.05,1.15], b∈[.35,.45], c=b−a∈[−.65,−.55] yields the point triangle (1.05,.40), (1.05,.45), (1.10,.45). Endpoint rounding permits the enlarged halfwidth boxes [.75,.85], [.65,.75], [.70,.80]. I separately evaluated all 24 point/variance-vertex combinations. Minimum covariance determinant 0.01195380636846352; maximum Q=8.556087823817016 at a=1.10,b=.45,h=(.75,.75,.70). Thus diagnostic P≥0.013869766053172373.

For physical twelve months: deliberately retain the larger point rectangle a∈[1.15,1.25], b∈[.85,.95], dropping the c constraint, and enlarged halfwidth boxes [.75,.85], [.85,.95], [.85,.95]. I separately evaluated all 32 point/variance-vertex combinations. Minimum covariance determinant 0.02217991416023505; maximum Q=12.281125558721055 at a=1.25,b=.95,h=(.75,.85,.95). Thus diagnostic P≥0.0021537112129520757.

The proof is not a grid search: Q=d′V⁻¹d is convex in d for fixed positive-definite V and convex in positive-definite V for fixed d; V is affine in the three contrast variances. All variance-box vertices are positive definite, hence so is their convex hull. Successive convexity therefore bounds Q by its point/variance-vertex maximum. Dropping point/endpoint halfwidth coupling, and the twelve-month c constraint, enlarges the feasible domains and preserves the bounds. Every actually precision-feasible tuple lies inside these conservative domains.

| Affected result | Conservative recomputed diagnostic P interval | Printed P half-unit interval | Minimum separating gap | Gap / absolute printed P |
|---|---|---|---:|---:|
| Physical functioning 6 months | [.013869766053172373,1] | [.0045,.0055] | .008369766053172373 | 1.6739532106344746 |
| Physical functioning 12 months | [.0021537112129520757,1] | [.0005,.0015] | .0006537112129520757 | .6537112129520757 |

**Calculation reproduced:** Yes, independently in JavaScript V8. Both outer diagnostic P intervals remain separated from the printed intervals even after conservative allowance for all displayed input precision. Route A category1 is independently exempt from rounding-based removal. The intervals' upper endpoints of 1 are deliberately loose logical bounds, not attainable maxima or fitted-P estimates. No replacement P is proposed. Both printed omnibus Ps and at least one contrast interval in each affected row indicate a result below .05; this candidate makes no claim of a .05-level conclusion reversal.

### Available inputs, exact missing definitions and alternatives

**Necessary inputs available:** Every printed target estimate, both interval limits, row/time and contrast identity, confidence level95%, corresponding numeric omnibus P, all19 same-display comparators, linear-GEE interval definition and broad replicated Wald-test context. These are sufficient to reproduce the diagnostic comparison and precision bounds.

**Necessary inputs unavailable for identification of the actual fitted analysis:** Unrounded estimates/interval endpoints; actual contrast covariance matrix; actual confidence critical value/reference distribution; omnibus reference distribution and degrees of freedom; explicit mapping of each omnibus P and contrast interval to the same covariance, fitted analysis and estimand; per-outcome/time sample size and missingness denominators; participant-level observations. The normal z and chi-square2 reference distribution are diagnostic choices, not reported facts.

**Source-grounded alternative interpretation:** eTable 11 note b identifies GEE intervals without explicitly naming their reference distribution, and the p15 replication statement may preserve broad structure rather than identical inferential details. An outcome/time-specific confidence distribution, a different omnibus reference distribution or df, separate covariance estimators, separate fitted analyses or another estimand/time-specific omnibus comparison could reconcile actual values. The table does not establish which of these applies. Missing definitions remain the human question rather than an inferred production mechanism.

**Direct observation versus inferred explanation:** Direct: the exact physical6/12 printed tuples, the two Ps and the stated model context. Reproduced mathematical observation: these tuples cannot yield those Ps within the independently supported normal-CI/common-covariance/chi-square2 reconstruction after half-unit rounding. Inferred only: that the authors used that exact reconstruction, that any particular production mechanism caused the discrepancy, or that one printed number should replace another. None of those inferences is asserted.

### Classification and determining evidence fact

**Document roles confirmed:** All compared numeric columns belong to REPORT results material, by content. Main article methods are REPORT corroboration. No PLAN content is compared.

**Relationship and precedence confirmed:** Primary S_W; all relationships S_W. The quantitative comparison is internal to one REPORT supplement. Main REPORT context only corroborates the tested family; it does not conflict with a numeric counterpart and adds no S_C relationship. No P_R or P_P relationship applies. No classification correction is required.

**Review domain confirmed:** statistical_results because the candidate concerns estimate/interval/test and method logic, rather than a conflicting assignment of a number to an outcome or analysis set.

**Classification ambiguity:** Exact supplement inferential mappings remain absent. This is an ambiguity of mathematical reconciliation, not of REPORT/PLAN content or relationship precedence.

**Evidence-state determining fact:** reproduced. All cited numbers and locations match the exact source, all19 comparator witnesses are precision-feasible when independently recalculated, and both affected tuples remain outside the diagnostic P half-unit intervals under exhaustive conservative bounds. No source transcription correction was needed. This evidence-record state does not identify the actual author implementation or adjudicate the candidate.

**Exact remaining human question:** Which fitted analysis, contrast covariance, confidence critical value/reference distribution and omnibus reference distribution/degrees of freedom produced the eTable11 physical-function six-/twelve-month P=.005/.001 and three MD95%CIs; do these columns refer to the same outcome, time, covariance and estimand; and which reported values should be extracted if their inferential constructions differ?

Completion: C018 separately rechecked; both affected rows and all19 corroborating rows covered; five distinct supplied-source pages visually inspected; one evidence state reproduced; zero source-reading gaps. Exact inferential definitions and fitted inputs named above remain unresolved. Every supplied source and previously written artifact was preserved.

