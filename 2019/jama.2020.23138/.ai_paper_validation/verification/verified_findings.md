# Evidence Verifier — Verification Round 1

Status: Complete  
Candidates: 8  
Accepted: 8  
Uncertain: 0  
Rejected: 0

Only the main article and results supplement were verified. The protocol, SAP, and data-sharing statement were not opened.

## V1. Primary SF-36 Analysis Switches Between Normalized and Raw Scores

- Disposition: **Accepted (Verified)**
- Category/severity: Cross-document inconsistency; moderate
- Locations:
  - `JAMA2020-23138-SUPP03-RESULTS`, `joi200126supp3_prod_1607962892.5372.pdf`, PDF p. 5, eMethods, “Quality of life tools and scoring.”
  - `JAMA2020-23138-MAIN`, `jama_kotecha_2020_oi_200126_1607962892.52158.pdf`, PDF p. 1 abstract Results; p. 6 Table 2 and Primary End Point; p. 9 Discussion.
- Evidence:
  - Supplement p. 5: “domain and summary scores were primarily analyzed using raw values.”
  - Main p. 1: “primary outcome of normalized SF-36 PCS at 6 months.”
  - Main p. 6 normalized row: 1.4 (95% CI −1.1 to 3.8), P=.28.
  - Main p. 6 raw row: 1.3 (95% CI −1.2 to 3.9), P=.30.
  - Main p. 9 Discussion says the upper 95% confidence limit for the primary outcome was 3.9.
- Logic: The supplement designates raw scoring as primary, the abstract/narrative use normalized scoring, and Discussion’s 3.9 limit uniquely matches the raw row. Differences are 0.1 PCS point in effect and CI endpoints and 0.02 in P value, exceeding displayed precision.
- Bounded impact: The null conclusion is unchanged, but the designated primary estimate, CI, and P value are ambiguous.
- Human verification:
  1. Confirm the supplement’s raw-score primary-analysis statement.
  2. Compare both main Table 2 rows.
  3. Confirm abstract/narrative use the normalized row.
  4. Confirm Discussion’s 3.9 uniquely matches the raw row.
  5. Resolve which row was the intended prespecified primary analysis.

## V2. Adverse-Event χ² Uses a Denominator Inconsistent With the Stated Analysis Set

- Disposition: **Accepted (Verified)**
- Category/severity: Statistical reporting inconsistency; moderate
- Locations:
  - Main PDF p. 4, Statistical Analysis and Results; p. 6, Adverse Events; p. 9, Table 4.
  - Results supplement p. 17, eTable 5 and footnote a.
- Evidence:
  - Main p. 4: full analysis set comprised randomized patients receiving at least one dose; each group had 80.
  - Main p. 6: 20 patients (25%) vs 51 (64%), χ²=24.91, P<.001.
  - Main Table 4 headings: digoxin n=80, bisoprolol n=80.
  - Supplement eTable 5 repeats 20 (25%), 51 (64%), total 71 (44%).
- Calculation: For 20/80 vs 51/80, Pearson χ² is

  `160 × (20×29 − 60×51)^2 / (80×80×71×89) = 24.3330`,

  which rounds to 24.33, not 24.91. With an untreated participant added as a digoxin non-event, 20/81 vs 51/80 gives

  `161 × (20×29 − 61×51)^2 / (81×80×71×90) = 24.9077`,

  which rounds to 24.91. Supplementary 12 (7%) and 28 (17%) totals also fit denominator 161 under ordinary rounding better than denominator 160.
- Bounded impact: The safety-analysis denominator is inconsistent or unstated. Both χ² values yield P<.001, so significance is unchanged.
- Human verification:
  1. Confirm the full-analysis-set definition and 80/80 counts.
  2. Confirm 20, 51, and χ²=24.91.
  3. Recalculate with 80/80; expected χ²=24.333.
  4. Recalculate with 81/80; expected χ²=24.908.
  5. Inspect source analysis output to determine the actual denominator/test.

## V3. Repeated Digoxin Baseline Summaries Differ Despite Identical n=80 Labels

- Disposition: **Accepted (Verified)**
- Category/severity: Statistical reporting inconsistency; minor
- Locations:
  - Main PDF p. 5, Table 1, digoxin n=80.
  - Main PDF p. 7, Table 3, baseline digoxin n=80.
  - Results supplement p. 14, eTable 2, baseline digoxin n=80.
- Evidence/comparison:

  | Measure | Main Table 1 | Main Table 3 / supplement eTable 2 |
  |---|---:|---:|
  | NT-proBNP, median (IQR), pg/mL | 1095 (715–1527) | Main Table 3: 1091 (710–1522) |
  | 12-lead ECG, mean (SD), /min | 100.1 (16.8) | 100.3 (16.8) |
  | Apex, mean (SD), /min | 98.2 (15.1) | 98.3 (15.1) |
  | Radial pulse, mean (SD), /min | 87.8 (12.1) | 87.8 (12.0) |

- Calculation: NT-proBNP median differs by 4 pg/mL and both IQR limits by 5 pg/mL; ECG mean differs by 0.2/min; apex mean and radial SD differ by 0.1/min. These exceed displayed precision, and no different subset/timing is disclosed.
- Bounded impact: Small baseline-description discrepancies; outcome comparisons are not shown to change.
- Human verification:
  1. Compare cited cells and confirm each n=80 label.
  2. Check footnotes for a different subset/timing/derivation.
  3. Resolve against the baseline dataset/version used for each table.

## V4. Table 3 Direction Footnote Reverses NYHA Interpretation

- Disposition: **Accepted (Verified)**
- Category/severity: Presentation inconsistency; minor
- Locations:
  - Main PDF p. 7, Table 3, NYHA and NT-proBNP rows, footnotes b/h/j.
  - Results supplement p. 12, eFigure 5 caption.
- Evidence:
  - Main Table 3 footnote b: “Higher values indicate better response with digoxin therapy.”
  - NYHA: digoxin 1.5, bisoprolol 2.0; adjusted difference −0.6 (95% CI −0.8 to −0.4).
  - Table footnote h defines lower NYHA classes as less limitation.
  - Supplement caption: “negative values indicating superiority of digoxin.”
  - NT-proBNP ratio: 0.77 (0.64–0.92).
- Logic/calculation: NYHA 1.5−2.0≈−0.5 and adjusted −0.6 favor digoxin; 0.77 means the digoxin geometric mean is about 23% lower than reference. A blanket higher-is-better rule does not apply.
- Bounded impact: Values remain interpretable, but the footnote can reverse treatment-direction interpretation.
- Human verification:
  1. Compare footnote b with the NYHA class definitions and −0.6 difference.
  2. Confirm the supplement’s negative-is-superior caption.
  3. Confirm 0.77<1 indicates a lower digoxin geometric mean.
  4. Restrict or replace the general footnote.

## V5. eTable 2 Heart-Rate Footnote Incorrectly Refers to Quality of Life

- Disposition: **Accepted (Verified)**
- Category/severity: Presentation inconsistency; minor
- Location: Results supplement PDF p. 14, eTable 2, footnote a.
- Evidence:
  - Title: “Resting and exertional heart rate.”
  - Rows use beats/min.
  - Footnote: “hence higher values represent better quality of life in the digoxin arm.”
- Logic: eTable 2 contains ECG/apex/radial/pulse-deficit/exertional heart-rate endpoints, not a quality-of-life score.
- Bounded impact: Invalid explanatory text; numerical results are unchanged.
- Human verification:
  1. Confirm title, units, and footnote.
  2. Verify that no QoL scale appears in the table.
  3. Replace with heart-rate-specific reference-direction wording.

## V6. Figure 1 Reports 161 Randomized but Accounts for Only 160 in Allocation Branches

- Disposition: **Accepted (Verified)**
- Category/severity: Participant flow inconsistency; minor
- Locations:
  - Main PDF p. 3, Figure 1 nodes/footnote b.
  - Main PDF p. 4, Sample Size and Results.
- Evidence:
  - Figure: 161 Randomized; 80 randomized to digoxin; 80 randomized to bisoprolol.
  - Footnote: one person withdrew after randomization before therapy.
  - Main p. 4: the participant did not complete baseline or start treatment and was replaced; 160 received at least one dose.
- Calculation/visual logic: 80+80=160, leaving 161−160=1 randomized participant absent from the allocation branches. Original-PDF inspection showed no separate allocation/nonreceipt/disposition branch.
- Bounded impact: The text explains the 160-person treated cohort, but the figure omits the participant’s allocated group/disposition. Analysis counts remain coherent.
- Human verification:
  1. Inspect original Figure 1.
  2. Sum branches and compare with the randomization node.
  3. Confirm footnote and p. 4 explanation.
  4. Check whether any allocation/nonreceipt branch accounts for the participant.

## V7. eFigure 4 Labels Mental Health as “SF35-MH”

- Disposition: **Accepted (Verified)**
- Category/severity: Presentation inconsistency; minor
- Locations:
  - Results supplement p. 11, eFigure 4 panel A, left-side domain labels.
  - Same-page caption.
  - Results supplement p. 15, eTable 3, SF36 Mental health row.
- Evidence:
  - Visible panel label: `SF35-MH`.
  - Caption: “SF36 domains are … MH = mental health.”
  - eTable 3: SF36 section, Mental health.
- Logic: A fresh 300-dpi original-PDF render clearly shows `5`; this is not an OCR substitution. Neighboring/caption/table labels identify the instrument as SF36.
- Bounded impact: One-character figure-label error; numerical bars are not affected.
- Human verification:
  1. Magnify original eFigure 4 panel A.
  2. Confirm `SF35-MH` between `SF36-SF` and `SF36-VT`.
  3. Compare with the caption and eTable 3.

## V8. eTable 2 Baseline Peripheral Pulse Deficit Conflicts With Component Means

- Disposition: **Accepted (Verified)**
- Category/severity: Arithmetic inconsistency; minor
- Location: Results supplement p. 14, eTable 2, baseline digoxin n=80, apex/radial/pulse-deficit rows and footnote b.
- Evidence:
  - Apex: 98.3 (SD 15.1) beats/min.
  - Radial: 87.8 (SD 12.0) beats/min.
  - Peripheral pulse deficit: −10.3 (SD 9.4) beats/min.
  - Footnote: difference between radial and apex resting pulse.
- Calculation: `87.8−98.3=−10.5 beats/min`, differing from −10.3 by 0.2 beats/min. One-decimal rounding intervals for the component-implied difference, approximately (−10.60, −10.40), do not overlap the displayed −10.3 interval [−10.35, −10.25). For the same paired n, mean(radial−apex)=mean(radial)−mean(apex), so paired averaging does not resolve it.
- Bounded impact: Small error in one displayed baseline mean; follow-up contrasts/conclusions are not shown to change.
- Human verification:
  1. Confirm the three values, n=80 header, and subtraction direction.
  2. Recalculate; expected displayed result is −10.5 beats/min.
  3. Check rounding intervals.
  4. Resolve against participant-level paired calculations or table-generation output.
