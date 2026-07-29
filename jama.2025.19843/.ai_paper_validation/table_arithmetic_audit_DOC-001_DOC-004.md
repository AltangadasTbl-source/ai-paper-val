# Table arithmetic/internal-consistency audit — DOC-001 and DOC-004

## Scope and method

Audited only result-relevant tables and directly labelled count displays named in the package manifest and result-evidence maps: DOC-001 Tables 1–3 and Figures 1–3; DOC-004 eTables 1–6 and eFigures 1, 2, 4, and 8 where labelled counts permit reconciliation. Protocol, SAP, and administrative documents were not opened. Percentages were checked against their printed numerator/denominator, allowing 0.1 percentage-point rounding; difference columns were checked against unrounded proportions where applicable.

## Candidate 1 — Figure 2’s displayed risk/event counts exceed the randomized group totals

- **Category:** Presentation inconsistency (internal count relationship)
- **Location:** DOC-001, `jama_combes_2025_oi_250087_1766516490.94011.pdf`, PDF p. 6 (journal p. 65), Figure 2, rows “No. of patients at risk” and “No. of patients with event,” at days 5, 10, and 15.
- **Source values:** randomized totals are levosimendan **N=101** and placebo **N=104** (Table 2 header and Figure 2 day-0 risk row). Figure 2 prints, respectively, at day 5: levosimendan **88 at risk** and **36 with event**; placebo **76 at risk** and **41 with event**. At day 10: **20 + 84** and **37 + 70**. At day 15: **10 + 93** and **19 + 89**.
- **Calculation:** At each time, the printed at-risk count plus printed cumulative “with event” count should not exceed the randomized total, before accounting for any competing events or censoring. Levosimendan: day 5, 88+36=**124** (101+**23**); day 10, 20+84=**104** (101+**3**); day 15, 10+93=**103** (101+**2**). Placebo: day 5, 76+41=**117** (104+**13**); day 10, 37+70=**107** (104+**3**); day 15, 19+89=**108** (104+**4**). This is a count identity, so no rounding tolerance applies.
- **Reasoning:** A risk set and the count of participants already having an event are disjoint in the displayed cumulative-incidence analysis. Adding competing events and the two reported levosimendan censored patients can only further reduce—not repair—the available total. Thus the two printed rows cannot simultaneously be standard cumulative event and at-risk counts for the stated randomized groups.
- **Bounded impact:** This affects the Figure 2 supporting risk/event display, not the Table 2 endpoint totals: Table 2’s primary-outcome partition reconciles (levosimendan 69+15+15+2 censored=101; placebo 71+21+12=104).
- **Human verification:** (1) Inspect the source figure artwork/data export and confirm what “No. of patients with event” is intended to count at each time. (2) Recompute each risk set after removing prior events and censoring. (3) The candidate is resolved if either row is relabelled with a non-disjoint quantity or its values are corrected so that risk + prior events (and competing events/censoring) does not exceed N.

## No additional local candidates identified

- **DOC-001:** Table 1 subgroup totals/printed percentages, Table 2 binary percentages and risk differences, Table 3 percentages/risk differences, Figure 1 allocation totals, and Figure 3 cardiogenic-etiology subtotals reconciled within displayed rounding.
- **DOC-004:** eTable 1 consent strata and their group totals; eTable 3 binary percentages, risk differences, and D30/D60 adjacent endpoint values; eTable 4 daily subgroup denominators; eTable 5 exposure percentages; eTable 6 etiologic subgroup totals; eFigure 1 trajectory totals; eFigure 2 and eFigure 4 terminal at-risk/event relationships; and eFigure 8 serious-adverse-event distributions reconciled. No further document-verifiable arithmetic candidate was found.
