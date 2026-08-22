# Numeric Consistency Review

## Scope, evidence basis, and method

This review processed every relationship in the complete 125-item numeric inventory: N001-N038 (DOC-001 main article, PDF pp. 1-12), N1001-N1022 (DOC-002 protocol, PDF pp. 1-69), N2001-N2030 (DOC-003 statistical analysis plan, PDF pp. 1-45), and N3001-N3035 (DOC-004 results supplement, PDF pp. 1-20; DOC-005 PDF p. 1). I used only the current durable relationship and extraction parts listed below, which document direct-PDF confirmation. They are locator/transcription aids; the source locations in every proposal below identify the governing PDF evidence.

- `relationships/parts/main_doc001_numeric.md` and `extraction/parts/main_doc001.md`
- `relationships/parts/support_doc002_numeric.md` and `extraction/parts/support_doc002.md`
- `relationships/parts/support_doc003_numeric.md` and `extraction/parts/support_doc003.md`
- `relationships/parts/support_doc004_doc005_numeric.md` and `extraction/parts/support_doc004_doc005.md`

For each applicable relationship I applied displayed arithmetic; category, subgroup, numerator, denominator, percentage, missingness and population identities; stated rounding; unit, scale, direction, reference-group and measure-label identities; rate/count distinctions; and repeated-value checks. A difference was proposed only where a direct printed contradiction remains after matching measure, population, time point, contrast, and stated precision. The proposals below are not stable candidate IDs, dispositions, severity ratings, or validity judgments; each requires human adjudication.

## Complete relationship disposition

| Inventory scope | IDs checked | Result |
|---|---|---|
| Main article flow, baseline, treatment, follow-up, primary and secondary results, safety, and editorial repetition | N001-N038 (38) | Five proposals below involving this source (flow and four baseline/repeated-value comparisons). All remaining applicable arithmetic, denominators, units, outcome directions, and rate/count labels reconciled or had a source-stated distinction. |
| Protocol treatment, eligibility, schedule, outcome, formula, safety, and planned-analysis definitions | N1001-N1022 (22) | Two proposals below (primary-outcome label and biomarker analyte label). Other protocol items are planning/administrative definitions or are consistent with the matched source result. |
| SAP population, model, formula, scale, template, outcome, safety, and subgroup definitions | N2001-N2030 (30) | Five proposals below (AFEQT label, E/e-prime direction, NT-proBNP time/unit heading, EHRA category example, and ambulatory-HR timing). Blank templates have no numerical result values and were not treated as failed arithmetic. |
| Results supplement schedule, tables, figures, medication, HR, PROM, safety, contextual values, and data-sharing page | N3001-N3035 (35) | Four proposals below involving this source (three baseline comparisons with the main article and the eTable 2 copied interpretation). All percentage, event-total, attendance, subgroup, count/rate, scale, and same-table arithmetic checks reconciled. |
| **Total** | **125** | **13 distinct proposal records** |

## Candidate proposals requiring human adjudication

### Proposal 1 — Randomized total is not the same across the flow diagram and article trial population

- **Mapped relationships and provenance:** N001 and N002; `relationships/parts/main_doc001_numeric.md`; `extraction/parts/main_doc001.md`.
- **Exact source locations:** DOC-001 `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=1` (abstract), `#page=3` (Figure 1), and `#page=4` (Results/analysis population).
- **Printed inputs:** Figure 1 prints 551 assessed, 390 excluded, and **161 randomized**. Its exclusion components are 161 + 100 + 50 + 38 + 22 + 12 + 7 = 390, so 551 - 390 = 161. The abstract prints **160 randomized**, and p. 4 prints that all **160** received allocated therapy, 80 per arm. Figure 1 also prints 80 assigned/received treatment per arm and a footnote that one participant withdrew after randomization before therapy.
- **Direct observation:** The flow diagram’s randomized count is 161, while the abstract and trial-arm totals describe 160 randomized participants.
- **Rule and calculation:** A randomization total should equal the two randomized arm totals when the same trial population is labelled “randomized”: 80 + 80 = 160, not 161. The Figure 1 upstream flow also independently yields 161 (551 - 390).
- **Tolerance:** Counts are exact integers; tolerance 0. This is not a rounding issue.
- **Inference and alternative:** The figure footnote may mean that 161 underwent randomization but one was excluded from the treated/full-analysis population before receiving therapy; if so, the 160 text may use “randomized” informally for a post-randomization treated set. The source does not explicitly reconcile those two denominators.
- **Quality-control relevance:** A data extractor could select 160 or 161 as the randomized denominator, altering retention, flow, and intention-to-treat interpretation.
- **Exact human question:** Did 161 participants undergo randomization, with one excluded before treatment, and if so should the abstract/p. 4 replace or qualify “160 randomized” rather than use that count without distinction?

### Proposal 2 — Main Table 1 and Table 3 print different baseline digoxin NT-proBNP summaries

- **Mapped relationships and provenance:** N011 and N022; `relationships/parts/main_doc001_numeric.md`; `extraction/parts/main_doc001.md`.
- **Exact source locations:** DOC-001 `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=5` (Table 1), `#page=6` (narrative), and `#page=7` (Table 3).
- **Printed inputs:** Table 1 prints digoxin baseline NT-proBNP **1095 (IQR 715-1527) pg/mL**. The p. 6 narrative repeats **1095 (715-1527)**. Table 3 prints, for the same digoxin baseline NT-proBNP row, **1091 (710-1522) pg/mL**. Both tables identify baseline digoxin as n=80; Table 3 identifies its baseline comparison as n=80/80.
- **Direct observation:** The median and both IQR endpoints differ between two printed baseline summaries of the same named measure, arm, and baseline population.
- **Rule and calculation:** Identical descriptive summaries rounded to whole pg/mL must print identically. Differences are 1095 - 1091 = **4 pg/mL**, 715 - 710 = **5 pg/mL**, and 1527 - 1522 = **5 pg/mL**.
- **Tolerance:** Whole-number display tolerance is at most 0.5 pg/mL per independently rounded value; the observed differences exceed that tolerance. No separate baseline analysis set, assay, or transformation is printed for Table 3.
- **Inference and alternative:** Table 3 may use an unlabelled complete-case baseline subset, a revised data cut, or a transcription error. If a distinct subset was intended, its denominator/selection rule is missing from the displayed row.
- **Quality-control relevance:** The mismatch can propagate to baseline extraction and biomarker change interpretation.
- **Exact human question:** What denominator, data cut, or calculation rule accounts for Table 3’s 1091 (710-1522) rather than Table 1/narrative’s 1095 (715-1527), and should the source identify that distinction or correct one value?

### Proposal 3 — Main Table 1 and eTable 2 differ on baseline digoxin 12-lead ECG heart rate

- **Mapped relationships and provenance:** N012 and N3010; `relationships/parts/main_doc001_numeric.md`, `relationships/parts/support_doc004_doc005_numeric.md`; `extraction/parts/main_doc001.md`, `extraction/parts/support_doc004_doc005.md`.
- **Exact source locations:** DOC-001 `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=5` (Table 1); DOC-004 `joi200126supp3_prod_1607962892.5372.pdf#page=14` (eTable 2).
- **Printed inputs:** Main Table 1, digoxin baseline ECG heart rate: **100.1 (16.8) /min**. eTable 2, digoxin baseline 12-lead ECG: **100.3 (16.8) beats/min**, n=80. Both sources compare the same baseline digoxin arm and print n=80 for that arm.
- **Direct observation:** The printed baseline means differ by 0.2 beats/min while the displayed SD and arm size match.
- **Rule and calculation:** Identical means displayed to one decimal must have the same printed value: 100.3 - 100.1 = **0.2 beats/min**.
- **Tolerance:** A single underlying value rounded to one decimal cannot produce values 0.2 apart; maximum disagreement due only to rounding is <0.1 beats/min.
- **Inference and alternative:** An unlabelled analytic subset, different ECG processing/measurement definition, or transcription/revision could explain the difference. eTable 2 calls the measure “12-lead ECG,” whereas Table 1 calls it “ECG heart rate”; no differing method or subset is printed.
- **Quality-control relevance:** The baseline covariate appears in the trial’s reporting and could be copied inconsistently into structured evidence summaries.
- **Exact human question:** Are Table 1 and eTable 2 intended to report the same baseline 12-lead ECG measure for all 80 digoxin participants; if yes, which mean is correct, and if no, where is the differing definition or denominator stated?

### Proposal 4 — Main Table 1 and eTable 2 differ on baseline digoxin radial-pulse SD

- **Mapped relationships and provenance:** N012 and N3012; `relationships/parts/main_doc001_numeric.md`, `relationships/parts/support_doc004_doc005_numeric.md`; `extraction/parts/main_doc001.md`, `extraction/parts/support_doc004_doc005.md`.
- **Exact source locations:** DOC-001 `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=5` (Table 1); DOC-004 `joi200126supp3_prod_1607962892.5372.pdf#page=14` (eTable 2).
- **Printed inputs:** Main Table 1, digoxin radial pulse: **87.8 (12.1) /min**. eTable 2, digoxin baseline radial 30-second measure: **87.8 (12.0) beats/min**. The eTable prints baseline n=80; Table 1 is digoxin n=80.
- **Direct observation:** The mean agrees but the displayed SD differs by 0.1 beats/min for the same named baseline arm measure.
- **Rule and calculation:** Identical SDs rounded to one decimal must print identically. |12.1 - 12.0| = **0.1 beats/min**.
- **Tolerance:** A single value rounded to one decimal cannot round to both 12.0 and 12.1. Each display has half-unit rounding interval [11.95,12.05) and [12.05,12.15), which do not overlap under ordinary nearest-tenth rounding.
- **Inference and alternative:** A minor extraction/revision difference or unlabelled measurement/subset distinction may explain it. The eTable adds “30 sec,” but the main table does not state a conflicting interval and reports the same radial-pulse construct.
- **Quality-control relevance:** This is a repeated baseline value that could create incompatible covariate summaries.
- **Exact human question:** Was the baseline digoxin radial pulse calculated from the same 80 participants and same 30-second assessment in both tables; if so, should the SD be 12.0 or 12.1?

### Proposal 5 — Main Table 1 and eTable 2 differ on baseline digoxin apex heart-rate mean

- **Mapped relationships and provenance:** N012 and N3011; `relationships/parts/main_doc001_numeric.md`, `relationships/parts/support_doc004_doc005_numeric.md`; `extraction/parts/main_doc001.md`, `extraction/parts/support_doc004_doc005.md`.
- **Exact source locations:** DOC-001 `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=5` (Table 1); DOC-004 `joi200126supp3_prod_1607962892.5372.pdf#page=14` (eTable 2).
- **Printed inputs:** Main Table 1, digoxin apex heart rate: **98.2 (15.1) /min**. eTable 2, digoxin baseline apex 30-second measure: **98.3 (15.1) beats/min**. Each table identifies the baseline digoxin group as n=80.
- **Direct observation:** The printed baseline mean differs by 0.1 beats/min, while the SD and arm size agree.
- **Rule and calculation:** Identical means displayed to one decimal must print identically: 98.3 - 98.2 = **0.1 beats/min**.
- **Tolerance:** Ordinary nearest-tenth rounding has nonoverlapping intervals [98.15,98.25) and [98.25,98.35); thus the difference cannot arise from one common unrounded mean. There is no stated alternative measurement method beyond eTable 2’s “30 sec.”
- **Inference and alternative:** The values may reflect an unlabelled subset, a transcription/revision difference, or different time-observation conventions. No such difference is shown in the printed table headers.
- **Quality-control relevance:** It creates a fourth nonidentical baseline descriptive value across article and supplement tables apparently describing the same trial arm.
- **Exact human question:** Are the Table 1 and eTable 2 apex values calculated from the same 80 baseline digoxin participants and same assessment; if yes, should the mean be 98.2 or 98.3?

### Proposal 6 — Protocol calls the primary endpoint both PCS and physical-functioning domain

- **Mapped relationships and provenance:** N1002; `relationships/parts/support_doc002_numeric.md`; `extraction/parts/support_doc002.md`.
- **Exact source locations:** DOC-002 `joi200126supp1_prod_1607962892.5372.pdf#page=14`, `#page=21`, `#page=22`, `#page=54`, and `#page=56`; matched result: DOC-001 `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=1` and `#page=6`.
- **Printed inputs:** DOC-002 pp. 14, 22, and 54 name the primary outcome **“SF-36 physical component summary score at six months.”** DOC-002 p. 21 calls the hypothesis measure the **“physical functioning domain,”** and p. 56 calls the primary outcome the continuous **“SF36 physical functioning domain score”** at six months. DOC-001 reports the trial primary outcome as the **SF-36 PCS**, with normalized 6-month values 31.9 versus 29.7 and adjusted difference 1.4.
- **Direct observation:** PCS and the physical-functioning domain are separate SF-36 scales, with different values and transformations; the protocol gives both labels to what it otherwise presents as the primary six-month endpoint.
- **Rule and calculation:** A primary endpoint must retain a single measure label. No arithmetic conversion can equate a PCS with a physical-functioning domain score; they have separate scale definitions in the supplied SAP.
- **Tolerance:** Not applicable: this is a categorical measure-label identity check, with no rounding tolerance.
- **Inference and alternative:** The p. 21/p. 56 language may be a drafting carryover or shorthand rather than a statement that the physical-functioning domain was analysed as primary. Repeated PCS wording and the published result support PCS, but the discrepant protocol wording remains unreconciled.
- **Quality-control relevance:** Endpoint extraction could incorrectly classify the primary outcome and conflate a domain with a component summary.
- **Exact human question:** Was the intended primary outcome the PCS throughout, and should the protocol’s “physical functioning domain” statements be corrected or explicitly described as erroneous drafting?

### Proposal 7 — Protocol labels the planned biomarker outcome BNP while specifying an NT-proBNP assay

- **Mapped relationships and provenance:** N1005 and N1016; `relationships/parts/support_doc002_numeric.md`; `extraction/parts/support_doc002.md`.
- **Exact source locations:** DOC-002 `joi200126supp1_prod_1607962892.5372.pdf#page=14`, `#page=15`, `#page=22`, `#page=41`, and `#page=54`; matched result: DOC-001 `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=6` and `#page=7`.
- **Printed inputs:** DOC-002 trial-summary/outcome pages call the outcome **change in BNP**. DOC-002 assay text identifies **NT-proBNP**, with stated range 5-35,000 pg/mL (0.6-4,130 pmol/L). DOC-001 reports **NT-proBNP** medians and geometric-mean ratios.
- **Direct observation:** BNP and NT-proBNP are differently named analytes in the protocol, while the assay description and reported results identify NT-proBNP.
- **Rule and calculation:** An analyte label should agree with the assay and matched reported measure. This is a label identity check, not a numeric conversion; the supplied sources do not give a formula that converts BNP concentration to NT-proBNP concentration.
- **Tolerance:** Not applicable.
- **Inference and alternative:** “BNP” may have been used as an informal umbrella abbreviation, not a claim that BNP itself was assayed. The distinct assay description and result terminology make that abbreviation potentially misleading rather than conclusively erroneous.
- **Quality-control relevance:** Biomarker meta-analysis/data extraction can treat BNP and NT-proBNP as noninterchangeable measures.
- **Exact human question:** Did “BNP” in the planned-outcome text intentionally mean NT-proBNP, and should every outcome label be standardized to the assay actually used?

### Proposal 8 — SAP AFEQT template calls its scale a visual-analogue score

- **Mapped relationships and provenance:** N2013; `relationships/parts/support_doc003_numeric.md`; `extraction/parts/support_doc003.md`.
- **Exact source locations:** DOC-003 `joi200126supp2_prod_1607962892.5372.pdf#page=17`, `#page=19`, and `#page=36`.
- **Printed inputs:** pp. 17 and 19 define **AFEQT overall score**, excluding the final two questions, from 0 (complete disability) to 100 (no disability). The AFEQT presentation-template footnote on p. 36 calls the 0-100 range a **“visual analogue score.”**
- **Direct observation:** The p. 36 footnote gives a visual-analogue label to an AFEQT score, despite the SAP separately defining EQ-5D VAS as the visual-analogue measure.
- **Rule and calculation:** AFEQT score and EQ-5D VAS are distinct labelled measures even though both use a 0-100 range; equality of range does not establish identity.
- **Tolerance:** Not applicable.
- **Inference and alternative:** This may be a template-footnote copy error and no completed SAP table supplies an affected numerical result.
- **Quality-control relevance:** A reader or extractor may misidentify the AFEQT outcome as a VAS, despite distinct instrument meaning.
- **Exact human question:** Does the p. 36 AFEQT footnote intend “AFEQT overall score” rather than “visual analogue score,” and should the template label be corrected?

### Proposal 9 — SAP gives incompatible direction statements for E/e-prime

- **Mapped relationships and provenance:** N2021; `relationships/parts/support_doc003_numeric.md`; `extraction/parts/support_doc003.md`.
- **Exact source locations:** DOC-003 `joi200126supp2_prod_1607962892.5372.pdf#page=20` and `#page=37`.
- **Printed inputs:** p. 20 states **E/e-prime is a ratio and lower is better**. The E/e-prime presentation-template wording on p. 37 says **higher values/positive difference favour Digoxin**.
- **Direct observation:** The source assigns opposite clinical/favourable directions to the same E/e-prime measure.
- **Rule and calculation:** For a fixed signed contrast (Digoxin minus Bisoprolol), a positive difference cannot simultaneously mean higher E/e-prime and be favourable if lower E/e-prime is better. This is a sign/direction identity contradiction, not a precision issue.
- **Tolerance:** Not applicable.
- **Inference and alternative:** The p. 37 sentence may be generic wording copied from higher-is-better continuous outcomes. The completed main article reports a negative adjusted difference (-0.1) but does not repeat the p. 37 favourable-direction sentence.
- **Quality-control relevance:** The inconsistency can reverse a reader’s interpretation of an E/e-prime effect.
- **Exact human question:** Which direction convention was intended for E/e-prime in the SAP table, and should p. 37 state that lower/negative Digoxin-minus-Bisoprolol values are favourable?

### Proposal 10 — SAP NT-proBNP template has a six-month heading but includes 12-month rows and switches units

- **Mapped relationships and provenance:** N2015 and N2027; `relationships/parts/support_doc003_numeric.md`; `extraction/parts/support_doc003.md`.
- **Exact source locations:** DOC-003 `joi200126supp2_prod_1607962892.5372.pdf#page=17`, `#page=21`, `#page=30`, and `#page=40`.
- **Printed inputs:** The p. 40 NT-proBNP outcome-table heading says **“at 6 months”** but the same blank table contains Baseline, 6-month, and **12-month** rows. p. 30 baseline template labels NTproBNP **pg/mL**; p. 40 labels it **ng/L**. pp. 17 and 21 describe baseline, 6- and 12-month analysis using log transformation/geometric-mean ratios.
- **Direct observation:** The template’s time heading excludes a displayed 12-month row. It also changes the concentration unit spelling from pg/mL to ng/L without explanation.
- **Rule and calculation:** A heading should cover every printed time row. For mass concentration, 1 pg/mL = 1 ng/L, so the unit texts are numerically equivalent but should not suggest a changed numeric scale; no multiplier should be applied. The time contradiction is independent of the equivalent unit conversion.
- **Tolerance:** No time-label tolerance. Unit conversion tolerance is exact (factor 1).
- **Inference and alternative:** The p. 40 heading may be a leftover template title, and the two units may be intentionally equivalent SI expressions. No filled SAP values create a demonstrated numerical conversion error.
- **Quality-control relevance:** A data extractor may omit the 12-month planned result or mistakenly apply a 1000-fold conversion where none is needed.
- **Exact human question:** Should the p. 40 heading say “at 6 and 12 months” (or equivalent), and should the SAP standardize NT-proBNP units or explicitly note pg/mL equals ng/L?

### Proposal 11 — SAP EHRA example uses an undefined “3a” category

- **Mapped relationships and provenance:** N2017; `relationships/parts/support_doc003_numeric.md`; `extraction/parts/support_doc003.md`.
- **Exact source locations:** DOC-003 `joi200126supp2_prod_1607962892.5372.pdf#page=18`.
- **Printed inputs:** The SAP defines modified EHRA categories **1, 2a, 2b, 3, and 4**. Its binary-improvement explanation then gives an example with baseline **“3a”** moving to 2a.
- **Direct observation:** “3a” is not one of the source’s defined five ordered categories.
- **Rule and calculation:** An illustrative category used to define the two-class binary-improvement rule must belong to the explicitly listed category set. Set membership check: 3a is not in {1, 2a, 2b, 3, 4}.
- **Tolerance:** Not applicable.
- **Inference and alternative:** “3a” may be a typographic slip for class 3; no completed source result is printed with a 3a category.
- **Quality-control relevance:** The example can confuse implementation or interpretation of the threshold used to produce the binary EHRA outcome.
- **Exact human question:** Was “3a” intended to be class 3, and should the binary-improvement example be corrected to a defined EHRA category?

### Proposal 12 — SAP ambulatory-HR timing text conflicts with its template placement

- **Mapped relationships and provenance:** N2022; `relationships/parts/support_doc003_numeric.md`; `extraction/parts/support_doc003.md`.
- **Exact source locations:** DOC-003 `joi200126supp2_prod_1607962892.5372.pdf#page=20` and `#page=38`; matched result: DOC-004 `joi200126supp3_prod_1607962892.5372.pdf#page=9`.
- **Printed inputs:** DOC-003 p. 20 says 24-hour ambulatory HR is **measured only once** and has **no baseline score to adjust**. Its p. 38 blank presentation template places the ambulatory-HR row under **“Baseline.”** DOC-004 p. 9 labels the reported 24-hour HR as **end uptitration**, with 79 +/-11 versus 74 +/-11 beats/min.
- **Direct observation:** The SAP describes a non-baseline one-time measure but locates its template row under baseline; the results supplement calls the one-time measurement end uptitration.
- **Rule and calculation:** A measure stated to have no baseline score should not be labelled or placed as a baseline value. This is a timepoint label identity check, with no arithmetic tolerance.
- **Inference and alternative:** The template layout may use “Baseline” as a column anchor for all outcome rows rather than asserting baseline ambulatory monitoring. The source does not explain that placement.
- **Quality-control relevance:** Misplacing the timing can cause a one-time post-titration outcome to be analysed or extracted as a baseline covariate.
- **Exact human question:** Was the p. 38 ambulatory-HR row intended to be labelled “end uptitration” (or another non-baseline visit), and should the template be amended to prevent a baseline interpretation?

### Proposal 13 — Results-supplement HR table calls higher HR “better quality of life”

- **Mapped relationships and provenance:** N3010-N3015; `relationships/parts/support_doc004_doc005_numeric.md`; `extraction/parts/support_doc004_doc005.md`.
- **Exact source locations:** DOC-004 `joi200126supp3_prod_1607962892.5372.pdf#page=14` (eTable 2 footnote a); supporting outcome definitions: DOC-001 `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=4` and `#page=6`.
- **Printed inputs:** eTable 2 reports 12-lead ECG, apex, radial, pulse-deficit, and post-walk heart-rate outcomes in **beats/min** and adjusted Digoxin-minus-beta-blocker differences. Its footnote says **“higher values represent better quality of life in the digoxin arm.”** DOC-001 identifies these as heart-rate outcomes and separately defines quality-of-life scales (SF-36, EQ-5D, AFEQT).
- **Direct observation:** A heart-rate table uses an interpretation sentence explicitly about quality of life, a different outcome construct.
- **Rule and calculation:** Measure labels must correspond to the quantities tabulated. Beats/min is not a QoL scale, and no supplied rule defines higher heart rate as higher QoL. This is a measure/label mismatch, not an assertion that any HR direction is clinically wrong.
- **Tolerance:** Not applicable.
- **Inference and alternative:** The sentence may be a copied generic footnote from eTables 3-4, where QoL values are tabulated. It might have intended only to state the contrast direction (Digoxin minus beta-blocker).
- **Quality-control relevance:** The footnote can cause an extractor or reader to interpret an HR difference as a QoL outcome or assign an unsupported favourable direction.
- **Exact human question:** Should eTable 2 remove the QoL interpretation sentence or replace it with a heart-rate-specific contrast/direction statement?

## Checked noncandidate outcomes and limitations

- **Arithmetic, totals, and percentages:** DOC-001 Figure 1 exclusion components total 390; arm category totals in Table 1 reconcile to n=80 subject to its stated rounding footnote; 76+74=150 and 73+72=145; 8+12=20 secondary outcomes. DOC-004 eTable 1 percentages reconcile to attendance denominators (for example, 73/76=96.1%, 58/72=80.6%, and 65/72=90.3%). eTable 5 patient and event totals reconcile, including 29+142=171 events and 20+51=71 patients with at least one event. Multiple events per patient explain event count exceeding patient count.
- **Population and missingness:** The 150 six-month and 145 12-month analysis counts reconcile to Figure 1 arm counts; differing randomized, attended, and safety denominators are otherwise expressly labelled. No further concrete sample-unit issue was identified.
- **Rate/count and units:** Treatment-related AEs are explicitly event counts with an incidence-rate ratio, not patient percentages. Table 4 separates events from patients. EQ-5D index and VAS, ratios versus odds ratios, and normalized versus unnormalized PCS are labelled as distinct measures. The SAP’s pg/mL versus ng/L notation is numerically factor 1, not a demonstrated conversion error.
- **Repeated values and rounding:** DOC-004 eFigure 4 prints P=.013/.049/.038 while eTable 3 prints .01/.05/.04 for matched 12-month vitality/global-health/EQ-5D VAS effects; these are compatible with additional versus two-decimal display precision and are not proposed. Main/supplement adjusted estimates and Figure 5 NYHA values are compatible with printed rounding. The Table 1/eTable 2 baseline differences identified above are separated because their common one-decimal precision cannot produce the stated different values from one underlying value.
- **Blank planned templates:** DOC-003 appendix templates contain placeholders rather than observed trial results. The label/time/direction conflicts above are retained because the source itself gives incompatible definitions, but no candidate was based on a dash, blank `N=`, or absent numerical value.
- **Limitations:** This numeric review did not rerun statistical interval/P-value compatibility beyond arithmetic and label/scale implications; that work belongs to the designated statistical pass. Some alternative explanations (data cut, subset, or drafting carryover) are not resolvable from supplied text and are therefore preserved as exact human questions.
