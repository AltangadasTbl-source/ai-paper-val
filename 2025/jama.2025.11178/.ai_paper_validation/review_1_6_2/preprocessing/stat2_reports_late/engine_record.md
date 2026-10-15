# REPORT-late statistical pass2 source/engine record

Agent:/root/stat2_reports_late;model:gpt-6.1-sol;effort:high;start:FRESH_SPAWN. Direct tools followed tooling_record.md: pdfinfo/pdftotext/render/OCR executables absent; pinned temporary PDF fallback available. Compute device:CPU.

New derivatives owned by this shard:

| Source | Exact units | Derivative | Engine/command |
|---|---|---|---|
| joi250046supp3_prod_1755300121.15087.pdf | PDFp2 | preprocessing/stat2_reports_late/doc004_p002.png | PyMuPDF1.26.4,200dpi,CPU; .ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py render SOURCE --page 2 OUTPUT |
| joi250046supp3_prod_1755300121.15087.pdf | PDFp5 | preprocessing/stat2_reports_late/doc004_p005.png | PyMuPDF1.26.4,200dpi,CPU; same helper --page5 |
| joi250046supp5_prod_1755300121.16087.xlsx | xl/workbook.xml | preprocessing/stat2_reports_late/workbook.xml | unzip -p suppliedSOURCE xl/workbook.xml |
| joi250046supp5_prod_1755300121.16087.xlsx | xl/worksheets/sheet1.xml | preprocessing/stat2_reports_late/workbook_sheet1.xml | unzip -p suppliedSOURCE xl/worksheets/sheet1.xml |
| joi250046supp5_prod_1755300121.16087.xlsx | xl/sharedStrings.xml | preprocessing/stat2_reports_late/workbook_sharedStrings.xml | unzip -p suppliedSOURCE xl/sharedStrings.xml |

Current-run renders independently reread: preprocessing/stat1_reports/doc005_p3.png,p4.png,p5.png,p7.png,p8.png,p9.png,p10.png,p13.png,p14.png,p15.png,p16.png (full filenames include doc005_ on every entry); preprocessing/cross_source_review/tidier-3.png andtidier-4.png; preprocessing/stat2_reports_early/doc004_p006.png. These are current supplied-source renders with pinned fallback/CPU engine provenance, not prior scientific conclusions.

Workbook XML decoding used Perl only to select exact cell elements and decode source shared strings; no Office recalculation, extra Python extractor or scientific orchestration was used. Exact worksheet name: `eTable 3`, confirmed from source XML. Selection cellsH12,J12,H18,I18,J18,H20,H39,I39,H41,H43,H45,I47,I51,H52,H54,H58,H60,H66,H68,H72,H74,H81,I81,H84,I84,H87,H100,H101,H102,H105,H108,I108. HeadersH2/I2/J2,A114; populationB3:E3; educationA12:A16;E82/E83/A110 were reread.

Arithmetic diagnostics used JavaScript arithmetic during the direct tool session. They do not select/classify candidates or replace scientific reasoning. For eTable8 half-unit percentage intervals give difference d±.1 and reciprocal100/(d±.1), compared with integer±.5 intervals. For eTable9 diagnostics use printed exact central n/N and half-unit input intervals. For eTable10 the explicitly labeled diagnostic enumerates one-decimal half-unit centers and CI endpoints on.005grid, enforcesc=b−a and symmetric intervals, converts halfwidthh to(h/1.96)^2, cov=(v1+v2−v3)/2, and uses exp(−W/2) for a chi-square2reference; normalcritical/covariance/reference choices are diagnostics only. Printed eTable10 physicalPreadings are feasible, so no new observation depends on this diagnostic.

No source or pre-existing derivative changed. No OCR was needed for this shard's exact comparisons. The coordinator retains responsibility for fallback removal and canonical merges.

