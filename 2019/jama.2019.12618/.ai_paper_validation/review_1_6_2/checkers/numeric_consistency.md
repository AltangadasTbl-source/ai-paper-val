# Numeric consistency review

Stage: numeric_consistency_reviewer. Runtime ID: 01a1295b-826f-79f2-8270-a4045d781af1. Fresh agent task: /root/numeric_review; model gpt-6.1-sol; reasoning effort medium. Scope: all REPORT numeric relationships in main article DOC-001 PDF pp. 1-10, results supplement DOC-002 PDF pp. 1-16 and administrative REPORT DOC-005 PDF p. 1. All 228 canonical N relationships are recorded in [numeric relationship inventory](../relationships/numeric_relationship_inventory.md), including all 114 main-map identities and 114 supplemental/context relationships. PLAN power/design/method rules are a disjoint assignment to the statistical and cross-source reviewers.

Both QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely. Checks cover patient/eye flow, randomized versus exposed versus analyzed counts, mutually exclusive totals, nonexclusive event categories, every printed numerator/denominator percentage, arithmetic directions and effect-measure identity. The complete current-run main evidence map and complete results-support map were used as locators; direct-source CPU Poppler pdftotext 26.01.0 layout extraction streamed main pp. 3-8 and supplementary pp. 8-15. Supplement p. 15 was visually read on the existing source-linked rendered page. No source/reused artifact was modified, no old candidate/report/checker conclusion was read, and no external evidence was used.

## Findings

### F-NUM-001

**Title:** Switching-group serious diarrhea percentage does not reconcile with its column denominator.

**Exact source locations and document roles:** REPORT DOC-002 [joi190092supp1_prod.pdf, physical PDF p. 15, eTable 9](../../../joi190092supp1_prod.pdf#page=15), Mycophenolate Mofetil column heading N=20 and Serious Systemic → Diarrhea row 1 (3.4). Same display comparators: Non-Serious Laboratory → Low hemoglobin 1 (5.0), Non-Serious Systemic → Allergic reaction 1 (5.0), and Fever 1 (5.0), all in the same N=20 column. REPORT DOC-002 [physical PDF p. 16, eTable 9 footnote b](../../../joi190092supp1_prod.pdf#page=16) attributes drug-related serious events to diarrhea and fatigue but specifies no alternate denominator. The primary compared relationship is within the one REPORT supplement, S_W. Canonical numeric relationship N225.

**Printed inputs:** Mycophenolate Mofetil N=20; serious systemic diarrhea number of patients reporting at least one event 1 (3.4%). The adjacent methotrexate column N=29 shows diarrhea 0 (0.0%) and serious fatigue 1 (3.4%). Counts represent patients, not episodes, under the explicit heading.

**Rule and reproduced calculation:** For the printed column denominator, 100 × 1/20 = 5.0%. With one-decimal display precision the printed 3.4% interval is [3.35%, 3.45%]; the recomputed interval is [5.0%, 5.0%]. Counts and denominator are finite integer participant counts: the feasible integers in their half-unit intervals [0.5, 1.5] and [19.5, 20.5] are exactly 1 and 20, so input rounding does not allow fractional patients. The interval gap is 5.0−3.45=1.55 percentage points and relative discrepancy 1.55/3.4=0.455882 (>0.05). The other three printed one-patient entries in the same column reproduce 5.0%; their one-decimal intervals include the ratio. If a denominator of 29 were used instead, 100 × 1/29=3.448276%, within [3.35%, 3.45%], but 29 is the other treatment column's heading.

**Focus area:** A, counts and denominators. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route A, category 3. The count, denominator and percentage in one display do not reconcile above the display-precision threshold. Category 4 additionally describes the numerical pattern: the patient-percentage calculation that reproduces other same-column rows does not reproduce this row.

**Affected result or extracted value:** The six- to twelve-month serious systemic diarrhea risk among patients switching to mycophenolate mofetil: its printed percentage is 3.4%, while its printed numerator and denominator imply 5.0%. This is a specific safety result; no claim about the primary treatment-effect conclusion is made.

**Why context does not resolve it:** Route A category 3 applies even when a reader could reconstruct an alternative percentage. The display provides both a percentage and a patient-count denominator that could be extracted, and does not identify a row-specific safety denominator. The p. 16 attribution footnote does not change N=20 or place the diarrhea event in the other treatment group.

**Source-grounded alternatives and missing definition:** A row-specific denominator of 29 would reproduce 3.4%, and 29 is visibly printed as the methotrexate column denominator; this calculation is an alternative interpretation, not an inferred production explanation. A different attribution of the event or an unstated diarrhea-specific population would also require source clarification. Other one-patient entries in the N=20 column support the conventional displayed 5.0% calculation, but this review assigns no final correction.

**Exact human question:** For eTable 9 serious systemic diarrhea in the Mycophenolate Mofetil N=20 column, which event count, denominator and percentage should be used, and does this row use a population different from the printed column population?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 PDF p. 5, Table 1 macular edema, N069 | F 55/201=27.363184080% versus printed 27.3%; one-decimal upper limit 27.35 gives gap 0.013184080/27.3=0.000482933, below 0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 PDF pp. 1, 7, 8, abstract/narrative/Table 3 nonserious ALT/AST, N099 | M 14/107=13.0841121% versus printed 13.0%; interval upper limit 13.05 gives gap 0.0341121/13.0=0.002624, below 0.05; repeated locations are one pattern. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 PDF p. 8, Table 3 F column, N091-N113 | Printed heading N=109 versus exposed N=108 disclosed in footnote b; percentages resemble 108-denominator values. Checking every printed F pair even against 109 gives maximum residual relative gap 0.008768, below 0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-002 PDF p. 10, eTable 4 F eye-floaters row, N135 | 5/108=4.6296296% versus printed 4.7%; lower limit 4.65 gives gap 0.0203704/4.7=0.004334, below 0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 PDF p. 5, Table 1 anterior vitreous/haze distributions, N059-N067 | Rounded M percentages sum 99.9% for vitreous cells and 100.1% for haze; the exact counts sum to their named parent denominator 202. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 PDF pp. 3, 6, 7, Figure 1/Table 2/switching narrative, N079 | Narrative eligible count 68 versus 32+42−3−2=69 from failures less safety exclusions; even an exact integer gap of 1/68=0.014706 is below 0.05. The printed-copy half-unit interval convention can only further reduce this gap. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-002 PDF p. 14, eTable 8 safety N62/N56, and DOC-001 PDF pp. 3, 6, 7 continued-treatment efficacy N60/N54, N178 | Six- to twelve-month safety observation and completed twelve-month efficacy need not have identical contributor sets; immediate table titles and endpoint context distinguish them. No single-result conflicting denominator is established. | CONTEXT_RESOLVES |
| REPORT DOC-001 PDF pp. 7-8, narrative 14 serious adverse events and Table 3 serious-category cells, N114 | Summing 20 patient-category memberships is not a count of unique serious episodes; hospitalization/other clinical-event categories can describe the same event. No disjoint-category assumption or participant-level cross-tabulation is printed. | CONTEXT_RESOLVES |
| REPORT DOC-001 PDF p. 6, Table 2 macular-thickness medians and modeled narrative contrast, N083/S014 | Crude median-change difference 12 μm differs from reported modeled contrast 2.4 μm; the paper explicitly supplies a regression model and clustering, so these are different summaries. | MODEL_VERSUS_CRUDE |

## Completion and limitations

228 of 228 N relationships are reviewed, including all assigned REPORT units. Findings: 1. Excluded apparent observations: 9, each with exactly one reason code. Reconciled checks appear in the relationship inventory rather than this excluded table. All Figure 1 patient and eye totals reconcile; all baseline mutually exclusive counts and grade-distribution parent sets reconcile; nonexclusive race/adverse-event memberships are not forced to sum to patient totals. All displayed supplemental patient percentages were recomputed; only the eTable 9 serious diarrhea row exceeds the inclusion threshold. Model-based ORs remain identifiable as odds ratios, and no label is evidently computed as an RR, rate or incompatible contrast.

No numerical source-unit gap remains. Raw participant records are not supplied, so means/medians, nonexclusive event unions and episode attribution cannot be independently reconstructed. Unreported row-specific definitions are retained as the human question rather than assumed. No rendering or OCR was newly performed; no derivative file was generated by this checker. Sources and reused assets remain unchanged.

