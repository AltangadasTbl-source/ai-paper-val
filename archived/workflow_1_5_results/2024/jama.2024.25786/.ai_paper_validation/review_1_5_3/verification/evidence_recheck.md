# Mechanical Evidence Recheck

## Scope and method

This artifact mechanically rechecks stable IDs C001, C002, C003, C004, C005, C006, C007, and C008 against the supplied direct PDFs. Reusable text and current mapping artifacts were used only as locators. The cited pages were extracted directly with `pdftotext -layout` and inspected in direct `pdftoppm` renderings. Supplement 2 PDF page 25 also received a targeted 600-dpi render, CPU Tesseract OCR, raw-text extraction, and bounding-box text extraction because the second slash in `135//750` is difficult to distinguish in a downsampled whole-page image. Those targeted derivatives are under `preprocessing/evidence_recheck/`. The direct PDFs remain the authority. This record makes no adjudicative disposition.

## C001 — Liberal walk-in transport percentage does not reconcile with 4/743

- **Location found:** [Supplement 2, eTable 2 — PDF p. 15](../../../joi240147supp2_prod_1738701765.29201.pdf#page=15), “Type of transport to the trauma center,” “Walk-in,” liberal oxygen group.
- **Source value/text matched:** The direct PDF prints `4/743 (5.3)` in the liberal-group cell. The section label prints `no./total no. (%)`.
- **Comparator matched:** The displayed `5.3` is the percentage paired in the same cell with numerator 4 and denominator 743. Adjacent liberal transport cells also use denominator 743 and the same notation.
- **Consistency rule applicable:** Yes. Under `no./total no. (%)`, the displayed percentage is compared with `100 × numerator / denominator`, rounded to the table's one-decimal display precision.
- **Calculation or logical comparison reproduced:** `100 × 4 / 743 = 0.538358008075%`, which is `0.5%` to one decimal, whereas the source prints `5.3%`.
- **Necessary inputs available:** The numerator, denominator, percentage, one-decimal precision, group, row label, and quantity format are printed on the cited page.
- **Exact missing inputs or definitions:** The package does not supply the underlying transport records, the table-program output, or a statement identifying which of the three printed fields is authoritative.
- **Source-grounded alternative interpretation:** The numerator, denominator, or percentage may be a transcription or typesetting value. No footnote on the page supplies an alternate denominator or percentage definition for the walk-in cell.
- **Direct observation:** The direct PDF visibly contains `4/743 (5.3)` and the `no./total no. (%)` label; the arithmetic above follows from those printed values.
- **Inferred explanation:** A production or transcription error is a possible explanation, but its mechanism and affected field cannot be determined from the supplied PDFs.
- **Exact remaining human question:** Which numerator, denominator, and percentage are authoritative for liberal-group walk-in transport in eTable 2?

## C002 — Liberal vascular-surgery percentage is nonzero with a printed zero numerator

- **Location found:** [Supplement 2, eTable 2 — PDF p. 15](../../../joi240147supp2_prod_1738701765.29201.pdf#page=15), “Surgery performed in the trauma resuscitation room,” “Vascular surgery,” liberal oxygen group.
- **Source value/text matched:** The direct PDF prints `0/747 (1.1)` in the liberal-group cell. The row itself is labelled `no./total no. (%)`.
- **Comparator matched:** The displayed `1.1` is the percentage paired in the same cell with numerator 0 and denominator 747.
- **Consistency rule applicable:** Yes. A zero numerator over a positive denominator gives zero percent under the printed count/total/percentage identity.
- **Calculation or logical comparison reproduced:** `100 × 0 / 747 = 0.0%`, whereas the source prints `1.1%`.
- **Necessary inputs available:** The numerator, denominator, percentage, one-decimal precision, group, row label, and quantity format are printed on the cited page.
- **Exact missing inputs or definitions:** The package does not supply the underlying surgery records, table-program output, or a statement identifying whether the printed numerator or percentage is authoritative.
- **Source-grounded alternative interpretation:** Either the numerator or percentage may be mistranscribed. No eTable 2 note defines an alternate numerator, denominator, or percentage rule for this row.
- **Direct observation:** The direct PDF visibly contains `0/747 (1.1)` under a count/total/percentage label, and zero divided by 747 is zero.
- **Inferred explanation:** A typographic zero, a carried-over percentage, or another production error is possible, but the supplied source does not establish a cause.
- **Exact remaining human question:** What numerator and percentage are authoritative for liberal-group vascular surgery in eTable 2?

## C003 — Matched all-patient adjusted confidence-interval upper limit differs between eTables 4 and 7

- **Location found:** [Supplement 2, eTable 4 — PDF p. 17](../../../joi240147supp2_prod_1738701765.29201.pdf#page=17), primary outcome, `Adjusted odds ratio (95% CI)`; [Supplement 2, eTable 7 — PDF p. 20](../../../joi240147supp2_prod_1738701765.29201.pdf#page=20), `All patients`, `Adjusted odds ratio (95% CI)`. Relevant model text appears in [Main article — PDF p. 5](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=5), Statistical Analysis; the continuation note on [Supplement 2 — PDF p. 21](../../../joi240147supp2_prod_1738701765.29201.pdf#page=21) describes the table generically as adjusted subgroup analyses but does not list a table-specific covariate formula.
- **Source value/text matched:** eTable 4 prints restrictive `118/733 (16.1)`, liberal `121/724 (16.7)`, and adjusted OR `0.98 (0.68 to 1.41)`. eTable 7 prints the same group counts and percentages for all patients and adjusted OR `0.98 (0.68 to 1.39)`.
- **Comparator matched:** The displayed population, 30-day primary composite, restrictive-versus-liberal contrast, event counts, denominators, effect label, point estimate, lower endpoint, and two-decimal precision match. The table-specific adjustment formulas are not explicitly printed in the two table notes, so exact model identity is not fully established by the cited rows alone.
- **Consistency rule applicable:** Conditionally. If both adjusted columns implement the same all-patient model, repeated presentations of the same estimate at the same precision should have the same confidence limits. If the models differ, the column labels or notes must provide the distinction needed to prevent a false same-result comparison.
- **Calculation or logical comparison reproduced:** The point estimates are both `0.98`, the lower limits are both `0.68`, and the upper limits are `1.41` versus `1.39`, an absolute displayed difference of `0.02`.
- **Necessary inputs available:** The outcome counts, denominators, population label, effect-measure label, confidence level, point estimates, endpoints, and display precision are available. Main-article methods define a stratification-adjusted model and an additional model adjusting for stratification variables, age, sex, ISS, and first available posttrauma Glasgow Coma Scale score, with site clustering and inverse-probability weighting described.
- **Exact missing inputs or definitions:** The package does not explicitly bind each table's `Adjusted odds ratio` column to an identical table-specific formula and implementation. It also lacks unrounded confidence limits, table-production code, the model matrix, covariance estimates, and row-level data needed to determine whether `1.41` and `1.39` arose from the same fitted model.
- **Source-grounded alternative interpretation:** The two adjusted columns may represent nonidentical covariate or subgroup-model implementations that are insufficiently distinguished in the table labels. If they implement the same additional model described on main-article PDF page 5, one displayed upper endpoint does not match the other.
- **Direct observation:** The direct PDFs print the same all-patient counts, adjusted point estimate, and lower limit, but different upper limits.
- **Inferred explanation:** Model nonidentity, differing implementation, rounding from different unrounded estimates, or a transcription/typesetting difference are possible explanations; none is established by the supplied tables.
- **Exact remaining human question:** Do the eTable 4 and eTable 7 all-patient adjusted rows use the identical fitted model and data handling, and, if so, what is the authoritative unrounded and displayed upper 95% confidence limit; if not, what exact model distinction should identify the rows?

## C004 — AIS less-than-3 subgroup percentage conflicts with its count and matched Figure 4

- **Location found:** [Main article, Figure 4 — PDF p. 8](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8), moderate or severe TBI, `AIS score <3`; [Supplement 2, eTable 7 — PDF p. 20](../../../joi240147supp2_prod_1738701765.29201.pdf#page=20), moderate or severe traumatic brain injury, `AIS < 3`.
- **Source value/text matched:** Figure 4 prints liberal `48/473 (10.1)`. eTable 7 prints liberal `48/473 (9.2)`.
- **Comparator matched:** Both locations print the same liberal-group numerator 48, denominator 473, AIS-less-than-3 subgroup, primary composite context, and one-decimal percentage format.
- **Consistency rule applicable:** Yes. The same count and denominator imply one percentage at a stated one-decimal precision, and repeated matched presentations should agree.
- **Calculation or logical comparison reproduced:** `100 × 48 / 473 = 10.147991543340%`, which is `10.1%` to one decimal. This matches Figure 4 and differs from eTable 7's `9.2%`.
- **Necessary inputs available:** Both printed occurrences, their subgroup and treatment-group labels, numerator, denominator, percentages, and display precision are available.
- **Exact missing inputs or definitions:** The package lacks the subgroup dataset, table-production code, and any note stating that eTable 7 used a denominator different from the printed 473.
- **Source-grounded alternative interpretation:** eTable 7 may contain a transcription or display value, or it may reflect an undisclosed analytic denominator that conflicts with the denominator printed in that cell. No table note supplies such a denominator.
- **Direct observation:** The matched direct-PDF cells print identical `48/473` values but percentages of `10.1` and `9.2`; the printed fraction yields 10.1% to one decimal.
- **Inferred explanation:** A table-production or transcription error is possible, but the supplied PDFs do not establish which production step or field was affected.
- **Exact remaining human question:** What numerator, denominator, and displayed percentage are authoritative for the liberal AIS-less-than-3 subgroup in Figure 4 and eTable 7?

## C005 — Known-lung-disease subgroup percentage conflicts with its count and matched Figure 4

- **Location found:** [Main article, Figure 4 — PDF p. 8](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8), known lung disease, `Yes`; [Supplement 2, eTable 7 — PDF p. 20](../../../joi240147supp2_prod_1738701765.29201.pdf#page=20), known lung disease, `Yes`.
- **Source value/text matched:** Figure 4 prints liberal `14/69 (20.3)`. eTable 7 prints liberal `14/69 (20.2)`.
- **Comparator matched:** Both locations print the same liberal-group numerator 14, denominator 69, known-lung-disease subgroup, primary composite context, and one-decimal percentage format.
- **Consistency rule applicable:** Yes. Under ordinary rounding to the displayed one-decimal precision, the same numerator and denominator should produce the same displayed percentage across matched locations.
- **Calculation or logical comparison reproduced:** `100 × 14 / 69 = 20.289855072464%`, which is `20.3%` to one decimal under nearest rounding. Figure 4 prints `20.3%`; eTable 7 prints `20.2%`.
- **Necessary inputs available:** Both printed occurrences, subgroup and treatment-group labels, numerator, denominator, percentages, and display precision are available.
- **Exact missing inputs or definitions:** The package lacks the subgroup dataset, unrounded table-program output, and an explicit publication-wide percentage-rounding rule.
- **Source-grounded alternative interpretation:** eTable 7 could reflect truncation rather than nearest rounding, while Figure 4 reflects nearest rounding, or one occurrence could be a transcription value. The supplied sources do not state that different rounding conventions apply.
- **Direct observation:** The direct PDFs print the same `14/69` with two different one-decimal percentages, and ordinary nearest rounding yields 20.3%.
- **Inferred explanation:** Differing production-time rounding or transcription is possible, but the supplied package does not establish the mechanism.
- **Exact remaining human question:** What percentage-rounding convention and displayed percentage are authoritative for the liberal known-lung-disease subgroup across Figure 4 and eTable 7?

## C006 — Postrandomization-exclusion total and group counts do not reconcile across eTable 10 and Figure 1

- **Location found:** [Supplement 2, eTable 10 — PDF p. 24](../../../joi240147supp2_prod_1738701765.29201.pdf#page=24), `Exclusion after randomization`; [Main article, Figure 1 — PDF p. 3](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=3), restrictive and liberal `Excluded after randomization` branches.
- **Source value/text matched:** eTable 10 prints row total `N=130`, restrictive `55/750 (45)`, and liberal `67/758 (55)`. Figure 1 prints 59 restrictive and 71 liberal exclusions after randomization. Within each Figure 1 branch, `4 Omitted according to Swiss law due to withdrawn consent` is printed.
- **Comparator matched:** The eTable note states that it gives detailed numbers on the postrandomization excluded patients from Figure 1. The row and Figure 1 therefore identify the same exclusion stage and treatment groups, while their group counts differ.
- **Consistency rule applicable:** Yes. Group counts presented as a partition of a stated total should sum to that total, and a table explicitly tied to the corresponding flow-diagram stage should reconcile or define a narrower population.
- **Calculation or logical comparison reproduced:** eTable group counts sum to `55 + 67 = 122`, leaving `130 - 122 = 8`. Figure 1 counts sum to `59 + 71 = 130`. The differences are `59 - 55 = 4` restrictive and `71 - 67 = 4` liberal. The eTable percentages correspond to the 122 classified table counts: `100 × 55 / 122 = 45.081967%` and `100 × 67 / 122 = 54.918033%`, which display as 45% and 55%.
- **Necessary inputs available:** The row total, group counts, percentages, group denominators, Figure 1 stage counts, eTable-to-Figure-1 note, and the two printed four-person Swiss-law categories are available.
- **Exact missing inputs or definitions:** eTable 10 does not state whether the eight Swiss-law consent-withdrawal omissions are excluded from its group cells while retained in `N=130`. The package lacks the table specification, analytic records, and an explicit definition of the numerator population and denominator/percentage basis for this row.
- **Source-grounded alternative interpretation:** The exact four-person difference in each group is compatible with eTable 10 omitting the four Swiss-law consent-withdrawal cases shown in each Figure 1 branch while retaining Figure 1's total of 130. This is a source-grounded inference, not an explicit table definition.
- **Direct observation:** The direct PDFs print 55 and 67 against `N=130`, while Figure 1 prints 59 and 71 and separately lists four Swiss-law omissions in each group.
- **Inferred explanation:** Intentional omission of the eight Swiss-law cases is a plausible mechanism, but the eTable does not say so and the supplied package does not establish its intended population definition.
- **Exact remaining human question:** Does eTable 10 intentionally exclude the four Swiss-law consent-withdrawal omissions in each group from its displayed group counts while retaining `N=130`, and what exact population and denominator definition should govern that row?

## C007 — Secondary-exclusion cells pair within-group denominators with cross-group partition percentages

- **Location found:** [Supplement 2, eTable 10 — PDF p. 24](../../../joi240147supp2_prod_1738701765.29201.pdf#page=24), `Secondary exclusion`; count comparator in [Main article, Figure 1 — PDF p. 3](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=3), restrictive and liberal `Secondary exclusions` branches.
- **Source value/text matched:** eTable 10 prints `N=341`, restrictive `174/750 (51)`, and liberal `165/758 (49)`. Its footnote states that two patients had missing randomized-oxygen data, explaining the discrepancy between `N=341` and the numbers in the table. Figure 1 prints 174 restrictive and 165 liberal secondary exclusions.
- **Comparator matched:** Figure 1 matches the eTable's group counts, 174 and 165. The percentages are paired in eTable cells with displayed denominators 750 and 758 under `no./total no. (%)`.
- **Consistency rule applicable:** Yes. A percentage shown in the same count/total cell should use the displayed denominator unless the source explicitly defines another percentage estimand. Mutually exclusive classified group counts may also be checked against the stated total and the footnote.
- **Calculation or logical comparison reproduced:** `174 + 165 = 339`, and `341 - 339 = 2`, matching the footnote's two missing randomized-oxygen assignments. Using the printed cell denominators gives `100 × 174 / 750 = 23.2%` and `100 × 165 / 758 = 21.767810%`, or 21.8% to one decimal. The printed 51% and 49% instead match the allocation distribution among 339 classified exclusions: `100 × 174 / 339 = 51.327434%` and `100 × 165 / 339 = 48.672566%`.
- **Necessary inputs available:** The stated total, group counts, within-group denominators, percentages, footnote, and Figure 1 count comparator are available.
- **Exact missing inputs or definitions:** The source does not state whether the intended percentage is within-group secondary-exclusion incidence or treatment-group distribution among the 339 classified secondary exclusions. It also does not show how the two patients with missing randomized-oxygen data enter any percentage denominator.
- **Source-grounded alternative interpretation:** The table may intend to show the treatment allocation distribution among the 339 classified secondary exclusions, in which case 51% and 49% follow but `/750` and `/758` describe a different denominator concept. Alternatively, it may intend within-group exclusion incidence, in which case the printed denominators yield 23.2% and 21.8%.
- **Direct observation:** The direct PDF prints counts and within-group denominators that yield 23.2% and 21.8%, while the printed percentages partition the 339 classified exclusions; Figure 1 matches the counts.
- **Inferred explanation:** Combining a distribution percentage with within-group count denominators is a possible table-construction explanation, but the intended estimand is not explicitly defined.
- **Exact remaining human question:** Is eTable 10 intended to report treatment-group distribution among classified secondary exclusions or within-group secondary-exclusion incidence, what denominator belongs to each percentage, and how should the two patients with missing randomized-oxygen assignment enter the presentation?

## C008 — Missing-as-event primary count uses a doubled numerator/denominator separator

- **Location found:** [Supplement 2, eTable 11 — PDF p. 25](../../../joi240147supp2_prod_1738701765.29201.pdf#page=25), primary outcome, `Missing counted as event`, restrictive oxygen group.
- **Source value/text matched:** At high resolution, the direct PDF visibly prints `135//750 (18.0)`. Direct raw-text and bounding-box extraction both emit `135//750`; targeted CPU OCR of the 600-dpi crop also emits the doubled separator. A low-resolution whole-page rendering can visually collapse the two closely spaced slashes.
- **Comparator matched:** The row label defines `no./total no. (%)`; the paired liberal cell prints `155/758 (20.4)`, and all other count/denominator cells on eTable 11 use a single slash.
- **Consistency rule applicable:** Yes for notation consistency. The doubled separator is compared with the table's single-slash count/total notation. The numeric count/denominator/percentage identity is separately checkable and does reconcile.
- **Calculation or logical comparison reproduced:** Treating the numeric values as numerator 135 and denominator 750 gives `100 × 135 / 750 = 18.0%`, matching the displayed percentage. The paired liberal value gives `100 × 155 / 758 = 20.448549%`, which displays as 20.4% to one decimal. The observation concerns the two printed slash glyphs, not numeric arithmetic.
- **Necessary inputs available:** The direct high-resolution glyph rendering, raw and bounding-box text, OCR output, row label, paired cell, numeric values, and table-wide separator convention are available.
- **Exact missing inputs or definitions:** The package lacks the publication production file or accessibility-layer specification needed to determine whether both slash glyphs were intentionally encoded or whether one is an unintended duplicate. It also lacks an authoritative table-program output separate from the supplied PDF.
- **Source-grounded alternative interpretation:** The doubled slash may be a typesetting or text-layer artifact that does not change the human-readable numeric relation but can be retained by machine extraction or manual transcription.
- **Direct observation:** The supplied PDF contains two slash glyphs in `135//750` when inspected at 600 dpi, and all three targeted extraction modes reproduce them; the same cell's arithmetic yields 18.0%.
- **Inferred explanation:** An unintended duplicate glyph or encoding artifact is possible, but its production cause and intended source string are not stated.
- **Exact remaining human question:** Is the authoritative intended source string for this cell `135/750` or `135//750`, and does the publication's visible and extractable representation intentionally contain two slash glyphs?

## Recheck summary

- **Stable IDs covered:** C001, C002, C003, C004, C005, C006, C007, C008.
- **Exact unresolved definitions:** authoritative fields for C001 and C002; table-specific model identity and unrounded interval for C003; authoritative percentage/denominator and rounding conventions for C004 and C005; eTable 10 population and denominator definitions for C006 and C007; and intended production string/encoding for C008.
- **Evidence authority:** Direct supplied PDFs at the cited pages. Reusable and targeted derivatives served only as locators and visual/transcription aids.
