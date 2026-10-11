# Cross-Source Consistency Review

## Scope, evidence boundary, and comparison method

This review independently checked every assigned mapped relationship: numeric/reporting `N001`–`N049` and `N200`–`N219`, plus inferential/statistical `S001`–`S038` and `S200`–`S214`. The source set was DOC-001 (main article), DOC-002 (protocol), DOC-003 (protocol-change log), DOC-004 (final SAP), DOC-005 (online supplement), and DOC-006 (data-sharing statement). Only the supplied PDFs and current-run native/layout text and rendered-page assets were used; preserved audit outputs were not used as evidence.

Before comparing printed items, this review required the same population/analysis set, time window, treatment contrast and reference group, outcome definition, model/effect measure, scale/unit, and display precision. A difference caused by a distinct analysis (for example, a time-to-event HR versus a cumulative-risk RR), a different population (ITT versus per protocol), or rounding was recorded as not comparable rather than treated as a discrepancy. `P = 0`/`P = .000` formatting was not observed as a standalone issue and would not qualify by itself in any event.

PDF links below resolve from this checker artifact.

## Complete relationship coverage

| Assigned IDs | Matched cross-source scope | Result |
|---|---|---|
| N001–N004; S001–S002 | Abstract, results, Table 3, and Figure 2: randomized/analyzed totals, primary PPC, and hypoxemia. | One CI-sign proposal for N004/S002; otherwise matches after precision and measure checks. |
| N005–N010; N200; N206; S003–S004 | Eligibility, allocation, flow, sample-size history, analysis population, alpha, and final-plan rules across main article/protocol/change log/SAP. | One ARISCAT threshold proposal (N005); versioned sample-size values and modified-ITT exclusions are appropriately non-identical. |
| N011–N021 | Table 1 characteristics, row denominators, units, categories, and footnote definitions. | No separate cross-location comparator with a conflicting matched result; complete no-applicable cross-source record. |
| N022–N033; S005–S019; N201–N202; N207–N211; N214 | Table 2, narrative, protocol/eMethods/eTables, and anesthesia time-series figures: intervention intensity, rescue sequence, intraoperative measures, counts, units, and displayed P values. | Matched items agree; no proposal. Protocol `IBW` and main/eMethods `predicted body weight` use the same printed sex-specific formula, so no measure conflict was established. |
| N034–N042; S020–S033; N204–N205; N212–N213 | Table 3 outcomes/definitions, SAP and eMethods, per-protocol table, sensitivity table, and time-to-event figures. | Matched main/supplement event rates agree. RR versus HR, ITT versus per-protocol, and `.48` versus `.484` are non-conflicting because their model/population/precision differ. |
| N043–N048; S034–S038 | Figure 2 subgroup results and main narrative/discussion statements. | All-patient primary RR agrees across Table 3/Figure 2/abstract; narrative event directions agree. Qualitative sensitivity wording has no same-scale numeric comparator. |
| N203 | Protocol Appendix i and DOC-005 eTable 1 ARISCAT ORs, CIs, beta coefficients, scores, and n=1624. | Exact matched-table agreement; no proposal. |
| N215–N217; S210–S213 | DOC-005 eFigures 2–10 versus Table 3 and definitions. | Same outcome rates agree where comparable; survival HRs are distinct time-to-event analyses and not inconsistent with Table 3 RRs. |
| N218; S214 | DOC-005 eFigure 11 mortality display, its narrative, main Table 3, and mortality definitions. | One internal outcome-label proposal; numerical mortality results otherwise match at displayed precision. |
| N049; N219 | Main-article reference/author pages and DOC-006 data-sharing statement. | COMPLETE no-applicable-result record. |
| S200–S205 | Protocol/change log/final SAP sample-size, interim-boundary, effect-measure, multiplicity, and planned-model relationships. | No conflict after matching document version and planned-versus-final status. |
| S206–S209 | DOC-005 ARISCAT, eTables 3–8, and matching main/protocol displays. | No cross-document mismatch found. eTable 8 column's unspecified effect-measure heading is a within-display label limitation, not a cross-source value conflict in this lane. |
| S214 | DOC-005 eFigure 11 mortality HR/CI/P and label. | Covered in the eFigure 11 proposal below. |

## Matched results with no qualifying difference

- **Primary PPC (N003/S001/S036):** The abstract, Table 3, Figure 2 all-patient line, and DOC-005 eFigure 8 consistently print 211/989 (21.3%) versus 233/987 (23.6%). The abstract/Table 3/Figure 2 RR is 0.93 (95% CI, 0.83–1.04); eFigure 8's HR 0.88 (0.73–1.06) is a separate time-to-event measure and is not a contradiction.
- **Hypoxemia rates and direction (N004/N040/N046/S030):** Apart from the abstract CI sign recorded below, the abstract and Table 3 both print 5.0% versus 13.6%, a −8.6 percentage-point difference, and P<.001; the narrative correctly says hypoxemia was less common with high PEEP.
- **Intervention and rescue definition (N002/N023–N024/N031/N201–N202):** Main article, protocol, eMethods, and eTable 2 agree on high PEEP 12 cm H2O with recruitment versus low PEEP 4 cm H2O without planned recruitment and on the group-specific rescue endpoints.
- **Analysis/population and outcome timing (N006–N010/N204/N206):** The final SAP's modified-ITT definition accords with the article's 1976 analyzed participants; the article separately reports the randomized total (2013) and per-protocol population (1829). Main/supplement distinguish 5-day mortality from in-hospital mortality.
- **Definitions and effect labels (N039–N042/S029–S033):** Hospital-free days is a day-90 mean-difference analysis, while 5-day mortality uses Cox HRs. These labels match the final SAP and the Table 3 footnotes. The mortality P values `.48` (Table 3) and `.484` (eFigure 11) agree at Table 3's two-decimal precision.
- **Supplement outcome figures (N215–N217/S211–S213):** eFigures 8–10 label PPC, severe PPC, and PEPC separately and print rates consistent with Table 3 (21.3/23.6, 11.7/13.6, and 16.9/15.2%, respectively).

## Distinct candidate proposals (no stable C IDs assigned)

### Proposal CS-01 — Hypoxemia confidence interval has an opposite upper-endpoint sign in the abstract

- **Category:** Cross-document numeric inconsistency; statistical reporting inconsistency.
- **Exact source locations:** [DOC-001 abstract, PDF p. 1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1); [DOC-001 Table 3, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9).
- **Printed values:** The abstract reports hypoxemia 5.0% versus 13.6%, difference −8.6% (95% CI, −11.1% to **6.1%**), P<.001. Table 3 prints the same event rates and difference but a 95% CI of −11.1% to **−6.1%**, with RR 0.51 (95% CI, 0.40–0.65).
- **Comparison logic:** Same ITT groups, same intraoperative hypoxemia outcome, same percentage-point difference, and same displayed P value. A confidence interval for a −8.6 percentage-point difference that extends to +6.1 would include the null and point in a direction opposite to the Table 3 interval; it is not a precision-only difference.
- **Supported alternatives:** The abstract upper endpoint may have lost a minus sign; Table 3 may instead be the erroneous location. The supplied package does not identify the authoritative typeset value.
- **Human verification steps:** Inspect the publisher proof/source file and analysis output for the hypoxemia absolute risk-difference CI; confirm whether the abstract endpoint should be −6.1% and align every reuse-facing abstract/metadata representation.
- **Duplicate key:** `DOC001|hypoxemia|ITT high-v-low|absolute-difference CI|abstract p1 vs Table3 p9`.

### Proposal CS-02 — Main-text ARISCAT eligibility threshold is printed as 18 of 26 or greater, unlike supplied protocol/eMethods threshold of 26 or greater

- **Category:** Cross-document numeric inconsistency; measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-001 Patients, PDF p. 2](../../../jama_bluth_2019_oi_190055_16092.pdf#page=2); [DOC-002 inclusion criteria, PDF p. 9](../../../joi190055supp1_prod_16092.pdf#page=9); [DOC-005 eMethods inclusion criteria, PDF p. 18](../../../joi190055supp4_prod_16092.pdf#page=18); [DOC-005 eTable 1, PDF p. 22](../../../joi190055supp4_prod_16092.pdf#page=22).
- **Printed values:** DOC-001 says intermediate-to-high risk was indicated by an ARISCAT “score **18 of 26 or greater**.” DOC-002 states ARISCAT score **≥26**; DOC-005 eMethods says ARISCAT **≥26** is intermediate-to-high risk, and eTable 1 identifies the score framework.
- **Comparison logic:** These locations describe the same trial's participant eligibility risk threshold, not different analysis populations or time points. `18 of 26 or greater` contains a numeric threshold incompatible with the unqualified ≥26 wording in the protocol/eMethods. The phrase could be a textual/reference-marker corruption, so its intended meaning cannot be resolved from the supplied sources alone.
- **Supported alternatives:** DOC-001 may have intended `score 18^ of 26 or greater`, where `18` is a citation superscript rather than an eligibility cutoff; alternatively, the printed main-text phrase may be a threshold error. The protocol and eMethods support ≥26 but do not establish the intended typography of DOC-001.
- **Human verification steps:** Examine the typeset PDF at high magnification and original manuscript/XML to determine whether `18` is citation 18; verify eligibility data/codebook threshold and correct any plain-text accessibility or indexing rendition if it encodes 18 as part of the threshold.
- **Duplicate key:** `ARISCAT|eligibility threshold|main p2 phrase vs protocol p9/eMethods p18|18-of-26 vs >=26`.

### Proposal CS-03 — eFigure 11 mortality narrative calls its displayed mortality rate postoperative extra-pulmonary complications

- **Category:** Measure, label, or scale inconsistency; cross-document numeric inconsistency.
- **Exact source locations:** [DOC-005 eFigure 11, PDF p. 41](../../../joi190055supp4_prod_16092.pdf#page=41); [DOC-005 eFigure 10, PDF p. 40](../../../joi190055supp4_prod_16092.pdf#page=40); [DOC-001 Table 3, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10); [DOC-005 eMethods outcome definitions, PDF pp. 20–21](../../../joi190055supp4_prod_16092.pdf#page=20).
- **Printed values:** eFigure 11 is headed “Probability of death in the first 5 postoperative days” and its parenthetical analysis says “hazard ratio for 5-day mortality, 1.67; 95% CI 0.40 to 6.97; P=0.484.” Its narrative immediately before those values calls 0.5% versus 0.3% “the rate of **postoperative extra-pulmonary complications**.” eFigure 10 is the separately headed PEPC display and correctly reports 16.9% versus 15.2% with HR 1.12. Table 3 separately prints 5-day death 5 (0.5%) versus 3 (0.3%), HR 1.67 (0.40–6.97), P=.48.
- **Comparison logic:** The figure heading, mortality HR label, Table 3 matched rates, and eMethods distinguish mortality from PEPC. Thus the eFigure 11 narrative label identifies a different defined outcome while retaining the mortality values; it is not a rate-versus-count or rounding difference.
- **Supported alternatives:** The sentence may have been copied from eFigure 10 without changing its outcome noun; the numerical mortality values and HR may be the intended eFigure 11 content. Supplied sources do not establish which text version is authoritative.
- **Human verification steps:** Compare eFigure 11 with the final figure proof/source, confirm the outcome noun associated with 0.5%/0.3% and HR 1.67, and correct any caption, figure narrative, or accessibility text that identifies those mortality data as PEPC.
- **Duplicate key:** `DOC005|eFigure11 p41|mortality 0.5-v-0.3 HR1.67|narrative PEPC label`.

## Limitations

The review is confined to supplied PDFs and their fresh extraction/rendering assets. It does not infer unreported model specifications or adjudicate which conflicting location is correct. DOC-006 contains no result-bearing quantitative content, and author/reference pages contain no matched trial result. No candidate ID, severity, validity judgment, or correction is assigned here; all three proposals require human adjudication.
