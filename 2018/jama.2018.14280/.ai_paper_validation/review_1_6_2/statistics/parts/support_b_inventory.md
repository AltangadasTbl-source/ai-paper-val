# Statistical relationship inventory — pass 1 support shard B

Runtime agent ID: /root/statistics_pass1_support_b. Model: gpt-6.1-sol. Reasoning effort: high. Stage: fresh statistical pass 1 shard. Exact disjoint scope: DOC-004 REPORT joi180108supp3_prod.pdf physical pages 7–9; 72 eTable 3 mode–variable–occasion tuples, 30 eTable 4 rows, 16 eTable 5 subgroup mean-difference/95%CI rows with eight shared interaction tests mapped to the row pairs. Total 118 stable relationships S321–S438. PASS_1_COMPLETE for every record; pass 2 remains for a different fresh agent.

Controls QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely. Scientific inputs: current support evidence map pp7–9 with specific SAP pp12,14,22 excerpts, current structured main map M013–M016/M061/M079–M080, and exact supplied supplement pages. Direct native/layout confirmation: Poppler pdftotext 25.03.0, command `pdftotext -layout -f 7 -l 9 joi180108supp3_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/st1-b-supp-p7-9.txt`. Visual confirmation: source-matched reusable page 7/page 8/page 9 images in review_1_5_2/preprocessing/rendered_pages, engine UNKNOWN_LEGACY_RENDERER, CPU. No original or reusable artifact changed.

## Rules and precise limits used for every record

T3-CONT: eTable 3 continuous values are median (IQR), not confidence intervals. Both medians lie within correctly ordered quartiles in all 48 continuous tuples. IQR overlap does not test a between-arm effect. No test statistic, standard error, row-specific continuous test or raw ranks supplied; no parametric/rank P reconstruction is asserted. Directions remain the printed low-versus-intermediate contrast, including equal rounded medians with possible distributional differences.

T3-COUNT: all 24 binary tuples checked count≤denominator, percentages under half-unit input/output intervals and the 0.05 relative-gap rule, pH<7.25/acidosis identity, and zero-event/no-P states. Acidosis means pH<7.35 AND PaCO2>45; it is not the same endpoint as pH<7.25. The table expressly attributes smaller binary denominators to missing ABG measurements. Event denominator≤mode contributor count in every arm/occasion. All percentage gaps remain at most 0.05. Exact binary test variants/continuity correction are unreported for this table; no variant is assumed.

T4-IQR: both medians contained in correctly ordered IQRs in all continuous rows. Equal rounded medians/IQRs do not establish an identical distribution, including RASS day 3 P=.01. No CIs, SEs or test statistics are printed, and row-specific continuous tests unreported.

T4-COUNT: explicit n/N percentages and rescue-therapy n/header-N percentages checked under half-unit intervals. All reconcile under precision. T4-HEADER_PRECISION: four count/% rows without explicit row-N show arithmetic differences against headers 477/484, but all remaining relative gaps≤ 0.05; recorded once as an excluded observation, without inventing available-data denominators.

T5: each point estimate lies inside its ordered 95% CI; low-minus-intermediate direction and displayed means' rounding intervals agree. All CIs include zero except ICU-start MD−2.50 CI(−4.63,−0.36). Eight P values are pair interaction tests from Gaussian GLMs (main REPORT p4); none is an individual subgroup effect P. Exact subgroup n, CI-producing method, degrees of freedom, link, covariates, variance estimator and covariance/mapping to interaction model are not supplied. No covariance is inferred. Independence/normal-CI-width calculations below are labelled diagnostics, not reproductions of the reported analysis. The main REPORT states two-sided P, alpha.05 and no multiplicity adjustment; subgroup results are exploratory. No noninferiority/equivalence margin, interim boundary or stopping conclusion appears in assigned displays.

eTable 3 mode contributor counts low/intermediate at after titration,day 1,day 2,day 3: VCV 309/362,129/214,61/68,46/42; PSV 110/73,225/164,211/223,181/192; Other 33/28,37/32,49/52,45/62.

## Stable records

Source links below point to the exact supplied REPORT page. Columns preserve all printed tuple components; the pass record explicitly applies the relevant rule above.

| S ID | Exact REPORT source/row | Occasion | Low printed statistic | Intermediate printed statistic | Printed P / shared interaction | Pass 1 record |
|---|---|---|---|---|---|---|
| S321 | [DOC-004 p7 eTable 3 VCV, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | 0.45 (0.40–0.60) | 0.40 (0.40–0.60) | .18 | PASS_1_COMPLETE; T3-CONT; no finding |
| S322 | [DOC-004 p7 eTable 3 VCV, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | 0.40 (0.30–0.50) | 0.35 (0.30–0.40) | .001 | PASS_1_COMPLETE; T3-CONT; no finding |
| S323 | [DOC-004 p7 eTable 3 VCV, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | 0.40 (0.35–0.45) | 0.35 (0.30–0.42) | .06 | PASS_1_COMPLETE; T3-CONT; no finding |
| S324 | [DOC-004 p7 eTable 3 VCV, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | 0.40 (0.35–0.45) | 0.35 (0.25–0.48) | .28 | PASS_1_COMPLETE; T3-CONT; no finding |
| S325 | [DOC-004 p7 eTable 3 VCV, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | 199 (149–287) | 204 (151–312) | .24 | PASS_1_COMPLETE; T3-CONT; no finding |
| S326 | [DOC-004 p7 eTable 3 VCV, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | 221 (164–283) | 245 (180–317) | .03 | PASS_1_COMPLETE; T3-CONT; no finding |
| S327 | [DOC-004 p7 eTable 3 VCV, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | 210 (169–274) | 240 (172–296) | .26 | PASS_1_COMPLETE; T3-CONT; no finding |
| S328 | [DOC-004 p7 eTable 3 VCV, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | 202 (158–247) | 249 (154–318) | .22 | PASS_1_COMPLETE; T3-CONT; no finding |
| S329 | [DOC-004 p7 eTable 3 VCV, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | 43.5 (39.0–49.5) | 35.2 (30.0–40.5) | <.001 | PASS_1_COMPLETE; T3-CONT; no finding |
| S330 | [DOC-004 p7 eTable 3 VCV, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | 41.2 (37.5–46.0) | 33.7 (30.7–37.5) | <.001 | PASS_1_COMPLETE; T3-CONT; no finding |
| S331 | [DOC-004 p7 eTable 3 VCV, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | 42.0 (38.2–47.2) | 36.0 (33.0–39.0) | <.001 | PASS_1_COMPLETE; T3-CONT; no finding |
| S332 | [DOC-004 p7 eTable 3 VCV, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | 43.5 (38.2–49.3) | 37.5 (35.4–41.1) | <.001 | PASS_1_COMPLETE; T3-CONT; no finding |
| S333 | [DOC-004 p7 eTable 3 VCV, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | 7.30 (7.23–7.36) | 7.40 (7.32–7.48) | <.001 | PASS_1_COMPLETE; T3-CONT; no finding |
| S334 | [DOC-004 p7 eTable 3 VCV, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | 7.35 (7.30–7.40) | 7.43 (7.36–7.48) | <.001 | PASS_1_COMPLETE; T3-CONT; no finding |
| S335 | [DOC-004 p7 eTable 3 VCV, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | 7.38 (7.32–7.42) | 7.43 (7.40–7.47) | <.001 | PASS_1_COMPLETE; T3-CONT; no finding |
| S336 | [DOC-004 p7 eTable 3 VCV, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | 7.39 (7.35–7.43) | 7.43 (7.39–7.47) | .007 | PASS_1_COMPLETE; T3-CONT; no finding |
| S337 | [DOC-004 p7 eTable 3 VCV, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | 74/264 (27.9) | 33/319 (10.3) | <.001 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S338 | [DOC-004 p7 eTable 3 VCV, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | 11/129 (8.5) | 8/213 (3.8) | .07 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S339 | [DOC-004 p7 eTable 3 VCV, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | 0/59 (0.0) | 0/67 (0.0) | — | PASS_1_COMPLETE; T3-COUNT; no finding |
| S340 | [DOC-004 p7 eTable 3 VCV, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | 3/46 (6.5) | 0/42 (0.0) | .28 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S341 | [DOC-004 p7 eTable 3 VCV, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | 100/264 (37.9) | 33/319 (10.3) | <.001 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S342 | [DOC-004 p7 eTable 3 VCV, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | 21/129 (16.3) | 10/213 (4.7) | <.001 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S343 | [DOC-004 p7 eTable 3 VCV, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | 9/59 (15.3) | 2/67 (3.0) | .01 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S344 | [DOC-004 p7 eTable 3 VCV, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | 6/46 (13.0) | 2/42 (4.8) | .18 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S345 | [DOC-004 p7 eTable 3 PSV, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | 0.40 (0.35–0.50) | 0.40 (0.35–0.50) | .51 | PASS_1_COMPLETE; T3-CONT; no finding |
| S346 | [DOC-004 p7 eTable 3 PSV, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | 0.35 (0.30–0.45) | 0.35 (0.30–0.40) | .53 | PASS_1_COMPLETE; T3-CONT; no finding |
| S347 | [DOC-004 p7 eTable 3 PSV, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | 0.35 (0.30–0.40) | 0.35 (0.30–0.40) | .79 | PASS_1_COMPLETE; T3-CONT; no finding |
| S348 | [DOC-004 p7 eTable 3 PSV, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | 0.35 (0.30–0.40) | 0.35 (0.30–0.40) | .36 | PASS_1_COMPLETE; T3-CONT; no finding |
| S349 | [DOC-004 p7 eTable 3 PSV, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | 239 (168–315) | 240 (179–293) | .70 | PASS_1_COMPLETE; T3-CONT; no finding |
| S350 | [DOC-004 p7 eTable 3 PSV, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | 237 (182–309) | 240 (187–306) | .96 | PASS_1_COMPLETE; T3-CONT; no finding |
| S351 | [DOC-004 p7 eTable 3 PSV, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | 227 (184–294) | 245 (183–300) | .57 | PASS_1_COMPLETE; T3-CONT; no finding |
| S352 | [DOC-004 p7 eTable 3 PSV, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | 241 (190–290) | 228 (172–304) | .52 | PASS_1_COMPLETE; T3-CONT; no finding |
| S353 | [DOC-004 p7 eTable 3 PSV, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | 42.7 (37.5–47.2) | 40.5 (36.0–44.2) | .23 | PASS_1_COMPLETE; T3-CONT; no finding |
| S354 | [DOC-004 p7 eTable 3 PSV, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | 39.0 (35.2–43.5) | 37.5 (33.6–42.0) | .04 | PASS_1_COMPLETE; T3-CONT; no finding |
| S355 | [DOC-004 p7 eTable 3 PSV, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | 39.0 (36.0–44.2) | 37.5 (33.7–42.9) | .03 | PASS_1_COMPLETE; T3-CONT; no finding |
| S356 | [DOC-004 p7 eTable 3 PSV, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | 39.7 (35.8–45.0) | 38.2 (33.0–42.7) | .01 | PASS_1_COMPLETE; T3-CONT; no finding |
| S357 | [DOC-004 p7 eTable 3 PSV, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | 7.35 (7.27–7.40) | 7.35 (7.29–7.40) | .78 | PASS_1_COMPLETE; T3-CONT; no finding |
| S358 | [DOC-004 p7 eTable 3 PSV, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | 7.40 (7.35–7.43) | 7.43 (7.37–7.46) | <.001 | PASS_1_COMPLETE; T3-CONT; no finding |
| S359 | [DOC-004 p7 eTable 3 PSV, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | 7.42 (7.38–7.46) | 7.43 (7.38–7.47) | .27 | PASS_1_COMPLETE; T3-CONT; no finding |
| S360 | [DOC-004 p7 eTable 3 PSV, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | 7.45 (7.40–7.48) | 7.45 (7.41–7.49) | .42 | PASS_1_COMPLETE; T3-CONT; no finding |
| S361 | [DOC-004 p7 eTable 3 PSV, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | 18/97 (18.6) | 8/65 (12.3) | .29 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S362 | [DOC-004 p7 eTable 3 PSV, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | 6/221 (2.7) | 6/161 (3.8) | .57 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S363 | [DOC-004 p7 eTable 3 PSV, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | 2/204 (1.0) | 3/218 (1.4) | .70 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S364 | [DOC-004 p7 eTable 3 PSV, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | 2/180 (1.1) | 1/189 (0.5) | .53 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S365 | [DOC-004 p7 eTable 3 PSV, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | 25/97 (25.8) | 13/65 (20.0) | .40 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S366 | [DOC-004 p7 eTable 3 PSV, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | 18/221 (8.1) | 10/161 (6.2) | .47 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S367 | [DOC-004 p7 eTable 3 PSV, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | 17/204 (8.3) | 17/218 (7.8) | .84 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S368 | [DOC-004 p7 eTable 3 PSV, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | 9/180 (5.0) | 5/189 (2.6) | .24 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S369 | [DOC-004 p7 eTable 3 Other, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | 0.50 (0.40–0.60) | 0.50 (0.40–0.60) | .87 | PASS_1_COMPLETE; T3-CONT; no finding |
| S370 | [DOC-004 p7 eTable 3 Other, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | 0.35 (0.25–0.60) | 0.30 (0.25–0.50) | .50 | PASS_1_COMPLETE; T3-CONT; no finding |
| S371 | [DOC-004 p7 eTable 3 Other, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | 0.37 (0.26–0.48) | 0.50 (0.40–0.70) | .02 | PASS_1_COMPLETE; T3-CONT; no finding |
| S372 | [DOC-004 p7 eTable 3 Other, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | 0.35 (0.25–0.55) | 0.37 (0.30–0.45) | .66 | PASS_1_COMPLETE; T3-CONT; no finding |
| S373 | [DOC-004 p7 eTable 3 Other, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | 211 (156–273) | 219 (170–363) | .68 | PASS_1_COMPLETE; T3-CONT; no finding |
| S374 | [DOC-004 p7 eTable 3 Other, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | 239 (153–349) | 270 (135–334) | .90 | PASS_1_COMPLETE; T3-CONT; no finding |
| S375 | [DOC-004 p7 eTable 3 Other, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | 244 (135–368) | 157 (108–272) | .07 | PASS_1_COMPLETE; T3-CONT; no finding |
| S376 | [DOC-004 p7 eTable 3 Other, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | 225 (157–277) | 219 (164–292) | .75 | PASS_1_COMPLETE; T3-CONT; no finding |
| S377 | [DOC-004 p7 eTable 3 Other, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | 43.9 (37.3–48.7) | 39.7 (33.7–42.9) | .08 | PASS_1_COMPLETE; T3-CONT; no finding |
| S378 | [DOC-004 p7 eTable 3 Other, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | 36.0 (33.7–40.5) | 38.2 (30.4–42.4) | .72 | PASS_1_COMPLETE; T3-CONT; no finding |
| S379 | [DOC-004 p7 eTable 3 Other, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | 40.5 (36.4–44.6) | 38.6 (33.9–41.7) | .26 | PASS_1_COMPLETE; T3-CONT; no finding |
| S380 | [DOC-004 p7 eTable 3 Other, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | 36.0 (33.7–39.4) | 39.0 (35.2–45.0) | .33 | PASS_1_COMPLETE; T3-CONT; no finding |
| S381 | [DOC-004 p7 eTable 3 Other, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | 7.32 (7.27–7.37) | 7.38 (7.30–7.42) | .12 | PASS_1_COMPLETE; T3-CONT; no finding |
| S382 | [DOC-004 p7 eTable 3 Other, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | 7.37 (7.32–7.41) | 7.45 (7.38–7.48) | .02 | PASS_1_COMPLETE; T3-CONT; no finding |
| S383 | [DOC-004 p7 eTable 3 Other, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | 7.39 (7.36–7.41) | 7.44 (7.37–7.47) | .26 | PASS_1_COMPLETE; T3-CONT; no finding |
| S384 | [DOC-004 p7 eTable 3 Other, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | 7.41 (7.36–7.49) | 7.46 (7.42–7.49) | .31 | PASS_1_COMPLETE; T3-CONT; no finding |
| S385 | [DOC-004 p7 eTable 3 Other, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | 4/20 (20.0) | 5/20 (25.0) | .99 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S386 | [DOC-004 p7 eTable 3 Other, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | 1/25 (4.0) | 0/19 (0.0) | .99 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S387 | [DOC-004 p7 eTable 3 Other, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | 0/18 (0.0) | 0/18 (0.0) | — | PASS_1_COMPLETE; T3-COUNT; no finding |
| S388 | [DOC-004 p7 eTable 3 Other, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | 2/11 (18.2) | 0/17 (0.0) | .15 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S389 | [DOC-004 p7 eTable 3 Other, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | 7/20 (35.) | 3/20 (15.0) | .27 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S390 | [DOC-004 p7 eTable 3 Other, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | 3/25 (12.0) | 1/19 (5.3) | .62 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S391 | [DOC-004 p7 eTable 3 Other, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | 3/18 (16.7) | 2/18 (11.1) | .99 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S392 | [DOC-004 p7 eTable 3 Other, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | 2/11 (18.2) | 1/17 (5.9) | .54 | PASS_1_COMPLETE; T3-COUNT; no finding |
| S393 | [DOC-004 p8 eTable 4 Sedative infusion](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 320 (70.6) | 333 (72.1) | .63 | PASS_1_COMPLETE; T4-HEADER_PRECISION; no finding |
| S394 | [DOC-004 p8 eTable 4 Days sedative administration](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 0.6 (0.3–1.5) | 0.6 (0.0–1.5) | .76 | PASS_1_COMPLETE; T4-IQR; no finding |
| S395 | [DOC-004 p8 eTable 4 Analgesic infusion](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 277 (61.1) | 273 (59.1) | .53 | PASS_1_COMPLETE; T4-HEADER_PRECISION; no finding |
| S396 | [DOC-004 p8 eTable 4 Days analgesic administration](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 0.7 (0.3–2.0) | 0.7 (0.4–2.0) | .65 | PASS_1_COMPLETE; T4-IQR; no finding |
| S397 | [DOC-004 p8 eTable 4 Lowest RASS day 1](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | −4 (−5 to−3) | −4 (−5 to−3) | .58 | PASS_1_COMPLETE; T4-IQR; no finding |
| S398 | [DOC-004 p8 eTable 4 Lowest RASS day 2](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | −4 (−4 to−1) | −3 (−4 to−1) | .17 | PASS_1_COMPLETE; T4-IQR; no finding |
| S399 | [DOC-004 p8 eTable 4 Lowest RASS day 3](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | −3 (−4 to−1) | −3 (−4 to−1) | .01 | PASS_1_COMPLETE; T4-IQR; no finding |
| S400 | [DOC-004 p8 eTable 4 Neuromuscular blockade](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 53 (11.7) | 60 (13.0) | .55 | PASS_1_COMPLETE; T4-HEADER_PRECISION; no finding |
| S401 | [DOC-004 p8 eTable 4 Days neuromuscular blockade](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 0.0 (0.0–0.3) | 0.0 (0.0–0.3) | .55 | PASS_1_COMPLETE; T4-IQR; no finding |
| S402 | [DOC-004 p8 eTable 4 Fluid balance 24h day 1 mL](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 1225 (−18–2471) | 1310 (108–2632) | .42 | PASS_1_COMPLETE; T4-IQR; no finding |
| S403 | [DOC-004 p8 eTable 4 Fluid balance 24h day 2 mL](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 259 (−869–1288) | 167 (−998–1203) | .59 | PASS_1_COMPLETE; T4-IQR; no finding |
| S404 | [DOC-004 p8 eTable 4 Fluid balance 24h day 3 mL](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | −278 (−1619–570) | −530 (−1932–641) | .39 | PASS_1_COMPLETE; T4-IQR; no finding |
| S405 | [DOC-004 p8 eTable 4 Use colloids](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 100/454 (22.0) | 107/464 (23.1) | .71 | PASS_1_COMPLETE; T4-COUNT; no finding |
| S406 | [DOC-004 p8 eTable 4 Volume colloids](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 0 (0–0) | 0 (0–0) | .97 | PASS_1_COMPLETE; T4-IQR; no finding |
| S407 | [DOC-004 p8 eTable 4 Volume crystalloids](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 6892 (3531–10643) | 7161 (3828–11054) | .50 | PASS_1_COMPLETE; T4-IQR; no finding |
| S408 | [DOC-004 p8 eTable 4 Transfusion red blood cells](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 129/454 (28.4) | 121/464 (26.1) | .43 | PASS_1_COMPLETE; T4-COUNT; no finding |
| S409 | [DOC-004 p8 eTable 4 Units red blood cells](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 0 (0–1) | 0 (0–1) | .50 | PASS_1_COMPLETE; T4-IQR; no finding |
| S410 | [DOC-004 p8 eTable 4 Transfusion fresh frozen plasma](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 30/454 (6.6) | 40/464 (8.6) | .25 | PASS_1_COMPLETE; T4-COUNT; no finding |
| S411 | [DOC-004 p8 eTable 4 Units fresh frozen plasma](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 0 (0–0) | 0 (0–0) | .24 | PASS_1_COMPLETE; T4-IQR; no finding |
| S412 | [DOC-004 p8 eTable 4 Transfusion platelets](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 48/454 (10.6) | 39/464 (8.4) | .26 | PASS_1_COMPLETE; T4-COUNT; no finding |
| S413 | [DOC-004 p8 eTable 4 Units platelets](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 0 (0–0) | 0 (0–0) | .26 | PASS_1_COMPLETE; T4-IQR; no finding |
| S414 | [DOC-004 p8 eTable 4 Use vasopressors](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 363 (80.0) | 353 (76.4) | .19 | PASS_1_COMPLETE; T4-HEADER_PRECISION; no finding |
| S415 | [DOC-004 p8 eTable 4 Days vasopressors](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 2 (1–4) | 2 (1–4) | .87 | PASS_1_COMPLETE; T4-IQR; no finding |
| S416 | [DOC-004 p8 eTable 4 Decreasing instrumental dead space](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 4 (0.8%) | 1 (0.2%) | .21 | PASS_1_COMPLETE; T4-COUNT_HEADER; no finding |
| S417 | [DOC-004 p8 eTable 4 Recruitment maneuvers](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 30 (6.3%) | 25 (5.2%) | .45 | PASS_1_COMPLETE; T4-COUNT_HEADER; no finding |
| S418 | [DOC-004 p8 eTable 4 Prone positioning](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 22 (4.6%) | 24 (5.0%) | .80 | PASS_1_COMPLETE; T4-COUNT_HEADER; no finding |
| S419 | [DOC-004 p8 eTable 4 Inhaled nitric oxide](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 1 (0.2%) | 1 (0.2%) | 1.00 | PASS_1_COMPLETE; T4-COUNT_HEADER; no finding |
| S420 | [DOC-004 p8 eTable 4 High frequency oscillatory ventilation](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 0 (0.0%) | 0 (0.0%) | NA | PASS_1_COMPLETE; T4-COUNT_HEADER; no finding |
| S421 | [DOC-004 p8 eTable 4 Extracorporeal membrane oxygenation](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 1 (0.2%) | 0 (0.0%) | .49 | PASS_1_COMPLETE; T4-COUNT_HEADER; no finding |
| S422 | [DOC-004 p8 eTable 4 Extracorporeal CO2 removal](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | 0 (0.0%) | 0 (0.0%) | NA | PASS_1_COMPLETE; T4-COUNT_HEADER; no finding |
| S423 | [DOC-004 p9 eTable 5 Pneumonia](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | 14.0 ± 11.4 | 13.1 ± 11.2 | MD 0.86 (−2.48,4.20); shared pair S423/S424 interaction P=.16 | PASS_1_COMPLETE; T5; no finding |
| S424 | [DOC-004 p9 eTable 5 Non-Pneumonia](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | 15.4 ± 11.6 | 16.0 ± 11.5 | MD −0.50 (−2.13,1.13); shared pair S423/S424 interaction P=.16 | PASS_1_COMPLETE; T5; no finding |
| S425 | [DOC-004 p9 eTable 5 Sepsis yes](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | 12.0 ± 11.7 | 14.2 ± 10.8 | MD −2.20 (−5.46,1.06); shared pair S425/S426 interaction P=.17 | PASS_1_COMPLETE; T5; no finding |
| S426 | [DOC-004 p9 eTable 5 Sepsis no](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | 16.0 ± 11.4 | 15.7 ± 11.6 | MD 0.25 (−1.38,1.89); shared pair S425/S426 interaction P=.17 | PASS_1_COMPLETE; T5; no finding |
| S427 | [DOC-004 p9 eTable 5 PaO2/FiO2 ≤200](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | 14.6 ± 11.5 | 15.5 ± 11.3 | MD −0.87 (−3.21,1.47); shared pair S427/S428 interaction P=.32 | PASS_1_COMPLETE; T5; no finding |
| S428 | [DOC-004 p9 eTable 5 PaO2/FiO2 >200](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | 15.7 ± 11.9 | 14.8 ± 11.8 | MD 0.87 (−1.62,3.36); shared pair S427/S428 interaction P=.32 | PASS_1_COMPLETE; T5; no finding |
| S429 | [DOC-004 p9 eTable 5 LIPS ≥4](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | 14.0 ± 11.4 | 14.2 ± 11.4 | MD −0.19 (−2.06,1.66); shared pair S429/S430 interaction P=.96 | PASS_1_COMPLETE; T5; no finding |
| S430 | [DOC-004 p9 eTable 5 LIPS <4](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | 17.0 ± 11.6 | 17.3 ± 11.3 | MD −0.27 (−2.61,2.07); shared pair S429/S430 interaction P=.96 | PASS_1_COMPLETE; T5; no finding |
| S431 | [DOC-004 p9 eTable 5 Admission clinical](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | 14.5 ± 11.7 | 15.2 ± 11.5 | MD −0.70 (−2.32,0.92); shared pair S431/S432 interaction P=.23 | PASS_1_COMPLETE; T5; no finding |
| S432 | [DOC-004 p9 eTable 5 Admission surgical](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | 18.7 ± 10.3 | 17.0 ± 11.1 | MD 1.70 (−1.62,5.03); shared pair S431/S432 interaction P=.23 | PASS_1_COMPLETE; T5; no finding |
| S433 | [DOC-004 p9 eTable 5 SAPS II ≥50](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | 12.0 ± 11.8 | 12.8 ± 11.9 | MD −0.88 (−2.96,1.18); shared pair S433/S434 interaction P=.26 | PASS_1_COMPLETE; T5; no finding |
| S434 | [DOC-004 p9 eTable 5 SAPS II <50](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | 19.5 ± 9.7 | 18.8 ± 10.0 | MD 0.75 (−1.14,2.64); shared pair S433/S434 interaction P=.26 | PASS_1_COMPLETE; T5; no finding |
| S435 | [DOC-004 p9 eTable 5 Pre-randomization ventilation numerical line 1; duration label displaced](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | 16.5 ± 11.6 | 16.8 ± 10.7 | MD −0.29 (−7.04,6.45); shared pair S435/S436 interaction P=.98 | PASS_1_COMPLETE; T5; F-ST1-501 label-to-number mapping |
| S436 | [DOC-004 p9 eTable 5 Pre-randomization ventilation numerical line 2; printed beside >6 h](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | 15.2 ± 11.6 | 15.4 ± 11.5 | MD −0.21 (−1.72,1.28); shared pair S435/S436 interaction P=.98 | PASS_1_COMPLETE; T5; F-ST1-501 label-to-number mapping |
| S437 | [DOC-004 p9 eTable 5 Start ventilation ICU](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | 12.7 ± 11.2 | 15.2 ± 11.0 | MD −2.50 (−4.63,−0.36); shared pair S437/S438 interaction P=.01 | PASS_1_COMPLETE; T5; no finding |
| S438 | [DOC-004 p9 eTable 5 Start ventilation outside ICU](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | 17.2 ± 11.5 | 15.8 ± 11.8 | MD 1.45 (−0.52,3.43); shared pair S437/S438 interaction P=.01 | PASS_1_COMPLETE; T5; no finding |

## Diagnostic pair checks and non-inference boundary

For navigation only, using SE≈CI width/3.92 and SE(interaction)≈sqrt(SE1²+SE2²) **under an additional independence and common normal-interval convention**, two-sided normal diagnostic P values are approximately pneumonia .473; sepsis .188; oxygenation .318; LIPS .958; admission .203; SAPS .255; prerandomization ventilation .982; ICU start .0077. These are not reported-analysis reconstructions. Pair dependence, CI-versus-GLM mapping, degrees of freedom and variance estimator are not given. In particular pneumonia P=.16 is preserved and passed to pass 2 with named missing definitions; a hypothetical independent contrast does not alone reproduce an interval-versus-test conflict. Neither pneumonia CI excludes zero, and .16 is nonsignificant; no individual-significance conflict exists. Other diagnostic-to-printed differences likewise do not establish a reproducing method for the whole display.

## Scope closure and limitations

118/118 assigned relationships marked PASS_1_COMPLETE. One source-layout finding F-ST1-501, four excluded apparent-observation rows. All assigned cells/definitions visually read; no extraction gap. Source limitations are missing subgroup n and exact inferential mappings, and unreported row-specific tests for median/IQR tables. These limits prohibit invented statistical reconstruction; they do not omit relationships. Counts, denominators, interval order, point containment, contrast direction, P attribution, stated two-sided alpha/multiplicity and applicable method logic were inspected for every tuple. Planned-versus-reported family-level analyses are outside this disjoint shard and remain with the coordinator's plan lane.

