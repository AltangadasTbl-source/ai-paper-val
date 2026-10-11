# Stable Candidate Ledger

All candidates remain **Pending Human Adjudication**. Stable IDs were assigned only after merging genuine duplicates across the numeric, statistical-pass-1, and cross-source lanes. Similar source neighborhoods were not merged when the compared fields or consistency rules differed.

## C001 — Conflicting economic price-year labels within the protocol

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** [DOC-002 PDF p.16, section 7.2.3](<../../joi250034supp1_prod_1750956984.09018.pdf#page=16>); [DOC-002 PDF p.17, section 8.2](<../../joi250034supp1_prod_1750956984.09018.pdf#page=17>).
- **Direct observation:** The first location says all costs will be presented in 2024/25 dollars; the second says all costs will be presented in 2023/24 dollars. Both describe a payer-perspective, one-year cost-utility analysis and five-year budget-impact analysis and both state that no discounting will be applied.
- **Consistency rule:** A single described economic analysis needs one unambiguous monetary base-year label. Direct comparison gives 2024/25 not equal to 2023/24.
- **Alternative interpretation:** The sections might reflect separately updated conventions or protocol revisions, but the supplied text does not distinguish them.
- **Human question:** Which financial year was prespecified and used, and should either statement be corrected or qualified?
- **Checker provenance:** N054; mapper P-SUP-001; numeric NC-P01; cross-source XSC-001.
- **Status:** Pending Human Adjudication.

## C002 — Primary-composite counting rationale does not reconcile with the displayed endpoint list

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** [DOC-002 PDF p.15, primary-composite list](<../../joi250034supp1_prod_1750956984.09018.pdf#page=15>); [DOC-002 PDF p.16, section 7.2.1](<../../joi250034supp1_prod_1750956984.09018.pdf#page=16>).
- **Direct observation:** The protocol displays ten separate endpoint bullets, then states that there are ten items because outcomes (i) and (viii) each contain two individual components.
- **Consistency rule:** Counting the displayed bullets yields 10. Treating two of those already displayed outcomes as two separately counted components would yield 12 component instances unless a different eight-group scheme is intended and specified.
- **Alternative interpretation:** The explanatory sentence may refer to an unstated eight-group clause structure; “Special Care or Intensive Care” may represent settings within one endpoint. The cross-source checker favored a grouped-clause reading, while the numeric and statistical reviewers found that reading insufficiently specified against the displayed ten-item list.
- **Human question:** What are the authoritative ten components, and which two outcomes, if any, were intended to contain separately counted components?
- **Checker provenance:** N052; mapper P-SUP-002; numeric NC-P02; statistical-pass-1 P-SP1-002; cross-source alternate interpretation recorded under N048-N053.
- **Status:** Pending Human Adjudication.

## C003 — Economic comparator label conflicts with the detailed trial comparison

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** [DOC-002 PDF p.5, intervention/control synopsis](<../../joi250034supp1_prod_1750956984.09018.pdf#page=5>); [DOC-002 PDF p.16, section 7.2.3](<../../joi250034supp1_prod_1750956984.09018.pdf#page=16>); [DOC-002 PDF p.17, section 8.2](<../../joi250034supp1_prod_1750956984.09018.pdf#page=17>).
- **Direct observation:** Section 7.2.3 calls the economic comparison “CS vs standard care.” The detailed economic section instead compares treatment with “SC” against placebo/standard care, and the synopsis defines the active treatment as sildenafil citrate. Elsewhere the protocol uses CS for cesarean section.
- **Consistency rule:** The intervention/comparator label should identify the same comparison across the synopsis and economic-analysis descriptions; CS and SC carry different supplied meanings.
- **Alternative interpretation:** “CS” may be a transposition of “SC” or a locally intended abbreviation not defined at that location. No completed economic result is supplied.
- **Human question:** Is “CS” intended to read “SC,” and what treatment/reference groups were specified for the economic model?
- **Checker provenance:** N054; cross-source XSC-002.
- **Status:** Pending Human Adjudication.

## C004 — Reported no-adjustment statement conflicts with the supplied multiplicity plan

- **Category:** Statistical reporting inconsistency
- **Exact source locations:** [DOC-001 PDF p.4, Statistical Analysis](<../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=4>); [DOC-002 PDF p.20](<../../joi250034supp1_prod_1750956984.09018.pdf#page=20>); [DOC-003 PDF p.12, section 3.2](<../../joi250034supp2_prod_1750956984.11521.pdf#page=12>); [DOC-003 PDF p.25, proposed Table 11](<../../joi250034supp2_prod_1750956984.11521.pdf#page=25>).
- **Direct observation:** The article states that there was no adjustment for multiple testing. The supplied protocol and draft SAP state that adjusted P values for the ten component comparisons will be derived using the Benjamini-Hochberg procedure, and the SAP table shell contains an adjusted-P-value column.
- **Consistency rule:** The reported multiplicity treatment for the same ten component comparisons conflicts with the supplied planned treatment unless a superseding decision or document is identified.
- **Alternative interpretation:** DOC-003 is marked draft v1.2; a final approved SAP, amendment, or documented pre-unblinding decision may have superseded the supplied plan. The raw P values are not thereby arithmetically invalid.
- **Human question:** Which approved analysis-plan version governed these component P values, and were adjusted values derived, omitted, superseded, or replaced?
- **Checker provenance:** S024, S029, S038; statistical-pass-1 P-SP1-001; cross-source XSC-003.
- **Status:** Pending Human Adjudication.

## Registration summary

- Stable candidate count: **4**.
- Stable ID set: C001, C002, C003, C004.
- Every record remains Pending Human Adjudication; no severity, validity, acceptance, exclusion, or correction has been assigned.
