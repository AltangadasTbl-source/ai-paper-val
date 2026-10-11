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

