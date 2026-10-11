# Stable Candidate Ledger

All registered candidates remain **Pending Human Adjudication**. Raw checker records were merged only
when they concerned the same printed values, comparator, and consistency rule. NC-02 and the sole
cross-source raw record were therefore merged as C002; all other raw records remain distinct.

## C001 — Usual-care exclusion hierarchy requires source-layout confirmation

- **Status:** Pending Human Adjudication
- **Category:** Numeric or arithmetic inconsistency
- **Checker provenance:** Numeric consistency NC-01, mechanically revised after the evidence-quality visual audit.
- **Exact source location:** [DOC-001 Figure 1, PDF p. 5](../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=5), usual-care branch.
- **Printed evidence:** The parent node reports 58 excluded. Visual indentation shows 13 Physician preference as a top-level reason, with 7 disease status/progression, 4 perceived psychosocial issues, and 2 reason not provided nested beneath it. The remaining top-level counts are 15, 14, 7, 4, 3, and 2.
- **Consistency rule:** Child reasons must reconcile to their immediate parent, and only top-level reasons are added to the 58-excluded total.
- **Calculation:** 7 + 4 + 2 = 13. The top-level calculation is 13 + 15 + 14 + 7 + 4 + 3 + 2 = 58. The original 71 calculation double-counted the 13 parent and its three children. The surrounding flow also reconciles: 323 - 58 = 265 and 265 - 41 = 224.
- **Direct observation versus inference:** Counts and indentation are directly visible. Interpreting indentation as parent-child structure is corroborated by the parallel screening arm, where 32 + 4 + 2 + 4 = the 42 Physician preference parent.
- **Human question:** Does the production source confirm that the visual indentation denotes the parent-child hierarchy described above? This stable ID is preserved for human adjudication because IDs cannot be deleted after registration; no 71-versus-58 mismatch should be propagated from a flat reading.

## C002 — Main-text rejected-statement percentage conflicts with the supplement counts

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** Numeric consistency NC-02 and the sole cross-source raw record.
- **Exact source locations:** [DOC-001 narrative, PDF p. 2](../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=2) and [DOC-003 eTable 3, PDF p. 6](../../joi240111supp2_prod_1733431204.76024.pdf#page=6).
- **Printed evidence:** The main text reports 6.4% rejected across all intervention sites. eTable 3 prints n=135 for each of 10 sites and reject counts 15, 23, 5, 25, 9, 25, 12, 11, 11, and 6.
- **Consistency rule:** Under the common printed denominator, the cross-site percentage equals the sum of reject counts divided by 10 x 135.
- **Calculation:** Reject counts total 142; 142 / 1,350 x 100 = 10.5185...%, or 10.5% to one decimal, not 6.4%. The table's keep and adapt totals independently reproduce the narrative's 40.8% and 48.7%.
- **Direct observation versus inference:** The narrative percentage, site denominators, and site counts are direct observations. The 10.5% comparator is derived using the displayed common denominator.
- **Human question:** What denominator or rejection definition yields 6.4%, or should the narrative be reconciled with the displayed 142/1,350 result?

## C003 — eTable 10 labels logistic-regression odds ratios as differences

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** Statistical pass 1 raw candidate.
- **Exact source locations:** [DOC-003 eTable 10, PDF pp. 13-15](../../joi240111supp2_prod_1733431204.76024.pdf#page=13) and [DOC-003 eMethods, PDF p. 22](../../joi240111supp2_prod_1733431204.76024.pdf#page=22).
- **Printed evidence:** eTable 10 uses the shared modeled-effect header “Difference (95% CI)” across documentation and intervention blocks. The eMethods states that logistic regression was used to estimate an odds ratio; table values include 0.53 (0.28, 1.01), 17.96 (1.03, 313.1), and 5.30 (2.50, 11.24).
- **Consistency rule:** A logistic-regression odds ratio is a multiplicative effect measure and should not be identified as an unqualified difference.
- **Calculation:** Label/measure identity comparison; no reconstructed test or P value is used.
- **Direct observation versus inference:** The column header and eMethods estimand are direct observations. Applying the source's method definition to the table blocks identifies the label conflict.
- **Human question:** Is the eTable 10 modeled-effect column intended to report odds ratios throughout, and if any cells instead report another measure, which blocks use which estimand?
