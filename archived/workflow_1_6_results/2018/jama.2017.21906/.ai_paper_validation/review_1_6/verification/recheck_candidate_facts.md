# Workflow 1.6 Mechanical Evidence Recheck

Assigned scope: all 28 stable IDs C001 through C028 in the current candidate ledger. Every ID remains Pending Human Adjudication. This file records evidence facts only; it assigns no human disposition, severity, scientific validity, or final source correction. No stable ID was deleted, merged, or renumbered.

The complete scope, performance profile, review contract, report specification, settings, tooling record, current ledger, source inventory and routing preflight were read. Source authority is the current supplied PDF, including fresh direct rendering when position or visual text matters. Reusable and mapper artifacts were used only to locate pages. No legacy candidate/report, web source, GPU, new Python extractor, OCR installation, or source mutation was used.

## Engine and exact source confirmation

Direct CPU Poppler 25.03.0 produced page-specific layout text with `pdftotext -layout -f N -l N SOURCE OUTPUT` and fresh PNGs with `pdftoppm -r 115 -f N -l N -singlefile -png SOURCE PREFIX`. All new derivatives are below `preprocessing/`, with the unique `recheck-` prefix. Main article layout pages: 1, 2, 3, 4, 6, 7, 9; main fresh raster pages: 2, 4, 6, 7. SAP layout pages: 3, 4, 7; protocol layout page: 18. Mixed supplement layout and fresh raster pages: 1, 6, 7, 8, 9, 10, 17, 24. Every listed raster was visually inspected. Exact names are `recheck-main-pN-layout.txt`, `recheck-main-pN.png`, `recheck-sap-pN-layout.txt`, `recheck-protocol-p18-layout.txt`, `recheck-supp-pN-layout.txt`, and `recheck-supp-pN.png` beneath `../preprocessing/`. The physical PDF page, rather than the sample toolkit's inconsistent internal pagination, controls every source link below.

Content roles confirmed: DOC-001 main article is REPORT; DOC-002 protocol and DOC-003 SAP are PLAN. In DOC-004, the prospective sample audit/checklist toolkit on physical pp. 2–16 is PLAN, while the trial-results index p. 1 and results pp. 17–27 are REPORT. No document-role or primary relationship-type repair is required. Corroboration does not add a discrepancy relationship. Precedence is P_R > P_P > S_C > S_W; each ID has one substantive relationship type, so precedence introduces no additional selection.

Evidence-state totals: 25 recorded_candidate; 1 not_reproduced (C017); 0 repaired_residual; 2 record_input_error (C018, C019). The determining source facts are separately recorded below. C017's cohort 2 step 5 value is 28, not 8; its corrected sum is 295. For C018/C019, equal-estimand alignment of the percentage and beta columns is not established by the supplied definitions. These are evidence-record distinctions, not dispositions.

## C001 — Inpatient beta-blocker upper confidence endpoint

- **Location found:** Yes. REPORT [main PDF p. 6](../../../jama_huffman_2018_oi_170166.pdf#page=6), Table 2 in-hospital beta-blocker row and last process paragraph; direct layout and raster confirmed both.
- **Source value/text matched:** Table RD 6.25% (95% CI 4.10 to 8.40), OR 1.46 (1.29–1.65).
- **Comparator matched:** Prose RD 6.25% (95% CI 4.10%–8.10%), with the same OR; the sentence continues on p. 7 but the differing endpoint is on p. 6.
- **Consistency rule applicable:** Yes. A repeated adjusted inpatient beta-blocker contrast under the same cluster/time adjustment should have one displayed confidence endpoint unless a different output is identified.
- **Calculation reproduced:** 8.40 − 8.10 = 0.30 percentage points, greater than the combined 0.01-point two-decimal rounding allowance.
- **Necessary inputs available / exact missing definitions:** Both repeated values and matching outcome/model context are supplied. The intended output and any unreported model/output revision are absent; no raw data are needed to observe the printed disagreement.
- **Source-grounded alternative interpretation:** A different revised output might have been used in prose, but no distinct analysis is labeled.
- **Direct observation versus inferred explanation:** Printed endpoints differ directly. A transcription or output-revision mechanism is inferred and unestablished.
- **Classification:** Statistical reporting inconsistency; REPORT Table 2 versus REPORT process prose in DOC-001; primary S_W; all relationships S_W; review domain statistical_results. Confirmed, no repair; both are achieved-results content of one report. Ambiguity: none in role/type.
- **Evidence state:** recorded_candidate. Determining fact: fresh PDF text and raster reproduce 8.40 versus 8.10 for the matched repeated result.
- **Exact remaining human question:** Which upper 95% confidence limit, 8.40% or 8.10%, belongs to the adjusted inpatient beta-blocker risk difference?

## C002 — Discharge beta-blocker risk-difference point

- **Location found:** Yes. REPORT [main Table 2, PDF p. 6](../../../jama_huffman_2018_oi_170166.pdf#page=6), discharge beta-blocker row, versus REPORT [discharge prose, PDF p. 7](../../../jama_huffman_2018_oi_170166.pdf#page=7); direct layout and raster confirmed both.
- **Source value/text matched:** Table RD 6.69% (4.43 to 8.95); control 5808/8894 (65.3%), intervention 6799/10178 (66.8%).
- **Comparator matched:** Prose uses 67% versus 65%, adjusted RD 6.63% (4.43%–8.95%) for discharge beta-blocker use.
- **Consistency rule applicable:** Yes, repeated adjusted same-outcome risk difference with identical interval and cluster/time context should agree at displayed precision.
- **Calculation reproduced:** 6.69 − 6.63 = 0.06 percentage points, exceeding combined two-decimal endpoint rounding of 0.01 point.
- **Necessary inputs available / exact missing definitions:** Repeated values, intervals, populations and context are supplied. Intended output/version is absent; crude proportions do not reconstruct the adjusted RD.
- **Source-grounded alternative interpretation:** An undocumented output update or model variation could yield a different point, but is not identified here.
- **Direct observation versus inferred explanation:** The two printed point estimates differ. A production mechanism remains inferred.
- **Classification:** Statistical reporting inconsistency; REPORT DOC-001 table versus REPORT DOC-001 prose; primary S_W; all relationships S_W; review domain statistical_results. Confirmed, no repair; no conflicting plan or second report. Ambiguity: none in role/type.
- **Evidence state:** recorded_candidate. Determining fact: direct source reproduces 6.69 versus 6.63 with the same printed CI.
- **Exact remaining human question:** Is the adjusted discharge beta-blocker RD 6.69% or 6.63%, and which point belongs with the displayed 4.43%–8.95% interval?

## C003 — Discharge beta-blocker odds-ratio point

- **Location found:** Yes. REPORT [main Table 2, PDF p. 6](../../../jama_huffman_2018_oi_170166.pdf#page=6) versus REPORT [discharge prose, PDF p. 7](../../../jama_huffman_2018_oi_170166.pdf#page=7); direct layout and raster confirmed.
- **Source value/text matched:** Table adjusted OR 1.48 (1.30–1.68).
- **Comparator matched:** Prose adjusted OR 1.47 (1.30–1.68), same discharge beta-blocker contrast.
- **Consistency rule applicable:** Yes to repeated displayed-result identity. This is not proof that the underlying unrounded outputs necessarily differ.
- **Calculation reproduced:** Printed difference 0.01. Under a common nearest-rounding convention, bins [1.475, 1.485) and [1.465, 1.475) do not overlap; a tie at 1.475 with different conventions remains possible.
- **Necessary inputs available / exact missing definitions:** Printed values, CI and matching context are supplied. Unrounded point and rounding/tie convention are absent.
- **Source-grounded alternative interpretation:** Separate rounding at an exact tie or an output revision could explain the adjacent displayed values.
- **Direct observation versus inferred explanation:** The repeated printed points differ; an underlying estimate/model mismatch is not directly established.
- **Classification:** Statistical reporting inconsistency; REPORT table versus REPORT prose within DOC-001; primary S_W; all relationships S_W; review domain statistical_results. Confirmed, no repair. Ambiguity: rounding mechanism, not content role.
- **Evidence state:** recorded_candidate. Determining fact: the current PDF prints 1.48 and 1.47 for the matched result.
- **Exact remaining human question:** Which displayed OR should accompany the discharge beta-blocker result, and were different rounding conventions used?

## C004 — Door-to-balloon difference unit

- **Location found:** Yes. REPORT [main Table 2, PDF p. 6](../../../jama_huffman_2018_oi_170166.pdf#page=6), door-to-balloon time row, Difference,% header and footnotes b/c; direct layout and raster confirmed.
- **Source value/text matched:** Row median (IQR), min: control 65 (53–105), intervention 77 (55–118); difference 6.18 (−4.78 to 17.14); beta 13.00 (3.64–22.36).
- **Comparator matched:** Common header is Difference, % (95% CI). Footnote b says ORs/betas are calculated as intervention-minus-control differences in marginal effects, using mixed logistic or quantile regression; no percent-change denominator is given.
- **Consistency rule applicable:** Yes to the scale-definition question: min − min has minute units; percentage requires normalization or another stated scale definition.
- **Calculation reproduced:** Dimensional comparison min − min = min versus the percent header. No numerical tolerance resolves the unit ambiguity. The 6.18 and 13.00 entries are not assumed to be the same estimand.
- **Necessary inputs available / exact missing definitions:** Row, header and footnotes are supplied. Missing: formula/normalization denominator and the column-specific scale for 6.18.
- **Source-grounded alternative interpretation:** 6.18 may be a relative percentage or another normalized marginal summary; beta may be a minute contrast.
- **Direct observation versus inferred explanation:** Minute row and percent header directly coexist. Any incorrect label or intended percentage transformation remains inferred.
- **Classification:** Measure, label, or scale inconsistency; REPORT DOC-001 row versus REPORT DOC-001 header/footnotes; primary S_W; all relationships S_W; review domain report_internal_inconsistency. Confirmed, no repair. Ambiguity: missing effect-scale definition.
- **Evidence state:** recorded_candidate. Determining fact: printed unit-definition ambiguity remains as registered, pending the named normalization definition.
- **Exact remaining human question:** Is 6.18 a percentage change or a difference in minutes, and what formula and denominator define that column?

## C005 — Door-to-needle difference unit

- **Location found:** Yes. REPORT [main Table 2, PDF p. 6](../../../jama_huffman_2018_oi_170166.pdf#page=6), door-to-needle row, Difference,% header and footnotes b/c; direct layout and raster confirmed.
- **Source value/text matched:** Median (IQR), min: control 44 (30–67), intervention 45 (27–75); difference 0.40 (−5.23 to 6.03); beta 5.00 (−5.20–15.20).
- **Comparator matched:** Percent difference header applies to the time row; no percent-change formula is supplied.
- **Consistency rule applicable:** Yes to the unit-definition question. An unnormalized time subtraction retains minutes; a percentage requires its normalization definition.
- **Calculation reproduced:** min − min = min compared with %. No rounding tolerance resolves this labeling question; 0.40 is not silently equated with beta 5.00.
- **Necessary inputs available / exact missing definitions:** Row/header/footnote are available. Missing: scale and percent formula/denominator for 0.40.
- **Source-grounded alternative interpretation:** The difference column may intentionally show a separately normalized percentage, while beta shows a native time contrast.
- **Direct observation versus inferred explanation:** Printed row/header scales differ; a labeling/transformation mechanism is unestablished.
- **Classification:** Measure, label, or scale inconsistency; REPORT row versus REPORT header/footnotes within DOC-001; primary S_W; all relationships S_W; review domain report_internal_inconsistency. Confirmed, no repair. Ambiguity: missing scale definition.
- **Evidence state:** recorded_candidate. Determining fact: direct source retains the registered scale-definition question.
- **Exact remaining human question:** Is 0.40 a percentage change or a difference in minutes, and how is this adjusted contrast calculated?

## C006 — Table 2 OR subtraction definition

- **Location found:** Yes. REPORT [main Table 2, PDF p. 6](../../../jama_huffman_2018_oi_170166.pdf#page=6), OR/beta header, prehospital aspirin and inpatient beta-blocker rows and footnote b; direct layout and raster confirmed.
- **Source value/text matched:** ORs 1.40 and 1.46, with separately printed RDs 3.80% and 6.25%.
- **Comparator matched:** Footnote b explicitly says odds ratios and beta coefficients are calculated as the difference in marginal effects, intervention group minus control group.
- **Consistency rule applicable:** Yes. Odds ratios are ratios with null 1; subtraction of probabilities is a risk difference with null 0 and range [−1,1]. These definitions cannot label the same raw probability subtraction.
- **Calculation reproduced:** 3.80% = 0.038, not OR 1.40; 6.25% = 0.0625, not OR 1.46. ORs greater than 1 exceed the probability-difference upper bound.
- **Necessary inputs available / exact missing definitions:** Explicit wording and columns are available. Missing: the authors' intended footnote target and any specialized meaning of marginal effect; no raw regression output is needed to observe the label conflict.
- **Source-grounded alternative interpretation:** The subtraction wording may belong to the RD column; betas may legitimately be differences. A specialized marginal-effects convention must be defined before it can reconcile the OR wording.
- **Direct observation versus inferred explanation:** The OR definition and subtraction phrase are printed together. A copied footnote is an inferred mechanism.
- **Classification:** Measure, label, or scale inconsistency; REPORT header/cells versus REPORT footnote within DOC-001; primary S_W; all relationships S_W; review domain report_internal_inconsistency. Confirmed, no repair. Ambiguity: intended footnote wording.
- **Evidence state:** recorded_candidate. Determining fact: direct source reproduces the OR/subtraction definition conflict.
- **Exact remaining human question:** What defines the OR column, and was the intervention-minus-control subtraction description intended for the RD column?

## C007 — Table 3 OR subtraction definition

- **Location found:** Yes. REPORT [main Table 3, PDF p. 7](../../../jama_huffman_2018_oi_170166.pdf#page=7), OR headers, MACE and optimal inpatient medication rows, footnote a; direct layout and raster confirmed.
- **Source value/text matched:** Primary MACE RD −0.09%, OR 0.98; optimal inpatient medication RD 6.00%, OR 1.45.
- **Comparator matched:** Footnote a states that odds ratios are calculated as the difference in marginal effects, intervention group minus control group.
- **Consistency rule applicable:** Yes. OR and probability subtraction have different definitions, units, nulls and ranges.
- **Calculation reproduced:** −0.09% = −0.0009 versus OR 0.98; 0.0600 versus OR 1.45. A raw probability difference cannot be 1.45.
- **Necessary inputs available / exact missing definitions:** Printed measure names, entries and explicit footnote are supplied. Missing: intended definition/target of the footnote and any specialized marginal-effect terminology.
- **Source-grounded alternative interpretation:** The subtraction wording may refer to RD, with OR computed separately. Corroborating results-supplement terminology does not itself create a conflicting comparator.
- **Direct observation versus inferred explanation:** Printed OR label versus subtraction definition is direct; copy/edit cause is inferred.
- **Classification:** Measure, label, or scale inconsistency; REPORT DOC-001 OR headings/cells versus REPORT DOC-001 footnote; primary S_W; all relationships S_W; review domain report_internal_inconsistency. Confirmed, no repair; a second report that merely corroborates a definition does not add S_C. Ambiguity: intended definition.
- **Evidence state:** recorded_candidate. Determining fact: the current PDF prints the registered OR/subtraction wording.
- **Exact remaining human question:** Does Table 3 footnote a's subtraction definition belong to risk differences, and what computation generated the ORs?

## C008 — Tobacco-counseling threshold

- **Location found:** Yes. REPORT [main PDF p. 7](../../../jama_huffman_2018_oi_170166.pdf#page=7), Table 3 tobacco cessation advice row and discharge counseling paragraph; direct layout and raster confirmed.
- **Source value/text matched:** Intervention 2618 (94.7%); control 3526 (96.0%).
- **Comparator matched:** Prose says rates of discharge second antiplatelet use and tobacco cessation counseling were high (>95%) and similar between groups.
- **Consistency rule applicable:** Yes if the threshold describes each listed group-specific rate; the scope of the prose remains the human question.
- **Calculation reproduced:** 95 − 94.7 = 0.3 percentage points. The one-decimal rounding interval [94.65,94.75) is entirely below 95.
- **Necessary inputs available / exact missing definitions:** Threshold and group percentages supplied. Missing: whether >95% was intended for every group, an average, or a loose collective summary.
- **Source-grounded alternative interpretation:** The phrase may summarize generally high uptake rather than assert each proportion exceeds 95; control counseling and both antiplatelet percentages exceed 95.
- **Direct observation versus inferred explanation:** Printed intervention 94.7 is below the stated threshold. Overgeneralization/edit mechanism is inferred.
- **Classification:** Numeric or arithmetic inconsistency; REPORT DOC-001 prose versus REPORT DOC-001 table; primary S_W; all relationships S_W; review domain statistical_results. Confirmed, no repair. Ambiguity: threshold scope.
- **Evidence state:** recorded_candidate. Determining fact: the supplied proportion cannot exceed 95 at its printed precision under the all-groups reading.
- **Exact remaining human question:** Was >95% intended to describe each group's counseling rate, or should the 94.7% intervention value be distinguished?

## C009 — ECG minute heading versus within-threshold proportion

- **Location found:** Yes. PLAN [toolkit physical PDF p. 9](../../../joi170166supp3_prod.pdf#page=9), Section III measure 18 heading, definition and performance panels; fresh direct raster confirmed.
- **Source value/text matched:** Heading Door to 1st ECG in minutes; definition is proportion of AMI patients receiving ECG within 10 minutes of arrival at a participating hospital.
- **Comparator matched:** Percentage scale, percentile values 99.8%, 96.1%, 92.0%, 87.6%, 71.5%; plotted hospital scores 87.6%, 93.4%, 94.7%, 98.5%.
- **Consistency rule applicable:** Yes. Continuous delay in minutes and percentage meeting a 10-minute threshold are distinct quantities.
- **Calculation reproduced:** A within-threshold count/eligible-patient proportion times 100 has percent units, not minutes. No numerical rounding can identify these units.
- **Necessary inputs available / exact missing definitions:** Heading, threshold definition and plotted units supplied. Missing: intended metric name and whether the heading merely names the underlying timestamp field.
- **Source-grounded alternative interpretation:** A short heading may describe the timing field while the definition supplies a proportion-based performance metric.
- **Direct observation versus inferred explanation:** Heading and defined/displayed scales differ directly; intended shorthand or template mechanism is inferred.
- **Classification:** Measure, label, or scale inconsistency; PLAN sample operational heading versus PLAN definition/graphics within DOC-004 toolkit; primary P_P; all relationships P_P; review domain plan_material. Confirmed, no repair; sample material is prospective operational content, not achieved trial results. Ambiguity: intended metric shorthand.
- **Evidence state:** recorded_candidate. Determining fact: fresh current-source raster reproduces minutes versus percentage definitions.
- **Exact remaining human question:** Does measure 18 mean the percentage receiving ECG within 10 minutes, or are any displayed scores intended as time in minutes?

## C010 — ECG graph dates versus stated window

- **Location found:** Yes. PLAN [toolkit physical PDF p. 9](../../../joi170166supp3_prod.pdf#page=9), measure 18 rolling-performance heading and graph x axis; fresh direct raster confirmed.
- **Source value/text matched:** Rolling 3 Months Performance (Oct 2014–Dec 2014).
- **Comparator matched:** Four x-axis periods 2011Q3, 2011Q4, 2012Q1, 2012Q2; four hospital scores 87.6%, 93.4%, 94.7%, 98.5%.
- **Consistency rule applicable:** Yes to same-panel period-label identity.
- **Calculation reproduced:** October–December 2014 is 2014Q4. None of the four printed 2011–2012 quarters overlaps that named interval; count four quarters versus three named months also differs.
- **Necessary inputs available / exact missing definitions:** Both sets of dates supplied. Missing: actual intended sample period and whether the graph deliberately illustrates a different period.
- **Source-grounded alternative interpretation:** Historical placeholder axis labels may have been retained in a sample template; no trial chronology conclusion follows.
- **Direct observation versus inferred explanation:** Date labels differ directly; placeholder cause is inferred.
- **Classification:** Measure, label, or scale inconsistency; PLAN heading versus PLAN graph labels within DOC-004 toolkit; primary P_P; all relationships P_P; review domain plan_material. Confirmed, no repair. Ambiguity: intended sample window.
- **Evidence state:** recorded_candidate. Determining fact: direct raster shows the nonoverlapping named dates in the same panel.
- **Exact remaining human question:** Which periods do the four scores represent, and does the Oct–Dec 2014 rolling-performance heading apply to them?

## C011 — Hospital gender percentage total

- **Location found:** Yes. PLAN [toolkit physical PDF p. 10](../../../joi170166supp3_prod.pdf#page=10), Distribution of Gender chart, Hospital legend/blue bars and Percent of Admissions axis; fresh direct raster confirmed.
- **Source value/text matched:** Hospital male 43%, female 28%.
- **Comparator matched:** Only Male and Female categories are displayed; axis is Percent of Admissions.
- **Consistency rule applicable:** Conditional. If these are exhaustive categories using one admissions denominator, their total should be 100% within rounding.
- **Calculation reproduced:** 43 + 28 = 71%; complement 29 percentage points. Two integer-rounded percentages allow less than 1 point of combined rounding error; even a 72% upper bound is below 100.
- **Necessary inputs available / exact missing definitions:** Printed percentages and axis supplied. Missing: denominator identity, missing-gender category and whether two displayed categories are exhaustive.
- **Source-grounded alternative interpretation:** An unshown missing/other category, differing denominators or illustrative template data could explain the remainder.
- **Direct observation versus inferred explanation:** Displayed sum 71 is direct. Exhaustiveness and a defect in the underlying data are not established.
- **Classification:** Denominator, proportion, or total inconsistency; PLAN Hospital bars versus PLAN admissions axis within DOC-004 toolkit; primary P_P; all relationships P_P; review domain plan_material. Confirmed, no repair. Ambiguity: category coverage/denominator.
- **Evidence state:** recorded_candidate. Determining fact: registered conditional 71% total is source-confirmed and awaits its named category/denominator definition.
- **Exact remaining human question:** What accounts for the other 29% of Hospital admissions, and do the male/female bars share an exhaustive common denominator?

## C012 — All-hospital gender percentage total

- **Location found:** Yes. PLAN [toolkit physical PDF p. 10](../../../joi170166supp3_prod.pdf#page=10), Distribution of Gender chart, All legend/orange bars and Percent of Admissions axis; fresh direct raster confirmed.
- **Source value/text matched:** All male 56%, female 29%.
- **Comparator matched:** Only Male and Female categories are displayed under Percent of Admissions.
- **Consistency rule applicable:** Conditional on one denominator and exhaustive categories.
- **Calculation reproduced:** 56 + 29 = 85%; complement 15 points. Two rounded integer values permit less than 1 point of sum error, so rounding cannot reach 100.
- **Necessary inputs available / exact missing definitions:** Printed values and labels supplied. Missing: all-hospital denominator, missing/other category and category completeness.
- **Source-grounded alternative interpretation:** Missing gender, omitted category, different denominators or nonreconciling illustrative sample values.
- **Direct observation versus inferred explanation:** Sum 85 is direct; an underlying categorical-data error is not established.
- **Classification:** Denominator, proportion, or total inconsistency; PLAN All bars versus PLAN axis within DOC-004 toolkit; primary P_P; all relationships P_P; review domain plan_material. Confirmed, no repair. Ambiguity: omitted category/denominator definition.
- **Evidence state:** recorded_candidate. Determining fact: source-confirmed conditional 85% total remains as registered.
- **Exact remaining human question:** What accounts for the remaining 15% of all-hospital admissions, and what common denominator defines the two bars?

## C013 — Age subgroup partitions

- **Location found:** Yes. PLAN [SAP physical PDF p. 7](../../../joi170166supp2_prod.pdf#page=7), section 7.5.2 lines 1243–1253, versus REPORT [main Figure 3, PDF p. 9](../../../jama_huffman_2018_oi_170166.pdf#page=9) and REPORT [main methods, PDF p. 3](../../../jama_huffman_2018_oi_170166.pdf#page=3); fresh direct layout confirmed.
- **Source value/text matched:** SAP a priori age groups <65 years and >65 years.
- **Comparator matched:** Figure 3 title says Prespecified Subgroups; age groups <50, 50–69 and ≥70; methods calls age subgroup analysis prespecified. Intervention denominators 2079, 6606, 2623; control 2045, 5863, 2158.
- **Consistency rule applicable:** Yes to matching a numeric subgroup/prespecification label to supplied plan, subject to any amendment.
- **Calculation reproduced:** Two groups with cutpoint 65 differ from three groups with cutpoints 50 and 70. Intervention denominators sum 11308, control 10066; the question concerns partitions, not a subgroup-total shortfall. Ages 60 and 68 fall into separate SAP groups but the same reported middle group.
- **Necessary inputs available / exact missing definitions:** Both partitions and prespecified labels supplied. Missing: any approved amended/additional prespecification supporting the reported groups; no count of patients exactly age 65 is supplied.
- **Source-grounded alternative interpretation:** Another plan/amendment may support the reported partition. The SAP's age-65 boundary omission is not a separate candidate without a concrete affected count.
- **Direct observation versus inferred explanation:** Plan/report thresholds differ directly. A protocol departure is not adjudicated.
- **Classification:** Analysis-unit or population inconsistency, tied to numeric subgroup definitions; PLAN DOC-003 versus REPORT DOC-001; primary P_R; all relationships P_R; review domain protocol_report. Confirmed, no repair. Ambiguity: possible additional prespecification, not document role.
- **Evidence state:** recorded_candidate. Determining fact: the supplied SAP and reported prespecified partition differ numerically.
- **Exact remaining human question:** Which prespecified plan or amendment supports the reported <50, 50–69 and ≥70 partition instead of the supplied SAP's 65-year split?

## C014 — Crossover period count within SAP

- **Location found:** Yes. PLAN [SAP physical PDF p. 3](../../../joi170166supp2_prod.pdf#page=3), study-design lines 1091–1105 and diagram, versus PLAN [SAP physical PDF p. 4](../../../joi170166supp2_prod.pdf#page=4), randomization lines 1123–1124; direct layout confirmed.
- **Source value/text matched:** Five steps/cohorts; first crossover after four-month baseline, then cohorts 2–5 at months 8, 12, 16, 20. Diagram has five crossover markers at 4, 8, 12, 16, 20.
- **Comparator matched:** Randomization paragraph says one cohort receives intervention in each of the four time periods.
- **Consistency rule applicable:** Yes if time periods denotes all scheduled cohort crossovers; a differing period convention remains possible.
- **Calculation reproduced:** Five distinct crossover dates minus four stated periods = one; exact count, no rounding allowance.
- **Necessary inputs available / exact missing definitions:** Both within-SAP descriptions supplied. Missing: whether four excludes the first crossover or denotes a different period grouping.
- **Source-grounded alternative interpretation:** Initial crossover may be counted separately, leaving four subsequent cohort crossovers.
- **Direct observation versus inferred explanation:** Five-date schedule versus four-period wording is direct; intended period convention/edit history is inferred.
- **Classification:** Numeric or arithmetic inconsistency; PLAN DOC-003 design versus PLAN DOC-003 randomization; primary P_P; all relationships P_P; review domain plan_material. Confirmed, no repair. Main article five-step corroboration does not create P_R. Ambiguity: period convention.
- **Evidence state:** recorded_candidate. Determining fact: source-confirmed five crossovers and four-period wording remain unresolved without that definition.
- **Exact remaining human question:** Does four time periods exclude the first crossover, or does it intend all five scheduled cohort crossovers?

## C015 — Planned dropout allowance arithmetic

- **Location found:** Yes. PLAN [protocol physical PDF p. 18](../../../joi170166supp1_prod.pdf#page=18), section 8.2 lines 573–579, repeated in PLAN [SAP physical PDF p. 4](../../../joi170166supp2_prod.pdf#page=4), lines 1113–1116; direct layout confirmed. REPORT [main methods p. 3](../../../jama_huffman_2018_oi_170166.pdf#page=3) repeats 15750 and 5% only as corroboration.
- **Source value/text matched:** Anticipated 15000 gives stated 80% power; increased to 15750 to account for up to 5% dropout between discharge and 30-day follow-up.
- **Comparator matched:** The retention requirement is conditional, not printed as a guaranteed final 15000: if 15000 is the required retained n and 5% is a recruited-patient fraction, the total must preserve it after multiplication by 0.95.
- **Consistency rule applicable:** Conditional on those two named premises; the package does not establish exact retained-sample requirement or unrounded power target.
- **Calculation reproduced:** 15750 × 0.95 = 14962.5; 15000 − 14962.5 = 37.5. 15000/0.95 = 15789.4737, minimum integer target 15790. Printed 15750 equals 15000 × 1.05.
- **Necessary inputs available / exact missing definitions:** Printed targets and allowance supplied. Missing: whether 15000 is exact/rounded and required retained sample, dropout denominator, and additive-padding convention/full power output.
- **Source-grounded alternative interpretation:** Approximate additive 5% contingency, a rounded 15000 target, or a target based on enrolled rather than retained participants may explain the arithmetic.
- **Direct observation versus inferred explanation:** Targets and stated inflation purpose are direct; strict retention premise and any power consequence are conditional and unestablished.
- **Classification:** Numeric or arithmetic inconsistency; PLAN DOC-002 sample-size statement, repeated in PLAN DOC-003; primary P_P; all relationships P_P; review domain plan_material. Confirmed, no repair. The two plan versions corroborate the same premise; main corroboration adds no P_R. Ambiguity: conditional retention definition.
- **Evidence state:** recorded_candidate. Determining fact: the explicitly registered conditional allowance calculation is reproduced with supplied targets; no unconditional shortfall claim is made.
- **Exact remaining human question:** Was 15750 approximate additive 5% padding or the total intended to retain 15000 after 5% loss, and is 15000 itself rounded or a retained-sample requirement?

## C016 — Follow-up-status table contrast footnote

- **Location found:** Yes. REPORT [results eTable 1, physical PDF p. 17](../../../joi170166supp3_prod.pdf#page=17), complete/missing headers, age/male rows and footnote a; fresh direct layout and raster confirmed.
- **Source value/text matched:** Complete Follow Up n=21079 versus Missing Follow Up n=295; age 60.6 versus 60.0, difference −0.6; male 75.8% versus 71.2%, difference −4.6.
- **Comparator matched:** Footnote says Difference = intervention minus control; neither displayed comparison column carries those treatment identities.
- **Consistency rule applicable:** Yes to explicit column/reference identity, independently of detailed CI construction.
- **Calculation reproduced:** 60.0 − 60.6 = −0.6; 71.2 − 75.8 = −4.6 points, matching missing-minus-complete direction.
- **Necessary inputs available / exact missing definitions:** Headers, entries and footnote supplied. Missing: intended footnote wording or a documented treatment-stratified contrast; no such analysis is specified here.
- **Source-grounded alternative interpretation:** An unseen treatment contrast could conceivably be intended, but cannot be identified with these two printed follow-up-status columns.
- **Direct observation versus inferred explanation:** Treatment-arm footnote versus follow-up-status columns is direct; a copied footnote is inferred.
- **Classification:** Measure, label, or scale inconsistency; REPORT DOC-004 results headers/rows versus REPORT DOC-004 results footnote; primary S_W; all relationships S_W; review domain report_internal_inconsistency. Confirmed, no repair; toolkit PLAN pages are not comparators. Ambiguity: intended reference definition.
- **Evidence state:** recorded_candidate. Determining fact: direct source reproduces the contrast-label mismatch while example arithmetic matches missing-minus-complete.
- **Exact remaining human question:** Should eTable 1's difference definition be missing follow-up minus complete follow-up, or is another contrast intended?

## C017 — Flow missing-follow-up sum

- **Location found:** Yes. REPORT [main Figure 1, physical PDF p. 4](../../../jama_huffman_2018_oi_170166.pdf#page=4), all 20 lost-follow-up boxes and caption, versus REPORT [main outcome-completeness prose p. 6](../../../jama_huffman_2018_oi_170166.pdf#page=6); direct current layout and fresh raster confirmed. REPORT [results eTable 1 p. 17](../../../joi170166supp3_prod.pdf#page=17) corroborates the prose total.
- **Source value/text matched:** Partially; the ledger's cohort 2 step 5 transcription of 8 is disproven. That box prints **28 Lost to follow-up**, between 627 enrolled and 600 included in analysis. Correct control steps 0–4: 42, 45, 54, 27, 2. Correct intervention cohort 1 steps 1–5: 2, 6, 0, 3, 10; cohort 2 steps 2–5: 18, 4, 6, **28**; cohort 3 steps 3–5: 10, 8, 7; cohort 4 steps 4–5: 7, 7; cohort 5 step 5: 9.
- **Comparator matched:** Prose 295 incomplete outcomes = 215 not followed by enrolling site + 80 unreachable after three attempts. eTable 1 missing follow-up n=295, complete n=21079. Figure caption includes both mechanisms and says lost participants were included in analysis.
- **Consistency rule applicable:** Yes, exact sum of the disjoint boxes against the printed aggregate under the stated lost-follow-up definition.
- **Calculation reproduced:** Control 42+45+54+27+2=170. Intervention (2+6+0+3+10)+(18+4+6+28)+(10+8+7)+(7+7)+9 = 21+56+25+14+9 = 125. Total 170+125=295. 21374−295=21079. The registered 275 total, 20-person discrepancy and 21099 completion count are not reproduced.
- **Necessary inputs available / exact missing definitions:** Every box and aggregate is available; no missing input is needed to settle this comparison. Exact box read is corroborated by direct text and raster.
- **Source-grounded alternative interpretation:** The legacy/registered locator dropped the leading 2 in 28; no extra missingness category is necessary to reconcile these source values.
- **Direct observation versus inferred explanation:** Box value 28 and source sum 295 are direct observations/calculation. How the prior transcription lost the leading digit is inferred.
- **Classification:** Denominator, proportion, or total inconsistency registration; REPORT Figure 1 versus REPORT prose within DOC-001; primary S_W; all relationships S_W; review domain statistical_results. Confirmed, no role/type repair; eTable 1 only corroborates 295 and adds no S_C. Ambiguity: none remaining for this sum.
- **Evidence state:** not_reproduced. Determining fact: corrected direct-source box 28 makes the figure sum 295, exactly reconciling with the registered comparator. This is explicit disproof of the mismatch, not an unsettled residual input question.
- **Exact remaining human question:** None for the registered numeric sum; a human can confirm the cohort 2 step 5 box reads 28 and the 20 boxes sum to 295. The stable ID remains present for adjudication.

## C018 — Door-to-balloon column-estimand alignment

- **Location found:** Yes. REPORT [main Table 2, physical PDF p. 6](../../../jama_huffman_2018_oi_170166.pdf#page=6), door-to-balloon row and both headers/footnotes; direct current layout and fresh raster confirmed.
- **Source value/text matched:** Difference,% 6.18 (−4.78 to 17.14); OR or beta column 13.00 (3.64–22.36), marked c=beta; outcome median time in minutes.
- **Comparator matched:** Numerical comparator 13.00 is correctly transcribed. However the registered shared-effect definition is not established as an identity rule for both entries: footnote b, though attached to both headers, explicitly defines **odds ratios and beta coefficients**, while the first column is labeled Difference,%.
- **Consistency rule applicable:** Not established for unconditional equality of these columns. If both were the same untransformed time contrast they should agree, but shared row/model/footnote marker alone does not supply that estimand alignment.
- **Calculation reproduced:** Conditional subtraction 13.00−6.18=6.82 is correct. One CI includes zero and the other excludes it, but this is not a same-test incompatibility without matched estimand/variance rules.
- **Necessary inputs available / exact missing definitions:** Printed entries and labels available. Missing: first-column formula, percent denominator, column-specific estimand/scale, transformation/marginalization and covariance/variance definition. Equal-estimand identity is a missing scientific input, not a consequence of conventional statistical practice.
- **Source-grounded alternative interpretation:** The explicit percent header permits 6.18 to be a relative or marginal percentage and 13.00 a native-time beta; distinct valid summaries may differ. A label question remains separately registered at C004.
- **Direct observation versus inferred explanation:** Distinct values and labels are direct. Treating their numerical inequality as a discrepancy requires an unsupported alignment premise; no source transcription error is found here.
- **Classification:** Statistical reporting inconsistency registration; REPORT column versus REPORT column/footnote within DOC-001; primary S_W; all relationships S_W; review domain statistical_results. Role/type confirmed, no repair. Classification ambiguity: the scientific comparison's equal-estimand premise is unestablished; document identity is clear.
- **Evidence state:** record_input_error. Determining fact: the numerical comparison relies on unsupported same-estimand alignment, and the package cannot settle whether a residual numerical discrepancy exists. Merely sharing footnote b does not establish equality of the two differently labeled columns.
- **Exact remaining human question:** What exact estimand, scale and formula generated each door-to-balloon entry, and were they intended to be the same untransformed intervention-minus-control time contrast?

## C019 — Door-to-needle column-estimand alignment

- **Location found:** Yes. REPORT [main Table 2, physical PDF p. 6](../../../jama_huffman_2018_oi_170166.pdf#page=6), door-to-needle row and headers/footnotes; direct current layout and fresh raster confirmed.
- **Source value/text matched:** Difference,% 0.40 (−5.23 to 6.03); beta 5.00 (−5.20–15.20), identified by c; median time in minutes.
- **Comparator matched:** Numerical comparator 5.00 is correctly transcribed. Footnote b explicitly describes ORs/betas rather than assigning an identical untransformed estimand to the percent difference column.
- **Consistency rule applicable:** Only conditional equality if a same-estimand/scale mapping is supplied. Shared row and adjustment label do not themselves establish that mapping.
- **Calculation reproduced:** Conditional difference 5.00−0.40=4.60; both CIs include zero. No P value or same-test contradiction is reconstructed.
- **Necessary inputs available / exact missing definitions:** Printed values and labels supplied. Missing: percent formula/denominator, exact column estimands, scale/transformation, marginalization and variance construction.
- **Source-grounded alternative interpretation:** Separate percentage/marginal and native-minute beta summaries could coherently differ; the unit-definition question is separately preserved at C005.
- **Direct observation versus inferred explanation:** Numerical inequality is direct, but discrepancy inference requires an unsupported identity of the inputs.
- **Classification:** Statistical reporting inconsistency registration; REPORT column versus REPORT column/footnote within DOC-001; primary S_W; all relationships S_W; review domain statistical_results. Confirmed, no role/type repair. Ambiguity: same-estimand identity remains unsupported.
- **Evidence state:** record_input_error. Determining fact: supplied labels/wording do not establish the equal-estimand alignment necessary to treat 0.40 and 5.00 as conflicting values; residual discrepancy cannot be settled.
- **Exact remaining human question:** What estimand, scale and formula generated each door-to-needle entry, and was the same untransformed intervention-minus-control contrast intended for both?

## C020 — Key Points significance negation

- **Location found:** Yes. REPORT [main Key Points, physical PDF p. 2](../../../jama_huffman_2018_oi_170166.pdf#page=2), Findings, versus REPORT [abstract p. 1](../../../jama_huffman_2018_oi_170166.pdf#page=1) and REPORT [primary result p. 7](../../../jama_huffman_2018_oi_170166.pdf#page=7); fresh direct text and p. 2/p. 7 rasters confirmed.
- **Source value/text matched:** Key Points prints “a difference that did not reach not statistical significance after adjustment for cluster and temporal trends.” Both occurrences of not are visible in the fresh raster.
- **Comparator matched:** Abstract says the observed difference was not statistically significant after adjustment; primary text says not statistically significant after further temporal adjustment. Matched result RD −0.09% (−1.32 to 1.14), OR 0.98 (0.80–1.21).
- **Consistency rule applicable:** Yes, matched-result significance wording should communicate one consistent interpretation; duplicate negation obscures it.
- **Calculation reproduced:** Logical comparison of one negation versus two; no reanalysis. RD interval includes zero and OR interval includes one, consistent with the surrounding nonsignificance wording, but no exact P is reconstructed.
- **Necessary inputs available / exact missing definitions:** Wording, result identity and interval supplied. Missing: intended edited sentence only.
- **Source-grounded alternative interpretation:** Accidental duplicate not is consistent with Key Points Meaning, abstract and primary prose expressing no detected reduction.
- **Direct observation versus inferred explanation:** Duplicated source word is direct. An editorial duplication mechanism is inferred; significance inversion is a possible literal reading, not a claim about the result.
- **Classification:** Statistical reporting inconsistency; REPORT Key Points versus REPORT abstract/primary prose within DOC-001; primary S_W; all relationships S_W; review domain statistical_results. Confirmed, no repair. Ambiguity: intended sentence, not roles.
- **Evidence state:** recorded_candidate. Determining fact: the direct source visibly prints duplicated negation against matched single-negation statements.
- **Exact remaining human question:** Is the second not intended, and should Key Points express the same nonsignificance interpretation as the abstract and primary-result prose?

## C021 — Residual sign description

- **Location found:** Yes. REPORT [results-supplement index, physical PDF p. 1](../../../joi170166supp3_prod.pdf#page=1), eFigure 1A line, versus REPORT [eFigure 1A axis/caption, physical PDF p. 24](../../../joi170166supp3_prod.pdf#page=24); fresh direct layout and rasters confirmed.
- **Source value/text matched:** Index labels residual as Expected – Observed.
- **Comparator matched:** Caption says hospital-level departures from mean MACE rate, residual zero at mean; left hospitals lower than mean, right higher. Plotted residuals run negative on the left to positive on the right.
- **Consistency rule applicable:** Conditional on index Expected identifying the caption's reference rate; both labels purport to describe the same eFigure 1A residual. Unlike an invented model-equality assumption, the subtraction order and directional reference are explicitly supplied.
- **Calculation reproduced:** For common expected/reference E and observed O, O<E implies E−O>0, whereas caption associates lower-than-reference with negative/left; O>E implies E−O<0, whereas caption assigns positive/right. This is conditional sign algebra, not a hospital-rate reconstruction.
- **Necessary inputs available / exact missing definitions:** Printed subtraction order and sign/direction/reference language available. Missing: actual plotted residual formula, link/scale, expected reference, inclusion/exclusion of random effects and mapping of predicted to observed rates.
- **Source-grounded alternative interpretation:** The plot may show a hospital random effect or residual on log-odds scale rather than arithmetic risk residual; expected may be hospital-specific rather than the caption's mean. Such a different definition could reconcile output while leaving the two descriptions needing clarification.
- **Direct observation versus inferred explanation:** Opposing stated sign descriptions are direct under their shared-reference reading; actual output identity and which description is intended are unresolved.
- **Classification:** Measure, label, or scale inconsistency; REPORT DOC-004 results index versus REPORT DOC-004 results figure/caption; primary S_W; all relationships S_W; review domain report_internal_inconsistency. Confirmed, no repair; no toolkit PLAN comparator. Ambiguity: residual reference/scale definition.
- **Evidence state:** recorded_candidate. Determining fact: both printed descriptions are source-confirmed and their conditional sign mismatch remains pending the named residual definition.
- **Exact remaining human question:** What residual is plotted, on what scale and against which expected/reference value, and which subtraction/direction description identifies it?

## C022 — STEMI/NSTEMI composite timeline point

- **Location found:** Yes. PLAN [toolkit physical PDF p. 6](../../../joi170166supp3_prod.pdf#page=6), measure 1, STEMI/NSTEMI composite, right performance panel, header, x labels and green My Hospital markers; fresh direct source raster confirmed this specific panel independently.
- **Source value/text matched:** Header 3 Months Performance (Oct 2014–Dec 2014); x labels 2014 Oct, 2014 Nov, 2014 Dec and corresponding score labels 87.6%, 93.4%, 94.7%. The panel's definition describes 11 acute and discharge measures for STEMI/NSTEMI.
- **Comparator matched:** Four green My Hospital points occupy separate horizontal positions. The third aligns with December and its 94.7% score; the fourth lies farther right without a date or score label, between the printed 98% and 100% ticks. No exact fourth score is asserted.
- **Consistency rule applicable:** Yes to labeling a time-series scope: each plotted period position needs a defined date/window within the named scope or an explanation of its distinct role. Counting the separate points does not assume that the fourth is December.
- **Calculation reproduced:** Four plotted green positions minus three explicit month/score labels = one additional unlabeled position. The three labeled scores and their positions match; there is no December 94.7%-versus-98% comparison.
- **Necessary inputs available / exact missing definitions:** Header, three dates/scores and four separate positions available from the fresh raster. Missing: fourth position's date/window, whether it is a forecast/extra period/template element, and its intended population; no unprinted numeric value is needed for this labeling comparison.
- **Source-grounded alternative interpretation:** This sample operational graph may include an extra period, forecast or template point. For a rolling window, prior observations may underlie the score, but that does not define an extra unlabeled window-end position. No achieved trial outcome is inferred.
- **Direct observation versus inferred explanation:** Four points and three labels are direct visual observations. An erroneous fourth point, omitted date, forecast or template origin is an inferred explanation requiring a definition.
- **Classification:** Measure, label, or scale inconsistency; PLAN DOC-004 toolkit heading/date labels versus PLAN same panel's markers; primary P_P; all relationships P_P; review domain plan_material. Confirmed, no role/type repair; this is sample prospective audit-and-feedback content. Ambiguity: fourth point's time definition.
- **Evidence state:** recorded_candidate. Determining fact: direct current-source raster confirms the registered additional unlabeled position in measure 1, pending its named time definition.
- **Exact remaining human question:** Which date/window and population does the fourth My Hospital point in measure 1 represent, and should the three-month panel include a fourth labeled period or only three plotted points?


## C023 — STEMI composite timeline point

- **Location found:** Yes. PLAN [toolkit physical PDF p. 6](../../../joi170166supp3_prod.pdf#page=6), measure 2, STEMI composite, right performance panel, header, x labels and green My Hospital markers; fresh direct source raster confirmed this specific panel independently.
- **Source value/text matched:** Header 3 Months Performance (Oct 2014–Dec 2014); x labels 2014 Oct, 2014 Nov, 2014 Dec and corresponding score labels 87.6%, 93.4%, 94.7%. The panel's definition describes 11 acute and discharge measures for STEMI.
- **Comparator matched:** Four green My Hospital points occupy separate horizontal positions. The third aligns with December and its 94.7% score; the fourth lies farther right without a date or score label, between the printed 98% and 100% ticks. No exact fourth score is asserted.
- **Consistency rule applicable:** Yes to labeling a time-series scope: each plotted period position needs a defined date/window within the named scope or an explanation of its distinct role. Counting the separate points does not assume that the fourth is December.
- **Calculation reproduced:** Four plotted green positions minus three explicit month/score labels = one additional unlabeled position. The three labeled scores and their positions match; there is no December 94.7%-versus-98% comparison.
- **Necessary inputs available / exact missing definitions:** Header, three dates/scores and four separate positions available from the fresh raster. Missing: fourth position's date/window, whether it is a forecast/extra period/template element, and its intended population; no unprinted numeric value is needed for this labeling comparison.
- **Source-grounded alternative interpretation:** This sample operational graph may include an extra period, forecast or template point. For a rolling window, prior observations may underlie the score, but that does not define an extra unlabeled window-end position. No achieved trial outcome is inferred.
- **Direct observation versus inferred explanation:** Four points and three labels are direct visual observations. An erroneous fourth point, omitted date, forecast or template origin is an inferred explanation requiring a definition.
- **Classification:** Measure, label, or scale inconsistency; PLAN DOC-004 toolkit heading/date labels versus PLAN same panel's markers; primary P_P; all relationships P_P; review domain plan_material. Confirmed, no role/type repair; this is sample prospective audit-and-feedback content. Ambiguity: fourth point's time definition.
- **Evidence state:** recorded_candidate. Determining fact: direct current-source raster confirms the registered additional unlabeled position in measure 2, pending its named time definition.
- **Exact remaining human question:** Which date/window and population does the fourth My Hospital point in measure 2 represent, and should the three-month panel include a fourth labeled period or only three plotted points?


## C024 — NSTEMI composite timeline point

- **Location found:** Yes. PLAN [toolkit physical PDF p. 6](../../../joi170166supp3_prod.pdf#page=6), measure 3, NSTEMI composite, right performance panel, header, x labels and green My Hospital markers; fresh direct source raster confirmed this specific panel independently.
- **Source value/text matched:** Header 3 Months Performance (Oct 2014–Dec 2014); x labels 2014 Oct, 2014 Nov, 2014 Dec and corresponding score labels 87.6%, 93.4%, 94.7%. The panel's definition describes 8 acute and discharge measures for NSTEMI.
- **Comparator matched:** Four green My Hospital points occupy separate horizontal positions. The third aligns with December and its 94.7% score; the fourth lies farther right without a date or score label, between the printed 98% and 100% ticks. No exact fourth score is asserted.
- **Consistency rule applicable:** Yes to labeling a time-series scope: each plotted period position needs a defined date/window within the named scope or an explanation of its distinct role. Counting the separate points does not assume that the fourth is December.
- **Calculation reproduced:** Four plotted green positions minus three explicit month/score labels = one additional unlabeled position. The three labeled scores and their positions match; there is no December 94.7%-versus-98% comparison.
- **Necessary inputs available / exact missing definitions:** Header, three dates/scores and four separate positions available from the fresh raster. Missing: fourth position's date/window, whether it is a forecast/extra period/template element, and its intended population; no unprinted numeric value is needed for this labeling comparison.
- **Source-grounded alternative interpretation:** This sample operational graph may include an extra period, forecast or template point. For a rolling window, prior observations may underlie the score, but that does not define an extra unlabeled window-end position. No achieved trial outcome is inferred.
- **Direct observation versus inferred explanation:** Four points and three labels are direct visual observations. An erroneous fourth point, omitted date, forecast or template origin is an inferred explanation requiring a definition.
- **Classification:** Measure, label, or scale inconsistency; PLAN DOC-004 toolkit heading/date labels versus PLAN same panel's markers; primary P_P; all relationships P_P; review domain plan_material. Confirmed, no role/type repair; this is sample prospective audit-and-feedback content. Ambiguity: fourth point's time definition.
- **Evidence state:** recorded_candidate. Determining fact: direct current-source raster confirms the registered additional unlabeled position in measure 3, pending its named time definition.
- **Exact remaining human question:** Which date/window and population does the fourth My Hospital point in measure 3 represent, and should the three-month panel include a fourth labeled period or only three plotted points?


## C025 — Discharge-AMI composite timeline point

- **Location found:** Yes. PLAN [toolkit physical PDF p. 7](../../../joi170166supp3_prod.pdf#page=7), measure 4, Discharge-AMI composite, right performance panel, header, x labels and green My Hospital markers; fresh direct source raster confirmed this specific panel independently.
- **Source value/text matched:** Header 3 Months Performance (Oct 2014–Dec 2014); x labels 2014 Oct, 2014 Nov, 2014 Dec and corresponding score labels 87.6%, 93.4%, 94.7%. The panel's definition describes 6 discharge measures for all AMI.
- **Comparator matched:** Four green My Hospital points occupy separate horizontal positions. The third aligns with December and its 94.7% score; the fourth lies farther right without a date or score label, between the printed 98% and 100% ticks. No exact fourth score is asserted.
- **Consistency rule applicable:** Yes to labeling a time-series scope: each plotted period position needs a defined date/window within the named scope or an explanation of its distinct role. Counting the separate points does not assume that the fourth is December.
- **Calculation reproduced:** Four plotted green positions minus three explicit month/score labels = one additional unlabeled position. The three labeled scores and their positions match; there is no December 94.7%-versus-98% comparison.
- **Necessary inputs available / exact missing definitions:** Header, three dates/scores and four separate positions available from the fresh raster. Missing: fourth position's date/window, whether it is a forecast/extra period/template element, and its intended population; no unprinted numeric value is needed for this labeling comparison.
- **Source-grounded alternative interpretation:** This sample operational graph may include an extra period, forecast or template point. For a rolling window, prior observations may underlie the score, but that does not define an extra unlabeled window-end position. No achieved trial outcome is inferred.
- **Direct observation versus inferred explanation:** Four points and three labels are direct visual observations. An erroneous fourth point, omitted date, forecast or template origin is an inferred explanation requiring a definition.
- **Classification:** Measure, label, or scale inconsistency; PLAN DOC-004 toolkit heading/date labels versus PLAN same panel's markers; primary P_P; all relationships P_P; review domain plan_material. Confirmed, no role/type repair; this is sample prospective audit-and-feedback content. Ambiguity: fourth point's time definition.
- **Evidence state:** recorded_candidate. Determining fact: direct current-source raster confirms the registered additional unlabeled position in measure 4, pending its named time definition.
- **Exact remaining human question:** Which date/window and population does the fourth My Hospital point in measure 4 represent, and should the three-month panel include a fourth labeled period or only three plotted points?


## C026 — Arrival-aspirin metric timeline point

- **Location found:** Yes. PLAN [toolkit physical PDF p. 7](../../../joi170166supp3_prod.pdf#page=7), measure 5, Arrival-aspirin metric, right performance panel, header, x labels and green My Hospital markers; fresh direct source raster confirmed this specific panel independently.
- **Source value/text matched:** Header Rolling 3 Months Performance (Oct 2014–Dec 2014); x labels 2014 Oct, 2014 Nov, 2014 Dec and corresponding score labels 87.6%, 93.4%, 94.7%. The panel's definition describes aspirin at arrival; definition excludes transfers in and out.
- **Comparator matched:** Four green My Hospital points occupy separate horizontal positions. The third aligns with December and its 94.7% score; the fourth lies farther right without a date or score label, between the printed 98% and 100% ticks. No exact fourth score is asserted.
- **Consistency rule applicable:** Yes to labeling a time-series scope: each plotted period position needs a defined date/window within the named scope or an explanation of its distinct role. Counting the separate points does not assume that the fourth is December.
- **Calculation reproduced:** Four plotted green positions minus three explicit month/score labels = one additional unlabeled position. The three labeled scores and their positions match; there is no December 94.7%-versus-98% comparison.
- **Necessary inputs available / exact missing definitions:** Header, three dates/scores and four separate positions available from the fresh raster. Missing: fourth position's date/window, whether it is a forecast/extra period/template element, and its intended population; no unprinted numeric value is needed for this labeling comparison.
- **Source-grounded alternative interpretation:** This sample operational graph may include an extra period, forecast or template point. For a rolling window, prior observations may underlie the score, but that does not define an extra unlabeled window-end position. No achieved trial outcome is inferred.
- **Direct observation versus inferred explanation:** Four points and three labels are direct visual observations. An erroneous fourth point, omitted date, forecast or template origin is an inferred explanation requiring a definition.
- **Classification:** Measure, label, or scale inconsistency; PLAN DOC-004 toolkit heading/date labels versus PLAN same panel's markers; primary P_P; all relationships P_P; review domain plan_material. Confirmed, no role/type repair; this is sample prospective audit-and-feedback content. Ambiguity: fourth point's time definition.
- **Evidence state:** recorded_candidate. Determining fact: direct current-source raster confirms the registered additional unlabeled position in measure 5, pending its named time definition.
- **Exact remaining human question:** Which date/window and population does the fourth My Hospital point in measure 5 represent, and should the three-month panel include a fourth labeled period or only three plotted points?


## C027 — Discharge-aspirin metric timeline point

- **Location found:** Yes. PLAN [toolkit physical PDF p. 7](../../../joi170166supp3_prod.pdf#page=7), measure 6, Discharge-aspirin metric, right performance panel, header, x labels and green My Hospital markers; fresh direct source raster confirmed this specific panel independently.
- **Source value/text matched:** Header Rolling 3 Months Performance (Oct 2014–Dec 2014); x labels 2014 Oct, 2014 Nov, 2014 Dec and corresponding score labels 87.6%, 93.4%, 94.7%. The panel's definition describes aspirin prescribed at discharge.
- **Comparator matched:** Four green My Hospital points occupy separate horizontal positions. The third aligns with December and its 94.7% score; the fourth lies farther right without a date or score label, between the printed 98% and 100% ticks. No exact fourth score is asserted.
- **Consistency rule applicable:** Yes to labeling a time-series scope: each plotted period position needs a defined date/window within the named scope or an explanation of its distinct role. Counting the separate points does not assume that the fourth is December.
- **Calculation reproduced:** Four plotted green positions minus three explicit month/score labels = one additional unlabeled position. The three labeled scores and their positions match; there is no December 94.7%-versus-98% comparison.
- **Necessary inputs available / exact missing definitions:** Header, three dates/scores and four separate positions available from the fresh raster. Missing: fourth position's date/window, whether it is a forecast/extra period/template element, and its intended population; no unprinted numeric value is needed for this labeling comparison.
- **Source-grounded alternative interpretation:** This sample operational graph may include an extra period, forecast or template point. For a rolling window, prior observations may underlie the score, but that does not define an extra unlabeled window-end position. No achieved trial outcome is inferred.
- **Direct observation versus inferred explanation:** Four points and three labels are direct visual observations. An erroneous fourth point, omitted date, forecast or template origin is an inferred explanation requiring a definition.
- **Classification:** Measure, label, or scale inconsistency; PLAN DOC-004 toolkit heading/date labels versus PLAN same panel's markers; primary P_P; all relationships P_P; review domain plan_material. Confirmed, no role/type repair; this is sample prospective audit-and-feedback content. Ambiguity: fourth point's time definition.
- **Evidence state:** recorded_candidate. Determining fact: direct current-source raster confirms the registered additional unlabeled position in measure 6, pending its named time definition.
- **Exact remaining human question:** Which date/window and population does the fourth My Hospital point in measure 6 represent, and should the three-month panel include a fourth labeled period or only three plotted points?


## C028 — Discharge-beta-blocker metric timeline point

- **Location found:** Yes. PLAN [toolkit physical PDF p. 8](../../../joi170166supp3_prod.pdf#page=8), measure 7, Discharge-beta-blocker metric, right performance panel, header, x labels and green My Hospital markers; fresh direct source raster confirmed this specific panel independently.
- **Source value/text matched:** Header Rolling 3 Months Performance (Oct 2014–Dec 2014); x labels 2014 Oct, 2014 Nov, 2014 Dec and corresponding score labels 87.6%, 93.4%, 94.7%. The panel's definition describes beta-blocker prescribed at discharge.
- **Comparator matched:** Four green My Hospital points occupy separate horizontal positions. The third aligns with December and its 94.7% score; the fourth lies farther right without a date or score label, between the printed 98% and 100% ticks. No exact fourth score is asserted.
- **Consistency rule applicable:** Yes to labeling a time-series scope: each plotted period position needs a defined date/window within the named scope or an explanation of its distinct role. Counting the separate points does not assume that the fourth is December.
- **Calculation reproduced:** Four plotted green positions minus three explicit month/score labels = one additional unlabeled position. The three labeled scores and their positions match; there is no December 94.7%-versus-98% comparison.
- **Necessary inputs available / exact missing definitions:** Header, three dates/scores and four separate positions available from the fresh raster. Missing: fourth position's date/window, whether it is a forecast/extra period/template element, and its intended population; no unprinted numeric value is needed for this labeling comparison.
- **Source-grounded alternative interpretation:** This sample operational graph may include an extra period, forecast or template point. For a rolling window, prior observations may underlie the score, but that does not define an extra unlabeled window-end position. No achieved trial outcome is inferred.
- **Direct observation versus inferred explanation:** Four points and three labels are direct visual observations. An erroneous fourth point, omitted date, forecast or template origin is an inferred explanation requiring a definition.
- **Classification:** Measure, label, or scale inconsistency; PLAN DOC-004 toolkit heading/date labels versus PLAN same panel's markers; primary P_P; all relationships P_P; review domain plan_material. Confirmed, no role/type repair; this is sample prospective audit-and-feedback content. Ambiguity: fourth point's time definition.
- **Evidence state:** recorded_candidate. Determining fact: direct current-source raster confirms the registered additional unlabeled position in measure 7, pending its named time definition.
- **Exact remaining human question:** Which date/window and population does the fourth My Hospital point in measure 7 represent, and should the three-month panel include a fourth labeled period or only three plotted points?


Coordinator handoff note: this exact prefix copy contains all 28 complete candidate fact records and the engine/source/classification/evidence-state introduction. Only the subsequent derivative-command provenance table and repeated coverage summary are omitted from this context-bound handoff. The full canonical evidence_recheck.md is preserved unchanged. No scientific candidate fact, definition, alternative or human question is omitted.
