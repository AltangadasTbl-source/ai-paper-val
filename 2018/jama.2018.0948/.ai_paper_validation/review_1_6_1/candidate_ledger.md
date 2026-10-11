# Candidate Ledger

Fresh discovery across all 69 direct-source pages and independent inclusion screening produced one stable candidate. Pending Human Adjudication. Candidate identity is fixed; the fresh mechanical recheck and independent audit finalized evidence/classification fields. No prior candidate or classification records were used.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | PLAN protocol pp.10,11,24 vs REPORT main article p.4 and REPORT results supplement p.6 | reproduced | CONFIRMED | F-XS-001, F-ST1-001 |

## C001 — Planned and reported eligibility components of the key secondary deterioration composite differ

Pending Human Adjudication.

**Candidate statement:** The supplied protocol requires both qualifying fluid and vasoactive therapy for the circulatory component and restricts the death component to ward death; the report permits either circulatory therapy and also includes death within one hour after urgent ICU admission. The package does not reconcile these eligibility definitions for the reported significant clinical deterioration event (SCDE) composite.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN protocol pp.10,11,24 vs REPORT main article p.4 and REPORT results supplement p.6
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-001, F-ST1-001
**Classification rationale:** Prospective protocol definitions conflict with reported outcome definitions. Both REPORT documents agree on the retained components; corroboration does not create S_C. The SAP supplies count-model context without a conflicting endpoint predicate. P_R is the sole relationship and maps to protocol_report.
**Classification ambiguity:** A dated endpoint amendment or operational classification document might reconcile these definitions, but none is supplied.

**Exact source locations:**

- PLAN [protocol p.10, main secondary outcome](../../joi180015supp1_prod.pdf#page=10): ward death without DNR and reference to operational Table 5.
- PLAN [protocol p.11, deterioration scale context](../../joi180015supp1_prod.pdf#page=11): early-ICU resuscitation components and death before transfer.
- PLAN [protocol p.24, Table 5 categories 4–7](../../joi180015supp1_prod.pdf#page=24): circulatory conjunction, category eligibility, ward death with no transfer, separate early-ICU CPR/ECMO category.
- REPORT [main article p.4, Study Outcomes](../../jama_parshuram_2018_oi_180015.pdf#page=4): one-or-more composite, vasoactive therapy or fluid boluses, first-hour ICU death.
- REPORT [results supplement p.6, eTable 1 components b and d](../../joi180015supp3_prod.pdf#page=6): fluid and/or vasoactive therapy; ward or first-hour ICU death; intent-to-resuscitate pronouncement without CPR.
- Matching affected REPORT result locations: [abstract p.1](../../jama_parshuram_2018_oi_180015.pdf#page=1), [secondary-result narrative p.6](../../jama_parshuram_2018_oi_180015.pdf#page=6), [Table 3 p.7](../../jama_parshuram_2018_oi_180015.pdf#page=7), [discussion p.9](../../jama_parshuram_2018_oi_180015.pdf#page=9), and [results supplement p.11, eTable 3](../../joi180015supp3_prod.pdf#page=11).

**Source evidence:** Protocol Table 5 circulatory category requires >60 mL/kg intravenous/intraosseous fluid in the preceding 12 hours and an inotrope/vasopressor at transfer or in that window. Category 7 defines no-DNR ward death with no transfer. Report eTable 1 uses and/or for therapies and includes ward or first-hour urgent-ICU death; it permits pronouncement without CPR when there was intent to resuscitate. The main definition agrees on either therapy and first-hour ICU death. Exact fluid-threshold boundary wording is outside this candidate.

**Reported-versus-comparator:** REPORT circulatory F OR V versus PLAN F AND V; REPORT death W OR I versus PLAN W, where W is qualifying ward death and I qualifying first-hour urgent-ICU death. The reported key secondary result is 127 versus 259 events (386 total), at 0.50 versus 0.84 per 1000 patient-days, rate ratio 0.77 (95% CI 0.61–0.97), P=.03. The absolute difference −0.34 (95% CI −0.73 to 0.05) uses the disclosed baseline-omitting model and is not another inconsistency.

**Reasoning procedure:** Read exact operational eligibility predicates, hold the population/window and non-boundary fluid threshold fixed, compare truth conditions, and separately identify what the aggregate data can establish. Circulatory and death-location changes are retained components of one named endpoint-definition issue shared by both checker findings. No numerical effect change is inferred.

**Calculation:** F AND V differs from F OR V for (F,V)=(true,false) or (false,true). The added component subsets are (F minus V) union (V minus F), apart from patients already qualifying through another component. W differs from W OR I outside W. Rounding does not alter conjunctions or death locations. Rates reproduce: 127/251859×1000=0.50425; 259/307584×1000=0.84205; 127+259=386. Individual component overlap and revised counts cannot be calculated from the supplied aggregates.

**Affected result or extracted value:** The prespecified key secondary SCDE eligibility definition attached to 386 events and the reported adjusted rate ratio 0.77 (0.61–0.97), P=.03. An extractor could record the protocol intersection/ward-only definition or the reported union/expanded-death definition with the same estimate.

**Why context does not resolve it:** The prospective operational table explicitly supplies narrower predicates; the report explicitly supplies broader ones. Neither the SAP nor immediate reported context identifies an amendment or a component-level mapping between them. Separate CPR/ECMO eligibility does not guarantee every early ICU death overlapped another component. The observed event totals alone cannot establish which rule was used throughout classification.

**Alternative source-grounded interpretations:** A prospective amendment may have reconciled the definitions; the report may state the consistently implemented operational rule; or overlapping components may have left observed counts unchanged. The package cannot select among these alternatives. No preferred definition or revised estimate is proposed.

**Mechanical evidence recheck:** The fresh rechecker found all ten cited pages, confirmed every predicate and matching result value, reproduced the logical comparison and precision check, and confirmed PLAN versus REPORT roles, P_R and protocol_report. Evidence state reproduced. Component overlaps, operational classification records and a dated amendment remain unavailable; no numerical consequence is established. Complete facts are in verification/evidence_recheck.md.

**Potential downstream evidence impact:** If confirmed by human review, endpoint harmonization or prespecification extraction could differ depending on the component definition attached to the SCDE estimate. No propagation, numerical effect change or changed paper conclusion is established.

**Human verification steps:** Inspect the source pages, operational case-report/adjudication definition and any dated amendment. Identify which circulatory conjunction and death location/window classified the 127 versus 259 events; determine whether component overlaps reconcile the supplied definitions.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
