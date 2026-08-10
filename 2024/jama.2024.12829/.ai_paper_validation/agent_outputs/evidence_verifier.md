# Evidence Verifier — Round 1

Verification stage: complete. Candidates reviewed: 10. Results: 10 Verified, 0 Uncertain, 0 Rejected. No second verification round was required.

The verifier checked each item in `candidate_shortlist.md` against the original supplied PDFs. The protocol/SAP and results-supplement pages 3–9 were not used.

| Candidate | Status | Verified basis |
|---|---|---|
| C1 | Verified | Main Table 2 displays incidence difference −0.4 with 95% CI −2.4 to −1.7; the estimate is outside its interval. |
| C2 | Verified | Figure S5 labels AMM N=252, but mRS category counts total 249 and percentages use 249; mRS >2 totals of 4/9 also conflict with Table S11’s identically defined 6/18 disabling-stroke counts. |
| C3 | Verified | Table S6 shows 249/252 headers but 9 (3.9%) uses 233 while 34 (13.5%) uses 252, mixing PPS-like and ITT raw results. |
| C4 | Verified | Table S7 headers are 233/238, while site totals, counts, and percentages reconstruct ITT arm totals of 249/252. |
| C5 | Verified | Table S8 is titled PPS and its body uses 233/238, but its headers show 249/252. |
| C6 | Verified | Table S9 is titled ATS and its body uses 247/254, but headers show 249/252; 8/247 rounds to 3.2%, not the displayed 3.3%. |
| C7 | Verified | Main text gives 258/501 lead-center patients, Table S7 gives 256/501, and Figure S3 shows 258 among the pre-exclusion enrollment population. |
| C8 | Verified | Main text reports arterial perforation 0.4% and cites Table S4, which reports 0 (0.0%). |
| C9 | Verified | All five selected count/percentage pairs fail direct one-decimal recalculation using their displayed and category-confirmed denominators. |
| C10 | Verified | Three Table S11 rows marked chi-square reproduce two-sided Fisher exact P values (.84, .35, .02), not ordinary Pearson chi-square; Fisher is separately identified by another marker. |

## Exact recalculations added during verification

- C1: `100 × (3/249 − 4/252) = −0.382` percentage points.
- C2 AMM Figure S5 counts: `169+58+13+3+3+2+1=249`; mRS >2 totals are 4 BA and 9 AMM.
- C4 reconstructed site-by-arm denominators: Beijing 138/118 and other centers 111/134, totaling 249/252.
- C6: `8/247=3.2%` and `8/249=3.2%` at one decimal.
- C9: `343/501=68.5%`, `77/249=30.9%`, `51/252=20.2%`, `25/249=10.0%`, and `131/215=60.9%`.
- C10 uncorrected Pearson P values: `.710285`, `.253089`, `.013126`; Yates-corrected: `.864965`, `.363360`, `.023139`; two-sided Fisher exact: `.840916`, `.350060`, `.019621`.

Exact source locations, displayed values, logical bases, and human verification instructions are retained in `candidate_shortlist.md`.
