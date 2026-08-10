# Statistical consistency checker response — DOC-001 and DOC-004

## Scope

- **DOC-001:** `jama_combes_2025_oi_250087_1766516490.94011.pdf`
- **DOC-004:** `joi250087supp3_prod_1766516490.97011.pdf`
- Evidence used: the main-text result evidence map, the result-relevant supplementary evidence map, the source-linked native page extracts, and rendered result figures.
- Protocol, SAP, administrative files, web sources, and external knowledge were not used.

## Local candidate 1

### Issue statement

The reported day-30 MACE composite is internally impossible under the main article's definition because the placebo composite count (36) is smaller than its dialysis component count (38); the supplement's MACE figure repeats the composite total while omitting dialysis from the displayed definition.

- **Category:** Statistical reporting inconsistency
- **Severity:** Moderate

### Exact evidence locations and values

1. **Reported definition**
   - **Document:** DOC-001, `jama_combes_2025_oi_250087_1766516490.94011.pdf`
   - **Location:** PDF p. 3 (journal p. 62), Methods, Outcomes, right column.
   - **Verbatim excerpt:** “major adverse cardiovascular events (death, heart transplant, escalation to need for left ventricular assist device, stroke, dialysis, or heart failure rehospitalization) at days 30 and 60”

2. **Reported composite and component**
   - **Document:** DOC-004, `joi250087supp3_prod_1766516490.97011.pdf`
   - **Location:** PDF p. 5, eTable 3, rows “Major adverse cardiovascular events during first 30 days” and “Dialysis by day 30,” Placebo column.
   - **Reported values:** day-30 MACE **36/104 (34.6%)**; dialysis by day 30 **38/104 (36.5%)**.

3. **Comparator display**
   - **Document:** DOC-004, `joi250087supp3_prod_1766516490.97011.pdf`
   - **Location:** PDF p. 13, eFigure 4, title and left (D30) panel, cumulative number of events at day 30.
   - **Displayed definition:** “MACE Defined as Death, Cardiac Transplant, Escalation to Permanent Left Ventricular Assist Device, Stroke, or Re-Hospitalization for Heart Failure” — **dialysis is omitted**.
   - **Displayed placebo event total at day 30:** **36**, repeating the eTable 3 composite count.

### Reported-versus-comparator comparison

- **Reported rule in DOC-001:** every participant with dialysis by day 30 is a day-30 MACE case because dialysis is one component of the composite.
- **Reported result in DOC-004:** only 36 placebo participants had day-30 MACE, while 38 placebo participants had dialysis by day 30.
- **Supplementary comparator:** eFigure 4 uses the 36-event MACE total but defines MACE without dialysis.

### Reproducible logical check

For a composite outcome \(C=A\cup B\cup \ldots\), its count cannot be smaller than the count of any included component:

\[
n(C) \ge n(B).
\]

Using the reported placebo values:

\[
n(\mathrm{MACE}_{D30}) = 36,\qquad n(\mathrm{dialysis}_{D30}) = 38,
\]

so

\[
36-38=-2.
\]

The composite is therefore **2 participants smaller** than a stated component. The same contradiction is visible in percentages: **34.6% < 36.5%**.

**Tolerance:** none for integer nesting. Percentage rounding cannot resolve a 36-versus-38 count contradiction.

### Bounded impact

At least 2 placebo participants with reported dialysis cannot be accommodated in the reported 36-participant day-30 composite under the main-text definition. The package alone does not establish whether dialysis was mistakenly included in the main-text definition or whether the composite count/figure omitted qualifying dialysis events. Until resolved, the day-30 MACE definition, count, risk difference, relative risk, and curve interpretation are not jointly verifiable.

### Human verification steps

1. On DOC-001 PDF p. 3, confirm that dialysis is explicitly listed as a MACE component at days 30 and 60.
2. On DOC-004 PDF p. 5, confirm placebo day-30 MACE is 36/104 and placebo dialysis is 38/104.
3. Apply the nesting rule that a composite count must be at least as large as each included component; **36 < 38 confirms the inconsistency**.
4. On DOC-004 PDF p. 13, confirm that eFigure 4 omits dialysis from its definition and shows 36 cumulative placebo MACE events at day 30.
5. Resolve by checking the authors' intended MACE definition and participant-level derivation: exclusion of dialysis from the intended composite would resolve the nesting contradiction but confirm a definition error in DOC-001; inclusion of dialysis would require correction/recalculation of the composite results.

## Other screened relationships

No additional evidence-backed candidate was retained. Repeated primary-outcome estimates and subgroup hazard-ratio confidence intervals agree across DOC-001 and DOC-004. The distinct 60-day mortality P values (main text P=.78; supplementary log-rank P=.56) are explicitly or contextually tied to different tests and therefore were not treated as an error. The ventricular-arrhythmia risk-difference CI and relative-risk CI use different effect measures and may validly differ in null-value inclusion; no model-dependent inconsistency was inferred.
