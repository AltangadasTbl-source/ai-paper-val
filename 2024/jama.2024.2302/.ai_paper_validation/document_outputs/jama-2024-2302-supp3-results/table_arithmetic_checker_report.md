# Table Arithmetic and Internal-Consistency Check

- **Document:** `jama-2024-2302-supp3-results` (`joi240020supp3_prod_1710443209.75411.pdf`)
- **Scoped pages reviewed:** source-PDF pp. 2-5 only (eTables 1-2), using the retained page renders as the authoritative table source because native glyph mappings are corrupted. No protocol, SAP, administrative material, raw data, or external sources were used.

## Candidate issue (1)

### TAI-01 — Conflicting description of the frequentist primary-outcome model

- **Taxonomy:** Presentation inconsistency
- **Location:** Results supplement PDF p. 5, eTable 2, table note beneath the frequentist outcome table.
- **Source values/statements:** The note first states: “A logistic mixed-effect model was used to analyze the primary outcome.” It later states: “Frequentist and Bayesian analyses used the same models except for the frequentist analysis of the primary outcome which used a generalized estimating equation logistic model … due to non-convergence of the mixed-effect model.”
- **Calculation/logical comparison:** eTable 2 is titled “Frequentist primary and major secondary outcome analyses.” Within that table’s single note, the frequentist primary analysis is described both as a logistic mixed-effect model and, in the stated exception, as a generalized estimating equation logistic model because the mixed-effect model did not converge. These descriptions cannot both identify the fitted frequentist primary-outcome model.
- **Reasoning:** The displayed estimates themselves are not arithmetically contradicted; the issue is a locally conflicting model-description sentence that could mislead a reader about how the p=.01 primary-outcome results were obtained.
- **Severity/uncertainty:** Low severity; low uncertainty as a wording conflict. The intended reading may be that the first sentence describes the Bayesian model, but the table is explicitly labelled frequentist and the first sentence does not make that distinction.
- **Verification instruction:** Check the wording against the corresponding main-article statistical-analysis paragraph and amend the eTable note to state unambiguously which model produced the frequentist primary-outcome estimates.

## Checks passed

| Location | Check and calculation | Result |
|---|---|---|
| PDF pp. 2-3, eTable 1 | Parent/guardian refusal: `280 + 196 + 71 + 66 = 613`. Physician refusal: `14 + 14 + 9 = 37`. | Agree with printed denominators. |
| PDF pp. 3-4, eTable 1 | “Other reasons” not consented: `4 + 4 + 3 + 2 + 1 + 1 + 1 = 16`. Site-level ineligibility rows sum to `51`; that section has no printed section denominator, so it was not treated as a partition of the 442 ineligible infants. | No arithmetic discrepancy. |
| PDF p. 5, eTable 2 | Primary outcome: early `44/159 = 27.7% -> 28%`; late `27/149 = 18.1% -> 18%`; crude RR `(27/149)/(44/159) = 0.65`, agreeing with displayed 0.65. The raw late-minus-early difference is `-9.5%`; the displayed `-9.0%` is model-derived and therefore is not expected to equal the unadjusted difference. | No numerical inconsistency. |
| PDF p. 5, eTable 2 vs main article PDF p. 6, Table 2 | eTable 2 and Table 2 report the same counts and rounded group percentages (44/159 [28%] vs 27/149 [18%]) and the same hospital medians/IQRs (19.0 [9.8,35] vs 16.0 [7,38]). Differences between frequentist and Bayesian interval/effect displays are identified by the tables’ analysis context, not an arithmetic contradiction. | No table-to-table value discrepancy. |
