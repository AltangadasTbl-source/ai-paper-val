# Stable Candidate Ledger

All candidates remain **Pending Human Adjudication**. Stable IDs were assigned only after merging
records that used the same printed values or labels, comparator, and consistency rule. Similar but
distinct definition mismatches remain separate.

## C001 — Primary SAE endpoint is labeled `>1` and `≥1`/“any” for matched results

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** `N-CAND-02`; cross-source Candidate 1; `P1-S-001`
- **Exact source locations:** [PDF-001 p. 6](<../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6>), Table 2; [PDF-004 p. 5](<../../joi240020supp3_prod_1710443209.75411.pdf#page=5>), eTable 2; [PDF-002 p. 2](<../../joi240020supp1_prod_1710443209.74911.pdf#page=2>); [PDF-003 p. 4](<../../joi240020supp2_prod_1710443209.75411.pdf#page=4>).
- **Source evidence:** Main Table 2 labels 44/159 and 27/149 as “Had ≥1 serious adverse event.” eTable 2 reports the same counts under “Infant had > 1 SAE.” Protocol locations use `>1`; SAP/main locations also use `≥1`, “at least one,” or “any.”
- **Consistency rule:** For a nonnegative event count, `>1` means at least two and `≥1` includes exactly one. The labels are not interchangeable unless no analyzed infant had exactly one SAE, which the package does not establish.
- **Direct observation and inference boundary:** The conflicting operators and matched counts are direct observations. A typographical convention or the number of infants with exactly one SAE is not inferred.
- **Alternative source-grounded interpretation:** Repeated “any” and “at least one” wording supports the possibility that `>1` was used informally for more than zero, but the repeated `>1` wording prevents source-only resolution.
- **Exact human question:** Which threshold generated 44/159 and 27/149, and does any location require correction, clarification, or version qualification?

## C002 — Planned median hospital-day values conflict across protocol/SAP locations

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** `N-CAND-01`; cross-source Candidate 2; `P1-S-002`
- **Exact source locations:** [PDF-002 p. 3](<../../joi240020supp1_prod_1710443209.74911.pdf#page=3>); [PDF-002 p. 12](<../../joi240020supp1_prod_1710443209.74911.pdf#page=12>); [PDF-003 p. 3](<../../joi240020supp2_prod_1710443209.75411.pdf#page=3>).
- **Source evidence:** Protocol p. 3 defines the planned 3-day median reduction as 18 days early versus 15 late. Protocol p. 12 gives medians 8 versus 5 (and means 18 versus 13). The SAP explicitly says the protocol p. 3 median values 18/15 are incorrect and identifies 8/5 as correct.
- **Consistency rule and calculation:** The same arm-specific planned medians cannot be both 18/15 and 8/5. Early: 18−8=10 days; late: 15−5=10 days. Both pairs preserve a 3-day contrast, so the inconsistency is in the arm values/summary label rather than the contrast arithmetic.
- **Direct observation and inference boundary:** The values and SAP correction are direct observations; their production/version history is not inferred.
- **Alternative source-grounded interpretation:** Protocol p. 12 distinguishes medians 8/5 from means 18/13, and the SAP identifies 8/5 as intended. The package does not supply drafting or amendment history.
- **Exact human question:** Which arm-specific medians governed the final design, and does protocol p. 3 require correction, clarification, or version qualification?

## C003 — Bayesian intervention-prior ranges differ between the article and SAP

- **Status:** Pending Human Adjudication
- **Category:** Statistical reporting inconsistency
- **Checker provenance:** `P1-S-003`
- **Exact source locations:** [PDF-001 p. 4](<../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4>); [PDF-003 p. 8](<../../joi240020supp2_prod_1710443209.75411.pdf#page=8>).
- **Source evidence:** The article states categorical and count intervention priors centered at 1.0 with 95% CrI 0.33-3.0. The SAP specifies categorical log-OR Normal(0, 0.7), described as OR 1.0 (95% CrI 0.2-4), and a count prior RR 1.0 (0.33-3.3).
- **Consistency rule:** These endpoints do not describe identical priors on the stated OR/RR scales.
- **Direct observation and inference boundary:** The different printed ranges are direct observations. No supplied amendment identifies whether the article simplified, replaced, or outcome-specifically applied them.
- **Alternative source-grounded interpretation:** The supplied sources do not select between their common article-level range and the SAP's class-specific ranges; any amendment or simplification history remains an evidence limitation.
- **Exact human question:** What final prior was used for each primary and major-secondary model, and how should the article and SAP descriptions be reconciled?

## C004 — Gestational-age subgroup boundary is printed as `≥28` and `>28` weeks

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** `P1-S-004`; numeric reviewer recorded the same unresolved label history as a checked noncandidate absent a supplied exactly-28-week mapping
- **Exact source locations:** [PDF-001 p. 8](<../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8>), Figure 3; [PDF-003 p. 9](<../../joi240020supp2_prod_1710443209.75411.pdf#page=9>); [PDF-003 p. 3](<../../joi240020supp2_prod_1710443209.75411.pdf#page=3>); [PDF-003 p. 8](<../../joi240020supp2_prod_1710443209.75411.pdf#page=8>).
- **Source evidence:** Figure 3 reports numeric subgroup results for `<28 wk` and `≥28 wk`; the SAP planned moderator/randomization wording uses `<28` and `>28` weeks, while SAP p. 8 itself uses `<28` and `≥28` for the model covariate.
- **Consistency rule:** `≥28` includes exactly 28 weeks, while `>28` excludes exactly 28 weeks; these labels define different partitions.
- **Direct observation and inference boundary:** The inequality symbols and reported subgroup results are direct observations. The package does not state how infants recorded at exactly 28 weeks, or rounded gestational ages, were assigned.
- **Alternative source-grounded interpretation:** The SAP's own p. 8 `≥28` wording and the article's complete displayed partition support the possibility that `>28` is inconsistent shorthand. The exact coding and rounding convention remain missing inputs.
- **Exact human question:** What cut point and rounding convention defined the analyzed subgroup and randomization stratum, and which label should be corrected?

## C005 — Primary-outcome time origin is labeled enrollment and randomization

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** `P1-S-005`; cross-source reviewer recorded the terminology difference but found no supplied event-count change
- **Exact source locations:** [PDF-002 p. 3](<../../joi240020supp1_prod_1710443209.74911.pdf#page=3>); [PDF-002 p. 11](<../../joi240020supp1_prod_1710443209.74911.pdf#page=11>); [PDF-003 p. 7](<../../joi240020supp2_prod_1710443209.75411.pdf#page=7>); [PDF-001 p. 3](<../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3>); [PDF-001 p. 6](<../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6>), hospital-days footnote `g` as secondary-outcome context only.
- **Source evidence:** The protocol defines SAE ascertainment from enrollment through 10 months after enrollment. The SAP and main article p. 3 describe primary-outcome collection for 10 months after randomization. Main article p. 6 footnote `g` says “From randomization until 10 months later,” but attaches to the hospital-stay row rather than directly to the primary SAE row.
- **Consistency rule:** Enrollment and randomization are different named time origins unless the study defines them as the same instant. The supplied sources do not do so or quantify the interval.
- **Direct observation and inference boundary:** The time-origin wording is directly observed. No difference in counted events or elapsed time is inferred.
- **Alternative source-grounded interpretation:** Enrollment and randomization may have been operationally simultaneous or the terms may have been used interchangeably in these documents.
- **Exact human question:** Were enrollment and randomization the same operational instant for SAE ascertainment, and what time origin should consistently label the primary analysis?

## Registration summary

- Stable candidates: 5 (`C001`, `C002`, `C003`, `C004`, `C005`).
- No candidate is based on a display-zero P value.
- No severity, validity, acceptance, exclusion, or correction has been assigned.
