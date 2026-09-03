# Numeric Consistency Check

## Scope and method

Independent numeric review of canonical relationships `N001`--`N033` and their mapper observations. I used the direct PDFs as authority for every possible issue: DOC-001 PDF p. 6 (printed article p. 403), DOC-002 PDF p. 118 (SAP p. 8), and DOC-003 PDF pp. 1 and 15--19. Native/layout text and the evidence maps were used as locators only. Checks covered arithmetic, totals, mutually exclusive subgroup sums, numerator/denominator/percentage agreement at printed precision, missingness and population identity, units/scales, repeated matched values, rates versus counts, and prospective-version matching. `DOC-002` entries are prospective planning definitions unless noted otherwise.

**Result:** 33 of 33 N relationships received `NUMERIC_CHECK_COMPLETE`. Three distinct source-grounded candidate observations are emitted below; no stable candidate IDs, severity, validity, or disposition is assigned.

## Relationship-level completion record

| Relationship | `NUMERIC_CHECK_COMPLETE` result | Checks and result |
|---|---|---|
| N001 | No candidate | `8258 + 8242 = 16,500`; 97-site and allocation values agree across matched observed sources. |
| N002 | No candidate | Flow: `52,747-3,514=49,233`; `49,233-10,754=38,479`; `38,479-21,979=16,500`. Printed component totals reconcile. |
| N003 | No candidate | Removed `28+38=66`; primary analysis `8230+8204=16,434`; known outcome `8211+8183=16,394`; difference is the printed 40 unlinked outcomes. |
| N004 | No candidate | Observed target/range matches final protocol/SAP; earlier 90%-93% wording is explicitly versioned and is not a same-version contradiction. |
| N005 | No candidate | Eligibility/exclusion definitions are prospective and internally compatible with the observed flow labels; no numeric conflict found. |
| N006 | No candidate | Versioned planning scenarios are distinct. Later allowance diagnostic: `15,444/(1-.06)=16,429.8`, compatible with planned target 16,500; not an observed-result comparison. |
| N007 | No candidate | Interim sizes and Peto-Haybittle threshold are consistently labelled prospective; no incompatible same-plan value found. |
| N008 | No candidate | `2,500/16,500=15.15%`, compatible with printed approximately 15%; first-10/random components are approximate planned counts. |
| N009 | No candidate | `1252+1237=2,489`; collection strata `952+1,537+13,945=16,434`. Matched main/supplement populations agree. |
| N010 | No candidate | Female counts total `2803+2849=5,652`; each printed percentage rounds from its stated linkage denominator (38.19% and 38.16% to 38.2%). |
| N011 | No candidate | Checked displayed baseline category rows: sex, ethnicity, BMI, diagnosis, SpO2, and PaO2:FIO2 subgroup counts reconcile within their stated, variable-specific denominators. |
| N012 | No candidate | Scale rule is arithmetically coherent: additional oxygen above room air is 0.79 at FIO2 1.00 and 0.395 at 0.605; one hour versus two hours gives equal 100%-equivalent exposure. |
| N013 | No candidate | `20.3-28.7=-8.4` hours; `-8.4/28.7=-29.27%`, compatible with -29.3% and abstract’s rounded 29% lower. Values/units match DOC-003 eTable 5. |
| N014 | Candidate observation emitted | Values match DOC-003 eTable 5, but direct DOC-001 prose places `mm Hg` after the usual-group SpO2 value; see Observation 1. |
| N015 | No candidate | Exposure times retain hour units and matched eTable 5 values; categories are not mutually exclusive time partitions, so no invalid sum was assumed. |
| N016 | No candidate | `526/1252=42.01%`, compatible with 42.1% at displayed precision; nonadherence reasons `857+413+127+265+609=2,271`. |
| N017 | No candidate | Figure 2 denominators decline over follow-up as expected and match the repeated collection-subset arm baselines; no duplicated-but-different count identified. |
| N018 | No candidate | `2908/8211=35.41%` and `2858/8183=34.93%`, both compatible with 35.4%/34.9%; crude difference rounds to 0.5 percentage points. |
| N019 | No candidate | ICU counts: `5211+2122=7333`, `5290+2158=7448`; hospital counts: `4791+2532=7323`, `4906+2528=7434`. Distinct duration populations are labelled. |
| N020 | No candidate | DAWOS death=-1 scale is explicitly defined. Survivor count plus 30-day deaths equals the relevant 30-day mortality denominator in each arm (`4933+2435=7368`, `5054+2427=7481`); the DAWOS available denominators are separately printed. |
| N021 | No candidate | Figure 3 diagnosis and COVID subgroup event counts/denominators each sum to the primary-outcome totals. Ethnicity is a labelled outcome-available subset, not the full primary population. |
| N022 | No candidate | Post-hoc data-collection subgroup counts and percentages are checked against stated denominators; first-10 comparator population is distinct and labelled. |
| N023 | No candidate | One-year at-risk/event rows, the 66 removals, and 342 undated-death censoring statement use explicitly different follow-up/status quantities; no false total comparison applied. |
| N024 | No candidate | `1176/16,434=7.16%`, compatible with 7.2%; `40/16,434=0.24%`, compatible with 0.2%; 13,052 is consistently labelled as reached one year. |
| N025 | No candidate | SAE reports are patients with events, not event incidence rates; `58/8230=0.705%` and `29/8204=0.354%` are compatible with 0.7%/0.4%. |
| N026 | No candidate | Direct DOC-003 eTable 1 site rows total 16,500 and enumerate 97 sites; no row/total mismatch found. |
| N027 | No candidate | Trial 16,500 and CMP 207,857 are separately labelled populations; associated demographic percentages use their displayed denominators. |
| N028 | No candidate | Outcome and DAWOS/censoring definitions distinguish time point and measure; no same-definition numeric conflict across versions found. |
| N029 | No candidate | Economic quantities are prospective definitions, retaining their 90-day/lifetime and GBP20,000-per-QALY labels; no observed-result conflict. |
| N030 | No candidate | Pilot traffic-light intervals are contiguous at stated boundary conventions and explicitly prospective; no arithmetic contradiction found. |
| N031 | No candidate | Historical values are contextual/cited rather than UK-ROX results; no cross-population comparison was treated as a candidate. |
| N032 | Candidate observation emitted | Direct DOC-003 contents-page eTable 1--4 titles do not identify the actual same-numbered eTables on pp. 15--19; see Observation 2. |
| N033 | Candidate observation emitted | Direct SAP p. 8 contains a broken internal cross-reference following numeric adherence/separation definitions; see Observation 3. |

## Candidate observations requiring human adjudication

### Observation 1 — Unit carryover in the DOC-001 arterial-oxygenation sentence

- **Category:** Measure, label, or scale inconsistency.
- **Exact source location:** DOC-001, `jama_martin_2025_oi_250042_1753377747.91025.pdf`, PDF p. 6 (printed article p. 403), Oxygen Exposure paragraph; matched comparator: DOC-003, `joi250042supp2_prod_1753377747.93025.pdf`, PDF p. 21, eTable 5.
- **Direct observation:** DOC-001 prints: “...median SpO2 of `93.3% (2.8%)` and the median PaO2 of `71.5 (13.9) mm Hg` compared with `95.1% (2.4%) mm Hg` and `79.5 (17.9) mm Hg`, respectively....” DOC-003 eTable 5 separately labels SpO2 as percent and PaO2 as mm Hg and prints the same values (93.3/95.1% and 71.5/79.5 mm Hg).
- **Rule and calculation:** Under the sentence’s explicit “respectively” pairing, each SpO2 summary should carry percent only and each PaO2 summary should carry mm Hg only. The usual-arm first value has both `%` and trailing `mm Hg`; its parallel conservative-arm SpO2 summary has percent only. This is a direct unit-string mismatch, not a reconstructed clinical measurement.
- **Tolerance:** None for a unit label; numeric rounding does not explain an additional incompatible unit.
- **Direct observation versus inference:** Directly observed is the printed `95.1% (2.4%) mm Hg` string. A copy-edit carryover from the subsequent PaO2 value is an inference, not established by the package.
- **Source-grounded alternatives:** The trailing `mm Hg` could be read as visually associating only with the next PaO2 phrase despite its grammatical placement; eTable 5 supplies the unambiguous paired units.
- **Quality-control relevance:** A data extractor could transcribe the usual-arm SpO2 measure with an erroneous pressure unit or incorrectly treat the narrative sentence as ambiguous.
- **Exact human question:** Does the source PDF’s `mm Hg` after `95.1% (2.4%)` constitute an unintended unit carryover that should be removed or repositioned to apply only to PaO2?

### Observation 2 — DOC-003 contents-page eTable titles conflict with actual eTable identities

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** DOC-003, `joi250042supp2_prod_1753377747.93025.pdf`, PDF p. 1 contents and PDF pp. 15--19 actual eTables 1--4.
- **Direct observation:** Contents page labels eTable 1 “Results of quality assessment per study,” eTable 2 “Diagnostic performance of serological tests – test combinations,” eTable 3 “Patients randomized by site,” and eTable 4 “Additional patient characteristics.” Actual eTable 1 on PDF p. 15 is “Patients randomized by site”; actual eTable 2 on p. 17 is “Additional patient characteristics”; actual eTable 3 on p. 18 is “Representativeness of patients recruited to the UK-ROX trial”; and actual eTable 4 on p. 19 is “Patient baseline characteristics by data collection group.”
- **Rule and calculation:** A contents entry’s number and title should identify the same-numbered table in the same PDF. Four observed mismatches share the same faulty contents list and the same document-navigation rule, so they are retained as one distinct observation rather than four candidate records.
- **Tolerance:** None; these are categorical document labels, not rounded quantities.
- **Direct observation versus inference:** The conflicting titles are directly observed. Whether they arose from an uncorrected template is an inference.
- **Source-grounded alternatives:** The first two contents titles might have been retained from another supplement template, while the later entries may be shifted/replaced rather than intentionally referring to the actual eTables.
- **Quality-control relevance:** A reviewer or evidence extractor using the contents page could open or cite an incorrect table and misattribute numeric data.
- **Exact human question:** Is DOC-003 PDF p. 1 an uncorrected contents/template list that should be corrected to the actual eTable 1--4 titles and numbering?

### Observation 3 — Broken SAP internal reference after quantitative separation/adherence definitions

- **Category:** Measure, label, or scale inconsistency.
- **Exact source location:** DOC-002, `joi250042supp1_prod_1753377747.92525.pdf`, PDF p. 118 (SAP p. 8), immediately after Table 1 and the separation/adherence definition.
- **Direct observation:** The source prints: “See Section 3.2 and `Error! Reference source not found.` for further details about assessment of separation and treatment adherence.” This follows stated numeric traffic-light thresholds and the definition of treatment deviation including 22%/23% FIO2 handling.
- **Rule and calculation:** An internal reference intended to supply “further details” must resolve to an identifiable source section. The printed error text supplies no target; this is a direct referential failure, not an arithmetic inference.
- **Tolerance:** None; a missing reference target cannot be reconciled by numeric rounding.
- **Direct observation versus inference:** The unresolved reference string is directly observed. The identity of the intended missing section is not available in the supplied source and is not inferred here.
- **Source-grounded alternatives:** “Section 3.2” may itself contain part of the intended detail, but the additional missing target prevents confirmation that it is complete.
- **Quality-control relevance:** Readers applying or extracting the progression/adherence thresholds may be unable to locate the stated fuller definition, risking inconsistent interpretation of those quantitative rules.
- **Exact human question:** What exact section or appendix was intended by the broken internal reference, and does its absence leave any Table 1 separation/adherence quantity insufficiently defined?

## Limitations

- DOC-002 native text is glyph-mapped; direct rendered/PDF confirmation was used for the one possible issue in this review. Its planning material was not treated as an observed-result comparator unless version and definition matched.
- Graph-only eFigure ordinates and bin heights were not digitized as exact numbers. No candidate was inferred from values that the PDFs do not print.
- This artifact reviews the numeric inventory. Inferential compatibility and display-zero P-value handling remain within the separately assigned statistical passes; no display-zero P value was registered here.
