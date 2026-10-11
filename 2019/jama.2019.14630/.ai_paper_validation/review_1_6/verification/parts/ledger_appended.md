## C059 — Pastries baseline mean-versus-median labels across reports

**Status:** Pending Human Adjudication

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main article p6 narrative; REPORT results supplement p5 eTable 2 baseline pastries.

**Review domain:** report_internal_inconsistency

**Checker provenance:** PASS2-N01 from statistical pass 2 fresh runtime 01a1289d-2ec2-73a1-bcae-13562fddd276; checkers/statistical_pass_2_new_candidates.md.


- **Primary category input:** Measure, label, or scale inconsistency.
- **Compared locations and document roles:** REPORT [main article physical p6, Foods and Food Groups narrative](../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=6); REPORT [results supplement physical p5, eTable 2 Pastries baseline row](../../joi190106supp3_prod_1635377898.49725.pdf#page=5). Both describe reported results, not prospective plans.
- **Relationship input:** S_C only; two different REPORT documents. Derived review-domain input: report_internal_inconsistency. No role ambiguity; the actual intended descriptive statistic remains the human question.
- **Source printed values:** Main narrative: “For pastries, mean baseline consumption was 114 g/wk in the control group and 121 g/wk in the intervention group.”
- **Comparator printed values:** eTable 2 Pastries (g/week), “Baseline, median (IQR)”: Intervention 121 (42, 275), Control 114 (42, 261). Same table's footer on p6 defines baseline data as median (IQR).
- **Identity and consistency rule:** Same food, time (baseline), arm, unit and numeric centers. Mean and median identify different descriptive statistics; matching center values do not make their labels interchangeable. No arithmetic tolerance, inferential-test reconstruction or raw-data premise is needed to reproduce the printed label disagreement.
- **Direct observation versus diagnostic explanation:** The exact repeated 121/114 values are called means in the article and medians in the results table. This is a label comparison, not proof that the numerical mean differs from the numerical median. No intended replacement label is selected.
- **Necessary inputs and limitations:** All printed comparison inputs are supplied. Actual baseline participant records, mean calculations, quantile calculations and author intent are absent.
- **Source-grounded alternative:** The same distribution could have means and medians that round to the same centers; alternatively the narrative may use “mean” loosely while the table carries the precise definition. Either interpretation requires the intended statistic to be established; the source does not separately supply a mean calculation for these values.
- **Exact human question:** Are 121/114 g/week intended as baseline means, baseline medians, or two independently calculated summaries that coincide at displayed precision, and which definition should accompany downstream extraction?
- **Relationship inventory implications:** S054–S056 and S097–S098 contain correctly labeled modeled mean changes, whereas their associated baseline values are descriptive medians under eTable 2. S141–S142 and S185–S186 are sensitivity analyses and are not substituted as main-analysis comparators.
- **Duplicate check:** Different printed row/comparator from C038 (olive-oil eTable 4 row/footnote) and C006 (risk-factor figure mean/median). Neither shared statistic names nor possible editorial cause makes these genuine duplicates.


## C060 — Vegetables baseline mean-versus-median labels across reports

**Status:** Pending Human Adjudication

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main article p6 narrative; REPORT results supplement p3 eTable 2 baseline vegetables.

**Review domain:** report_internal_inconsistency

**Checker provenance:** PASS2-N02 from statistical pass 2 fresh runtime 01a1289d-2ec2-73a1-bcae-13562fddd276; checkers/statistical_pass_2_new_candidates.md.


- **Primary category input:** Measure, label, or scale inconsistency.
- **Compared locations and document roles:** REPORT [main article physical p6, Foods and Food Groups narrative](../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=6); REPORT [results supplement physical p3, eTable 2 Vegetables baseline row](../../joi190106supp3_prod_1635377898.49725.pdf#page=3). Both are retrospective results.
- **Relationship input:** S_C only; two different REPORT documents. Derived review-domain input: report_internal_inconsistency. No role ambiguity; intended statistic remains to be identified.
- **Source printed values:** Main narrative: “mean baseline consumption of 2130 g/wk in the control group and 2168 g/wk in the intervention group.”
- **Comparator printed values:** eTable 2 Vegetables (g/week), “Baseline, median (IQR)”: Intervention 2,168 (1,621, 2,814), Control 2,130 (1,596, 2,863). Footer on p4 defines baseline data as median (IQR).
- **Identity and consistency rule:** Same food, baseline time, arms, unit and displayed centers. The same repeated descriptive values have different statistic labels. Mean and median definitions differ independently of rounding; no conclusion about their actual unreported numerical difference is made.
- **Direct observation versus diagnostic explanation:** Source label disagreement is directly observed. Inferring a transcription mechanism or selecting median as a correction would exceed supplied evidence and is not done.
- **Necessary inputs and limitations:** Printed labels and centers available; raw baseline values, actual mean/quantile calculations and author intent absent.
- **Source-grounded alternative:** Independently calculated rounded means and medians could coincide, or narrative wording could loosely describe central consumption. The supplied source does not identify a separate baseline mean calculation for 2168/2130.
- **Exact human question:** Which baseline vegetable statistic is intended for 2168/2130 g/week, and do independently calculated means coincide with the table's medians or is one label unintended?
- **Relationship inventory implications:** S058–S060 and S079–S080 describe modeled mean changes, distinct from the associated baseline median (IQR). S123–S124 and S167–S168 retain their respective completer/replacement analyses; their results are not assumed identical to the MI estimates.
- **Duplicate check:** Distinct food, printed row and comparator from PASS2-N01 and all existing C001–C058. Shared mean/median issue does not authorize merging separate food comparisons.

Statistical pass2 appended C059 and C060 after exact duplicate checking; all prior IDs remain unchanged. No new statistical relationship IDs were required because each comparison cross-references the existing fully registered food-result relationships.
\n
## C061 — Twelve-month total-alcohol interval and P-value require a construction definition

**Status:** Pending Human Adjudication

**Category:** Statistical reporting inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article p7 Table 3 total-alcohol twelve-month contrast, interval and P-value in the same row.

**Review domain:** statistical_results

**Checker provenance:** S026 statistical pass1/pass2 definition-limited observation; fresh quality auditor recommendation; coordinator conditional registration under QUALITY_CONTROL_SCOPE Candidate threshold. Pass2 original conservative non-registration assessment is preserved; no common construction is asserted.

**Exact source locations:** [Main physical p7 Table 3 total alcohol twelve-month change](../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=7); [main physical p4 Statistical Analysis](../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4); [main physical p8 Table 3 footnotes](../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=8).

**Source printed inputs:** The intervention-minus-control twelve-month total-alcohol contrast is −0.2 percentage points/day,95%CI−0.4 to+0.1,P=.01; main table change means are−0.3 and−0.1. Two-sided tests and mixed models/multiple imputation are described, but the interval/P common construction is not explicitly established.

**Conditional consistency rule:** If this95%interval and two-sidedP refer to the same contrast and compatible test/variance/construction at the5%level, an interval spanning zero and P=.01 do not reconcile. This is a conditional reporting question; the package does not establish every necessary compatibility condition. No inverse-Wald calculation or exact replacementP is made.

**Direct observation versus diagnostic reasoning:** The same-row interval spans zero and P=.01 is directly printed. The upper endpoint+0.1 cannot be explained merely as a zero endpoint rounded from a small negative number. A definite test/CI contradiction, shared variance estimator, identical degrees of freedom, or intended correction is not inferred.

**Named missing definition:** Whether the CI and P correspond to exactly the same modeled contrast; CI construction; test statistic; common variance estimator; multiple-imputation pooling; degrees of freedom; model-adjustment identity and confidence/test compatibility.

**Alternative source-grounded interpretations:** Different documented CI and P constructions or pooling conventions might reconcile the displays; the supplied package does not fully identify those constructions. A transcription difference is also possible but unproven. The six-month upper endpoint0 is a separate rounded-endpoint situation and is not treated as this same comparison.

**Human question:** What exact CI and P constructions generated the twelve-month total-alcohol row, are they compatible for the same contrast, and do they explain the positive upper endpoint alongsideP=.01?

**Quality-control relevance:** A data extractor could copy an interval containing zero together with a nominalPbelow.05 without a construction definition. Resolve that conditional extraction question; no paper conclusion or methodological verdict is asserted.
