# Support PLAN Visual-Content Mapping Repair

Owner: `/root/support_visual_repair`; fresh bounded support-mapping repair; `gpt-6.1-sol` / `medium`; current provider inherited. This artifact supplements the current source-linked support map. It assigns no candidates or dispositions. Canonical maps, ledgers, manifests, sources, and reusable assets are unchanged.

## Exact assigned scope and source authority

Direct visual mapping: DOC-002, `joi190007supp1_prod.pdf`, physical PDF page 26, both raster product-label panels. Document role is PLAN by prospective operational content. The supplied PDF page was inspected through its existing source-matched render `.ai_paper_validation/review_1_6/preprocessing/recheck-joi190007supp1-p26.png`; no duplicate rendering was needed. The native-text omission of the product labels is closed by this visual mapping. U019 retains its existing separate text relationship: 13-week supply at baseline and months 3, 6, and 9, weighing unused bottles and pills/capsules for consumption accountability.

Additional assigned gap search: complete direct raster inventories for every support PDF, plus fresh visual identity checks of DOC-002 p1 and DOC-003 p1 graphics. These cover all substantial raster objects absent from the earlier targeted visual list. Existing support-mapper visual inspections of DOC-002 pp12,25,31,32,38 and DOC-004 pp16–23 remain source-linked coverage; they are not reinterpreted here.

## U065 — Complete product-label quantitative and operational content

Source location for every subkey: [DOC-002 physical p26](../../../../joi190007supp1_prod.pdf#page=26), upper and lower product-label panels above section 6.5. Translation below is English; quantities retain the printed units. Label typography identifies the study as MooDFOOD and displays example code EX59. Neither label displays clinical outcomes, P values, confidence intervals, or participant denominators.

| Local relationship key | Exact panel/content | Printed quantity or operational meaning | Main-paper matching key / alignment |
|---|---|---|---|
| U065.a | Upper multivitamin composition | Calcium 100 mg; folic acid 400 μg; selenium 30 μg; vitamin D3 20 μg; or placebo tablet. | Intervention micronutrient composition; distinguish this product-label quantity from broader protocol dose ranges and measured content. |
| U065.b | Upper dosage | 1 tablet per day, preferably before a meal. | Daily multivitamin tablet dose; count is tablets/day. |
| U065.c | Upper package contents | Contents: 30 capsules. This is the exact English translation of the upper label's contents line; retain its noun even though the dose line specifies tablet. | Product packaging count/unit; separate from actual adherence denominator and from U019's supply schedule. |
| U065.d | Lower omega-3 composition | Omega 3: 1412 mg fish oil, of which at least 65% EPA and at least 10% DHA; or placebo capsule. | Omega-3 intervention dose and composition. The printed mass is fish-oil mass; the percentages are the composition minima as written. Keep fish-oil mass distinct from a separately stated combined EPA+DHA mass. |
| U065.e | Lower dosage | 1 capsule per day, preferably before a meal. | Daily omega-3 capsule dose; count is capsules/day. |
| U065.f | Lower package contents | Contents: 30 capsules. | Product packaging count/unit; separate from actual adherence denominator and U019 supply duration. |
| U065.g | Both panels, storage | Store dry and at room temperature (15–25°C); protect from sunlight. | Storage temperature and handling; temperature range is a storage condition rather than a nutrient dose or outcome scale. |
| U065.h | Both panels, other operations | Only for MooDFOOD study; keep out of reach of children; contact M. Bot, telephone 020-7884594; example code EX59. | Administrative identifiers, not result values. The surrounding rulers display graphical dimensions, not a drug-dose or clinical-measure scale. |

No source-unreported formulation equivalence, actual nutrient mass, manufacturing tolerance, or clinical interpretation is inferred. The label supplies composition and mass-basis definitions for later source matching. This mapping does not decide whether other dose descriptions agree with it.

## Complete raster-object gap inventory

Engine: direct Poppler `pdfimages` 26.01.0. Every object listed below was included in the inventory; repeated objects and transparency masks are not independent scientific relationships.

| Source | Exact raster inventory | Visual coverage / content | Gap outcome |
|---|---|---|---|
| DOC-002, PLAN, pp1–60 | 66 image instances: object 2859 (170×29) repeats once on each of all 60 pages; p1 objects 2862 (999×220) and 2864 (1259×667); p12 object 25 (983×627); p26 objects 58 (617×273) and 59 (630×273); p31 object 70 (721×1044). | Repeated object 2859 is the MooDFOOD header logo, directly visible on p26 and fresh p1. Fresh p1 inspection identifies object 2862 as the large MooDFOOD cover logo and object 2864 as the VU medical-center logo; both NO_APPLICABLE for quantitative results. P12 conceptual diagram is U004; p31 recruitment flowchart is U023; both were previously visually mapped. Both p26 labels are fully mapped as U065 here. | No other substantial raster image exists in the complete protocol inventory. No further scientific raster unit remains uninspected. |
| DOC-003, PLAN, pp1–5 | One image instance: p1 object 45, 700×142. | Fresh direct p1 visual inspection identifies the MooDFOOD logo. NO_APPLICABLE for quantitative results. Page text relationships U039 remain unchanged. | No other raster image exists in the SAP inventory. |
| DOC-004, REPORT, pp1–25 | P17 object 45, 1306×909 image, plus matching 1306×909 soft mask. | Four symptom/utility figure panels already visually mapped in U056; existing p16–23 inspections also covered tables, which need not be raster objects. The soft mask is image transparency rather than a separate result. | No additional raster scientific unit remains uninspected. |
| DOC-005, REPORT, p1 | No raster image objects. | Complete page already mapped as no applicable quantitative results. | No raster gap. |

Protocol p25, p32 and p38 were additionally rendered by the original support mapper, despite having no raster objects apart from the header logo: the p25 text content, p32 isolated 24-month questionnaire box, and p38 blank body remain explicitly covered. Raster inventory is used here to discover omissions, not to replace all-page native/vector coverage.

## Derivatives and exact commands

All commands use available direct local CPU tools; no Python extraction, OCR, web access, fallback environment, or GPU was used. New derivatives are unique `visualrepair-*` files and are not reused legacy artifacts.

- `pdfimages -list joi190007supp1_prod.pdf > .ai_paper_validation/review_1_6/preprocessing/visualrepair-s1-images.txt`
- `pdfimages -list joi190007supp2_prod.pdf > .ai_paper_validation/review_1_6/preprocessing/visualrepair-s2-images.txt`
- `pdfimages -list joi190007supp3_prod.pdf > .ai_paper_validation/review_1_6/preprocessing/visualrepair-s3-images.txt`
- `pdfimages -list joi190007supp4_prod.pdf > .ai_paper_validation/review_1_6/preprocessing/visualrepair-s4-images.txt`
- `pdftoppm -r 110 -f 1 -l 1 -singlefile -png joi190007supp1_prod.pdf .ai_paper_validation/review_1_6/preprocessing/visualrepair-s1-p1`
- `pdftoppm -r 110 -f 1 -l 1 -singlefile -png joi190007supp2_prod.pdf .ai_paper_validation/review_1_6/preprocessing/visualrepair-s2-p1`

Fresh render engine: direct Poppler `pdftoppm` 26.01.0, 110 dpi. Existing p26 render was visually readable; targeted OCR was unnecessary. Four complete raster inventories plus two fresh page renders were produced. All source links use physical PDF pagination.

## Repair counts and limitations

Two scientific raster panels repaired on one physical PLAN page; one added local relationship family U065 with eight explicit subkeys. Two additional PLAN pages visually inspected for three unique administrative graphics (two protocol-cover logos and one SAP logo); all are NO_APPLICABLE for scientific numeric results. Four support PDFs inventoried completely. U019 text schedule and all previously mapped source-unit counts remain unchanged. Further scientific-coverage gaps: none found. Manufacturer documentation referenced elsewhere remains unsupplied, and the label does not supply independent assay data; neither limits transcription of these visible labels.
