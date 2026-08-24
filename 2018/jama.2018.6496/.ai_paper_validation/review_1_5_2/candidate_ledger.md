# Stable Candidate Ledger

Four distinct quality-control candidates were registered after merging only genuine duplicate discoveries from the numeric, cross-source, and statistical pass-1 lanes. The stable IDs will not be deleted, merged, or renumbered. Each remains **Pending Human Adjudication**.

## C001 — Reverse-ordered confidence-interval endpoints for all-patient first-attempt duration

- **Status:** Pending Human Adjudication
- **Category:** Statistical reporting inconsistency
- **Discovery provenance:** Numeric `NC-01`; cross-source provisional record 1; statistical pass-1 `P1-01`; canonical relationships N021, N043, S007, S030.
- **Exact source locations:** [DOC-001 Table 3 — PDF p. 7](../../jama_driver_2018_oi_180054.pdf#page=7); distinct clustered-model context [DOC-003 eTable 1 — PDF p. 2](../../joi180054supp2_prod.pdf#page=2).
- **Direct source evidence:** Main Table 3 prints all-patient medians `38 (29 to 51)` and `36 (25 to 54)` seconds, a difference `1 (4 to -1)`, and `P=.24`. The supplementary physician-clustered table prints the matched outcome as `1 s (-1 s to 4 s)` but states that its inferential columns were recalculated for clustering.
- **Comparator and rule:** In lower-to-upper interval notation `L to U`, endpoint order requires `L <= U`; the main display has `4 > -1`. The clustered interval supports checking the printed order but is not substituted for the unclustered result.
- **Calculation:** Printed endpoint comparison: `4 > -1`; ordering fails. Reordering would produce `-1 to 4`, but that is a diagnostic possibility, not an assigned correction.
- **Direct observation versus inference:** The reverse order is directly printed. A typesetting/transposition mechanism is inferred and not established by the package.
- **Alternative source-grounded interpretations:** An unstated reversed-endpoint convention or source-specific transcription could explain the display; other intervals in the paper use lower-to-upper order.
- **Exact human question:** What are the analysis-specific unclustered 95% limits from the reported Hodges-Lehmann procedure, and were the two printed endpoints transposed?

## C002 — Two-patient ETT+stylet denominator difference across linked hypoxemia outcomes

- **Status:** Pending Human Adjudication
- **Category:** Denominator, proportion, or total inconsistency
- **Discovery provenance:** Numeric `NC-02`; cross-source provisional record 2; canonical relationships N019, N027, N035.
- **Exact source locations:** [DOC-001 Table 3 — PDF p. 7](../../jama_driver_2018_oi_180054.pdf#page=7); [DOC-001 Table 5 — PDF p. 9](../../jama_driver_2018_oi_180054.pdf#page=9).
- **Direct source evidence:** Table 3 reports ETT+stylet first-attempt success without hypoxemia as `282/366 (77%)`. Table 5 reports ETT+stylet hypoxemia as `50/364 (14%)`. Both footnotes invoke the same hypoxemia threshold/window language and unavailable valid waveform; the Bougie denominators are 371 in both linked rows.
- **Comparator and rule:** The valid-waveform patient set for linked arm-specific hypoxemia classifications should be traceable, or a distinct eligibility/missing-data rule should be stated. The two printed ETT+stylet denominators differ by two.
- **Calculation:** `366 - 364 = 2` patients. This is not treated as a claim that the two outcomes are simple complements because first-attempt success is also part of the Table 3 outcome.
- **Direct observation versus inference:** The denominators and shared waveform qualification are direct. An outcome-specific exclusion or data-cleaning rule is inferred as possible but is not printed.
- **Alternative source-grounded interpretations:** Table 3 may require additional first-attempt ascertainment, or Table 5 may impose a complication-specific eligibility rule; neither source location names a rule that accounts for these two patients.
- **Exact human question:** Which ETT+stylet patient sets generated `282/366` and `50/364`, and is the two-patient difference intentional and documented?

## C003 — Protocol and published hypoxemia observation windows use different endpoint events

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Discovery provenance:** Numeric `NC-03`; cross-source provisional record 3; canonical relationships N035, S033, S034.
- **Exact source locations:** [DOC-002 protocol — PDF pp. 9-10](../../joi180054supp1_prod.pdf#page=9); [DOC-001 Table 3 — PDF p. 7](../../jama_driver_2018_oi_180054.pdf#page=7); [DOC-001 Table 5 — PDF p. 9](../../jama_driver_2018_oi_180054.pdf#page=9); [DOC-003 eTable 1 footnote — PDF p. 3](../../joi180054supp2_prod.pdf#page=3).
- **Direct source evidence:** The protocol observes hypoxemia from first-attempt start through one minute after inflation of the ETT cuff. The article and eTable describe hypoxemia during or within one minute after completion of the intubation attempt; the published attempt-duration definition ends at blade removal.
- **Comparator and rule:** The threshold agrees, but cuff inflation and attempt completion/blade removal are distinct named procedural events. Matched outcome definitions should agree or document an implemented change.
- **Calculation:** No numeric recalculation is applicable; the reproducible comparison is the nonidentity of the printed end events.
- **Direct observation versus inference:** The different endpoints are directly printed. A protocol amendment, shorthand, or operational equivalence is possible but not supplied.
- **Alternative source-grounded interpretations:** Cuff inflation and blade removal may have been operationally close or synchronized, or the analysis may implement an approved change absent from the package.
- **Exact human question:** Which endpoint ended hypoxemia surveillance in the analyzed data, and was the published attempt-completion wording a documented change from the protocol cuff-inflation endpoint?

## C004 — Protocol and published first-attempt-duration measures use different endpoint events

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Discovery provenance:** Numeric `NC-04`; cross-source provisional record 4; canonical relationships N036, S005, S007, S023, S027, S030.
- **Exact source locations:** [DOC-002 protocol — PDF p. 9](../../joi180054supp1_prod.pdf#page=9); [DOC-001 outcome methods — PDF p. 3](../../jama_driver_2018_oi_180054.pdf#page=3); [DOC-001 Table 3 — PDF p. 7](../../jama_driver_2018_oi_180054.pdf#page=7); [DOC-003 eTable 1 footnote — PDF p. 3](../../joi180054supp2_prod.pdf#page=3).
- **Direct source evidence:** The protocol defines first-attempt time to intubation from attempt start through ETT cuff inflation with the tube in the trachea. The main article and eTable define duration from laryngoscope blade entry through blade removal and report, among other results, all-patient medians of 38 versus 36 seconds.
- **Comparator and rule:** The start event is compatible; cuff inflation and blade removal are different end events and can define different time scales. A matched outcome label should disclose such a change.
- **Calculation:** No numeric recalculation is applicable; the check compares the two explicitly named endpoints.
- **Direct observation versus inference:** The definitions are direct. The possibility of an intended analysis change or a protocol amendment is inferred but not documented in the supplied package.
- **Alternative source-grounded interpretations:** The final analysis may deliberately replace the planned measure, or the two labels may refer to a harmonized recording procedure not described in the sources.
- **Exact human question:** Which timestamp generated the published duration analyses, and where is any change from cuff inflation to blade removal documented and justified?

## Registration summary

- Stable candidate count: 4.
- Ledger IDs: C001, C002, C003, C004.
- All candidates: Pending Human Adjudication.
- No candidate concerns a coherent finite-precision display-zero P value.
