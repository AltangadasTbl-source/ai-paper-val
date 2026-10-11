# Stable Candidate Ledger

This ledger was rebuilt from the complete Workflow 1.5.1 relationship inventories and the three independent first-wave checker artifacts. Exact duplicates were merged only when they concerned the same printed values, comparator, and consistency rule. Similar but distinct severe-NDI definition discrepancies remain separate. Every entry is **Pending Human Adjudication**; no validity, importance, correction, or severity determination is made.

## C001 — eTable 4 expands RR as risk difference although the table reports relative risk

- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** NUM-CAND-001; CROSS-CAND-001; STAT1-CAND-003; canonical relationships N125 and S056.
- **Exact source locations:** DOC-005, PDF p. 7, eTable 4 header; DOC-005, PDF p. 8, abbreviation line and binary-outcome model note.
- **Printed evidence:** The header says `Relative Risk (RR) or Mean Difference (MD)` and the model note says binary outcomes report relative risks, while the abbreviation line says `RR = risk difference`. Values such as PDA `RR: 0.86 (0.75, 0.99)` are displayed on a ratio scale.
- **Consistency rule:** Relative risk and risk difference are different measures and scales; one abbreviation must not identify both within the same table.
- **Direct observation versus inference:** The conflicting labels are direct observations. A localized copyediting error is a possible explanation, not an established cause.
- **Remaining human question:** Should the p. 8 abbreviation expand RR as `relative risk`, consistently with the header, model note, and displayed estimates?
- **State:** Pending Human Adjudication

## C002 — Registered eligibility-bound discrepancy is not reproduced on direct-source recheck

- **Category:** Analysis-unit or population inconsistency
- **Checker provenance:** NUM-CAND-002; CROSS-CAND-005.
- **Exact source locations:** DOC-002, PDF p. 4; DOC-003, PDF p. 7; DOC-004, PDF pp. 8 and 15; DOC-001, PDF p. 2.
- **Printed evidence:** Direct rendered-page recheck shows DOC-002 p. 4 prints eligibility through `28 6/7` weeks, agreeing with the manual, SAP, and final article. The earlier mapper/checker transcription of `27 6/7` is not present on the cited page.
- **Consistency rule:** The same trial eligibility population should have one upper boundary. The rule is applicable, but the direct sources compared here agree.
- **Direct observation versus inference:** Agreement at `28 6/7` is the authoritative direct observation. The registered discrepancy arose from an unusable embedded-font extraction/transcription, not a reproduced source conflict.
- **Remaining human question:** Can a human confirm the direct-page reading and retain this ID solely as an audit trail for the corrected transcription?
- **State:** Pending Human Adjudication

## C003 — Registered first-dose discrepancy is not reproduced on direct-source recheck

- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** NUM-CAND-003; CROSS-CAND-006.
- **Exact source locations:** DOC-002, PDF p. 4; DOC-003, PDF pp. 7 and 12; DOC-004, PDF pp. 8 and 15; DOC-001, PDF p. 2; DOC-005, PDF p. 4.
- **Printed evidence:** Direct rendered-page recheck shows DOC-002 p. 4 prints `2.5 mL/kg` for the first dose, agreeing with the manual, SAP, article, and results supplement; `1.25 mL/kg` is the second-dose volume. The earlier first-dose transcription is not present on the cited page.
- **Consistency rule:** A matched intervention dose and dose-order label should agree. The rule is applicable, and the direct-source first-dose values agree at `2.5 mL/kg`.
- **Direct observation versus inference:** Direct-page agreement is authoritative. The registered factor-of-two discrepancy came from broken-font extraction/transcription.
- **Remaining human question:** Can a human confirm the direct-page dose sequence and retain this ID solely as an audit trail for the corrected transcription?
- **State:** Pending Human Adjudication

## C004 — Severe-NDI GMFCS cutoff differs between the manual and SAP

- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** NUM-CAND-004; part of CROSS-CAND-007.
- **Exact source locations:** DOC-003, PDF pp. 14-17, particularly p. 16; DOC-004, PDF p. 10 and pp. 33-34.
- **Printed evidence:** The manual defines severe NDI with GMFCS levels `3-5`; the SAP passages use GMFCS levels `4-5`.
- **Consistency rule:** A binary endpoint component should use one categorical threshold; the discrepancy changes whether GMFCS level 3 is included.
- **Direct observation versus inference:** The thresholds are directly printed. A versioned definition change is possible, but no governing amendment is supplied.
- **Remaining human question:** Which GMFCS threshold governed the severe-NDI endpoint, and should the other document be reconciled or version-labelled?
- **State:** Pending Human Adjudication

## C005 — Registered severe-NDI instrument-edition discrepancy is not reproduced on direct-source recheck

- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** NUM-CAND-005; part of CROSS-CAND-007.
- **Exact source locations:** DOC-003, PDF pp. 14-17, particularly p. 16; DOC-004, PDF p. 10 and pp. 33-34.
- **Printed evidence:** Direct rendered-page recheck shows DOC-004 p. 33 says `4th edition`, consistent with BSID-IV in the manual and SAP p. 10; the earlier `Bayley-III` transcription is not present on the cited page.
- **Consistency rule:** A matched outcome definition should identify one assessment edition. The rule is applicable, and the compared direct-source passages agree on the fourth edition.
- **Direct observation versus inference:** The direct page supports BSID-IV/fourth edition. The registered edition conflict arose from an extraction/transcription error.
- **Remaining human question:** Can a human confirm the fourth-edition wording and retain this ID solely as an audit trail for the corrected transcription?
- **State:** Pending Human Adjudication

## C006 — Registered first-interim-alpha discrepancy is not reproduced on direct-source recheck

- **Category:** Statistical reporting inconsistency
- **Checker provenance:** NUM-CAND-006; CROSS-CAND-002.
- **Exact source locations:** DOC-002, PDF p. 29; DOC-004, PDF pp. 26-28.
- **Printed evidence:** Direct rendered-page recheck shows both DOC-002 p. 29 and DOC-004 p. 26 print the first-look alpha as `0.000015`, followed by `.0030`, `.0183`, and `.0440`. The earlier protocol transcription of `0.00015` is not present on the cited page.
- **Consistency rule:** The same planned interim look should have one nominal alpha. The rule is applicable, and the direct sources agree at `0.000015`; no tenfold source difference remains.
- **Direct observation versus inference:** Direct-page agreement is authoritative. The registered discrepancy arose from broken-font extraction/transcription.
- **Remaining human question:** Can a human confirm both direct-page alpha strings and retain this ID solely as an audit trail for the corrected transcription?
- **State:** Pending Human Adjudication

## C007 — Final primary-analysis alpha differs between the article and prospective documents

- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** CROSS-CAND-003.
- **Exact source locations:** DOC-001, PDF p. 3 and Table 2 on p. 7; DOC-002, PDF p. 29; DOC-004, PDF p. 26.
- **Printed evidence:** The article states primary alpha `.049`; the protocol and SAP state final alpha `.0440` for the sequential framework.
- **Consistency rule:** A matched final primary-analysis significance threshold should be traceable to one spending rule or documented recalculation; the printed thresholds differ by `.005`.
- **Direct observation versus inference:** The thresholds are direct. A recalculated Lan-DeMets boundary at realized information or an amendment could explain the difference, but neither is supplied.
- **Remaining human question:** What information fraction, amendment, or boundary output produced `.049`, and how does it reconcile with the printed `.0440` plan?
- **State:** Pending Human Adjudication

## C008 — Trial center count differs between final and prospective documents

- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** CROSS-CAND-004.
- **Exact source locations:** DOC-001, PDF p. 1; DOC-002, PDF p. 29; DOC-004, PDF p. 8.
- **Printed evidence:** The final article states `17` US centers; the protocol and SAP state `15` centers.
- **Consistency rule:** A matched trial-setting count should agree or be explicitly time/version qualified. The displayed difference is 2 centers.
- **Direct observation versus inference:** The counts are direct. Later activation of two sites is plausible but not documented in the supplied package.
- **Remaining human question:** How many centers enrolled participants, and should the prospective documents or final report identify the timing/version basis for 15 versus 17?
- **State:** Pending Human Adjudication

## C009 — Table 3 RR label conflicts with a stated common-OR approximation

- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** STAT1-CAND-001; canonical relationship S019.
- **Exact source locations:** DOC-001, PDF p. 8, Table 3 row `Additional open-label surfactant` and footnote g.
- **Printed evidence:** The row reports `RR: 0.69 (0.33 to 1.46)`, while footnote g says relative risk was estimated by Mantel-Haenszel methods, `approximated by the common OR`, after robust-Poisson nonconvergence.
- **Consistency rule:** Relative risk and common odds ratio are distinct measures; the reported estimator/approximation and label should be unambiguous.
- **Direct observation versus inference:** The wording conflict is direct. The crude risk ratio from `13/312` versus `18/299` is about `0.69`, but that diagnostic does not establish the stratified estimator.
- **Remaining human question:** Is the printed estimate a Mantel-Haenszel relative risk or a common-OR approximation, and which effect label should accompany it?
- **State:** Pending Human Adjudication

## C010 — eTable 3 relative-risk header conflicts with odds-ratio approximation footnote

- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** STAT1-CAND-002; canonical relationships S053 and S054.
- **Exact source locations:** DOC-005, PDF pp. 5-6, eTable 3 effect-estimate header and footnote b.
- **Printed evidence:** The column is headed `Relative Risk (95% CI) or P-value`; footnote b says marked low-prevalence rows use the crude unadjusted odds ratio with exact 95% confidence intervals as an approximation. Marked examples include `0.73 (0.16, 3.28)`, `0.65 (0.11, 3.90)`, and `2.64 (0.69, 10.05)`.
- **Consistency rule:** Relative risk and odds ratio are distinct effect measures; rows using an OR approximation should have an unambiguous measure label.
- **Direct observation versus inference:** The header and footnote wording are direct. Rare-event counts support why an approximation may have been chosen but do not determine the intended reported label.
- **Remaining human question:** Were the marked estimates intended to be reported as odds ratios or explicitly labelled approximations to relative risks, and should the row/header/footnote labelling be clarified?
- **State:** Pending Human Adjudication

## Duplicate-Merge Record

- C001 merges NUM-CAND-001, CROSS-CAND-001, and STAT1-CAND-003 because all concern the same DOC-005 eTable 4 abbreviation line, comparator, and measure-label rule.
- C002 merges NUM-CAND-002 with CROSS-CAND-005; C003 merges NUM-CAND-003 with CROSS-CAND-006; C006 merges NUM-CAND-006 with CROSS-CAND-002.
- CROSS-CAND-007 is intentionally split into C004 and C005 because the GMFCS threshold and cognitive-instrument edition are different printed statements, comparators, and consistency rules.
- STAT1-CAND-001 and STAT1-CAND-002 remain separate as C009 and C010 because they concern different tables, estimators, and source locations.

**Stable candidate count:** 10. The count is an observed result of complete discovery, not a limit or target.
