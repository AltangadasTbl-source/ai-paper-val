# Numeric Consistency Check

## Scope, evidence rule, and result

This checker reviewed every relationship N001-N034 in `relationships/numeric_relationship_inventory.md` across the current-run main and support maps. It applied arithmetic, row/column and subgroup totals, numerator/denominator/percentage, missingness and population identity, rounding, measure/label/scale/unit/reference-group, rate/risk/proportion/person-time/count, and repeated-value checks whenever the source supplied compatible inputs. The direct PDFs are the authority. This is a checker record, not a stable candidate ledger: local observations `NC-001` through `NC-004` have no `C` ID, no severity, no validity decision, and no disposition.

## Candidate observations requiring human adjudication

### NC-001 — Quality-of-life pooled CI upper limit differs across matched main-paper locations

- **Relationships:** N011; MS005.
- **Exact source locations:** DOC-001, `jama_wilson_2020_oi_190154.pdf`, PDF p. 5 Figure 4; PDF p. 5 narrative; PDF p. 1 abstract.
- **Printed inputs:** Figure 4 prints overall SMD 0.16 (95% CI, -0.06 to **0.38**) for BPAP versus no device, 9 studies/833 patients. The p. 5 narrative and p. 1 abstract print the otherwise matched SMD 0.16 (95% CI, -0.06 to **0.39**), likewise 9 studies/833 patients.
- **Rule and reproducible calculation:** Match population (BPAP/no device), outcome (quality of life), summary measure (SMD), study count, and patient total. Compare the printed endpoints: `0.39 - 0.38 = 0.01`.
- **Tolerance:** Both endpoints are printed to two decimals. Under ordinary nearest-0.01 display, the intervals represented by 0.38 and 0.39 are adjacent and do not overlap except at a rounding boundary; the printed discrepancy is one final displayed unit. A source-specific alternate rounding convention is not stated.
- **Direct observation versus inference:** Direct observation is the 0.38/0.39 difference at matched locations. The conclusion that it is a reporting-consistency issue is an inference from the matched identifiers; it does not establish which endpoint is intended.
- **Source-grounded alternatives:** A pooled value may have been rounded/exported differently for the figure and narrative, including a boundary-case rounding difference; the package does not identify separate populations or models.
- **Quality-control relevance:** An evidence extractor could copy different CI limits for the same pooled SMD, affecting interval-based evidence tables or computational checks.
- **Exact human question:** Which upper 95% CI limit, 0.38 or 0.39, is the intended reported value for the BPAP/no-device quality-of-life meta-analysis, and was a different rounding/export rule deliberately used?

### NC-002 — HMV mortality P value does not reconcile with the printed effect and interval under the stated two-sided convention

- **Relationships:** N005; MS002.
- **Exact source locations:** DOC-001, `jama_wilson_2020_oi_190154.pdf`, PDF p. 1 abstract; PDF p. 4 Figure 1; PDF p. 6 Table 1/text.
- **Printed inputs:** The abstract and Table 1/text print HMV/no-device mortality OR 0.56 (95% CI, 0.29-1.08), P = .49, 2 studies/175 patients; percentages are 21.84% versus 34.09%. Figure 1 prints the same pooled OR/CI and separately labels `Subtotal (I2 = 84.3%; P = .01)`, where the figure label makes that P the heterogeneity P rather than the pooled-effect P. DOC-001 p. 3 states two-tailed P < .05 as the significance convention.
- **Rule and reproducible calculation:** Use the conventional normal approximation from a log effect and its displayed 95% CI: `log(0.56) = -0.5798`; `SE ≈ [log(1.08)-log(0.29)] / (2 × 1.96) = 0.3355`; `z ≈ -0.5798 / 0.3355 = -1.73`; two-sided `P ≈ 0.084`. As a compatible diagnostic from the displayed RD, `-11.99 / [((0.79)-(-24.77))/(2×1.96)] ≈ -1.84`, giving P about .066. Neither diagnostic approaches .49.
- **Tolerance:** The OR and CI are displayed to two decimals, so the diagnostic is deliberately approximate; allowing endpoint rounding and normal-approximation variation gives a broad diagnostic band roughly P .05-.12, not .49. This is not a claim that the diagnostic substitutes for the reported meta-analytic test.
- **Direct observation versus inference:** Directly observed: OR/CI/P values and the figure’s explicit heterogeneity-P label. Inference: the approximate P incompatibility under a standard two-sided effect-test relationship. The exact pooled-effect test, variance adjustment, and precision are not supplied.
- **Source-grounded alternatives:** P = .49 could concern another analysis/quantity, a different pooling/test convention, or a transcription error. The protocol describes variance adjustment rules, but the source does not identify the exact rule used for this two-study estimate or a separate P = .49 target.
- **Quality-control relevance:** A downstream evidence table may record an internally discordant significance value for the same effect estimate and CI.
- **Exact human question:** What exact test and analysis quantity produced P = .49 for HMV/no-device mortality, and does it correspond to the printed OR 0.56 (0.29-1.08) or should one reported inferential value be corrected?

### NC-003 — Quality-of-life standardized-direction statement conflicts with the Table 2 footnote

- **Relationships:** N011, N015, N020; MS042.
- **Exact source locations:** DOC-001, `jama_wilson_2020_oi_190154.pdf`, PDF p. 3 Methods; PDF p. 5 Figure 4; PDF p. 7 narrative; PDF p. 8 Table 2 footnote b. DOC-003, `joi190154supp2_prod.pdf`, PDF pp. 15 and 43-44 provide original-scale direction labels for context.
- **Printed inputs:** DOC-001 p. 3 says the authors standardized quality-of-life direction and used “higher scores to represent better outcomes.” Figure 4 on p. 5 labels negative SMDs “Favors NIPPV” and positive SMDs “Favors No NIPPV”; p. 7 describes the observational SMD 0.97 as “higher quality of life.” Table 2 footnote b on p. 8 says “Higher scores indicate worse quality of life.” DOC-003 p. 15 and eTable 10 show that original instruments have mixed directions (for example SGRQ higher=worse and SRIQ higher=better).
- **Rule and reproducible comparison:** The stated standardized higher-score direction, SMD sign under the group subtraction, figure favor labels, and table footnote must use one coherent polarity or explicitly distinguish contexts. The source does not state the subtraction order, and its higher=better and higher=worse statements have opposite polarity.
- **Tolerance:** No numerical rounding tolerance applies; this is a label/polarity comparison.
- **Direct observation versus inference:** Directly observed: the two contradictory global statements and the positive SMD narrative. Inference: absent an explicit qualification, the Table 2 footnote reverses the stated standardized scale direction. This does not assert that the underlying original instruments are mislabeled.
- **Source-grounded alternatives:** Table 2’s footnote may have intended to describe some original instruments rather than the standardized SMD direction, or it may be an overbroad generic footnote. The supplement documents mixed original-scale directions, which makes that alternative plausible but does not reconcile the Table 2 wording.
- **Quality-control relevance:** A reviewer or data extractor may reverse the direction of the Table 2 quality-of-life subgroup results or misinterpret which direction favors NIPPV.
- **Exact human question:** What sign transformations and group-subtraction order were used, and which Figure 4 favor labels and Table 2 direction footnote were intended for the standardized SMDs?

### NC-004 — Cheung BPAP/CPAP effectiveness-table total differs from the matched baseline-table group total

- **Relationships:** N027; SS009.
- **Exact source locations:** DOC-003, `joi190154supp2_prod.pdf`, PDF p. 19 eTable 6, Cheung 2010 RCT row; PDF p. 43 eTable 10, BPAP versus CPAP exacerbation row.
- **Printed inputs:** eTable 6 p. 19 lists Cheung 2010 CPAP, 24 patients, and BPAP-ST, 23 patients: `24 + 23 = 47`. eTable 10 p. 43 lists the matched BPAP versus CPAP exacerbation comparison as `1 RCT17; 49 patients`, with 30.43% versus 53.85%, RD -0.23, and OR 0.38.
- **Rule and reproducible calculation:** Match author/year, RCT citation 17, intervention pair, and comparison. Compare displayed totals: `49 - (24 + 23) = 2` patients.
- **Tolerance:** Patient counts are integers, so no rounding tolerance applies to the 2-patient total difference. The outcome percentages are rounded and are not used to assert event counts or a unique alternative denominator.
- **Direct observation versus inference:** Directly observed: the eTable 6 group counts and eTable 10 49-patient label. Inference: the matching author/citation/intervention pair denotes the same study comparison. The source does not say whether effectiveness outcomes used a different analysis population.
- **Source-grounded alternatives:** eTable 10 may include two randomized participants omitted from the baseline display, or it may use a different outcome-analysis denominator; either table could also contain a reporting/transcription error. The percentage pair may be based on outcome-specific denominators, but no such denominator is printed.
- **Quality-control relevance:** The inconsistency affects the reported study total and could lead to an incorrect participant denominator in evidence extraction or meta-analysis review.
- **Exact human question:** Does the 49-patient effectiveness label include two participants not shown in the 24/23 baseline groups (and, if so, what is the stated analysis population), or is one table’s total incorrect?

## Checked relationships without a candidate observation

| Relationships | Applied rule and calculation or direct comparison | Result and limitation |
|---|---|---|
| N001, N025, N033 | `21 + 12 = 33`; country counts `4+1+23+3+1+1=33`; flow `6,222+83=6,305`; `6,305-5,204=1,101`; `1,101-1,034=67`; printed exclusions `257+4+156+66+114+37+154+23+117+18+54+16+17+1=1,034`. | PASS. Flow outputs have distinct labels (original studies, ongoing trials, guidelines, reviews) and are not addends to the 67 residual records. |
| N004 | Fig. 1 rows total BPAP `166/744=22.31%`, control `194/679=28.57%`; totals `744+679=1,423`; RD from unrounded risks is about -6.26 percentage points, whereas reported meta-analytic RD is -5.53%. | PASS for event/denominator and total. The RD is pooled/meta-analytic rather than a crude total-risk difference, so it need not equal the crude calculation. |
| N005 | HMV rows total `19/87=21.84%`, control `30/88=34.09%`; `87+88=175`. | PASS for counts, percentages, and total. The P-value issue is separately retained as NC-002. |
| N006 | BPAP/HMV denominators `1,423+175=1,598`; weighted/event-derived all-NIPPV percentages are not required to equal simple combination because p. 6 prints pooled estimates. | PASS for study/patient total. No unmatched same-measure value found. |
| N007-N009, N012, N016, N031-N032 | Compared labels `rate ratio`/`RR`, “per patient,” “number of admissions,” “number of patients,” and WMD. | PASS. The source distinguishes recurrent-event count/rate outcomes from patient risks; no conversion to a patient proportion or event count was made. |
| N010 | Fig. 3 totals `7/131=5.34%`, `20/136=14.71%`, `131+136=267`. | PASS. Reported RD is meta-analytic and differs permissibly from crude arithmetic. |
| N012-N014 | Checked Table 1 and subgroup labels against the Methods definition of OR/RD for binary outcomes, RR for count outcomes, and original units for distance/survival. | PASS. Some rows lack event numerators or a CI; the missing inputs preclude a stronger arithmetic reconstruction but are not a candidate by themselves. |
| N015 | Table 2 RCT/observational patient totals: mortality `985+613=1,598`; intubation `52+215=267`; admission count `243+176=419`; QOL `784+49=833`. | PASS for subgroup sums. Direction conflict is separately retained as NC-003. |
| N016 | Total, serious, and nonserious adverse-event incidences are separately pooled incidence estimates; `.21` need not equal a simple sum of `.00` and `.24`. `0.00` serious-event incidence is treated as finite-precision display, not a literal-zero candidate. | PASS; `DISPLAY_ZERO_NOT_CANDIDATE` retained for coverage. |
| N017-N019, N022-N024, N034 | Compared protocol/main eligibility, device labels, thresholds, usage units, and time frames only where the sources state a matching definition. | PASS. Protocol/method differences are not candidates unless they create a concrete reported-result inconsistency; none was shown. |
| N020, N028-N032 | Compared original-scale direction labels on DOC-003 pp. 15 and 43-44 with each outcome’s own label (SGRQ/CAT/MRC/ESS higher=worse; SRIQ higher=better; 6MWD meters). | PASS except the separate globally conflicting main-paper Table 2 statement (NC-003). Mixed original scale directions are expected and are not duplicated-value defects. |
| N021 | Compared serious-adverse-event category definition with main-paper statement that mortality, hospital admission, and intubation were primary outcomes and not rereported as serious adverse events. | PASS. This explains rather than conflicts with the separate adverse-event summaries. |
| N026 | `315+39,385=39,700`; `315+9,156=9,471` using the p. 32 baseline group counts cited by eTable 10’s observational comparison. | PASS. Exact totals reconcile. |
| N027 | Compared eTable 10’s rounded percentages and effect estimates with the stated 49 participants without deriving exact events. | No additional percentage candidate; outcome-specific denominators are not supplied. The concrete table-total difference is NC-004. |

## Counts and limitations

- **Relationships checked:** 34 of 34 canonical `N` relationships.
- **Distinct local candidate observations:** 4 (`NC-001` through `NC-004`).
- **Explicit checked non-candidate groups:** 14, covering the remaining relationships and the display-zero incidence notation.
- **Limitations:** Some meta-analytic RDs, RRs, and CIs are pooled rather than crude calculations; they were not falsely required to equal aggregated event totals. Exact model variance, effect-test method, and outcome-specific denominators are absent for some relationships. Those omissions constrain calculation precision but do not erase the directly printed mismatches recorded above.
