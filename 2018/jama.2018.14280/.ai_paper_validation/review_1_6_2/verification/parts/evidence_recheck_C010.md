# Appended stable-ID evidence recheck

Fresh runtime `/root/append_rechecker_c010`, `qc162_evidence_rechecker`, run model `gpt-6.1-sol`, reasoning effort `high`. Assigned scope is C010 only; C001–C009 are outside this part. QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely. Registration and the independent pass-2 inclusion screen were used to identify the exact comparison; the current supplied PDFs are final authority. No legacy scientific decisions, external evidence, or other candidates were used to select this issue. Sources and reused artifacts were preserved.

## C010 — Vasopressor-duration window and counting unit remain unresolved

**Review domain:** report_internal_inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 4 title vs its vasopressor-duration row and footer

**Evidence state:** reproduced

**Finding IDs:** F-ST2-501

**Qualifying route:** Route B

**Human review status:** Pending Human Adjudication

### Location found and source value/text matched

The exact supplied results supplement, `joi180108supp3_prod.pdf`, physical p8, was read using fresh selected-page native/layout extraction and independently viewed as a fresh direct-PDF rendering. This confirmed every affected location of the two-arm pattern. Evidence links below identify the source PDF, not the extraction or image as authority.

| Affected source location | Role by content | Found | Exact source content matched |
|---|---|---|---|
| [Physical p8, eTable 4 title](../../../../joi180108supp3_prod.pdf#page=8) | REPORT: clinical result display | Yes | “Sedatives, analgesics, neuromuscular blockade, fluids, vasopressors and co-interventions during the first three days.” |
| [Physical p8, Days of vasopressor use, Low Tidal Volume column](../../../../joi180108supp3_prod.pdf#page=8) | REPORT: observed duration distribution | Yes | `2 (1–4)` under the arm header `n = 477`. |
| [Physical p8, Days of vasopressor use, Intermediate Tidal Volume column](../../../../joi180108supp3_prod.pdf#page=8) | REPORT: observed duration distribution | Yes | `2 (1–4)` under the arm header `n = 484`. |
| [Physical p8, P-value cell for Days of vasopressor use](../../../../joi180108supp3_prod.pdf#page=8) | REPORT: between-arm comparison | Yes | `0.87`. This is matched context, not a conflicting value. |
| [Physical p8, summary footer](../../../../joi180108supp3_prod.pdf#page=8) | REPORT: distribution definition attached to result | Yes | “Data are number / total (%) or median (interquartile range).” Thus the duration entries are medians with IQRs. |
| [Physical p8, vasopressor footnote a](../../../../joi180108supp3_prod.pdf#page=8) | REPORT: exposure definition attached to result | Yes | Need of any dose of norepinephrine and/or epinephrine, and dopamine `>5 µg/kg/min`; no day-counting convention, start/end, or row-specific duration window is specified. |

Both arm cells belong to this one pattern and have been separately confirmed. No source transcription or location amendment is needed.

### Comparator matched and source-grounded context

The comparator is the **same table's first-three-days horizon**, read directly from its title, against the **upper quartile 4 days in each duration cell**, interpreted using its own median/IQR footer. This is a comparison within one REPORT, rather than a difference between a protocol and a report or between two result documents.

The following supplied REPORT locations were also reread directly as context. They do not introduce additional conflicting relationships:

| Context location | Found and matched | Consequence for this comparison |
|---|---|---|
| [Results supplement p5, eTable 1 title and column labels](../../../../joi180108supp3_prod.pdf#page=5) | “Respiratory variables during the first three days of ventilation”; columns “After titration on day of randomization”, “Day 1”, “Day 2”, and “Day 3”. | Four measurement occasions are explicitly displayed under a first-three-days heading. Randomization date plus days 1–3 can support a calendar-date interpretation. They do not define vasopressor duration. |
| [Results supplement p6, eTable 2 title and repeated column labels](../../../../joi180108supp3_prod.pdf#page=6) | “Ventilator settings during the first three days of ventilation”; after-titration randomization-day and day-1/day-2/day-3 columns in each mode block. | Corroborates the same possible date-label convention. Measurement occasions alone do not establish elapsed exposure length. |
| [Results supplement p7, eTable 3 title and repeated column labels](../../../../joi180108supp3_prod.pdf#page=7) | “Respiratory variables during the first three days of ventilation”; after-titration randomization-day and day-1/day-2/day-3 columns in each mode block. | Corroborates the alternative but does not specify how eTable 4's duration row was computed. |
| [Results supplement p8, nearby duration and daily rows](../../../../joi180108supp3_prod.pdf#page=8) | Sedative durations `0.6 (0.3–1.5)` / `0.6 (0.0–1.5)`, analgesic durations `0.7 (0.3–2.0)` / `0.7 (0.4–2.0)`; RASS and “Fluid balance in 24 hours” explicitly have Day 1, Day 2, Day 3 rows. | Fractional drug durations and integer vasopressor displays do not establish a shared or different counting convention. The explicit daily labels reinforce the observation-horizon question. |
| [Main article physical p4, Outcomes and Other Study Parameters](../../../../jama_simonis_2018_oi_180108.pdf#page=4) | Describes secondary measures including sedatives, analgesics, neuromuscular blocking agents, transfusions, dead-space reduction and delirium; describes cumulative drug-use collection for economic measures. | Does not supply an exposure start/end or a definition of days for the vasopressor-duration cells. Cumulative drug-use collection is not assigned to this result by the main text. |
| [Main article physical p6, eTable 4 narrative reference](../../../../jama_simonis_2018_oi_180108.pdf#page=6) | Narrative refers to need for, duration of, and amount of sedatives, analgesics and neuromuscular blocking agents, citing eTable 4; also discusses fluids, transfusion and rescue therapies. | Supplies no independent vasopressor-duration distribution or counting rule that chooses between elapsed time, dates touched, and a longer course. |

### Consistency rule applicable

The applicable logical rule is that an exposure duration computed **as elapsed time confined to a three-day window** cannot have an upper quartile above three days. If instead the quantity counts **exposed calendar dates including randomization date and days 1–3**, four can be an admissible upper quartile. These are different quantities for extraction; neither convention is selected as the authors' convention by this recheck.

The registered issue is the unresolved attribution of the two printed distributions to an observation window and counting unit. It is not a claim that four calendar dates cannot occur within the described study phase, a quartile-order issue, a between-arm discrepancy, or an interval-versus-P-value conflict. The IQR is a marginal distribution summary, not a confidence interval for a between-arm effect. P=.87 cannot be used to test its compatibility with either arm's IQR.

Scope permits a label that changes which quantity a value represents when the values do not identify the intended quantity. Here the named values are both arms' `2 (1–4)` vasopressor-duration distributions. The issue concerns their attached analysis window/counting definition, rather than merely different table headings or a peripheral copy of a descriptive value. The p5–7 headings are contextual support for an alternative; they are not independently registered differences. No primary/key-secondary designation is inferred for vasopressor duration.

### Calculation and logical comparison reproduced, including precision

For each arm separately:

| Check | Printed or recomputed intervals | Gap and conclusion |
|---|---|---|
| Median 2, Q1 1, Q3 4 rounding allowances | Median `[1.5,2.5]`; Q1 `[0.5,1.5]`; Q3 `[3.5,4.5]`. | Ordered quartiles containing the median are possible. No order or containment discrepancy is present. |
| Conditional elapsed-duration interpretation within exactly three days | Admissible Q3 interval `[0,3]`, compared with printed Q3 interval `[3.5,4.5]`. | Minimum gap `3.5−3=0.5` days; relative discrepancy `0.5/4=0.125`, exceeding `0.05`. The elapsed-window reading does not reconcile through display precision. |
| Conditional four-calendar-date counting interpretation | Admissible Q3 interval `[0,4]`, compared with printed Q3 interval `[3.5,4.5]`. | Intervals overlap on `[3.5,4]`; gap zero. Such counting can reconcile the numeric upper quartile. It remains an alternative because no vasopressor-specific counting definition is supplied. |
| Both arms' printed summaries compared as copies | Both medians and both quartiles have identical intervals. | Every copy-comparison gap is zero; no inter-arm numerical discrepancy is alleged. |

The phrase “first three days” is a declared observation window, not a rounded numeric estimate. The three-day upper bound in the elapsed-duration calculation is therefore exactly 3, not `[2.5,3.5]`. That calculation is expressly conditional on elapsed counting. A calendar-date count is discrete and may have value 4; no fractional-calendar-date convention is assumed. The printed rounding interval is a conservative display check, rather than a claim that the underlying count was fractional.

The logical reproduction is therefore: exact title and exact upper quartiles admit substantively different result quantities, one of which conflicts beyond rounding with an elapsed three-day bound and one of which can reconcile through calendar-date counting, while the source does not specify the convention. The mechanical check does **not** establish a source-authoritative elapsed-duration contradiction. It reproduces the registered unresolved quantity attribution.

### Necessary inputs available and exact missing inputs or definitions

**Available:** exact title, duration row label, both arm summaries, arm headers, distribution footer, vasopressor drug/dose criterion, P-value cell, adjacent explicit day labels, neighboring four-occasion displays, and relevant main-text references. These suffice to confirm the printed observation and the conditional precision comparisons.

**Missing:** the vasopressor-duration exposure start and stop, whether partial days are accumulated as elapsed fractions or count as calendar dates, whether randomization date is included in addition to days 1–3, whether the duration row is truncated to eTable 4's stated horizon or summarizes a longer course, the patient-level durations and contribution set, and a row-specific definition that maps the table title to this summary. Patient-level observations are unnecessary for the two conditional bounds but would be needed to reconstruct the actual distributions. Neither a day-counting rule nor the producing mechanism can be determined from drug names and dose threshold.

### Source-grounded alternative interpretation

The strongest supplied-context alternative is counting calendar dates with vasopressor use, including the randomization date plus day 1, day 2 and day 3. The adjacent tables explicitly display these four occasions under similar first-three-days headings. This would permit an upper quartile 4 and remove the conditional elapsed-bound discrepancy. Those respiratory-measurement labels do not explicitly extend their counting convention to the vasopressor-duration row.

A row summarizing a longer treatment course is also possible, but the supplied p8 row/footnote does not disclose a longer window. A different intended title or upper quartile could also be contemplated, but no alternative printed value is supplied. None of these possibilities is established or proposed as a correction. The remaining issue is which quantity the displayed values actually summarize.

### Direct observation versus inferred explanation

**Direct observation:** the REPORT title says first three days; both arm cells print median 2 and upper quartile 4; the footer identifies IQRs; the footnote defines drugs/dose but supplies no duration convention; adjacent tables show four measurement occasions under similar headings; relevant main text supplies no resolving vasopressor-duration definition.

**Conditional logical calculation:** an elapsed exposure limited to three days gives a 0.5-day minimum rounding-interval gap for Q3=4; a four-calendar-date interpretation gives zero gap. Both calculations reproduce.

**Inferred explanation, not established:** that the authors actually counted calendar dates, used a longer course, or intended another title/quartile. The recheck selects none. It also does not infer the individual-level vasopressor distribution or its generating analysis from the identical summaries and P=.87.

### Classification confirmation and ambiguity

Every conflicting location belongs to the same observed-results supplement and is REPORT by content. The within-document title/result-definition comparison gives **S_W** as the sole relationship, so precedence does not introduce another type. The contextual main-article references are REPORT but do not contain an opposing definition or result and therefore do not add S_C. No PLAN content participates in the comparison; there is no P_R or P_P relationship.

**report_internal_inconsistency** is confirmed because the registered question is which time-window/counting quantity the numbers belong to. It is not a claim that an identified statistical method, inter-arm estimate, interval or test fails. The provisional classification needs no correction.

**Classification ambiguity:** calendar-date counting including randomization date may reconcile the upper quartile with the heading, whereas an elapsed three-day interpretation does not. A longer course or different intended title/quartile remains possible. This ambiguity concerns result meaning, not the role or document identity.

### Evidence state and determining recheck fact

**reproduced.** The exact current supplied source confirms every registered location and numerical value without a transcription amendment; both conditional precision comparisons reproduce. No row-specific exposure or counting definition resolves which quantity receives the two duration distributions. The source-grounded calendar-date alternative is retained explicitly. This state records reproduction of the unresolved quantity-attribution candidate, not an adjudication or an assertion that elapsed duration is the authors' convention.

### Exact remaining human question

Which exposure start/end and definition of “days” produced both `2 (1–4)` summaries, and how does the four-day upper quartile relate to eTable 4's first-three-days horizon?

### Tooling, derivative provenance and limits

Compute device: CPU, as recorded in tooling_record.md. Exact current-source layout text was read with direct `pdftotext`, Poppler 25.03.0, for results supplement physical pp5–8 and main physical pp4/6. These selected-page extractions were returned to stdout; no text derivative was written. Fresh visual confirmation used direct `pdftoppm`, Poppler 25.03.0, `-f 8 -l 8 -singlefile -r 130 -png joi180108supp3_prod.pdf`, producing `preprocessing/recheck-C010-supp3-p8.png` within this run. The fresh image was viewed completely, confirming title, arm alignment, both cells, P value and footnotes against the current source. No OCR or fallback environment was used. Relative PDF links were checked mechanically and resolve to supplied files.

Scope completed: 1 assigned stable ID, C010; 1 two-arm pattern; all affected p8 locations and 5 contextual source pages reread. No scientific inspection gap remains in this scope. The duration convention and underlying observations remain unavailable in the supplied evidence and are recorded above as the human question. Sources/reused assets and coordinator-owned canonical artifacts were not changed.
