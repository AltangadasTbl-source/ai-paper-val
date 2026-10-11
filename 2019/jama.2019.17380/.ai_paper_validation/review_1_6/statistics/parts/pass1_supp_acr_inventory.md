# Statistical Pass 1: ACR Relationship Inventory Part

Agent: /root/stats_pass1_supp_acr; fresh gpt-6.1-sol/high. Canonical runtime ID is recorded by the coordinator in agent_execution_manifest.md. Scope: DOC-003 REPORT, eTables 6–9, PDF pp. 11–14. This part owns S401–S496 only. All 96 estimate/95% CI cells are independent records: 48 marginal geometric means, 32 within-assignment geometric change ratios, 16 active/placebo change ratios. Eight year-5 P values are integral to their contrast records. Baseline 1.0 reference constants are checked below but are not estimated intervals.

Authority: exact direct PDF and Poppler 26.01.0 layout extraction, command pdftotext -layout -f 11 -l 14 joi190122supp2_prod.pdf -. Current locator maps results_transcription.md, support_structured_map.md, and support_field_index.md were read. No old scientific conclusions or external evidence used. Source links below are relative to this part's location.

## Definitions carried into every row

MA and MP = active and placebo marginal geometric mean urine ACR, mg albumin/g creatinine; 95% CI. CA and CP = active and placebo geometric mean change ratio from baseline, dimensionless; 95% CI. D = ratio of change from baseline, active/placebo, dimensionless; 95% CI. Thus the reference/null is 1 for change and contrast ratios, not 0. A marginal level is positive but has no supplied hypothesis P value. The active assignment is vitamin D or omega-3 as named, compared with its corresponding placebo. All nonbaseline CA/CP fields indicate increase (>1). D>1 indicates larger active increase; D<1 indicates smaller active increase.

Model key GM: the table labels geometric mean/95% CI; exact marginal CI estimator is not supplied here. CH: change from baseline summarized over all participants using multiple imputation; no exact change-CI estimator stated. CT: linear mixed model adjusted for age and sex, missing data via multiple imputation; test refers to baseline-to-year-5 change for that assignment. The footnote anchors for GM/CH/CT are eTable6 p11 headers/**/* and ***, eTable7 p12 headers/***/** and ^, eTable8 p13 headers/**/* and ***, eTable9 p14 headers/**/* and ***. These keys carry those actual definitions, not invented estimates of variance or degrees of freedom.

P6: overall ACR analysis; source N varies by assignment/time. P7: baseline and year-5 available-case analysis, title N944; title and arm sums conflict with footnote991 (STAT-UA01). P8: adherent participants, >=2/3 study drug at >=4 of6 questionnaire times, stated N1032 per assignment; observed urine N is field-specific and may be less. P9: visits reporting UTI symptoms excluded; urine N is field-specific. N in D rows is the printed active/placebo observed N pair, not an assertion of the imputed inferential sample size.

Check key BASIC: printed point is within positive ordered interval; measure/scale and assignment/reference labels recorded. All 96 BASIC checks completed individually; no candidate from containment/endpoints alone. CA/CP intervals lie wholly above1. All16 D intervals include1, including rounded year2 endpoints1.00 in eTables7/8; those endpoint displays do not establish exact boundary significance. Paired year5 P values all exceed.05 and descriptively agree with the interval crossing1; this is a qualitative diagnostic, not a reconstruction of the exact test.

Missing inference definitions: the ACR contrast-specific SE/test statistic, reference distribution, degrees of freedom, covariance, variance estimator and multiple-imputation pooling output are absent from these tables. Even where the main statistical methods say two-sided testing, that does not supply each table's CI/test df or pooling definition. GM and CH CI construction is unspecified. Exact CI/P equality is therefore not asserted or used for candidate discovery. No finite-precision display-zero P occurs in this shard.

## Complete independent relationships

| S ID | Source and exact row | Field | Point | Lower95% | Upper95% | P | Printed N | Population | Model/footnote key | Pass1 check | Status |
|---|---|---|---:|---:|---:|---|---|---|---|---|---|
| S401 | [DOC-003 REPORT p11 eTable6 Vitamin D Baseline U066.MA](../../../../joi190122supp2_prod.pdf#page=11) | MA | 3.3 | 3.0 | 3.8 | not printed | 702 | P6 | GM | BASIC | PASS_1_COMPLETE |
| S402 | [DOC-003 REPORT p11 eTable6 Vitamin D Baseline U066.MP](../../../../joi190122supp2_prod.pdf#page=11) | MP | 3.2 | 2.8 | 3.6 | not printed | 609 | P6 | GM | BASIC | PASS_1_COMPLETE |
| S403 | [DOC-003 REPORT p11 eTable6 Vitamin D Year 2 U067.MA](../../../../joi190122supp2_prod.pdf#page=11) | MA | 5.5 | 4.8 | 6.5 | not printed | 529 | P6 | GM | BASIC | PASS_1_COMPLETE |
| S404 | [DOC-003 REPORT p11 eTable6 Vitamin D Year 2 U067.MP](../../../../joi190122supp2_prod.pdf#page=11) | MP | 4.7 | 4.0 | 5.5 | not printed | 463 | P6 | GM | BASIC | PASS_1_COMPLETE |
| S405 | [DOC-003 REPORT p11 eTable6 Vitamin D Year 2 U067.CA](../../../../joi190122supp2_prod.pdf#page=11) | CA | 1.79 | 1.60 | 2.01 | not printed | 529 | P6 | CH | BASIC | PASS_1_COMPLETE |
| S406 | [DOC-003 REPORT p11 eTable6 Vitamin D Year 2 U067.CP](../../../../joi190122supp2_prod.pdf#page=11) | CP | 1.57 | 1.41 | 1.76 | not printed | 463 | P6 | CH | BASIC | PASS_1_COMPLETE |
| S407 | [DOC-003 REPORT p11 eTable6 Vitamin D Year 2 U067.D](../../../../joi190122supp2_prod.pdf#page=11) | D | 1.14 | 0.96 | 1.37 | not printed | 529/463 | P6 | CT | BASIC | PASS_1_COMPLETE |
| S408 | [DOC-003 REPORT p11 eTable6 Vitamin D Year 5 U068.MA](../../../../joi190122supp2_prod.pdf#page=11) | MA | 9.3 | 8.1 | 10.6 | not printed | 505 | P6 | GM | BASIC | PASS_1_COMPLETE |
| S409 | [DOC-003 REPORT p11 eTable6 Vitamin D Year 5 U068.MP](../../../../joi190122supp2_prod.pdf#page=11) | MP | 9.2 | 8.0 | 10.5 | not printed | 440 | P6 | GM | BASIC | PASS_1_COMPLETE |
| S410 | [DOC-003 REPORT p11 eTable6 Vitamin D Year 5 U068.CA](../../../../joi190122supp2_prod.pdf#page=11) | CA | 2.97 | 2.66 | 3.32 | not printed | 505 | P6 | CH | BASIC | PASS_1_COMPLETE |
| S411 | [DOC-003 REPORT p11 eTable6 Vitamin D Year 5 U068.CP](../../../../joi190122supp2_prod.pdf#page=11) | CP | 3.02 | 2.70 | 3.38 | not printed | 440 | P6 | CH | BASIC | PASS_1_COMPLETE |
| S412 | [DOC-003 REPORT p11 eTable6 Vitamin D Year 5 U068.D](../../../../joi190122supp2_prod.pdf#page=11) | D | 0.99 | 0.84 | 1.17 | 0.90 | 505/440 | P6 | CT | BASIC; qualitative CI/P coherent | PASS_1_COMPLETE |
| S413 | [DOC-003 REPORT p11 eTable6 Omega-3 Baseline U069.MA](../../../../joi190122supp2_prod.pdf#page=11) | MA | 3.3 | 2.9 | 3.8 | not printed | 658 | P6 | GM | BASIC | PASS_1_COMPLETE |
| S414 | [DOC-003 REPORT p11 eTable6 Omega-3 Baseline U069.MP](../../../../joi190122supp2_prod.pdf#page=11) | MP | 3.2 | 2.8 | 3.6 | not printed | 653 | P6 | GM | BASIC | PASS_1_COMPLETE |
| S415 | [DOC-003 REPORT p11 eTable6 Omega-3 Year 2 U070.MA](../../../../joi190122supp2_prod.pdf#page=11) | MA | 5.2 | 4.5 | 6.2 | not printed | 502 | P6 | GM | BASIC | PASS_1_COMPLETE |
| S416 | [DOC-003 REPORT p11 eTable6 Omega-3 Year 2 U070.MP](../../../../joi190122supp2_prod.pdf#page=11) | MP | 5.0 | 4.3 | 5.8 | not printed | 490 | P6 | GM | BASIC | PASS_1_COMPLETE |
| S417 | [DOC-003 REPORT p11 eTable6 Omega-3 Year 2 U070.CA](../../../../joi190122supp2_prod.pdf#page=11) | CA | 1.66 | 1.48 | 1.86 | not printed | 502 | P6 | CH | BASIC | PASS_1_COMPLETE |
| S418 | [DOC-003 REPORT p11 eTable6 Omega-3 Year 2 U070.CP](../../../../joi190122supp2_prod.pdf#page=11) | CP | 1.71 | 1.53 | 1.91 | not printed | 490 | P6 | CH | BASIC | PASS_1_COMPLETE |
| S419 | [DOC-003 REPORT p11 eTable6 Omega-3 Year 2 U070.D](../../../../joi190122supp2_prod.pdf#page=11) | D | 0.97 | 0.81 | 1.16 | not printed | 502/490 | P6 | CT | BASIC | PASS_1_COMPLETE |
| S420 | [DOC-003 REPORT p11 eTable6 Omega-3 Year 5 U071.MA](../../../../joi190122supp2_prod.pdf#page=11) | MA | 9.1 | 7.9 | 10.5 | not printed | 478 | P6 | GM | BASIC | PASS_1_COMPLETE |
| S421 | [DOC-003 REPORT p11 eTable6 Omega-3 Year 5 U071.MP](../../../../joi190122supp2_prod.pdf#page=11) | MP | 9.4 | 8.2 | 10.6 | not printed | 467 | P6 | GM | BASIC | PASS_1_COMPLETE |
| S422 | [DOC-003 REPORT p11 eTable6 Omega-3 Year 5 U071.CA](../../../../joi190122supp2_prod.pdf#page=11) | CA | 2.94 | 2.62 | 3.30 | not printed | 478 | P6 | CH | BASIC | PASS_1_COMPLETE |
| S423 | [DOC-003 REPORT p11 eTable6 Omega-3 Year 5 U071.CP](../../../../joi190122supp2_prod.pdf#page=11) | CP | 3.05 | 2.74 | 3.40 | not printed | 467 | P6 | CH | BASIC | PASS_1_COMPLETE |
| S424 | [DOC-003 REPORT p11 eTable6 Omega-3 Year 5 U071.D](../../../../joi190122supp2_prod.pdf#page=11) | D | 0.96 | 0.81 | 1.14 | 0.64 | 478/467 | P6 | CT | BASIC; qualitative CI/P coherent | PASS_1_COMPLETE |
| S425 | [DOC-003 REPORT p12 eTable7 Vitamin D Baseline U072.MA](../../../../joi190122supp2_prod.pdf#page=12) | MA | 3.0 | 2.6 | 3.5 | not printed | 504 | P7 | GM | BASIC | PASS_1_COMPLETE |
| S426 | [DOC-003 REPORT p12 eTable7 Vitamin D Baseline U072.MP](../../../../joi190122supp2_prod.pdf#page=12) | MP | 3.1 | 2.6 | 3.5 | not printed | 440 | P7 | GM | BASIC | PASS_1_COMPLETE |
| S427 | [DOC-003 REPORT p12 eTable7 Vitamin D Year 2 U073.MA](../../../../joi190122supp2_prod.pdf#page=12) | MA | 5.2 | 4.5 | 6.1 | not printed | 449 | P7 | GM | BASIC | PASS_1_COMPLETE |
| S428 | [DOC-003 REPORT p12 eTable7 Vitamin D Year 2 U073.MP](../../../../joi190122supp2_prod.pdf#page=12) | MP | 4.5 | 3.8 | 5.3 | not printed | 396 | P7 | GM | BASIC | PASS_1_COMPLETE |
| S429 | [DOC-003 REPORT p12 eTable7 Vitamin D Year 2 U073.CA](../../../../joi190122supp2_prod.pdf#page=12) | CA | 1.80 | 1.58 | 2.05 | not printed | 449 | P7 | CH | BASIC | PASS_1_COMPLETE |
| S430 | [DOC-003 REPORT p12 eTable7 Vitamin D Year 2 U073.CP](../../../../joi190122supp2_prod.pdf#page=12) | CP | 1.51 | 1.33 | 1.71 | not printed | 396 | P7 | CH | BASIC | PASS_1_COMPLETE |
| S431 | [DOC-003 REPORT p12 eTable7 Vitamin D Year 2 U073.D](../../../../joi190122supp2_prod.pdf#page=12) | D | 1.20 | 1.00 | 1.44 | not printed | 449/396 | P7 | CT | BASIC | PASS_1_COMPLETE |
| S432 | [DOC-003 REPORT p12 eTable7 Vitamin D Year 5 U074.MA](../../../../joi190122supp2_prod.pdf#page=12) | MA | 9.3 | 8.1 | 10.7 | not printed | 504 | P7 | GM | BASIC | PASS_1_COMPLETE |
| S433 | [DOC-003 REPORT p12 eTable7 Vitamin D Year 5 U074.MP](../../../../joi190122supp2_prod.pdf#page=12) | MP | 9.2 | 8.0 | 10.5 | not printed | 440 | P7 | GM | BASIC | PASS_1_COMPLETE |
| S434 | [DOC-003 REPORT p12 eTable7 Vitamin D Year 5 U074.CA](../../../../joi190122supp2_prod.pdf#page=12) | CA | 3.08 | 2.70 | 3.50 | not printed | 504 | P7 | CH | BASIC | PASS_1_COMPLETE |
| S435 | [DOC-003 REPORT p12 eTable7 Vitamin D Year 5 U074.CP](../../../../joi190122supp2_prod.pdf#page=12) | CP | 3.00 | 2.65 | 3.41 | not printed | 440 | P7 | CH | BASIC | PASS_1_COMPLETE |
| S436 | [DOC-003 REPORT p12 eTable7 Vitamin D Year 5 U074.D](../../../../joi190122supp2_prod.pdf#page=12) | D | 1.03 | 0.86 | 1.22 | 0.77 | 504/440 | P7 | CT | BASIC; qualitative CI/P coherent | PASS_1_COMPLETE |
| S437 | [DOC-003 REPORT p12 eTable7 Omega-3 Baseline U075.MA](../../../../joi190122supp2_prod.pdf#page=12) | MA | 3.1 | 2.7 | 3.6 | not printed | 477 | P7 | GM | BASIC | PASS_1_COMPLETE |
| S438 | [DOC-003 REPORT p12 eTable7 Omega-3 Baseline U075.MP](../../../../joi190122supp2_prod.pdf#page=12) | MP | 3.0 | 2.6 | 3.4 | not printed | 467 | P7 | GM | BASIC | PASS_1_COMPLETE |
| S439 | [DOC-003 REPORT p12 eTable7 Omega-3 Year 2 U076.MA](../../../../joi190122supp2_prod.pdf#page=12) | MA | 5.0 | 4.2 | 5.9 | not printed | 433 | P7 | GM | BASIC | PASS_1_COMPLETE |
| S440 | [DOC-003 REPORT p12 eTable7 Omega-3 Year 2 U076.MP](../../../../joi190122supp2_prod.pdf#page=12) | MP | 4.7 | 4.0 | 5.5 | not printed | 412 | P7 | GM | BASIC | PASS_1_COMPLETE |
| S441 | [DOC-003 REPORT p12 eTable7 Omega-3 Year 2 U076.CA](../../../../joi190122supp2_prod.pdf#page=12) | CA | 1.62 | 1.43 | 1.84 | not printed | 433 | P7 | CH | BASIC | PASS_1_COMPLETE |
| S442 | [DOC-003 REPORT p12 eTable7 Omega-3 Year 2 U076.CP](../../../../joi190122supp2_prod.pdf#page=12) | CP | 1.69 | 1.49 | 1.92 | not printed | 412 | P7 | CH | BASIC | PASS_1_COMPLETE |
| S443 | [DOC-003 REPORT p12 eTable7 Omega-3 Year 2 U076.D](../../../../joi190122supp2_prod.pdf#page=12) | D | 0.96 | 0.80 | 1.15 | not printed | 433/412 | P7 | CT | BASIC | PASS_1_COMPLETE |
| S444 | [DOC-003 REPORT p12 eTable7 Omega-3 Year 5 U077.MA](../../../../joi190122supp2_prod.pdf#page=12) | MA | 9.1 | 7.9 | 10.5 | not printed | 477 | P7 | GM | BASIC | PASS_1_COMPLETE |
| S445 | [DOC-003 REPORT p12 eTable7 Omega-3 Year 5 U077.MP](../../../../joi190122supp2_prod.pdf#page=12) | MP | 9.4 | 8.2 | 10.6 | not printed | 467 | P7 | GM | BASIC | PASS_1_COMPLETE |
| S446 | [DOC-003 REPORT p12 eTable7 Omega-3 Year 5 U077.CA](../../../../joi190122supp2_prod.pdf#page=12) | CA | 2.94 | 2.58 | 3.36 | not printed | 477 | P7 | CH | BASIC | PASS_1_COMPLETE |
| S447 | [DOC-003 REPORT p12 eTable7 Omega-3 Year 5 U077.CP](../../../../joi190122supp2_prod.pdf#page=12) | CP | 3.15 | 2.77 | 3.57 | not printed | 467 | P7 | CH | BASIC | PASS_1_COMPLETE |
| S448 | [DOC-003 REPORT p12 eTable7 Omega-3 Year 5 U077.D](../../../../joi190122supp2_prod.pdf#page=12) | D | 0.93 | 0.78 | 1.11 | 0.44 | 477/467 | P7 | CT | BASIC; qualitative CI/P coherent | PASS_1_COMPLETE |
| S449 | [DOC-003 REPORT p13 eTable8 Vitamin D Baseline U078.MA](../../../../joi190122supp2_prod.pdf#page=13) | MA | 3.1 | 2.7 | 3.5 | not printed | 545 | P8 | GM | BASIC | PASS_1_COMPLETE |
| S450 | [DOC-003 REPORT p13 eTable8 Vitamin D Baseline U078.MP](../../../../joi190122supp2_prod.pdf#page=13) | MP | 3.1 | 2.7 | 3.6 | not printed | 486 | P8 | GM | BASIC | PASS_1_COMPLETE |
| S451 | [DOC-003 REPORT p13 eTable8 Vitamin D Year 2 U079.MA](../../../../joi190122supp2_prod.pdf#page=13) | MA | 5.4 | 4.6 | 6.3 | not printed | 481 | P8 | GM | BASIC | PASS_1_COMPLETE |
| S452 | [DOC-003 REPORT p13 eTable8 Vitamin D Year 2 U079.MP](../../../../joi190122supp2_prod.pdf#page=13) | MP | 4.4 | 3.7 | 5.2 | not printed | 420 | P8 | GM | BASIC | PASS_1_COMPLETE |
| S453 | [DOC-003 REPORT p13 eTable8 Vitamin D Year 2 U079.CA](../../../../joi190122supp2_prod.pdf#page=13) | CA | 1.80 | 1.58 | 2.05 | not printed | 481 | P8 | CH | BASIC | PASS_1_COMPLETE |
| S454 | [DOC-003 REPORT p13 eTable8 Vitamin D Year 2 U079.CP](../../../../joi190122supp2_prod.pdf#page=13) | CP | 1.51 | 1.34 | 1.70 | not printed | 420 | P8 | CH | BASIC | PASS_1_COMPLETE |
| S455 | [DOC-003 REPORT p13 eTable8 Vitamin D Year 2 U079.D](../../../../joi190122supp2_prod.pdf#page=13) | D | 1.20 | 1.00 | 1.43 | not printed | 481/420 | P8 | CT | BASIC | PASS_1_COMPLETE |
| S456 | [DOC-003 REPORT p13 eTable8 Vitamin D Year 5 U080.MA](../../../../joi190122supp2_prod.pdf#page=13) | MA | 9.2 | 8.0 | 10.6 | not printed | 467 | P8 | GM | BASIC | PASS_1_COMPLETE |
| S457 | [DOC-003 REPORT p13 eTable8 Vitamin D Year 5 U080.MP](../../../../joi190122supp2_prod.pdf#page=13) | MP | 9.1 | 7.9 | 10.5 | not printed | 407 | P8 | GM | BASIC | PASS_1_COMPLETE |
| S458 | [DOC-003 REPORT p13 eTable8 Vitamin D Year 5 U080.CA](../../../../joi190122supp2_prod.pdf#page=13) | CA | 3.03 | 2.68 | 3.44 | not printed | 467 | P8 | CH | BASIC | PASS_1_COMPLETE |
| S459 | [DOC-003 REPORT p13 eTable8 Vitamin D Year 5 U080.CP](../../../../joi190122supp2_prod.pdf#page=13) | CP | 2.99 | 2.64 | 3.37 | not printed | 407 | P8 | CH | BASIC | PASS_1_COMPLETE |
| S460 | [DOC-003 REPORT p13 eTable8 Vitamin D Year 5 U080.D](../../../../joi190122supp2_prod.pdf#page=13) | D | 1.02 | 0.85 | 1.22 | 0.87 | 467/407 | P8 | CT | BASIC; qualitative CI/P coherent | PASS_1_COMPLETE |
| S461 | [DOC-003 REPORT p13 eTable8 Omega-3 Baseline U081.MA](../../../../joi190122supp2_prod.pdf#page=13) | MA | 3.1 | 2.7 | 3.5 | not printed | 517 | P8 | GM | BASIC | PASS_1_COMPLETE |
| S462 | [DOC-003 REPORT p13 eTable8 Omega-3 Baseline U081.MP](../../../../joi190122supp2_prod.pdf#page=13) | MP | 3.1 | 2.7 | 3.5 | not printed | 514 | P8 | GM | BASIC | PASS_1_COMPLETE |
| S463 | [DOC-003 REPORT p13 eTable8 Omega-3 Year 2 U082.MA](../../../../joi190122supp2_prod.pdf#page=13) | MA | 4.9 | 4.2 | 5.8 | not printed | 461 | P8 | GM | BASIC | PASS_1_COMPLETE |
| S464 | [DOC-003 REPORT p13 eTable8 Omega-3 Year 2 U082.MP](../../../../joi190122supp2_prod.pdf#page=13) | MP | 4.8 | 4.2 | 5.7 | not printed | 441 | P8 | GM | BASIC | PASS_1_COMPLETE |
| S465 | [DOC-003 REPORT p13 eTable8 Omega-3 Year 2 U082.CA](../../../../joi190122supp2_prod.pdf#page=13) | CA | 1.63 | 1.43 | 1.86 | not printed | 461 | P8 | CH | BASIC | PASS_1_COMPLETE |
| S466 | [DOC-003 REPORT p13 eTable8 Omega-3 Year 2 U082.CP](../../../../joi190122supp2_prod.pdf#page=13) | CP | 1.70 | 1.51 | 1.91 | not printed | 441 | P8 | CH | BASIC | PASS_1_COMPLETE |
| S467 | [DOC-003 REPORT p13 eTable8 Omega-3 Year 2 U082.D](../../../../joi190122supp2_prod.pdf#page=13) | D | 0.96 | 0.80 | 1.16 | not printed | 461/441 | P8 | CT | BASIC | PASS_1_COMPLETE |
| S468 | [DOC-003 REPORT p13 eTable8 Omega-3 Year 5 U083.MA](../../../../joi190122supp2_prod.pdf#page=13) | MA | 9.2 | 7.9 | 10.7 | not printed | 443 | P8 | GM | BASIC | PASS_1_COMPLETE |
| S469 | [DOC-003 REPORT p13 eTable8 Omega-3 Year 5 U083.MP](../../../../joi190122supp2_prod.pdf#page=13) | MP | 9.1 | 8.0 | 10.4 | not printed | 430 | P8 | GM | BASIC | PASS_1_COMPLETE |
| S470 | [DOC-003 REPORT p13 eTable8 Omega-3 Year 5 U083.CA](../../../../joi190122supp2_prod.pdf#page=13) | CA | 3.03 | 2.67 | 3.44 | not printed | 443 | P8 | CH | BASIC | PASS_1_COMPLETE |
| S471 | [DOC-003 REPORT p13 eTable8 Omega-3 Year 5 U083.CP](../../../../joi190122supp2_prod.pdf#page=13) | CP | 3.04 | 2.70 | 3.43 | not printed | 430 | P8 | CH | BASIC | PASS_1_COMPLETE |
| S472 | [DOC-003 REPORT p13 eTable8 Omega-3 Year 5 U083.D](../../../../joi190122supp2_prod.pdf#page=13) | D | 0.99 | 0.83 | 1.19 | 0.94 | 443/430 | P8 | CT | BASIC; qualitative CI/P coherent | PASS_1_COMPLETE |
| S473 | [DOC-003 REPORT p14 eTable9 Vitamin D Baseline U084.MA](../../../../joi190122supp2_prod.pdf#page=14) | MA | 3.3 | 2.9 | 3.7 | not printed | 680 | P9 | GM | BASIC | PASS_1_COMPLETE |
| S474 | [DOC-003 REPORT p14 eTable9 Vitamin D Baseline U084.MP](../../../../joi190122supp2_prod.pdf#page=14) | MP | 3.1 | 2.7 | 3.5 | not printed | 582 | P9 | GM | BASIC | PASS_1_COMPLETE |
| S475 | [DOC-003 REPORT p14 eTable9 Vitamin D Year 2 U085.MA](../../../../joi190122supp2_prod.pdf#page=14) | MA | 5.5 | 4.7 | 6.4 | not printed | 510 | P9 | GM | BASIC | PASS_1_COMPLETE |
| S476 | [DOC-003 REPORT p14 eTable9 Vitamin D Year 2 U085.MP](../../../../joi190122supp2_prod.pdf#page=14) | MP | 4.5 | 3.9 | 5.3 | not printed | 449 | P9 | GM | BASIC | PASS_1_COMPLETE |
| S477 | [DOC-003 REPORT p14 eTable9 Vitamin D Year 2 U085.CA](../../../../joi190122supp2_prod.pdf#page=14) | CA | 1.77 | 1.59 | 1.98 | not printed | 510 | P9 | CH | BASIC | PASS_1_COMPLETE |
| S478 | [DOC-003 REPORT p14 eTable9 Vitamin D Year 2 U085.CP](../../../../joi190122supp2_prod.pdf#page=14) | CP | 1.52 | 1.37 | 1.70 | not printed | 449 | P9 | CH | BASIC | PASS_1_COMPLETE |
| S479 | [DOC-003 REPORT p14 eTable9 Vitamin D Year 2 U085.D](../../../../joi190122supp2_prod.pdf#page=14) | D | 1.16 | 0.97 | 1.39 | not printed | 510/449 | P9 | CT | BASIC | PASS_1_COMPLETE |
| S480 | [DOC-003 REPORT p14 eTable9 Vitamin D Year 5 U086.MA](../../../../joi190122supp2_prod.pdf#page=14) | MA | 9.1 | 7.9 | 10.4 | not printed | 487 | P9 | GM | BASIC | PASS_1_COMPLETE |
| S481 | [DOC-003 REPORT p14 eTable9 Vitamin D Year 5 U086.MP](../../../../joi190122supp2_prod.pdf#page=14) | MP | 9.1 | 7.9 | 10.4 | not printed | 422 | P9 | GM | BASIC | PASS_1_COMPLETE |
| S482 | [DOC-003 REPORT p14 eTable9 Vitamin D Year 5 U086.CA](../../../../joi190122supp2_prod.pdf#page=14) | CA | 2.94 | 2.63 | 3.28 | not printed | 487 | P9 | CH | BASIC | PASS_1_COMPLETE |
| S483 | [DOC-003 REPORT p14 eTable9 Vitamin D Year 5 U086.CP](../../../../joi190122supp2_prod.pdf#page=14) | CP | 2.98 | 2.67 | 3.32 | not printed | 422 | P9 | CH | BASIC | PASS_1_COMPLETE |
| S484 | [DOC-003 REPORT p14 eTable9 Vitamin D Year 5 U086.D](../../../../joi190122supp2_prod.pdf#page=14) | D | 0.99 | 0.84 | 1.17 | 0.90 | 487/422 | P9 | CT | BASIC; qualitative CI/P coherent | PASS_1_COMPLETE |
| S485 | [DOC-003 REPORT p14 eTable9 Omega-3 Baseline U087.MA](../../../../joi190122supp2_prod.pdf#page=14) | MA | 3.3 | 2.9 | 3.7 | not printed | 635 | P9 | GM | BASIC | PASS_1_COMPLETE |
| S486 | [DOC-003 REPORT p14 eTable9 Omega-3 Baseline U087.MP](../../../../joi190122supp2_prod.pdf#page=14) | MP | 3.1 | 2.8 | 3.6 | not printed | 627 | P9 | GM | BASIC | PASS_1_COMPLETE |
| S487 | [DOC-003 REPORT p14 eTable9 Omega-3 Year 2 U088.MA](../../../../joi190122supp2_prod.pdf#page=14) | MA | 5.0 | 4.2 | 5.9 | not printed | 482 | P9 | GM | BASIC | PASS_1_COMPLETE |
| S488 | [DOC-003 REPORT p14 eTable9 Omega-3 Year 2 U088.MP](../../../../joi190122supp2_prod.pdf#page=14) | MP | 5.0 | 4.3 | 5.8 | not printed | 477 | P9 | GM | BASIC | PASS_1_COMPLETE |
| S489 | [DOC-003 REPORT p14 eTable9 Omega-3 Year 2 U088.CA](../../../../joi190122supp2_prod.pdf#page=14) | CA | 1.62 | 1.44 | 1.82 | not printed | 482 | P9 | CH | BASIC | PASS_1_COMPLETE |
| S490 | [DOC-003 REPORT p14 eTable9 Omega-3 Year 2 U088.CP](../../../../joi190122supp2_prod.pdf#page=14) | CP | 1.69 | 1.52 | 1.88 | not printed | 477 | P9 | CH | BASIC | PASS_1_COMPLETE |
| S491 | [DOC-003 REPORT p14 eTable9 Omega-3 Year 2 U088.D](../../../../joi190122supp2_prod.pdf#page=14) | D | 0.96 | 0.80 | 1.15 | not printed | 482/477 | P9 | CT | BASIC | PASS_1_COMPLETE |
| S492 | [DOC-003 REPORT p14 eTable9 Omega-3 Year 5 U089.MA](../../../../joi190122supp2_prod.pdf#page=14) | MA | 9.2 | 8.0 | 10.6 | not printed | 460 | P9 | GM | BASIC | PASS_1_COMPLETE |
| S493 | [DOC-003 REPORT p14 eTable9 Omega-3 Year 5 U089.MP](../../../../joi190122supp2_prod.pdf#page=14) | MP | 9.0 | 7.9 | 10.2 | not printed | 449 | P9 | GM | BASIC | PASS_1_COMPLETE |
| S494 | [DOC-003 REPORT p14 eTable9 Omega-3 Year 5 U089.CA](../../../../joi190122supp2_prod.pdf#page=14) | CA | 2.91 | 2.60 | 3.25 | not printed | 460 | P9 | CH | BASIC | PASS_1_COMPLETE |
| S495 | [DOC-003 REPORT p14 eTable9 Omega-3 Year 5 U089.CP](../../../../joi190122supp2_prod.pdf#page=14) | CP | 3.01 | 2.70 | 3.35 | not printed | 449 | P9 | CH | BASIC | PASS_1_COMPLETE |
| S496 | [DOC-003 REPORT p14 eTable9 Omega-3 Year 5 U089.D](../../../../joi190122supp2_prod.pdf#page=14) | D | 0.98 | 0.83 | 1.16 | 0.80 | 460/449 | P9 | CT | BASIC; qualitative CI/P coherent | PASS_1_COMPLETE |

## Reference and repetition checks

All eight intervention baseline rows across these four tables print 1.0 (Ref.) in both within-assignment change columns and the active/placebo contrast column; these are reference constants, not inferred CIs or tests. The table headers call the outer column “Difference in change” but explicitly specify ratio of change active/placebo; the explicit ratio subheader resolves the scale. Dimensional units mg/g apply to marginal ACR levels; change ratios have no mg/g dimension. The generic “Mean and SD values” units footnote does not redefine the displayed 95% CI as an SD.

Repeated printed values were checked without assuming that distinct sensitivity populations must give different estimates. eTable6 and eTable9 vitamin D year5 D are both0.99(0.84,1.17),P.90; their populations differ, so repetition is possible at printed precision. eTable7 and eTable8 vitamin D year2 active changes both1.80(1.58,2.05); populations differ. Repeated eTable7/eTable8/eTable9 marginal means and endpoints similarly do not establish a duplicate-data defect. All row identities are retained.

The tables summarize marginal ACR at time-specific observed N while changes use multiple imputation and D uses an adjusted mixed model. Dividing displayed marginal means need not recover imputed change estimates; dividing separately summarized CA by CP need not recover an adjusted D. Such arithmetic is only diagnostic unless a common estimator and identical contributing participants are supplied. Example eTable9 omega-3 year5:2.91/3.01=0.9668, while adjusted D=.98; these different printed estimator definitions do not establish a candidate. Rounded ratio CIs are not expected to be symmetric on the raw ratio scale.

One candidate is emitted on the independently printed P7 population disagreement. It affects the population definition for S425–S448 without making the interval values numerically contradictory. All relationships remain available for fresh pass2 using the complete cross-lane ledger and recheck.

