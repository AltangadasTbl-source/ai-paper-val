# Candidate Shortlist for Evidence Verification

The coordinator deduplicated and prioritized checker outputs to the permitted maximum of 10 candidates.

## C01 — Cross-document inconsistency: missing mHealth cluster in prior-attempt table

- DOC-003 p4, eTable 2 lists 17 mHealth sites and omits site 2012; its displayed “Yes” counts sum to 168 across 680 participants.
- DOC-001 p5, Table 1 reports 178/720 mHealth participants with a prior quit attempt.
- DOC-003 p8, eTable 5 identifies site 2012 as an mHealth cluster.
- Basis: 178 − 168 = 10 prior attempts and 720 − 680 = 40 participants absent from eTable 2.

## C02 — Arithmetic inconsistency: site 2008 death percentage

- DOC-003 p9, eTable 6 reports control site 2008 as `5 (7.5)` deaths.
- DOC-003 p8, eTable 5 gives site 2008 denominator 40.
- Basis: 5/40 = 12.5%, not 7.5%.

## C03 — Arithmetic inconsistency: death-cause percentages

- DOC-003 p6, eTable 4 reports usual-care “Drug user” 1 (7.4%) and “Severe pneumonia” 1 (7.4%) with 27 usual-care deaths.
- Basis: 1/27 = 3.7%, not 7.4%; verify all percentages in the table, including smaller rounding discrepancies.

## C04 — Cross-document inconsistency: adverse-event percentages

- DOC-001 p5 reports nausea 23.0% vs 22.3% and diarrhea 7.5% vs 7.5%.
- DOC-003 p15, eTable 10 severity counts sum to nausea 161/699 vs 71/334 and diarrhea 51/699 vs 25/334.
- Basis: nausea 23.0% vs 21.3%; diarrhea 7.3% vs 7.5%.

## C05 — Statistical reporting inconsistency: adverse-event direction reversed

- DOC-001 p5 states dry mouth, irritability, and anxiety were more common in the mHealth group.
- DOC-003 pp15-16, eTable 10 gives irritability 283/699 (40.5%) vs 145/334 (43.4%) and anxiety 233/699 (33.3%) vs 123/334 (36.8%).
- Basis: overall irritability and anxiety occurrence is lower in mHealth, contrary to “more common.”

## C06 — Presentation inconsistency: adverse-event analysis denominator unidentified

- DOC-003 pp15-16, eTable 10 totals 699 mHealth and 334 control for every symptom, without an analysis denominator or missingness note.
- These totals differ from randomized 720/360, complete-case 667/318, and death-excluded 695/333 sets.

## C07 — Statistical reporting inconsistency: “PP” versus complete-case label

- DOC-001 p3 defines a complete-case analysis that discards missing primary outcomes.
- DOC-001 p6, Table 2 labels rows “PP” (per protocol) with denominators 667/318.
- Basis: 720 − 53 = 667 and 360 − 42 = 318, exactly matching the complete-case set; no additional per-protocol criteria are stated.

## C08 — Statistical reporting inconsistency: “intention to treat” label after excluding deaths

- DOC-001 p3 distinguishes primary ITT from a post hoc sensitivity analysis excluding deaths; primary ITT denominators are 720/360.
- DOC-003 p13, eTable 9 is titled “Post-hoc sensitivity analysis (intention to treat) after excluding deaths” with denominators 695/333.
- Basis: 720 − 25 = 695 and 360 − 27 = 333.

## C09 — Cross-document inconsistency: subgroup scheme differs from prespecified list

- DOC-001 p3 prespecifies employment categories active, dependent, and retired; SMS-reading ability is not listed.
- DOC-003 p12, eTable 8 combines dependent or retired and adds Reading SMS Yes/No.
- DOC-001 p5 summarizes both without identifying changed/added analyses as post hoc.

## C10 — Presentation inconsistency: eTable 6 title/body mismatch

- DOC-003 p9, eTable 6 title states “Cluster-wise death rates and unsuccessful TB treatment outcomes.”
- Visible body contains only study arm, site ID, and deaths n(%); no unsuccessful TB-treatment outcome column is shown.

## Verification requirement

For each candidate, inspect the original relevant PDF page(s) and classify as Verified, Rejected, or Uncertain. Record exact file/page/table evidence, source values or statements, calculation/logical basis, and a concise human verification instruction. Do not exceed two rounds per candidate.

