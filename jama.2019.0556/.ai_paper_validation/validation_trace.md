# Validation Stage Trace

| Stage | Agent role | Result |
|---|---|---|
| Package inventory | `package_inventory` | Five PDFs classified; scientific scope limited to the main article and result-relevant supplement pages. |
| AI-use restriction screen | `ai_use_restriction_checker` | Five document-level records completed. Four had no AI-training restriction located; `DOC-005` requires Human Compliance Review for underlying study-data use. |
| PDF preprocessing | `pdf_preprocessor` | Completed with validated `tesseract-cpu`; fresh OCR on 13 selected visual pages; all source SHA-256 values unchanged. |
| Main extraction | `main_text_extractor` | Primary/secondary results and participant-flow evidence extracted; one Table 2 footnote-label candidate identified. |
| Supplement extraction | `results_supplement_extractor` | PDF pp. 16–23 extracted; two presentation candidates identified. |
| Table arithmetic | `table_arithmetic_checker` | Totals and effect-code conversions reconciled; supported three candidates. |
| Figure/flow | `figure_flow_checker` | Screening/randomization/follow-up counts reconciled; supported four candidates. |
| Statistical consistency | `statistical_consistency_checker` | Estimates/CIs/P values and cross-document results reconciled; proposed four candidates including one estimand-label candidate. |
| Evidence verification | `evidence_verifier` | Five deduplicated candidates verified in round 1. |
| Critic | `critic` | One abstract-wording candidate rejected as document-defined ambiguity; four minor findings retained. |
| Report generation | `report_generator` | Human Adjudication report generated from critic-retained findings only. |

Workflow limits observed: 5 candidates sent to verification; 1 verification round; 4 final issues; 1 critic stage.
