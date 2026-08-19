# Stable Candidate Ledger

All six records are quality-control candidates and remain **Pending Human Adjudication**. Local observations were merged only when they concern the same printed values, comparator, and consistency rule. No candidate count limit was used.

## C001 — BPAP mortality pooled confidence-interval lower endpoint differs across matched main-article displays

- **Category:** Cross-document numeric inconsistency
- **Relationships:** N004; S001
- **Checker provenance:** CS-001
- **Exact source locations:** [DOC-001 PDF p. 1, abstract](../../jama_wilson_2020_oi_190154.pdf#page=1); [DOC-001 PDF p. 4, Figure 1](../../jama_wilson_2020_oi_190154.pdf#page=4); [DOC-001 PDF p. 5, results narrative](../../jama_wilson_2020_oi_190154.pdf#page=5)
- **Direct source evidence:** The abstract and p. 5 narrative print BPAP versus no-device mortality OR 0.66 (95% CI, 0.51-0.87), while Figure 1 prints the otherwise matched OR 0.66 (95% CI, 0.50-0.87), for 13 studies and 1423 patients.
- **Consistency rule and calculation:** Matched displays of the same pooled effect at two decimals should reproduce the same interval absent a stated analysis or precision distinction; `0.51 - 0.50 = 0.01`.
- **Source-grounded alternative:** A shared unrounded endpoint may have been formatted differently at a rounding boundary; no distinct population, model, follow-up, or confidence level is stated.
- **Exact human question:** Which lower endpoint is intended, and were the figure and summaries produced from the same final pooled result?
- **Status:** Pending Human Adjudication

## C002 — BPAP quality-of-life pooled confidence-interval upper endpoint differs across matched main-article displays

- **Category:** Cross-document numeric inconsistency
- **Relationships:** N011; S005
- **Checker provenance:** NC-001; CS-002; P1-OBS-001; main mapper observation 1
- **Exact source locations:** [DOC-001 PDF p. 1, abstract](../../jama_wilson_2020_oi_190154.pdf#page=1); [DOC-001 PDF p. 5, Figure 4 and results narrative](../../jama_wilson_2020_oi_190154.pdf#page=5)
- **Direct source evidence:** Figure 4 prints BPAP versus no-device quality-of-life SMD 0.16 (95% CI, -0.06 to 0.38), while the abstract and p. 5 narrative print the matched SMD 0.16 (95% CI, -0.06 to 0.39), for 9 studies and 833 patients.
- **Consistency rule and calculation:** Identically labeled displays should repeat the same rounded interval absent a stated distinction; `0.39 - 0.38 = 0.01`.
- **Source-grounded alternative:** The difference could reflect independent display rounding or export from a common unprinted boundary value; the package identifies no distinct analysis.
- **Exact human question:** Which upper endpoint is intended, and was a different rounding or export convention deliberately used?
- **Status:** Pending Human Adjudication

## C003 — Quality-of-life direction label conflicts with the stated standardized direction

- **Category:** Measure, label, or scale inconsistency
- **Relationships:** N011; N015; N020; S005; S053; S054
- **Checker provenance:** NC-003; CS-003; P1-OBS-003; main mapper observation 3
- **Exact source locations:** [DOC-001 PDF p. 3, synthesis methods](../../jama_wilson_2020_oi_190154.pdf#page=3); [DOC-001 PDF p. 5, Figure 4](../../jama_wilson_2020_oi_190154.pdf#page=5); [DOC-001 PDF p. 8, Table 2 footnote b](../../jama_wilson_2020_oi_190154.pdf#page=8); [DOC-003 PDF p. 15, instrument directions](../../joi190154supp2_prod.pdf#page=15)
- **Direct source evidence:** The methods say quality-of-life direction was standardized so higher scores represent better outcomes. Figure 4 places negative SMDs toward “Favors NIPPV” and positive SMDs toward “Favors No NIPPV.” Table 2 footnote b says higher scores indicate worse quality of life. The supplement shows that underlying instruments have mixed native directions.
- **Consistency rule and calculation:** The stated standardized higher-score direction, the sign of the SMD under the chosen group subtraction, the forest-plot favor labels, and the table footnote must express one coherent polarity or explicitly distinguish scale contexts. The printed mappings are `positive standardized score = better`, `positive SMD = favors no NIPPV`, and `higher score = worse`, which cannot all describe one convention without an unstated distinction.
- **Source-grounded alternative:** The footnote may describe selected original instruments and Figure 4 may use a control-minus-intervention subtraction orientation, but neither distinction is stated and the native instruments have mixed directions.
- **Exact human question:** What sign transformations and group-subtraction convention were used, and which Figure 4 favor labels and Table 2 direction footnote were intended for the standardized SMDs?
- **Status:** Pending Human Adjudication

## C004 — High-versus-low intensity CAT confidence interval differs between the main article and supplement

- **Category:** Cross-document numeric inconsistency
- **Relationships:** N031; S024
- **Checker provenance:** CS-004; P1-OBS-005
- **Exact source locations:** [DOC-001 PDF p. 7, other-comparisons narrative](../../jama_wilson_2020_oi_190154.pdf#page=7); [DOC-003 PDF p. 43, eTable 10](../../joi190154supp2_prod.pdf#page=43)
- **Direct source evidence:** For the same one-RCT, 14-patient high- versus low-intensity CAT comparison, both locations print WMD 2.30. The main article prints 95% CI -2.23 to 6.83 and P=.32; eTable 10 prints 95% CI -2.35 to 6.95.
- **Consistency rule and calculation:** Same matched point estimate, contrast, outcome, study, and patient count should have the same rounded CI absent a stated distinct computation; both endpoints differ by `0.12`.
- **Source-grounded alternative:** The two files may reflect different calculation or export versions; neither source states an analysis-set, time-point, or model distinction.
- **Exact human question:** Which interval belongs to the 14-patient CAT result, and do both displays use the same data and calculation?
- **Status:** Pending Human Adjudication

## C005 — Cheung 2010 participant total differs between matched baseline and effectiveness displays

- **Category:** Denominator, proportion, or total inconsistency
- **Relationships:** N027; S020
- **Checker provenance:** CO-001; NC-004; CS-005; P1-OBS-004
- **Exact source locations:** [DOC-003 PDF p. 19, eTable 6](../../joi190154supp2_prod.pdf#page=19); [DOC-003 PDF p. 43, eTable 10](../../joi190154supp2_prod.pdf#page=43); [DOC-001 PDF p. 6, BPAP-versus-CPAP narrative](../../jama_wilson_2020_oi_190154.pdf#page=6)
- **Direct source evidence:** The Cheung 2010 eTable 6 row lists CPAP 24 patients and BPAP-ST 23 patients, totaling 47. The matched reference-17 BPAP-versus-CPAP effectiveness result in eTable 10 and the main article states 49 patients.
- **Consistency rule and calculation:** Matched study/intervention totals should reconcile or name distinct populations; `24 + 23 = 47` and `49 - 47 = 2`.
- **Source-grounded alternative:** The 49 may be an enrolled, randomized, or outcome-analysis total containing two participants absent from the baseline display; the package does not state that distinction.
- **Exact human question:** What populations do 47 and 49 represent, and is either displayed total a transcription error?
- **Status:** Pending Human Adjudication

## C006 — Final-report meta-analysis model rule differs from the protocol rule for syntheses with 3 through 18 studies

- **Category:** Statistical reporting inconsistency
- **Relationships:** N004; N006; N007; N009; N010; N011; S001; S003; S004; S005; S058
- **Checker provenance:** CS-006
- **Exact source locations:** [DOC-002 PDF p. 11, Data Synthesis](../../joi190154supp1_prod.pdf#page=11); [DOC-001 PDF p. 3, Data Synthesis and Analysis](../../jama_wilson_2020_oi_190154.pdf#page=3); [DOC-001 PDF p. 4, Figures 1 and 2](../../jama_wilson_2020_oi_190154.pdf#page=4); [DOC-001 PDF p. 5, Figures 3 and 4](../../jama_wilson_2020_oi_190154.pdf#page=5)
- **Direct source evidence:** The protocol specifies DerSimonian-Laird random effects for more than 18 studies and DerSimonian-Laird with Knapp-Hartung variance adjustment otherwise. The final article states DerSimonian-Laird random effects except when fewer than 3 studies are included, when fixed-effect Mantel-Haenszel is used. Several printed syntheses contain 3-15 studies.
- **Consistency rule and calculation:** The stated rules assign nonidentical methods to the concrete overlapping range `3 <= k <= 18`, including printed results with k=3, 5, 9, 13, and 15.
- **Source-grounded alternative:** The plan may have been amended, or the article may omit the variance-adjustment detail; no supplied amendment or reconciliation is present.
- **Exact human question:** Which model and variance adjustment were used for each 3-18-study synthesis, and was the protocol rule amended or incompletely described?
- **Status:** Pending Human Adjudication

## Diagnostic retained without stable candidate registration

The HMV mortality OR 0.56 (95% CI 0.29-1.08) with P=.49 is retained as a documented interval-to-P diagnostic in the checker artifacts. A normal approximation from rounded endpoints suggests a different P value, but the package does not provide an exact compatible effect test, variance construction, weights, or continuity rule. It therefore does not meet the source-supplied reproducible-rule threshold for a stable candidate.
