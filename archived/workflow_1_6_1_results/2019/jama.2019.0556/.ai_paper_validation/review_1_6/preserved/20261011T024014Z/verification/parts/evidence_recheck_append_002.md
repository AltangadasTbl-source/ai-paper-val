# Appended Stable-Candidate Evidence Recheck: C022

Owner: `/root/recheck_append_002`; fresh `qc16_evidence_rechecker`, `gpt-6.1-sol` / `high`; provider inherited from the current session. Assigned scope is C022 only. This part does not edit the canonical ledger, canonical recheck, other agents' artifacts, or supplied sources.

The normative classification and mechanical-recheck rules were read in `QUALITY_CONTROL_SCOPE.md` and `workflow_1_6/review_contract.md`. `tooling_record.md` records direct Poppler tools as available and no fallback environment. Current-run `extraction/parts/support_plan_p26_visual_repair.md`, `checkers/numeric_visual_repair.md`, and `relationships/parts/numeric-visual-repair.md` were read. Provenance is local candidate VR01, numeric relationship N185, and mapping U065.a–c. The supplied protocol page was visually inspected using its readable, source-matched direct Poppler render `preprocessing/recheck-joi190007supp1-p26.png`. Its printed footer identifies page 26 of 60 and Version 7, July 6, 2017. The preceding physical page 25 was also visually inspected using `preprocessing/support-s1-p25.png` to confirm the example-label context. No additional derivative, OCR, external evidence, or GPU was needed. These current-run derivatives are locators and transcription aids; the displayed supplied-source pages are the authority.

## C022

**Candidate:** The upper multivitamin example product label specifies a daily tablet but calls its package contents capsules.

**Status:** Pending Human Adjudication.

**Location found:** Yes. [Protocol physical PDF p26, upper multivitamin product label](../../../../joi190007supp1_prod.pdf#page=26), above section 6.5. Its product/composition, dosage, and contents lines are separately legible within the same upper panel. The lower omega-3 label and surrounding section 6.5 are also visible on that exact page and were inspected for an alternative explanation.

**Source value/text matched:** Yes. In English translation, the upper label identifies multivitamins with calcium 100 mg, folic acid 400 micrograms, selenium 30 micrograms, and vitamin D3 20 micrograms, or a placebo tablet. Its next line states dosage of **1 tablet per day**, preferably before a meal. The numeral 1 and tablet unit are directly visible; there is no native-text or OCR substitution in this confirmation.

**Comparator matched:** Yes. The contents line of the **same upper label** states, in English translation, **Contents: 30 capsules**. The numeral 30 and capsule noun are directly visible. This is not a contents line imported from the lower panel: both panels independently display 30 capsules, while the lower panel's dosage is 1 capsule per day.

**Consistency rule applicable:** Yes. Within a single product label, the named dosage unit and named units in its package contents should describe the same dosage form unless a conversion, mixed package, or explicit alternative convention is supplied. This is a unit-label identity check, not a calculation of nutrient mass, adherence, duration, or treatment effect. The candidate concerns tablet versus capsule terminology; it does not allege that the printed count 30 is numerically incorrect.

**Calculation or logical comparison reproduced:** Yes. The upper panel's daily-dose unit is tablet, whereas its contents unit is capsule. The two different named dosage forms occur in adjacent lines for the same labeled product. The mismatch therefore reproduces directly without arithmetic or an inferred dispensing schedule. The lower omega-3 panel is internally capsule/capsule and provides context rather than a second discrepancy relationship.

**Necessary inputs available:** Yes for the printed unit-label comparison: panel identity, dose line, and contents line are all visible together on the supplied page. No quantitative input is missing for establishing that the two nouns differ.

**Exact missing inputs or definitions:** The supplied label does not define tablet and capsule as interchangeable terms, identify a mixed-form package, provide a conversion between the forms, or state the intended upper-label dosage-form noun. The referenced C1.2 document's official labels and manufacturing information are not supplied in this package. An authoritative final label or dispensing record establishing the actual dispensed upper product is also absent from this comparison. Those absent inputs limit explanation and adjudication, not transcription of the observed mismatch.

**Source-grounded alternative interpretation:** [Protocol physical p25, preparation and labelling section](../../../../joi190007supp1_prod.pdf#page=25) explicitly describes the displayed labels as patient-information examples and refers to official labels on C1.2 pages 4–12 and manufacturing details on C1.2 pages 24–27. Thus the visible mismatch may be confined to an example rather than an actual final dispensing label. Section 6.5 on p26 uses the broader expressions multi-vitamin pills and capsules, and unused pills/capsules, in its shipping and accountability instructions. That generic wording may permit loose operational terminology; however, it does not explicitly equate tablet and capsule on the upper product label. The lower label has the same 30-capsule contents wording, making shared label-template wording a possible explanation. Neither the example status, broad accountability wording, nor similar lower panel establishes which upper-label noun was intended or what was actually dispensed.

**Direct observation versus inferred explanation:** Direct observation is the upper panel's tablet dosage and capsule contents terminology, together with the lower panel's consistent capsule terminology, the broad accountability prose, and p25's example-label framing. A copied template, informal synonym usage, a different actual dosage form, or a mixed package is an inferred explanation only. No production mechanism, clinical implication, or actual dispensing error is established by this observation.

**Exact remaining human question:** Does the upper multivitamin example label intentionally use capsule as an interchangeable term for tablet, or which dosage-form noun should describe its contents and daily dose? Was this wording confined to the patient-information example, or does an authoritative C1.2 final label or dispensing record establish the same wording and actual product form?

**Document-role confirmation:** The upper product/composition and dosage lines are PLAN, and the upper contents line is PLAN. By content, this is a prospective operational example product label embedded in a trial protocol, not a report of study results. The lower label, section 6.5, and p25's label-preparation explanation are also PLAN context. No REPORT location is part of this discrepancy.

**Relationship confirmation and precedence:** `P_P` confirmed. Both compared locations occur inside one PLAN label on one protocol page. All substantive discrepancy relationships are `P_P` only. The lower label and accountability prose support interpretation but introduce no additional discrepancy relationship. There is no `P_R`, `S_C`, or `S_W` comparison. No correction to the provisional category or relationship type is required.

**Classification ambiguity:** None for document role or relationship type. The unresolved issue is intended dosage-form terminology, not whether these source locations are PLAN content.

**Primary category:** Measure, label, or scale inconsistency.

**Relationship type:** P_P.

**All relationships:** P_P.

**Compared document roles:** PLAN protocol p26 upper product-label tablet dosage vs PLAN protocol p26 upper product-label capsule contents.

**Review domain:** plan_material.

**Evidence state:** recorded_candidate.

**Evidence-state determining fact:** Direct visual reading confirms that the same upper label gives a tablet daily dose and 30 capsule contents. The package does not supply a definition reconciling these dosage-form terms. The registered label mismatch remains as registered pending that named definition; no original input or alignment assumption is disproved.

**Suggested review disposition:** retain. This follows mechanically from `recorded_candidate` and is a prefilled human-review field, not an adjudication.

**Distinctness:** C006 compares fish-oil versus EPA+DHA mass descriptions across PLAN and REPORT content. C014 compares the separately printed 13-week and four-month supply durations. C022 instead compares two dosage-form nouns inside the same upper multivitamin label. Its values, comparator, and consistency rule are distinct from both IDs.

**Bounded downstream relevance:** An ambiguous dosage-form noun could be copied into intervention or packaging descriptions. The observation does not establish a changed dose, participant exposure, or paper-level conclusion effect.

## Classification row

| ID | Primary category | Relationship type | All relationships | Compared document roles | Review domain | Evidence state | Suggested review disposition |
|---|---|---|---|---|---|---|---|
| C022 | Measure, label, or scale inconsistency | P_P | P_P | PLAN protocol p26 upper product-label tablet dosage vs PLAN protocol p26 upper product-label capsule contents | plan_material | recorded_candidate | retain |

## Assigned-scope completion

C022 was directly rechecked against the exact supplied-source page. All required recheck facts and classification fields are recorded separately. The intended dosage-form terminology and actual dispensed upper product remain for human adjudication. No candidate was deleted, assigned severity, or finally adjudicated.
