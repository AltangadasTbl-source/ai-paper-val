# Evidence Verifier Response

- Package: `jama.2025.16450`
- Verification stage: one stage completed
- Verification rounds used: one round for each candidate; no second round was needed
- Candidate scope: C-01 through C-05 only
- Sources reviewed: the cited checker responses, the original main-article and results-supplement PDFs, and the retained page-linked images/text
- Excluded by design: protocol, Manual of Operations, SAP, and external sources
- Result: 4 Verified, 0 Uncertain, 1 Rejected

## Summary

| Candidate | Classification | Category | Short basis |
|---|---|---|---|
| C-01 | Verified | Presentation inconsistency | eTable 1 percentages use unstated nonmissing denominators rather than the displayed population sizes. |
| C-02 | Verified | Presentation inconsistency | eTable 3 B+S percentages consistently use 321 although the column is headed n=322 and no alternate denominator is disclosed. |
| C-03 | Verified | Presentation inconsistency | Main Table 1 and Figure 2 give control-arm baseline FIO2 totals of 230 and 231 for the same pretreatment variable. |
| C-04 | Verified | Presentation inconsistency | eTable 4 visibly expands RR as "risk difference" although its header and methods define RR as relative risk. |
| C-05 | Rejected | Proposed arithmetic inconsistency | The comparison treats a mutually exclusive GDB disposition status as equivalent to cumulative all-cause in-hospital death; the supplied notes do not establish that equivalence and show different nonmissing denominators. |

## C-01 - Verified

**Issue:** eTable 1 GDB-status percentages use unstated smaller denominators.

**Location:** `joi250072supp4_prod_1761000786.6988.pdf`, PDF p.2, eTable 1, column headers and "GDB status (up to 120 days postnatal age), n (%)" rows. The complete footnote block is also on PDF p.2.

**Visible source values:**

- Column headers: ITT `n=641`; ITT excluding untreated participants `n=635`; SAF `n=635`; PP `n=617`.
- ITT rows: discharged home `340 (53.9)`, still in hospital `189 (30.0)`, transferred `16 (2.5)`, death `86 (13.6)`.
- ITT excluding untreated rows: `337 (53.7)`, `189 (30.1)`, `16 (2.5)`, `86 (13.7)`.
- SAF rows: `337 (53.7)`, `189 (30.1)`, `16 (2.5)`, `86 (13.7)`.
- PP rows: `329 (53.8)`, `184 (30.1)`, `15 (2.5)`, `84 (13.7)`.
- The visible abbreviation and population footnotes define GDB and the four analysis populations but do not state a nonmissing GDB-status denominator or show a missing/unknown category.

**Calculation and logical basis:**

- ITT: `340 + 189 + 16 + 86 = 631`, which is 10 fewer than 641. `340/631 = 53.9%` after rounding, whereas `340/641 = 53.0%`.
- ITT excluding untreated: `337 + 189 + 16 + 86 = 628`, which is 7 fewer than 635. `337/628 = 53.7%`, whereas `337/635 = 53.1%`.
- SAF: the same row values total 628, again 7 fewer than 635, and use 628 for the percentages.
- PP: `329 + 184 + 15 + 84 = 612`, which is 5 fewer than 617. `329/612 = 53.8%`, whereas `329/617 = 53.3%`.

The calculations reproduce the printed percentages only with the unstated row-sum denominators. The table therefore omits the applicable nonmissing denominators or a missing-status category.

**Human verification instruction:** On Supplement 4 PDF p.2, sum the four GDB-status rows in each population column and recompute the percentages using both the column-header n and the row-sum; then determine whether the table should add nonmissing denominators or a missing/unknown row.

## C-02 - Verified

**Issue:** eTable 3 B+S percentages imply n=321 despite the displayed n=322 header.

**Location:** `joi250072supp4_prod_1761000786.6988.pdf`, PDF p.5, eTable 3, Budesonide + Surfactant column; PDF p.6, continuation and complete eTable 3 notes.

**Visible source values:**

- The Budesonide + Surfactant column is headed `n=322`.
- PDF p.5 reports `242 (75.4)` for Experienced Any AEs, `240 (74.8)` for Any of interest, `214 (66.7)` for Hyperglycemia, and `22 (6.9)` for Any fatal.
- The notes on PDF p.6 define the safety population and monitoring rules but do not give a row-specific or nonmissing denominator for these `n (%)` entries.

**Calculation and logical basis:**

- `242/322 = 75.2%`, but `242/321 = 75.4%`.
- `240/322 = 74.5%`, but `240/321 = 74.8%`.
- `214/322 = 66.5%`, but `214/321 = 66.7%`.
- `22/322 = 6.8%`, but `22/321 = 6.9%`.

All values are rounded to one decimal. The four printed percentages consistently reproduce n=321, not the displayed n=322, and eTable 3 supplies no visible denominator qualification.

**Human verification instruction:** Inspect the eTable 3 header on PDF p.5 and its full notes on PDF p.6, then confirm whether the B+S adverse-event denominator was 321; if so, disclose that denominator or use n/N, otherwise correct the header or percentages.

## C-03 - Verified

**Issue:** The control-arm denominator for baseline FIO2 differs between main Table 1 and Figure 2.

**Location:** `jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf`, PDF p.6 / printed p.1457, Table 1 continuation, "FIO2 at baseline" and "High FIO2 (>=0.5) at baseline"; PDF p.9 / printed p.1460, Figure 2, "Baseline FIO2" subgroup and footnote c.

**Visible source values and statements:**

- Table 1 reports B+S baseline FIO2 `[n=228]` and High FIO2 `86/228 (37.7)`.
- Table 1 reports surfactant-alone baseline FIO2 `[n=230]` and High FIO2 `81/230 (35.2)`.
- Table 1 footnote b states that baseline respiratory metrics report the last available data collected before study-drug initiation.
- Figure 2 reports B+S denominators `142` for FIO2 `<0.50` and `86` for FIO2 `>=0.50`.
- Figure 2 reports surfactant-alone denominators `150` for FIO2 `<0.50` and `81` for FIO2 `>=0.50`.
- Figure 2 footnote c calls this the last known level before treatment initiation and states that the FIO2 subgroups exclude 182 participants from the ITT population because they lack baseline respiratory data.

**Calculation and logical basis:**

- B+S reconciles: `228 - 86 = 142`, and Figure 2 gives `142 + 86 = 228`.
- Surfactant alone does not reconcile: Table 1 implies `230 - 81 = 149` below 0.50, whereas Figure 2 gives 150 below 0.50 and `150 + 81 = 231`.
- Figure 2 totals `228 + 231 = 459`; this also equals `641 - 182 = 459`. Table 1 totals only `228 + 230 = 458`.

The labels and footnotes identify the same pretreatment baseline FIO2 variable and threshold. No visible note explains why the surfactant-alone subgroup contains one more participant in Figure 2.

**Human verification instruction:** Compare main Table 1 on PDF p.6 with the Figure 2 FIO2 rows and footnote c on PDF p.9, then check the subgroup input to determine whether the surfactant-alone `<0.50` denominator should be 149 or 150.

## C-04 - Verified

**Issue:** eTable 4 incorrectly expands RR as "risk difference."

**Location:** `joi250072supp4_prod_1761000786.6988.pdf`, PDF p.7, eTable 4 header and estimate labels; PDF p.8, abbreviation line and methods note. Corroborating internal usage: `jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf`, PDF p.8 / printed p.1459, Table 3 abbreviation line.

**Visible source statements:**

- eTable 4's estimate header is `Relative Risk (RR) or Mean Difference (MD) (95% CI)`.
- Binary rows are labeled `RR`, including Death before 120 days PNA: `RR: 1.09 (0.76, 1.57)`.
- The PDF p.8 methods note states, `Binary outcomes report relative risks, estimated by robust Poisson regression, unless otherwise noted.`
- The abbreviation line on the same page states, `RR = risk difference`.
- Main Table 3 separately defines `RD, risk difference; RR, relative risk`.

**Logical basis:** The eTable 4 header, estimate labels, analysis description, and the main article's abbreviation convention all establish that RR means relative risk. Only the eTable 4 abbreviation line calls RR a risk difference, so that expansion is internally inconsistent.

**Human verification instruction:** Compare the eTable 4 header on Supplement 4 PDF p.7 with the abbreviation and binary-outcome methods lines on p.8; correct the abbreviation to `RR = relative risk`.

## C-05 - Rejected

**Proposed issue:** 120-day death counts differ within the displayed safety population.

**Locations reviewed:** `joi250072supp4_prod_1761000786.6988.pdf`, PDF p.2, eTable 1; PDF pp.7-8, eTable 4 and notes; PDF pp.15-16, eTable 8 and notes.

**Visible source and comparison values:**

- eTable 1, SAF column, reports a four-category `GDB status (up to 120 days postnatal age)` distribution: discharged `337`, still hospitalized `189`, transferred `16`, death `86`. These counts total 628 despite the SAF header n=635.
- eTable 4 reports `Death before 120 days PNA` as `50/321` for B+S and `44/313` for surfactant alone.
- eTable 4's note states that clinical outcomes are assessed through GDB status at 120 days while in hospital, or at prior death, transfer, or discharge, and separately states that death composites consider in-hospital deaths by 120 days PNA.
- eTable 8 is titled `In-hospital Deaths by 120 Days' Postnatal Age, Safety Population`, reports `50/321` and `44/313`, and states that it reports `all-cause, in-hospital deaths through 120 days postnatal age`.

**Calculation:** eTables 4 and 8 give `50 + 44 = 94` deaths among `321 + 313 = 634` participants with nonmissing outcome data. eTable 1 gives 86 participants in the GDB-status category "Death" among 628 displayed status records. The numerical difference is `94 - 86 = 8`.

**Rejection basis:** The candidate requires the eTable 1 disposition category and the eTables 4/8 cumulative death outcome to be equivalent. The supplied pages do not establish that equivalence. Instead, the visible definitions distinguish:

1. a mutually exclusive GDB status distribution that includes transfer and discharge as terminal status categories; and
2. all-cause in-hospital deaths accumulated through 120 days.

The observed subsets also differ: 628 displayed GDB statuses versus 634 participants with a 120-day death value. A participant reaching transfer status can therefore be counted in a different disposition category from a later in-hospital death outcome without an arithmetic contradiction. The aggregate tables do not provide participant-level linkage, so `86` and `94` cannot validly be required to match.

**Human verification instruction:** Compare the eTable 1 GDB-status label and categories on PDF p.2 with the eTable 4 assessment/death-composite note on p.8 and the all-cause in-hospital-death definition on p.15; do not treat 86 and 94 as the same measure without participant-level status-to-death mapping.

## Verification-stage disposition

Advance C-01 through C-04 as Verified findings to the critic. Retain C-05 in the audit trail as Rejected. No candidate requires a second verification round.
