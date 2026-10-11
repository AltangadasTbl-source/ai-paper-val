# Workflow 1.6 Mechanical Evidence Recheck

Scope: all 58 stable IDs C001–C058, retained separately and Pending Human Adjudication. Current supplied PDFs are final authority. Previous OCR/layout derivatives were only locators. This fresh recheck used direct CPU-only Poppler 26.01.0 pdftotext `-layout -f N -l N` from the exact current source PDF into preprocessing/recheck/{main,protocol,sap,results}-pN.txt; targeted current-source pdftoppm `-singlefile -png -f N -l N` produced 13 unique rendered pages (main1,3,4,10; protocol24,45; SAP14; results1,2,7,8,19,26), below the 32-page bound. Main renders 130 dpi, selected protocol/results 160 dpi, matrix/SAP 145 dpi. No fallback, OCR, Python helper, GPU, or external evidence was needed. No source or reusable artifact was changed.

All assigned printed inputs were located in fresh current-source exact-page text or current images. Each card below records all 12 contract facts separately. Operator/geometry/glyph confirmations include all 11 Figure 4 physical-axis confidence qualifiers, all 9 strict threshold comparisons plus the separate diastolic omission, each of the seven eFigure 2 bar pair, and protocol≤1 red-meat glyph. Results-supplement p8 is visually blank in the current source: it supplies no unseen comparator and does not license an omitted candidate. C037/C042/C043 keep separate ordering/intervention/control comparisons. All 58 evidence states are recorded_candidate because the assigned printed comparison reproduces or remains exactly conditional on a named missing definition. This does not establish the production mechanism or any human disposition. All 58 remain Pending Human Adjudication.

Classification: 48 report-only comparisons (41 S_W, 7 S_C), 9 plan-internal P_P, 1 P_R. C044–C050 primary category is corrected to Numeric or arithmetic inconsistency because same percentage is encoded as differing label and bar height; arm-label mismatch is only an explanation. Their domain changes mechanically to statistical_results. No document-role or primary-relationship correction is needed. A corroborating plan or Methods passage is not counted as a substantive discrepancy relationship. Conditional interpretations, adjusted rounding, exact-equality counts, and endpoint-specific baseline identity are explicit below.

## C001 — Abstract male percentage uses a different population denominator

**Status:** Pending Human Adjudication. **Primary category:** Denominator, proportion, or total inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** statistical_results. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p1](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=1) abstract Results; [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) Table 1 and Results. Both exact locations found.
- **Source printed value/text matched:** `Among 6874 randomized participants ... 3406 [52%] men` matched.
- **Comparator printed value/text matched:** Table 1 men 1702+1704=3406 and Results analyzed population 6583 matched.
- **Consistency rule applicable:** Within a stated population, percentage = 100 × count / denominator; ordinary whole-percent rounding is applicable if no different denominator is intended.
- **Calculation or logical comparison reproduced:** 3406/6874 ×100=49.549025%, rounding to 50%; 3406/6583 ×100=51.739329%, rounding to 52%. Thus the printed 52% aligns with the analyzed denominator rather than the abstract's grammatical 6874 denominator.
- **Necessary inputs available; exact missing inputs/definitions:** Counts and both denominators available. The randomized male count and intended parenthetical population are not separately supplied; 3406 is also the intervention randomized arm count, which does not establish a sex count.
- **Source-grounded alternative interpretation:** The parenthesis may describe analyzed participants while the introductory clause describes all randomized participants.
- **Direct observation versus inferred explanation:** Printed clause, count, percentage and Table 1 sex counts are direct observations. Population conflation or copying an arm count is an inferred mechanism only.
- **Exact remaining human question:** Does the 3406 [52%] male summary describe 6583 analyzed participants or all 6874 randomized participants, and what is the sex count for the latter?
- **Document roles confirmed by content:** REPORT abstract Results; REPORT Table 1/Results in the same retrospective article.
- **Relationship type and all relationships confirmed/corrected:** Same REPORT document discrepancy: S_W only; no PLAN comparator. Category and statistical_results domain confirmed.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The count/percentage does not reconcile with the clause's 6874 denominator under usual rounding; the denominator question remains as registered.

## C002 — Abstract analysis population labeled as twelve-month completers

**Status:** Pending Human Adjudication. **Primary category:** Analysis-unit or population inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** statistical_results. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p1](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=1) abstract Results; [main physical p3](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=3) Figure 1; [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) Statistical Analysis/Results; [main physical p5](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5) Table 2 footnote a. All found.
- **Source printed value/text matched:** `6583 (96%) completed the 12-month follow-up and were included in the main analysis` matched.
- **Comparator printed value/text matched:** Figure 1 main analysis 3272/3311, absent nutritional information at 12 months 439/368, completer-only analysis 2833/2943; Table 2 er-MedDiet 517 imputed at 12 months matched.
- **Consistency rule applicable:** An imputed analysis population must be distinguished from an observed outcome-completer population; attendance and measurement completeness are separate definitions.
- **Calculation or logical comparison reproduced:** 6874−134−157=6583; 3272+3311=6583; 2833+2943=5776 nutritional completers; 439+368=807 absent nutritional information; 6583−517=6066 observed er-MedDiet measurements, conditional on one score per person. 6583/6874=95.766657%, so 96% itself rounds correctly.
- **Necessary inputs available; exact missing inputs/definitions:** All printed counts available; person-level visit attendance and the abstract's operational completion definition unavailable.
- **Source-grounded alternative interpretation:** A participant can attend a 12-month visit while lacking nutrition/score data; the abstract may use attendance completion rather than complete outcome measurement.
- **Direct observation versus inferred explanation:** Observed analysis/completer count distinctions are direct. Equating absent nutrition with absent visit would be an unsupported inference and is not made.
- **Exact remaining human question:** What attendance or completion definition supports 6583 twelve-month completers, and how does it distinguish visit attendance, observed nutrition, and the imputed analysis population?
- **Document roles confirmed by content:** REPORT abstract, Figure 1, analysis text and Table 2 in one article.
- **Relationship type and all relationships confirmed/corrected:** S_W only. Secondary analysis-unit category is justified by a concrete 6583 completion/population label; statistical_results confirmed.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The printed completion label remains conditionally inconsistent with the declared analysis/completer definitions; missing attendance definition is named.

## C003 — Twelve-month nutritional imputation percentage and rounding

**Status:** Pending Human Adjudication. **Primary category:** Denominator, proportion, or total inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** statistical_results. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p3](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=3) Figure 1; [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) Results; [main physical p5](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5) Table 2 footnote a; [main physical p8](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=8) Table 3 footnote a. All found.
- **Source printed value/text matched:** Results `12.7% at 6 months and 12.2% at 12 months` matched.
- **Comparator printed value/text matched:** Main N=6583; 439+368=807; Table 2 MDS/MEDAS/PDQS and Table 3 all energy variables each have 807 imputed at 12 months, 838 at 6 months, matched.
- **Consistency rule applicable:** For the stated 6583-person measurement denominator, ordinary nearest rounding at one decimal must follow count/denominator.
- **Calculation or logical comparison reproduced:** 807/6583×100=12.25884855%, nearest one decimal 12.3; 838/6583×100=12.729758%, nearest 12.7. The 12-month percentage lies beyond 12.2's ordinary rounding interval [12.15,12.25).
- **Necessary inputs available; exact missing inputs/definitions:** Printed numerator and analysis N available. The Results percentage's exact measurement denominator and rounding/truncation policy are not specified.
- **Source-grounded alternative interpretation:** 12.2 may be truncation to one decimal, or a percentage of a different pool of measurements; that definition would change the comparison.
- **Direct observation versus inferred explanation:** Printed percentage and counts direct; rounding diagnostic conditional on the stated participant/measurement denominator, not a claim that all variable-specific missingness must be identical.
- **Exact remaining human question:** Was 12.2% truncated, calculated with another denominator, or intended to represent ordinary nearest-rounded 807/6583?
- **Document roles confirmed by content:** REPORT flow, Results, and table footnotes within the article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; category and statistical_results confirmed.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Count/denominator diagnostic reproduces the registered rounding discrepancy; exact percentage denominator/policy remains to be defined.

## C004 — Intervention university education percentage and rounding

**Status:** Pending Human Adjudication. **Primary category:** Denominator, proportion, or total inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** statistical_results. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) Table 1 Education, intervention column. Exact row/denominator found and current image checked.
- **Source printed value/text matched:** Education n=3240; University 703 (21) matched.
- **Comparator printed value/text matched:** Primary 1540 (48), Secondary 997 (31), and education denominator 3240 matched.
- **Consistency rule applicable:** Ordinary independent nearest whole-percent rounding is a comparator, while an explicitly declared sum-preserving allocation could differ.
- **Calculation or logical comparison reproduced:** 703/3240×100=21.697531%, nearest 22%; counts1540+997+703=3240. Exact shares47.530864%,30.771605%,21.697531%; independent rounded shares48,31,22 sum101. Largest-remainder allocation floors47,30,21 and adds to secondary/university, yielding47,31,22, not48,31,21. The printed48,31,21 sum100 but require another adjustment convention.
- **Necessary inputs available; exact missing inputs/definitions:** All counts available; deliberate adjusted rounding/percentage allocation policy absent.
- **Source-grounded alternative interpretation:** An author may retain the first two independently rounded cells and adjust the last to force100%; this reproduces48,31,21 but is not largest remainder.
- **Direct observation versus inferred explanation:** Printed21% and counts direct; the candidate concerns ordinary rounding. A particular production convention is inferred, never established.
- **Exact remaining human question:** Was university21% an intentional sum-preserving adjustment, and what precise percentage allocation rule was applied?
- **Document roles confirmed by content:** REPORT Table 1 cells and denominator within one article.
- **Relationship type and all relationships confirmed/corrected:** S_W, statistical_results and category confirmed. Corrected checker explanatory arithmetic does not create a new relationship or alter source values.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The source's21 differs from usual22; correction to the checker's largest-remainder explanation leaves the same registered conditional rounding question.

## C005 — Control secondary education percentage and rounding

**Status:** Pending Human Adjudication. **Primary category:** Denominator, proportion, or total inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** statistical_results. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) Table 1 Education, control column. Exact row/denominator found and current image checked.
- **Source printed value/text matched:** Education n=3285; Secondary902 (28) matched.
- **Comparator printed value/text matched:** Primary1647 (50), University736 (22) and denominator3285 matched.
- **Consistency rule applicable:** Nearest whole-percent rounding and explicitly declared sum-preserving allocation must be distinguished.
- **Calculation or logical comparison reproduced:** 902/3285×100=27.458143%, nearest27%;1647+902+736=3285. Exact shares50.136986%,27.458143%,22.404871%; independent rounded50,27,22 sum99. Largest remainder assigns the extra point to secondary, producing50,28,22 exactly as printed.
- **Necessary inputs available; exact missing inputs/definitions:** All arithmetic inputs available; the source's percentage allocation convention is absent.
- **Source-grounded alternative interpretation:** Intentional largest-remainder rounding to100% fully explains the printed control cells; without a stated convention, the registered ordinary-rounding question remains conditional.
- **Direct observation versus inferred explanation:** Printed28% and counts direct. Deliberate sum-preserving rounding is a reproducible alternative, not evidence that the authors used it.
- **Exact remaining human question:** Did Table 1 deliberately use adjusted whole percentages summing100%, and was the same specified rule applied in both education columns?
- **Document roles confirmed by content:** REPORT Table 1 cells and denominator within one article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; category/statistical_results confirmed. A coherent alternative does not remove a missing rounding-policy question from the assigned ID.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The stated ordinary independent-rounding difference reproduces; the exact adjusted-rounding alternative is documented rather than silently treated as a defect.

## C006 — Figure 3 mean-versus-median summary labels

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p8](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=8) Risk Factors first paragraph; [main physical p9](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=9) Figure 3 caption. Both found.
- **Source printed value/text matched:** `The mean changes after 6 and 12 months ... are presented in Figure 3 and Figure 4` matched.
- **Comparator printed value/text matched:** Figure 3 caption `middle line represents the within-group median change in observed risk factors`, boxes IQR and whiskers observed extremes within1.5IQR, matched.
- **Consistency rule applicable:** Mean and median denote different descriptive statistics; the narrative explicitly points to the figure.
- **Calculation or logical comparison reproduced:** Logical comparison: the narrative names mean changes while the Figure 3 central line is defined as a median. No arithmetic or geometric digitization needed; zero tolerance for statistic identity.
- **Necessary inputs available; exact missing inputs/definitions:** Both labels and referential sentence available; actual summary-producing code and author intent absent.
- **Source-grounded alternative interpretation:** The narrative may refer generally to companion mean-model estimates and figures as a results presentation, with the figure caption supplying the precise median definition.
- **Direct observation versus inferred explanation:** Both labels direct. A drafting shorthand or wrong plotted statistic is only an inferred explanation; no actual mean or median is reconstructed.
- **Exact remaining human question:** Does the narrative mean companion model means, or should its reference to Figure 3 identify the plotted central summaries as medians?
- **Document roles confirmed by content:** REPORT Risk Factors narrative and REPORT Figure 3 caption in one article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; measure category/report_internal_inconsistency confirmed.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Exact referred-to mean label and explicit median definition reproduce the assigned labeling comparison.

## C007 — Body weight Figure 4 confidence label and boxplot definition

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 Body weight physical-axis label and common caption. Both found; current source image individually checked for this panel.
- **Source printed value/text matched:** Axis `Body Weight Change, kg (95% CI)` matched.
- **Comparator printed value/text matched:** Caption defines median change, boxes IQR, whiskers extreme observed values within1.5×IQR of nearer quartile, and dots observed values outside that range. Separate percentage column I 40.6 (38.7–42.5), C 12.2 (11.0–13.5) carries its own95%CI label; matched.
- **Consistency rule applicable:** A descriptive observed distribution (median/IQR/whiskers) is a different quantity from an inferential95%confidence interval. Axis label and caption assign competing meanings to the plotted quantity.
- **Calculation or logical comparison reproduced:** Logical comparison reproduced for this named axis: the95%CI qualifier is printed on the physical-unit axis but the caption defines distribution marks. No inferred confidence endpoints, raw measurements, or graphical digitization are needed; statistic-type identity has no rounding tolerance.
- **Necessary inputs available; exact missing inputs/definitions:** All labels and graphic definitions available. Which graphic object the physical-axis95%CI qualifier was intended to describe is not stated.
- **Source-grounded alternative interpretation:** The axis qualifier may have been intended for the adjacent participant-percentage confidence intervals; the figure separately labels that percentage quantity.
- **Direct observation versus inferred explanation:** Axis text, box marks, caption, and separate percentage intervals are direct observations. A misplaced qualifier is an inference only, not a claim that the plotted endpoints are inferentially wrong.
- **Exact remaining human question:** Which Body weight graphic elements, if any, are intended as95%confidence intervals, given the caption's median/IQR definition?
- **Document roles confirmed by content:** REPORT axis and REPORT caption in one results figure/article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; category and report_internal_inconsistency confirmed. No plan or separate report discrepancy is compared.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Exact axis confidence qualifier and descriptive-caption definition reproduce the registered quantity-label comparison.

## C008 — Waist circumference Figure 4 confidence label and boxplot definition

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 Waist circumference physical-axis label and common caption. Both found; current source image individually checked for this panel.
- **Source printed value/text matched:** Axis `Waist Circumference Change, cm (95% CI)` matched.
- **Comparator printed value/text matched:** Caption defines median change, boxes IQR, whiskers extreme observed values within1.5×IQR of nearer quartile, and dots observed values outside that range. Separate percentage column I 39.5 (37.6–41.3), C 13.5 (12.2–14.8) carries its own95%CI label; matched.
- **Consistency rule applicable:** A descriptive observed distribution (median/IQR/whiskers) is a different quantity from an inferential95%confidence interval. Axis label and caption assign competing meanings to the plotted quantity.
- **Calculation or logical comparison reproduced:** Logical comparison reproduced for this named axis: the95%CI qualifier is printed on the physical-unit axis but the caption defines distribution marks. No inferred confidence endpoints, raw measurements, or graphical digitization are needed; statistic-type identity has no rounding tolerance.
- **Necessary inputs available; exact missing inputs/definitions:** All labels and graphic definitions available. Which graphic object the physical-axis95%CI qualifier was intended to describe is not stated.
- **Source-grounded alternative interpretation:** The axis qualifier may have been intended for the adjacent participant-percentage confidence intervals; the figure separately labels that percentage quantity.
- **Direct observation versus inferred explanation:** Axis text, box marks, caption, and separate percentage intervals are direct observations. A misplaced qualifier is an inference only, not a claim that the plotted endpoints are inferentially wrong.
- **Exact remaining human question:** Which Waist circumference graphic elements, if any, are intended as95%confidence intervals, given the caption's median/IQR definition?
- **Document roles confirmed by content:** REPORT axis and REPORT caption in one results figure/article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; category and report_internal_inconsistency confirmed. No plan or separate report discrepancy is compared.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Exact axis confidence qualifier and descriptive-caption definition reproduce the registered quantity-label comparison.

## C009 — BMI Figure 4 confidence label and boxplot definition

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 BMI physical-axis label and common caption. Both found; current source image individually checked for this panel.
- **Source printed value/text matched:** Axis `Body Mass Index, kg/m² (95% CI)` matched.
- **Comparator printed value/text matched:** Caption defines median change, boxes IQR, whiskers extreme observed values within1.5×IQR of nearer quartile, and dots observed values outside that range. Separate percentage column I 40.5 (38.6–42.4), C 12.5 (11.3–13.8) carries its own95%CI label; matched.
- **Consistency rule applicable:** A descriptive observed distribution (median/IQR/whiskers) is a different quantity from an inferential95%confidence interval. Axis label and caption assign competing meanings to the plotted quantity.
- **Calculation or logical comparison reproduced:** Logical comparison reproduced for this named axis: the95%CI qualifier is printed on the physical-unit axis but the caption defines distribution marks. No inferred confidence endpoints, raw measurements, or graphical digitization are needed; statistic-type identity has no rounding tolerance.
- **Necessary inputs available; exact missing inputs/definitions:** All labels and graphic definitions available. Which graphic object the physical-axis95%CI qualifier was intended to describe is not stated.
- **Source-grounded alternative interpretation:** The axis qualifier may have been intended for the adjacent participant-percentage confidence intervals; the figure separately labels that percentage quantity.
- **Direct observation versus inferred explanation:** Axis text, box marks, caption, and separate percentage intervals are direct observations. A misplaced qualifier is an inference only, not a claim that the plotted endpoints are inferentially wrong.
- **Exact remaining human question:** Which BMI graphic elements, if any, are intended as95%confidence intervals, given the caption's median/IQR definition?
- **Document roles confirmed by content:** REPORT axis and REPORT caption in one results figure/article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; category and report_internal_inconsistency confirmed. No plan or separate report discrepancy is compared.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Exact axis confidence qualifier and descriptive-caption definition reproduce the registered quantity-label comparison.

## C010 — Total cholesterol Figure 4 confidence label and boxplot definition

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 Total cholesterol physical-axis label and common caption. Both found; current source image individually checked for this panel.
- **Source printed value/text matched:** Axis `Total Cholesterol Change, mg/dL (95% CI)` matched.
- **Comparator printed value/text matched:** Caption defines median change, boxes IQR, whiskers extreme observed values within1.5×IQR of nearer quartile, and dots observed values outside that range. Separate percentage column I 37.5 (35.7–39.4), C 34.3 (32.5–36.1) carries its own95%CI label; matched.
- **Consistency rule applicable:** A descriptive observed distribution (median/IQR/whiskers) is a different quantity from an inferential95%confidence interval. Axis label and caption assign competing meanings to the plotted quantity.
- **Calculation or logical comparison reproduced:** Logical comparison reproduced for this named axis: the95%CI qualifier is printed on the physical-unit axis but the caption defines distribution marks. No inferred confidence endpoints, raw measurements, or graphical digitization are needed; statistic-type identity has no rounding tolerance.
- **Necessary inputs available; exact missing inputs/definitions:** All labels and graphic definitions available. Which graphic object the physical-axis95%CI qualifier was intended to describe is not stated.
- **Source-grounded alternative interpretation:** The axis qualifier may have been intended for the adjacent participant-percentage confidence intervals; the figure separately labels that percentage quantity.
- **Direct observation versus inferred explanation:** Axis text, box marks, caption, and separate percentage intervals are direct observations. A misplaced qualifier is an inference only, not a claim that the plotted endpoints are inferentially wrong.
- **Exact remaining human question:** Which Total cholesterol graphic elements, if any, are intended as95%confidence intervals, given the caption's median/IQR definition?
- **Document roles confirmed by content:** REPORT axis and REPORT caption in one results figure/article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; category and report_internal_inconsistency confirmed. No plan or separate report discrepancy is compared.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Exact axis confidence qualifier and descriptive-caption definition reproduce the registered quantity-label comparison.

## C011 — HDL cholesterol Figure 4 confidence label and boxplot definition

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 HDL cholesterol physical-axis label and common caption. Both found; current source image individually checked for this panel.
- **Source printed value/text matched:** Axis `HDL Cholesterol Change, mg/dL (95% CI)` matched.
- **Comparator printed value/text matched:** Caption defines median change, boxes IQR, whiskers extreme observed values within1.5×IQR of nearer quartile, and dots observed values outside that range. Separate percentage column I 45.6 (43.7–47.6), C 40.0 (38.1–41.8) carries its own95%CI label; matched.
- **Consistency rule applicable:** A descriptive observed distribution (median/IQR/whiskers) is a different quantity from an inferential95%confidence interval. Axis label and caption assign competing meanings to the plotted quantity.
- **Calculation or logical comparison reproduced:** Logical comparison reproduced for this named axis: the95%CI qualifier is printed on the physical-unit axis but the caption defines distribution marks. No inferred confidence endpoints, raw measurements, or graphical digitization are needed; statistic-type identity has no rounding tolerance.
- **Necessary inputs available; exact missing inputs/definitions:** All labels and graphic definitions available. Which graphic object the physical-axis95%CI qualifier was intended to describe is not stated.
- **Source-grounded alternative interpretation:** The axis qualifier may have been intended for the adjacent participant-percentage confidence intervals; the figure separately labels that percentage quantity.
- **Direct observation versus inferred explanation:** Axis text, box marks, caption, and separate percentage intervals are direct observations. A misplaced qualifier is an inference only, not a claim that the plotted endpoints are inferentially wrong.
- **Exact remaining human question:** Which HDL cholesterol graphic elements, if any, are intended as95%confidence intervals, given the caption's median/IQR definition?
- **Document roles confirmed by content:** REPORT axis and REPORT caption in one results figure/article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; category and report_internal_inconsistency confirmed. No plan or separate report discrepancy is compared.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Exact axis confidence qualifier and descriptive-caption definition reproduce the registered quantity-label comparison.

## C012 — LDL cholesterol Figure 4 confidence label and boxplot definition

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 LDL cholesterol physical-axis label and common caption. Both found; current source image individually checked for this panel.
- **Source printed value/text matched:** Axis `LDL Cholesterol Change, mg/dL (95% CI)` matched.
- **Comparator printed value/text matched:** Caption defines median change, boxes IQR, whiskers extreme observed values within1.5×IQR of nearer quartile, and dots observed values outside that range. Separate percentage column I 41.4 (39.5–43.3), C 40.2 (38.3–42.1) carries its own95%CI label; matched.
- **Consistency rule applicable:** A descriptive observed distribution (median/IQR/whiskers) is a different quantity from an inferential95%confidence interval. Axis label and caption assign competing meanings to the plotted quantity.
- **Calculation or logical comparison reproduced:** Logical comparison reproduced for this named axis: the95%CI qualifier is printed on the physical-unit axis but the caption defines distribution marks. No inferred confidence endpoints, raw measurements, or graphical digitization are needed; statistic-type identity has no rounding tolerance.
- **Necessary inputs available; exact missing inputs/definitions:** All labels and graphic definitions available. Which graphic object the physical-axis95%CI qualifier was intended to describe is not stated.
- **Source-grounded alternative interpretation:** The axis qualifier may have been intended for the adjacent participant-percentage confidence intervals; the figure separately labels that percentage quantity.
- **Direct observation versus inferred explanation:** Axis text, box marks, caption, and separate percentage intervals are direct observations. A misplaced qualifier is an inference only, not a claim that the plotted endpoints are inferentially wrong.
- **Exact remaining human question:** Which LDL cholesterol graphic elements, if any, are intended as95%confidence intervals, given the caption's median/IQR definition?
- **Document roles confirmed by content:** REPORT axis and REPORT caption in one results figure/article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; category and report_internal_inconsistency confirmed. No plan or separate report discrepancy is compared.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Exact axis confidence qualifier and descriptive-caption definition reproduce the registered quantity-label comparison.

## C013 — Non-HDL cholesterol Figure 4 confidence label and boxplot definition

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 Non-HDL cholesterol physical-axis label and common caption. Both found; current source image individually checked for this panel.
- **Source printed value/text matched:** Axis `Non-HDL Cholesterol Change, mg/dL (95% CI)` matched.
- **Comparator printed value/text matched:** Caption defines median change, boxes IQR, whiskers extreme observed values within1.5×IQR of nearer quartile, and dots observed values outside that range. Separate percentage column I 43.6 (41.7–45.5), C 37.5 (35.7–39.4) carries its own95%CI label; matched.
- **Consistency rule applicable:** A descriptive observed distribution (median/IQR/whiskers) is a different quantity from an inferential95%confidence interval. Axis label and caption assign competing meanings to the plotted quantity.
- **Calculation or logical comparison reproduced:** Logical comparison reproduced for this named axis: the95%CI qualifier is printed on the physical-unit axis but the caption defines distribution marks. No inferred confidence endpoints, raw measurements, or graphical digitization are needed; statistic-type identity has no rounding tolerance.
- **Necessary inputs available; exact missing inputs/definitions:** All labels and graphic definitions available. Which graphic object the physical-axis95%CI qualifier was intended to describe is not stated.
- **Source-grounded alternative interpretation:** The axis qualifier may have been intended for the adjacent participant-percentage confidence intervals; the figure separately labels that percentage quantity.
- **Direct observation versus inferred explanation:** Axis text, box marks, caption, and separate percentage intervals are direct observations. A misplaced qualifier is an inference only, not a claim that the plotted endpoints are inferentially wrong.
- **Exact remaining human question:** Which Non-HDL cholesterol graphic elements, if any, are intended as95%confidence intervals, given the caption's median/IQR definition?
- **Document roles confirmed by content:** REPORT axis and REPORT caption in one results figure/article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; category and report_internal_inconsistency confirmed. No plan or separate report discrepancy is compared.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Exact axis confidence qualifier and descriptive-caption definition reproduce the registered quantity-label comparison.

## C014 — Total-to-HDL cholesterol ratio Figure 4 confidence label and boxplot definition

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 Total-to-HDL cholesterol ratio physical-axis label and common caption. Both found; current source image individually checked for this panel.
- **Source printed value/text matched:** Axis `Total Cholesterol/HDL Ratio Change (95% CI)` matched.
- **Comparator printed value/text matched:** Caption defines median change, boxes IQR, whiskers extreme observed values within1.5×IQR of nearer quartile, and dots observed values outside that range. Separate percentage column I 48.4 (46.5–50.4), C 41.3 (39.4–43.2) carries its own95%CI label; matched.
- **Consistency rule applicable:** A descriptive observed distribution (median/IQR/whiskers) is a different quantity from an inferential95%confidence interval. Axis label and caption assign competing meanings to the plotted quantity.
- **Calculation or logical comparison reproduced:** Logical comparison reproduced for this named axis: the95%CI qualifier is printed on the physical-unit axis but the caption defines distribution marks. No inferred confidence endpoints, raw measurements, or graphical digitization are needed; statistic-type identity has no rounding tolerance.
- **Necessary inputs available; exact missing inputs/definitions:** All labels and graphic definitions available. Which graphic object the physical-axis95%CI qualifier was intended to describe is not stated.
- **Source-grounded alternative interpretation:** The axis qualifier may have been intended for the adjacent participant-percentage confidence intervals; the figure separately labels that percentage quantity.
- **Direct observation versus inferred explanation:** Axis text, box marks, caption, and separate percentage intervals are direct observations. A misplaced qualifier is an inference only, not a claim that the plotted endpoints are inferentially wrong.
- **Exact remaining human question:** Which Total-to-HDL cholesterol ratio graphic elements, if any, are intended as95%confidence intervals, given the caption's median/IQR definition?
- **Document roles confirmed by content:** REPORT axis and REPORT caption in one results figure/article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; category and report_internal_inconsistency confirmed. No plan or separate report discrepancy is compared.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Exact axis confidence qualifier and descriptive-caption definition reproduce the registered quantity-label comparison.

## C015 — Triglycerides Figure 4 confidence label and boxplot definition

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 Triglycerides physical-axis label and common caption. Both found; current source image individually checked for this panel.
- **Source printed value/text matched:** Axis `Triglycerides Change, mg/dL (95% CI)` matched.
- **Comparator printed value/text matched:** Caption defines median change, boxes IQR, whiskers extreme observed values within1.5×IQR of nearer quartile, and dots observed values outside that range. Separate percentage column I 47.3 (45.4–49.2), C 38.2 (36.3–40.0) carries its own95%CI label; matched.
- **Consistency rule applicable:** A descriptive observed distribution (median/IQR/whiskers) is a different quantity from an inferential95%confidence interval. Axis label and caption assign competing meanings to the plotted quantity.
- **Calculation or logical comparison reproduced:** Logical comparison reproduced for this named axis: the95%CI qualifier is printed on the physical-unit axis but the caption defines distribution marks. No inferred confidence endpoints, raw measurements, or graphical digitization are needed; statistic-type identity has no rounding tolerance.
- **Necessary inputs available; exact missing inputs/definitions:** All labels and graphic definitions available. Which graphic object the physical-axis95%CI qualifier was intended to describe is not stated.
- **Source-grounded alternative interpretation:** The axis qualifier may have been intended for the adjacent participant-percentage confidence intervals; the figure separately labels that percentage quantity.
- **Direct observation versus inferred explanation:** Axis text, box marks, caption, and separate percentage intervals are direct observations. A misplaced qualifier is an inference only, not a claim that the plotted endpoints are inferentially wrong.
- **Exact remaining human question:** Which Triglycerides graphic elements, if any, are intended as95%confidence intervals, given the caption's median/IQR definition?
- **Document roles confirmed by content:** REPORT axis and REPORT caption in one results figure/article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; category and report_internal_inconsistency confirmed. No plan or separate report discrepancy is compared.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Exact axis confidence qualifier and descriptive-caption definition reproduce the registered quantity-label comparison.

## C016 — Systolic blood pressure Figure 4 confidence label and boxplot definition

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 Systolic blood pressure physical-axis label and common caption. Both found; current source image individually checked for this panel.
- **Source printed value/text matched:** Axis `Systolic Blood Pressure Change, mm Hg (95% CI)` matched.
- **Comparator printed value/text matched:** Caption defines median change, boxes IQR, whiskers extreme observed values within1.5×IQR of nearer quartile, and dots observed values outside that range. Separate percentage column I 47.5 (45.6–49.5), C 41.8 (39.9–43.7) carries its own95%CI label; matched.
- **Consistency rule applicable:** A descriptive observed distribution (median/IQR/whiskers) is a different quantity from an inferential95%confidence interval. Axis label and caption assign competing meanings to the plotted quantity.
- **Calculation or logical comparison reproduced:** Logical comparison reproduced for this named axis: the95%CI qualifier is printed on the physical-unit axis but the caption defines distribution marks. No inferred confidence endpoints, raw measurements, or graphical digitization are needed; statistic-type identity has no rounding tolerance.
- **Necessary inputs available; exact missing inputs/definitions:** All labels and graphic definitions available. Which graphic object the physical-axis95%CI qualifier was intended to describe is not stated.
- **Source-grounded alternative interpretation:** The axis qualifier may have been intended for the adjacent participant-percentage confidence intervals; the figure separately labels that percentage quantity.
- **Direct observation versus inferred explanation:** Axis text, box marks, caption, and separate percentage intervals are direct observations. A misplaced qualifier is an inference only, not a claim that the plotted endpoints are inferentially wrong.
- **Exact remaining human question:** Which Systolic blood pressure graphic elements, if any, are intended as95%confidence intervals, given the caption's median/IQR definition?
- **Document roles confirmed by content:** REPORT axis and REPORT caption in one results figure/article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; category and report_internal_inconsistency confirmed. No plan or separate report discrepancy is compared.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Exact axis confidence qualifier and descriptive-caption definition reproduce the registered quantity-label comparison.

## C017 — Diastolic blood pressure Figure 4 confidence label and boxplot definition

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 Diastolic blood pressure physical-axis label and common caption. Both found; current source image individually checked for this panel.
- **Source printed value/text matched:** Axis `Diastolic Blood Pressure Change, mm Hg (95% CI)` matched.
- **Comparator printed value/text matched:** Caption defines median change, boxes IQR, whiskers extreme observed values within1.5×IQR of nearer quartile, and dots observed values outside that range. Separate percentage column I 48.1 (46.2–50.1), C 44.3 (42.4–46.2) carries its own95%CI label; matched.
- **Consistency rule applicable:** A descriptive observed distribution (median/IQR/whiskers) is a different quantity from an inferential95%confidence interval. Axis label and caption assign competing meanings to the plotted quantity.
- **Calculation or logical comparison reproduced:** Logical comparison reproduced for this named axis: the95%CI qualifier is printed on the physical-unit axis but the caption defines distribution marks. No inferred confidence endpoints, raw measurements, or graphical digitization are needed; statistic-type identity has no rounding tolerance.
- **Necessary inputs available; exact missing inputs/definitions:** All labels and graphic definitions available. Which graphic object the physical-axis95%CI qualifier was intended to describe is not stated.
- **Source-grounded alternative interpretation:** The axis qualifier may have been intended for the adjacent participant-percentage confidence intervals; the figure separately labels that percentage quantity.
- **Direct observation versus inferred explanation:** Axis text, box marks, caption, and separate percentage intervals are direct observations. A misplaced qualifier is an inference only, not a claim that the plotted endpoints are inferentially wrong.
- **Exact remaining human question:** Which Diastolic blood pressure graphic elements, if any, are intended as95%confidence intervals, given the caption's median/IQR definition?
- **Document roles confirmed by content:** REPORT axis and REPORT caption in one results figure/article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; category and report_internal_inconsistency confirmed. No plan or separate report discrepancy is compared.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Exact axis confidence qualifier and descriptive-caption definition reproduce the registered quantity-label comparison.

## C018 — Body weight meaningful-change threshold boundary

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) Outcomes meaningful-risk-factor-change paragraph; [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 Body weight percentage header. Both found; current images checked.
- **Source printed value/text matched:** Methods reduction `at least 5%` matched.
- **Comparator printed value/text matched:** Figure header `Reduction >5%`; I 40.6 (38.7–42.5), C 12.2 (11.0–13.5), matched for this panel.
- **Consistency rule applicable:** Inclusive at-least (≥) and strict greater-than (>) rules assign different membership at exact equality; the displayed participant percentage's definition depends on that operator.
- **Calculation or logical comparison reproduced:** At change exactly 5%, the Methods rule includes the participant but the figure header excludes that participant. Printed operator comparison reproduced; zero tolerance for definition identity. Actual percentage difference equals boundary-count/denominator×100 and cannot be computed without that count.
- **Necessary inputs available; exact missing inputs/definitions:** Both operator definitions and percentages available. Arm-specific exact-equality counts, measurement precision/unrounded changes, operational classification code and percentage denominators are not supplied.
- **Source-grounded alternative interpretation:** If no participant equals the threshold, both rules give the same percentages; a strict header might also abbreviate an inclusive operational rule.
- **Direct observation versus inferred explanation:** Printed operators and percentages direct; a changed trial proportion or implementation error is not directly observed and is not inferred.
- **Exact remaining human question:** For Body weight, was the percentage computed using ≥ or >5%, at what precision, and how many participants lay exactly at the boundary?
- **Document roles confirmed by content:** REPORT Methods and REPORT Figure 4 within the same retrospective article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; measure category and report_internal_inconsistency confirmed. No PLAN material is a discrepancy comparator.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The exact inclusive-versus-strict printed boundary mismatch remains as registered pending operational definition and equality counts.

## C019 — Waist circumference meaningful-change threshold boundary

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) Outcomes meaningful-risk-factor-change paragraph; [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 Waist circumference percentage header. Both found; current images checked.
- **Source printed value/text matched:** Methods reduction `at least 5%` matched.
- **Comparator printed value/text matched:** Figure header `Reduction >5%`; I 39.5 (37.6–41.3), C 13.5 (12.2–14.8), matched for this panel.
- **Consistency rule applicable:** Inclusive at-least (≥) and strict greater-than (>) rules assign different membership at exact equality; the displayed participant percentage's definition depends on that operator.
- **Calculation or logical comparison reproduced:** At change exactly 5%, the Methods rule includes the participant but the figure header excludes that participant. Printed operator comparison reproduced; zero tolerance for definition identity. Actual percentage difference equals boundary-count/denominator×100 and cannot be computed without that count.
- **Necessary inputs available; exact missing inputs/definitions:** Both operator definitions and percentages available. Arm-specific exact-equality counts, measurement precision/unrounded changes, operational classification code and percentage denominators are not supplied.
- **Source-grounded alternative interpretation:** If no participant equals the threshold, both rules give the same percentages; a strict header might also abbreviate an inclusive operational rule.
- **Direct observation versus inferred explanation:** Printed operators and percentages direct; a changed trial proportion or implementation error is not directly observed and is not inferred.
- **Exact remaining human question:** For Waist circumference, was the percentage computed using ≥ or >5%, at what precision, and how many participants lay exactly at the boundary?
- **Document roles confirmed by content:** REPORT Methods and REPORT Figure 4 within the same retrospective article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; measure category and report_internal_inconsistency confirmed. No PLAN material is a discrepancy comparator.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The exact inclusive-versus-strict printed boundary mismatch remains as registered pending operational definition and equality counts.

## C020 — BMI meaningful-change threshold boundary

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) Outcomes meaningful-risk-factor-change paragraph; [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 BMI percentage header. Both found; current images checked.
- **Source printed value/text matched:** Methods reduction `at least 5%` matched.
- **Comparator printed value/text matched:** Figure header `Reduction >5%`; I 40.5 (38.6–42.4), C 12.5 (11.3–13.8), matched for this panel.
- **Consistency rule applicable:** Inclusive at-least (≥) and strict greater-than (>) rules assign different membership at exact equality; the displayed participant percentage's definition depends on that operator.
- **Calculation or logical comparison reproduced:** At change exactly 5%, the Methods rule includes the participant but the figure header excludes that participant. Printed operator comparison reproduced; zero tolerance for definition identity. Actual percentage difference equals boundary-count/denominator×100 and cannot be computed without that count.
- **Necessary inputs available; exact missing inputs/definitions:** Both operator definitions and percentages available. Arm-specific exact-equality counts, measurement precision/unrounded changes, operational classification code and percentage denominators are not supplied.
- **Source-grounded alternative interpretation:** If no participant equals the threshold, both rules give the same percentages; a strict header might also abbreviate an inclusive operational rule.
- **Direct observation versus inferred explanation:** Printed operators and percentages direct; a changed trial proportion or implementation error is not directly observed and is not inferred.
- **Exact remaining human question:** For BMI, was the percentage computed using ≥ or >5%, at what precision, and how many participants lay exactly at the boundary?
- **Document roles confirmed by content:** REPORT Methods and REPORT Figure 4 within the same retrospective article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; measure category and report_internal_inconsistency confirmed. No PLAN material is a discrepancy comparator.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The exact inclusive-versus-strict printed boundary mismatch remains as registered pending operational definition and equality counts.

## C021 — Total cholesterol meaningful-change threshold boundary

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) Outcomes meaningful-risk-factor-change paragraph; [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 Total cholesterol percentage header. Both found; current images checked.
- **Source printed value/text matched:** Methods reduction `at least 5%` matched.
- **Comparator printed value/text matched:** Figure header `Reduction >5%`; I 37.5 (35.7–39.4), C 34.3 (32.5–36.1), matched for this panel.
- **Consistency rule applicable:** Inclusive at-least (≥) and strict greater-than (>) rules assign different membership at exact equality; the displayed participant percentage's definition depends on that operator.
- **Calculation or logical comparison reproduced:** At change exactly 5%, the Methods rule includes the participant but the figure header excludes that participant. Printed operator comparison reproduced; zero tolerance for definition identity. Actual percentage difference equals boundary-count/denominator×100 and cannot be computed without that count.
- **Necessary inputs available; exact missing inputs/definitions:** Both operator definitions and percentages available. Arm-specific exact-equality counts, measurement precision/unrounded changes, operational classification code and percentage denominators are not supplied.
- **Source-grounded alternative interpretation:** If no participant equals the threshold, both rules give the same percentages; a strict header might also abbreviate an inclusive operational rule.
- **Direct observation versus inferred explanation:** Printed operators and percentages direct; a changed trial proportion or implementation error is not directly observed and is not inferred.
- **Exact remaining human question:** For Total cholesterol, was the percentage computed using ≥ or >5%, at what precision, and how many participants lay exactly at the boundary?
- **Document roles confirmed by content:** REPORT Methods and REPORT Figure 4 within the same retrospective article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; measure category and report_internal_inconsistency confirmed. No PLAN material is a discrepancy comparator.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The exact inclusive-versus-strict printed boundary mismatch remains as registered pending operational definition and equality counts.

## C022 — HDL cholesterol meaningful-change threshold boundary

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) Outcomes meaningful-risk-factor-change paragraph; [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 HDL cholesterol percentage header. Both found; current images checked.
- **Source printed value/text matched:** Methods increase `at least 5%` matched.
- **Comparator printed value/text matched:** Figure header `Increase >5%`; I 45.6 (43.7–47.6), C 40.0 (38.1–41.8), matched for this panel.
- **Consistency rule applicable:** Inclusive at-least (≥) and strict greater-than (>) rules assign different membership at exact equality; the displayed participant percentage's definition depends on that operator.
- **Calculation or logical comparison reproduced:** At change exactly 5%, the Methods rule includes the participant but the figure header excludes that participant. Printed operator comparison reproduced; zero tolerance for definition identity. Actual percentage difference equals boundary-count/denominator×100 and cannot be computed without that count.
- **Necessary inputs available; exact missing inputs/definitions:** Both operator definitions and percentages available. Arm-specific exact-equality counts, measurement precision/unrounded changes, operational classification code and percentage denominators are not supplied.
- **Source-grounded alternative interpretation:** If no participant equals the threshold, both rules give the same percentages; a strict header might also abbreviate an inclusive operational rule.
- **Direct observation versus inferred explanation:** Printed operators and percentages direct; a changed trial proportion or implementation error is not directly observed and is not inferred.
- **Exact remaining human question:** For HDL cholesterol, was the percentage computed using ≥ or >5%, at what precision, and how many participants lay exactly at the boundary?
- **Document roles confirmed by content:** REPORT Methods and REPORT Figure 4 within the same retrospective article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; measure category and report_internal_inconsistency confirmed. No PLAN material is a discrepancy comparator.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The exact inclusive-versus-strict printed boundary mismatch remains as registered pending operational definition and equality counts.

## C023 — LDL cholesterol meaningful-change threshold boundary

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) Outcomes meaningful-risk-factor-change paragraph; [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 LDL cholesterol percentage header. Both found; current images checked.
- **Source printed value/text matched:** Methods reduction `at least 5%` matched.
- **Comparator printed value/text matched:** Figure header `Reduction >5%`; I 41.4 (39.5–43.3), C 40.2 (38.3–42.1), matched for this panel.
- **Consistency rule applicable:** Inclusive at-least (≥) and strict greater-than (>) rules assign different membership at exact equality; the displayed participant percentage's definition depends on that operator.
- **Calculation or logical comparison reproduced:** At change exactly 5%, the Methods rule includes the participant but the figure header excludes that participant. Printed operator comparison reproduced; zero tolerance for definition identity. Actual percentage difference equals boundary-count/denominator×100 and cannot be computed without that count.
- **Necessary inputs available; exact missing inputs/definitions:** Both operator definitions and percentages available. Arm-specific exact-equality counts, measurement precision/unrounded changes, operational classification code and percentage denominators are not supplied.
- **Source-grounded alternative interpretation:** If no participant equals the threshold, both rules give the same percentages; a strict header might also abbreviate an inclusive operational rule.
- **Direct observation versus inferred explanation:** Printed operators and percentages direct; a changed trial proportion or implementation error is not directly observed and is not inferred.
- **Exact remaining human question:** For LDL cholesterol, was the percentage computed using ≥ or >5%, at what precision, and how many participants lay exactly at the boundary?
- **Document roles confirmed by content:** REPORT Methods and REPORT Figure 4 within the same retrospective article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; measure category and report_internal_inconsistency confirmed. No PLAN material is a discrepancy comparator.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The exact inclusive-versus-strict printed boundary mismatch remains as registered pending operational definition and equality counts.

## C024 — Non-HDL cholesterol meaningful-change threshold boundary

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) Outcomes meaningful-risk-factor-change paragraph; [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 Non-HDL cholesterol percentage header. Both found; current images checked.
- **Source printed value/text matched:** Methods reduction `at least 5%` matched.
- **Comparator printed value/text matched:** Figure header `Reduction >5%`; I 43.6 (41.7–45.5), C 37.5 (35.7–39.4), matched for this panel.
- **Consistency rule applicable:** Inclusive at-least (≥) and strict greater-than (>) rules assign different membership at exact equality; the displayed participant percentage's definition depends on that operator.
- **Calculation or logical comparison reproduced:** At change exactly 5%, the Methods rule includes the participant but the figure header excludes that participant. Printed operator comparison reproduced; zero tolerance for definition identity. Actual percentage difference equals boundary-count/denominator×100 and cannot be computed without that count.
- **Necessary inputs available; exact missing inputs/definitions:** Both operator definitions and percentages available. Arm-specific exact-equality counts, measurement precision/unrounded changes, operational classification code and percentage denominators are not supplied.
- **Source-grounded alternative interpretation:** If no participant equals the threshold, both rules give the same percentages; a strict header might also abbreviate an inclusive operational rule.
- **Direct observation versus inferred explanation:** Printed operators and percentages direct; a changed trial proportion or implementation error is not directly observed and is not inferred.
- **Exact remaining human question:** For Non-HDL cholesterol, was the percentage computed using ≥ or >5%, at what precision, and how many participants lay exactly at the boundary?
- **Document roles confirmed by content:** REPORT Methods and REPORT Figure 4 within the same retrospective article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; measure category and report_internal_inconsistency confirmed. No PLAN material is a discrepancy comparator.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The exact inclusive-versus-strict printed boundary mismatch remains as registered pending operational definition and equality counts.

## C025 — Total-to-HDL cholesterol ratio meaningful-change threshold boundary

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) Outcomes meaningful-risk-factor-change paragraph; [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 Total-to-HDL cholesterol ratio percentage header. Both found; current images checked.
- **Source printed value/text matched:** Methods reduction `at least 5%` matched.
- **Comparator printed value/text matched:** Figure header `Reduction >5%`; I 48.4 (46.5–50.4), C 41.3 (39.4–43.2), matched for this panel.
- **Consistency rule applicable:** Inclusive at-least (≥) and strict greater-than (>) rules assign different membership at exact equality; the displayed participant percentage's definition depends on that operator.
- **Calculation or logical comparison reproduced:** At change exactly 5%, the Methods rule includes the participant but the figure header excludes that participant. Printed operator comparison reproduced; zero tolerance for definition identity. Actual percentage difference equals boundary-count/denominator×100 and cannot be computed without that count.
- **Necessary inputs available; exact missing inputs/definitions:** Both operator definitions and percentages available. Arm-specific exact-equality counts, measurement precision/unrounded changes, operational classification code and percentage denominators are not supplied.
- **Source-grounded alternative interpretation:** If no participant equals the threshold, both rules give the same percentages; a strict header might also abbreviate an inclusive operational rule.
- **Direct observation versus inferred explanation:** Printed operators and percentages direct; a changed trial proportion or implementation error is not directly observed and is not inferred.
- **Exact remaining human question:** For Total-to-HDL cholesterol ratio, was the percentage computed using ≥ or >5%, at what precision, and how many participants lay exactly at the boundary?
- **Document roles confirmed by content:** REPORT Methods and REPORT Figure 4 within the same retrospective article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; measure category and report_internal_inconsistency confirmed. No PLAN material is a discrepancy comparator.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The exact inclusive-versus-strict printed boundary mismatch remains as registered pending operational definition and equality counts.

## C026 — Systolic blood pressure meaningful-change threshold boundary

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) Outcomes meaningful-risk-factor-change paragraph; [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 Systolic blood pressure percentage header. Both found; current images checked.
- **Source printed value/text matched:** Methods reduction `at least 5 mm Hg` matched.
- **Comparator printed value/text matched:** Figure header `Reduction >5 mm Hg`; I 47.5 (45.6–49.5), C 41.8 (39.9–43.7), matched for this panel.
- **Consistency rule applicable:** Inclusive at-least (≥) and strict greater-than (>) rules assign different membership at exact equality; the displayed participant percentage's definition depends on that operator.
- **Calculation or logical comparison reproduced:** At change exactly 5 mm Hg, the Methods rule includes the participant but the figure header excludes that participant. Printed operator comparison reproduced; zero tolerance for definition identity. Actual percentage difference equals boundary-count/denominator×100 and cannot be computed without that count.
- **Necessary inputs available; exact missing inputs/definitions:** Both operator definitions and percentages available. Arm-specific exact-equality counts, measurement precision/unrounded changes, operational classification code and percentage denominators are not supplied.
- **Source-grounded alternative interpretation:** If no participant equals the threshold, both rules give the same percentages; a strict header might also abbreviate an inclusive operational rule.
- **Direct observation versus inferred explanation:** Printed operators and percentages direct; a changed trial proportion or implementation error is not directly observed and is not inferred.
- **Exact remaining human question:** For Systolic blood pressure, was the percentage computed using ≥ or >5 mm Hg, at what precision, and how many participants lay exactly at the boundary?
- **Document roles confirmed by content:** REPORT Methods and REPORT Figure 4 within the same retrospective article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; measure category and report_internal_inconsistency confirmed. No PLAN material is a discrepancy comparator.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The exact inclusive-versus-strict printed boundary mismatch remains as registered pending operational definition and equality counts.

## C027 — Diastolic meaningful-change header omits the threshold operator

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) Outcomes blood-pressure threshold; [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 diastolic percentage header. Both found and current images checked.
- **Source printed value/text matched:** Methods reductions `at least 2.5 mm Hg` matched.
- **Comparator printed value/text matched:** Header `Reduction 2.5 mm Hg`, I48.1 (46.2–50.1), C44.3 (42.4–46.2), matched; direct image confirms no ≥ or > operator.
- **Consistency rule applicable:** An explicitly inclusive Methods threshold and an operator-free figure header do not provide identical explicit definitions; absence of an operator is not evidence of equality-only classification.
- **Calculation or logical comparison reproduced:** Logical comparison reproduced: Methods specifies≥2.5; figure header supplies2.5 and no relation. No numerical percentage discrepancy can be computed from this omission; no rounding tolerance is relevant.
- **Necessary inputs available; exact missing inputs/definitions:** Labels and percentages available; actual operator, equality counts, precision and denominator for this panel absent.
- **Source-grounded alternative interpretation:** `Reduction2.5 mm Hg` may be ordinary shorthand for the Methods≥2.5 rule and may yield entirely coherent percentages.
- **Direct observation versus inferred explanation:** Missing operator is directly observed. It is not evidence that only exactly2.5 reductions were counted or that reported percentages changed.
- **Exact remaining human question:** Which operator and change precision produced diastolic48.1%/44.3%, and is the header intended as shorthand for≥2.5 mm Hg?
- **Document roles confirmed by content:** REPORT Methods and REPORT Figure 4 within one article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; measure category/report_internal_inconsistency confirmed.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The registered explicit-definition omission is reproduced, with the operational threshold question retained.

## C028 — BMI axis names an absolute value while showing change

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) Figure 4 BMI physical-axis label/ticks and common caption. Found and visually checked.
- **Source printed value/text matched:** `Body Mass Index, kg/m² (95% CI)` with ticks−10,−5,0,5,10 matched.
- **Comparator printed value/text matched:** Caption `median change in observed risk factors`; neighboring physical labels explicitly say Change, matched.
- **Consistency rule applicable:** Absolute BMI is a nonnegative mass/height² quantity; a change can be negative. The caption establishes that this display is change.
- **Calculation or logical comparison reproduced:** Logical comparison reproduced: the negative-tick BMI distribution is consistently interpreted as change from the caption, while the BMI axis omits Change. No negative absolute participant BMI is asserted.
- **Necessary inputs available; exact missing inputs/definitions:** Axis, ticks and caption available; author intent about the abbreviated label absent.
- **Source-grounded alternative interpretation:** The common Figure 4 context/caption may communicate change adequately without repeating the word on this axis.
- **Direct observation versus inferred explanation:** Direct observation is omitted Change and negative ticks; the graph being a BMI change is source-grounded by the caption, not an inferred physiological abnormality.
- **Exact remaining human question:** Is this axis intended to identify change in BMI explicitly for extraction, or is its common-caption context the intended definition?
- **Document roles confirmed by content:** REPORT BMI axis and REPORT caption within one article.
- **Relationship type and all relationships confirmed/corrected:** S_W only; measure category/report_internal_inconsistency confirmed; separate rule from C009's confidence qualifier.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The literal quantity-label omission remains as registered, with caption-supported change interpretation documented.

## C029 — Original screening criterion count

**Status:** Pending Human Adjudication. **Primary category:** Numeric or arithmetic inconsistency. **Relationship type:** P_P. **All relationships:** P_P. **Review domain:** plan_material. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [protocol physical p22](../../../joi190106supp1_prod_1635377898.47058.pdf#page=22) lines693–696; [protocol physical p23](../../../joi190106supp1_prod_1635377898.47058.pdf#page=23) lines697–703; [protocol physical p4](../../../joi190106supp1_prod_1635377898.47058.pdf#page=4) amendment52–55. Exact locations found in current direct extraction.
- **Source printed value/text matched:** `following four criteria` and first numbered entry1 matched.
- **Comparator printed value/text matched:** Contiguous numbered criteria2,3,4,5; fifth criterion loss>1.5kg matched. Amendment removes the1.5kg criterion after initial70 participants at2 centers; matched.
- **Consistency rule applicable:** A heading's item count must match its contiguous numbered list for the same version; explicit amendment context distinguishes historical and amended rules.
- **Calculation or logical comparison reproduced:** Counting numbered entries1–5 gives5 versus label4 (difference1), with zero integer tolerance. Amendment explains why an intended later list may have4, but the visible unstruck original list retains5.
- **Necessary inputs available; exact missing inputs/definitions:** All count/list/amendment inputs available; intended version applying to the four-criteria introductory phrase is not explicitly stated.
- **Source-grounded alternative interpretation:** The heading could reflect the amended four-rule scheme with criterion5 retained as historical text.
- **Direct observation versus inferred explanation:** Five entries and four-count label are direct observations. Mixing historical/amended text is an inferred drafting explanation; no participant eligibility error is inferred.
- **Exact remaining human question:** Does the four-criteria label refer deliberately to the amended rule with entry5 superseded, or to this visible original five-item list?
- **Document roles confirmed by content:** PLAN prospective operational screening passages and PLAN protocol amendment; content confirms all roles.
- **Relationship type and all relationships confirmed/corrected:** P_P only: same bound plan material, including the amendment context. Numeric category/plan_material confirmed; amendment corroborates a possible explanation, not a REPORT discrepancy.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The visible original list count differs from its label, exactly as registered; amendment-aware interpretation is recorded.

## C030 — Five versus six cognitive tests at screening3

**Status:** Pending Human Adjudication. **Primary category:** Numeric or arithmetic inconsistency. **Relationship type:** P_P. **All relationships:** P_P. **Review domain:** plan_material. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [protocol physical p22](../../../joi190106supp1_prod_1635377898.47058.pdf#page=22) lines681–686; [protocol physical p27](../../../joi190106supp1_prod_1635377898.47058.pdf#page=27) lines821–825; [protocol physical p28](../../../joi190106supp1_prod_1635377898.47058.pdf#page=28) lines826–836; [protocol physical p24](../../../joi190106supp1_prod_1635377898.47058.pdf#page=24) cognitive footnote. All found; table currently rendered.
- **Source printed value/text matched:** `5 cognitive-neuropsychological tests` and five named tests MMSE, phonological verbal fluency, reverse digits, trail making, clock matched.
- **Comparator printed value/text matched:** `Six cognitive neuropsychological tests` numbered1–6 includes semantic animal fluency and phonemic P fluency separately; six administered at third screening visit matched. Footnote names animals+P within fluency.
- **Consistency rule applicable:** An explicitly numbered battery count must match at the same visit if instruments/subtests are counted identically; separate grouping conventions are an alternative.
- **Calculation or logical comparison reproduced:** Later numbered entries1–6 count6; earlier explicit list counts5. Difference1 is reproduced with zero integer tolerance. The added separately named semantic task explains the difference under task counting.
- **Necessary inputs available; exact missing inputs/definitions:** Exact lists and same-visit statements available; uniform instrument-family versus separately scored subtest counting convention not supplied.
- **Source-grounded alternative interpretation:** Five instrument families could count both semantic and phonemic fluency together; table footnote's animals+P supports that convention, despite earlier wording naming only phonological fluency.
- **Direct observation versus inferred explanation:** Counts and named tasks direct; an omitted administered task or differing counting conventions are possible explanations, not observations.
- **Exact remaining human question:** Do five and six intentionally count instrument families versus separate fluency tasks, or does the earlier screening list omit the semantic animal task?
- **Document roles confirmed by content:** PLAN operational protocol at every compared location.
- **Relationship type and all relationships confirmed/corrected:** P_P only; numeric category/plan_material confirmed. Table footnote supplies context within PLAN, not another relationship type.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Both explicit counts and same screening-visit definitions match and reproduce the registered count question under a common task convention.

## C031 — Yearly versus biennial cognitive evaluation schedule

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** P_P. **All relationships:** P_P. **Review domain:** plan_material. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [protocol physical p38](../../../joi190106supp1_prod_1635377898.47058.pdf#page=38) lines1216–1219; [protocol physical p27](../../../joi190106supp1_prod_1635377898.47058.pdf#page=27) lines802–810; [protocol physical p28](../../../joi190106supp1_prod_1635377898.47058.pdf#page=28) lines833–836; [protocol physical p24](../../../joi190106supp1_prod_1635377898.47058.pdf#page=24) row16. All found and matrix visually checked.
- **Source printed value/text matched:** `Also evaluated yearly ... cognitive function ... neuropsychological questionnaire scores` matched.
- **Comparator printed value/text matched:** Tests at baseline then2/4/6/8; third screening visit then even follow-up years; matrix row16 marksS3,Y2,Y4,Y6,Y8, matched.
- **Consistency rule applicable:** The cadence of new measurements must be identified consistently for the same named outcome; evaluation/review can differ from administration.
- **Calculation or logical comparison reproduced:** Literal annual cadence implies one-year spacing, versus explicit two-year spacing and four follow-up administrations through year8. Eight versus four collections is conditional on interpreting evaluation as collection, not an observed count.
- **Necessary inputs available; exact missing inputs/definitions:** Printed schedules and matrix available; whether yearly evaluation means new testing, reviewing past results, or a separate abbreviated instrument is not defined.
- **Source-grounded alternative interpretation:** Annual evaluation could mean reviewing available cognitive records while full six-test battery is administered only even years.
- **Direct observation versus inferred explanation:** Cadence phrases and marks direct; additional/unperformed administrations are not inferred.
- **Exact remaining human question:** Does yearly cognitive evaluation mean new battery administration or annual review of existing scores, and which instrument/cadence is intended?
- **Document roles confirmed by content:** PLAN intermediate-marker plan and PLAN operational collection schedule/matrix.
- **Relationship type and all relationships confirmed/corrected:** P_P only; measure category/plan_material confirmed; no reported trial collection data are compared.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Literal yearly/even-year schedule contrast reproduces; the distinction between evaluation and collection remains named.

## C032 — Yearly versus odd-year quality-of-life evaluation schedule

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** P_P. **All relationships:** P_P. **Review domain:** plan_material. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [protocol physical p38](../../../joi190106supp1_prod_1635377898.47058.pdf#page=38) lines1216–1219; [protocol physical p27](../../../joi190106supp1_prod_1635377898.47058.pdf#page=27) lines811–814; [protocol physical p28](../../../joi190106supp1_prod_1635377898.47058.pdf#page=28) lines838–842; [protocol physical p24](../../../joi190106supp1_prod_1635377898.47058.pdf#page=24) row18. All found and matrix visually checked.
- **Source printed value/text matched:** `Also evaluated yearly ... quality of life` matched.
- **Comparator printed value/text matched:** SF-36 beginning/run-in thenY1/Y3/Y5/Y7; matrixS3,Y1,Y3,Y5,Y7, matched.
- **Consistency rule applicable:** The same named outcome needs a consistent collection cadence unless evaluation is a separate operation.
- **Calculation or logical comparison reproduced:** Annual one-year spacing differs from stated odd-year two-year spacing; conditional collection counts8 versus4 throughyear8. No actual completed assessments are counted.
- **Necessary inputs available; exact missing inputs/definitions:** Schedules, instrument and marks available; definition of yearly evaluation versus SF-36 administration absent.
- **Source-grounded alternative interpretation:** Yearly evaluation may review prior records or be generic outcome-summary wording while full SF-36 collection is only odd years.
- **Direct observation versus inferred explanation:** Printed cadence direct; a missed collection or actual follow-up conduct discrepancy is not observed.
- **Exact remaining human question:** Is yearly quality-of-life evaluation distinct from odd-year SF-36 collection, or which cadence governs new SF-36 assessments?
- **Document roles confirmed by content:** PLAN marker and collection-schedule passages at all locations.
- **Relationship type and all relationships confirmed/corrected:** P_P only; measure category/plan_material confirmed.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Yearly versus explicit odd-year wording matches and reproduces the assigned schedule-definition question.

## C033 — Cognitive baseline versus screening3 timing label

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** P_P. **All relationships:** P_P. **Review domain:** plan_material. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [protocol physical p27](../../../joi190106supp1_prod_1635377898.47058.pdf#page=27) lines802–803; [protocol physical p24](../../../joi190106supp1_prod_1635377898.47058.pdf#page=24) row16S3/Baseline columns; [protocol physical p28](../../../joi190106supp1_prod_1635377898.47058.pdf#page=28) lines833–836. All found; current matrix image confirms column positions.
- **Source printed value/text matched:** `At baseline and every two years thereafter ... battery of6 tests` matched.
- **Comparator printed value/text matched:** Row16 X underS3, blank separateBaseline column; passage initial six tests at third screening visit, matched.
- **Consistency rule applicable:** Two explicitly distinct visit-column labels should not be silently equated; baseline may alternatively mean the initial pre-randomization measure.
- **Calculation or logical comparison reproduced:** Literal visit alignment differs: narrative baseline versus matrix S3=marked, Baseline=blank. Only one initial collection is indicated by matrix; no second measurement or missing collection is asserted.
- **Necessary inputs available; exact missing inputs/definitions:** Text, initial visit statement and precise matrix columns available. Operational meaning of baseline cognition relative to separate baseline trial visit absent.
- **Source-grounded alternative interpretation:** Baseline cognition may intentionally mean the S3 initial cognitive result carried forward as baseline, fully coherent operationally.
- **Direct observation versus inferred explanation:** Printed labels/mark positions direct; assuming a separate unperformed baseline test would be inference and is not made.
- **Exact remaining human question:** Does cognitive baseline intentionally refer to the S3 measurement before randomization, or was a separate baseline-visit collection intended?
- **Document roles confirmed by content:** PLAN protocol narrative and prospective collection matrix.
- **Relationship type and all relationships confirmed/corrected:** P_P only; measure category/plan_material confirmed. Concrete initial-assessment timing label is compared; no broad methodology claim.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Registered literal baseline-versusS3 label comparison reproduces pending operational equivalence definition.

## C034 — Total-fat target range and subtype bounds

**Status:** Pending Human Adjudication. **Primary category:** Numeric or arithmetic inconsistency. **Relationship type:** P_P. **All relationships:** P_P. **Review domain:** plan_material. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [protocol physical p44](../../../joi190106supp1_prod_1635377898.47058.pdf#page=44) energy-restricted Mediterranean diet nutrient table. Current direct exact-page extraction found all rows.
- **Source printed value/text matched:** Total fat35–40% of total calories matched.
- **Comparator printed value/text matched:** Saturated8–10%, monounsaturated>20%, polyunsaturated>10%, each of total calories, matched.
- **Consistency rule applicable:** Nonoverlapping fat-energy components sum to no more than total fat when all use the same total-energy denominator.
- **Calculation or logical comparison reproduced:** Minimum subtype sum≥8+>20+>10=>38%, so35–38% of total-fat range cannot jointly meet all literal bounds. Feasible overlap exists:8+20.5+10.5=39% within35–40. Targets are not wholly incompatible. Even ±0.5-point display allowances leave component lower sum>36.5 versus total35 lower endpoint at most35.5.
- **Necessary inputs available; exact missing inputs/definitions:** All displayed bounds and common denominator supplied. Whether ranges are independent approximate guidance rather than simultaneous mandatory bounds is unspecified.
- **Source-grounded alternative interpretation:** Only the feasible>38–40% overlap may be intended; approximate independent nutrition recommendations may not require every endpoint combination.
- **Direct observation versus inferred explanation:** Printed target bounds direct; infeasible lower portion is derived arithmetic. Implemented participant diets or menus are not inspected.
- **Exact remaining human question:** Are these simultaneous constraints read only on their>38–40% feasible overlap, or does a component/denominator/inequality intentionally differ?
- **Document roles confirmed by content:** PLAN nutrient-prescription table, every compared bound.
- **Relationship type and all relationships confirmed/corrected:** P_P only; numeric category/plan_material confirmed.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The registered partial-range infeasibility reproduces, while feasible overlap prevents the stronger unsupported whole-range claim.

## C035 — Additional blood volume and tube components

**Status:** Pending Human Adjudication. **Primary category:** Numeric or arithmetic inconsistency. **Relationship type:** P_P. **All relationships:** P_P. **Review domain:** plan_material. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [protocol physical p49](../../../joi190106supp1_prod_1635377898.47058.pdf#page=49) lines1574–1576. Exact total/components found in current extraction.
- **Source printed value/text matched:** `55.5 ml of blood` matched.
- **Comparator printed value/text matched:** `two10 ml K2E EDTA tubes; one4.5 ml citrate tube; and two10 ml and6 ml gel serum separator tubes` matched.
- **Consistency rule applicable:** An exact nominal total must equal the sum of tube volumes and counts; multiplicity ambiguity requires separate parses.
- **Calculation or logical comparison reproduced:** EDTA20+citrate4.5 +serum two10 and one6=50.5 (−5); serum two10 and two6=56.5 (+1); serum one10 and one6=40.5. Exact nominal20+4.5+10a+6b=55.5 demands10a+6b=31, impossible for integer counts because the left is even. Total rounding±0.05mL alone cannot bridge1mL; integer-printed tube capacities must not be assumed individually rounded to0.1mL. Approximate capacities/actual fills could reconcile the residual and are undefined.
- **Necessary inputs available; exact missing inputs/definitions:** Total and listed nominal sizes supplied; serum multiplicities, actual fill volumes, whether integer tube capacities are exact or approximate, and whether an extra tube/partial fill is omitted are not defined.
- **Source-grounded alternative interpretation:** Partial fill or an unlisted volume can reconcile55.5; the wording may omit a tube or misidentify a nominal size.
- **Direct observation versus inferred explanation:** Printed55.5 and tube wording direct; choice of parse, omitted tube, or actual fill correction is inferred only.
- **Exact remaining human question:** Which exact serum counts, nominal/actual fill volumes, or additional volume account for55.5mL?
- **Document roles confirmed by content:** PLAN laboratory operational protocol for both total and components.
- **Relationship type and all relationships confirmed/corrected:** P_P only; numeric category/plan_material confirmed.
- **Evidence state and determining recheck fact:** `recorded_candidate` — All straightforward nominal-volume parses fail to reproduce55.5; ambiguous multiplicity remains explicitly unresolved.

## C036 — Two eTable2 columns carry the intervention label

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [results physical p3](../../../joi190106supp3_prod_1635377898.49725.pdf#page=3) eTable2 arm headings; [results physical p5](../../../joi190106supp3_prod_1635377898.49725.pdf#page=5) same table continuation headings. Both found in direct exact-page extraction.
- **Source printed value/text matched:** p3 Intervention group N=3272; second Intervention group N=3311 matched.
- **Comparator printed value/text matched:** p5 Intervention N=3272 and Control N=3311, with same table number, MI-all-randomized header and between-group difference matched.
- **Consistency rule applicable:** Repeated arm identity for the same table/denominator must stay consistent across continuations absent an announced population change.
- **Calculation or logical comparison reproduced:** Logical comparison reproduced: the N3311 second arm changes its printed identity from Intervention to Control. No rounding tolerance for the arm-label identity.
- **Necessary inputs available; exact missing inputs/definitions:** Headings and continuation identity available; author-intended p3 second-column heading not separately stated.
- **Source-grounded alternative interpretation:** The second heading may be a copied label; two intervention subgroups would require an unprovided definition and would conflict with the table continuation.
- **Direct observation versus inferred explanation:** Both headings direct; choosing which heading/value assignment is intended is an inference, not performed here.
- **Exact remaining human question:** Which randomized arm is intended for the p3 N3311 column, and does its heading correspond to the control column in the continuation?
- **Document roles confirmed by content:** REPORT retrospective results-table headings at both locations.
- **Relationship type and all relationships confirmed/corrected:** S_W only within one results supplement. Measure category/report_internal_inconsistency confirmed; main arm counts corroborate but do not create another discrepancy relationship.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Exact conflicting arm headings for the same table/denominator reproduce the registered comparison.

## C037 — Red-wine median exceeds its upper quartile

**Status:** Pending Human Adjudication. **Primary category:** Numeric or arithmetic inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** statistical_results. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [results physical p7](../../../joi190106supp3_prod_1635377898.49725.pdf#page=7) eTable2 red-wine intervention baseline and row/footer median(IQR) definition. Exact location found; current image confirms33 glyph.
- **Source printed value/text matched:** Intervention red wine g/week baseline33 (0,29) matched.
- **Comparator printed value/text matched:** Row says Baseline, median(IQR); footer Baseline data are median(IQR); control4 (0,29) matched.
- **Consistency rule applicable:** A median lies between the first and third quartiles for any coherently defined one distribution, including common quantile interpolation conventions.
- **Calculation or logical comparison reproduced:** Q1=0≤median33 but33>Q3=29 by4g/week. Independent integer rounding intervals±0.5 leave minimum excess3g/week, so ordinary rounding cannot reconcile the order.
- **Necessary inputs available; exact missing inputs/definitions:** All ordering inputs and summary definition available; intended erroneous digit/statistic not identifiable from supplied data.
- **Source-grounded alternative interpretation:** A central value or quartile may be mistyped or the summary definition may be wrong; the source does not select an alternative.
- **Direct observation versus inferred explanation:** Direct observation is source33,0,29 and median label; impossible order is derived. A correction to any particular digit is not inferred.
- **Exact remaining human question:** Which baseline red-wine value or summary definition is intended for intervention33 (0,29)?
- **Document roles confirmed by content:** REPORT eTable2 cell and REPORT descriptive-statistic definition within the same supplement.
- **Relationship type and all relationships confirmed/corrected:** S_W only; numeric category/statistical_results confirmed. Different rule from C042's cross-table baseline comparison.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Current visual reading preserves33 and reproduces the median-aboveQ3 comparison; not an OCR-only issue.

## C038 — Olive-oil baseline summary label and table definition

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [results physical p10](../../../joi190106supp3_prod_1635377898.49725.pdf#page=10) eTable4 total olive-oil baseline row; [results physical p11](../../../joi190106supp3_prod_1635377898.49725.pdf#page=11) footnote before continued eTable4. Both exact locations found.
- **Source printed value/text matched:** `Baseline, mean(SD)` with350 (175,350) in both groups matched.
- **Comparator printed value/text matched:** `Baseline data are median(IQR)` footnote matched; parentheses contain two endpoints.
- **Consistency rule applicable:** A mean(SD) convention denotes one dispersion summary while median(IQR) denotes a central quantile and two quartile endpoints; the table defines competing statistic identities for this row.
- **Calculation or logical comparison reproduced:** Logical comparison reproduced: row mean(SD) versus footnote median(IQR), with endpoint-format support. No numeric test or rounding tolerance needed.
- **Necessary inputs available; exact missing inputs/definitions:** Printed label, both endpoint values and applicable table footnote available; actual statistic-producing code/data absent.
- **Source-grounded alternative interpretation:** The row's heading may be generic/copied and350 (175,350) may intentionally follow the median/IQR footnote, which clarifies intended interpretation.
- **Direct observation versus inferred explanation:** Labels and format direct; a copied heading is inference only; no350mean/median value correction is chosen.
- **Exact remaining human question:** Is total olive-oil baseline350 (175,350) a median withQ1/Q3 or a mean with a differently defined dispersion, and which label is intended?
- **Document roles confirmed by content:** REPORT results-table row and REPORT same table's footnote.
- **Relationship type and all relationships confirmed/corrected:** S_W only; measure category/report_internal_inconsistency confirmed.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Exact conflicting summary-statistic labels reproduce the registered labeling question.

## C039 — Contents entry inserts245 into the participant label

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [results physical p1](../../../joi190106supp3_prod_1635377898.49725.pdf#page=1) eTable9 contents entry; [results physical p23](../../../joi190106supp3_prod_1635377898.49725.pdf#page=23) eTable9 all-randomized MI header. Found; current source p1 image confirms inline245.
- **Source printed value/text matched:** `all randomized245 participants (multiple imputation[MI]) and completers only` matched.
- **Comparator printed value/text matched:** eTable9 all-randomized MI interventionN3272 and controlN3311 matched; the actual title has no245.
- **Consistency rule applicable:** Matched contents/title population wording should agree; an unexplained number inside the participant phrase creates a quantitative-label ambiguity.
- **Calculation or logical comparison reproduced:** 3272+3311=6583 versus245 would differ6338 if245 were read as a count. That subtraction is conditional and is not evidence that245 was intended as denominator. Literal unexpected inline245 and its absence from the actual title are reproduced.
- **Necessary inputs available; exact missing inputs/definitions:** Contents text and actual table counts/title available; whether245 is an editorial line number, an intended count, or another artifact is unspecified.
- **Source-grounded alternative interpretation:** A stray manuscript line number is a strong explanation; actual table populations make a245-person interpretation unsupported.
- **Direct observation versus inferred explanation:** Visible245 and table headers direct. Interpretation as intended cohort size or line number remains inference.
- **Exact remaining human question:** Is245 an unintended line-number insertion, and what participant phrase is intended in this contents entry?
- **Document roles confirmed by content:** REPORT contents and REPORT results table within one supplement.
- **Relationship type and all relationships confirmed/corrected:** S_W only; measure category/report_internal_inconsistency confirmed. Candidate framed as label ambiguity rather than a demonstrated245 denominator.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The current PDF visibly contains245 in the phrase; registered quantitative-label ambiguity is reproduced.

## C040 — Waist-to-height ratio scale is unmarked

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** P_P. **All relationships:** P_P. **Review domain:** plan_material. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [sap physical p14](../../../joi190106supp2_prod_1635377898.49605.pdf#page=14) Table2 waist-to-height ratio and waist rows; [sap physical p17](../../../joi190106supp2_prod_1635377898.49605.pdf#page=17) quantitative-trait list. Found; current Table2 image checked. p17 is a variable-summary list, not an explicit dimensional/scaling formula; locator description clarified.
- **Source printed value/text matched:** Waist-to-height ratio66.2 (6.5),66.4 (5.5), without% or×100 unit matched.
- **Comparator printed value/text matched:** Waist means109.9cm,110.4cm; p17 lists baseline waist-to-height ratio among traits summarized with means/SD, matched; it does not define scaling.
- **Consistency rule applicable:** A waist/height ratio in common length units is dimensionless; interpreting66.2 as0.662 requires an explicit factor100 convention. A mathematical ratio definition is supplied by the variable name, while exact scale is absent.
- **Calculation or logical comparison reproduced:** Diagnostic only:109.9/66.2=1.660121 versus109.9/0.662=166.0121. These are not actual mean heights because mean of ratios differs from ratio of means. Exact100-fold interpretive scale ambiguity is reproduced; no participant height is reconstructed.
- **Necessary inputs available; exact missing inputs/definitions:** Printed ratios, waist summaries and labels available. Height records, length-unit convention and whether the ratio is a percent-scaled variable absent.
- **Source-grounded alternative interpretation:** Values may conventionally represent percentages or use mixed length units; source leaves the conversion unmarked.
- **Direct observation versus inferred explanation:** Printed values and absence of scale marker direct. Intention of percent scaling is inference only; no physiologically impossible height is asserted.
- **Exact remaining human question:** Are66.2/66.4 equal to100×waist/height, or which explicit units and transform define this row?
- **Document roles confirmed by content:** PLAN SAP prospective/background trial-population table and PLAN analysis-variable list by content.
- **Relationship type and all relationships confirmed/corrected:** P_P only; measure category/plan_material confirmed. Corrected p17 description changes no document role or relationship.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The registered unmarked scaling question remains; p17 provides no definition that would resolve it.

## C041 — Diabetes upper-bound wording and screening prevalence

**Status:** Pending Human Adjudication. **Primary category:** Denominator, proportion, or total inconsistency. **Relationship type:** P_P. **All relationships:** P_P. **Review domain:** plan_material. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [sap physical p15](../../../joi190106supp2_prod_1635377898.49605.pdf#page=15) lines356–357; [sap physical p14](../../../joi190106supp2_prod_1635377898.49605.pdf#page=14) Table2 randomized self-reported diabetes row. Both found; table image checked.
- **Source printed value/text matched:** `Approximately,50% ... women and diabetic participants do not exceed27% of the total cohort` matched.
- **Comparator printed value/text matched:** RandomizedN6874 self-reported diabetes27.2% matched.
- **Consistency rule applicable:** An exact upper bound27% would conflict with same-cohort27.2%; a rounded descriptive27% is compatible. The wording must determine which rule applies.
- **Calculation or logical comparison reproduced:** 27.2−27=0.2percentage point. Nearest one-decimal interval[27.15,27.25) remains>27. However27.2 rounds to27 at whole-percent precision; thus no arithmetic contradiction is established if27 is descriptive rounding.
- **Necessary inputs available; exact missing inputs/definitions:** Displayed percentages and cohorts available; exact-versus-rounded meaning of do-not-exceed, diabetic definition and table-specific denominator are not explicit.
- **Source-grounded alternative interpretation:** The opening Approximately may qualify this descriptive composition sentence, making27 a rounded prevalence; self-report and another diabetes definition could also differ.
- **Direct observation versus inferred explanation:** Printed wording and27.2 direct. Reading27 as a hard recruitment cap is conditional inference and no cap violation is claimed.
- **Exact remaining human question:** Does27% mean approximate descriptive composition or an exact cap, and does it use the Table2 randomized self-reported-diabetes denominator/definition?
- **Document roles confirmed by content:** PLAN SAP participant-composition passage and PLAN historical/background screening table.
- **Relationship type and all relationships confirmed/corrected:** P_P only; denominator category/plan_material confirmed; this is plan-internal even though Table2 reports background recruitment data.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The registered conditional strict-bound question reproduces; the ordinary rounded-prevalence alternative fully reconciles the numbers if adopted.

## C042 — Intervention baseline red-wine medians across analyses

**Status:** Pending Human Adjudication. **Primary category:** Numeric or arithmetic inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** statistical_results. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [results physical p7](../../../joi190106supp3_prod_1635377898.49725.pdf#page=7) eTable2 Intervention red-wine baseline; [results physical p19](../../../joi190106supp3_prod_1635377898.49725.pdf#page=19) eTable7 Intervention red-wine baseline; [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) follow-up imputation/replacement definition. Exact cells found and current p7/p19 images checked.
- **Source printed value/text matched:** eTable2 InterventionN3272, red wine g/week Baseline,median(IQR) 33 (0,29), matched.
- **Comparator printed value/text matched:** eTable7 InterventionN3272, red wine g/week Baseline,median(IQR)0 (0,29), matched. Header replaces missing values with baseline value. Methods states imputed values used for follow-up but not baseline.
- **Consistency rule applicable:** An unchanged observed baseline variable in the same arm/sample/definition should have the same baseline summary when only follow-up missingness handling changes. Same header alone is insufficient proof of exact record-set identity.
- **Calculation or logical comparison reproduced:** 33−0=33g/week median display difference, far greater than joint integer rounding interval width1. Quantile endpoints match0/29. The observed cross-table difference is reproduced; exact same-record premise remains conditional.
- **Necessary inputs available; exact missing inputs/definitions:** Both summaries, armN, baseline labels and main follow-up-only imputation statement available. Endpoint-specific baseline denominator, missing wine handling, exact record sets, recoding and quantile algorithm not supplied.
- **Source-grounded alternative interpretation:** Different available baseline records or recoding/quantile procedure may alter the median despite equal cohort headers. Follow-up replacement alone cannot alter an identically defined fixed baseline, but exact analytic record-set identity is not demonstrated.
- **Direct observation versus inferred explanation:** Direct printed cross-table summaries differ. Assuming identical baseline available records is an explicit conditional identity diagnostic, not established by cohortN alone.
- **Exact remaining human question:** Why does Intervention baseline red-wine median change from33 to0: were baseline records, denominators, coding, or quantile procedures changed as well as follow-up handling?
- **Document roles confirmed by content:** REPORT eTable2 and REPORT eTable7 in one results supplement. REPORT main analysis passage only supports the follow-up-handling premise.
- **Relationship type and all relationships confirmed/corrected:** S_W only: compared baseline mismatch is inside one supplement; main Methods only corroborates one side/premise, so it creates no S_C discrepancy. Category/statistical_results confirmed. C042 and C043 remain distinct arms; C037 uses a different quartile-order rule.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The exact baseline displays reproduce the registered comparison; named analytic-definition inputs remain absent, so the question remains conditional.

## C043 — Control baseline red-wine medians across analyses

**Status:** Pending Human Adjudication. **Primary category:** Numeric or arithmetic inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** statistical_results. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [results physical p7](../../../joi190106supp3_prod_1635377898.49725.pdf#page=7) eTable2 Control red-wine baseline; [results physical p19](../../../joi190106supp3_prod_1635377898.49725.pdf#page=19) eTable7 Control red-wine baseline; [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) follow-up imputation/replacement definition. Exact cells found and current p7/p19 images checked.
- **Source printed value/text matched:** eTable2 ControlN3311, red wine g/week Baseline,median(IQR) 4 (0,29), matched.
- **Comparator printed value/text matched:** eTable7 ControlN3311, red wine g/week Baseline,median(IQR)0 (0,29), matched. Header replaces missing values with baseline value. Methods states imputed values used for follow-up but not baseline.
- **Consistency rule applicable:** An unchanged observed baseline variable in the same arm/sample/definition should have the same baseline summary when only follow-up missingness handling changes. Same header alone is insufficient proof of exact record-set identity.
- **Calculation or logical comparison reproduced:** 4−0=4g/week median display difference, far greater than joint integer rounding interval width1. Quantile endpoints match0/29. The observed cross-table difference is reproduced; exact same-record premise remains conditional.
- **Necessary inputs available; exact missing inputs/definitions:** Both summaries, armN, baseline labels and main follow-up-only imputation statement available. Endpoint-specific baseline denominator, missing wine handling, exact record sets, recoding and quantile algorithm not supplied.
- **Source-grounded alternative interpretation:** Different available baseline records or recoding/quantile procedure may alter the median despite equal cohort headers. Follow-up replacement alone cannot alter an identically defined fixed baseline, but exact analytic record-set identity is not demonstrated.
- **Direct observation versus inferred explanation:** Direct printed cross-table summaries differ. Assuming identical baseline available records is an explicit conditional identity diagnostic, not established by cohortN alone.
- **Exact remaining human question:** Why does Control baseline red-wine median change from4 to0: were baseline records, denominators, coding, or quantile procedures changed as well as follow-up handling?
- **Document roles confirmed by content:** REPORT eTable2 and REPORT eTable7 in one results supplement. REPORT main analysis passage only supports the follow-up-handling premise.
- **Relationship type and all relationships confirmed/corrected:** S_W only: compared baseline mismatch is inside one supplement; main Methods only corroborates one side/premise, so it creates no S_C discrepancy. Category/statistical_results confirmed. C042 and C043 remain distinct arms; C037 uses a different quartile-order rule.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The exact baseline displays reproduce the registered comparison; named analytic-definition inputs remain absent, so the question remains conditional.

## C044 — Fat eFigure 2 percentage annotations and bar heights

**Status:** Pending Human Adjudication. **Primary category:** Numeric or arithmetic inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** statistical_results. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [results physical p26](../../../joi190106supp3_prod_1635377898.49725.pdf#page=26) eFigure 2 Down Fat pair, same-color percent labels, percent-axis ticks and arm legend. Current fresh source render at160dpi visually checked for this exact pair.
- **Source printed value/text matched:** Blue Intervention34%; grey Control32%; P=0.14, matched.
- **Comparator printed value/text matched:** Blue shorter than grey; blue/grey bar heights approximately32 and34%, respectively, against0/20/40/60/80/100% ticks. Legend blue/purpleIntervention, greyControl and percentage-of-participants caption matched.
- **Consistency rule applicable:** Same-color numeric percentage and percentage-height encoding for the same outcome/arm must agree. Rank inversion can establish disagreement without exact digitization; the dessert mismatch additionally uses clear scale separation.
- **Calculation or logical comparison reproduced:** Numeric labels have blue34>grey32, but the graph's bar order is the opposite (blue shorter than grey). Since integer rounding preserves order and bars differ visibly, the registered disagreement reproduces without treating pixel coordinates as exact percentages. Heights approximately32 and34% are diagnostic only; ordinary label±0.5point plus approximate visual≈1point is acknowledged.
- **Necessary inputs available; exact missing inputs/definitions:** All graphic elements needed for label-versus-height/order comparison available. Exact underlying percentages, denominators, compliant counts, CI procedure, test/covariance and graphics input dataset are absent. The printed P value is not mechanically recalculated.
- **Source-grounded alternative interpretation:** Annotations may be assigned to the opposite arms, or the bar/legend encoding may be wrong; a different annotation quantity would require a definition absent from the caption.
- **Direct observation versus inferred explanation:** Labels, bar order/heights, axis and legend are direct current-image observations. A swap, stale text, wrong graphics data or group assignment is an inferred explanation, not an identified production error.
- **Exact remaining human question:** Which exact arm-specific fat compliance percentages and population/definition generated the labels and bars, and which assignments are intended?
- **Document roles confirmed by content:** REPORT graphic annotations, REPORT same graphic height/percent axis/legend in one results supplement.
- **Relationship type and all relationships confirmed/corrected:** Primary category corrected from Measure, label, or scale inconsistency to Numeric or arithmetic inconsistency: the directly compared quantities are two numeric encodings of the same percentage; a mislabeled arm is only a possible mechanism. S_W/allS_W remain; derived domain corrected to statistical_results. No PLAN comparison.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Current visual label-versus-graphic comparison reproduces the assigned mismatch, independent of approximate inherited pixel coordinates.

## C045 — MUFA eFigure 2 percentage annotations and bar heights

**Status:** Pending Human Adjudication. **Primary category:** Numeric or arithmetic inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** statistical_results. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [results physical p26](../../../joi190106supp3_prod_1635377898.49725.pdf#page=26) eFigure 2 Up MUFA pair, same-color percent labels, percent-axis ticks and arm legend. Current fresh source render at160dpi visually checked for this exact pair.
- **Source printed value/text matched:** Blue Intervention72%; grey Control77%; P<0.001, matched.
- **Comparator printed value/text matched:** Blue taller than grey; blue/grey bar heights approximately77 and72%, respectively, against0/20/40/60/80/100% ticks. Legend blue/purpleIntervention, greyControl and percentage-of-participants caption matched.
- **Consistency rule applicable:** Same-color numeric percentage and percentage-height encoding for the same outcome/arm must agree. Rank inversion can establish disagreement without exact digitization; the dessert mismatch additionally uses clear scale separation.
- **Calculation or logical comparison reproduced:** Numeric labels have blue72<grey77, but the graph's bar order is the opposite (blue taller than grey). Since integer rounding preserves order and bars differ visibly, the registered disagreement reproduces without treating pixel coordinates as exact percentages. Heights approximately77 and72% are diagnostic only; ordinary label±0.5point plus approximate visual≈1point is acknowledged.
- **Necessary inputs available; exact missing inputs/definitions:** All graphic elements needed for label-versus-height/order comparison available. Exact underlying percentages, denominators, compliant counts, CI procedure, test/covariance and graphics input dataset are absent. The printed P value is not mechanically recalculated.
- **Source-grounded alternative interpretation:** Annotations may be assigned to the opposite arms, or the bar/legend encoding may be wrong; a different annotation quantity would require a definition absent from the caption.
- **Direct observation versus inferred explanation:** Labels, bar order/heights, axis and legend are direct current-image observations. A swap, stale text, wrong graphics data or group assignment is an inferred explanation, not an identified production error.
- **Exact remaining human question:** Which exact arm-specific mufa compliance percentages and population/definition generated the labels and bars, and which assignments are intended?
- **Document roles confirmed by content:** REPORT graphic annotations, REPORT same graphic height/percent axis/legend in one results supplement.
- **Relationship type and all relationships confirmed/corrected:** Primary category corrected from Measure, label, or scale inconsistency to Numeric or arithmetic inconsistency: the directly compared quantities are two numeric encodings of the same percentage; a mislabeled arm is only a possible mechanism. S_W/allS_W remain; derived domain corrected to statistical_results. No PLAN comparison.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Current visual label-versus-graphic comparison reproduces the assigned mismatch, independent of approximate inherited pixel coordinates.

## C046 — MUFA-to-SFA ratio eFigure 2 percentage annotations and bar heights

**Status:** Pending Human Adjudication. **Primary category:** Numeric or arithmetic inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** statistical_results. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [results physical p26](../../../joi190106supp3_prod_1635377898.49725.pdf#page=26) eFigure 2 Up MUFA:SFA pair, same-color percent labels, percent-axis ticks and arm legend. Current fresh source render at160dpi visually checked for this exact pair.
- **Source printed value/text matched:** Blue Intervention79%; grey Control86%; P<0.001, matched.
- **Comparator printed value/text matched:** Blue taller than grey; blue/grey bar heights approximately86 and79%, respectively, against0/20/40/60/80/100% ticks. Legend blue/purpleIntervention, greyControl and percentage-of-participants caption matched.
- **Consistency rule applicable:** Same-color numeric percentage and percentage-height encoding for the same outcome/arm must agree. Rank inversion can establish disagreement without exact digitization; the dessert mismatch additionally uses clear scale separation.
- **Calculation or logical comparison reproduced:** Numeric labels have blue79<grey86, but the graph's bar order is the opposite (blue taller than grey). Since integer rounding preserves order and bars differ visibly, the registered disagreement reproduces without treating pixel coordinates as exact percentages. Heights approximately86 and79% are diagnostic only; ordinary label±0.5point plus approximate visual≈1point is acknowledged.
- **Necessary inputs available; exact missing inputs/definitions:** All graphic elements needed for label-versus-height/order comparison available. Exact underlying percentages, denominators, compliant counts, CI procedure, test/covariance and graphics input dataset are absent. The printed P value is not mechanically recalculated.
- **Source-grounded alternative interpretation:** Annotations may be assigned to the opposite arms, or the bar/legend encoding may be wrong; a different annotation quantity would require a definition absent from the caption.
- **Direct observation versus inferred explanation:** Labels, bar order/heights, axis and legend are direct current-image observations. A swap, stale text, wrong graphics data or group assignment is an inferred explanation, not an identified production error.
- **Exact remaining human question:** Which exact arm-specific mufa-to-sfa ratio compliance percentages and population/definition generated the labels and bars, and which assignments are intended?
- **Document roles confirmed by content:** REPORT graphic annotations, REPORT same graphic height/percent axis/legend in one results supplement.
- **Relationship type and all relationships confirmed/corrected:** Primary category corrected from Measure, label, or scale inconsistency to Numeric or arithmetic inconsistency: the directly compared quantities are two numeric encodings of the same percentage; a mislabeled arm is only a possible mechanism. S_W/allS_W remain; derived domain corrected to statistical_results. No PLAN comparison.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Current visual label-versus-graphic comparison reproduces the assigned mismatch, independent of approximate inherited pixel coordinates.

## C047 — Fruit eFigure 2 percentage annotations and bar heights

**Status:** Pending Human Adjudication. **Primary category:** Numeric or arithmetic inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** statistical_results. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [results physical p26](../../../joi190106supp3_prod_1635377898.49725.pdf#page=26) eFigure 2 Up Fruit pair, same-color percent labels, percent-axis ticks and arm legend. Current fresh source render at160dpi visually checked for this exact pair.
- **Source printed value/text matched:** Blue Intervention58%; grey Control63%; P<0.001, matched.
- **Comparator printed value/text matched:** Blue taller than grey; blue/grey bar heights approximately63 and58%, respectively, against0/20/40/60/80/100% ticks. Legend blue/purpleIntervention, greyControl and percentage-of-participants caption matched.
- **Consistency rule applicable:** Same-color numeric percentage and percentage-height encoding for the same outcome/arm must agree. Rank inversion can establish disagreement without exact digitization; the dessert mismatch additionally uses clear scale separation.
- **Calculation or logical comparison reproduced:** Numeric labels have blue58<grey63, but the graph's bar order is the opposite (blue taller than grey). Since integer rounding preserves order and bars differ visibly, the registered disagreement reproduces without treating pixel coordinates as exact percentages. Heights approximately63 and58% are diagnostic only; ordinary label±0.5point plus approximate visual≈1point is acknowledged.
- **Necessary inputs available; exact missing inputs/definitions:** All graphic elements needed for label-versus-height/order comparison available. Exact underlying percentages, denominators, compliant counts, CI procedure, test/covariance and graphics input dataset are absent. The printed P value is not mechanically recalculated.
- **Source-grounded alternative interpretation:** Annotations may be assigned to the opposite arms, or the bar/legend encoding may be wrong; a different annotation quantity would require a definition absent from the caption.
- **Direct observation versus inferred explanation:** Labels, bar order/heights, axis and legend are direct current-image observations. A swap, stale text, wrong graphics data or group assignment is an inferred explanation, not an identified production error.
- **Exact remaining human question:** Which exact arm-specific fruit compliance percentages and population/definition generated the labels and bars, and which assignments are intended?
- **Document roles confirmed by content:** REPORT graphic annotations, REPORT same graphic height/percent axis/legend in one results supplement.
- **Relationship type and all relationships confirmed/corrected:** Primary category corrected from Measure, label, or scale inconsistency to Numeric or arithmetic inconsistency: the directly compared quantities are two numeric encodings of the same percentage; a mislabeled arm is only a possible mechanism. S_W/allS_W remain; derived domain corrected to statistical_results. No PLAN comparison.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Current visual label-versus-graphic comparison reproduces the assigned mismatch, independent of approximate inherited pixel coordinates.

## C048 — Vegetables eFigure 2 percentage annotations and bar heights

**Status:** Pending Human Adjudication. **Primary category:** Numeric or arithmetic inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** statistical_results. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [results physical p26](../../../joi190106supp3_prod_1635377898.49725.pdf#page=26) eFigure 2 Up Vegetables pair, same-color percent labels, percent-axis ticks and arm legend. Current fresh source render at160dpi visually checked for this exact pair.
- **Source printed value/text matched:** Blue Intervention56%; grey Control64%; P<0.001, matched.
- **Comparator printed value/text matched:** Blue taller than grey; blue/grey bar heights approximately64 and56%, respectively, against0/20/40/60/80/100% ticks. Legend blue/purpleIntervention, greyControl and percentage-of-participants caption matched.
- **Consistency rule applicable:** Same-color numeric percentage and percentage-height encoding for the same outcome/arm must agree. Rank inversion can establish disagreement without exact digitization; the dessert mismatch additionally uses clear scale separation.
- **Calculation or logical comparison reproduced:** Numeric labels have blue56<grey64, but the graph's bar order is the opposite (blue taller than grey). Since integer rounding preserves order and bars differ visibly, the registered disagreement reproduces without treating pixel coordinates as exact percentages. Heights approximately64 and56% are diagnostic only; ordinary label±0.5point plus approximate visual≈1point is acknowledged.
- **Necessary inputs available; exact missing inputs/definitions:** All graphic elements needed for label-versus-height/order comparison available. Exact underlying percentages, denominators, compliant counts, CI procedure, test/covariance and graphics input dataset are absent. The printed P value is not mechanically recalculated.
- **Source-grounded alternative interpretation:** Annotations may be assigned to the opposite arms, or the bar/legend encoding may be wrong; a different annotation quantity would require a definition absent from the caption.
- **Direct observation versus inferred explanation:** Labels, bar order/heights, axis and legend are direct current-image observations. A swap, stale text, wrong graphics data or group assignment is an inferred explanation, not an identified production error.
- **Exact remaining human question:** Which exact arm-specific vegetables compliance percentages and population/definition generated the labels and bars, and which assignments are intended?
- **Document roles confirmed by content:** REPORT graphic annotations, REPORT same graphic height/percent axis/legend in one results supplement.
- **Relationship type and all relationships confirmed/corrected:** Primary category corrected from Measure, label, or scale inconsistency to Numeric or arithmetic inconsistency: the directly compared quantities are two numeric encodings of the same percentage; a mislabeled arm is only a possible mechanism. S_W/allS_W remain; derived domain corrected to statistical_results. No PLAN comparison.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Current visual label-versus-graphic comparison reproduces the assigned mismatch, independent of approximate inherited pixel coordinates.

## C049 — Meat eFigure 2 percentage annotations and bar heights

**Status:** Pending Human Adjudication. **Primary category:** Numeric or arithmetic inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** statistical_results. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [results physical p26](../../../joi190106supp3_prod_1635377898.49725.pdf#page=26) eFigure 2 Down Meat pair, same-color percent labels, percent-axis ticks and arm legend. Current fresh source render at160dpi visually checked for this exact pair.
- **Source printed value/text matched:** Blue Intervention60%; grey Control62%; P=0.08, matched.
- **Comparator printed value/text matched:** Blue taller than grey; blue/grey bar heights approximately62 and60%, respectively, against0/20/40/60/80/100% ticks. Legend blue/purpleIntervention, greyControl and percentage-of-participants caption matched.
- **Consistency rule applicable:** Same-color numeric percentage and percentage-height encoding for the same outcome/arm must agree. Rank inversion can establish disagreement without exact digitization; the dessert mismatch additionally uses clear scale separation.
- **Calculation or logical comparison reproduced:** Numeric labels have blue60<grey62, but the graph's bar order is the opposite (blue taller than grey). Since integer rounding preserves order and bars differ visibly, the registered disagreement reproduces without treating pixel coordinates as exact percentages. Heights approximately62 and60% are diagnostic only; ordinary label±0.5point plus approximate visual≈1point is acknowledged.
- **Necessary inputs available; exact missing inputs/definitions:** All graphic elements needed for label-versus-height/order comparison available. Exact underlying percentages, denominators, compliant counts, CI procedure, test/covariance and graphics input dataset are absent. The printed P value is not mechanically recalculated.
- **Source-grounded alternative interpretation:** Annotations may be assigned to the opposite arms, or the bar/legend encoding may be wrong; a different annotation quantity would require a definition absent from the caption.
- **Direct observation versus inferred explanation:** Labels, bar order/heights, axis and legend are direct current-image observations. A swap, stale text, wrong graphics data or group assignment is an inferred explanation, not an identified production error.
- **Exact remaining human question:** Which exact arm-specific meat compliance percentages and population/definition generated the labels and bars, and which assignments are intended?
- **Document roles confirmed by content:** REPORT graphic annotations, REPORT same graphic height/percent axis/legend in one results supplement.
- **Relationship type and all relationships confirmed/corrected:** Primary category corrected from Measure, label, or scale inconsistency to Numeric or arithmetic inconsistency: the directly compared quantities are two numeric encodings of the same percentage; a mislabeled arm is only a possible mechanism. S_W/allS_W remain; derived domain corrected to statistical_results. No PLAN comparison.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Current visual label-versus-graphic comparison reproduces the assigned mismatch, independent of approximate inherited pixel coordinates.

## C050 — Sugary dessert eFigure 2 percentage annotations and bar heights

**Status:** Pending Human Adjudication. **Primary category:** Numeric or arithmetic inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** statistical_results. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [results physical p26](../../../joi190106supp3_prod_1635377898.49725.pdf#page=26) eFigure 2 Down Sugary dessert pair, same-color percent labels, percent-axis ticks and arm legend. Current fresh source render at160dpi visually checked for this exact pair.
- **Source printed value/text matched:** Blue Intervention59%; grey Control58%; P<0.001, matched.
- **Comparator printed value/text matched:** Blue near68%, grey near60%; blue/grey bar heights approximately68 and60%, respectively, against0/20/40/60/80/100% ticks. Legend blue/purpleIntervention, greyControl and percentage-of-participants caption matched.
- **Consistency rule applicable:** Same-color numeric percentage and percentage-height encoding for the same outcome/arm must agree. Rank inversion can establish disagreement without exact digitization; the dessert mismatch additionally uses clear scale separation.
- **Calculation or logical comparison reproduced:** Blue59% is below60 by its text while the bar top is clearly well above60, around68; grey58% is near a60-height bar. The blue difference is approximately9points, far beyond ordinary integer-label±0.5 and conservative visual reading≈1point. Swapping59/58 cannot reproduce the blue height. Heights are approximate visual diagnostics, not replacement source values.
- **Necessary inputs available; exact missing inputs/definitions:** All graphic elements needed for label-versus-height/order comparison available. Exact underlying percentages, denominators, compliant counts, CI procedure, test/covariance and graphics input dataset are absent. The printed P value is not mechanically recalculated.
- **Source-grounded alternative interpretation:** Annotations may be stale or use a different compliance definition; the caption does not distinguish their quantity from bar heights. Pairwise swapping alone is insufficient.
- **Direct observation versus inferred explanation:** Labels, bar order/heights, axis and legend are direct current-image observations. A swap, stale text, wrong graphics data or group assignment is an inferred explanation, not an identified production error.
- **Exact remaining human question:** Which exact arm-specific sugary dessert compliance percentages and population/definition generated the labels and bars, and which assignments are intended?
- **Document roles confirmed by content:** REPORT graphic annotations, REPORT same graphic height/percent axis/legend in one results supplement.
- **Relationship type and all relationships confirmed/corrected:** Primary category corrected from Measure, label, or scale inconsistency to Numeric or arithmetic inconsistency: the directly compared quantities are two numeric encodings of the same percentage; a mislabeled arm is only a possible mechanism. S_W/allS_W remain; derived domain corrected to statistical_results. No PLAN comparison.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Current visual label-versus-graphic comparison reproduces the assigned mismatch, independent of approximate inherited pixel coordinates.

## C051 — Intervention baseline weight summaries differ across reports

**Status:** Pending Human Adjudication. **Primary category:** Cross-document numeric inconsistency. **Relationship type:** S_C. **All relationships:** S_C. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) Table1 Intervention baseline row; [results physical p23](../../../joi190106supp3_prod_1635377898.49725.pdf#page=23) eTable9 MI Intervention baseline row. Exact current-PDF cells found in fresh direct extraction; [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) baseline/follow-up analysis statement checked.
- **Source printed value/text matched:** Table1 Intervention headerN3272, baseline mean(SD) 86.7 (13.0) kg, matched.
- **Comparator printed value/text matched:** eTable9 MI Intervention headerN3272, baseline mean(SD) 86.5 (12.9) kg, matched. The selected eTable9 cells are MI, not its separately labeled completers-only columns.
- **Consistency rule applicable:** Matched baseline arm/variable/unit/summary labels should agree when the same records/calculation are intended. Matching cohort headers establish a reporting identity cue but do not prove identical endpoint-specific available records.
- **Calculation or logical comparison reproduced:** Means differ0.2kg; SDs0.1kg. Means' nearest one-decimal bins [86.65,86.75) versus[86.45,86.55) are disjoint. Registered displayed-value comparison reproduced; it remains conditional on common baseline records and statistic convention.
- **Necessary inputs available; exact missing inputs/definitions:** Both printed values/labels, armN and main follow-up-only imputation text available. Exactendpoint-specific baseline weight availability, mean/SD definition and exact measurement selection, plus variable-specific available-case denominators and analytic data/code, are unavailable.
- **Source-grounded alternative interpretation:** Different endpoint-specific available cases, measurement selection or analytic weighting may explain different baseline means despite equal arm headers. Completers-only summaries are a different population and do not resolve the selected MI/replacement comparison.
- **Direct observation versus inferred explanation:** Printed differing baseline summaries are direct. Identical baseline record sets are an explicit conditional premise; a copying/preparation error or hidden subset change is an inferred explanation only.
- **Exact remaining human question:** Do these two intervention weight baseline summaries use identical records and statistic/rounding definitions, and what explains 86.7 (13.0) kg versus86.5 (12.9) kg?
- **Document roles confirmed by content:** REPORT main trial baseline table and REPORT retrospective results supplement baseline table. The main Methods is REPORT supporting context.
- **Relationship type and all relationships confirmed/corrected:** S_C only: mismatch is between two REPORT documents; contextual same-document method statements do not add discrepancy relationships. Cross-document category/report_internal_inconsistency confirmed; no PLAN material is used as a discrepancy comparator.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The exact printed summaries match the registered comparison; differing inputs or definitions remain a named conditional question rather than a resolved mechanism.

## C052 — Control baseline weight summaries differ across reports

**Status:** Pending Human Adjudication. **Primary category:** Cross-document numeric inconsistency. **Relationship type:** S_C. **All relationships:** S_C. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) Table1 Control baseline row; [results physical p23](../../../joi190106supp3_prod_1635377898.49725.pdf#page=23) eTable9 MI Control baseline row. Exact current-PDF cells found in fresh direct extraction; [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) baseline/follow-up analysis statement checked.
- **Source printed value/text matched:** Table1 Control headerN3311, baseline mean(SD) 86.4 (13.0) kg, matched.
- **Comparator printed value/text matched:** eTable9 MI Control headerN3311, baseline mean(SD) 86.3 (13.0) kg, matched. The selected eTable9 cells are MI, not its separately labeled completers-only columns.
- **Consistency rule applicable:** Matched baseline arm/variable/unit/summary labels should agree when the same records/calculation are intended. Matching cohort headers establish a reporting identity cue but do not prove identical endpoint-specific available records.
- **Calculation or logical comparison reproduced:** Means differ0.1kg; SDs agree13.0kg. Distinct adjacent one-decimal bins cannot ordinarily arise from the same unrounded mean under one rounding convention; tie handling at their shared boundary is a narrow special case. Registered displayed-value comparison reproduced; it remains conditional on common baseline records and statistic convention.
- **Necessary inputs available; exact missing inputs/definitions:** Both printed values/labels, armN and main follow-up-only imputation text available. Exactendpoint-specific baseline weight availability, mean definition, exact measurement selection and rounding, plus variable-specific available-case denominators and analytic data/code, are unavailable.
- **Source-grounded alternative interpretation:** Different endpoint-specific available cases, measurement selection or analytic weighting may explain different baseline means despite equal arm headers. Completers-only summaries are a different population and do not resolve the selected MI/replacement comparison.
- **Direct observation versus inferred explanation:** Printed differing baseline summaries are direct. Identical baseline record sets are an explicit conditional premise; a copying/preparation error or hidden subset change is an inferred explanation only.
- **Exact remaining human question:** Do these two control weight baseline summaries use identical records and statistic/rounding definitions, and what explains 86.4 (13.0) kg versus86.3 (13.0) kg?
- **Document roles confirmed by content:** REPORT main trial baseline table and REPORT retrospective results supplement baseline table. The main Methods is REPORT supporting context.
- **Relationship type and all relationships confirmed/corrected:** S_C only: mismatch is between two REPORT documents; contextual same-document method statements do not add discrepancy relationships. Cross-document category/report_internal_inconsistency confirmed; no PLAN material is used as a discrepancy comparator.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The exact printed summaries match the registered comparison; differing inputs or definitions remain a named conditional question rather than a resolved mechanism.

## C053 — Intervention baseline BMI summaries differ across reports

**Status:** Pending Human Adjudication. **Primary category:** Cross-document numeric inconsistency. **Relationship type:** S_C. **All relationships:** S_C. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) Table1 Intervention baseline row; [results physical p23](../../../joi190106supp3_prod_1635377898.49725.pdf#page=23) eTable9 MI Intervention baseline row. Exact current-PDF cells found in fresh direct extraction; [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) baseline/follow-up analysis statement checked.
- **Source printed value/text matched:** Table1 Intervention headerN3272, baseline mean(SD) 32.5 (3.4), matched.
- **Comparator printed value/text matched:** eTable9 MI Intervention headerN3272, baseline mean(SD) 32.6 (3.4) kg/m², matched. The selected eTable9 cells are MI, not its separately labeled completers-only columns.
- **Consistency rule applicable:** Matched baseline arm/variable/unit/summary labels should agree when the same records/calculation are intended. Matching cohort headers establish a reporting identity cue but do not prove identical endpoint-specific available records.
- **Calculation or logical comparison reproduced:** Means differ0.1kg/m²; SDs agree3.4. Adjacent one-decimal displays need different means or rounding conventions; shared-boundary tie handling is a narrow special case. Registered displayed-value comparison reproduced; it remains conditional on common baseline records and statistic convention.
- **Necessary inputs available; exact missing inputs/definitions:** Both printed values/labels, armN and main follow-up-only imputation text available. Exactendpoint-specific baseline BMI availability, BMI calculation/averaging, imputation/weighting and rounding, plus variable-specific available-case denominators and analytic data/code, are unavailable.
- **Source-grounded alternative interpretation:** Different endpoint-specific available cases, measurement selection or analytic weighting may explain different baseline means despite equal arm headers. Completers-only summaries are a different population and do not resolve the selected MI/replacement comparison.
- **Direct observation versus inferred explanation:** Printed differing baseline summaries are direct. Identical baseline record sets are an explicit conditional premise; a copying/preparation error or hidden subset change is an inferred explanation only.
- **Exact remaining human question:** Do these two intervention BMI baseline summaries use identical records and statistic/rounding definitions, and what explains 32.5 (3.4) versus32.6 (3.4) kg/m²?
- **Document roles confirmed by content:** REPORT main trial baseline table and REPORT retrospective results supplement baseline table. The main Methods is REPORT supporting context.
- **Relationship type and all relationships confirmed/corrected:** S_C only: mismatch is between two REPORT documents; contextual same-document method statements do not add discrepancy relationships. Cross-document category/report_internal_inconsistency confirmed; no PLAN material is used as a discrepancy comparator.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The exact printed summaries match the registered comparison; differing inputs or definitions remain a named conditional question rather than a resolved mechanism.

## C054 — Control baseline BMI summaries differ across reports

**Status:** Pending Human Adjudication. **Primary category:** Cross-document numeric inconsistency. **Relationship type:** S_C. **All relationships:** S_C. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) Table1 Control baseline row; [results physical p23](../../../joi190106supp3_prod_1635377898.49725.pdf#page=23) eTable9 MI Control baseline row. Exact current-PDF cells found in fresh direct extraction; [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) baseline/follow-up analysis statement checked.
- **Source printed value/text matched:** Table1 Control headerN3311, baseline mean(SD) 32.5 (3.5), matched.
- **Comparator printed value/text matched:** eTable9 MI Control headerN3311, baseline mean(SD) 32.6 (3.5) kg/m², matched. The selected eTable9 cells are MI, not its separately labeled completers-only columns.
- **Consistency rule applicable:** Matched baseline arm/variable/unit/summary labels should agree when the same records/calculation are intended. Matching cohort headers establish a reporting identity cue but do not prove identical endpoint-specific available records.
- **Calculation or logical comparison reproduced:** Means differ0.1kg/m²; SDs agree3.5. Adjacent one-decimal displays need different means or rounding conventions; shared-boundary tie handling is a narrow special case. Registered displayed-value comparison reproduced; it remains conditional on common baseline records and statistic convention.
- **Necessary inputs available; exact missing inputs/definitions:** Both printed values/labels, armN and main follow-up-only imputation text available. Exactendpoint-specific baseline BMI availability, BMI calculation/averaging, imputation/weighting and rounding, plus variable-specific available-case denominators and analytic data/code, are unavailable.
- **Source-grounded alternative interpretation:** Different endpoint-specific available cases, measurement selection or analytic weighting may explain different baseline means despite equal arm headers. Completers-only summaries are a different population and do not resolve the selected MI/replacement comparison.
- **Direct observation versus inferred explanation:** Printed differing baseline summaries are direct. Identical baseline record sets are an explicit conditional premise; a copying/preparation error or hidden subset change is an inferred explanation only.
- **Exact remaining human question:** Do these two control BMI baseline summaries use identical records and statistic/rounding definitions, and what explains 32.5 (3.5) versus32.6 (3.5) kg/m²?
- **Document roles confirmed by content:** REPORT main trial baseline table and REPORT retrospective results supplement baseline table. The main Methods is REPORT supporting context.
- **Relationship type and all relationships confirmed/corrected:** S_C only: mismatch is between two REPORT documents; contextual same-document method statements do not add discrepancy relationships. Cross-document category/report_internal_inconsistency confirmed; no PLAN material is used as a discrepancy comparator.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The exact printed summaries match the registered comparison; differing inputs or definitions remain a named conditional question rather than a resolved mechanism.

## C055 — Intervention baseline PDQS summaries differ across reports

**Status:** Pending Human Adjudication. **Primary category:** Cross-document numeric inconsistency. **Relationship type:** S_C. **All relationships:** S_C. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p5](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5) Table2 Intervention baseline row; [results physical p16](../../../joi190106supp3_prod_1635377898.49725.pdf#page=16) eTable6 baseline replacement Intervention baseline row. Exact current-PDF cells found in fresh direct extraction; [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) baseline/follow-up analysis statement checked.
- **Source printed value/text matched:** Table2 Intervention headerN3272, baseline mean(SD) 21.1 (3.7), matched.
- **Comparator printed value/text matched:** eTable6 baseline replacement Intervention headerN3272, baseline mean(SD) 21.0 (3.7), matched.
- **Consistency rule applicable:** Matched baseline arm/variable/unit/summary labels should agree when the same records/calculation are intended. Matching cohort headers establish a reporting identity cue but do not prove identical endpoint-specific available records.
- **Calculation or logical comparison reproduced:** Means differ0.1point; SDs agree3.7. Adjacent one-decimal displays ordinarily cannot be the same mean under one rounding rule; exact boundary tie handling could matter. Registered displayed-value comparison reproduced; it remains conditional on common baseline records and statistic convention.
- **Necessary inputs available; exact missing inputs/definitions:** Both printed values/labels, armN and main follow-up-only imputation text available. Exactbaseline PDQS record sets, scoring version, missingness/recoding and rounding, plus variable-specific available-case denominators and analytic data/code, are unavailable.
- **Source-grounded alternative interpretation:** Different endpoint-specific available cases, measurement selection or analytic weighting may explain different baseline means despite equal arm headers. Completers-only summaries are a different population and do not resolve the selected MI/replacement comparison.
- **Direct observation versus inferred explanation:** Printed differing baseline summaries are direct. Identical baseline record sets are an explicit conditional premise; a copying/preparation error or hidden subset change is an inferred explanation only.
- **Exact remaining human question:** Do these two intervention PDQS baseline summaries use identical records and statistic/rounding definitions, and what explains 21.1 (3.7) versus21.0 (3.7)?
- **Document roles confirmed by content:** REPORT main trial baseline table and REPORT retrospective results supplement baseline table. The main Methods is REPORT supporting context.
- **Relationship type and all relationships confirmed/corrected:** S_C only: mismatch is between two REPORT documents; contextual same-document method statements do not add discrepancy relationships. Cross-document category/report_internal_inconsistency confirmed; no PLAN material is used as a discrepancy comparator.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The exact printed summaries match the registered comparison; differing inputs or definitions remain a named conditional question rather than a resolved mechanism.

## C056 — Control baseline PDQS summaries differ across reports

**Status:** Pending Human Adjudication. **Primary category:** Cross-document numeric inconsistency. **Relationship type:** S_C. **All relationships:** S_C. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p5](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5) Table2 Control baseline row; [results physical p16](../../../joi190106supp3_prod_1635377898.49725.pdf#page=16) eTable6 baseline replacement Control baseline row. Exact current-PDF cells found in fresh direct extraction; [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) baseline/follow-up analysis statement checked.
- **Source printed value/text matched:** Table2 Control headerN3311, baseline mean(SD) 21.1 (3.7), matched.
- **Comparator printed value/text matched:** eTable6 baseline replacement Control headerN3311, baseline mean(SD) 21.0 (3.7), matched.
- **Consistency rule applicable:** Matched baseline arm/variable/unit/summary labels should agree when the same records/calculation are intended. Matching cohort headers establish a reporting identity cue but do not prove identical endpoint-specific available records.
- **Calculation or logical comparison reproduced:** Means differ0.1point; SDs agree3.7. Adjacent one-decimal displays ordinarily cannot be the same mean under one rounding rule; exact boundary tie handling could matter. Registered displayed-value comparison reproduced; it remains conditional on common baseline records and statistic convention.
- **Necessary inputs available; exact missing inputs/definitions:** Both printed values/labels, armN and main follow-up-only imputation text available. Exactbaseline PDQS record sets, scoring version, missingness/recoding and rounding, plus variable-specific available-case denominators and analytic data/code, are unavailable.
- **Source-grounded alternative interpretation:** Different endpoint-specific available cases, measurement selection or analytic weighting may explain different baseline means despite equal arm headers. Completers-only summaries are a different population and do not resolve the selected MI/replacement comparison.
- **Direct observation versus inferred explanation:** Printed differing baseline summaries are direct. Identical baseline record sets are an explicit conditional premise; a copying/preparation error or hidden subset change is an inferred explanation only.
- **Exact remaining human question:** Do these two control PDQS baseline summaries use identical records and statistic/rounding definitions, and what explains 21.1 (3.7) versus21.0 (3.7)?
- **Document roles confirmed by content:** REPORT main trial baseline table and REPORT retrospective results supplement baseline table. The main Methods is REPORT supporting context.
- **Relationship type and all relationships confirmed/corrected:** S_C only: mismatch is between two REPORT documents; contextual same-document method statements do not add discrepancy relationships. Cross-document category/report_internal_inconsistency confirmed; no PLAN material is used as a discrepancy comparator.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The exact printed summaries match the registered comparison; differing inputs or definitions remain a named conditional question rather than a resolved mechanism.

## C057 — Intervention baseline energy SD summaries differ across reports

**Status:** Pending Human Adjudication. **Primary category:** Cross-document numeric inconsistency. **Relationship type:** S_C. **All relationships:** S_C. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main physical p7](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=7) Table3 Intervention baseline row; [results physical p21](../../../joi190106supp3_prod_1635377898.49725.pdf#page=21) eTable8 baseline replacement Intervention baseline row. Exact current-PDF cells found in fresh direct extraction; [main physical p4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) baseline/follow-up analysis statement checked.
- **Source printed value/text matched:** Table3 Intervention headerN3272, baseline mean(SD) 2355 (555) kcal/d, matched.
- **Comparator printed value/text matched:** eTable8 baseline replacement Intervention headerN3272, baseline mean(SD) 2355 (544) kcal/d, matched.
- **Consistency rule applicable:** Matched baseline arm/variable/unit/summary labels should agree when the same records/calculation are intended. Matching cohort headers establish a reporting identity cue but do not prove identical endpoint-specific available records.
- **Calculation or logical comparison reproduced:** Means agree2355kcal/d; SD difference555−544=11kcal/d. Joint nearest integer rounding allowance1kcal/d cannot explain11. Registered displayed-value comparison reproduced; it remains conditional on common baseline records and statistic convention.
- **Necessary inputs available; exact missing inputs/definitions:** Both printed values/labels, armN and main follow-up-only imputation text available. Exactbaseline energy record sets, SD denominator/calculation, analytic weighting and subset selection, plus variable-specific available-case denominators and analytic data/code, are unavailable.
- **Source-grounded alternative interpretation:** Different available baseline records, SD convention or weighting could explain an SD difference despite equal mean/cohort header. A completers544SD is context only and does not establish identity with the main population.
- **Direct observation versus inferred explanation:** Printed differing baseline summaries are direct. Identical baseline record sets are an explicit conditional premise; a copying/preparation error or hidden subset change is an inferred explanation only.
- **Exact remaining human question:** Do these two intervention energy intake baseline summaries use identical records and statistic/rounding definitions, and what explains 2355 (555) kcal/d versus2355 (544) kcal/d?
- **Document roles confirmed by content:** REPORT main trial baseline table and REPORT retrospective results supplement baseline table. The main Methods is REPORT supporting context.
- **Relationship type and all relationships confirmed/corrected:** S_C only: mismatch is between two REPORT documents; contextual same-document method statements do not add discrepancy relationships. Cross-document category/report_internal_inconsistency confirmed; no PLAN material is used as a discrepancy comparator.
- **Evidence state and determining recheck fact:** `recorded_candidate` — The exact printed summaries match the registered comparison; differing inputs or definitions remain a named conditional question rather than a resolved mechanism.

## C058 — Red-meat one-point boundary differs between plan and report

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** P_R. **All relationships:** P_R. **Review domain:** protocol_report. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [protocol physical p45](../../../joi190106supp1_prod_1635377898.47058.pdf#page=45) item6 lines1446–1447 and one-point instructionlines1435–1438; [results physical p2](../../../joi190106supp3_prod_1635377898.49725.pdf#page=2) eTable1 er-MedDiet negatively weighted red/processed-meat row. Exact locations found; current source images visually checked.
- **Source printed value/text matched:** Protocol `Consume≤1 serving ... of red meat, hamburgers, or meat products ... per week`, serving100–150g, and `One point ... for each objective met`, matched. Native glyph extraction d1/ambiguous encoding is overridden by direct image's clear≤1.
- **Comparator printed value/text matched:** Results17-item er-MedDiet row `<1 servings/wk red or processed meats`, matched; image confirms strict<.
- **Consistency rule applicable:** For the same one-point food component and weekly serving unit,≤1 and<1 classify exact1 differently. Content/score-version alignment is required before interpreting implementation.
- **Calculation or logical comparison reproduced:** At exactly1 serving/week, PLAN objective met and awards1point, while REPORT's strict<1 objective is not met. Difference1point for this component; no rounding tolerance for literal operator identity. Effect on observed scores/means not calculable without boundary counts.
- **Necessary inputs available; exact missing inputs/definitions:** Both score names, item semantics, operators, weekly unit and plan point award available. Applied questionnaire/version, report serving-size convention, equality counts and any deliberate score amendment not identified in supplied relevant passages.
- **Source-grounded alternative interpretation:** An intentional updated score version or differing serving operationalization could explain the boundary; the package's mapped amendment list does not identify this equality change.
- **Direct observation versus inferred explanation:** Inclusive PLAN glyph and strict REPORT glyph are direct observations. Actual scoring-code divergence, protocol violation, or changed trial means are not inferred.
- **Exact remaining human question:** Which17-item score version/operator and serving definition were applied, was equality handling deliberately amended, and how many scored records were exactly1serving/week?
- **Document roles confirmed by content:** PLAN prospective17-objective operational protocol; REPORT retrospective dietary-score-definition results table. Roles confirmed from compared content.
- **Relationship type and all relationships confirmed/corrected:** P_R only under precedenceP_R>P_P>S_C>S_W: a genuine PLAN–REPORT score-definition discrepancy. Measure category/protocol_report confirmed. This plan is a discrepancy comparator, not mere corroboration.
- **Evidence state and determining recheck fact:** `recorded_candidate` — Direct image confirms≤1 versus<1 and reproduces the registered boundary mismatch; missing applied-version inputs do not settle implementation.

## C059 — Pastries baseline mean-versus-median labels across reports

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_C. **All relationships:** S_C. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main article physical p6, Foods and Food Groups narrative](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=6); [results supplement physical p5, eTable 2 continued, Pastries baseline row](../../../joi190106supp3_prod_1635377898.49725.pdf#page=5); [results supplement physical p6, eTable 2 continued footer](../../../joi190106supp3_prod_1635377898.49725.pdf#page=6). All locations found in current-source extraction; main p6 and results p5 also visually confirmed.
- **Source printed value/text matched:** The main narrative says, “For pastries, mean baseline consumption was 114 g/wk in the control group and 121 g/wk in the intervention group.” The intervening line breaks and hyphenation are typographical; the word mean and the values/arm assignments are visually confirmed.
- **Comparator printed value/text matched:** eTable 2 p5 prints Pastries (g/week), Baseline, median (IQR): Intervention group N=3,272, 121 (42, 275); Control group N=3,311, 114 (42, 261). Its p6 footer says, “Baseline data are median (IQR)” and separately states that 6-month and 12-month changes are means (95% CI) calculated using mixed effect models. The comparison uses baseline centers, not change estimates.
- **Consistency rule applicable:** The same food, baseline time, unit and arm-specific printed centers are described by different statistical labels in two REPORT documents. Mean and median denote different summary definitions. This is an applicable label comparison, without assuming that the actual unreported numerical means differ from the medians. Ordinary formatting differences between g/wk and g/week do not change the unit.
- **Calculation or logical comparison reproduced:** Main intervention 121 equals table intervention baseline median center 121; main control 114 equals table control baseline median center 114. The narrative label mean differs from both the baseline row label median (IQR) and the baseline-specific footer. The repeated numbers and different labels reproduce the registered conditional question. No raw-data arithmetic or inferential reconstruction is needed for this printed comparison.
- **Necessary inputs available; exact missing inputs/definitions:** Printed centers, labels, food, baseline timing, arm headings and unit are available. The package does not supply participant-level baseline pastry observations, independently calculated baseline arithmetic means, the applicable mean/quantile calculations for these centers, or author intent. Those inputs are necessary to distinguish coincident rounded means/medians from an unintended statistic label; they are not necessary to observe the printed labeling difference.
- **Source-grounded alternative interpretation:** Independently calculated baseline means and medians might both round to 121 and 114 g/week, in which case the two reports could be reporting different summaries with coincident displayed centers. The p6 footer distinguishes mean changes from median baselines, so the word mean in nearby change-result prose could also explain the narrative wording. Neither possibility is established by the supplied values, and neither selects a correction.
- **Direct observation versus inferred explanation:** The baseline values and words mean and median (IQR) are direct observations. Copying a median into mean prose, loose wording, or an editorial mechanism is inference only. A claim that the actual mean differs numerically from the actual median is not established.
- **Exact remaining human question:** Are the baseline pastry values 121 g/week for intervention and 114 g/week for control intended as means, medians, or independently calculated summaries that coincide at displayed precision, and which statistic definition should accompany these values in downstream extraction?
- **Document roles confirmed by content:** REPORT main article p6 narrative; REPORT results supplement p5 eTable 2 baseline pastries. The p6 footer is also REPORT results content. These locations present observed baseline data and modeled follow-up results, rather than prospective protocol/SAP instructions. Roles are confirmed without using file names as the basis.
- **Relationship type and all relationships confirmed/corrected:** S_C only, confirmed: the substantive compared labels are in the main article and a different results supplement. The p6 footer corroborates the table's baseline label and is not a separate within-report discrepancy. No PLAN content is a comparator. No higher-precedence P_R or P_P relationship applies. Primary category and mechanically derived report_internal_inconsistency domain are confirmed; no classification correction is required. Classification ambiguity: roles/type are clear; the intended statistic remains unresolved.
- **Evidence state and determining recheck fact:** recorded_candidate — the current sources contain the registered 121/114 baseline centers labeled mean in the article and median (IQR) in eTable 2. Their intended summary identity remains conditional on the named missing calculations/definition. No registered transcription or source location is disproven.

## C060 — Vegetables baseline mean-versus-median labels across reports

**Status:** Pending Human Adjudication. **Primary category:** Measure, label, or scale inconsistency. **Relationship type:** S_C. **All relationships:** S_C. **Review domain:** report_internal_inconsistency. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main article physical p6, Foods and Food Groups narrative](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=6); [results supplement physical p3, eTable 2 Vegetables baseline row](../../../joi190106supp3_prod_1635377898.49725.pdf#page=3); [results supplement physical p4, eTable 2 footer](../../../joi190106supp3_prod_1635377898.49725.pdf#page=4). All found in current-source extraction; main p6 and results p3 also visually confirmed. [Results supplement physical p5, eTable 2 continuation headings](../../../joi190106supp3_prod_1635377898.49725.pdf#page=5) was inspected for arm-context corroboration.
- **Source printed value/text matched:** Main p6 says vegetables had “mean baseline consumption of 2130 g/wk in the control group and 2168 g/wk in the intervention group.” The relevant mean word, centers and arm assignments are visually confirmed; the next clause concerns subsequent within-group changes.
- **Comparator printed value/text matched:** eTable 2 p3 prints Vegetables (g/week), Baseline, median (IQR): first numeric column 2,168 (1,621, 2,814), N=3,272; second numeric column 2,130 (1,596, 2,863), N=3,311. Both p3 column headings literally say Intervention group. This duplicated heading is preserved, not silently normalized. In the same table's p5 continuation, the columns are explicitly Intervention group N=3,272 and Control group N=3,311. The p4 footer says, “Baseline data are median (IQR)” and separately defines 6-month and 12-month changes as means (95% CI) from mixed effect models.
- **Consistency rule applicable:** Same food, baseline time, unit and displayed centers are compared across two REPORT documents. Mean and median are different summary definitions. The p5 continuation and consistent N/column position support the registered control-column interpretation of p3's second numeric column, while its literal duplicated heading is an additional identity caveat. The mean-versus-median label difference for the 2168 intervention value is explicit even without interpreting the second column. No assumption of numerical inequality of means/medians is made.
- **Calculation or logical comparison reproduced:** Article intervention 2168 equals p3 first-column baseline median center 2,168; article control 2130 equals p3 second-column baseline median center 2,130. Removing thousands-separator commas changes neither value. Both table centers are under the baseline median (IQR) label, while the article calls the pair mean baseline consumption. The explicit baseline footer supports this reading. This reproduces the registered conditional label comparison; it does not compute a numerical mean-minus-median difference.
- **Necessary inputs available; exact missing inputs/definitions:** Printed centers, baseline label/footer, food, timing and unit are supplied. Table continuation headings and Ns supply arm-context support. Participant-level baseline vegetable observations, independently calculated baseline arithmetic means, the applicable mean/quantile calculations, and author intent are absent. The intended p3 second-column heading is not explicitly explained in the package. These missing definitions prevent deciding whether different summaries happen to coincide or one label is unintended; they do not erase the direct statistic-label comparison.
- **Source-grounded alternative interpretation:** The means and medians might independently round to 2168/2130, so the article and table could present different summaries with equal printed centers. The narrative's nearby modeled mean-change results and the table's explicit mean-change/median-baseline distinction offer a possible explanation for wording, but no production mechanism is shown. The p3 second-column heading may itself be unintended, as the p5 continuation calls the same-position N=3,311 column Control group; this is corroborating context, not an independently adjudicated correction.
- **Direct observation versus inferred explanation:** Main mean wording, p3 median baseline row, footer, both duplicated p3 headings and p5 continuation headings are directly observed. Treating the p3 N=3,311 column as the control column is a source-supported contextual interpretation, explicitly bounded. Copying, loose prose, intended headings and the actual unreported numerical mean/median relationship are inferred or unresolved.
- **Exact remaining human question:** Are the vegetable centers 2168 and 2130 g/week intended as baseline means, baseline medians, or independently calculated summaries that coincide at displayed precision? Does eTable 2 p3's N=3,311 column denote control, consistent with its continuation, and which statistic definition should accompany each baseline value in downstream extraction?
- **Document roles confirmed by content:** REPORT main article p6 narrative; REPORT results supplement p3 eTable 2 baseline vegetables. Its p4 footer and p5 continuation are also REPORT result content, showing observed baseline summaries and modeled changes rather than prospective instructions. Both registered document roles are confirmed by content.
- **Relationship type and all relationships confirmed/corrected:** S_C only, confirmed: the registered substantive mean/median comparison crosses main article and results supplement. The footer/continuation corroborate the table side; the independent duplicated arm heading is not added as a substantive within-report discrepancy relationship to this candidate. No PLAN comparator or higher-precedence relationship is present. Primary category and mechanically derived report_internal_inconsistency domain are confirmed; no classification correction is required. Classification ambiguity: document roles and S_C are clear; the p3 second arm heading is duplicated and its control identity is supported by the continuation, while intended summary identity remains unresolved.
- **Evidence state and determining recheck fact:** recorded_candidate — the current sources contain the registered 2168/2130 baseline centers called mean in the article and median (IQR) in eTable 2. The intervention-side label comparison is explicit, and continuation headings/Ns support the registered second-column context. No registered number/location is disproven; the statistical-identity question remains as registered with the literal heading caveat now recorded.

## C061 — Twelve-month total-alcohol interval and P-value require a construction definition

**Status:** Pending Human Adjudication. **Primary category:** Statistical reporting inconsistency. **Relationship type:** S_W. **All relationships:** S_W. **Review domain:** statistical_results. **Evidence state:** recorded_candidate. **Suggested review disposition:** retain (mechanical prefill only).

- **Cited location found:** [main article physical p7, Table 3 total-alcohol twelve-month change row](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=7); [main article physical p4, Statistical Analysis](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4); [main article physical p8, Table 3 footnotes a and b](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=8). All locations were read in fresh current-source native/layout extraction; the p7 row, column headings and positive upper endpoint were also visually confirmed.
- **Source printed value/text matched:** Table 3 p7 has the row Total Alcohol, %/d, 12-mo change, mean (SD): intervention −0.3 (3.0), control −0.1 (3.0), between-group difference −0.2 (−0.4 to 0.1) under the Between-Group Difference (95% CI) heading. The upper endpoint is printed positive 0.1, not zero or negative 0.1. The row is under Multiple Imputation: All Randomized Participants, with arm Ns 3272 and 3311.
- **Comparator printed value/text matched:** The same twelve-month row prints P Value .01. Main p4 states all statistical tests were 2-sided and P < .05 was deemed statistically significant. It describes mixed-effects linear models, random intercepts at site, participant and cluster family level, eight imputations for each missing measurement, and exploratory secondary analyses without additional type I error adjustment. Table 3 p8 footnote b defines between-group estimates as calculated using mixed-effect models with site and intracluster correlations (couples) as random factors; footnote a gives 838 imputed energy-variable values at six months and 807 at twelve months. None of these statements specifies the exact common CI/test construction for this row.
- **Consistency rule applicable:** Only conditionally: for a 95% interval and a two-sided test of the same zero contrast, using compatible confidence/test constructions, variance estimation, adjustment, degrees of freedom and multiple-imputation pooling, a zero-containing interval and a P value below .05 disagree on that matched null comparison. The report supplies the row pairing, 95% label, general two-sided statement and mixed-model context; it does not establish every compatibility condition. A definite contradiction under an assumed inverse-Wald rule is not claimed.
- **Calculation or logical comparison reproduced:** The printed bounds satisfy −0.4 < 0 < 0.1, and .01 < .05. Thus the interval contains zero while the displayed two-sided P is below the source's significance threshold. The interval also contains the −0.2 point estimate; the candidate does not concern point-estimate containment. Rounded descriptive changes satisfy −0.3 − (−0.1) = −0.2, but this arithmetic does not establish the model's inferential construction. Under ordinary nearest rounding to one decimal, a positive displayed upper endpoint 0.1 cannot arise solely from rounding a small negative endpoint to zero. This does not establish compatible interval/test construction or an exact alternative P value.
- **Necessary inputs available; exact missing inputs/definitions:** The row, contrast label, point estimate, both confidence limits, 95% level, P value, two-sided statement, alpha threshold, mixed-model context and use of eight imputations are available. Missing are confirmation that P and CI test exactly the same modeled contrast; exact CI construction and test statistic; their variance estimators; model/adjustment identity for each display; multiple-imputation pooling for CI and P; effective degrees of freedom; and whether the resulting confidence and testing procedures are compatible. The compared supplied locations do not resolve these definitions. No raw-data, standard-error or degrees-of-freedom reconstruction is substituted.
- **Source-grounded alternative interpretation:** The source's mixed-model/multiple-imputation setting allows the possibility of different CI and P constructions or pooling conventions; if the displays use different inferential definitions, zero inclusion need not invert the displayed test. The package locations cited here do not establish that explanation. A transcription difference is possible but unproven. The six-month row's displayed upper endpoint 0 is a distinct rounding situation and is not substituted for the twelve-month positive endpoint.
- **Direct observation versus inferred explanation:** Same-row −0.2 (−0.4 to 0.1), P=.01, the 95% column label and the general two-sided declaration are direct observations. CI/test duality is a conditional logical rule. A shared variance estimator, identical degrees of freedom, identical pooling, a production mistake and any intended numerical correction are unestablished explanations or assumptions.
- **Exact remaining human question:** What exact CI and P-value constructions generated the twelve-month total-alcohol row, do they refer to the same modeled contrast with compatible variance estimation, adjustment, degrees of freedom and multiple-imputation pooling, and do those definitions explain the positive 0.1 upper confidence endpoint alongside P=.01?
- **Document roles confirmed by content:** REPORT main article p7 Table 3 total-alcohol twelve-month contrast, interval and P-value in the same row. The p4 Methods and p8 result-table footnotes are also REPORT content explaining the analysis used in this retrospective report. Their discussion of analysis methods does not turn them into PLAN documents.
- **Relationship type and all relationships confirmed/corrected:** S_W only, confirmed: the registered interval/P-value comparison is within the same row of one REPORT document. Its Methods and footnotes are contextual definitions, not additional discrepancy relationships. There is no PLAN comparator and no cross-document comparison in this ID. Statistical reporting inconsistency category and mechanically derived statistical_results domain are confirmed; no classification correction is required. Classification ambiguity: roles/type are clear; confidence/test compatibility remains the explicit missing inferential definition.
- **Evidence state and determining recheck fact:** recorded_candidate — the current source confirms the exact same-row twelve-month positive-upper-bound 95% interval and P=.01. The registered conditional question remains as registered because common CI/test construction is not established. The source neither disproves the printed comparison nor supplies a transcription repair; no definite inferential error is asserted.

Limitations: No tool or assigned-location confirmation gap. C059/C060 require the named unavailable baseline summary calculations/definitions and author intent to settle whether equal displayed means and medians were independently calculated. C060 additionally preserves the duplicated p3 heading and its continuation-based arm-context interpretation. C061 requires exact CI/test, contrast, variance, degrees-of-freedom, adjustment and multiple-imputation pooling compatibility definitions. These are evidence limitations, not human dispositions.
