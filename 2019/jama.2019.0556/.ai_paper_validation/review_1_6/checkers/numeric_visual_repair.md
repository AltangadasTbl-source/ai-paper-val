# Numeric Consistency Review — Product-Label Visual Repair

Fresh specialist: root/numeric_visual_repair, gpt-6.1-sol / medium, current inherited provider. Scope: all U065.a–h and N185, protocol DOC-002 physical p26 upper/lower raster labels, with supplied dose definitions for identity matching. Read QUALITY_CONTROL_SCOPE.md, workflow_1_6/review_contract.md and tooling_record.md completely. Required numeric/reporting checks applied under the exact quantitative scope; no broad design or clinical review. Source-linked visual mapping is a locator; independent direct image inspection confirmed the printed inputs. No old candidate/report conclusions were used for discovery. The current-run C006 ledger was consulted solely for genuine-duplicate comparison after source inspection, as assigned.

## VR01 — Upper multivitamin package unit is capsule while its identity and dose are tablet

**Relationship:** N185; U065.a–c. Local checker provenance VR01; no stable C ID assigned here.

**Exact compared locations and document roles:** Both locations are PLAN, the prospective protocol [joi190007supp1_prod.pdf physical p26](../../../joi190007supp1_prod.pdf#page=26), upper product-label panel. First location: composition/product description and immediately following dosage line. Second location: immediately following contents line. Lower label on the same page is contextual PLAN corroboration, not a separate discrepancy edge.

**Printed inputs:** Upper composition line identifies multivitamin ingredients calcium100mg, folic acid400μg, selenium30μg and vitaminD3 20μg, followed by the placebo-tablet designation. The upper dosage line says1 tablet per day. Its contents line says30 capsules. The lower omega label identifies a capsule, dose1 capsule/day, contents30 capsules. English translations retain the source's distinct tablet and capsule terms; the original Dutch upper dosage noun is tablet and the contents noun is capsules.

**Reproducible rule and calculation:** For one labeled dosage product, its unit of contents should identify the same dosage form as its product identity and administration unit unless a conversion or combined-package definition is supplied. Upper label identity=tablet; daily-dose unit=tablet; content unit=capsule. The source gives no tablet-to-capsule equivalence or mixed-package definition. No numerical subtraction is needed to reproduce a unit-label contradiction. Conditionally30 matching dosage units ÷1 matching unit/day =30days, but that duration is not asserted while the upper units differ and is not a separate candidate.

**Tolerance:** Exact categorical unit identity; numeric rounding does not transform a tablet into a capsule. The printed count30 is not challenged.

**Direct observation versus inference:** Direct visual observation is the opposing upper-label dosage-form nouns on one panel. A copied template line, translation convention, example-label defect or product formulation change would be an inferred production mechanism; none is established. No inference about the tablets/capsules actually dispensed, adherence, active nutrient intake or trial result is made.

**Source-grounded alternatives and missing inputs:** Protocolp25 calls these patient-information label examples and points to unsupplied official-label/manufacturing documentC1.2. The same-p26 lower capsule label also has contents30 capsules, so the upper could be a template example. Generic use of capsules for package contents or a later dosage-form amendment could reconcile the terminology, but no such convention is stated. The necessary missing input is the intended dosage form and meaning of the upper contents noun in the example label; supplied official labels would help distinguish an example-only text defect from actual package labeling.

**Quality-control relevance:** A contradictory dosage-form unit can propagate to intervention descriptions or dosing extraction. This bounded reporting observation does not imply a changed active dose or altered study conclusion.

**Exact human question:** For the upper multivitamin example label on protocol physical p26, does contents30 capsules refer to the same product administered as1 tablet/day, and which dosage-form designation and packaging definition were intended? Was this only an example-label text inconsistency or did the official label use the same wording?

**Candidate category recommendation:** Measure, label, or scale inconsistency. Compared content is PLAN versus PLAN within one label; classification is left to coordinator/rechecker. No severity, validity, disposition or final correction is assigned.

**Distinctness:** Existing C006 compares intended EPA+DHA1g/day with reported EPA+DHA1412mg/day. VR01 compares tablet versus capsule package-unit labels in a different product, with a different comparator and identity rule. It is not a duplicate. The lower fish-oil label informs C006's already named mass-basis alternative; minimum65%EPA and10%DHA do not establish another independent exact active-dose discrepancy.

## Completed no-candidate checks and boundaries

N185 completion is fully recorded in relationships/parts/numeric-visual-repair.md: four micronutrient doses and conversions; planned-range alignment; two daily dosage units; both30-unit package counts without assuming one bottle per13-week shipment; fish-oil1412mg/minimum composition with conditional lower bounds and no unsupported exact ratio; both15–25°C storage ranges; repeated administrative identifiers and graphic-ruler nonapplicability. No inferential S relationship is added. Exactly one local candidate emitted after all eight U065 subkeys were checked. Source units, reusable assets and canonical files unchanged. Limits: C1.2 official-label/manufacturing records are unsupplied; composition minima and label examples cannot establish actual batch dose or dispensing form. These do not prevent direct reproduction of VR01.
