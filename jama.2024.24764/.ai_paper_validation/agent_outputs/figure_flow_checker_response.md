# Figure and Flow Consistency Check

- **Role:** `figure_flow_checker`
- **Scientific scope:** JAMA2024-24764-MAIN PDF pp. 3 and 9; JAMA2024-24764-SUPP3 PDF pp. 3-9.
- **Visual basis:** Retained page images were inspected for main Figure 1, main Figure 2, Supplementary eTables 1-6, and Supplementary eFigures 1-4. Captions, axes, labels, footnotes, visible counts, and cross-referenced main-text statements were checked.
- **Candidate count:** 3
- **Taxonomy used:** `Statistical reporting inconsistency` and `Presentation inconsistency`.

## Candidate 1 - Figure 2 subgroup inventory does not match the article's stated prespecified inventory

- **Status:** Candidate
- **Category:** Statistical reporting inconsistency
- **Locations and source evidence:**
  - `jama_atherton_2025_oi_240145_1741627844.85412.pdf`, PDF p. 4 (printed p. 856), **Statistical Analysis**: “Prespecified subgroup analyses” are described as including the minimization variables, operative procedure, skin preparation, BMI, country, assessment method, and randomization before/on or after March 11, 2020.
  - Same file, PDF pp. 2-3, **Randomization, Blinding, and Minimization**: the minimization variables are degree of contamination, presence of a stoma, and recruiting center.
  - Same file, PDF p. 9 (printed p. 861), **Figure 2**: the visible subgroup families include **Length of incision, cm** (`<15` and `>=15`; interaction `P=.42`), which is not named in the prespecified list. Figure 2 has no recruiting-center subgroup row.
  - Same file, PDF p. 1 abstract and PDF p. 8 discussion: the result is described as consistent across “all preplanned subgroups.”
- **Logical basis:** The displayed set used to support the “all preplanned subgroups” claim adds incision length, whose planned status is not identified in the article, while omitting recruiting center despite the Methods statement that prespecified analyses included the minimization variables. The article therefore does not let the reader determine whether incision length was prespecified/exploratory or whether a stated prespecified center analysis was omitted.
- **Verification instruction:** Compare the complete subgroup inventory in Statistical Analysis and the earlier explicit minimization-variable list with every Figure 2 family. Confirm that incision length lacks a prespecified designation and that recruiting center is absent. Do not open the SAP unless the coordinator separately authorizes this specific comparison.

## Candidate 2 - The pandemic subgroup population is narrower in Figure 2 than in the Methods description

- **Status:** Candidate
- **Category:** Statistical reporting inconsistency
- **Locations and source evidence:**
  - `jama_atherton_2025_oi_240145_1741627844.85412.pdf`, PDF p. 4 (printed p. 856), **Statistical Analysis**: the prespecified pandemic subgroup is described without a country restriction as patients randomized before vs on/after March 11, 2020.
  - Same file, PDF p. 9 (printed p. 861), **Figure 2**, SARS-CoV-2 pandemic subgroup: the footnote states **“UK-based patients only.”**
  - The Figure 2 pandemic-row event counts prove the restriction: iNPWT `60 + 19 = 79` and surgeon's preference `55 + 18 = 73`, exactly matching the Figure 2 UK country-row event counts (`79` and `73`) rather than the primary totals (`112` and `108`).
- **Logical basis:** The Methods presentation describes a patient-level date subgroup but does not disclose that Australian participants would be excluded. Figure 2 reports a UK-only analysis. This is a document-visible mismatch in the stated analysis population, even though the figure footnote locally discloses the restriction.
- **Verification instruction:** Re-read the full Statistical Analysis paragraph for any UK limitation and compare it with Figure 2 footnote `a` and the UK/pandemic event totals. If no narrative limitation is present, ask the authors whether the planned estimand was UK-only and correct either the Methods text or the figure description.

## Candidate 3 - Figure 2 omits subgroup denominators and undisclosed missing-category event counts

- **Status:** Candidate
- **Category:** Presentation inconsistency
- **Location and source evidence:**
  - `jama_atherton_2025_oi_240145_1741627844.85412.pdf`, PDF p. 9 (printed p. 861), **Figure 2**: the column headers give only the overall primary-analysis denominators (`n=394` per group). No category-specific denominators or missing/unknown rows are displayed, and the sole footnote concerns the UK-only pandemic analysis.
  - Primary events are `112` vs `108`.
  - BMI category events total `109` vs `103` (`5+33+30+41`; `4+37+30+32`), leaving `3` vs `5` primary events unrepresented.
  - Incision-length category events total `111` vs `103` (`21+90`; `22+81`), leaving `1` vs `5` unrepresented.
  - Assessment-method category events total `101` vs `107` (`77+15+9`; `78+16+13`), leaving `11` vs `1` unrepresented.
- **Logical basis:** The visible figure gives subgroup event counts and adjusted RRs but neither subgroup denominators nor the amount of missing subgroup data. Several families visibly omit primary-outcome events without explanation. The RRs cannot be reconciled from the displayed information, and the extent/direction of missing subgroup classification differs by randomized group.
- **Verification instruction:** Recalculate each family’s displayed event total against `112/108`, confirm that no missing/unknown footnote or denominator is present, and request category denominators plus missing counts (or an explicit complete-case subgroup-analysis note) for Figure 2.

## Uncertain lead - not a candidate

### Figure 1 total deaths vs Table 3 30-day mortality

- **Status:** Uncertain
- **Locations and evidence:** Main Figure 1, PDF p. 3, footnote `b`, reports `25` total deaths (`10` iNPWT, `15` surgeon's preference). Main Table 3, PDF p. 8, reports mortality **within 30 days** as `10/411` vs `14/410`, total `24`.
- **Reason not advanced:** Figure 1 says “total deaths” without an explicit 30-day qualifier. One surgeon's-preference death could have occurred after day 30, so the documents do not establish identical time windows. Do not infer a contradiction unless the time window for all 25 Figure 1 deaths is verified.
- **Verification instruction if pursued:** Establish from a supplied results page, not external material, whether Figure 1 footnote `b` is restricted to deaths within 30 days.

## Reconciled / rejected leads

- **Figure 1 arithmetic reconciles:** `2916 - 2076 = 840`; the nine exclusion reasons sum to `2076`; `424+416=840`; removing `13+6` gives `411+410=821`; `411-12=399` and `410-12=398`; and `394+5=399`, `394+4=398`.
- **Allocation adherence reconciles:** Figure 1 (`404/411`, `402/410`, `6`, `8`, and `1` undetermined) matches SUPP3 eTable 1, PDF p. 3.
- **Primary-outcome flow reconciles:** Main Table 3 reports `112/394` vs `108/394`; SUPP3 eTable 6 gives `109+0+3=112` and `107+1+0=108`; SUPP3 eFigure 3 repeats RR `1.03 (0.83-1.28)`.
- **Sensitivity figures reconcile:** SUPP3 eFigure 3 gives extreme missing-data RRs `1.19 (0.96-1.46)` and `0.89 (0.72-1.10)`; the corresponding 100% endpoints in eFigure 4 visually match and both CIs cross 1, consistent with the eFigure 4 caption.
- **No supported SUPP3 eFigure issue:** eFigure 1 labels were legible; eFigure 2's visible criteria did not contradict the main outcome definition; eFigure 3 axes/direction and estimates matched the article; eFigure 4 axes, direction note, extreme imputations, and caption were mutually consistent.
