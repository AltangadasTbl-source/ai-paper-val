# Figure, flow, caption, and visible-annotation consistency check — DOC-001 / DOC-003

## Scope and method

- **DOC-001:** `jama_cinciripini_2024_oi_240036_1716416465.98349.pdf`, PDF pages 1–10; rendered pages 3, 5, 6, and 7 were paired with page-linked native text and the main-text extractor.
- **DOC-003:** `joi240036supp2_prod_1716416466.01349.pdf`, PDF pages 4–35; rendered E-Figures 1–3 (pp. 14–16) and E-Tables 1–12 (pp. 17–35) were paired with page-linked native text and the results-supplement extractor.
- **Not inspected:** DOC-002 (protocol), DOC-003 pp. 1–3 and 36. These are **Not Audited by Design** under the package manifest.
- Source PDFs were not changed. No external source or unstated external knowledge was used. Ambiguous visual patterns were not treated as contradictions.

## Prioritized local candidates (10 maximum)

### FF-01 — Participant flow does not reconcile from assessed to randomized

- **Status:** Candidate
- **Category:** Participant flow inconsistency
- **Exact location:** DOC-001, PDF p. 6, **Figure 2, “The Flow Diagram Depicting Participant Flow Through the Trial,”** top eligibility/randomization portion.
- **Visible/source evidence:** Figure 2 displays **2232 assessed for eligibility**, **1740 excluded** (1052 declined + 688 ineligible), and **491 randomized**.
- **Basis:** `2232 − 1740 = 492`, not 491. The displayed exclusion subcounts also reconcile to 1740: declined `459+377+198+18=1052`; ineligible `134+103+88+84+61+47+32+31+21+20+67=688`. One assessed participant is therefore not represented between eligibility assessment and randomization.
- **Verification instruction:** Independently sum both exclusion lists and subtract the displayed total excluded from 2232; check whether an unprinted exclusion/nonrandomization category accounts for the remaining participant.

### FF-02 — Baseline sex counts exceed both displayed arm denominators

- **Status:** Candidate
- **Category:** Arithmetic inconsistency
- **Exact location:** DOC-001, PDF p. 5, **Table, “Baseline Measures and Demographics,”** Sex rows.
- **Visible/source evidence:** Each arm header is **n=245**. Each arm displays **Female 105 (42.9)** and **Male 145 (57.1)**.
- **Basis:** In each arm, `105+145=250`, exceeding the displayed denominator by 5; across arms, the table gives 500 sex observations for 490 analyzed participants. The percentages sum to 100%, and `57.1% of 245 ≈ 140`, not 145. DOC-001 p. 1/p. 4 also reports 210 women among 490 participants, consistent with the two female counts.
- **Verification instruction:** Recalculate sex counts against each n=245 header and inspect the source table proof to determine whether both male counts should be 140.

### FF-03 — Nearby participant-flow prose reverses attendance status

- **Status:** Candidate
- **Category:** Presentation inconsistency
- **Exact location:** DOC-001, PDF p. 4, **Results—Baseline Characteristics and Participant Flow**; compared with DOC-001 p. 6, **Figure 2**, continuation boxes/footnote.
- **Visible/source evidence:** Main text says the 40 CNRT and 35 varenicline participants “**who did attend rerandomization** were assigned to continue.” Figure 2 labels the same groups “**did not attend rerandomization**” and shows them assigned to continuation.
- **Basis:** “Did attend” and “did not attend” are opposite participant-disposition statements for the same 40 and 35 people.
- **Verification instruction:** Compare the sentence on p. 4 with the two nonattendance boxes on p. 6 and confirm whether “did” in the prose is missing “not.”

### FF-04 — Increased-CNRT lozenge dose differs between main and supplemental figure descriptions

- **Status:** Candidate
- **Category:** Cross-document inconsistency
- **Exact location:** DOC-001, PDF p. 3, **Figure 1, Sequential Multiple Assignment Randomized Trial Design**, increased-CNRT box; DOC-003, PDF p. 14, **E-Figure 1** caption.
- **Visible/source evidence:** Main Figure 1 describes increased CNRT as **two 21-mg patches and 2-mg lozenges**. Supplemental E-Figure 1 states **two 21-mg patches + 4 mg lozenge**. DOC-003 E-Tables 1–3 (pp. 17–20) and the E-Figure 2 caption (p. 15) define CNRT+ using a **2-mg lozenge**.
- **Basis:** The visible E-Figure 1 caption assigns a 4-mg lozenge where the main design figure and multiple supplemental exhibit definitions assign 2 mg.
- **Verification instruction:** Compare the CNRT+ wording on DOC-001 p. 3 and DOC-003 pp. 14–15 and confirm the intended lozenge strength from the exhibit definitions.

### FF-05 — Main secondary-outcome text uses n=42 where supplemental figures use N=77

- **Status:** Candidate
- **Category:** Cross-document inconsistency
- **Exact location:** DOC-001, PDF p. 7, **Secondary Outcomes of Abstinence**; DOC-003, PDF p. 15, **E-Figure 2**, and p. 16, **E-Figure 3**, “Varenicline → Non-abst → Varenicline” row; DOC-003 pp. 19–20, **E-Table 3** corresponding header.
- **Visible/source evidence:** DOC-001 says varenicline continuation was **0%; n=42** at EOT+30. E-Figure 2 displays **0/77**, N=77; E-Figure 3 also displays **0/77**; E-Table 3 labels this pathway **VAR (N=77)**. Main Figure 2 shows 42 rerandomized to continuation plus 35 nonattenders assigned to continuation, yielding 77.
- **Basis:** The main prose denominator does not match the visible analysis-cell denominator consistently used in the flow diagram and supplemental outcome figures. The neighboring CNRT prose uses n=90, which includes its analogous 40 assigned nonattenders, making the n=42 usage asymmetrical.
- **Verification instruction:** Check the analysis population intended for the p. 7 secondary-outcome sentence and determine whether the denominator should be 77 or whether a rerandomized-only analysis should have been explicitly identified.

### FF-06 — E-Table 4 reverses the sign of the varenicline switch-vs-stay contrast

- **Status:** Candidate
- **Category:** Statistical reporting inconsistency
- **Exact location:** DOC-003, PDF p. 21, **E-Table 4**, row “Varenicline-Non-Abst. → CNRT (switch) vs. Varenicline-(stay)”; DOC-001, PDF p. 5 result text and p. 7 **Figure 3**.
- **Visible/source evidence:** E-Table 4 prints switch-vs-stay ARD **+3% (1% to 4%)**. Main Figure 3 shows switch **0/41; 0%** and stay **2/77; 3%**. Main result text reports the same contrast as **−3% (−4% to −1%)**.
- **Basis:** For the table’s printed order “switch vs stay,” the displayed values and main prose support a negative, not positive, risk difference.
- **Verification instruction:** Confirm the contrast coding/order for this E-Table 4 row and compare it with the signed model output reported in DOC-001.

### FF-07 — E-Table 8 footnote denominator does not match the marked column

- **Status:** Candidate
- **Category:** Presentation inconsistency
- **Exact location:** DOC-003, PDF p. 32, **E-Table 8, Phase 2 Visit and Medication Compliance**, CNRT nonabstainer continuation column and footnote b.
- **Visible/source evidence:** The marked column header is **CNRT (N=50)b**. Footnote b says medication data were incomplete or missing for **2/51**.
- **Basis:** The footnote denominator 51 cannot describe the marked N=50 column as printed; 51 is the neighboring varenicline-switch column, which has no b marker.
- **Verification instruction:** Trace the footnote marker in the source table and verify whether the footnote should be 2/50 or marker b belongs on the neighboring N=51 column.

### FF-08 — E-Table 11’s six-month contrast sign conflicts with its header and E-Figure 3

- **Status:** Candidate
- **Category:** Statistical reporting inconsistency
- **Exact location:** DOC-003, PDF p. 35, **E-Table 11, Phase 2 Outcomes for Phase 1 Abstainers**, six-month row; DOC-003 p. 16, **E-Figure 3**, first two rows; DOC-003 p. 12, six-month abstainer prose.
- **Visible/source evidence:** E-Table 11’s header specifies **“ARD For CNRT vs. VAR”** and prints **+1% (−11% to 12%)**. E-Figure 3 displays CNRT **21/54; 39%** and varenicline **35/88; 40%**; the p. 12 prose describes a small benefit of varenicline.
- **Basis:** Under the table’s stated CNRT-minus-VAR direction, the displayed point estimates imply approximately −1 percentage point, whereas +1 corresponds to VAR minus CNRT. The same header yields the expected positive sign for EOT+30 (67% vs 56%; +11%).
- **Verification instruction:** Confirm the model contrast direction and whether the point estimate should be −1% or the header/order should change.

### FF-09 — Supplemental detailed prose corrupts percentages/credible limits shown in E-Figures/E-Tables

- **Status:** Candidate
- **Category:** Presentation inconsistency
- **Exact location:** DOC-003, PDF pp. 10–12, **Secondary Outcome Detailed Analysis**; compared with E-Figure 2 (p. 15), E-Figure 3 (p. 16), E-Table 9 (p. 33), and E-Table 11 (p. 35).
- **Visible/source evidence:** Examples: p. 10 prints CNRT-to-varenicline **1.0% (7.0%–1.3%)**, while E-Figure 2 shows **10% (7%–13%; 5/51)**; p. 10 prints CNRT+ **8.0% (5.0%–1.1%)**, while the figure shows **8% (5%–11%)**; p. 10 gives the switch ARD interval as **3.0%–1.0%**, while E-Table 9 shows **3%–10%**; p. 11 prints the abstainer ARD as **1.1% (−1.0%–22%)**, while E-Table 11 shows **11% (−1%–22%)**; p. 12 prints **−1.3%–1.1%**, while E-Table 11 shows **−11%–12%**.
- **Basis:** The prose values contain dropped digits/decimal shifts and descending intervals; the corresponding figure/table entries are mutually consistent with their displayed numerators and denominators.
- **Verification instruction:** Proofread pp. 10–12 against E-Figures 2–3 and E-Tables 9–11, restoring each point estimate and interval directly from the exhibit.

### FF-10 — E-Table 3 reverses the stated n (%) order for Employment and one race cell

- **Status:** Candidate
- **Category:** Presentation inconsistency
- **Exact location:** DOC-003, PDF p. 19, **E-Table 3**, “Race and ethnicity, n (%)” Other row and “Employment, n (%)” rows.
- **Visible/source evidence:** Sex, race, and income generally use count first, percentage second (eg, 21 [38.9]). Employment instead uses percentage first, count second (eg, **72.2 (39)** for N=54 and **74.5 (38)** for N=51). The “Other” race cell for varenicline nonabstainers switched to CNRT is uniquely **4.9 (2)**.
- **Basis:** The values are recoverable (39/54=72.2%; 2/41=4.9%) but their order contradicts the table’s n (%) labels and adjacent rows.
- **Verification instruction:** Reformat Employment and the 4.9 (2) race cell to count followed by percentage, or relabel those rows if percentage-first formatting was intended.

## Screened observations not advanced as candidates

- **Uncertain:** DOC-003 E-Table 8 uses rerandomized-only continuation Ns of 50 and 42, whereas E-Figures 2–3 and E-Table 3 use pathway Ns of 90 and 77. This may be a deliberate compliance-analysis restriction, so the population difference alone was not advanced.
- **Rejected:** Density-curve heights in DOC-001 Figure 3 and DOC-003 E-Figures 2–3 were not compared as common-scale frequencies. Their captions say each density has area 1 and height is scaled for depiction.
- **Rejected:** DOC-003 E-Table 12 confidence intervals are printed as separated endpoint pairs (eg, `0.03 0.70`) without a dash. The endpoints remain unambiguous and no nearby value contradicts them, so this was not advanced.

## Check result

- **Local candidates returned:** 10 (maximum reached).
- **Candidate mix:** Participant flow inconsistency (1), arithmetic inconsistency (1), cross-document inconsistency (2), statistical reporting inconsistency (2), presentation inconsistency (4).
- These are local candidates for coordinator deduplication and evidence verification, not final adjudicated findings.
