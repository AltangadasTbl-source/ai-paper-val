# Workflow 1.6.1 Candidate Ledger

Pending Human Adjudication. Discovery began from complete source-linked mapping; only independently included issues receive stable IDs. One distinct issue was registered in source order. Stable IDs are never deleted. No scientific disposition or numerical correction is assigned.

## Classification table

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | PLAN protocol pp. 9-10 vs REPORT main pp. 3, 7, 9 and REPORT results supplement pp. 2-3 | reproduced | CONFIRMED | F-XS-001 |

## C001 — Planned cuff-inflation timing anchors differ from reported first-attempt timing anchors

**Candidate statement:** The supplied protocol ends the planned duration at cuff inflation and hypoxemia monitoring one minute after cuff inflation; the reports end duration at blade removal and monitoring one minute after first-attempt completion. The package does not reconcile these written endpoint definitions.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN protocol pp. 9-10 vs REPORT main pp. 3, 7, 9 and REPORT results supplement pp. 2-3
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-001
**Classification rationale:** The conflicting specifications compare prospective trial protocol PLAN content with published main and supplementary REPORT definitions. Both reports agree. The prospective operational form corroborates attempt boundaries and does not independently specify an incompatible endpoint, so no P_P or S_C relationship is added.
**Classification ambiguity:** None

Checker provenance: cross-source F-XS-001; statistical pass-1 F-ST1-001 is screened as DUPLICATE_OF_INCLUDED and supplies the independently stated hypoxemia-window occurrence within the same timing-anchor pattern. The classification Finding IDs cell lists the INCLUDE finding only, as required. All associated locations are retained below.


**Included issue:** Planned cuff-inflation timing anchors differ from reported first-attempt timing anchors.

**Finding provenance and grouping:** F-XS-001 supplies the included duration issue; F-ST1-001 is the duplicate/pattern association to that same included issue and contributes the explicitly stated hypoxemia observation-window locations. Both `C001` cells refer to this one issue; the coordinator assigned C001. The remaining three findings have no candidate association.

**Comparison tier and focus:** These are report-versus-plan secondary endpoint/time-window specifications, including duration and hypoxemia results named in the abstract, and qualify for focus area D. They are not baseline, administrative, or contributor-count comparisons. The proposed review domain is `protocol_report`; primary relationship type and all relationships are `P_R`. The main article and non-plan outcome tables are REPORT; the trial protocol is PLAN. The operational form is PLAN by its prospective content but corroborates an attempt boundary rather than establishing an additional incompatible duration-outcome specification, so it does not add `P_P`. The two report documents agree, so they do not add `S_C`.

**Exact compared source locations:**

- **PLAN:** [Protocol p. 9, section 2.2, lines 304-317](../../joi180054supp1_prod.pdf#page=9) defines first-pass success without hypoxemia and its observation endpoint at one minute after cuff inflation, and time to intubation from the beginning of the attempt to cuff inflation when the tube is in the trachea.
- **PLAN:** [Protocol p. 10, section 3.2, lines 340-347](../../joi180054supp1_prod.pdf#page=10) repeats the cuff-inflation oxygen-monitoring endpoint and specifies stopwatch measurement according to section 2.2.
- **REPORT:** [Main p. 3, Measurements and Trial Outcomes](../../jama_driver_2018_oi_180054.pdf#page=3) describes observation until one minute after the first attempt ends and defines duration from laryngoscope-blade insertion to removal.
- **REPORT:** [Main p. 7, Table 3 and footnotes b/c](../../jama_driver_2018_oi_180054.pdf#page=7) repeats the attempt-completion hypoxemia window and blade-removal duration endpoint; it reports difficult-airway duration medians 39 versus 40 seconds, overall duration medians 38 versus 36 seconds, and first-attempt success without hypoxemia 156/191 versus 123/177 and 317/371 versus 282/366.
- **REPORT:** [Main p. 9, Table 5 and footnote b](../../jama_driver_2018_oi_180054.pdf#page=9) reports hypoxemia 47/371 versus 50/364, with monitoring during or within one minute after attempt completion.
- **REPORT:** [Main p. 1, abstract](../../jama_driver_2018_oi_180054.pdf#page=1) repeats overall duration 38 versus 36 seconds and hypoxemia 13% versus 14%.
- **REPORT:** [Supplement p. 2, eTable 1](../../joi180054supp2_prod.pdf#page=2) repeats the planned duration and success-without-hypoxemia outcome values, and [p. 3, footnotes](../../joi180054supp2_prod.pdf#page=3) repeats the attempt-completion window and blade-removal duration definition.

**All remaining cited locations retained as context:** [Operational form p. 10, Attempt 1 instructions](../../joi180054supp2_prod.pdf#page=10) and [p. 11, Attempt 2 instructions](../../joi180054supp2_prod.pdf#page=11) explicitly define a blade-insertion-to-blade-removal attempt; [main p. 5, duration and time-to-success narrative](../../jama_driver_2018_oi_180054.pdf#page=5), [main p. 8, Figure 2](../../jama_driver_2018_oi_180054.pdf#page=8), and [supplement p. 4, eFigure 1](../../joi180054supp2_prod.pdf#page=4) are the related time-to-success analyses cited by F-ST1-001. Main p. 7 and main p. 5 also show the distinct post hoc successful-first-attempt-only duration of 38 versus 34 seconds. Those additional duration and survival displays are context for the declared first-attempt endpoint; this screen does not infer different hazard ratios, effect estimates, or significance conclusions from them.

**Reproduced source comparison:** For the duration definitions, if blade insertion is b, cuff inflation c, and blade removal r, the protocol specifies c-b and the reports specify r-b; for oxygen monitoring, the protocol explicitly specifies a stop at c+60 seconds while the reports specify one minute after completion of the first attempt. These are source-stated event anchors rather than display-precision differences. The report's duration definition and operational form identify blade removal as its procedural attempt boundary, but the screen does not assume patient-level identity or a numerical separation between c and r. Neither the immediate report definitions nor the protocol measurement section states that the cuff-inflation and attempt-end anchors are equivalent or explains an endpoint amendment.

**Inclusion criteria:** The definitions are reproduced from supplied source pages; their comparison is a focus-D endpoint/time-window specification; immediate context defines each side but does not reconcile the two; and treating the reported 38-versus-36-second duration or 13%-versus-14% hypoxemia result as implementing the protocol's cuff-inflation definition could change the outcome definition recorded in evidence extraction. The timing-window occurrence is supported directly by its own protocol and report clauses, rather than extrapolated solely from the duration clause.

**Bounded interpretation and remaining human question:** The supplied statements support a discrepancy in the written endpoint specifications. They do not establish that a particular duration, hypoxemia event count, composite proportion, hazard ratio, or continuation decision would change, nor do they establish which event actually stopped a stopwatch or oxygen observation in each patient. Which timing anchors produced the reported outcomes, and does an applicable prospective clarification or amendment reconcile them? No preferred analysis or numerical correction is proposed. Any resulting candidate remains Pending Human Adjudication.


**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

Mechanical recheck update: All 13 registered comparison/context pages found and source statements matched. Written-definition comparison reproduced; no transcription or location correction. The domain and sole P_R relationship are confirmed. Actual patient timing, observation implementation and an applicable amendment remain unreported. No numerical effect is inferred. Detailed facts are in [evidence recheck](verification/evidence_recheck.md).

Independent audit update: Inclusion audit CONFIRMED. All four criteria hold for the written definitions and the named result specification a data extractor would record. No new issue or screening repair. Both statistical passes and all checker exclusions were audited; actual numerical consequences remain unestablished. See [quality audit](quality/evidence_quality_audit.md).
