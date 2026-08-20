# Main Statistical Relationship Register

Fresh-source inventory for DOC-001. These records are statistical relationships to be independently checked; this map assigns no candidate or disposition.

| ID | Printed statistic / source location | Population, contrast, model, match key | Applicable later checks |
|---|---|---|---|
| S001 | p3 sample plan: 80% power, 2-sided P<.05, Bonferroni; 10-point target difference; 1280/320, 20% loss ->1600/400. | Cluster RCT power simulation; `sample-size-planning`. | Planning-number arithmetic and stated-rule compatibility only. |
| S002 | p3 respondent/nonrespondent comparison uses chi-square; adjusted/unadjusted GEE logistic regression, within-hospital clustering; listed covariates. | Prespecified analyses; `analysis-model-definition`. | Model/population/covariate-label consistency. |
| S003 | p3 adjusted ORs and 95% CIs converted to adjusted risk differences/95%CIs using observed control prevalence. | Four outcomes; `effect-measure-conversion`. | Effect-measure and scale/transform compatibility; do not reconstruct absent ORs. |
| S004 | p5: Hochberg-adjusted P values presented; 20 imputed data sets in post-hoc analysis. | Multiple outcomes/missing data; `multiplicity-imputation`. | Adjustment/imputation labels and result-model match. |
| S005 | p6: nonrespondents differed on age<30, black race, never married, no college: P<.001 for all. | Respondent vs nonrespondent comparison; `nonresponse-comparison`. | Displayed common P bound and model/test availability. |
| S006 | p6/p7 supine main mHealth: aRD 8.9% (5.3--11.7), P<.001; 89.1 vs80.2. | Adjusted mHealth main effect; `outcome-supine-mhealth-main`. | Difference/CI/P/direction and abstract/narrative/table identity. |
| S007 | p7 supine NQI-only: aRD -1.7% (-10.1--4.7), P=.74; adjusted risks78.5 vs80.2. | Adjusted NQI main effect; `table3-nqi-main-supine`. | Difference/CI/P/direction. |
| S008 | p7 supine mHealth-only interaction context: aRD2.6%(-3.1--7.2), P=.34; risks82.8 vs80.2; multiplicative interaction P=.01. | Interaction model; `table3-supine-interaction`. | Contrast identity, CI/P/model distinction, interaction label. |
| S009 | p7 supine mHealth+NQI interaction contrast: aRD9.4%(2.9--13.6), P=.03; risks89.6 vs80.2. | Interaction model; `table3-supine-interaction-estimate`. | Difference/CI/P/direction, outcome/model match. |
| S010 | p7 room sharing NQI: aRD3.7%(-0.4--7.2), P=.07; risks74.1 vs70.4. | Adjusted NQI main effect; `table3-nqi-roomshare`. | Difference/CI/P/direction. |
| S011 | p7 room sharing mHealth: aRD12.4%(9.3--15.1), P<.001; risks82.8 vs70.4; interaction P=.08. | Adjusted mHealth main effect; `outcome-roomshare-mhealth-main`. | Difference/CI/P/direction and abstract/narrative/table identity. |
| S012 | p7 no soft bedding NQI: aRD3.3%(-1.4--7.8), P=.22; risks70.9 vs67.6. | Adjusted NQI main effect; `table3-nqi-softbedding`. | Difference/CI/P/direction. |
| S013 | p7 no soft bedding mHealth: aRD11.8%(8.1--15.2), P<.001; risks79.4 vs67.6; interaction P=.29. | Adjusted mHealth main effect; `outcome-softbedding-mhealth-main`. | Difference/CI/P/direction and abstract/narrative/table identity. |
| S014 | p7 any pacifier NQI: aRD6.8%(1.4--11.9), P=.07; risks66.6 vs59.8. | Adjusted NQI main effect; `table3-nqi-pacifier`. | Difference/CI/P/direction; Hochberg label. |
| S015 | p7 any pacifier mHealth: aRD8.7%(3.9--13.1), P<.001; risks68.5 vs59.8; interaction P=.54. | Adjusted mHealth main effect; `outcome-pacifier-mhealth-main`. | Difference/CI/P/direction and abstract/narrative/table identity. |
| S016 | p7 post-hoc imputation says supine NQI-by-mHealth interaction was not significant; mHealth effects attenuated but consistent. | Multiple-imputation sensitivity analysis, no printed effect estimates. `posthoc-imputation-supine`. | Qualitative conclusion/model-label match; no numerical reconstruction. |
| S017 | p7 post-hoc race-stratified analysis says G4 beneficial-outcome rates similarly high regardless of race; p8 says disparities no longer significant. | Exploratory race analysis, no printed estimates/P values. `posthoc-race`. | Cross-location qualitative-statistical statement match only. |

Table 3 footnote constraints for S006--S015: adjusted for infant survey age/sex; maternal age, parity, race, education, marital status, income; and hospital SAFE rate where available. Risk differences/CIs are calculated from logistic-regression ORs/CIs; P values are Hochberg-adjusted logistic-regression values; interaction P values are multiplicative-interaction logistic-regression tests. No `P = 0` display occurs in DOC-001.
