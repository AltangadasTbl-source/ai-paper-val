# Stable Candidate Ledger

This ledger contains every distinct quality-control candidate identified after complete mapping and the independent numeric, cross-source, and statistical-pass-1 reviews. Similar checker leads were merged only when they concerned the same printed values, comparator, and consistency rule. Every candidate remains **Pending Human Adjudication**; no severity, validity, acceptance, exclusion, or correction is assigned.

## C001 — Table 5 absolute difference does not reproduce from the displayed counts

- **Status:** Pending Human Adjudication
- **Category:** Numeric or arithmetic inconsistency
- **Exact source locations:** [DOC-001 main article — PDF p. 9](../../jama_flint_2019_oi_190079.pdf#page=9), Table 5, total-cholesterol and LDL rows.
- **Direct source evidence:** Each row prints 9/64 (14.1%) versus 6/62 (9.7%) and an “Absolute Unadjusted Difference Between Groups” of 4.3%; the value is repeated for both outcomes.
- **Comparator and rule:** An unadjusted absolute difference between the two displayed group proportions should equal the first displayed proportion minus the second, using the displayed counts and arm denominators.
- **Calculation:** `(9/64 - 6/62) × 100 = 4.3850806` percentage points, which displays as 4.4% to one decimal under conventional rounding. The displayed rounded percentages also give `14.1 - 9.7 = 4.4` percentage points. The printed 4.3% differs by about 0.085 percentage point and is outside a ±0.05 one-decimal rounding interval.
- **Alternative source-grounded interpretations:** The table footnote identifies exact confidence intervals but does not name an alternative point-estimator, adjusted denominator, continuity correction, or different analysis population. An undocumented estimator or more precise hidden inputs could explain the display, but the supplied source does not establish one.
- **Exact human question:** Was the point difference calculated by a method other than the raw unadjusted difference of the displayed proportions; if so, what method and denominator were used?
- **Checker provenance:** N014; numeric consistency reviewer. Cross-source review found no second location that resolves the point-estimator definition.

## C002 — HbA1c interaction is labelled with a concentration unit while matched displays use percent

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** [DOC-001 main article — PDF p. 1](../../jama_flint_2019_oi_190079.pdf#page=1), abstract; [DOC-001 main article — PDF p. 7](../../jama_flint_2019_oi_190079.pdf#page=7), secondary outcomes; [DOC-001 main article — PDF p. 8](../../jama_flint_2019_oi_190079.pdf#page=8), Table 4; [DOC-003 eFigures — PDF p. 9](../../joi190079supp2_prod.pdf#page=9), eFigure 8.
- **Direct source evidence:** The same HbA1c daily treatment-by-time estimate is printed as -0.0002 `mg/dL` (95% CI, -0.0021 to 0.0016) on main-paper pp. 1 and 7. Table 4 labels HbA1c as `%`, and the matched longitudinal eFigure axis is `HbA1c (%)`.
- **Comparator and rule:** A measure and its matched model display should use a compatible scale/unit. HbA1c percent is not a mass concentration in mg/dL, and no conversion or distinct transformed HbA1c metric is defined in the supplied package.
- **Calculation:** Label comparison only; no numeric conversion is supportable from the supplied sources. The estimate and interval repeat exactly across the abstract and results, while only the unit conflicts with the table/figure scale.
- **Alternative source-grounded interpretations:** A distinct transformed concentration-scale HbA1c variable might have been analyzed, but the methods, Table 4, and eFigure 8 provide no such label or transformation. The intended replacement unit cannot be inferred conclusively.
- **Exact human question:** Was `mg/dL` a production-label error for a percentage-point-per-day HbA1c interaction, or was a distinct transformed HbA1c measure analyzed but not defined?
- **Checker provenance:** N016; S008, S012, S047; numeric reviewer; cross-source reviewer; statistical pass 1.

## C003 — Protocol recruitment target conflicts between 82 and 98 participants per site

- **Status:** Pending Human Adjudication
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [DOC-002 protocol/SAP — PDF p. 7](../../joi190079supp1_prod.pdf#page=7), Figure 1; [DOC-002 protocol/SAP — PDF p. 17](../../joi190079supp1_prod.pdf#page=17), Table 4; [DOC-002 protocol/SAP — PDF p. 21](../../joi190079supp1_prod.pdf#page=21), Human Subjects recruitment statement.
- **Direct source evidence:** Figure 1 prints acute N=392. Table 4 prints four sites recruiting 98 acute participants each and randomizing 44 each. The Human Subjects text states that each of four sites will recruit 82 patients.
- **Comparator and rule:** For the same four-site acute recruitment plan, the per-site count multiplied by four should equal the stated total, absent an explicitly different population, phase, or time frame.
- **Calculation:** `98 × 4 = 392`, matching Figure 1. `82 × 4 = 328`, differing from 392 by 64 participants and from 98/site by 16 participants per site.
- **Alternative source-grounded interpretations:** The 82/site statement may reflect an earlier or amended recruitment target, a different recruitment denominator, or an unlabelled revision; the supplied page does not state a different phase, population, or version basis.
- **Exact human question:** Do the 82/site and 98/site statements describe different recruitment targets or document versions; if not, which count defines the intended four-site acute recruitment total?
- **Checker provenance:** N044; numeric reviewer; cross-source reviewer.

Stable candidate count: 3. Stable IDs are C001, C002, and C003. No candidate was created from a display-zero P value.
