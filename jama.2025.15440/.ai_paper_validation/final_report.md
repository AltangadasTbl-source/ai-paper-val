# Human Adjudication Report

## Package Manifest

| Document ID | Source | Type | Scientific audit status |
|---|---|---|---|
| doc_001_main_article | [Main article](/C:/Users/juliz/Documents/Document_Agent_Reading/AI_paper_validation_multi_agents_1/jama.2025.15440/jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf) | Main article, 9 PDF pages | Audited: results-relevant PDF pages 1-8 |
| doc_002_protocol | [Protocol](/C:/Users/juliz/Documents/Document_Agent_Reading/AI_paper_validation_multi_agents_1/jama.2025.15440/joi250068supp1_prod_1760999665.28862.pdf) | Protocol, 26 PDF pages | **Not Audited by Design** |
| doc_003_statistical_analysis_plan | [SAP](/C:/Users/juliz/Documents/Document_Agent_Reading/AI_paper_validation_multi_agents_1/jama.2025.15440/joi250068supp2_prod_1760999665.29862.pdf) | Statistical analysis plan, 24 PDF pages | **Not Audited by Design** |
| doc_004_results_supplement | [Results supplement](/C:/Users/juliz/Documents/Document_Agent_Reading/AI_paper_validation_multi_agents_1/jama.2025.15440/joi250068supp3_prod_1760999665.30362.pdf) | Results supplement, 11 PDF pages | Audited: PDF page 1 and pages 4-11; pages 2-3 not audited by design |

## AI Training Restriction Summary

Supplied-materials screen only; not a legal opinion. Package instructions record user/institutional permission for model-mediated processing. That operational authorization does not alter the statuses below.

| Document ID | Status | Exact evidence location | Human Compliance Review |
|---|---|---|---|
| doc_001_main_article | **Explicit AI Training Restriction** | Footer, PDF pages 1-9: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | **Yes — flag retained** |
| doc_002_protocol | **No AI Training Restriction Located in Provided Materials** | Metadata; targeted visual review, PDF pages 1-2 and 25-26. No rights page or training/fine-tuning/model-improvement statement located. | No flag from supplied-materials screen |
| doc_003_statistical_analysis_plan | **No AI Training Restriction Located in Provided Materials** | Metadata; native-text screen, PDF pages 1-24; targeted review, pages 1-2 and 23-24. No rights page or training/fine-tuning/model-improvement statement located. | No flag from supplied-materials screen |
| doc_004_results_supplement | **Explicit AI Training Restriction** | Footer, PDF pages 4 and 8: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | **Yes — flag retained** |

Silence is not treated as permission. The separately named text-and-data-mining language is not equated here with OCR, inference, redistribution, or unmentioned activities.

## Scientific Findings

### C-01 — Minor — Statistical reporting inconsistency

- **Location:** Main article, PDF p. 1, structured-abstract Results; PDF p. 5, final Results paragraph; PDF p. 7, Figure 4B, “Any stroke” row.
- **Compared values:** The abstract reports 69/2520 (2.7%) versus 64/2520 (2.5%), rate ratio 1.08 (95% CI, **0.76-1.53**). The Results text and Figure 4B report the same counts, percentages, denominators, and rate ratio, but 95% CI **0.77-1.51**.
- **Basis:** Both CI limits differ (0.76 vs 0.77; 1.53 vs 1.51) for the same any-stroke comparison and stated 2.5-year time-to-event analysis; no alternative outcome, population, follow-up horizon, or analysis is identified for the abstract value. The point estimate and null-value interpretation are unchanged.
- **Verification:** Compare the final structured-abstract Results sentence (p. 1), final Results paragraph (p. 5), and Figure 4B “Any stroke” row (p. 7); confirm the repeated 69-versus-64 result and determine whether **0.76-1.53** or **0.77-1.51** is intended.

## Rejected and Uncertain Candidates

| ID | Disposition | Category | Location and basis | Verification instruction |
|---|---|---|---|---|
| C-02 | **Rejected** | Participant flow inconsistency | Main article, PDF p. 4, Figure 1. Explicit transitions reconcile: 22,044 − 1,186 = 20,858 and 5,116 − 76 = 5,040. The inferred differences (368,000 − 22,044 = 345,956; 20,858 − 5,116 = 15,742) occur between differently labelled recruitment stages; the source does not claim they must be separately enumerated. | Trace Figure 1 and confirm the two displayed transitions and the estimated 368,000 denominator. |
| FFC-U01 | **Uncertain** | Presentation inconsistency | Results supplement, PDF p. 8, eFigure 1 caption, “The primary outcome of ratio of proportions overall is represented by a diamond.” The figure plots the primary-or-secondary-care sensitivity outcome (overall ratio 1.21 [95% CI, 1.02-1.45]); the main article defines the trial primary outcome as primary-care AF and reports 1.26 [1.02-1.57] (PDF p. 3 Methods; p. 6 Figure 2). “Primary outcome” may instead mean the figure’s overall row. | Ask whether the caption refers to the trial primary outcome; if not, consider “overall estimate” or “sensitivity-analysis outcome.” |

## Human Adjudication Checklist

- Confirm the intended C-01 confidence interval and correct the discordant repeated value.
- Confirm C-02 remains rejected; no external flow-reporting requirement was used.
- Resolve or retain FFC-U01 as uncertain based on the intended eFigure 1 caption meaning.
- Record review of the retained Human Compliance Review flags for doc_001_main_article and doc_004_results_supplement.
- Retain protocol and SAP as **Not Audited by Design** unless a specific comparison is requested.
