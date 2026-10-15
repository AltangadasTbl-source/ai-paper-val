# Statistical pass2 REPORT-early derivative provenance

Fresh runtime /root/stat2_reports_early; gpt-6.1-sol/high. Tooling_record.md records unavailable direct PDF/render tools and an existing package-local fallback environment. Compute device: CPU.

New derivatives use the permitted workflow_1_6_2/scripts/pdf_tools.py render helper via .ai_paper_validation/review_1_6_2/tooling/venv/bin/python, pinned PyMuPDF1.26.4,150dpi,CPU:

| Exact source | Physical page | New derivative |
|---|---:|---|
| joi250046supp4_prod_1755300121.15587.pdf | 2 | preprocessing/stat2_reports_early/doc005_p002.png |
| joi250046supp4_prod_1755300121.15587.pdf | 6 | preprocessing/stat2_reports_early/doc005_p006.png |
| joi250046supp3_prod_1755300121.15087.pdf | 6 | preprocessing/stat2_reports_early/doc004_p006.png |

All three were visually inspected. Other assigned current-source images were inspected from preprocessing/stat1_reports/doc005_p{4,5,7,8,9,10,11,13,14}.png (pinned PyMuPDF1.26.4,200dpi,CPU), preprocessing/numeric_review/main_p004.png, preprocessing/protocol_b_restart/page-56.png and preprocessing/sap_restart/page-{4,19,20}.png, with engines recorded by the current mapper/checker. No image editing/OCR was used in this shard.

Workbook authority is the supplied joi250046supp5_prod_1755300121.16087.xlsx ZIP: `unzip -p` directly read xl/workbook.xml, xl/worksheets/sheet1.xml and xl/sharedStrings.xml. Perl displayed exact targeted cell/shared-string fragments only. Worksheet eTable 3 and B3:E3,H12:J12,H18:J18 were read without recalculation. No workbook-derived PDF page was fabricated. No extra Python script, web input, source modification or previous-run conclusion was used.
