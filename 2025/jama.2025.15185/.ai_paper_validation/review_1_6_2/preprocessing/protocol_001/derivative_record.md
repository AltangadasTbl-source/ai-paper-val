# PR1 derivative provenance

Source DOC-002 physical pp1–24, PLAN. Compute CPU. Tesseract5.5.0 and Poppler26.01.0.

- Initial command for n01–24: `tesseract .ai_paper_validation/review_1_5_1/preprocessing/support_mapper/doc002/page-NN.png .ai_paper_validation/review_1_6_2/preprocessing/protocol_001/page-NN -l eng --psm 3`; stderr `ocr.log`. Completed pp1–20, process exit143 while starting p21.
- Successful remaining-page command n21–24: `OMP_THREAD_LIMIT=1 timeout 45s tesseract .ai_paper_validation/review_1_5_1/preprocessing/support_mapper/doc002/page-NN.png .ai_paper_validation/review_1_6_2/preprocessing/protocol_001/page-NN -l eng --psm 6`; exit0. Total24 text files,62039 bytes. Page13 text unreadable (rotated schedule); p20 table text garbled; source-image mapping used.
- Detail render: `pdftoppm -f 20 -l 20 -r 200 -singlefile -png joi250066supp1_prod_1761597796.4601.pdf .ai_paper_validation/review_1_6_2/preprocessing/protocol_001/page-20-detail`; exit0. Purpose: resolve small historical forest-plot cells.1 fresh render, no new full-document render.
- Source and reused images preserved unchanged. All24 units scientifically mapped in extraction/support_protocol_001.md.
