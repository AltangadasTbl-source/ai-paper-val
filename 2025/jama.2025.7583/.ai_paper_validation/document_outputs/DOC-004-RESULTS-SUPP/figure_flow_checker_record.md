# Figure and flow checker record

- **Document:** DOC-004-RESULTS-SUPP, `joi250033supp4_prod_1750956987.77981.pdf`
- **Audited scope:** PDF pp. 1-15; visual priority pp. 8-15.
- **Comparison source:** DOC-001-MAIN PDF pp. 1-9 only.
- **Status:** Complete. Three local candidates retained; none is adjudicated.

## Retained candidates

### FF-01 - Exclusion-flow title and cross-reference use an inclusion label for excluded patients

- **Category:** Presentation inconsistency
- **Exact locations:** DOC-004-RESULTS-SUPP PDF p. 8, eFigure 1 title and exclusion box; DOC-001-MAIN PDF p. 4, Figure 1 footnote a; DOC-001-MAIN PDF p. 2, Methods, Patients.
- **Visible/source statements:** The eFigure title and main Figure 1 footnote say “reasons for excluding patients with an inclusion criterion.” The eFigure box instead lists `Patient refusal (n=101)`, `Other pre-specified non-inclusion criteria (n=164)`, `Other reasons (n=18)`, and `Unknown reasons (n=34)`. The main Methods separately defines eligibility and conditions under which patients “were not eligible for inclusion.”
- **Logic:** The title/cross-reference does not name a displayed exclusion category and uses an inclusion label where the figure and Methods describe exclusion or non-inclusion.
- **Verification instruction:** Compare the exact eligibility wording on main p. 2 with the title and four top-level exclusion categories on supplement p. 8 and footnote a on main p. 4; confirm no missing qualifier is present in the source.

### FF-02 - Full-analysis-set/imputation labels are paired with observed evaluable-case denominators

- **Category:** Presentation inconsistency
- **Exact locations:** DOC-004-RESULTS-SUPP PDF p. 9, eFigure 2 primary row; DOC-004-RESULTS-SUPP PDF p. 15, eTable 4 EMPROTECT row; DOC-001-MAIN PDF p. 4, Figure 1 primary-analysis boxes; DOC-001-MAIN PDF p. 6, Table 2 footnotes a-c.
- **Visible/source values:** eFigure 2 labels the primary population `Full analysis set, multiple imputation` but displays `24/162` and `33/157`. The eTable 4 outcome cell repeats these fractions and calls the analysis `ITT with imputation`. Main Figure 1 states that all `171` participants per arm were included, with `9` and `14` nonevaluable cases imputed; main Table 2 separately explains that `24/162` and `33/157` are observed pre-imputation counts.
- **Logic:** The fractions visibly use evaluable denominators, not the stated full/ITT imputed population. Unlike main Table 2, eFigure 2 and eTable 4 do not label those fractions as observed pre-imputation counts.
- **Verification instruction:** Inspect the eFigure 2 legend and eTable 4 notes for a definition of the displayed fractions. If none is present, retain this as a population-label/denominator presentation issue.

### FF-03 - MAGIC-MT comparative outcome omits the usual-care event count

- **Category:** Presentation inconsistency
- **Exact location:** DOC-004-RESULTS-SUPP PDF p. 14, eTable 4, MAGIC-MT row, `Primary outcome` column.
- **Visible/source statement:** The cell says `24 patients (6.7%)` reached the outcome in the intervention group “as compared to `(9.9%)` in the usual-care group,” followed by the between-group difference and CI. The control-arm numerator is absent; neighboring EMBOLISE and STEM rows give counts for both arms.
- **Logic:** The comparative sentence is visibly incomplete and prevents direct count verification for the usual-care arm from this table.
- **Verification instruction:** Inspect the MAGIC-MT primary-outcome cell at native magnification and confirm that no numeral precedes `(9.9%)`; compare the formatting with both-arm counts in the EMBOLISE and STEM rows.

## Rejected checks

- **eFigure 1 totals:** Top-level exclusions sum to `101+164+18+34=317`; the listed non-inclusion subcounts sum to `164`; the listed “other reasons” subcounts sum to `18`; `659-317=342`. Rejected.
- **eFigure 1 versus main Figure 1:** Assessed, excluded, randomized, and all four top-level exclusion-category counts match. Rejected.
- **eFigure 2 visible estimates:** The primary OR/CI/P (`0.64`, `0.36-1.14`, `.13`) and on-site sensitivity estimate (`0.61`, `0.35-1.06`, `.08`) match the explicitly referenced main Results text. Axis direction and null reference are coherent. Rejected.
- **eTables 1-3:** Center totals reconcile to `171`, `171`, and `342`; eTable 2 event-component arm totals and percentages match the main primary-event counts; eTable 3 major/minor totals and component rows match main Table 2 and its nearby text. Rejected.
- **eTable 4 EMPROTECT result values:** Apart from FF-02's labeling issue, the displayed observed event fractions and OR/CI/P agree with the main article. Rejected.
