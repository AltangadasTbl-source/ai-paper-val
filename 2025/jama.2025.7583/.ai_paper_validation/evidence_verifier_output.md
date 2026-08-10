# Evidence verifier output

- **Article package:** `jama.2025.7583`
- **Verification stage:** Single evidence-verification stage
- **Candidates received:** 4
- **Verification rounds used:** 1 per candidate
- **Authority:** Original supplied PDFs, visually re-opened at the cited PDF pages; retained checker evidence used only as an aid
- **External sources:** None
- **Excluded documents audited:** None
- **Disposition:** 2 Verified; 0 Uncertain; 2 Rejected

## Candidate 1 - Treatment-type rows exceed the shared denominator

- **Status:** Rejected
- **Proposed category:** Arithmetic inconsistency
- **Location:** DOC-001-MAIN, `jama_shotar_2025_oi_250033_1750956987.75881.pdf`, PDF p. 5, Table 1, `Treatment` section, standard-care column and footnote e.
- **Visible source values/statements:** `Trepanation burr hole craniostomy`: `146/163 (89.6)`; `Trephine craniostomy`: `18/163 (11.0)`. Footnote e says craniostomy procedures were performed either with a cranial drill or a skull trephine cylindrical saw. The same column also reports `Unilateral CSDH surgery 137/163 (84.0)` and `Bilateral CSDH surgery 26/163 (16.0)`.
- **Calculation:** 146 + 18 = 164, and 89.6% + 11.0% = 100.6%.
- **Logical basis for rejection:** The arithmetic is correct, but the claimed contradiction assumes the two rows are mutually exclusive at the patient level. Footnote e classifies individual craniostomy procedures/openings, not patients. Table 1 establishes that 26 standard-care patients had bilateral CSDH surgery, so a patient could have more than one procedure/opening and could potentially contribute to both technique rows. The supplied package does not state that the technique rows are mutually exclusive per patient. Therefore, a sum of 164 over 163 patients does not by itself establish an arithmetic error.
- **Human verification instruction:** If source case coding is available, determine whether one bilateral-surgery patient received one burr-hole and one trephine procedure. Do not call the published counts erroneous unless the technique categories were mutually exclusive per patient.

## Candidate 2 - Inclusion label applied to excluded patients

- **Status:** Verified
- **Category:** Presentation inconsistency
- **Locations:**
  - DOC-001-MAIN, `jama_shotar_2025_oi_250033_1750956987.75881.pdf`, PDF p. 4, Figure 1 footnote a.
  - DOC-004-RESULTS-SUPP, `joi250033supp4_prod_1750956987.77981.pdf`, PDF p. 8, eFigure 1 title and exclusion box.
- **Visible source statements:** Main Figure 1 footnote a says, `See eFigure 1 in Supplement 4 for reasons for excluding patients with an inclusion criterion...`. The supplement title says, `eFigure 1. Detailed list of reasons for excluding patients with an inclusion criterion`. The eFigure 1 box is headed `Excluded (n=317)` and lists `Patient refusal (n=101)`, `Other pre-specified non-inclusion criteria (n=164)`, `Other reasons (n=18)`, and `Unknown reasons (n=34)`.
- **Comparison/logical basis:** The title and cross-reference characterize the exclusion list using `with an inclusion criterion`, but the displayed list includes non-inclusion criteria and other exclusion reasons. The qualifier needed to make the label consistent (for example, `not meeting an inclusion criterion` or `with a non-inclusion criterion`) is visibly absent in both cited locations. This is a document-grounded labeling error; no external knowledge is required.
- **Human verification instruction:** Read the full Figure 1 footnote on main PDF p. 4 and the complete eFigure 1 title and four top-level exclusion categories on supplement PDF p. 8; confirm that no `not meeting` or `non-` qualifier appears before `inclusion criterion`.

## Candidate 3 - Full-analysis-set/imputation labels beside observed denominators

- **Status:** Rejected
- **Proposed category:** Presentation inconsistency
- **Locations:**
  - DOC-004-RESULTS-SUPP, `joi250033supp4_prod_1750956987.77981.pdf`, PDF p. 9, eFigure 2 primary-analysis row.
  - DOC-004-RESULTS-SUPP, same file, PDF p. 15, eTable 4, EMPROTECT primary-outcome cell.
  - Resolving context: DOC-001-MAIN, `jama_shotar_2025_oi_250033_1750956987.75881.pdf`, PDF p. 4, Figure 1 primary-analysis boxes; PDF p. 6, Table 2 primary row and footnotes a-c.
- **Visible source values/statements:** eFigure 2 labels the population `Full analysis set, multiple imputation` and displays `24/162` and `33/157`, with OR `0.64 (0.36 to 1.14)`, P `0.13`. eTable 4 displays `24/162 (14.8%)` and `33/157 (21.0%)`, followed by `ITT with imputation: OR, 0.64; 95% confidence interval, 0.36 to 1.14; p=0.13`. Main Figure 1 states that 171 patients per arm were included in the primary analysis, comprising 162 evaluable plus 9 imputed cases and 157 evaluable plus 14 imputed cases. Main Table 2 footnote a explicitly states, `Case numbers and percentages based on observed values before multiple imputation were reported`; footnotes b-c state that the treatment effect was estimated after imputation in the ITT/full analysis set.
- **Calculation:** 162 + 9 = 171 and 157 + 14 = 171. The displayed fractions are the observed descriptive values, while the OR/CI/P value are the post-imputation inferential result.
- **Logical basis for rejection:** The package expressly distinguishes observed case numbers/percentages from the multiply imputed effect analysis. Multiple imputation does not require the descriptive fractions to be rewritten as integer event counts over 171. The p. 9 and p. 15 displays repeat this resolved descriptive-versus-inferential pairing and do not contradict the main article.
- **Human verification instruction:** Read main Table 2 footnotes a-c together with eFigure 2 and the EMPROTECT eTable 4 cell. Confirm that `24/162` and `33/157` are observed descriptors and that the `full analysis set`/`ITT with imputation` label applies to the reported effect estimate.

## Candidate 4 - MAGIC-MT usual-care event count omitted

- **Status:** Verified
- **Category:** Presentation inconsistency
- **Location:** DOC-004-RESULTS-SUPP, `joi250033supp4_prod_1750956987.77981.pdf`, PDF p. 14, eTable 4, MAGIC-MT row, `Primary outcome` column.
- **Visible source statement:** `24 patients (6.7%) reached the primary outcome in the intervention group as compared to (9.9%) in the usual-care group (between-group difference, -3.3 percentage points; 95% confidence interval, -7.4 to 0.8; P = 0.10)`.
- **Comparison/logical basis:** No numeral appears before `(9.9%)`; the usual-care event count is absent from the comparative sentence. On the same page, the EMBOLISE row reports `8 patients (4.1%)` versus `23 patients (11.3%)`, and the STEM row reports `19 of 120 patients (16%)` versus `47 of 129 patients (36%)`. The omission makes the MAGIC-MT summary visibly incomplete and prevents direct verification of the control event count from the supplied table.
- **Human verification instruction:** Inspect the MAGIC-MT primary-outcome cell at native magnification and confirm that no control numerator precedes `(9.9%)`; compare with the two-arm count formatting in the EMBOLISE and STEM rows immediately above.

