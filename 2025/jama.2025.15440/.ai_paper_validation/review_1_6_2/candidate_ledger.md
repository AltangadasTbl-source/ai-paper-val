# Candidate ledger — Workflow 1.6.2

**Status:** Pending Human Adjudication

Discovery was rebuilt from the complete supplied-source maps. Exactly one initial issue was included by the independent screen, in supplied-source order. Stable IDs are never deleted or renumbered. The fresh mechanical rechecker confirmed the source facts, evidence state, review domain and relationships. The mandatory fresh independent quality-control auditor confirmed inclusion, classifications and evidence state; all candidates remain Pending Human Adjudication.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | plan_material | P_P | P_P | PLAN protocol Table 4 affected power cell versus PLAN protocol Table 4 assumptions and all 23 other power cells. | reproduced | CONFIRMED | F-ST1-001 |

## C001 — Age-under-75 subgroup power does not reconcile with a reproducing same-table calculation

**Candidate statement:** Protocol Table 4 prints 34% power for the age-under-75 subgroup at total trial size 5000 and two-sided significance level .01. A continuity-corrected two-proportion reconstruction that satisfies the workflow precision rule for the other 23 power cells gives a central diagnostic power of 28.585280%; its full conservative printed-input enclosure remains below the printed 34% interval.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol Table 4 affected power cell versus PLAN protocol Table 4 assumptions and all 23 other power cells.

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-001

**Qualifying route:** Route A, category 4

**Classification rationale:** The affected power, its numerical inputs and the reproducing comparison cells are prospective PLAN content in one protocol. This is plan-internal, P_P. The report's trial context corroborates the design but is not a conflicting comparator, so it creates no P_R relationship.

**Classification ambiguity:** None for document roles or relationship. The exact Table 4 software/function and underlying correction implementation are not supplied.

**Exact source locations:** [Protocol, PDF p. 22, Table 4](../../joi250068supp1_prod_1760999665.28862.pdf#page=22), age <75 row, rightmost “Power for total of 5000, 2p<0.01” cell; all input and other-power comparison cells in the same Table 4. Contextual design support only: [protocol, PDF p. 20, Table 2](../../joi250068supp1_prod_1760999665.28862.pdf#page=20), continuity-corrected sample-size heading, and [protocol, PDF p. 21, Table 3](../../joi250068supp1_prod_1760999665.28862.pdf#page=21), whole-trial power design.

**Source evidence:** Table 4 age <75 row: population 25%; patch AF 2.52%; active AF at 2.5 years 2.96%; active/control ratio 2.5; implied control AF 1.18%; 90%-power sample sizes 2924 at .05 and 4048 at .01. Powers at total trial 4000/.05, 4000/.01, 5000/.05 and 5000/.01 are 41%, 20%, 52% and 34%. The screen independently inspected the printed cell and same-table comparators visually.

**Reported-versus-comparator:** Printed 34% versus diagnostic 28.585280%. At 4000/.01 the same method gives 20.530754% versus 20%; at 4000/.05 and 5000/.05 it gives 41.851152% and 52.055448% versus 41% and 52%. All other 23 Table 4 power outputs satisfy the precision threshold; all 12 displayed sample-size outputs also track the reconstruction within 1% central discrepancy. No corrected power is assigned.

**Reasoning procedure:** Use equal allocation, subgroup per-arm size m=Tf/2, control and active rates p0 and p1, and the source-grounded continuity-corrected two-proportion normal reconstruction. Establish same-display tracking across every Table 4 power cell, then apply full conservative interval arithmetic for each displayed input and the affected printed power. The source does not identify the exact power implementation; this is an empirically reproducing diagnostic method, not an asserted universal algorithm.

**Calculation:** Let d=p1−p0, A=√[(p0+p1)(1−(p0+p1)/2)], B=√[p0(1−p0)+p1(1−p1)], z=Φ⁻¹(1−α/2). Power (%) = 100{Φ[(√m d−zA−1/√m)/B]+Φ[(−√m d−zA−1/√m)/B]}. At p0=.0118, p1=.0296, T=5000, f=.25, α=.01 and m=625, the diagnostic value is 28.585280%. Allow p0∈[.01175,.01185], p1∈[.02955,.02965], f∈[.245,.255], and conservatively T∈[4999.5,5000.5], while .01 remains the exact decision threshold. Full interval arithmetic gives 27.225013–29.972805%; printed 34% permits [33.5,34.5]%. Minimum gap = 33.5−29.972805 = 3.527195 percentage points; relative discrepancy = 3.527195/34 = .103741 > .05. The narrower endpoint envelope 27.350760–29.844731% likewise remains separated. Allowing rates independently is conservative; imposing the displayed ratio can only narrow the permitted box.

**Affected result or extracted value:** The planned age-under-75 subgroup power at total trial size 5000 and two-sided .01. No discrepancy in the primary reported treatment-effect result or the reported age-80/sex .05 power claim is established by this candidate.

**Why context does not resolve it:** Route A, category 4: a printed result remains separated from the precision enclosure of a method that tracks the other rows/cells of the same display. The unknown exact implementation becomes the human question, rather than an exclusion.

**Alternative source-grounded interpretations:** A cell-specific correction or underlying unprinted rate/subgroup input may account for 34%. An uncorrected normal calculation gives 35.699810%, near 34% under the workflow threshold, but gives 27.416397% at 4000/.01 and does not track the same row's printed 20%. The source does not supply a separate rule for the affected cell.

**Mechanical evidence recheck:** Completed by fresh runtime /root/evidence_rechecker. All cited locations, printed 34%, inputs and 23 power comparators were found and matched against source visuals. The rule and independent full interval calculation reproduce the discrepancy. PLAN/PLAN, P_P and plan_material are confirmed; evidence state is reproduced. No source-transcription or classification correction was required. The outward numerical guard of ±0.00002 percentage point is included in the enclosure reported above; the exact implementation remains unspecified.

**Potential downstream evidence impact:** If a reviewer uses the protocol for design extraction, they could copy 34% as the stated subgroup power. This candidate does not establish any change to observed trial results or downstream conclusions.

**Remaining human question:** Which power calculation and underlying inputs produced the printed 34%, and how do those rules account for the same row's 20% at total trial 4000/.01 and the remaining Table 4 cells?

Registration provenance: statistics_pass_1 /root/statistics_pass1, independently screened by /root/initial_screener. There was no consolidation with another included finding. The cross-source finding F-XS-001 was screened out and receives no stable ID.
