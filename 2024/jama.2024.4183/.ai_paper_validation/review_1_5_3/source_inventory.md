# Direct Source Inventory

Inventory scope: every supplied direct PDF, DOC, DOCX, XLS, XLSX, and CSV at the package root or below it, excluding workflow controls and pre-existing audit derivatives. Direct local `file`, `pdfinfo`, and `sha256sum` were used. No DOC, DOCX, XLS, XLSX, or CSV direct source exists.

| Source ID | Package-relative source path | Format | Stable unit type | Units | Direct-source SHA-256 | Source identity and inventory result |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_cinciripini_2024_oi_240036_1716416465.98349.pdf | PDF 1.4 | PDF_PAGE | 10 | f51fd5b8f20a10df81121eb8aa19f1c4defb98d04ad476ce1e60dd95c68a18d1 | Main article; text layer present; all PDF pages 1-10 are direct-source units. |
| DOC-002 | joi240036supp1_prod_1716416466.00349.pdf | PDF 1.3 | PDF_PAGE | 45 | eb73035cb7b875a25b3c955e6f730eb7f6ef88b711b3d18f0296ee3a857ed004 | Protocol; text layer present; all PDF pages 1-45 remain direct-source units under the complete-coverage contract. |
| DOC-003 | joi240036supp2_prod_1716416466.01349.pdf | PDF 1.6 | PDF_PAGE | 36 | 51a06c53356580e94c262ebe16a3efc634ef1130da3ad33c478f97e0eae6f566 | Results supplement; text layer present; all PDF pages 1-36 are direct-source units. |

Unique direct sources: 3. Unique direct-source units: 91 PDF pages. No duplicate direct source was found.

## Integrity comparison with reusable records

The earlier DOC-001 record names SHA-256 `569b993c763876fe9f0497de1d244178bf403e3dc4b172641bc9e951a4dc0a51`, which does not match the current DOC-001 source hash. The earlier DOC-003 record names SHA-256 `47b190307d73e0fba77600f0baef4b3a07aa67d59066a05c42688a47db7c99de`, which does not match the current DOC-003 source hash. Their page-level derivatives are therefore stale and cannot provide reusable scientific coverage. The DOC-002 recorded hash matches its current source, but it has no page extraction or render derivative.
