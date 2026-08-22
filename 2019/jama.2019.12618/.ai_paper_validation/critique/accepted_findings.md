# Critic adjudication — JAMA 2019.12618

## Review scope and result

This adjudication reviews only the candidates and evidence presented in
`.ai_paper_validation/verification/evidence_verification.md`. It does not search
for or introduce new issues.

| Candidate | Critic decision | Final severity | Category | Evidence-card completeness |
|---|---|---|---|---|
| V1 | Retained | Minor | Presentation inconsistency | Complete |
| V2 | Retained | Minor | Arithmetic inconsistency | Complete |
| V3 | Retained | Minor | Arithmetic inconsistency | Complete |
| V4 | Retained | Minor | Arithmetic inconsistency | Complete |
| V5 | Rejected | — | Proposed cross-document inconsistency | Incomplete for a finding |

**Final retained issue count: 4 (V1, V2, V3, V4).**

No retained finding is Major or Uncertain. Each retained issue is a localized
denominator-label or displayed-percentage inconsistency; none establishes an
error in the underlying event count, patient-level data, clinical
interpretation, or study methodology.

## Retained findings

### V1 — Table 3 denominator label does not match the displayed percentages

- **Critic decision:** Retained
- **Category:** Presentation inconsistency
- **Severity:** Minor
- **Issue statement:** Main Table 3 labels the mycophenolate mofetil column
  `n = 109`, but its displayed percentages use 108 recipients; footnote b
  explains the one nonrecipient but the percentage denominator is not stated in
  the column header.
- **Location:** Document ID `JAMA2019-12618-MAIN`;
  `jama_rathinam_2019_oi_190092.pdf`; PDF p. 8; Table 3; header and
  Mycophenolate Mofetil column; rows “Elevated ALT or AST (2 to 5 times upper
  limit of normal <28 d)” and “Headache.”
- **Source evidence:** Measurement header: “No. (%) of Patients Reporting ≥1
  Adverse Event.” Column header: “Mycophenolate Mofetil (n = 109)ᵇ.” Cells:
  `8 (7.4)` and `45 (41.7)`. Footnote b: “One patient in the mycophenolate
  mofetil group never received mycophenolate mofetil due to medical
  contraindication discovered postrandomization.”
- **Reported versus comparator:** The printed header supplies 109, whereas the
  footnote-derived exposed denominator is `109 − 1 = 108`.
- **Reproducible calculation:** `8/109 × 100 = 7.339%`, which rounds to 7.3%,
  while `8/108 × 100 = 7.407%`, which rounds to the reported 7.4%. Likewise,
  `45/109 × 100 = 41.284%`, which rounds to 41.3%, while
  `45/108 × 100 = 41.667%`, which rounds to the reported 41.7%. At one-decimal
  precision, the n=109 results fall outside the rounding intervals for both
  displayed percentages.
- **Bounded impact:** The inconsistency is confined to denominator presentation
  for mycophenolate percentages in Table 3. Footnote b makes the likely use of
  the 108-recipient safety population understandable, so this does not
  contradict the event counts or establish different patient-level events.
- **Human verification:**
  1. On PDF p. 8, confirm the `n = 109` header, superscript b, footnote text, and
     the two cited cells.
  2. Recalculate both cells using 109 and 108. Values of 7.4% and 41.7% only
     with 108 confirm the denominator-label mismatch.
- **Critic rationale:** The finding is document-grounded, reproducible, and
  within the Presentation inconsistency category. The footnote prevents a
  stronger interpretation but does not make the printed `n = 109` agree with
  the percentages calculated from 108.
- **Evidence-card completeness:** Complete. It supplies an issue statement,
  allowed category, severity, exact locations, labelled source values, a direct
  comparison, reproducible arithmetic and rounding, bounded impact, and
  resolution-oriented verification steps.

### V2 — Table 3 reports 14 of 107 as 13.0%

- **Critic decision:** Retained
- **Category:** Arithmetic inconsistency
- **Severity:** Minor
- **Issue statement:** Main Table 3 reports methotrexate elevated ALT or AST as
  `14 (13.0)`, although 14 of the stated 107 patients rounds to 13.1%.
- **Location:** Document ID `JAMA2019-12618-MAIN`;
  `jama_rathinam_2019_oi_190092.pdf`; PDF p. 8; Table 3; Nonserious laboratory;
  row “Elevated ALT or AST (2 to 5 times upper limit of normal <28 d)”;
  Methotrexate column.
- **Source evidence:** Column header: “Methotrexate (n = 107).” Target cell:
  `14 (13.0)`. Same table and column, Nonserious systemic “Allergic reaction”
  row: `14 (13.1)`.
- **Reported versus comparator:** Reported 13.0%; the numerator and header
  denominator, as well as the same-numerator internal comparator, give 13.1%.
- **Reproducible calculation:** `14/107 × 100 = 13.0841%`, which rounds to
  13.1% to one decimal. The value lies outside the `[12.95%, 13.05%)` interval
  that would round to 13.0%.
- **Bounded impact:** One percentage cell is understated by 0.1 displayed
  percentage point. The count of 14 and other Table 3 results are unaffected.
- **Human verification:**
  1. Confirm the n=107 header, `14 (13.0)` target cell, and `14 (13.1)`
     allergic-reaction cell on PDF p. 8.
  2. Compute `14/107 × 100`; a result rounding to 13.1% confirms the issue
     unless a different row-specific denominator is documented.
- **Critic rationale:** The count, denominator, and displayed percentage are
  directly reported in one table, and the arithmetic comparison is valid.
  Nothing in the verifier output identifies a row-specific denominator.
- **Evidence-card completeness:** Complete. All required location, source,
  comparison, calculation, impact, and human-verification elements are present.

### V3 — eTable 9 reports 1 of 20 as 3.4%

- **Critic decision:** Retained
- **Category:** Arithmetic inconsistency
- **Severity:** Minor
- **Issue statement:** Supplement eTable 9 reports serious systemic diarrhea in
  the mycophenolate mofetil N=20 column as `1 (3.4)`, although one of 20 is
  5.0%; 3.4% corresponds to the adjacent N=29 denominator.
- **Location:** Document ID `JAMA2019-12618-SUPP-RESULTS`;
  `joi190092supp1_prod.pdf`; PDF p. 15; eTable 9; Serious Systemic;
  “Diarrheaᵇ” row; Mycophenolate Mofetil column.
- **Source evidence:** Column headers: “Methotrexate (N=29)” and
  “Mycophenolate Mofetil (N=20).” Target cell: `1 (3.4)`. In the same N=20
  column, Low hemoglobin and Allergic reaction each read `1 (5.0)`. The
  adjacent N=29 column repeatedly displays `1 (3.4)`.
- **Reported versus comparator:** Reported 3.4%; the N=20 calculation and
  same-column one-patient cells give 5.0%.
- **Reproducible calculation:** `1/20 × 100 = 5.0%`; `1/29 × 100 = 3.4483%`,
  which rounds to 3.4%. The reported value is 1.6 percentage points below the
  stated-denominator result.
- **Bounded impact:** The displayed percentage for one serious adverse-event
  cell is affected. The visible event count remains one; the evidence does not
  determine whether a production correction should change the percentage,
  count, or denominator.
- **Human verification:**
  1. Confirm that `1 (3.4)` is placed under Mycophenolate Mofetil N=20 on PDF
     p. 15.
  2. Compute `1/20 × 100` and compare it with the same-column `1 (5.0)` cells.
     A result of 5.0% confirms the displayed inconsistency.
- **Critic rationale:** The evidence establishes the cell’s column placement
  and provides both arithmetic and same-table comparators. The finding remains
  limited to the internal display rather than speculating about the production
  cause or underlying data.
- **Evidence-card completeness:** Complete. All required location, source,
  comparison, calculation, impact, and human-verification elements are present.

### V4 — eTable 4 reports 5 of 108 as 4.7%

- **Critic decision:** Retained
- **Category:** Arithmetic inconsistency
- **Severity:** Minor
- **Issue statement:** Supplement eTable 4 reports mycophenolate eye floaters
  as `5 (4.7)`, although five of the stated 108 recipients rounds to 4.6%.
- **Location:** Document ID `JAMA2019-12618-SUPP-RESULTS`;
  `joi190092supp1_prod.pdf`; PDF p. 10; eTable 4; “Eye floaters” row;
  Mycophenolate Mofetil column.
- **Source evidence:** Column header: “Mycophenolate Mofetil (N=108).” Target
  cell: `5 (4.7)`. Adjacent Methotrexate N=107 cell: `5 (4.7)`. Footnote a:
  “Out of 107 patients who received methotrexate and 108 patients who received
  mycophenolate mofetil.”
- **Reported versus comparator:** Reported 4.7%; the stated N=108 calculation
  gives 4.6%. The displayed percentage instead matches the adjacent N=107
  calculation.
- **Reproducible calculation:** `5/108 × 100 = 4.6296%`, which rounds to 4.6%.
  `5/107 × 100 = 4.6729%`, which rounds to 4.7%. The N=108 result falls outside
  the `[4.65%, 4.75%)` interval that would round to 4.7%.
- **Bounded impact:** One displayed percentage is overstated by 0.1 percentage
  point. The event count of five is unaffected.
- **Human verification:**
  1. Confirm the N=108 header, footnote, and `5 (4.7)` cell on PDF p. 10.
  2. Compute `5/108 × 100`; a result rounding to 4.6% confirms the issue unless
     an explicit row-specific denominator replaces 108.
- **Critic rationale:** The header and footnote independently identify the
  denominator, the calculation is reproducible, and the finding is a narrow
  arithmetic inconsistency without an unsupported claim about its cause.
- **Evidence-card completeness:** Complete. All required location, source,
  comparison, calculation, impact, and human-verification elements are present.

## Rejected candidate

### V5 — Proposed cross-document population inconsistency

- **Critic decision:** Rejected
- **Proposed category:** Cross-document inconsistency
- **Severity:** Not assigned
- **Rationale:** The compared denominators are not shown to represent the same
  analysis population. Supplement p. 14 eTable 8 reports interval adverse
  events from six to 12 months among patients continuing after success
  (`N=62`, `N=56`), whereas main p. 3 Figure 1 identifies `60` and `54`
  patients included in the 12-month secondary analysis and main p. 6 Table 2
  reports 12-month point-outcome denominators. The verifier also records
  withdrawals and loss before the 12-month visit. Because an interval safety
  population need not equal a 12-month point-efficacy population, the numerical
  difference alone does not establish an inconsistency.
- **Evidence-card completeness:** Incomplete for retention. Necessary
  document-grounded evidence that eTable 8 and the main-article denominators are
  intended to describe the identical cohort is unavailable. Retaining the
  candidate would require speculation about analysis-population definitions.

