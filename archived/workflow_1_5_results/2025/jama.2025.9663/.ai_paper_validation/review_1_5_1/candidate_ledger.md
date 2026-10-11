# Stable Candidate Ledger

All entries are quantitative quality-control candidates and remain **Pending Human Adjudication**. The three stable IDs below were assigned after merging only genuine duplicates across the numeric, statistical-pass-1, cross-source, and mapper observations. No candidate-count limit was applied.

## C001 — Extraneous pressure unit after the usual-group SpO2 summary

- **Category:** Measure, label, or scale inconsistency
- **Relationships:** N014; S004; S012
- **Exact source locations:** DOC-001 `jama_martin_2025_oi_250042_1753377747.91025.pdf`, PDF p. 6 (printed article p. 403), Oxygen Exposure paragraph; comparator DOC-003 `joi250042supp2_prod_1753377747.93025.pdf`, PDF p. 21, eTable 5.
- **Printed evidence:** DOC-001 pairs conservative SpO2 `93.3% (2.8%)` and PaO2 `71.5 (13.9) mm Hg` with usual-group `95.1% (2.4%) mm Hg` and `79.5 (17.9) mm Hg`, respectively. DOC-003 eTable 5 separately labels SpO2 as percent and PaO2 as mm Hg for the same values.
- **Reproducible rule:** Under the explicit “respectively” pairing, SpO2 carries percent and PaO2 carries mm Hg. The usual-group SpO2 string has both `%` and a trailing pressure unit, unlike its conservative-group counterpart and the supplement table.
- **Direct observation versus inference:** The source unit string is directly observed. A typesetting carryover is a possible explanation only.
- **Alternative source-grounded interpretation:** A reader might visually associate the trailing `mm Hg` with the next PaO2 phrase despite its grammatical placement; eTable 5 supplies the unambiguous pairing.
- **Human question:** Should the `mm Hg` after `95.1% (2.4%)` be removed or repositioned so it applies only to PaO2?
- **Checker provenance:** Main mapper O-001; numeric reviewer Observation 1; statistical pass 1 SP1-O001; cross-source reviewer Observation 1.
- **Status:** Pending Human Adjudication

## C002 — Results-supplement contents page does not identify actual eTables 1–4

- **Category:** Measure, label, or scale inconsistency
- **Relationship:** N032
- **Exact source locations:** DOC-003 `joi250042supp2_prod_1753377747.93025.pdf`, PDF p. 1 contents; actual eTable 1 on PDF p. 15, eTable 2 on p. 17, eTable 3 on p. 18, and eTable 4 on p. 19.
- **Printed evidence:** The contents page calls eTable 1 “Results of quality assessment per study,” eTable 2 “Diagnostic performance of serological tests – test combinations,” eTable 3 “Patients randomized by site,” and eTable 4 “Additional patient characteristics.” The actual same-numbered tables are “Patients randomized by site,” “Additional patient characteristics,” “Representativeness of patients recruited to the UK-ROX trial,” and “Patient baseline characteristics by data collection group,” respectively.
- **Reproducible rule:** A contents entry’s number and title should identify the same-numbered table in the same supplied PDF. The four mismatches share one contents-list identity defect and therefore form one candidate.
- **Direct observation versus inference:** The conflicting table identities are directly observed. An uncorrected template is only a possible explanation.
- **Alternative source-grounded interpretation:** The contents titles may be shifted or retained from another source rather than intended to name the printed UK-ROX tables.
- **Human question:** Should DOC-003 PDF p. 1 be corrected to the actual eTable 1–4 titles and numbering?
- **Checker provenance:** DOC-003 mapper D3-C01; numeric reviewer Observation 2; cross-source reviewer Observation 2.
- **Status:** Pending Human Adjudication

## C003 — Final SAP contains an unresolved reference after quantitative separation/adherence rules

- **Category:** Measure, label, or scale inconsistency
- **Relationships:** N030; N033
- **Exact source location:** DOC-002 `joi250042supp1_prod_1753377747.92525.pdf`, PDF p. 118 (SAP p. 8), immediately after Table 1 and the separation/adherence definition.
- **Printed evidence:** The source states, “See Section 3.2 and Error! Reference source not found. for further details about assessment of separation and treatment adherence,” after numeric traffic-light thresholds and a treatment-deviation definition that includes 22%/23% FIO2 handling.
- **Reproducible rule:** A stated internal reference intended to supply further quantitative definition must resolve to an identifiable section. The error text supplies no target.
- **Direct observation versus inference:** The unresolved reference string is directly observed. The intended section and its content are unavailable and are not inferred.
- **Alternative source-grounded interpretation:** Section 3.2 may supply part of the intended detail, but the additional missing target prevents confirmation that the definition is complete.
- **Human question:** What section or appendix was intended, and does its absence leave any Table 1 separation/adherence quantity insufficiently defined?
- **Checker provenance:** DOC-002 mapper observation on PDF p. 118; numeric reviewer Observation 3; cross-source reviewer Observation 3.
- **Status:** Pending Human Adjudication

