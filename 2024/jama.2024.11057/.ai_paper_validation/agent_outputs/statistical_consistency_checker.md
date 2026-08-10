# Statistical consistency checker — D001 main article and scoped D003 results supplement

## Scope and evidence

- **Main article:** `D001_main_article`, source PDF `jama_graham_2024_oi_240078_1739900423.19074.pdf`, especially PDF source pp. 1 and 4–7 (printed pp. 713 and 716–719), using the main-text evidence map, page-native text, and rendered tables.
- **Results supplement:** `D003_results_supplement`, source PDF `joi240078supp2_prod_1739900423.24574.pdf`, scoped PDF source pp. 4–15, using the supplement evidence map, page-native text, and rendered eTables.
- **Excluded by design:** `D002_protocol` was not opened. D003 pp. 2–3 and 16 were not opened. No web search or external evidence was used.

## Local candidates (3)

### Candidate 1 — Direction of responder/nonresponder associations is reversed for gender and race

- **Allowed category:** Cross-document inconsistency
- **Locations and source statements**
  - D001 main article, PDF source p. 5 / printed p. 717, Results, “Vaping Cessation”: the narrative says that “male gender, Black and multiracial race” were significant predictors of **nonresponse** after Holm adjustment.
  - D003 results supplement, PDF source p. 12, **eTable 4, Comparison of Baseline Characteristics Between 7-Month Non-Responders and Responders**:
    - Gender: nonresponders `n=436` with nonmissing gender and responders `n=1,057`; male `153/436 (35.1%)` among nonresponders versus `475/1,057 (44.9%)` among responders; overall `P-nom=.001`, `P-adj=.025`.
    - Race: nonresponders `n=432` with nonmissing race and responders `n=1,053`; Black `32/432 (7.4%)` versus `120/1,053 (11.4%)`; multiracial `62/432 (14.4%)` versus `213/1,053 (20.2%)`; overall `P-nom=.002`, `P-adj=.034`.
- **Logical basis:** Each named category is less prevalent among nonresponders and more prevalent among responders. Thus the table supports an association in the direction of response—not nonresponse—for male gender, Black race, and multiracial race. Other directions in the same sentence (eg, greater vaping frequency, lower confidence, higher dependence) agree with eTable 4, making a wholesale reversal of the table columns unlikely.
- **Concise verification instruction:** On D003 PDF p. 12, read the column headings and the male, Black, and multiracial rows in eTable 4; compare their direction with the exact “predictors of nonresponse” wording on D001 PDF p. 5.

### Candidate 2 — eTable 4 labels two mean/SD-style summaries as “median (IQR)”

- **Allowed category:** Presentation inconsistency
- **Location and values:** D003 results supplement, PDF source p. 12, **eTable 4**, vaping-related items:
  - “Motivation to quit vaping, median (IQR)”: nonresponder `4.1 (0.8)`, responder `4.1 (0.8)`.
  - “Confidence to quit vaping, median (IQR)”: nonresponder `3.2 (1.1)`, responder `3.5 (1.1)`.
  - Footnote b on the same page defines each response on an integer `1–5` scale.
  - By contrast, neighboring rows display actual median/IQR triples: days per month vaping `30.0 (27.0–30.0)` versus `29.0 (26.0–30.0)`, and concern about health consequences `4.0 (3.0–5.0)` versus `3.0 (3.0–4.0)`.
  - D001 Table 1 (PDF source p. 4 / printed p. 716) also displays motivation and confidence medians as `4.0 (4.0–5.0)` and `3.0 (3.0–4.0)` in each treatment arm.
- **Logical basis:** The two eTable 4 parenthetical entries contain one dispersion value rather than the lower and upper quartiles used by every genuine median/IQR row. In addition, an unweighted median of integer 1–5 responses can only be an observed integer or the midpoint of two integers, not `4.1`, `3.2`, or `3.5` in the displayed pattern. The values are formatted like means (SDs), while the row labels say medians (IQRs).
- **Concise verification instruction:** Inspect the rendered D003 PDF p. 12 and compare the formatting of the four adjacent continuous-item rows; confirm whether the motivation and confidence labels should read “mean (SD)” or whether two quartile endpoints are missing.

### Candidate 3 — “Another race” percentage does not reproduce from Table 1 counts

- **Allowed category:** Arithmetic inconsistency
- **Locations and values**
  - D001 main article, PDF source p. 1 / printed p. 713, Abstract Results, and PDF source p. 4 / printed p. 716, Results: both report `8.7% another race`.
  - D001 PDF source p. 4 / printed p. 716, **Table 1**: race denominators are intervention `n=748` and assessment-only control `n=737`, total nonmissing `1,485`. Counts outside the separately reported Black, White, and multiracial categories are:
    - American Indian/Alaska Native: `11 + 7 = 18`
    - Asian: `16 + 20 = 36`
    - Native Hawaiian/Other Pacific Islander: `3 + 2 = 5`
    - Other: `34 + 35 = 69`
    - Combined: `18 + 36 + 5 + 69 = 128`
- **Calculation:** `128 / 1,485 × 100 = 8.6195%`, which rounds to `8.6%` at one decimal, not `8.7%`. Using the full randomized denominator also does not yield 8.7%: `128 / 1,503 × 100 = 8.5163%`, or `8.5%`.
- **Concise verification instruction:** Sum the four “another race” category counts across both Table 1 arms and divide by the displayed nonmissing race denominator (`748+737`); reconcile the result with the repeated `8.7%` claim.

## Checks with no candidate finding

- **Point estimates versus CIs:** Every displayed D001 Table 2 and D003 eTable 5 rate, rate difference, RR, and OR point estimate lies inside its reported CI.
- **CI/null/P-value relationship:** D001 Table 2 and D003 eTable 5 effect CIs exclude their respective nulls (`0` for differences; `1` for ratios) and are directionally consistent with `P<.001`. The main-text CTP differences `17.0 (95% CI, 13.5–20.5; P<.001)` and `17.9 (11.9–23.8; P<.001)` are likewise internally consistent.
- **Repeated estimates and inference:** Primary missing=vaping values repeat exactly across D001 Table 2 and D003 eTable 5: `37.8%` versus `28.0%`, RD `9.9`, RR `1.35`, OR `1.57`, with the same CIs and `P<.001`; repeated-abstinence values also repeat exactly. D001’s CCA/IPRW RRs, CIs, and P values repeat exactly in D003 eAppendix C/eTable 5.
- **Moderator labels and multiplicity:** D001’s statement of no significant moderators after Holm adjustment agrees with D003 eTable 6, where all adjusted P values are at least `.250`.
- **Counts/percentages:** D001 Table 3 category counts sum to each displayed subgroup denominator, and its reported 24.1% follow-up CTP use is reproduced by `(30+215)/1,016 = 24.114%`.

## Uncertain or rejected alternatives

1. **Uncertain — D003 eTable 3 limiting rates versus the primary missing=vaping rates.** At `OR.miss=+∞`, eTable 3 reports P1 `37.98%` and P0 `28.06%`, whereas D001 Table 2/D003 eTable 5 report `37.8%` and `28.0%` from `287/759` and `208/744`. The supplement describes an imputation model enriched with baseline dependence, so the small difference could reflect model-based marginal estimates rather than a reporting error. Do not advance without confirmation of how P1/P0 were computed.

2. **Uncertain — eTable 5 IPRW OR CI asymmetry.** D003 eTable 5 reports OR `1.92 (95% CI, 1.50–2.24)` for 30-day IPRW. Although the interval is unusually asymmetric on the log scale relative to the other ratio intervals, the package does not state the CI construction in enough detail to make a symmetry check definitive. It excludes the null and agrees with `P<.001`; not advanced.

3. **Uncertain — “3.4% (n=10)” CTP use among baseline-exclusive participants who quit vaping.** D001 PDF p. 7 says `3.4% (n=10)`. Within the Table 3 complete-data subgroup, quitters total `163+115+3+7=288`, giving `10/288=3.47%` (normally 3.5%). However, the prose denominator could include additional participants with known vaping status but incomplete joint e-cigarette/CTP data, so the discrepancy is not verifiable from the displayed table alone.

4. **Rejected — subgroup P values from Table 3 reconstructed with an unstated test.** The package does not identify whether the subgroup P values use a binary dual-abstinence comparison, the full 4-category outcome, or another specified model. Different plausible tests yield different P values, so no document-grounded inconsistency is asserted.

5. **Rejected — CI symmetry checks generally.** The reported logistic and survey-weighted analyses do not specify a uniform interval-construction method sufficient to assume symmetry on the raw or transformed scale. No candidate relies on CI symmetry.

