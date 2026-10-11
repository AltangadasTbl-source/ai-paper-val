# Mechanical evidence recheck

Assigned stable IDs: C001 and C002. Scope is the finalized ledger and initial screening log, with every affected repeated location. This record contains evidence facts and content-based classifications only. Both IDs remain Pending Human Adjudication.

QUALITY_CONTROL_SCOPE.md and the complete workflow_1_6_1/review_contract.md were read. Current-run ledger, initial screening and relevant F-NUM-001, F-XS-001, F-XS-002, F-ST1-001 and F-ST1-002 were used to define the assigned comparisons. Earlier review conclusions and external sources were not used.

## Source authority and tooling

Every cited page below was independently read from the supplied PDF using direct Poppler pdftotext 26.01.0 with -layout. Fresh direct Poppler pdftoppm source renders were visually inspected for main article pp.9–10, results supplement pp.20,29,42 and protocol p.31. Native extraction of results p.42 omits the plot: its exact headers and numbers were confirmed visually from the fresh render. Existing extraction and maps served as locators only. No OCR, fallback environment, source mutation, reused-artifact mutation or GPU was used.

Derivatives reside only in preprocessing/recheck/. Paths in this inventory are relative to review_1_6_1; all native derivatives use Poppler pdftotext -layout; all PNG derivatives use Poppler pdftoppm -singlefile -png, 130 dpi except results p.42 at 150 dpi.

| Direct supplied source and exact scope | Native derivative | Fresh rendered derivative |
|---|---|---|
| jama_bluth_2019_oi_190055_16092.pdf, PDF p.1 | preprocessing/recheck/main-p1.txt | Not needed: native text directly confirms abstract |
| jama_bluth_2019_oi_190055_16092.pdf, PDF p.4 | preprocessing/recheck/main-p4.txt | Not needed: native text directly confirms methods |
| jama_bluth_2019_oi_190055_16092.pdf, PDF pp.8–10 | preprocessing/recheck/main-p8-10.txt | preprocessing/recheck/main-p9.png; preprocessing/recheck/main-p10.png |
| joi190055supp4_prod_16092.pdf, PDF pp.20–21 | preprocessing/recheck/results-p20-21.txt | preprocessing/recheck/results-p20.png |
| joi190055supp4_prod_16092.pdf, PDF p.29 | preprocessing/recheck/results-p29.txt | preprocessing/recheck/results-p29.png |
| joi190055supp4_prod_16092.pdf, PDF p.42 | preprocessing/recheck/results-p42.txt | preprocessing/recheck/results-p42.png |
| joi190055supp1_prod_16092.pdf, PDF p.31 | preprocessing/recheck/protocol-p31.txt | preprocessing/recheck/protocol-p31.png |
| joi190055supp2_prod_16092.pdf, complete PDF pp.1–3 | preprocessing/recheck/amendments-p1-3.txt | Not needed: native text directly confirms complete amendment list |
| joi190055supp3_prod_16092.pdf, PDF pp.1–2 | preprocessing/recheck/sap-p1-2.txt | Not needed: native text directly confirms outcomes and methods |

The direct tool availability and versions agree with tooling_record.md. Numerical substitutions below were independently evaluated in JavaScript using the source-confirmed inputs; JavaScript did not select candidates or determine classifications.

## C001 — Binary effect-quantity identity

**Evidence state:** reproduced

**Determining recheck fact:** Source Table 3 and the abstract directly label 0.93 (0.83–1.04) as the primary risk ratio for 211/989 versus 233/987. The incidence ratio from those printed probabilities is 0.903748096; its conservative input-bound interval is 0.898765734–0.908757159, disjoint from 0.925–0.935. The fresh source render of eFigure 12 directly prints the same primary vector under Odds Ratio (95% CI). These registered comparisons remain after exact source reading; no registered value or location needed a transcription change.

### Locations found, printed inputs matched and comparator matched

All rows in the following location table were found. The row-level calculation tables below enumerate all 33 main binary rows, all 11 forest rows and all 13 per-protocol corroborating rows, including rows that do not independently establish a disparity.

| Location and content-based role | Direct source printed content matched | Comparator matched and role in comparison |
|---|---|---|
| REPORT [main abstract, PDF p.1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1) | Primary five-day PPC 211/989 (21.3%) versus 233/987 (23.6%); difference −2.3 (−5.9,1.4); risk ratio 0.93 (0.83,1.04); P=.23. Abstract hypoxemia 5.0% versus 13.6%, difference −8.6, P<.001. | Same primary counts/vector in Table 3 and Figure 2; source denominators define the empirical incidence contrast. Hypoxemia counts and ratio are supplied in Table 3. |
| REPORT [Statistical Analysis, PDF p.4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4) | Primary effect estimated with RRs/95% CIs and Wald likelihood ratio approximation; chi-square test; primary alpha .044. Other binary outcomes use the same RR/interval/test description. Site-random-effect primary mixed model is separately described as sensitivity analysis; binomial treatment-by-subgroup model describes interaction tests. | Matched Table 3 footnotes b/c and Figure 2 RR heading. The separately specified adjusted sensitivity and Cox analyses are preserved as different analyses. |
| REPORT [primary/component narrative, PDF p.8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8) | Primary 211/233, RR 0.93 (0.83–1.04), P=.23; mild respiratory failure 135/154, RR 0.92 (0.80–1.05), P=.22; pleural effusion 43/21, RR 1.35 (1.14–1.62), P=.005. | Exactly matches those three Table 3 rows, reference totals 989/987 and their ratio labels. |
| REPORT [Table 3, PDF p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) | Header High n=989 / Low n=987; Risk Ratio (95% CI). All 31 binary ratio rows, their counts, intervals and P values are transcribed below and matched visually. | Each empirical H incidence divided by L incidence, with shared reference totals; ratio point display precision. Equal-event and sparse rows are retained without requiring an independent disparity in each. |
| REPORT [Table 3 continuation and Figure 2, PDF p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) | Rescue 59/166, RR 0.49 (0.39–0.62), P<.001; vasoactive 491/439, RR 1.10 (1.01–1.21), P=.02. Footnote a defines reference patients; b states ratios unless otherwise indicated and Wald likelihood ratio approximation; c chi-square. All 11 Figure 2 count/denominator/ratio vectors matched below. | Shared denominators and incidence contrast for the two continuation rows; exact within-stratum counts/denominators for forest diagnostics. Figure heading, column and horizontal axis all say Risk Ratio. |
| REPORT [eTable 8 per-protocol, PDF p.29](../../../joi190055supp4_prod_16092.pdf#page=29) | H n=917 / L n=912; generic Effect Estimate 95% CI. All 13 count/denominator/estimate/CI/P vectors matched below. | Same diagnostic pattern within the named PP population. The generic header does not independently establish an RR label, and PP results are not compared numerically with the different ITT population. |
| REPORT [eFigure 12, PDF p.42](../../../joi190055supp4_prod_16092.pdf#page=42) | Fresh source image: Global Tests; Odds Ratio (95% CI); Collapsed Composite 0.93 [0.83,1.04]. The upper component block separately says Risk Ratio (99.58% CI). | Exact primary estimate/95% interval triple under main RR headings. Other global rows have Count (Proportional Odds), Common Effect GEE and Average Relative Effect GEE names; these model-based effects are not forced to equal crude ratios. |
| PLAN [final SAP primary and secondary methods, PDF p.2](../../../joi190055supp3_prod_16092.pdf#page=2) | Prospectively finalized SAP: effects on incidence of PPC estimated with risk ratio/95% CI and chi-square; same incidence wording for binary secondary outcomes. | Corroborates one side of the report comparison. It is not a conflicting comparator and adds no P_R relationship. |

### Applicable consistency rule and reproduced calculation

The applicable rule is identity of the declared intervention incidence risk ratio and clarity of the effect measure assigned to the matched primary vector. For exact source events a in H total n and c in L total m, the empirical incidence comparison is (a/n)/(c/m). The source identifies the groups, populations, first-five-day primary outcome and reference totals. No explicitly adjusted, mixed, GEE, proportional-odds or time-to-event effect is required to equal this empirical ratio.

Integer event and reference-patient counts are exact counts, not rounded continuous estimates. As an additional conservative display check, the table permits every positive count and total its artificial ±0.5 interval. A printed two-decimal ratio q is permitted q±0.005. The conservative RR endpoints are ((a−0.5)/(n+0.5))/((c+0.5)/(m−0.5)) and ((a+0.5)/(n−0.5))/((c−0.5)/(m+0.5)). At zero events, the count interval is restricted to nonnegative values; the exact incidence RR has a zero denominator and the conservative upper limit is unbounded. Closed intervals are used so boundary contact favors reconciliation. Bounds are displayed to six decimals; overlap decisions use unrounded arithmetic.

The diagnostic allocation contrast T is [a/(a+c)]/[(n−a)/(n−a+m−c)]. It is reproduced only to characterize the repeated numerical pattern. It is not an asserted author implementation, not a replacement result and not a basis for extending the issue to separately specified model-based results. Some T values differ from conventional final rounding of the printed estimates.

#### All 33 main binary rows

Source authority: [Table 3 p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) and [continuation p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10). Source headers and footnote a assign H/L totals 989/987 unless otherwise indicated. No local alternative denominator is printed for these rows.

| Exact source row | Source H / L events and totals | Printed estimate (95% CI); P | Empirical incidence RR | Conservative input-bound RR | Printed point half-unit interval | Bound comparison | Diagnostic allocation ratio T |
|---|---|---|---:|---|---|---|---:|
| Primary PPC; PDF p.9 | 211/989; 233/987 | 0.93 (0.83–1.04); .23 | 0.903748 | 0.898766–0.908757 | 0.925–0.935 | disjoint | 0.935791 |
| Mild respiratory failure; PDF p.9 | 135/989; 154/987 | 0.92 (0.80–1.05); .22 | 0.874851 | 0.867911–0.881843 | 0.915–0.925 | disjoint | 0.922769 |
| Moderate respiratory failure; PDF p.9 | 42/989; 58/987 | 0.83 (0.65–1.05); .10 | 0.722674 | 0.707251–0.738383 | 0.825–0.835 | disjoint | 0.832017 |
| Severe respiratory failure; PDF p.9 | 30/989; 36/987 | 0.90 (0.69–1.18); .45 | 0.831648 | 0.805769–0.858286 | 0.895–0.905 | disjoint | 0.905299 |
| Atelectasis; PDF p.9 | 44/989; 55/987 | 0.88 (0.70–1.10); .25 | 0.798382 | 0.781407–0.815688 | 0.875–0.885 | disjoint | 0.882775 |
| Pleural effusion; PDF p.9 | 43/989; 21/987 | 1.35 (1.14–1.62); .005 | 2.043478 | 1.970751–2.119805 | 1.345–1.355 | disjoint | 1.357955 |
| New pulmonary infiltrates; PDF p.9 | 14/989; 18/987 | 0.87 (0.59–1.29); .47 | 0.776205 | 0.727517–0.827733 | 0.865–0.875 | disjoint | 0.872308 |
| Cardiopulmonary edema; PDF p.9 | 17/989; 9/987 | 1.31 (0.99–1.74); .12 | 1.885069 | 1.731576–2.056741 | 1.305–1.315 | disjoint | 1.311728 |
| Bronchospasm; PDF p.9 | 12/989; 10/987 | 1.09 (0.74–1.60); .67 | 1.197573 | 1.091918–1.314458 | 1.085–1.095 | overlap | 1.090909 |
| Pulmonary infection; PDF p.9 | 10/989; 10/987 | 0.99 (0.64–1.55); >.99 | 0.997978 | 0.902019–1.104145 | 0.985–0.995 | overlap | 0.998979 |
| Aspiration pneumonitis; PDF p.9 | 2/989; 1/987 | 1.33 (0.60–2.97); >.99 | 1.995956 | 0.996968–4.994942 | 1.325–1.335 | overlap | 1.332658 |
| ARDS; PDF p.9 | 3/989; 1/987 | 1.50 (0.85–2.64); .62 | 2.993933 | 1.661614–6.992919 | 1.495–1.505 | disjoint | 1.500000 |
| Pneumothorax; PDF p.9 | 1/989; 3/987 | 0.50 (0.09–2.72); .37 | 0.332659 | 0.142424–0.599393 | 0.495–0.505 | overlap | 0.498988 |
| Severe PPC; PDF p.9 | 116/989; 134/987 | 0.91 (0.80–1.05); .22 | 0.863921 | 0.856133–0.871776 | 0.905–0.915 | disjoint | 0.917370 |
| Extrapulmonary composite; PDF p.9 | 167/989; 150/987 | 1.06 (0.95–1.19); .31 | 1.111082 | 1.102958–1.119268 | 1.055–1.065 | disjoint | 1.063241 |
| Systemic inflammatory response syndrome; PDF p.9 | 93/989; 83/987 | 1.06 (0.91–1.22); .44 | 1.118216 | 1.104426–1.132187 | 1.055–1.065 | disjoint | 1.061536 |
| Sepsis; PDF p.9 | 18/989; 15/987 | 1.09 (0.79–1.49); .60 | 1.197573 | 1.125609–1.274571 | 1.085–1.095 | disjoint | 1.091471 |
| Severe sepsis; PDF p.9 | 7/989; 10/987 | 0.82 (0.46–1.45); .46 | 0.698584 | 0.617171–0.788675 | 0.815–0.825 | disjoint | 0.821433 |
| Septic shock; PDF p.9 | 7/989; 8/987 | 0.93 (0.54–1.60); .79 | 0.873231 | 0.762387–0.998988 | 0.925–0.935 | overlap | 0.931908 |
| Gastrointestinal failure; PDF p.9 | 65/989; 56/987 | 1.07 (0.90–1.28); .40 | 1.158367 | 1.138132–1.178986 | 1.065–1.075 | disjoint | 1.078450 |
| Acute kidney failure; PDF p.9 | 31/989; 32/987 | 0.98 (0.76–1.26); .89 | 0.966791 | 0.935616–0.998988 | 0.975–0.985 | overlap | 0.982586 |
| Extrapulmonary infection; PDF p.9 | 29/989; 23/987 | 1.11 (0.87–1.42); .40 | 1.258320 | 1.209089–1.309785 | 1.105–1.115 | disjoint | 1.117708 |
| Hepatic failure; PDF p.9 | 9/989; 9/987 | 0.99 (0.63–1.59); >.99 | 0.997978 | 0.892024–1.116516 | 0.985–0.995 | overlap | 0.998980 |
| Coma; PDF p.9 | 2/989; 2/987 | 0.99 (0.37–2.66); >.99 | 0.997978 | 0.598181–1.664981 | 0.985–0.995 | overlap | 0.998987 |
| Disseminated intravascular coagulation; PDF p.9 | 1/989; 0/987 | 2.00 (1.91–2.09); >.99 | undefined / ∞ | 0.996968–undefined / ∞ | 1.995–2.005 | overlap | 1.998988 |
| Impaired postoperative wound healing; PDF p.9 | 22/989; 26/987 | 0.91 (0.66–1.24); .55 | 0.844443 | 0.808861–0.881460 | 0.905–0.915 | disjoint | 0.913823 |
| Unexpected ICU admission/readmission; PDF p.9 | 41/989; 32/987 | 1.12 (0.91–1.38); .29 | 1.278659 | 1.242376–1.316128 | 1.115–1.125 | disjoint | 1.127435 |
| Hypoxemia; PDF p.9 | 49/989; 134/987 | 0.51 (0.40–0.65); <.001 | 0.364932 | 0.359502–0.370411 | 0.505–0.515 | disjoint | 0.510737 |
| Hypotension; PDF p.9 | 313/989; 170/987 | 1.43 (1.31–1.56); <.001 | 1.837453 | 1.827288–1.847686 | 1.425–1.435 | disjoint | 1.431233 |
| Bradycardia; PDF p.9 | 98/989; 59/987 | 1.27 (1.11–1.45); .001 | 1.657658 | 1.633687–1.682057 | 1.265–1.275 | disjoint | 1.274329 |
| In-hospital mortality; PDF p.9 | 12/989; 5/987 | 1.41 (0.95–1.81); .09 | 2.395147 | 2.084570–2.774968 | 1.405–1.415 | disjoint | 1.415377 |
| Rescue strategy for desaturation; PDF p.10 | 59/989; 166/987 | 0.49 (0.39–0.62); <.001 | 0.354703 | 0.350286–0.359153 | 0.485–0.495 | disjoint | 0.493711 |
| Need for vasoactive drugs; PDF p.10 | 491/989; 439/987 | 1.10 (1.01–1.21); .02 | 1.116189 | 1.112657–1.119733 | 1.095–1.105 | disjoint | 1.108922 |

Twenty-four of the 33 rows have disjoint conservative intervals. The remaining nine rows have overlap under the deliberately broadened input intervals; they are common-block occurrences, not nine additional numerical contradictions. Pulmonary infection, hepatic failure and coma have equal event counts and do not independently establish the registered pattern. The DIC exact incidence ratio is undefined because the L count is zero; its conservative nonnegative-input interval overlaps the finite printed point. No interval-versus-P inversion is assumed.

The printed hospital-free-day mean difference and five-day mortality HR have explicit exceptions and are outside this repeated binary ratio block. Acute myocardial infarction has no printed ratio. Graded gastrointestinal/renal distributions are nested classification rows rather than additional binary ratio rows.

#### All 11 Figure 2 rows

Source authority: [Figure 2 PDF p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10). Subgroup RR labels and event/reference counts are direct observations. The described binomial interaction model supports interaction tests; its presence is not proof that a particular adjusted model produced the displayed subgroup point estimates. Calculations remain diagnostics of the displayed contrast identity, bounded by this missing estimator definition.

| Exact source row | Source H / L events and totals | Printed estimate (95% CI); P | Empirical incidence RR | Conservative input-bound RR | Printed point half-unit interval | Bound comparison | Diagnostic allocation ratio T |
|---|---|---|---:|---|---|---|---:|
| Nonlaparoscopic; PDF p.10 | 79/240; 74/253 | 1.09 (0.90–1.32); interaction block, listed below | 1.125394 | 1.106266–1.144860 | 1.085–1.095 | disjoint | 1.090407 |
| Laparoscopic; PDF p.10 | 130/740; 156/727 | 0.88 (0.77–1.01); interaction block, listed below | 0.818694 | 0.811832–0.825610 | 0.875–0.885 | disjoint | 0.880030 |
| BMI <40; PDF p.10 | 76/336; 94/376 | 0.93 (0.77–1.13); interaction block, listed below | 0.904762 | 0.891538–0.918168 | 0.925–0.935 | disjoint | 0.931946 |
| BMI ≥40; PDF p.10 | 135/653; 139/611 | 0.94 (0.82–1.08); interaction block, listed below | 0.908755 | 0.900717–0.916865 | 0.935–0.945 | disjoint | 0.941648 |
| SpO2 <96%; PDF p.10 | 88/317; 112/342 | 0.88 (0.74–1.06); interaction block, listed below | 0.847679 | 0.836570–0.858925 | 0.875–0.885 | disjoint | 0.881921 |
| SpO2 ≥96%; PDF p.10 | 123/672; 121/645 | 0.99 (0.86–1.13); interaction block, listed below | 0.975686 | 0.966252–0.985213 | 0.985–0.995 | overlap | 0.985241 |
| Peripheral incision; PDF p.10 | 32/126; 25/126 | 1.16 (0.89–1.53); interaction block, listed below | 1.280000 | 1.225529–1.337101 | 1.155–1.165 | disjoint | 1.164614 |
| Upper abdominal incision; PDF p.10 | 179/863; 208/861 | 0.90 (0.80–1.02); interaction block, listed below | 0.858583 | 0.853141–0.864057 | 0.895–0.905 | disjoint | 0.904102 |
| Waist-to-hip <1; PDF p.10 | 97/467; 100/457 | 0.97 (0.83–1.13); interaction block, listed below | 0.949229 | 0.937606–0.960995 | 0.965–0.975 | disjoint | 0.967472 |
| Waist-to-hip ≥1; PDF p.10 | 98/447; 112/449 | 0.92 (0.78–1.08); interaction block, listed below | 0.878915 | 0.868603–0.889344 | 0.915–0.925 | disjoint | 0.917287 |
| All patients; PDF p.10 | 211/989; 233/987 | 0.93 (0.83–1.04); interaction block, listed below | 0.903748 | 0.898766–0.908757 | 0.925–0.935 | disjoint | 0.935791 |

Ten of 11 forest rows have disjoint conservative intervals. The SpO2 ≥96% row has overlap under conservative inputs and is recorded as an occurrence. Printed interaction P values are .08 (type of surgery), .97 (BMI), .35 (SpO2), .11 (incision) and .65 (waist-to-hip). All were matched to the exact source; they are not individual-stratum P values and were not recomputed as such.

#### All 13 per-protocol corroborating rows

Source authority: [eTable 8 PDF p.29](../../../joi190055supp4_prod_16092.pdf#page=29). The effect column is generic. These rows provide corroborating numerical observations rather than independent explicit-RR contradictions.

| Exact source row | Source H / L events and totals | Printed estimate (95% CI); P | Empirical incidence RR | Conservative input-bound RR | Printed point half-unit interval | Bound comparison | Diagnostic allocation ratio T |
|---|---|---|---:|---|---|---|---:|
| Primary PPC; PDF p.29 | 186/917; 209/912 | 0.92 (0.82–1.04); .17 | 0.885100 | 0.879651–0.890580 | 0.915–0.925 | disjoint | 0.923735 |
| Mild respiratory failure; PDF p.29 | 119/917; 140/912 | 0.90 (0.78–1.04); .15 | 0.845365 | 0.837901–0.852892 | 0.895–0.905 | disjoint | 0.903949 |
| Moderate respiratory failure; PDF p.29 | 38/917; 51/912 | 0.84 (0.66–1.07); .15 | 0.741035 | 0.723394–0.759049 | 0.835–0.845 | disjoint | 0.845189 |
| Severe respiratory failure; PDF p.29 | 25/917; 35/912 | 0.83 (0.61–1.11); .18 | 0.710391 | 0.685628–0.735905 | 0.825–0.835 | disjoint | 0.826327 |
| ARDS; PDF p.29 | 3/917; 1/912 | 1.50 (0.84–2.64); .62 | 2.983642 | 1.655767–6.969449 | 1.495–1.505 | disjoint | 1.497538 |
| Bronchospasm; PDF p.29 | 11/917; 10/912 | 1.04 (0.69–1.57); .84 | 1.094002 | 0.993460–1.205243 | 1.035–1.045 | overlap | 1.045306 |
| New pulmonary infiltrates; PDF p.29 | 14/917; 14/912 | 0.99 (0.68–1.44); .99 | 0.994547 | 0.924946–1.069386 | 0.985–0.995 | overlap | 0.997231 |
| Pulmonary infection; PDF p.29 | 10/917; 9/912 | 1.05 (0.68–1.61); .83 | 1.105053 | 0.993460–1.229903 | 1.045–1.055 | overlap | 1.050310 |
| Aspiration pneumonitis; PDF p.29 | 2/917; 1/912 | 1.33 (0.59–2.96); 1.00 | 1.989095 | 0.993460–4.978178 | 1.325–1.335 | overlap | 1.330419 |
| Pleural effusion; PDF p.29 | 38/917; 18/912 | 1.37 (1.14–1.65); .01 | 2.099600 | 2.013771–2.190398 | 1.365–1.375 | disjoint | 1.368723 |
| Atelectasis; PDF p.29 | 38/917; 50/912 | 0.85 (0.67–1.09); .18 | 0.755856 | 0.737718–0.774383 | 0.845–0.855 | disjoint | 0.855285 |
| Cardiopulmonary edema; PDF p.29 | 15/917; 7/912 | 1.36 (1.02–1.82); .09 | 2.131173 | 1.920690–2.374208 | 1.355–1.365 | disjoint | 1.365904 |
| Pneumothorax; PDF p.29 | 1/917; 2/912 | 0.66 (0.13–3.29); .62 | 0.497274 | 0.198692–0.995636 | 0.655–0.665 | overlap | 0.664483 |

Eight of 13 PP rows have disjoint conservative intervals if the generic effect were interpreted as an empirical incidence RR. Five have overlap. This conditional identity calculation does not silently supply the missing effect-measure definition.

#### Primary-vector label and precision check

Main abstract, narrative, Table 3 and Figure 2 each print RR 0.93 (0.83–1.04). The eFigure 12 global collapsed-composite row prints 0.93 [0.83,1.04] under Odds Ratio (95% CI). Point display interval 0.925–0.935 and endpoint intervals 0.825–0.835 / 1.035–1.045 are identical across these locations. Thus there is no numerical between-document discrepancy in that triple; the source difference is its explicit measure identity. Display precision cannot decide whether this is a repeated RR under the global OR header or a separately estimated OR.

For orientation only, the primary crude treatment OR is 211×754/(778×233)=0.877643788, and primary T=0.935790546. Neither assigns the reported quantity. The original reported P=.23, two-sided primary alpha .044 and no-reduction conclusion are recorded separately from effect magnitude/scale. Exact chi-square options and interval implementation are unavailable; this recheck does not claim a P-value/CI inversion failure or a changed primary significance conclusion.

### Necessary inputs available; exact missing inputs or definitions

Available: direct primary and all repeated-row events/totals, populations, binary method text, explicit exceptions, source estimates/intervals/P values, main RR headers, supplementary OR header and exact matched primary triple. These are sufficient for the declared probability contrast and label comparisons, including interval arithmetic.

Missing: analysis code; exact binary estimator and denominator orientation; any unreported adjustment or transformation used for the main ratios; exact CI algorithm/options behind the named Wald likelihood ratio approximation; the estimator producing forest point estimates rather than interaction tests; PP row-specific effect measure/estimator; eFigure 12 collapsed-composite row-specific model/link/contrast and proof of whether it reproduces the main incidence result or a separate odds result. These gaps bound explanation and reconstruction; they do not erase the observed source values and labels.

### Source-grounded alternative interpretation

The source-described incidence RR may have been estimated through an unreported procedure; a different two-by-two orientation may explain the observed pattern; the PP generic column may follow the same or a separate estimator; the collapsed-composite row may repeat the main vector under the global header or may contain a separately estimated OR. The separately described site-adjusted/GEE/count analyses are alternatives for their own rows, but the package does not establish that one defines these main vectors. No alternative is selected.

### Direct observation versus inferred explanation

Direct observations: all source values above; main incidence RR wording; generic PP wording; eFigure 12 OR heading; exact primary-vector repetition; empirical incidence calculations and conservative interval comparisons. Inferred explanations: the diagnostic transposed orientation, an unreported estimator, a shared-heading convention or a distinct coincident OR. No computation mechanism or intent is asserted.

### Content-based document roles and classification confirmation

**Review domain:** statistical_results
**Relationship type:** S_C
**All relationships:** S_C, S_W
**Compared document roles:** REPORT main article binary methods/results versus REPORT results supplement eFigure 12 primary collapsed-composite label; REPORT main article internal method/count/ratio comparisons.

Main article locations report completed-trial methods and results, hence REPORT. eTable 8 and eFigure 12 present completed-trial results, hence REPORT. Final SAP p.2 describes prospective analysis, hence PLAN. Main internal quantitative identity is S_W; the matched primary vector with conflicting explicit measure labels across two REPORT documents is S_C. S_C takes precedence over S_W. PLAN SAP corroboration is not a relationship. PP pattern corroboration does not independently add a conflict. The provisional ledger classification is confirmed; no role/type/domain change is required. The domain concerns estimates and method identity, rather than attribution of a result to a different endpoint.

**Classification ambiguity:** Whether eFigure 12 is copying the main vector or independently modeling it is unresolved, but either compared published location is REPORT. Its ambiguity does not support a PLAN relationship.

### Exact remaining human question

Which probability contrast, denominator orientation, estimator and CI computation produced the main Table 3/Figure 2 binary vectors and the PP vectors; and is eFigure 12's Collapsed Composite 0.93 [0.83,1.04] the main incidence RR or a separately estimated OR? Which effect measure and matching interval should accompany the primary vector in data extraction?

## C002 — Planned and reported respiratory-severity criteria

**Evidence state:** reproduced_after_transcription_correction

**Determining recheck fact:** Exact protocol p.31 retains oxygen-responsive mild failure without a flow limit and moderate failure as hypoxemia despite supplemental oxygen. Exact main footnote d retains response at no more than 2 L for mild and only above 2 L for moderate. The ledger's generalized statement that both sources use room-air hypoxemia for at least ten minutes must be narrowed: those qualifiers appear in protocol mild, while protocol moderate does not repeat them. After this comparator-transcription qualification, the registered oxygen-response/severity criterion difference remains. All source page assignments and reported counts are unchanged.

### Locations found, printed inputs matched and comparator matched

| Location and content-based role | Exact source value/text matched | Comparator or evidentiary function |
|---|---|---|
| PLAN [protocol version 2.6 Appendix iii, physical PDF p.31](../../../joi190055supp1_prod_16092.pdf#page=31), printed protocol page 30 | Mild: PaO2 <60 mmHg or SpO2 <90% in room air during at least 10 min, responding to supplemental oxygen, excluding hypoventilation; no oxygen-flow boundary. Moderate: PaO2 <60 mmHg or SpO2 <90% despite supplemental oxygen, excluding hypoventilation. Severe: need for noninvasive or invasive mechanical ventilation, excluding hypoventilation. | Prospective endpoint component criteria compared with completed-report criteria. Exact moderate text omits the room-air/ten-minute wording; that detail is retained rather than supplied from the neighboring mild definition. |
| REPORT [eMethods 2.8, physical PDF p.20](../../../joi190055supp4_prod_16092.pdf#page=20) | Mild: room-air PaO2 <60 or SpO2 <90% for at least ten minutes, responds to oxygen printed “= 2 L/min”. Moderate: same room-air abnormality, responding only to >2 L/min. Severe: noninvasive/invasive ventilation, excluding hypoventilation due to sedative agents. | Response-to-flow distinction matched against protocol response/persistence distinction. Fresh visual reading confirms the printed mild equals glyph; it is not an OCR substitution. Main footnote d supplies the explicit no-more-than-2 boundary. |
| REPORT [main Table 3 component/severe-composite rows, physical PDF p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) | H/L reference totals 989/987. Mild 135 (13.7%)/154 (15.6%); moderate 42 (4.2%)/58 (5.9%); severe respiratory failure 30 (3.0%)/36 (3.6%); severe PPC 116 (11.7%)/134 (13.6%). Primary PPC 211/233. | Exact named counts to which operational definitions attach. No alternate event count is computed. |
| REPORT [main Table 3 footnote d, physical PDF p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) | PaO2 <60 mmHg or SpO2 <90% after at least ten minutes of room air (beach chair), excluding hypoventilation. Response to 2 L or less oxygen defines mild; response only to greater than 2 L defines moderate. Severe requires noninvasive/invasive ventilation. | Direct explicit report comparator to protocol p.31; corroborates eMethods response/flow interpretation. |
| REPORT [eMethods severe-composite definition, physical PDF p.21](../../../joi190055supp4_prod_16092.pdf#page=21) | Severe PPC is any listed adverse pulmonary event except mild respiratory failure. | Establishes relevance of severity-category boundary to the severe-composite definition. |
| PLAN [final SAP section 1.1, physical PDF p.1](../../../joi190055supp3_prod_16092.pdf#page=1) | Primary collapsed composite within first five postoperative days; at least one event; mild/moderate/severe respiratory components defined elsewhere. Severe PPC excludes mild respiratory failure. | Corroborates endpoint/window and exclusion rule. It supplies no superseding flow criterion and is not itself a conflicting relationship. |
| PLAN [complete amendment list, physical PDF p.1](../../../joi190055supp2_prod_16092.pdf#page=1) | Version 2.4.1 changes steering committee, background wording, surgery inclusion wording and hepatic-failure definition; begins version 2.4.2 interim-analysis deletion. | Complete page read; no respiratory-severity criterion replacement appears. |
| PLAN [complete amendment list, physical PDF p.2](../../../joi190055supp2_prod_16092.pdf#page=2) | Completes interim deletion; analysis plan, adverse-event reporting, DSMB and visit updates; version 2.5 site/sample-size recalculation and interim reintroduction. | Complete page read; no respiratory-severity criterion replacement appears. |
| PLAN [complete amendment list, physical PDF p.3](../../../joi190055supp2_prod_16092.pdf#page=3) | Completes sequential-design change and DSMB addition; version 2.6 adds preoperative SpO2 after ten minutes room air supine when beach-chair SpO2 ≥92%. | Complete page read. The SpO2 collection-position amendment does not state a change to the mild/moderate oxygen-response criterion. |

### Applicable consistency rule and reproduced logical comparison

The applicable rule is coherence of the planned-versus-reported primary-component operational definition, including an explicit threshold that can change which severity category a component denotes. Oxygen response without a flow restriction and hypoxemia persisting despite oxygen are distinct criteria from separating responsive events at no more than versus more than 2 L.

A purely definitional example reproduces the boundary difference: consider a qualifying room-air abnormality that responds at 3 L/min but not at 2 L/min, without need for mechanical ventilation. Protocol mild permits it because response to supplemental oxygen has no flow limit; report moderate names it because response requires more than 2 L/min. This is a logical witness to different definitions, not an observation that such a patient existed. The protocol does not specify which supplemental-oxygen dose is used when assessing “despite”; that omission limits reconstruction of implementation.

Display-precision interval check: the source thresholds 60 mmHg, 90%, ten minutes and 2 L are operational cutoffs, not rounded estimates to be assigned arbitrary half-unit uncertainty. Even if a conservative ±0.5 L display interval were allowed around 2 L, a clearly responsive event at 3 L remains beyond the full 1.5–2.5 L range, while protocol mild still has no flow limit. No possible numerical rounding converts responsiveness into hypoxemia persisting despite oxygen. The event counts are exact integers and are not rival reported counts here; no count or percentage reconciliation is proposed.

The severe-composite rule excludes mild and includes other primary PPC components. The difference therefore concerns the definition accompanying mild 135/154, moderate 42/58 and severe-PPC 116/134. Both mild and moderate enter overall primary PPC; this evidence does not establish any changed overall primary incidence 211/233. Actual category or severe-composite membership changes cannot be computed from aggregate counts.

### Necessary inputs available; exact missing inputs or definitions

Available: exact protocol and report component text, clinical thresholds, report first-five-day component/window, Table 3 reference totals and associated event counts, severe-composite mild exclusion, final SAP outcome references, and all three supplied amendment pages. These suffice to compare operational criteria and identify which published definitions attach to the named results.

Missing: implemented case-report-form/data-dictionary severity fields, exact supplemental-oxygen dose and response assessment procedure for protocol “despite”, any further approved respiratory-definition amendment or operational manual, timing of any implemented refinement, patient-level oxygen-response/flow measurements and respiratory-category assignments, and overlap of respiratory components with other severe-composite events. These are required to establish implementation and quantify membership consequences.

### Source-grounded alternative interpretation

A later oxygen-flow refinement could have governed classification without being disclosed in the supplied amendment list; or protocol criteria could have governed collection while the report used a later summary convention. The final SAP explicitly refers to definitions elsewhere rather than providing a replacement definition. The package does not establish either interpretation, a protocol violation or any numerical consequence.

The supplementary mild “=2 L/min” and main “2 L or less” have different literal glyphs, but the main explicit boundary and complementary >2 category identify the report's intended flow distinction. This is recorded without creating a separate S_C relationship.

### Direct observation versus inferred explanation

Direct observations: exact protocol/report definitions; protocol moderate lacks the generalized room-air/ten-minute wording; actual printed eMethods equals glyph; reported component counts; severe-PPC excludes mild; final SAP refers elsewhere; complete supplied amendment list contains no respiratory-severity replacement. Direct logical result: response/flow and persistence-on-oxygen criteria are not identical.

Inferred explanations: an undisclosed operational refinement, summary convention, actual patient reclassification or altered severe-composite counts. None is established. The definitional example is an illustration of criterion non-equivalence, not a raw-data audit or incidence calculation.

### Content-based document roles and classification confirmation

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN protocol Appendix iii respiratory definitions versus REPORT main article Table 3 footnote d and REPORT results supplement eMethods 2.8.

Protocol Appendix iii defines prospective endpoint criteria and is PLAN. The amendment document records prospective approved plan versions and is PLAN. The final pre-analysis SAP is PLAN. Main Table 3 and eMethods describe completed-trial outcomes and definitions and are REPORT. The conflicting relationship is P_R; no plan-internal conflict is reproduced, so no P_P is added. The main and supplementary report descriptions corroborate one another in their oxygen-flow distinction and do not create an independent S_C conflict. Final SAP and amendment list are contextual evidence rather than new conflicting sides. The provisional ledger role/type/domain assignments are confirmed. Only the comparator transcription qualification requires an evidence-state update.

**Classification ambiguity:** A further supplied-to-investigators definition change might explain the difference, but it is not present in the supplied package. It does not change either document's role or establish a separate relationship.

### Exact remaining human question

Which operational oxygen-response criterion governed classification of mild and moderate respiratory failure: responsiveness without a stated flow limit and persistent hypoxemia despite oxygen, or responsiveness at ≤2 versus only >2 L/min? What case-report-form definition or approved amendment establishes that criterion, and which definition should accompany the published mild/moderate counts and severe-PPC composite? Patient-level evidence would be needed to determine any membership consequence.

## Coverage and remaining limits

Both assigned stable IDs are covered in full. C001 covers 33 main binary rows, 11 forest rows, 13 PP corroborating rows, all registered matching main narrative/method occurrences and the supplementary collapsed-composite label. C002 covers every registered definition, associated count, exclusion-rule, SAP and amendment location. All cited links use physical PDF pages. There is no unvisited assigned location. Remaining items are named implementation/estimator questions and unavailable inputs, not omissions of the assigned source scope. No inclusion disposition, severity, or final correction is assigned.

