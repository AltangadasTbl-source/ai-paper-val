# Package manifest — initial inventory

Inventory performed from supplied local PDFs only on 2026-07-23. Page counts are from `pdfinfo`; text-layer status is based on successful `pdftotext` extraction. Source PDFs were not changed.

| Document ID | Source PDF | Pages | Text layer | Likely content type | Classification evidence | Initial scientific-audit scope |
|---|---|---:|---|---|---|---|
| DOC-001 | `/home/bulunte/ai-paper-val/jama.2024.4183/jama_cinciripini_2024_oi_240036_1716416465.98349.pdf` | 10 | Available (49,819 extracted characters) | Main article | First-page masthead says “JAMA \| Original Investigation”; title is “Smoking Cessation After Initial Treatment Failure With Varenicline or Nicotine Replacement: A Randomized Clinical Trial.” | Pages 1–10 (entire article). Results evidence includes Table (p5), participant flow Figure 2 (p6), and outcome Figure 3 (p7). |
| DOC-002 | `/home/bulunte/ai-paper-val/jama.2024.4183/joi240036supp1_prod_1716416466.00349.pdf` | 45 | Available (148,208 extracted characters) | Protocol | First-page title is “Protocol 2014-0213”; table of contents lists Background, Objectives, Patient Accrual and Eligibility, Study Design and Procedures, Data Analysis, Protection of Human Subjects, and References. | **Not Audited by Design** (protocol). No result-relevant range selected. May be opened only for a specific parent-requested comparison. |
| DOC-003 | `/home/bulunte/ai-paper-val/jama.2024.4183/joi240036supp2_prod_1716416466.01349.pdf` | 36 | Available (73,312 extracted characters) | Results supplement | First page says “Supplemental Online Content” and lists eAppendices, E-Figures, and E-Tables. TOC identifies secondary-outcome analyses (pp9–13), E-Figures (pp14–16), and outcome/demographic/adverse-event/compliance tables (pp17–35). | Pages 4–35 are conservatively result-relevant. Pages 1–3 are cover/TOC; p36 is references. Within p4, behavioral-counseling text is non-result context, but the page also starts sample-size material. |

## Audit-routing note

DOC-001 and DOC-003 are scientific-audit inputs. DOC-002 is retained for the separate document-level AI-training-restriction screen but is **Not Audited by Design** for the default scientific audit. This inventory does not determine AI-training-restriction status; that requires the dedicated supplied-files rights screen.
