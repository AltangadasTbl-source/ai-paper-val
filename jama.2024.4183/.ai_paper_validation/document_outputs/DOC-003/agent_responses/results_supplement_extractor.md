# Results-supplement evidence map — DOC-003

## Scope and handling

- **Document:** `joi240036supp2_prod_1716416466.01349.pdf` (results supplement; 36 PDF pages).
- **Audited evidence scope:** PDF pp. 4–35 only.  Native text is page-linked at `preprocessing/native_text/page-XXX.txt`; rendered figures/tables are page-linked at `preprocessing/page_images/page-XXX.jpg`.
- **Not Audited by Design:** PDF pp. 1–3 (cover/contents) and p. 36 (references).  DOC-002 is a protocol and is **Not Audited by Design**; it was not opened.
- **Method:** direct native text; no OCR.  Rendered pp. 14–35 were consulted where table/figure layout or plotted labels mattered.  Source PDFs were not changed.
- **Assessment boundary:** this is an evidence extraction only. It makes no error diagnosis or finding.

## Result-supporting analysis material

| Evidence item | Source PDF page(s) | Extracted evidence |
|---|---:|---|
| eAppendix 2 — Sample Size Estimation | 4–5 | Primary outcome selected: 7-day point-prevalence abstinence; initial sample-size estimates used 12-week continuous abstinence because point-prevalence inputs were unavailable. Anticipated cell outcome distributions were modelled rather than single point estimates; Monte Carlo simulations and logistic regression with neutral `N(0, 1000)` coefficient priors were used. E-Figure 1 contains the initial point estimates/95% credible intervals. |
| eAppendix 3 — inverse-probability weighting/model | 5–9 | Phase-1 randomization probability 0.5; Phase-2 abstainers remain on treatment (probability 1); phase-1 non-abstainers are rerandomized continue/increase/switch at 0.33. Stated weights: 2.0 at week 6; 2.0 for week-6 abstainers at week 12; 6.06 for rerandomized non-abstainers at week 12. Models used R 4.3/brms. Initial coefficient priors were `N(0, 1×10^6)` on log scale; after MCMC convergence difficulty, the intercept prior was revised to `N(0, 10)` while treatment-coefficient priors remained unchanged. `K=1000` simulations; prespecified confirmation threshold: `Pr(OR>1 | data)>0.80`. |
| eAppendix 4 — secondary continuous-abstinence results | 9–12 | Secondary outcomes: continuous abstinence (CA) at EOT+30 and 6 months; described as not powered for frequentist differences at these distal time points. Reports E-Figures 2–3, E-Tables 9–11 and detailed group-level values/contrasts (captured below). |
| eAppendix 5 — post-hoc dynamic treatment effects | 12–13 | Post-hoc (not original statistical plan) inverse-probability-weighted/data-augmentation dynamic treatment effects, estimated with frequentist GEE and robust standard errors. E-Table 12 gives point estimates and 95% confidence intervals for week-12 pathway-level abstinence. |

## Participant-pathway denominators and primary-outcome anchors

The supplement uses eight phase-2 analysis cells (E-Table 3, pp. 19–20; E-Figures 2–3, pp. 15–16):

| Phase-1 treatment/status → phase-2 treatment | N |
|---|---:|
| CNRT, abstainer → CNRT | 54 |
| CNRT, non-abstainer → varenicline switch | 51 |
| CNRT, non-abstainer → CNRT continue | 90 |
| CNRT, non-abstainer → CNRT+ increase | 50 |
| Varenicline, abstainer → varenicline | 88 |
| Varenicline, non-abstainer → CNRT switch | 41 |
| Varenicline, non-abstainer → varenicline continue | 77 |
| Varenicline, non-abstainer → varenicline+ increase | 39 |

These sum to 245 in each initial-treatment arm: CNRT `54+51+90+50`; varenicline `88+41+77+39`.  The direct cross-reference targets are main-article Figure 2 (DOC-001 PDF p. 6: phase-2 allocation, losses and primary-analysis denominators) and Figure 3 (DOC-001 p. 7: week-12 7-day point-prevalence outcome cells).  The main article explicitly points to: E-Table 3 for phase-2 demographics (DOC-001 p. 5); E-Table 4 for NNT (p. 5); E-Tables 5–6 for adverse events and E-Tables 7–8 for adherence (p. 7); and eAppendix 4/E-Figures 2–3/E-Tables 9–10 for secondary CA outcomes (p. 7).

## Results evidence by supplemental figure and table

| Exhibit / source page(s) | Evidence extracted |
|---|---|
| **E-Figure 1** (p. 14) | Anticipated 7-day point-prevalence EOT primary-outcome parameters. Phase-1 abstention: CNRT `0.48 (0.38–0.58), Beta(193,210)`; varenicline `0.50 (0.40–0.60), Beta(785,869)`. Week-12 anticipated outcomes: CNRT abstainer→CNRT `0.50 (0.40–0.60)`; CNRT non-abstainer→CNRT `0.02 (0.0007–0.0978)`, →varenicline `0.40 (0.25–0.57)`, →CNRT+ `0.20 (0.10–0.34)`; varenicline abstainer→varenicline `0.75 (0.65–0.83)`; varenicline non-abstainer→varenicline `0.15 (0.05–0.30)`, →CNRT `0.20 (0.15–0.26)`, →varenicline+ `0.40 (0.26–0.55)`. |
| **E-Figure 2** (p. 15) | EOT+30 CA observed cells, `n(abstinent)/N; estimate (95% CrI)`: CNRT abstainer→CNRT `36/54; 67% (58%–75%)`; varenicline abstainer→varenicline `49/88; 56% (48%–63%)`; CNRT non-abstainer→varenicline `5/51; 10% (7%–13%)`, →CNRT+ `4/50; 8% (5%–11%)`, →CNRT `3/90; 3% (2%–5%)`; varenicline non-abstainer→CNRT `0/41; 0% (0%–0%)`, →varenicline+ `3/39; 8% (5%–11%)`, →varenicline `0/77; 0% (0%–0%)`. |
| **E-Figure 3** (p. 16) | Six-month post-target-quit-date CA cells: CNRT abstainer→CNRT `21/54; 39% (30%–48%)`; varenicline abstainer→varenicline `35/88; 40% (33%–47%)`; CNRT non-abstainer→varenicline `2/51; 4% (2%–6%)`, →CNRT+ `3/50; 6% (4%–9%)`, →CNRT `3/90; 3% (2%–5%)`; varenicline non-abstainer→CNRT `0/41; 0% (0%–0%)`, →varenicline+ `1/39; 2% (1%–5%)`, →varenicline `0/77; 0% (0%–0%)`. |
| **E-Table 1** (p. 17) | Simulation-derived cell estimates: phase-1 abstainers: CNRT `0.504 (0.441–0.566)`, VAR `0.749 (0.692–0.801)`; phase-2 non-abstainers: CNRT→CNRT `0.029 (0.017–0.047)`, CNRT→CNRT+ `0.204 (0.160–0.255)`, CNRT→VAR `0.399 (0.343–0.458)`; VAR→VAR `0.159 (0.120–0.203)`, VAR→VAR+ `0.404 (0.347–0.463)`, VAR→CNRT `0.201 (0.157–0.251)`. |
| **E-Table 2** (p. 18) | Simulation power and effect estimates (average point estimate, 95% CI): phase-1 abstainers VAR>CNRT `0.240 (0.160–0.327)`; power for posterior-probability thresholds 0.80/0.85/0.90/0.95: `0.948/0.980/0.974/0.963`. CNRT non-abstainers: VAR switch>CNRT continue `0.370 (0.309–0.431)`, power `0.999/0.999/0.999/0.998`; CNRT+>CNRT continue `0.175 (0.125–0.228)`, `0.964/0.957/0.951/0.939`; VAR switch vs CNRT+ `0.195 (0.119–0.269)`, `0.878/0.863/0.842/0.819`. VAR non-abstainers: VAR+>VAR continue `0.245 (0.172–0.316)`, `0.930/0.922/0.915/0.895`; VAR+ vs CNRT switch `0.202 (0.127–0.288)`, `0.917/0.905/0.890/0.859`. |
| **E-Table 3** (pp. 19–20) | Baseline measures/demographics by the eight pathway cells above. Complete cell-level values are retained in the linked native-text pages. Variables: age; sex; NIH race/ethnicity; employment; education; income/not reported; CO; cigarettes/day; FTCD; years smoking; age at initiation. Exact displayed `Other` race/ethnicity value in the VAR non-abstainer→CNRT column is `4.9 (2)`; all other race/ethnicity values are formatted `n (%)`. Eligibility footnote: CO ≥6 ppm. |
| **E-Table 4** (p. 21) | 7-day point-prevalence EOT ARD (95% lower/upper CrI) and NNT: CNRT abstainer vs VAR abstainer `6% (-4%,16%), NNT 16`; CNRT non-abstainer CNRT+ vs CNRT `6% (2%,11%), 16`; CNRT non-abstainer VAR vs CNRT `6% (2%,10%), 17`; CNRT+ vs VAR `0% (-5%,6%), 378`; VAR non-abstainer VAR+ vs VAR `18% (13%,23%), 6`; VAR non-abstainer CNRT vs VAR `3% (1%,4%), 39`; VAR+ vs CNRT `20% (16%,26%), 5`. Main-article cross-reference: DOC-001 p. 5 and Figure 3, p. 7. |
| **E-Table 5** (pp. 22–25) | Phase-1 adverse-event table: participant event counts plus inverse-probability-weighted estimates and 95% CrIs, by organ system for CNRT versus varenicline. The table states no between-arm AE difference exceeded 2%, except nausea in varenicline, and that estimates are descriptive/no multiple-comparison correction. Exact nausea row: CNRT `17; 7.17 (4.39–10.83)` versus varenicline `54; 22.19 (17.31–27.65)`. Other high-count examples: dreaming abnormal CNRT `35; 14.48 (10.46–19.23)`, VAR `38; 15.7 (11.52–20.58)`; insomnia `20; 8.39 (5.36–12.28)` versus `22; 9.2 (6.02–13.23)`. Complete row-level evidence: native text pp. 22–25 and renders pp. 22–25. Main-article cross-reference: DOC-001 p. 7. |
| **E-Table 6** (pp. 26–30) | Phase-2 adverse-event table: counts, estimates, 95% CrIs for CNRT continue/CNRT+/VAR continue/VAR+. It states comparisons include increased versus respective continuation conditions (among abstainers and rerandomized non-abstainers) and increased conditions versus each other; no AE difference exceeded 2% with non-overlapping CrI; descriptive/no multiple-comparison correction. Complete row-level evidence is retained in native text/renders pp. 26–30. Illustrative exact rows: depression `3;2.25 (0.67–5.28)`, `4;7.87 (2.81–16.46)`, `8;3.97 (1.9–7.1)`, `3;11.01 (3.4–24.33)`; insomnia `4;2.86 (1–6.16)`, `7;12.93 (6.04–22.93)`, `7;3.51 (1.6–6.5)`, `0;2.08 (0.08–10.58)` in table column order. Main-article cross-reference: DOC-001 p. 7. |
| **E-Table 7** (p. 31) | Phase-1 compliance, CNRT N=245/VAR N=245: visit compliance mean (SD) `89 (21)`/`87 (21)`; active varenicline `85 (24)`/`87 (22)` (placebo indicated in opposite arm); active NRT patch `84 (23)`/`84 (23)`; total NRT lozenge median (IQR) `76 (9.75–140)`/`80 (22–135.5)`. Medication data missing/incomplete: 1/245 CNRT and 3/245 VAR. |
| **E-Table 8** (p. 32) | Phase-2 compliance. The printed eight column headers are: CNRT phase-1/abstinent→CNRT `N=54(a)`; CNRT phase-1/non-abstinent→VAR 2 mg `N=51`; →CNRT `N=50(b)`; →CNRT+ `N=50`; VAR 2 mg phase-1/abstinent→VAR 2 mg `N=88(c)`; VAR 2 mg phase-1/non-abstinent→CNRT `N=41(d)`; →VAR 2 mg `N=42(e)`; →VAR+ `N=39(f)`. Visit-compliance means (SD), in that displayed order: `90(19), 86(25), 78(32), 78(31), 92(22), 72(36), 77(31), 79(33)`. Varenicline mean (SD): `85(28)*,82(28),84(26)*,84(26)*,80(32),77(32)*,83(27),87(23)`; NRT-patch: `80(28),77(31)*,77(33),85(25),76(34)*,79(35),84(31)*,85(30)*`; lozenge median (IQR): `40(0–118),65.5(2.5–135)*,59.5(0.25–140),72.2(0–140),12(0–76)*,40(2.5–130),68(3–140)*,40(0–132)*`. Missing/incomplete medication data: `a=3/54, b=2/51, c=7/88, d=1/41, e=2/42, f=1/39`; `*`=placebo. Main-article cross-reference: DOC-001 p. 7. |
| **E-Table 9** (p. 33) | CA ARD (95% CrI) vs respective continuation, with probability of non-zero difference. EOT+30: CNRT→VAR `6% (3%–10%), >99%`; CNRT→CNRT+ `5% (1%–8%), >99%`; VAR→CNRT `0% (0%–0%), 50%`; VAR→VAR+ `8% (5%–11%), >99%`. Six months: `1% (-2%–3%), 66%`; `3% (0%–6%), 96%`; `0% (0%–0%), 50%`; `2% (1%–5%), >99%`, respectively. |
| **E-Table 10** (p. 34) | CA ARD for increase minus switch. EOT+30: CNRT+ vs VAR `-2% (-6%–3%), 79%`; VAR+ vs CNRT `8% (5%–11%), >99%`. Six months: CNRT+ vs VAR `2% (-1%–6%), 89%`; VAR+ vs CNRT `2% (1%–5%), >99%`. |
| **E-Table 11** (p. 35) | Phase-1 abstainers, CNRT versus VAR CA ARD: EOT+30 `11% (-1%–22%), probability 97%`; 6 months `1% (-11%–12%), probability 56%`. |
| **E-Table 12** (p. 35) | Post-hoc frequentist GEE pathway probabilities of week-12 abstinence (95% confidence interval): `VAR,VAR,VAR 0.21 (0.03–0.70)`; `VAR,VAR,CNRT 0.30 (0.04–0.80)`; `VAR,VAR,VAR+ 0.42 (0.05–0.90)`; `CNRT,CNRT,CNRT 0.19 (0.02–0.74)`; `CNRT,CNRT,VAR 0.30 (0.03–0.87)`; `CNRT,CNRT,CNRT+ 0.31 (0.03–0.87)`. The printed nomenclature specifies phase-1 treatment, then phase-2 treatment if abstinent, then phase-2 treatment if non-abstinent. |

## Secondary-outcome prose evidence and printed cross-references

- **Summary values (pp. 9–10):** CNRT phase-1 non-abstainers `n=191`: EOT+30 CNRT+ `8%; n=50` and VAR switch `10%; n=51` versus CNRT continue `3%; n=90`, each stated posterior probability `>99%`; VAR phase-1 non-abstainers `n=157`: only VAR+ `8%; n=39` is stated as providing benefit versus continuation `0%; n=42`. Six-month CA: CNRT+ `3%` and VAR+ `2%` versus respective continuation `0%`, with stated probabilities `96%` and `99%`. Among phase-1 abstainers, EOT+30 CNRT higher than VAR with probability `97%`; no six-month difference stated.
- **Detailed printed text (pp. 10–12):** contains the comparison statements/values reproduced above in E-Figures 2–3 and E-Tables 9–11.  Exact examples retained for source-level comparison: p. 10 describes CNRT non-abstainer EOT+30 switch/ CNRT+/continue probabilities as `1.0% (7.0%–1.3%), 8.0% (5.0%–1.1%), 3.0% (2.0%–5.0%)`, respectively; p. 11 describes CNRT and VAR abstainer EOT+30 values `67% (58%–75%)` and `56% (48%–63%)`, with ARD `1.1% (-1.0%–22%)`; p. 12 describes six-month abstainer values `39% (30%–48%)` and `40% (33%–47%)`, ARD `1.0% (-1.3%–1.1%)`.
- **Printed internal targets:** p. 9 assigns CA switch/increase-vs-continue contrasts to E-Table 9, increase-vs-switch to E-Table 10, and abstainer contrast to E-Table 11.  Later prose at p. 10 directs the phase-1-abstainer comparison to E-Table 10; p. 11 directs one six-month CNRT comparison to E-Table 7. These are recorded as printed cross-references only.

## Extraction count and themes

- **19 labelled result-supporting items extracted:** eAppendices 2–5 (4), E-Figures 1–3 (3), and E-Tables 1–12 (12).
- Themes: design/simulation and IPW support; phase-2 participant pathways and primary outcome; secondary continuous-abstinence analyses; adverse-event frequencies; adherence/compliance; demographics; and post-hoc GEE pathway effects.
