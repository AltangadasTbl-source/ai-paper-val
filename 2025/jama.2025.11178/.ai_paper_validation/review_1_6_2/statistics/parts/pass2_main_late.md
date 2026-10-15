# Statistical relationship inventory — pass 2 main-late shard

Fresh runtime agent: `/root/stat2_main_late`; model gpt-6.1-sol, reasoning effort high. Assigned exactly55 relationships S056–S110; each is completed below. This part preserves the complete pass1 source tuples and records independent pass2 checks. No shared canonical artifact was edited.

Direct-source authority: visually reread current pinned PyMuPDF1.26.4 CPU renders of REPORT main physical PDF pp.4,10,11, plus REPORT results pp.17,18 for cross-lane PGIC context. Source links: [main methods](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), [Table3](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), [Table3 continuation and definitions](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11). Current native source text independently reread for the narrative and footnotes; OCR/text serve as locators. Complete current ledger17 IDs, screening26 decisions, evidence-recheck17 cards and original47 excluded rows were read. No legacy scientific record, web source or new Python helper was used.

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

