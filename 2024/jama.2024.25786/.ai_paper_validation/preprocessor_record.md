# PDF Preprocessor Record

Native text extraction was attempted first for every source PDF with pypdf. Page-delimited UTF-8 outputs are stored in `preprocessed/`.

| Document ID | Native extraction | Selective render/OCR decision | Scientific routing |
|---|---|---|---|
| DOC-001 | Successful; 11/11 pages yielded text | Source pages 1-11 rendered after the user's explicit full-scope continuation instruction; OCR not indicated | Main-article and cross-document audit completed |
| DOC-002 | Successful; 103/103 pages yielded text | No rendering or OCR; protocol/SAP not required for a triggered comparison | Not Audited by Design |
| DOC-003 | Successful; 26/26 pages yielded text | Render source pages 13-25 for eFigure and eTables; OCR not indicated | Results supplement audit |
| DOC-004 | Successful; 3/3 pages yielded text | No rendering or OCR; administrative content | Not Audited by Design |
| DOC-005 | Successful; 1/1 page yielded text | No rendering or OCR; administrative content | Not Audited by Design |

No source PDF was modified, renamed, moved, uploaded, or overwritten.
