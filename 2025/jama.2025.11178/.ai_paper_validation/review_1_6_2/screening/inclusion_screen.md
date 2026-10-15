# Independent initial inclusion screen

Fresh screener: `/root/initial_screen`, gpt-6.1-sol/high. Scope: every finding in the current canonical numeric, cross-source and statistical-pass-1 artifacts: 5 + 8 + 13 = 26 findings. QUALITY_CONTROL_SCOPE.md and the full review contract were read. Every cited location was independently reread from 31 distinct current exact-source PDF renders and the supplied workbook XML/shared strings; checker transcription alone was never authority. No earlier scientific conclusions or web inputs were used. Sources and reused assets remain unchanged.

The coordinator assigned stable candidate IDs after these independent decisions, in substantive source order. Issue-group labels remain provenance labels; corroborating-only source definitions do not move an issue ahead of its conflicting report locations.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-001 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-NUM-002 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C017 |
| F-NUM-003 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C015 |
| F-NUM-004 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-NUM-005 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-XS-001 | cross_source_consistency_reviewer | initial | SCREENED_OUT | TERMINOLOGY_OR_WORDING | — |
| F-XS-002 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-XS-003 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C005 |
| F-XS-004 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C006 |
| F-XS-005 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C007 |
| F-XS-006 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C013 |
| F-XS-007 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C012 |
| F-XS-008 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C016 |
| F-ST1-001 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C009 |
| F-ST1-002 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C010 |
| F-ST1-003 | statistics_pass_1 | initial | SCREENED_OUT | CONTEXT_RESOLVES | — |
| F-ST1-004 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-ST1-005 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C004 |
| F-ST1-006 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C008 |
| F-ST1-201 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C014 |
| F-ST1-202 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C014 |
| F-ST1-203 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C012 |
| F-ST1-204 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C013 |
| F-ST1-205 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C011 |
| F-ST1-206 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C004 |
| F-ST1-601 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C016 |
| F-ST2-1001 | statistics_pass_2 | pass_2 | INCLUDE | MEETS_THRESHOLD | C018 |

## One-sentence finding justifications

- **F-NUM-001:** Include through **Route A, category 3**, because the stated randomized denominator 776 and count 371 give a percentage interval [47.714102,47.904578] separated from printed 43% [42.5,43.5] by 4.214102 points, relative discrepancy .098002.
- **F-NUM-002:** Include through **Route A, category 3**, because workbook E82's 711 (73.2) conflicts with E3's N=1568, E83's two missing and A110's nonmissing-denominator rule, with recomputed [45.341417%,45.463259%] and relative gap .378234.
- **F-NUM-003:** Include through **Route A, category 3**, because the first eTable 8 header's at-three-month arm counts sum to [452.5,455.5], exceeding its [365.5,366.5] any-follow-up count by at least 86, relative gap .234973.
- **F-NUM-004:** Include through **Route B**, because the explicitly shared usual-care SD requires pairwise SMD additivity, 17 displayed triples remain separated above .05 after precision, and the intended standardized contrasts cannot be identified from the table for extraction.
- **F-NUM-005:** Include through **Route A, category 4**, because the stated reciprocal method reproduces other NNT rows but the three specified printed points remain separated from their recomputed intervals by relative gaps .050975, .062771 and .057218.
- **F-XS-001:** Screen out as **TERMINOLOGY_OR_WORDING**, because the main article's clinical diagnosis description and the plans' repeated-code EHR ascertainment describe the same malignancy exclusion at different levels of operational detail, without establishing that different participants entered the reported analysis.
- **F-XS-002:** Include through **Route B**, because the online session-duration endpoints differ by 14 minutes after half-unit precision, relative gaps .311 and .233, and the supplied sources do not identify whether the extracted primary intervention duration was revised or merely estimated differently.
- **F-XS-003:** Include through **Route A, category 5**, because age is labeled part of the prespecified base analysis in the report and workbook but is absent from the plans' explicit primary adjustment set.
- **F-XS-004:** Include through **Route B**, because the reported secondary models add the outcome-specific baseline value and import primary-model factors beyond the plans' explicit list, leaving the planned versus implemented adjustment of the key secondary estimates unresolved.
- **F-XS-005:** Include through **Route A, category 5**, because the SAP retains a primary follow-up/MAR specification while the report assigns primary status to weighted MNAR estimation and sensitivity status to the follow-up analysis, with the disclosed IPW amendment retained as an alternative explanation.
- **F-XS-006:** Include through **Route B**, because a stated binary education adjustment and three displayed education coefficients describe different primary-model coding and the repeated AA labels prevent definite coefficient attribution.
- **F-XS-007:** Include through **Route B**, because the stated final weight-model list names education while the fitted coefficient table substitutes employment, leaving the covariate set that generated primary response weights unresolved.
- **F-XS-008:** Include through **Route B**, because eTable 11's median/quartile labels conflict with its mean description and five PGIC centers beyond display tolerance for ordinary medians of the stated single-item scale, so an extractor cannot identify the summary and bounds to take.
- **F-ST1-001:** Include through **Route A, category 1**, because the main Table 2 intensity 12-month HC/PT NNT point 63 lies outside its printed 18–38 interval.
- **F-ST1-002:** Include through **Route A, category 1**, because the fourteen source-confirmed SMD points lie outside their printed intervals, including six physical-function points outside even the numerically sorted endpoints.
- **F-ST1-003:** Screen out as **CONTEXT_RESOLVES**, because descending endpoints identify the same numerical interval by their minimum and maximum without changing an extractable endpoint value, while separate point-containment and SMD-construction issues remain included.
- **F-ST1-004:** Include through **Route A, category 4**, because the common-SD construction reproduces the severity six-month row but fails twenty other rows by additivity, MD/SMD scaling or sign, extending included IG03 beyond F-NUM-004's seventeen triples.
- **F-ST1-005:** Screen out as **DUPLICATE_OF_INCLUDED**, because both main-table reciprocal-NNT occurrences are already retained by F-NUM-005 in IG04.
- **F-ST1-006:** Include through **Route B**, because six matched HC/PT response contrasts have null-containing RR intervals and finite positive NNT intervals, and the source's infinity rule does not establish how the different extracted null readings reconcile.
- **F-ST1-201:** Include through **Route A, category 1**, because seven imputation-model 95% intervals exclude zero while their P values exceed .05, independent of an unreported coefficient-test convention.
- **F-ST1-202:** Include through **Route A, category 1**, because three ratio intervals include a printed endpoint of 1 while their P values are below .05, and this route expressly forbids rounding-based removal.
- **F-ST1-203:** Screen out as **DUPLICATE_OF_INCLUDED**, because the education-versus-employment weight-model discrepancy and all its method locations are already retained by F-XS-007 in IG13.
- **F-ST1-204:** Screen out as **DUPLICATE_OF_INCLUDED**, because the binary-versus-multilevel education coding and repeated-label pattern is retained by F-XS-006 in IG14 with every coefficient and workbook location.
- **F-ST1-205:** Include through **Route B**, because the restricted-primary-analysis narrative and base-only covariate footnote do not identify whether education and employment entered the models generating eTable 8's primary-outcome subset estimates.
- **F-ST1-206:** Screen out as **DUPLICATE_OF_INCLUDED**, because the reminder-letter six-month PT/UC NNT point and its percentage inputs are already retained by F-NUM-005 in IG04.
- **F-ST1-601:** Screen out as **DUPLICATE_OF_INCLUDED**, because its five precision-qualified PGIC raw centers and summary-definition conflict are retained by F-XS-008 in IG11, including the p.18 method note.

## Consolidated stable-ID mapping

The complete independent issue-group source evidence is retained in candidate_ledger.md and registration/inclusion_screen_full_handoff.md. This canonical log retains every decision and justification; no screening decision changed.

- C001 (IG01): F-XS-002.
- C002 (IG02): F-NUM-001.
- C003 (IG03): F-NUM-004, F-ST1-004.
- C004 (IG04): F-NUM-005.
- C005 (IG05): F-XS-003.
- C006 (IG06): F-XS-004.
- C007 (IG07): F-XS-005.
- C008 (IG08): F-ST1-006.
- C009 (IG09): F-ST1-001.
- C010 (IG10): F-ST1-002.
- C011 (IG12): F-ST1-205.
- C012 (IG13): F-XS-007.
- C013 (IG14): F-XS-006.
- C014 (IG15): F-ST1-201, F-ST1-202.
- C015 (IG16): F-NUM-003.
- C016 (IG11): F-XS-008.
- C017 (IG17): F-NUM-002.
- C018 (pass2 appended): F-ST2-1001.

## Source confirmation and limitations

Source roles by content: DOC-001 main, DOC-004 intervention results description, DOC-005 results/method supplement and DOC-006 workbook are REPORT; DOC-002 protocol and DOC-003 SAP are PLAN. Every finding's quoted values and comparison locations were checked against the supplied source renders or direct worksheet/shared-string XML, including all fourteen containment tuples, all twenty SMD-construction rows and all ten interval/P rows. The precision calculations use half-unit bounds and the fixed relative-gap rule; interval-versus-test/point-containment comparisons are never rounded away. No scientific source-reading gap remains in this assigned scope.

Durable engine/source notes: `preprocessing/initial_screen/engine_record.md`; freshly generated mainp5/mainp9 derivatives use pinned PyMuPDF1.26.4,200dpi,CPU; other exact-source pages are current-run renders independently visually reread, not reused checker conclusions. Workbook XML copies came from direct `unzip -p`; no spreadsheet recalculation or new Python helper was used.

Named evidence limits: no participant-level records, exact UC change SDs, complete covariance/test degrees of freedom, unrounded coefficient endpoints, RD/NNT interval construction, or additional prospective amendment is supplied; the PGIC median calculation uses the ordinary empirical median and retains alternative interpolation as a question. These limits are recorded in the relevant included group and do not replace observable source comparisons. No severity, validity or human disposition is assigned.

Counts: **26 findings;19 INCLUDE rows consolidated into17 included issues;7 SCREENED_OUT rows**: DUPLICATE_OF_INCLUDED5, TERMINOLOGY_OR_WORDING1, CONTEXT_RESOLVES1; all other permitted screened-out reason codes0. Every finding has exactly one initial decision.


Mechanical classification alignment: C016/IG11 is S_W, with the main PGIC score definition used only as corroboration. All26 independent initial decisions remain unchanged.

## Pass-2 independent inclusion update

One new finding F-ST2-1001 was independently included as C018. Its complete justification, exact sources, precision proof and alternatives are in [pass-2 screen](inclusion_screen_pass_2.md). The proposed S218 expansion of C008 was screened out as ROUNDING_OR_DISPLAY_PRECISION; existing C008 locations are unchanged. Overall finding decisions:27; INCLUDE20; SCREENED_OUT7 (DUPLICATE_OF_INCLUDED5, TERMINOLOGY_OR_WORDING1, CONTEXT_RESOLVES1); stable issues18.

## Final-auditor qualification refinement

C007/F-XS-005 remains INCLUDE/MEETS_THRESHOLD, now confirmed through Route B (focusD, unresolved retained primary/MAR versus reported primary MNAR/sensitivity hierarchy, and extractable primary-analysis specification). The initial RouteA5 rationale above is historical screening provenance; it is not the final qualifying route. The supplied follow-up result is reported as sensitivity, and the SAP4IPWamendment/SAP19conditionalweightedfirstbranch remain substantive alternatives. No decision or stableID changed.
