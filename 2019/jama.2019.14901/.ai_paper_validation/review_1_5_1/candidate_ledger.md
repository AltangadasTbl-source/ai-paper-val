# Stable Candidate Ledger

All entries are quality-control candidates with status **Pending Human Adjudication**. Stable IDs were assigned after merging only genuine duplicates across the numeric, cross-source, and statistical pass-1 checker artifacts. No candidate count limit was used.

## C001 — Day-7 respiratory-failure absolute difference differs across matched article locations

- **Status:** Pending Human Adjudication
- **Category:** Numeric or arithmetic inconsistency
- **Relationship provenance:** N011; S004.
- **Checker provenance:** NUM-CAND-001; CROSS-CAND-001; STAT1-CAND-001.
- **Exact source locations:** [main article — PDF p. 1](<../../jama_thille_2019_oi_190108.pdf#page=1>) (abstract Results); [main article — PDF p. 6](<../../jama_thille_2019_oi_190108.pdf#page=6>) (Results); [main article — PDF p. 8](<../../jama_thille_2019_oi_190108.pdf#page=8>) (Table 2).
- **Printed evidence:** The abstract and Results print 21% versus 29%, difference -8.7% (95% CI -15.2% to -1.8%; P=.01). Table 2 prints 88/302 versus 70/339 and difference -8.5% with the same CI and P value.
- **Reproducible rule:** In the printed contrast order, `(70/339 - 88/302) x 100 = -8.4901` percentage points, which rounds to -8.5 at one decimal; -8.7 is a distinct printed value for the otherwise matched result.
- **Direct observation versus inference:** The two point estimates are direct observations. Count-derived reconciliation supports the table value diagnostically but does not establish why the prose differs.
- **Alternative source-grounded interpretations:** An undocumented distinct calculation, an earlier retained value, or a transcription/editing difference; the supplied package does not label a distinct analysis.
- **Exact human question:** Which absolute difference was intended, and does any documented analysis distinction justify -8.7 rather than the count-derived/Table 2 -8.5?

## C002 — Reintubation respiratory-acidosis cutoff differs between article and protocol

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Relationship provenance:** N004; N032; S001; S024.
- **Checker provenance:** CROSS-CAND-002; STAT1-CAND-003.
- **Exact source locations:** [main article — PDF p. 4](<../../jama_thille_2019_oi_190108.pdf#page=4>) (Outcomes); [protocol — PDF p. 31](<../../joi190108supp1_prod.pdf#page=31>) (section 5.4, continued from p. 30).
- **Printed evidence:** The article defines reintubation respiratory acidosis as pH below 7.25 with PaCO2 above 45 mm Hg. Protocol version 4 defines the matched criterion as pH below 7.35 with PaCO2 above 45 mm Hg.
- **Reproducible rule:** The criterion role, two-criteria structure, PaCO2 condition, unit, and decision context match, but the pH thresholds differ by 0.10 units.
- **Direct observation versus inference:** The printed thresholds are direct observations. A later amendment or implementation change is possible but is not supplied.
- **Alternative source-grounded interpretations:** The article may reflect a later approved amendment or an implementation-specific definition; no amendment history in the package resolves the difference.
- **Exact human question:** Which pH cutoff governed event ascertainment, and is there a dated amendment explaining the change from <7.35 to <7.25?

## C003 — Hypercapnic ineffective-cough percentages conflict with printed fractions

- **Status:** Pending Human Adjudication
- **Category:** Denominator, proportion, or total inconsistency
- **Relationship provenance:** N050.
- **Checker provenance:** NUM-CAND-002.
- **Exact source locations:** [results supplement — PDF p. 4](<../../joi190108supp2_prod.pdf#page=4>) (eTable 2, hypercapnic ineffective-cough row); [main article — PDF p. 6](<../../jama_thille_2019_oi_190108.pdf#page=6>) (Table 1 aggregate row).
- **Printed evidence:** eTable 2 prints 14/45 (69%) and 16/59 (73%) under `Ineffective cough, No./total No. (%)`. The same row's nonhypercapnic values are 51/239 (21%) and 70/263 (27%); main Table 1 prints aggregate 65/284 (23%) and 86/322 (27%).
- **Reproducible rule:** 14/45=31.1% and 16/59=27.1%, not 69% and 73%. The printed percentages equal the complementary proportions, while stratum numerators and denominators sum exactly to the article aggregates.
- **Direct observation versus inference:** The fraction-percentage conflicts are direct observations. Complement coding is a numerical inference not stated by the row label.
- **Alternative source-grounded interpretations:** The numerator, denominator, row label, or percentages may be inversely coded or mistranscribed.
- **Exact human question:** What do 69% and 73% denote, and should the cells instead report 31% and 27% or use different labelled numerators/denominators?

## C004 — Hypercapnic abundant-secretion percentages conflict with printed fractions

- **Status:** Pending Human Adjudication
- **Category:** Denominator, proportion, or total inconsistency
- **Relationship provenance:** N050.
- **Checker provenance:** NUM-CAND-003.
- **Exact source locations:** [results supplement — PDF p. 4](<../../joi190108supp2_prod.pdf#page=4>) (eTable 2, hypercapnic abundant-secretions row); [main article — PDF p. 6](<../../jama_thille_2019_oi_190108.pdf#page=6>) (Table 1 aggregate row).
- **Printed evidence:** eTable 2 prints 20/46 (57%) and 23/61 (62%) under `Abundant secretions, No./total No. (%)`. The nonhypercapnic values are 101/242 (42%) and 91/265 (34%); main Table 1 prints aggregate 121/288 (42%) and 114/326 (35%).
- **Reproducible rule:** 20/46=43.5% and 23/61=37.7%, not 57% and 62%. The printed percentages equal complementary proportions, and the stratum fractions reconcile to the article aggregates.
- **Direct observation versus inference:** The fraction-percentage conflicts are direct observations. Inverse coding is possible but unlabelled.
- **Alternative source-grounded interpretations:** The numerator/denominator labels, row label, or percentages may describe an inverse measure or contain a transcription error.
- **Exact human question:** Do 57% and 62% describe absence rather than presence of abundant secretions; if so, what are the correct label and fractions, and if not, which values should be reconciled?

## C005 — Matched nonhypercapnic day-7 reintubation P values differ across article and supplement

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Relationship provenance:** S019; S036.
- **Checker provenance:** STAT1-CAND-002.
- **Exact source locations:** [main article — PDF p. 7](<../../jama_thille_2019_oi_190108.pdf#page=7>) (subgroup Results); [results supplement — PDF p. 7](<../../joi190108supp2_prod.pdf#page=7>) (eTable 4).
- **Printed evidence:** For the same nonhypercapnic day-7 reintubation result—35/276 versus 45/254, difference -5.0 percentage points, 95% CI -11.2 to 1.1—the article prints P=.10 and eTable 4 prints P=.1057.
- **Reproducible rule:** Population, contrast, endpoint, counts, effect, and interval match, yet the attached printed P values differ. At conventional rounding, .1057 becomes .11 at two decimals, not .10; the source does not state a truncation or different-test convention.
- **Direct observation versus inference:** The two P values and matched-result identity are direct observations. Their calculation conventions are not fully specified.
- **Alternative source-grounded interpretations:** Different display precision, truncation, continuity handling, or separate analysis outputs could explain the values, but none is documented in the supplied sources.
- **Exact human question:** Were P=.10 and P=.1057 intentionally produced or displayed under different documented conventions, or should one matched location be reconciled?

## C006 — Protocol total-duration breakdown does not arithmetically reach the printed total

- **Status:** Pending Human Adjudication
- **Category:** Numeric or arithmetic inconsistency
- **Relationship provenance:** N027.
- **Checker provenance:** Quality-audit coverage repair of the original N027 no-candidate closure.
- **Exact source locations:** [protocol — PDF p. 11](<../../joi190108supp1_prod.pdf#page=11>) (synopsis study duration); [protocol — PDF p. 32](<../../joi190108supp1_prod.pdf#page=32>) (section 5.6, Duration of the Study).
- **Printed evidence:** Page 11 states 36 months of inclusion, 3 months of participation for each patient, and 51 months total comprising 39 months for the study plus 12 months for analysis. Page 32 states 3 months' participation, 36 months' recruitment, then `Total study duration: 51 months with 36 months for the study and 12 months for analysis`.
- **Reproducible rule:** The page-11 decomposition is `36 + 3 + 12 = 51`. The components explicitly named in page 32's total-duration sentence give `36 + 12 = 48`, three months short of the printed 51.
- **Direct observation versus inference:** Both breakdowns and the arithmetic mismatch are direct observations. It is an inference that page 32 intended to include the separately printed 3-month final-participant follow-up without naming it in the breakdown.
- **Alternative source-grounded interpretations:** Page 32's `36 months for the study` may be shorthand for recruitment followed by the final participant's 3-month follow-up, with the adjacent participation line supplying the omitted component; page 11 explicitly supports that interpretation.
- **Exact human question:** Should page 32 describe 39 months for the study plus 12 months for analysis, or otherwise state that the separately listed 3-month follow-up is included in the 51-month total?
