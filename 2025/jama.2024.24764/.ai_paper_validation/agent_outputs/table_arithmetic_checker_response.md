# Table Arithmetic Checker Response

## Scope and sources

- Checked only result-relevant tables designated in the page-level manifest and evidence maps: main article Tables 1-3 (PDF pp. 5-8; printed pp. 857-860) and Supplement 3 eTables 1-6 (PDF pp. 3-6).
- Did not inspect protocol, SAP, administrative tables, figures, or unavailable underlying data.
- Source PDFs were not changed.

## Candidate issue (1)

### TAC-01 - Table 2 surgeon-level rows exceed the stated participant denominators without a multiple-response explanation

- **Category:** Presentation inconsistency
- **Location:** `jama_atherton_2025_oi_240145_1741627844.85412.pdf`, PDF p. 7 (printed p. 859), Table 2, rows "Level of operating surgeon," "Level of surgeon closing fascia," and "Level of surgeon closing skin."
- **Source values and calculation:** Table 2 is headed "No. of participants (%)" with group denominators iNPWT **n=411** and surgeon's preference **n=410**. Yet the three listed surgeon-level categories sum above these denominators:
  - Operating surgeon: iNPWT **319 + 123 + 4 = 446** (35 above 411); control **318 + 110 + 1 = 429** (19 above 410).
  - Closing fascia: iNPWT **201 + 218 + 26 = 445** (34 above 411); control **193 + 225 + 15 = 433** (23 above 410).
  - Closing skin: iNPWT **115 + 214 + 96 = 425** (14 above 411); control **102 + 241 + 73 = 416** (6 above 410).
- **Reasoning:** The table provides no footnote or other statement that more than one surgeon level may be recorded per participant. Thus, the displayed participant-count header is internally ambiguous: either these are multiple-response data and need explicit labeling, or the row counts need confirmation. This is a presentation issue, not a claim of an erroneous underlying count.
- **Verification instruction:** Confirm the intended recording rule for surgeon roles. If multiple surgeons/levels per operation can be entered, add a clear multiple-response note; otherwise recheck the six category columns against the source tabulation.

## Rejected or unsupported leads

These checks did not yield document-verifiable candidates.

- **Main Table 1 (PDF pp. 5-6): Rejected.** Checked visible category totals and percentage denominators. Examples: sex, **204+207=411** and **186+224=410**; smoking, **220+95+90=405** and **223+70+109=402**, matching each displayed `Total No.`; contamination, **98+175+81+57=411** and **99+176+79+56=410**; ASA class, **29+162+173+43+4=411** and **29+157+178+43+3=410**; skin preparation, **192+56+54+44+34+28+3=411** and **183+62+52+46+32+33+1=409**. Displayed percentages agree with their stated group or local total denominators after rounding.

- **Main Table 2 (PDF p. 7), other count rows: Rejected.** Actual-procedure rows total **411** and **410**; surgical-approach rows total **411** and **410**; blood-loss categories total the displayed local denominators (**274+115+16+2=407**; **249+144+9+4=406**); and skin-closure rows total **411** and **410**. No arithmetic inconsistency identified in those rows.

- **Main Table 3 (PDF p. 8): Rejected.** Event counts, percentages, and direct totals reconcile. Primary SSI: **112/394 - 108/394 = 0.01015**, consistent with displayed absolute difference **0.010**; wound complication grading totals equal the reported affected-participant counts (**53+16+4+0+0=73**; **47+17+7+0+0=71**); and total SAEs **237+259=496**. The table states analyses are adjusted for minimization variables, so adjusted effects are not expected to exactly equal crude differences/ratios and were not treated as discrepancies.

- **Supplement 3 eTable 1 (PDF p. 3): Rejected.** Allocation status sums to group and total denominators: iNPWT **6+404+1=411**, control **8+402+0=410**, total **14+806+1=821**. Dressing rows are explicitly identified as not mutually exclusive.

- **Supplement 3 eTables 2-4 (PDF pp. 3-4): Rejected.** Every displayed total N equals the two group Ns (for example, SF-12 PCS day 30 **235+211=446**; EuroQol day 7 **292+283=575**; health score day 30 **281+250=531**). Displayed total means are consistent with weighted group means at shown precision. Reported mean differences are adjusted model estimates, so direct subtraction of displayed crude means is not a valid inconsistency test.

- **Supplement 3 eTables 5a-5b (PDF p. 5): Rejected.** All visible row and column totals reconcile: iNPWT **64+16+4+0+0=84** and control **59+17+7+0+0=83**; each complication-type row also equals its displayed row total. The table explicitly states that participants can contribute more than one complication type.

- **Supplement 3 eTable 6 (PDF p. 6): Rejected.** The italicized early-only/diary-only counts reproduce the primary-outcome event numerators cited in main Table 3: iNPWT **109 day-30 + 0 early-only + 3 diary-only = 112**; control **107 + 1 + 0 = 108**. Other timepoint rows are overlapping by the table's explicit note and must not be added.

## Result

- **Document-verifiable candidate count:** 1
- **Unsupported leads retained as rejected:** 6
