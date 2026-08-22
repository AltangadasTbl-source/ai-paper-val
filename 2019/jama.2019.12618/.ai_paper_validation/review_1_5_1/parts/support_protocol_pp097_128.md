# DOC-003 Support Quantitative Evidence Mapping — PDF pp. 97–128

## Scope and method

- **Direct source:** `joi190092supp2_prod.pdf` (DOC-003), PDF pp. 97–128 only; these pages are printed manual pp. 33–64.
- **Fresh extraction:** `pdftotext -layout -f 97 -l 128` was used for the run-local locator file `preprocessing/protocol_pp097_128_layout.txt`, then each assigned PDF page was directly extracted/inspected. PDF pp. 105, 107, 109, 116, 118, and 120 have no machine-text layer; their rendered source pages were visually inspected because they contain continuation text and tables.
- **Scope boundary:** This is protocol/manual content, not outcome-result reporting. The records below preserve definitions, schedules, thresholds, formulas, scales, and planned comparisons needed to match reported outcomes. They are not candidates or adjudications.
- **Main-paper matching keys used locally:** `VA_SECONDARY_OUTCOME` (best-corrected visual acuity); `CONTROLLED_INFLAMMATION_PRIMARY_SECONDARY` (anterior-chamber cells and NEI vitreous haze); `QOL_OUTCOMES` (SF-36, NEI-VFQ-25, IND-VFQ); `CATARACT_GRADE`; `PHASE_I_PHASE_II_POPULATION_AND_TIMEPOINT`.

## Page-complete extraction log

| PDF page | Printed page | Mapping status | Result-relevant content or explicit no-applicable record |
|---:|---:|---|---|
| 97 | 33 | MAPPED | Baseline timing and inflammation eligibility thresholds: N-P097-01. |
| 98 | 34 | MAPPED | Baseline laboratory windows and measured components: N-P098-01. |
| 99 | 35 | MAPPED | Follow-up measurement timepoints and phase-specific assessment schedule: N-P099-01. |
| 100 | 36 | MAPPED | Phase-II timing and treatment-failure follow-up: N-P100-01. |
| 101 | 37 | NO_APPLICABLE_RESULT_RELATIONSHIP | Non-study-visit procedure; no standalone result-relevant quantitative definition beyond a qualitative treatment-failure workflow. |
| 102 | 38 | MAPPED | Quality-of-life outcome timepoints; refraction waiting/distance requirements: N-P102-01, N-P102-02. |
| 103 | 39 | MAPPED | Letter-chart acuity threshold and trial-lens guide: N-P103-01. |
| 104 | 40 | MAPPED | Letter-chart high-acuity sphere/cylinder procedure: N-P104-01. |
| 105 | 41 | MAPPED (VISUAL) | Letter-chart cylinder-axis step table and spherical-equivalent rule: N-P105-01. |
| 106 | 42 | MAPPED | Letter-chart 20/100–20/200 procedure: N-P106-01. |
| 107 | 43 | MAPPED (VISUAL) | Letter-chart axis-step table, cylinder-power and refinement rules: N-P107-01. |
| 108 | 44 | MAPPED | Letter-chart <20/200, 1-metre adjustment and refraction procedure: N-P108-01. |
| 109 | 45 | MAPPED (VISUAL) | Letter-chart <20/200 axis/cylinder rules and step table: N-P109-01. |
| 110 | 46 | MAPPED | Letter-chart secondary-outcome definition, chart geometry and equipment calibration: N-P110-01. |
| 111 | 47 | MAPPED | Letter-chart illumination, time/distance, and lane specifications: N-P111-01. |
| 112 | 48 | MAPPED | Letter-chart test stopping/relocation thresholds and count-fingers criterion: N-P112-01. |
| 113 | 49 | MAPPED | Letter-chart hand-motion/light-perception rules and score-data specification: N-P113-01. |
| 114 | 50 | MAPPED | Tumbling-E chart refraction threshold and setup: N-P114-01. |
| 115 | 51 | MAPPED | Tumbling-E high-acuity trial-lens guide/procedure: N-P115-01. |
| 116 | 52 | MAPPED (VISUAL) | Tumbling-E high-acuity cylinder-axis table and spherical-equivalent rule: N-P116-01. |
| 117 | 53 | MAPPED | Tumbling-E high-to-medium acuity sphere procedure: N-P117-01. |
| 118 | 54 | MAPPED (VISUAL) | Tumbling-E medium-acuity cylinder-axis table and power rule: N-P118-01. |
| 119 | 55 | MAPPED | Tumbling-E medium and <6/60 sphere procedure; 1-metre adjustment: N-P119-01. |
| 120 | 56 | MAPPED (VISUAL) | Tumbling-E <6/60 cylinder-axis table and power procedure: N-P120-01. |
| 121 | 57 | MAPPED | Tumbling-E secondary-outcome/chart-scale definition: N-P121-01. |
| 122 | 58 | MAPPED | Tumbling-E equipment, illumination and distance calibration: N-P122-01. |
| 123 | 59 | MAPPED | Tumbling-E test stopping/relocation thresholds: N-P123-01. |
| 124 | 60 | MAPPED | Tumbling-E low-vision thresholds and explicit visual-acuity score formula: N-P124-01. |
| 125 | 61 | MAPPED | Highest score, Snellen conversion, certification/timing, and cataract scale: N-P125-01, N-P125-02. |
| 126 | 62 | MAPPED | Cataract categories and SUN anterior-chamber-cell scale: N-P126-01. |
| 127 | 63 | MAPPED | Flare, vitreous-cell, and NEI/Miami vitreous-haze definitions plus planned correlation: N-P127-01, S-P127-01. |
| 128 | 64 | MAPPED | NEI vitreous-haze grade-to-description table: N-P128-01. |

## Numeric/reporting relationship records

### N-P097-01 — Baseline eligibility timing and inflammation thresholds

- **Exact source location:** `joi190092supp2_prod.pdf#page=97` (printed p. 33, §4.3).
- **Main-paper key:** `PHASE_I_PHASE_II_POPULATION_AND_TIMEPOINT`; `CONTROLLED_INFLAMMATION_PRIMARY_SECONDARY`.
- **Direct observation:** Baseline eye examination and other assessments may be collected up to **14 days** before enrolment/randomization. Laboratory measurements may be collected within **4 weeks** or **90 days** before/on randomization, depending on test. Active inflammation eligibility is **at least 1+ anterior-chamber (AC) cells**, **at least 1+ vitreous haze by the NEI scale**, or active retinal/choroidal inflammation. Inflammation that met criteria within the preceding **14 days** may supply baseline values.
- **Relationship/definition:** Population entry, baseline measurement time, and the numerical controlled-inflammation components must be matched to the relevant visit/date and NEI scale, not to a generic pre-randomization assessment.

### N-P098-01 — Baseline laboratory time windows and assay groups

- **Exact source location:** `joi190092supp2_prod.pdf#page=98` (printed p. 34, §4.3.4).
- **Main-paper key:** `PHASE_I_PHASE_II_POPULATION_AND_TIMEPOINT`.
- **Direct observation:** Within **4 weeks**: CBC differential (limited to neutrophil and lymphocyte percentages), site-limited CD4, AST/ALT/creatinine, and pregnancy testing. Within **90 days**: HBsAg, hepatitis-C antibody, tuberculosis testing, chest radiograph, and specified syphilis tests.
- **Relationship/definition:** The two windows are distinct eligibility/input definitions; percentages of neutrophils/lymphocytes are not absolute counts.

### N-P099-01 — Follow-up and outcome-collection schedule

- **Exact source location:** `joi190092supp2_prod.pdf#page=99` (printed p. 35, §4.4).
- **Main-paper key:** `PHASE_I_PHASE_II_POPULATION_AND_TIMEPOINT`; `VA_SECONDARY_OUTCOME`; `QOL_OUTCOMES`.
- **Direct observation:** For Phase-I patients continuing the same drug, study information is recorded at **month 9**, **month 12**, or a non-study treatment-failure visit; laboratory results are collected **monthly**. Secondary eye exam, fundus photography, and quality-of-life forms occur in Phase 1 at treatment failure and the **6-month** visit (whichever comes first) and **12 months**; in Phase 2 at treatment failure and **6 months**.
- **Relationship/definition:** Result timepoint and phase must be matched before comparing outcome counts or measures.

### N-P100-01 — Phase-II transition and follow-up time

- **Exact source location:** `joi190092supp2_prod.pdf#page=100` (printed p. 36, §4.5).
- **Main-paper key:** `PHASE_I_PHASE_II_POPULATION_AND_TIMEPOINT`.
- **Direct observation:** Baseline Phase II can occur on the same day as Phase-I failure, or up to **2 weeks** later. A patient with a study-drug-related serious adverse event who cannot enter Phase II should still be followed for **6 months**.
- **Relationship/definition:** Phase-II baseline date may equal the Phase-I failure date but need not; these populations/time origins are not interchangeable.

### N-P102-01 — Quality-of-life outcome timing and instruments

- **Exact source location:** `joi190092supp2_prod.pdf#page=102` (printed p. 38, §5.1).
- **Main-paper key:** `QOL_OUTCOMES`.
- **Direct observation:** SF-36 is administered to all patients; NEI-VFQ-25 to all patients; IND-VFQ to Indian patients only. Assessments occur at baseline and **6 months** or treatment failure, whichever is first. Phase-I successes continuing from **6 to 12 months** also complete questionnaires at **12 months**, or earlier at failure; failure before 6 months also requires collection at failure and 6 months.
- **Relationship/definition:** Instrument population and assessment timepoint are explicit; do not compare an all-patient measure with the India-only IND-VFQ or collapse failure and scheduled-time assessments.

### N-P102-02 — Refraction precondition

- **Exact source location:** `joi190092supp2_prod.pdf#page=102` (printed p. 38, §5.2.1.A).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** Contact lenses are removed and refraction waits **30 minutes**. Refraction may begin at another distance, but spherical refinement is repeated at **4 metres** for acuity testing.
- **Relationship/definition:** Refraction/visual-acuity measurement conditions are specified operationally.

### N-P103-01 — Letter-chart threshold and trial-lens guide

- **Exact source location:** `joi190092supp2_prod.pdf#page=103` (printed p. 39, §5.2.1.A).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** Use Chart R (Precision Vision **2110**) at **4 m** unless acuity is worse than **20/200**—defined as missing **2 or more** letters on the top 20/200 (6/60) line—then test/refraction occurs at **1 m**. Trial-lens bands are 20/10–20/80 (6/3–6/24), 20/100–20/200 (6/30–6/60), and <20/200 (<6/60). The printed guide specifies sphere, cross-cylinder, axis/power increments and sphere-refinement increments: high band +0.50/+0.50, −0.37/−0.25, cross-cylinder 0.50 D with 0.25 D axis/power increment; middle band +1.00/+1.00, −1.00/−1.00, 1.00 D with 1.00 D axis/power increment; low band +2.00/+2.00, −2.00/−2.00, 1.00 D with 1.00 D axis/power increment.
- **Relationship/definition:** The published visual-acuity score must identify chart type and test distance; Snellen and metric equivalents are paired bands, not separate outcomes.

### N-P104-01 — Letter-chart high-acuity refraction rule

- **Exact source location:** `joi190092supp2_prod.pdf#page=104` (printed p. 40, §5.2.1.A).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** For 20/10–20/80 (6/3–6/24), plus probing is **+0.50 D** and lens replacement is +0.50 more plus; a **−0.37 D** improvement of at least one letter changes the trial lens by **−0.25 D**. Cylinder screening uses ±0.50 D at 90°, 180°, then 45°/135°; if a cylinder axis test is initially indifferent, shift axis **15°**.
- **Relationship/definition:** These are chart-specific operational thresholds, not effect estimates.

### N-P105-01 — Letter-chart cylinder-axis and spherical-equivalent rule

- **Exact source location:** `joi190092supp2_prod.pdf#page=105` (printed p. 41; visual source confirmation).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** Axis step size by cylinder power is: <**1.00 D** → **10°**; 1.00 to <2.00 D → **5°**; 2.00 to <3.00 D → **3°**; 3.00 to <5.00 D → **2°**; 5.00 to <8.00 D → **1°**. Refinement uses ±**0.25 D** cross-cylinder and changes cylinder by ±**0.25 D**. Beginning at cylinder ≥**1.00 D**, each **0.5 D** cylinder-power change requires a **0.25 D** sphere adjustment of opposite sign to maintain spherical equivalent. The final high-acuity sphere refinement repeats +0.37/−0.37 D probing with +0.25/−0.25 D lens changes.
- **Relationship/definition:** Explicit operational arithmetic: a 0.5-D cylinder change maps to an opposite-sign 0.25-D sphere change.

### N-P106-01 — Letter-chart middle-acuity refraction rule

- **Exact source location:** `joi190092supp2_prod.pdf#page=106` (printed p. 42, §5.2.1.A).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** For 20/100–20/200 (6/30–6/60), use ±**1.00 D** sphere increments and ±**1.00 D** cross-cylinder; improvement by at least one letter with −1.00 D changes the trial lens by −1.00 D. Cylinder screening uses 90°/180° and, if needed, 45°/135°.

### N-P107-01 — Letter-chart middle-acuity axis, cylinder, and final sphere rules

- **Exact source location:** `joi190092supp2_prod.pdf#page=107` (printed p. 43; visual source confirmation).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** Initial axis indifference allows a **15°** move. The axis-step table is identical to N-P105-01. Cylinder refinement uses ±**1.00 D** cross-cylinder, cylinder change ±**1.00 D**, and, at cylinder ≥1.00 D, an opposite-sign sphere adjustment of **0.25 D per 0.5 D** cylinder change. Final spherical refinement uses +0.50/−0.50 D probing and ±0.50-D lens changes.

### N-P108-01 — Letter-chart low-acuity/one-metre rule

- **Exact source location:** `joi190092supp2_prod.pdf#page=108` (printed p. 44, §5.2.1.A).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** If 4-m refraction cannot be performed (missing **2 or more** letters on the largest line), move to **1 m** and add **+0.75 D** to the beginning approximate refraction for the accommodation difference. For <20/200 (<6/60), use +2.00/−2.00 D probing and ±2.00-D trial-lens changes; cylinder screening uses ±1.00 D.

### N-P109-01 — Letter-chart low-acuity cylinder rule

- **Exact source location:** `joi190092supp2_prod.pdf#page=109` (printed p. 45; visual source confirmation).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** For the <20/200 letter-chart band, cylinder-axis testing uses the same **15°** initial adjustment and the same power-to-axis-step table as N-P105-01; cylinder refinement uses ±**1.00 D** and the opposite-sign sphere correction of **0.25 D per 0.5 D** cylinder change at cylinder ≥1.00 D.

### N-P110-01 — Letter-chart secondary outcome and scale/equipment definition

- **Exact source location:** `joi190092supp2_prod.pdf#page=110` (printed p. 46, §5.2.2.A).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** Visual acuity is explicitly a **secondary outcome**. Charts 1, 2, and R (Precision Vision 2110, 2111, 2112) each have **14 lines** of high-contrast letters and geometric progression of letter size/arithmetic progression of logMAR. Chart 1 is right eye, Chart 2 left eye, and Chart R refraction. Light-box dimensions are **24.75 in (62.9 cm) × 25.75 in (65.4 cm) × 7 in (17.8 cm)**. The top of row 3 (0.8 logMAR, **45 letters**, 20/125 Snellen) is **49 ± 2 in (124.5 ± 5.1 cm)** above the floor; the five-pronged base has prongs about **14 in (35.6 cm)** long and two lockable wheels.
- **Relationship/definition:** Scale label is logMAR/letter-score related, while 20/125 is a Snellen reference for the calibration row.

### N-P111-01 — Letter-chart illumination and distance calibration

- **Exact source location:** `joi190092supp2_prod.pdf#page=111` (printed p. 47, §5.2.2.A).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** With light box off, chart-centre illumination must be ≤**15 foot-candles**. The box has two **20-W** fluorescent tubes; illumination diminishes **5%** in the first **100 h** and another **5%** in the next **2,000 h**; new tubes are on about **4 days (~96 h)** before use and replaced annually. Each 14-in (35.6-cm) sleeve leaves about 4 3/16 in (10.6 cm) uncovered at both ends. Test distances: **4 m = 13 ft 1.5 in = 157.5 in** and **1 m = 39 3/8 in**; add 7 in (17.8 cm) wall-box depth or 13 in (33 cm) stand-caster clearance where applicable.

### N-P112-01 — Letter-chart test thresholds and count-fingers criterion

- **Exact source location:** `joi190092supp2_prod.pdf#page=112` (printed p. 48, §5.2.2.A).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** Each eye is tested separately after refraction at **4 m**. If fewer than **20 letters** are identified at 4 m, retest at **1 m**; only the first **6 rows** are read at 1 m. If no letters are read at 1 m, proceed to low vision. Count-fingers testing uses 1, 2, or 5 fingers at **1 m**, repeated **5** times; **3/5** correct identifies count-fingers vision.
- **Relationship/definition:** This threshold belongs specifically to the letter-chart protocol, not the tumbling-E protocol.

### N-P113-01 — Letter-chart low-vision and score-data definition

- **Exact source location:** `joi190092supp2_prod.pdf#page=113` (printed p. 49, §5.2.2.A).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** Hand motion is tested at **0.5 m**, with approximately one back-and-forth movement per second, **5** times; **4/5** correct indicates hand-motion vision. Light perception is tested from **0.5 m** with the light directed **4** times. The form records row-level numbers of correct letters at 4 m and, where applicable, 1 m and low-vision results; the biostatistician calculates visit score. Snellen equivalent is the ratio for the hardest line with at least **4 of 5** letters correct.
- **Missing-definition note:** This letter-chart section does not state the numerical visit-score conversion formula on these pages; it refers only to biostatistician calculation. Do not assume the tumbling-E formula (N-P124-01) applies without the named chart/formula source.

### N-P114-01 — Tumbling-E refraction threshold and setup

- **Exact source location:** `joi190092supp2_prod.pdf#page=114` (printed p. 50, §5.2.1.B).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** This alternative protocol uses Chart R Precision Vision **2305b**. Contact-lens removal requires **30 minutes**; final refinement is at **4 m**. Worse than 20/200 means missing **2 or more** letters on the 20/200/6/60 top line and triggers **1-m** refraction.

### N-P115-01 — Tumbling-E high-acuity trial-lens guide

- **Exact source location:** `joi190092supp2_prod.pdf#page=115` (printed p. 51, §5.2.1.B).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** The table pairs 6/3–6/24 with 20/10–20/80 at 4 m, 6/30–6/60 with 20/100–20/200 at 4 m, and <6/60 with <20/200 at 1 m. It specifies the same high/middle/low sphere and cylinder increments as N-P103-01. For high acuity, +0.50 D probing and +0.50-D increments, −0.37 D probing and −0.25-D changes, and ±0.50-D cross-cylinder are used.

### N-P116-01 — Tumbling-E high-acuity cylinder and spherical-equivalent rule

- **Exact source location:** `joi190092supp2_prod.pdf#page=116` (printed p. 52; visual source confirmation).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** Axis-step table: <1.00 D → 10°; 1.00 to <2.00 D → 5°; 2.00 to <3.00 D → 3°; 3.00 to <5.00 D → 2°; 5.00 to <8.00 D → 1°. High-acuity cylinder refinement uses ±0.25 D; for cylinder ≥1.00 D, each 0.5-D cylinder change requires opposite-sign 0.25-D sphere adjustment. Final high-acuity sphere refinement uses ±0.37-D probes and ±0.25-D lens changes.

### N-P117-01 — Tumbling-E middle-acuity procedure

- **Exact source location:** `joi190092supp2_prod.pdf#page=117` (printed p. 53, §5.2.1.B).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** The page completes high-acuity final refinement, then defines 6/30–6/60 (20/100–20/200) testing: +1.00-D probes/increments, −1.00-D probes/changes if at least one-letter improvement, and ±1.00-D cross-cylinder. It directs a change to the trial lenses for a new acuity band if acuity improves substantially during refraction.

### N-P118-01 — Tumbling-E middle-acuity cylinder rule

- **Exact source location:** `joi190092supp2_prod.pdf#page=118` (printed p. 54; visual source confirmation).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** The 6/30–6/60 cylinder-axis procedure uses ±1.00-D cross-cylinder, 15° initial axis movement if indifferent, the same five-band axis-step table, ±1.00-D cylinder changes, and the 0.25-D opposite-sign sphere correction for each 0.5-D cylinder change when cylinder is at least 1.00 D.

### N-P119-01 — Tumbling-E low-acuity/one-metre rule

- **Exact source location:** `joi190092supp2_prod.pdf#page=119` (printed p. 55, §5.2.1.B).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** This page completes middle-band final refinement with +1.00/−1.00 D. For <6/60 (<20/200), inability to refract at 4 m is missing 2 or more letters on the largest line; move to 1 m and add +0.75 D to initial refraction. Use +2.00/−2.00-D sphere probes and changes and ±1.00-D cross-cylinder.

### N-P120-01 — Tumbling-E low-acuity cylinder rule

- **Exact source location:** `joi190092supp2_prod.pdf#page=120` (printed p. 56; visual source confirmation).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** For <6/60 (<20/200), the continuation specifies 15° initial axis movement, the five-band axis-step table, ±1.00-D cylinder refinement, and the 0.25-D opposite-sign sphere correction per 0.5-D cylinder change for cylinder ≥1.00 D.

### N-P121-01 — Tumbling-E outcome/chart-scale definition

- **Exact source location:** `joi190092supp2_prod.pdf#page=121` (printed p. 57, §5.2.2.B).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** Visual acuity is again explicitly a secondary outcome. Charts 1, 2, and R are Precision Vision **2305, 2305a, 2305b**, respectively, with **14 lines** of high-contrast tumbling E characters; letter size progresses geometrically and logMAR progresses arithmetically. Chart 1 is right eye, Chart 2 left eye, Chart R refraction.

### N-P122-01 — Tumbling-E equipment, illumination and lane calibration

- **Exact source location:** `joi190092supp2_prod.pdf#page=122` (printed p. 58, §5.2.2.B).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** Light box: 24.75 in (62.9 cm) × 25.75 in (65.4 cm) × 7 in (17.8 cm); row 3 is 0.8 logMAR, 45 letters, 20/125 Snellen and placed 49 ± 2 in (124.5 ± 5.1 cm) high. Illumination is ≤15 foot-candles with light box off; two 20-W tubes decrease 5% in first 100 h and 5% in next 2,000 h, warm up about 4 days (~96 h), and are replaced annually. Test distances are 4 m (157.5 in) and 1 m (39 3/8 in); wall-box depth is 7 in and stand allowance 13 in.

### N-P123-01 — Tumbling-E test stopping/relocation thresholds

- **Exact source location:** `joi190092supp2_prod.pdf#page=123` (printed p. 59, §5.2.2.B).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** Test each eye after refraction at 4 m. Stop a row from Row 3 or below when **3 or fewer** letters are correct. If fewer than **10 letters** are read at 4 m, retest at **1 m**; only the first **6 rows** are needed at 1 m. If fewer than **10 letters** are read at 1 m, proceed to count fingers, then hand motion, then light perception.
- **Relationship/definition:** These explicit thresholds differ from the letter-chart branch (N-P112-01); they should not be treated as a cross-source contradiction without confirming which chart protocol was used.

### N-P124-01 — Tumbling-E low-vision thresholds and visual-acuity scoring formula

- **Exact source location:** `joi190092supp2_prod.pdf#page=124` (printed p. 60, §5.2.2.B).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** Count fingers: at 1 m, 1/2/5 fingers in random order, **5** trials, count fingers if **3/5** correct. Hand motion: at 0.5 m, **5** trials, present if **4/5** correct. Light perception: 0.5 m, light presented **4** times. Score rule: if **10 or more** letters of the first line are correct at 4 m, score = (letters correct at 4 m) **+ 30**. If **3 or fewer** letters of the largest 4-m line are correct, score = letters correct at 1 m. If **3 or fewer** letters are read at 1 m, low-vision status is converted to logMAR using the Visual Acuity Calculation Table.
- **Relationship/definition:** This is the explicit score formula for the tumbling-E branch; it has a conditional +30 offset and a separate low-vision logMAR conversion.

### N-P125-01 — Tumbling-E score ceiling, Snellen conversion, and certification timing

- **Exact source location:** `joi190092supp2_prod.pdf#page=125` (printed p. 61, §§5.2.2.B–5.2.3.B).
- **Main-paper key:** `VA_SECONDARY_OUTCOME`.
- **Direct observation:** Highest attainable 4-m visual-acuity score is **100**. Snellen equivalent is the hardest line with at least **4/5** letters correct. Certification is valid **18 months ± 2 months**; at least **2** certified technicians are required at each site.

### N-P125-02 — Cataract grade definition

- **Exact source location:** `joi190092supp2_prod.pdf#page=125` (printed p. 61, §5.3.1).
- **Main-paper key:** `CATARACT_GRADE`.
- **Direct observation:** Nuclear, cortical and posterior-subcapsular opacity: 1 = clinical presence, 2 = clinical significance, 3 = severe occurrence; half grades permitted (example **1.5**).

### N-P126-01 — Cataract categories and SUN anterior-chamber-cell scale

- **Exact source location:** `joi190092supp2_prod.pdf#page=126` (printed p. 62, §§5.3.1–5.3.2).
- **Main-paper key:** `CATARACT_GRADE`; `CONTROLLED_INFLAMMATION_PRIMARY_SECONDARY`.
- **Direct observation:** Cataract categories are <1, 1, 1.5, 2, 2.5, >3. SUN AC-cell grades in a **1 mm × 1 mm** slit-lamp field: 0 = <1 cell; 0.5+ = 1–5; 1+ = 6–15; 2+ = 16–25; 3+ = 26–50; 4+ = >50. Assessment is in a completely dark room before dilation.
- **Relationship/definition:** Baseline eligibility at ≥1+ AC cells (N-P097-01) maps to **at least 6 cells per stated field**, subject to this protocol's measurement conditions.

### N-P127-01 — Flare, vitreous-cell, and vitreous-haze measure definitions

- **Exact source location:** `joi190092supp2_prod.pdf#page=127` (printed p. 63, §5.3.2).
- **Main-paper key:** `CONTROLLED_INFLAMMATION_PRIMARY_SECONDARY`.
- **Direct observation:** Flare grades: 0 none; 1+ faint; 2+ moderate (iris/lens details clear); 3+ marked (details hazy); 4+ intense (fibrin/plastic aqueous); flare is not a controlled-inflammation criterion. Vitreous-cell grades in a **1 mm × 0.5 mm** field after dilation: 0 no cells; 0.5+ 0–5; 1+ 6–10; 2+ 11–20; 3+ 21–50; 4+ >50; vitreous cells are not a controlled-inflammation criterion. NEI vitreous haze is used for **all primary and secondary outcome measures**; the 9-point Miami scale is separately assessed. A media opacity may make haze grading unreliable and is recorded as such.
- **Relationship/definition:** NEI, not Miami, is the stated outcome scale. AC cells, NEI haze, flare, and vitreous cells are distinct constructs and scales.

### N-P128-01 — NEI vitreous-haze grade-to-description table

- **Exact source location:** `joi190092supp2_prod.pdf#page=128` (printed p. 64, Figure 1).
- **Main-paper key:** `CONTROLLED_INFLAMMATION_PRIMARY_SECONDARY`.
- **Direct observation:** NEI haze grade 0 = clear; 0.5+ = slight blurring of optic-disc margin with normal nerve-fibre-layer striations/reflex not visualized; 1+ = opacities without obscuration of retinal details; 2+ = few opacities with mild blurring of optic-nerve/retinal-vessel details; 3+ = optic nerve head/vessels significantly blurred but visible; 4+ = dense opacity obscuring optic nerve head. Grading is in a completely dark room.
- **Relationship/definition:** The protocol threshold ≥1+ NEI haze in N-P097-01 corresponds to at least the grade-1+ description here, not a 9-point Miami value.

## Statistical-definition record

### S-P127-01 — Exploratory NEI–Miami/fundus-photo comparison

- **Exact source location:** `joi190092supp2_prod.pdf#page=127` (printed p. 63, §5.3.2).
- **Main-paper key:** `CONTROLLED_INFLAMMATION_PRIMARY_SECONDARY`.
- **Direct observation:** The manual states that an exploratory analysis will correlate NEI and Miami vitreous-haze measurements; clinical haze measurements will also be compared with objective reading-centre fundus-photo grading.
- **Definition limits:** No correlation coefficient, model, population, timepoint, confidence interval, P-value convention, or missing-data rule is specified on these assigned pages. This is a planned relationship, not a reported inferential result.

## Local count and limitations

- **Numeric/reporting relationship records:** 33 (N-P097-01 through N-P128-01, including the two p. 125 records; identifiers describe local records and are not stable package-wide IDs).
- **Statistical-definition records:** 1 (S-P127-01); **reported effect estimates/intervals/P values/test statistics:** 0 in this range.
- **No-applicable page units:** 1 (PDF p. 101), explicitly recorded above.
- **Limitations:** The machine-text layer is absent on six assigned pages, but direct visual confirmation supplied their continuation tables/text. Letter-chart visit-score conversion is not numerically specified within assigned pp. 97–128; the tumbling-E formula must not be substituted for it without source confirmation. No candidate conclusion is made in this extraction artifact.
