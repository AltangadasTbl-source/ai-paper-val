# Reused evidence-asset inventory

This is a file-level inventory of all 98 eligible pre-existing OCR/native/layout/table-or-workbook extraction/rendered-page/page-manifest/document-record/source-location assets below the existing audit area. No table/workbook extraction exists, and the package has no workbook or CSV source. Legacy candidate, verifier, critic, checker, endetail, and final-report material was not read or used as discovery scope.

Fitness terms: **USABLE** means source-matched and adequate as a locator/transcription aid; **PARTIAL** means only the named units are usable; **STALE** means it can identify the document but cannot satisfy the current complete-coverage contract; **DUPLICATE** means an identical or superseded derivative; **UNREADABLE** means unusable for the stated source unit.

| Asset class and exact paths | Exact source location(s) | Fitness | Coverage / gap and permitted use |
|---|---|---|---|
| Layout native text: `document_outputs/DOC-001/main_layout.txt` | DOC-001 PDF pp. 1-14; 14 form-feed units. | USABLE | Complete reusable page coverage; primary reusable locator for pp. 12-14 and cross-check for pp. 1-11. |
| Page-native text: `document_outputs/DOC-001-main-article/normalized_text/page-001.txt` through `page-011.txt` | DOC-001 PDF pp. 1-11 respectively. | USABLE | One-to-one page coverage, with the manifest reporting high/adequate extraction. Does not cover pp. 12-14; layout asset closes that derivative gap. |
| OCR text and map: `document_outputs/DOC-001-main-article/ocr/page-003.txt`; `page_metadata/page-003.ocr.json` | DOC-001 PDF p. 3. | USABLE | CPU OCR aid for the flow diagram; native text remains preferred. |
| Rendered table image: `document_outputs/DOC-001-main-article/page_images/table_check-07.png` | DOC-001 PDF p. 7, Table 3 area. | USABLE | Targeted visual-table corroboration only; no additional page coverage. |
| Page/source maps: `document_outputs/DOC-001-main-article/page_manifest.md`; `preprocessing_record.md` | DOC-001 PDF pp. 1-11, with stated pp. 12-14 omission. | PARTIAL | Accurate map for named page-native assets; layout text supplies pp. 12-14. |
| Native extraction summary: `document_outputs/DOC-001-main-article/main_text_extraction.md` | DOC-001 PDF pp. 1-11 as stated in its header. | STALE | Reduced, prior-run summary rather than complete unit extraction; not used for discovery or coverage. |
| Layout native text: `document_outputs/DOC-004/supp3_layout.txt` | DOC-004 PDF pp. 1-29; 29 form-feed units. | USABLE | Complete reusable page coverage; primary reusable locator for pp. 28-29 and cross-check for pp. 1-27. |
| Page-native text: `document_outputs/DOC-004-supplement-3-results/normalized_text/page-001.txt` through `page-027.txt` | DOC-004 PDF pp. 1-27 respectively. | PARTIAL | Usable for pp. 1-7 and 9-27. Page 8’s 60-character copyright-only native layer is UNREADABLE; its layout text remains usable and direct-source confirmation is required for any candidate. |
| OCR text and maps: `document_outputs/DOC-004-supplement-3-results/ocr/page-004.txt`, `page-006.txt`, `page-008.txt`, `page-013.txt`, `page-020.txt`; matching `page_metadata/page-004.ocr.json`, `page-006.ocr.json`, `page-008.ocr.json`, `page-013.ocr.json`, `page-020.ocr.json` | DOC-004 PDF pp. 4, 6, 8, 13, and 20. | PARTIAL | CPU OCR aids for sparse pages. Pp. 4, 6, 13, and 20 are usable aids; p. 8 OCR is UNREADABLE for content because it also contains only copyright-level text. |
| Rendered-page/table/figure images: `document_outputs/DOC-004-supplement-3-results/page_images/page-004.png`, `page-006.png`, `page-008.png`, `page-013.png`, `page-020.png`, `table_check-07.png`, `table_check-10.png`, `table_check-21.png`, `figure_render-25.png`, `figure_render-26.png`, `figure_render-27.png` | DOC-004 PDF pp. 4, 6, 8, 13, 20; tables on pp. 7, 10, 21; figures on pp. 25-27. | USABLE | Targeted visual corroboration for named pages; p. 8 image is usable visually even though its OCR/native text is not. |
| Additional rendered pages: `preprocessing/rendered/supp3-03.png`, `supp3-07.png`, `supp3-09.png`, `supp3-10.png` | DOC-004 PDF pp. 3, 7, 9, 10. | USABLE | Targeted visual corroboration. `supp3-10.png` is byte-identical to `table_check-10.png` and is DUPLICATE for that page. |
| Derived page PDF: `document_outputs/DOC-004/supp3-p7.pdf` | DOC-004 PDF p. 7. | USABLE | Single-page visual derivative; auxiliary only. |
| Page/source maps: `document_outputs/DOC-004-supplement-3-results/page_manifest.md`; `preprocessing_record.md` | DOC-004 PDF pp. 1-27, with stated pp. 28-29 omission. | PARTIAL | Accurate map for page-native/OCR assets; layout text supplies pp. 28-29. |
| Legacy source-location map: `document_outputs/DOC-004-supplement-3-results/results_supplement_evidence_map.md` | DOC-004, prior-run selected evidence locations; exact unit scope intentionally not reused. | STALE | Hashed and retained, but not read or used because it may encode legacy selection scope. |
| Duplicate native/layout material: `tmp_rights/supp3.txt` | DOC-004 PDF pp. 1-29. | DUPLICATE | Byte-identical to `document_outputs/DOC-004/supp3_layout.txt`; no independent coverage. |
| Metadata only: `tmp_rights/supp3_metadata.txt`; `preprocessing/ocr_backend.json` | DOC-004 source PDF metadata; prior CPU OCR environment. | STALE | No source-unit extraction; identity/process context only. |
| Document records: `document_outputs/package_manifest.md`; all `ai_training_restriction_record.md`, `completion_record.md`, `initial_document_record.md`, and `preprocessing_record.md` files listed in the hash register below | DOC-001 through DOC-005 as named by each record. | STALE | Identity and prior-process context only. Prior narrowed/default scopes cannot reduce current coverage. The additional `document_outputs/jama_saynorea_2019_oi_190106_1635377898.43062/ai_training_restriction_record.md` is a duplicate identity record. |

## Complete hashed asset register

Every listed file is hashed in `reused_artifact_hashes_before.sha256`; this register repeats the exact path and checksum for auditability.

```text
6c1bba989980c3658508c9a5744f19342bd95c38aa5601508882ffb5050ef9c9  .ai_paper_validation/document_outputs/DOC-001-main-article/ai_training_restriction_record.md
bc92b27adc810b0f1c5e7080950a26786e3d1f326d54751d2c2c54d632e3c124  .ai_paper_validation/document_outputs/DOC-001-main-article/completion_record.md
e48d4c681e18878fdae7af0de1f62e076e97c24ba88a981a38bb869a743ba087  .ai_paper_validation/document_outputs/DOC-001-main-article/initial_document_record.md
699d300cb5aba10809afde525a3e326517a69e579c48e4736133412267734289  .ai_paper_validation/document_outputs/DOC-001-main-article/main_text_extraction.md
ed847488a30a00969c0f7e3108aa762515987459da01d42c987d44de159b3c19  .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-001.txt
6446a296fa910f84e4358330eb41ca5959814ad05044c2d7182f571e7e78318b  .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-002.txt
f5577879a68c65f39be799356336bbb6f875e1709074f2a68f1b7fc2cdf1f69d  .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-003.txt
7d2ca4f7f87ab4863a7873d18024083da12d2bd6eeab08700bce7286492d2af2  .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-004.txt
5848a5d0dd77e17ef708312d9f7152203bbf264584a57f77205b24d8df75a812  .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-005.txt
333aadff78683a772b017d1f356698131e41e2a6e3c5858538892d554a33d989  .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-006.txt
056dc349ff2047fd31dfba27a5ec8fa830b58429ae5b629ee017469ba0d6d7be  .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-007.txt
c820114b92f91ea59bab17f69523d4691f369b878efec871864a4dc89214b400  .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-008.txt
b4011f213f06c11b920c574dbf3839f6522dbe1e5be4623499905e1d93ea97c5  .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-009.txt
ccf727359aefab7c86bf5be5e9a5ed5bd61c232141498084a5fc4f9154c5a684  .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-010.txt
883eb38a43ebae539037845afb3ddc2cf6d3fb9edef928452fbf193dfdce3194  .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-011.txt
f913c14445e2c7f5e318b24cf3699b662d74cd6a47cc9c8249ce606e440af737  .ai_paper_validation/document_outputs/DOC-001-main-article/ocr/page-003.txt
8aec7dd60440dc2489a54cb8b4f5e9e14e73fd5b5ec740651b8d11e8d9761bde  .ai_paper_validation/document_outputs/DOC-001-main-article/page_images/table_check-07.png
dc645a6d2952630b1072ed0ab683e75dddda89f6eff0bc33cd71b4031393887e  .ai_paper_validation/document_outputs/DOC-001-main-article/page_manifest.md
ff97c1ea70185e2d3fae8ed9035963c67244b4c60e631fb7557f1b68cc9bf8da  .ai_paper_validation/document_outputs/DOC-001-main-article/page_metadata/page-003.ocr.json
50b773f8cd51820d64848f948da41634eeaa9c3e762030f7625c98d8b956ea3f  .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing_record.md
dcd1eee66de6321b21635afccc72fce1f2b63d9bb4f297c68886322835aa6079  .ai_paper_validation/document_outputs/DOC-001/main_layout.txt
c8208cec49034cd522b799ec97c3f1ef0897be014352849658572aa6fb6e6553  .ai_paper_validation/document_outputs/DOC-002-supplement-1-protocol/ai_training_restriction_record.md
6e117c3bb091edd2abd51ae262581bfee242950fd34bac21ab846ce755c91e6c  .ai_paper_validation/document_outputs/DOC-002-supplement-1-protocol/completion_record.md
11386588f47f0866337bd24e996ed6a9ef4df26a0e9690ba63b96a38fc73e6e3  .ai_paper_validation/document_outputs/DOC-002-supplement-1-protocol/initial_document_record.md
e634a93ef17fccfda95b51bcb083460ea64d36cf15d6051ee749d84757bcf9d9  .ai_paper_validation/document_outputs/DOC-002-supplement-1-protocol/preprocessing_record.md
11125110afe55d7cbe8347adaa96cfec02db13e3cec93b468a7987ff25a5025f  .ai_paper_validation/document_outputs/DOC-003-supplement-2-sap/ai_training_restriction_record.md
833a222605a9e41fbc3b4c0b26ff52f6d2fa0abe6c61b919455ea085dc61a961  .ai_paper_validation/document_outputs/DOC-003-supplement-2-sap/completion_record.md
c47ec424c7b924b51522b17a0314210a860ec4a7a12b9de4afb1a7a8b5e077f4  .ai_paper_validation/document_outputs/DOC-003-supplement-2-sap/initial_document_record.md
fc0df463d45c9ab4b571049d91f1f1f88d5caf892fc932ea91d69dc33736dd9d  .ai_paper_validation/document_outputs/DOC-003-supplement-2-sap/preprocessing_record.md
f38e5291b6694dc6acf69f88b936e959e3bd797c41e8b9e7a1d375bcdb232669  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/ai_training_restriction_record.md
a02d252b8bf141b3158afc7df5b793dbf90d23459c0ab0c9aedbd2ec4633744e  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/completion_record.md
16bbf5313cff2402f4fbb38c18070fef230d5980650668679941372197aba28b  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/initial_document_record.md
2e625500c976de54db283082ced949d3d69b83374c74904ef08c79fa825381a9  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-001.txt
3583399e66bd26b25cbbc0e093a1586214c2aa894e07978fb0606c55622c2641  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-002.txt
be527d54eddaea5f6e2aee0be993923c2f5af4317afc6c4ce2534c0a842bb7f3  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-003.txt
aaf89bd53dfa27b4a807bb60f2950c386ec4a36168e11dc3ec2dffc1176b9f58  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-004.txt
fa79f17f7e3851910774cb9cdcd5b0aa5337c6a7eac2eb62ba79eacb279a619c  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-005.txt
b92edc173b72254336877699b4df2f3dd3981d9ac2425fc92c38121e4465261c  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-006.txt
2efb1350c670ffcc9ae5009b8acb81261e14933920e6e275022659eae7bd8694  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-007.txt
5ee65f68d5e151f31476dab96e6dc0b3caf3006f95c537ff55a17dd56af69f7a  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-008.txt
43fb72494b9c493669c914afc7591b0a7519fb15cf7ccac4cb2bc494062342fa  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-009.txt
511d5ec73c1edd6454136b396eeebe8a0abab3eb0b6efa97fbfe96dcad760cc7  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-010.txt
b51473a95ff946115dff301d8aa9a7d85e8f8d872623d677bf4bedc67caeb0e8  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-011.txt
542a953ab79fa3fb59ae75a499094a979ec1f3d76a00b8aff586edfc23540f23  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-012.txt
8e163695b484bd9857fc0b0393e6899b744fec00d609d13a50a88fe5ee1c6197  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-013.txt
955809b9626db9b23d21a0164962bb952e1b2821e3b5a6e9eac8fa85a340f525  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-014.txt
9bf4e20aa2e14e048ffab071d626d547ab2461e5092b76edd5a5065b9d65e2e6  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-015.txt
32c29870c8eb1f92d9bc32d06299febd7c6e8c093ba5ac9352d91adc289f87bb  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-016.txt
54d6a1ee175b4f9ea591603700ee8b5ba2f878fd16fd72b0901961254720743d  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-017.txt
316bc2da18358ccc4c6aad1a1dbc221156b3776a8d9f6ee659108e3ebebbabbd  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-018.txt
943ff2c8579748a7777c301344195caa48c4b45fa5e4276628cecfe374a0321a  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-019.txt
c59cacc058b12b3bbaa60fe3aa83331104fb5bba46c60c8298732d0525ed79e1  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-020.txt
2ff231413dcd40af3ccea64442c3284ec0a6bb5dd42be16eb4d3795b4594ca38  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-021.txt
8933ea11a7a8491652fd0fc83c6b4995c671f608a163bb36647e21213a196d75  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-022.txt
f57eea39ed80def897360a465fd00170e29fbe86600bbd91ba3de17b52162dfa  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-023.txt
a6cead27bee32a2ce59e482412a3c8d6e03976fc3dde8dbdbb82b96f685e4d05  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-024.txt
b7984963bb12b3da90719c2cc6e3f6a66f9827c896a4467f482e786ce3ee0a0c  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-025.txt
0227645b9dfa6e9c4fc6c11d7321a878594c2dc2341d1cee5bbd8812c0613f8d  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-026.txt
31efad97bbc17c7093b664f8efe7bda7e648be8f48c9b97fcc045e870c0e2890  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-027.txt
65176f95094af8ce6946f5d76eb098eaba6f7e6dc53aae2c5c9b192ec3433ec9  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/ocr/page-004.txt
39b5d45d1e713beeeea749a04b0d6179da2b5a42063ed628725cba3ac7745c14  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/ocr/page-006.txt
e2ab69577f9e1601a5792a07c42ad7269df9bce37b7b0960d6c0bdaa1ebe0aec  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/ocr/page-008.txt
38cfde66c6fbd0b4186731cb7eea2986775227ab1d4805c48fddea3b8bc4ac58  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/ocr/page-013.txt
0fed86f24323b7309d9634c7b8197e7427c730ae68adf20b57f3f06b16583d6e  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/ocr/page-020.txt
ac40a53b24cf75b5c508d85cb4333ca5711b5ced49b1f0238652a04e9e04faf6  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/figure_render-25.png
e1f4b165661a69ebe061aeb2d97122953848b33bf1c94c174bf85a764e95fada  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/figure_render-26.png
410f9bc950e14d5e372a6d85b3b790187d08e4af15e7e23fd61b9f192b97e381  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/figure_render-27.png
c733ef4bac33236c87b72a7fc8a89c1299cd0626592b5f18075090f521bc9313  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/page-004.png
4f9a54e22bf66499fefea0d690f8d37fe78f017dc0b0c17d16467f9f8ae6ad86  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/page-006.png
7d9727a36facd068ea6231928e3def934feaf07346f2311f645ad6c66c24ac96  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/page-008.png
4984bbe10c7d1b1e829b773ebb14c9ba2c50825879fa4376d9087ef8dd159820  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/page-013.png
feae4fb04d3e3e9f9fd2b99e5e2600a058bd673f7ef2d550a86d9cb59570f72f  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/page-020.png
0b4487cfd8c734d7d5387176ec138f04c54afaa23f4113d1ccffa6f798868bf2  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/table_check-07.png
11280e7a8a59706c5e762f97bf6bb47bfd4a4edc8cb4a42187f2950271e74367  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/table_check-10.png
407b55fc3f55834864cd938d77b867ac45df8c09af8355bb2ce0ce0e1d3afd7f  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/table_check-21.png
d58f476ca04c764a5f7fe5b5828b1c5d410cb50e25cbb5771026d1468b204f7b  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_manifest.md
7f497c98839e77bc5c62ff256892a1d46b7a14c155d07aaafa5b14dbb27fba34  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_metadata/page-004.ocr.json
be3462a5d036ed3b8b43ab76be5c9c3984eba4f6afcd805f7bb20f6ce6d3d107  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_metadata/page-006.ocr.json
6390df076d389ff0c3f26f719a2f1f0ad7dccfc076150c2eaf2ff70324d852eb  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_metadata/page-008.ocr.json
2cb6c02acd42d9f5772b2574b458ded35a3ad55c159dd9e6b8e371b6dfd06f41  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_metadata/page-013.ocr.json
245d844cac9639bd70940b4b165671bd343247e54fb9c440c68bdab10782fba4  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_metadata/page-020.ocr.json
53ba13f5b7e84e14cf721eb5b8950698eaa57680c31541178b7282c82c2b2045  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/preprocessing_record.md
9ee90d2f0d851ce98ef0fa266d1fadc1f709df5e2f616125fc124baf5c8e0a54  .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/results_supplement_evidence_map.md
3c1f22f112321ff40ace133802b7abcd5fa1bfec734f7c2000dc80ae16f63f1c  .ai_paper_validation/document_outputs/DOC-004/supp3-p7.pdf
8c6464723f6ee1d2a1b57760e7f61a3ca3983c8bc4b2f5daa000d931d7af3350  .ai_paper_validation/document_outputs/DOC-004/supp3_layout.txt
73d909d14f92b1863edcca27b16e036a620cf674fe3138f710c8d2ec1a450880  .ai_paper_validation/document_outputs/DOC-005-supplement-4-data-sharing/ai_training_restriction_record.md
172a9aa58d521674061446b85c2198aeb6b3aa5c13e02b3b3be640599c4f0373  .ai_paper_validation/document_outputs/DOC-005-supplement-4-data-sharing/completion_record.md
2ffa2c596ed8d7f9f1e9c6b950f21e70e199d20efd295c9b259443489d14ebff  .ai_paper_validation/document_outputs/DOC-005-supplement-4-data-sharing/initial_document_record.md
3c7ba5e5dde0dad8bd48b418bf3bfcaa673a86af8ab290145649a66c47b9d8de  .ai_paper_validation/document_outputs/DOC-005-supplement-4-data-sharing/preprocessing_record.md
7ac560e645e43313ffd4aefea07177d2f20c94cdd274d560fd4f6dfe7d75ab43  .ai_paper_validation/document_outputs/jama_saynorea_2019_oi_190106_1635377898.43062/ai_training_restriction_record.md
b40622421d9b83c19daa1ff867ce2b2acd0d9e50dddc84d737d713cdf3316a3c  .ai_paper_validation/document_outputs/package_manifest.md
fb6cd51ea48f9be1fb48a5dff9f2daad4e32881a3c446281ba43cb82b0319c45  .ai_paper_validation/preprocessing/ocr_backend.json
16927391c9f7563759c65d431a66027cafb7582e3d4ee04ff883e998ec2160a4  .ai_paper_validation/preprocessing/rendered/supp3-03.png
ae22925e3eafbc65ef133cbe8fa35882aaed8a006d706bdb0bf60a6ec79344ae  .ai_paper_validation/preprocessing/rendered/supp3-07.png
c6da65564ab61e36ed1313b40bccb932cc3f2d7a5911a651cafeb85286c6d83a  .ai_paper_validation/preprocessing/rendered/supp3-09.png
11280e7a8a59706c5e762f97bf6bb47bfd4a4edc8cb4a42187f2950271e74367  .ai_paper_validation/preprocessing/rendered/supp3-10.png
8c6464723f6ee1d2a1b57760e7f61a3ca3983c8bc4b2f5daa000d931d7af3350  .ai_paper_validation/tmp_rights/supp3.txt
9aac07ada1f743b87cf2c3ab8806227f4cdd30e903e012b03b639c9ded910790  .ai_paper_validation/tmp_rights/supp3_metadata.txt
```

## Coverage conclusion

- **Eligible reusable page units:** DOC-001 pp. 1-14 and DOC-004 pp. 1-29, for 43 units.
- **Fresh-required units:** DOC-002 pp. 1-75, DOC-003 pp. 1-30, and DOC-005 p. 1, for 106 units.
- **No eligible table/workbook extraction:** none found.
- **No current scientific-coverage gap:** all non-usable, stale, duplicate, unreadable, or absent derivative units are assigned to direct-source mapping where relevant; derivative limitations remain documented above.

