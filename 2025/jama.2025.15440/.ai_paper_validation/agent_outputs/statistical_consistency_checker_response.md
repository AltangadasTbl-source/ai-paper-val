# Statistical Consistency Checker Response

## Scope and evidence used

- Main article: `jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf`, PDF pages 1-8.
- Results supplement: `joi250068supp3_prod_1760999665.30362.pdf`, PDF pages 1 and 4-11.
- Evidence basis: package manifest, page-linked normalized text/OCR, rendered result pages, `main_text_extractor_response.md`, and `results_supplement_evidence_map.md`.
- Protocol and SAP were not used. No external sources were used.

## Retained local candidate

### SC-01 - Repeated confidence interval for "any stroke" is inconsistent

- **Category:** Statistical reporting inconsistency
- **Status:** Candidate for evidence verification
- **Main-article locations and reported values:**
  - `jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf`, PDF p. 1, structured abstract, Results: stroke in patch **69 (2.7%)** versus usual care **64 (2.5%)**; rate ratio **1.08 (95% CI, 0.76-1.53)**.
  - Same PDF, p. 5, Results: the same event counts, **69 (2.7%)** versus **64 (2.5%)**, and event RR **1.08 (95% CI, 0.77-1.51)**.
  - Same PDF, p. 7, Figure 4B, row "Any stroke": the same counts and rate ratio **1.08 (95% CI, 0.77-1.51)**.
- **Logical basis:** The outcome label, event counts, group denominators (2520 per group), point estimate (1.08), and follow-up horizon (2.5 years) are repeated, but both CI limits differ: **0.76 versus 0.77** and **1.53 versus 1.51**. The article does not identify different analyses or CI methods for the abstract and body repetitions. This is a direct repeated-value comparison and does not rely on confidence-interval symmetry or any unstated model property.
- **Verification instruction:** Visually compare the structured-abstract Results on PDF p. 1 with the Results sentence on p. 5 and Figure 4B on p. 7; confirm that each refers to "any stroke" with 69 versus 64 events and rate ratio 1.08, then determine which CI is intended.

## Checked relationships with no retained issue

- **Estimate versus CI:** Every reported point estimate examined was contained within its stated CI.
- **CI versus null and P value:** Primary AF ratio **1.26 (1.02-1.57), P=.03**; time-to-AF rate ratio **1.29 (1.03-1.61), P=.03**; oral-anticoagulation risk ratio **1.13 (0.98-1.30), P=.08**; oral-anticoagulation time-to-event rate ratio **1.15 (0.99-1.34), P=.07**; and supplementary overall AF ratio **1.21 (1.02-1.45), P=.03** all agree as to whether the null is included.
- **Effect direction:** Main Figure 2, main Figure 4, and supplementary eFigure 1 estimates agree with the corresponding patch/usual-care event proportions.
- **Repeated P values:** Repeated primary AF **P=.03**, time-to-AF **P=.03**, oral-anticoagulation **P=.07**, and supplementary sensitivity-analysis **P=.03** values were consistent across text and figures.
- **Subgroups and labels:** Main Figure 2 age totals reconcile to **172 versus 136**, and sex totals reconcile to the same overall counts; eFigure 1 age and sex totals reconcile to **251 versus 207**. Age and sex labels were consistent. Main heterogeneity values (**age P=.78; sex P=.06**) and supplement values (**age P=.28; sex P=.07**) support the respective "no significant heterogeneity" interpretation.
- **Cross-document distinction:** Main Figure 2 uses primary-care AF only, whereas supplementary eFigure 1 uses primary- or secondary-care AF. Their differing estimates are therefore not treated as repeated-result inconsistencies.
- **Supplement denominators:** eTable 1 and eTable 3 use the explicitly stated denominators **2520 randomized** and **2126 wore/returned**. eTable 2 partitions **2520 = 2126 + 394**; its reported categorical P values were consistent with the displayed counts to the reported precision.

## Rejected or uncertain checks

- **Rejected:** Treating the main Figure 2 and supplementary eFigure 1 estimates as contradictory. The outcome definitions differ explicitly (primary care only versus primary or secondary care).
- **Uncertain / not used:** Confidence-interval symmetry or reconstruction of time-to-event CIs from event totals. The reported methods are model-dependent and the package does not provide the event-time data needed for independent reconstruction.

**Candidate count:** 1
