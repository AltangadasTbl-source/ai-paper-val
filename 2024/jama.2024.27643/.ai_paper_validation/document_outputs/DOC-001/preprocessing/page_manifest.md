# DOC-001 Page-Level Preprocessing Manifest

Source PDF: `jama_berry_2025_oi_240158_1742927563.7361.pdf` (unchanged). Native extraction used `pdftotext -layout`; native text was assessed before any rendering. “Usable” means the text layer contains readable article content without missing/sparse/corrupted scientific text. Page images are 200-dpi PNG renders retained only where a flow diagram, figure, or table is needed for later checks.

| PDF page | Content / audit role | Native-text quality | Text used | Render retained | OCR | Source-linked artifacts |
|---:|---|---|---|---|---|---|
| 1 | Article title, abstract | Usable | Native | No | No—native sufficient | `native_pages/page-01.txt` |
| 2 | Introduction / methods | Usable | Native | No | No—native sufficient | `native_pages/page-02.txt` |
| 3 | Methods / analysis | Usable | Native | No | No—native sufficient | `native_pages/page-03.txt` |
| 4 | Results narrative | Usable | Native | No | No—native sufficient | `native_pages/page-04.txt` |
| 5 | Figure 1 participant flow | Usable but layout-intensive | Native | Yes—flow diagram | No—native sufficient | `native_pages/page-05.txt`; `page_images/page-05.png` |
| 6 | Table 1; results narrative | Usable | Native | Yes—Table 1 | No—native sufficient | `native_pages/page-06.txt`; `page_images/page-06.png` |
| 7 | Figure 2; Table 2 | Usable | Native | Yes—figure and table | No—native sufficient | `native_pages/page-07.txt`; `page_images/page-07.png` |
| 8 | Figure 3; results narrative | Usable | Native | Yes—figure | No—native sufficient | `native_pages/page-08.txt`; `page_images/page-08.png` |
| 9 | Discussion | Usable | Native | No | No—native sufficient | `native_pages/page-09.txt` |
| 10 | Discussion / author information | Usable | Native | No | No—native sufficient | `native_pages/page-10.txt` |
| 11 | References | Usable | Native | No | No—native sufficient | `native_pages/page-11.txt` |
| 12 | References / end matter | Usable | Native | No | No—native sufficient | `native_pages/page-12.txt` |

Selected audit text range: PDF pp. 1–12. OCR page range: none. Retained image range: PDF pp. 5–8. The combined normalized text preserves `SOURCE PDF PAGE` delimiters in `normalized_text.txt`.
