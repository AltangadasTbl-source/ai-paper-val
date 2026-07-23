# Human Adjudication Report

Scope: supplied local PDFs only; no external sources used. DOC-002 (protocol) and DOC-003 pages 1–3 and 36 were **Not Audited by Design** for scientific findings.

## Scientific Issues

1. **C01 — Participant flow inconsistency — Minor**
   - **Location:** `jama_cinciripini_2024_oi_240036_1716416465.98349.pdf` (DOC-001), PDF p. 6, Figure 2.
   - **Compared values:** 2232 assessed; 1740 excluded; 491 randomized.
   - **Basis:** `2232 − 1740 = 492`, not 491. Listed exclusion subgroups reconcile to 1740.
   - **Verify:** Trace Figure 2 eligibility branches and subtract exclusions from assessed participants.

2. **C02 — Arithmetic inconsistency — Minor**
   - **Location:** `jama_cinciripini_2024_oi_240036_1716416465.98349.pdf` (DOC-001), PDF p. 5, Table “Baseline Measures and Demographics,” Sex rows.
   - **Compared values:** Each n=245 arm reports Female 105 (42.9%) and Male 145 (57.1%).
   - **Basis:** `105 + 145 = 250`; `145 / 245 = 59.2%`, not 57.1%.
   - **Verify:** Sum sex counts within each arm and recompute the male percentage.

3. **C03 — Participant flow inconsistency — Minor**
   - **Location:** `jama_cinciripini_2024_oi_240036_1716416465.98349.pdf` (DOC-001), PDF p. 4 participant-flow prose and p. 6, Figure 2.
   - **Compared statements:** Prose states that 40 CNRT and 35 varenicline participants “did attend rerandomization”; Figure 2 states they “did not attend rerandomization.”
   - **Basis:** Figure totals support nonattendance: `151 + 40 = 191`; `122 + 35 = 157`.
   - **Verify:** Compare the p. 4 sentence with both Figure 2 nonattendance boxes.

4. **C04 — Cross-document inconsistency — Major**
   - **Location:** `jama_cinciripini_2024_oi_240036_1716416465.98349.pdf` (DOC-001), PDF p. 3, Figure 1; `joi240036supp2_prod_1716416466.01349.pdf` (DOC-003), PDF p. 14, E-Figure 1 caption, and pp. 15–18 and 20.
   - **Compared statements:** DOC-001 Figure 1 and later DOC-003 definitions specify CNRT+ with 2-mg lozenges; DOC-003 E-Figure 1 specifies a 4-mg lozenge.
   - **Basis:** The intervention definition differs across supplied exhibits.
   - **Verify:** Compare the E-Figure 1 caption with DOC-001 Figure 1 and the cited supplemental definitions.

5. **C06 — Statistical reporting inconsistency — Minor**
   - **Location:** `jama_cinciripini_2024_oi_240036_1716416465.98349.pdf` (DOC-001), PDF pp. 5 and 7, outcome text/Figure 3; `joi240036supp2_prod_1716416466.01349.pdf` (DOC-003), PDF p. 21, E-Table 4.
   - **Compared values/statements:** Switch is 0/41 (0%); stay is 2/77 (3%). DOC-001 prints −3% but says continuing was worse; E-Table 4 labels switch versus stay but prints +3%.
   - **Basis:** In the stated order, switch minus stay is approximately `0% − 3% = −3%`.
   - **Verify:** Recompute the difference in the displayed order and compare the prose, Figure 3, and E-Table 4 label/value.

6. **C07 — Statistical reporting inconsistency — Minor**
   - **Location:** `joi240036supp2_prod_1716416466.01349.pdf` (DOC-003), PDF p. 8 simulation description and p. 18, E-Table 2.
   - **Compared values:** Under stated `K = 1000` simulations, power is 0.948 at threshold 0.80 and 0.980 at the stricter threshold 0.85.
   - **Basis:** The event meeting 0.85 is nested within the event meeting 0.80; under unchanged simulations, the stricter event cannot occur more often.
   - **Verify:** Compare the first two threshold/power rows with the stated simulation conditions.

7. **C08 — Presentation inconsistency — Major**
   - **Location:** `joi240036supp2_prod_1716416466.01349.pdf` (DOC-003), PDF pp. 10–11 prose, p. 15 E-Figure 2, and p. 35 E-Table 11.
   - **Compared values:** Prose reports 1.0% (7.0%–1.3%); E-Figure 2 reports 5/51, 10% (7%–13%). Prose reports ARD 1.1% (−1.0%–22%); E-Table 11 reports 11% (−1%–22%).
   - **Basis:** The prose values differ by apparent decimal placement from the linked figure and table.
   - **Verify:** Compare each prose value directly with its linked exhibit.

8. **C09 — Presentation inconsistency — Minor**
   - **Location:** `jama_cinciripini_2024_oi_240036_1716416465.98349.pdf` (DOC-001), PDF pp. 6–7, Figure 2/outcome text; `joi240036supp2_prod_1716416466.01349.pdf` (DOC-003), PDF pp. 9–10 and pp. 15–16, E-Figures 2–3.
   - **Compared values:** Prose uses n=42 for varenicline continuation; E-Figures 2–3 use 0/77.
   - **Basis:** Figure 2 shows 42 rerandomized plus 35 nonattenders assigned to continuation: `42 + 35 = 77`.
   - **Verify:** Trace both continuation branches in Figure 2 and compare the resulting denominator with prose and E-Figures 2–3.

9. **C10 — Presentation inconsistency — Minor**
   - **Location:** `joi240036supp2_prod_1716416466.01349.pdf` (DOC-003), PDF pp. 22–24, E-Table 5; `jama_cinciripini_2024_oi_240036_1716416465.98349.pdf` (DOC-001), PDF p. 7.
   - **Compared statements/values:** E-Table 5 states no adverse-event differences exceeded 2% except nausea; displayed absolute differences exceed two points for pruritus (2.84), skin rash (3.65), headache (3.25), and concentration impairment (2.44). DOC-001 adds “with nonoverlapping CrIs.”
   - **Basis:** The supplemental statement omits the qualifying condition present in the main article.
   - **Verify:** Recompute the cited row differences and compare the supplement preamble with the complete main-article statement.

Excluded from the scientific list: C05 was rejected by the critic as insufficiently supported.

## AI Training Restriction Summary

| Document ID | Source PDF | Status | Exact evidence location and quotation | Human Compliance Review |
|---|---|---|---|---|
| DOC-001 | `jama_cinciripini_2024_oi_240036_1716416465.98349.pdf` | No AI Training Restriction Located in Provided Materials | PDF text layer pp. 1–10 (repeated footer); embedded XMP metadata. “© 2024 American Medical Association. All rights reserved.” | No |
| DOC-002 | `joi240036supp1_prod_1716416466.00349.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1; pp. 43–45; targeted text screen pp. 1–45; embedded XMP metadata. No rights or AI-use statement located. | No |
| DOC-003 | `joi240036supp2_prod_1716416466.01349.pdf` | No AI Training Restriction Located in Provided Materials | PDF pp. 1–2; pp. 35–36; targeted text screen pp. 1–36; embedded XMP metadata. No rights or AI-use statement located. | No |

This separate rights screen is not a legal opinion and does not infer permission from silence.

**Submission status:** Human Adjudication
