# Workflow 1.6.2 Candidate Ledger

Pending Human Adjudication. Discovery began from supplied sources and reusable extraction, followed by complete mapping and independent screening. One issue is registered after the initial screen; there is no count target. IDs are permanent.

## Classification table

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R, P_P | PLAN DOC-002 protocol and DOC-003 SAP vs REPORT DOC-001 main article; PLAN vs PLAN | reproduced | CONFIRMED | F-XS-001 |

## C001 — Primary outcome hierarchy differs across supplied plan clauses and the report

Pending Human Adjudication.

**Candidate statement:** Broad primary-endpoint descriptions in protocol §§3.9 and 7.2 include specificity and ROC AUC, with §7.2 referring to both immunochemical assays, whereas other protocol sections, the SAP and the report identify quantitative FOBGold sensitivity as primary and the other metrics as secondary. The report explicitly does not present AUC results. The supplied hierarchy statements do not reconcile.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol and DOC-003 SAP vs REPORT DOC-001 main article; PLAN vs PLAN

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001

**Checker provenance:** Cross-source F-XS-001 is included; statistical F-ST1-001 independently reproduces the same issue and is screened out as DUPLICATE_OF_INCLUDED, linked to C001. All locations from both findings are retained.

**Qualifying route:** Route A, category 5

**Classification rationale:** The broad protocol primary list conflicts directly with the report's secondary/unreported status, establishing P_R; mutually conflicting protocol clauses and SAP content also establish P_P. P_R takes precedence. The plan is a conflicting comparator, rather than merely corroborating an internal report observation.

**Classification ambiguity:** The detailed endpoint sections and SAP may have governed the narrow hierarchy; the broad clauses may reflect a retained specification. The supplied package does not state a hierarchy amendment or governing-clause precedence. This does not establish which list governed.

**Exact source locations:**

- PLAN [DOC-002 protocol PDF p11 §3.4](../../joi190039supp1_prod.pdf#page=11) and [p22 §6.1](../../joi190039supp1_prod.pdf#page=22): narrow primary and secondary lists.
- PLAN [DOC-002 PDF p13 §3.9](../../joi190039supp1_prod.pdf#page=13), continuing [p14](../../joi190039supp1_prod.pdf#page=14): broader parenthetical primary endpoint.
- PLAN [DOC-002 PDF p28 §§7.1–7.2](../../joi190039supp1_prod.pdf#page=28): narrow primary sensitivity and confirmatory status in §7.1; broad both-assay primary wording in §7.2.
- PLAN [DOC-003 SAP PDF p6 §3.2](../../joi190039supp2_prod.pdf#page=6) and [p8 §5.4 continuation and §5.5](../../joi190039supp2_prod.pdf#page=8): quantitative sensitivity primary, other diagnostic metrics secondary.
- PLAN [DOC-003 PDF p9 §7](../../joi190039supp2_prod.pdf#page=9): disclosed population/missingness changes; no explicit hierarchy amendment.
- REPORT [DOC-001 PDF p1 Main Outcome and Measures](../../jama_brenner_2019_oi_190039.pdf#page=1) and [p3 Outcomes/Statistical Analyses](../../jama_brenner_2019_oi_190039.pdf#page=3): narrow primary hierarchy; secondary analyses exploratory; AUC explicitly unreported.
- REPORT [DOC-001 PDF p4 Primary/Secondary End Points](../../jama_brenner_2019_oi_190039.pdf#page=4): numerical secondary specificity and qualitative-sensitivity results.

**Source evidence:** Protocol §§3.4/6.1 designate FOBGold sensitivity primary and specificity/AUC secondary. The §3.9 primary parenthesis adds specificity and AUC of FOBGold; §7.2 adds sensitivity, specificity and ROC AUC of two immunochemical FOBTs. Protocol §7.1 says primary endpoints are confirmatory. SAP and report retain quantitative sensitivity primary. The report identifies secondary outcomes not presented, including AUC, and regards secondary analyses as exploratory.

**Reported-versus-comparator:** Quantitative specificity is secondary in the report but included in broader protocol primary lists. Qualitative sensitivity and ROC AUC fall within the broad both-assay list but are secondary in the SAP/report; AUC results are explicitly absent. Narrow protocol clauses agree with the report and are retained as alternative source-grounded interpretation.

**Reasoning procedure:** Compare the exact outcome-status lists within one supplied protocol version and between PLAN and REPORT. Preserve the explicit SAP amendments to population and missing timing; neither explicitly reconciles outcome status. Consolidate the repeated hierarchy pattern into one candidate.

**Calculation:** Categorical status comparison; recomputed rounding intervals and relative discrepancy are not applicable. No numeric estimate, interval or P-value conflict is asserted. Both statistical passes separately review all inferential relationships.

**Affected result or extracted value:** Primary/confirmatory versus secondary/exploratory status of quantitative-specificity differences −6.4 percentage points (95% CI −9.6 to −3.2), P<.001, and −3.1 (−5.4 to −0.8), P=.008; qualitative-sensitivity difference 12.7 (0.1 to 24.7), P=.048, and qualitative-specificity difference −8.0 (−11.0 to −4.9), P<.001; and completeness of AUC reporting if the broader primary list governed.

**Why context does not resolve it:** Route A category 5 requires registration of a reproduced outcome-status conflict. Plausible precedence of detailed endpoint sections does not remove the express broader primary language; the package supplies no explicit hierarchy reconciliation.

**Alternative source-grounded interpretations:** Detailed endpoint sections/SAP may establish the intended narrow primary list, while broad synopsis/power wording retains another specification. Alternatively a broader original list may have been narrowed. The package does not identify the mechanism or governing hierarchy, and no actual conclusion change is inferred.

**Mechanical evidence recheck:** Fresh root/evidence_recheck inspected all eleven exact source pages; source and comparator statements matched, rule applicable and categorical discrepancy reproduced; no transcription or classification replacement. Evidence state reproduced.

**Potential downstream evidence impact:** A data extractor could classify specificity or qualitative sensitivity as primary/confirmatory or secondary/exploratory depending on the plan clause selected, and could assess AUC reporting completeness differently. No actual propagation, change in the paper's conclusion, or quantitative correction is asserted.

**Exact human question:** Which prespecified primary outcome hierarchy governed quantitative specificity, qualitative sensitivity/specificity and ROC AUC, and what supplied statement reconciles the broad protocol lists with the narrow endpoint sections/SAP and the report's secondary/exploratory or unreported status?
