# Statistical pass 1 — DSMC monitoring displays

Runtime: 01a129be-d2f9-73e3-94d5-a2df0a75cd43; gpt-6.1-sol/high; fresh spawn. Scope DOC-002 physical pp.189–194, PLAN by content. Stable relationships S601–S685 (85), fully recorded in `statistics/parts/monitoring.md`, each PASS_1_COMPLETE. Complete normative scope and review contract read. Sources/old audit artifacts preserved. No web, external literature, custom Python, old candidates or old conclusions used.

Direct source: `pdftotext -layout -f 189 -l 194 joi180132supp1_prod.pdf -`. All six source-matched reusable page images inspected. Finding independently confirmed on a fresh direct-source p192 render with Poppler pdftoppm25.03.0, CPU, command/derivative recorded in the relationship part.

## Findings

### F-ST1-301

**Title:** The July2016 cumulative favourable-GOSE chart's Y series follows unfavourable counts.

**Relationships:** S636, S641, S642, S654. One repeated cumulative-series pattern; all affected points retained below.

**Exact compared locations and document roles:** PLAN DOC-002 [`joi180132supp1_prod.pdf`, physical p192](../../../../joi180132supp1_prod.pdf#page=192), upper chart, “180 day favourable outcome (GOSE5–8) in blocks of25”, Y numerator/denominator row; same PLAN p192 lower chart, “Cummulative 180 day favourable outcome (GOSE5–8)”, blue Y series. PLAN [physical p191](../../../../joi180132supp1_prod.pdf#page=191), GOSE favourable and unfavourable score rows, corroborates totals but is not needed to reproduce the same-page cumulative discrepancy.

**Printed values:** The p192 Y favourable block pairs are7/13,2/8,11/16,5/10,8/10,6/12,3/8,5/12,6/14,5/12,2/9,4/9,3/11,6/9. The lower blue Y series lies near6,12,17,22,24,30,35,42,50,57,64,69,77,80 at the corresponding successive blocks. These are graphical coordinates read against labelled count-axis ticks, not printed point-label transcriptions. The lower orange X series follows its favourable block sums. The table prints favourable Y73 and unfavourable Y80.

**Rule and calculation:** A cumulative favourable-count series should sum the favourable numerators in its corresponding block series. That method reproduces orange X throughout:10,18,20,27,36,41,50,57,62,66,69,78,81,86. Applied to Y it yields7,9,20,25,33,39,42,47,53,58,60,64,67,73, whereas the displayed blue line follows the complements (denominator minus favourable count):6,12,17,22,24,30,35,42,50,57,64,69,77,80. The complement identity is an observed reproduction pattern, not a claim about production mechanism.

**Display-precision calculation:** For the second cumulative point (through block26–50), displayed favourable inputs7 and2 each receive ±.5, giving cumulative interval[8,10]. The plotted blue Y point is near12; a conservative graphical reading interval[11,13] is used, wider than the usual ±.5 count-display interval. The interval gap is at least1, relative to the graphical count12 it is at least1/12=.0833>.05. With usual half-unit graphical precision[11.5,12.5], the gap is1.5/12=.125. The third point should sum7+2+11=20, interval[18.5,21.5], while the graphical reading is near17; using ±.5 gives[16.5,17.5], gap1/17=.0588>.05. The second point is the conservative reproduction anchor. End totals73 versus graph near80 corroborate the pattern; that endpoint alone is not the inclusion anchor because permitting14 independent half-unit input intervals gives an interval broad enough to overlap80.

**Focus area:** A/B, cumulative count and outcome identity used in primary dichotomized-GOSE interim monitoring.

**Proposed review domain:** `plan_material`.

**Proposed primary relationship type:** `P_P`; **All relationships:** `P_P`.

**Qualifying route:** Route A, category4. The printed graphical cumulative result does not reproduce under a cumulative-sum method that reproduces the other series of the same display, with a reproduced relative discrepancy>.05. The monitored outcome is the primary GOSE dichotomy used in the supplied interim decision process; these are operational monitoring inputs rather than background historical baseline values.

**Affected result or extracted value:** Y cumulative favourable-GOSE count at the350-patient July2016 monitoring review, particularly cumulative count through block26–50 (near12 in the cumulative display versus9 from the favourable block numerators), and the identity of the Y curve presented to support primary-outcome monitoring.

**Why context does not resolve it:** Route A category4 applies. A reader sees a favourable-outcome title, favourable block pairs and an X cumulative series that agree, alongside a Y cumulative series representing different outcome counts. The immediate display does not state that Y is intended to show unfavourable outcomes. The table and upper chart reproduce one reading while the lower chart supplies another; reconstruction of the intended series does not eliminate the displayed count a reader may use.

**Alternatives and missing definition:** The blue series may intentionally have been an unfavourable outcome series, with an undeclared difference from the X series/title; alternatively it may be intended as a favourable series. No point-level data labels or explanatory note specify a different Y estimand. The exact plotted-series data are not supplied as structured numbers; the conservative early-point graph-reading bound is therefore explicit. No claim is made about whether the DSMC used this line rather than the coherent table or about any resulting stopping decision. Arm identity is not supplied and is not inferred.

**Classification ambiguity:** The observation is entirely inside prospective PLAN monitoring material; no REPORT location is a side of the discrepancy. The independent screen should assess the proposed routeA category4 application to a graphical cumulative primary-outcome result. No separate protocol-versus-report claim is made.

**Exact human question:** Should the July2016 p192 blue Y cumulative series represent favourable GOSE5–8 counts, as the title and block table state, or unfavourable GOSE1–4 counts, which reproduce the plotted sequence; which cumulative series should a reader use for this monitoring display?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| PLAN DOC-002 pp189,191,193, monitoring-table P columns and GOSE-score rows | Specific tests, sidedness, variance estimation and the name of the parenthesized GOSE dispersion are not supplied. Exact P reproduction or a claimed method/data conflict would depend on additional assumptions; all means and diagnostic sample SDs reconcile and no confidence interval or printed test conclusion contradicts these P values. | CONDITIONAL_OR_UNREPORTED |

## Completed checks and limitations

All GOSE-category count sums, category-derived mean scores, diagnostic sample SDs, favourable/unfavourable/death/survival aggregates, table percentages under display precision, missingness/refusal/enrollment decompositions, block numerator bounds, block denominator sums, bar-height/numerator matches, and cumulative-chart/table outcome matches were reviewed. Two dates' Y cumulative favourable plots differ in the expected way: May2017 p194 follows its favourable counts, while the July2016 p192 pattern above remains reproduced against its own block data. No issue is inferred merely from increasing contributor counts over time.

No estimate interval, printed confidence level, standard error, test statistic, equivalence/noninferiority margin, or stopping conclusion occurs in this six-page shard. Exact table-test mechanics cannot be established; those definitions are missing, not substituted by conventional assumptions. The supplied primary-outcome monitoring P values .26/.53/.68 do not satisfy the charter's .001 threshold, so these displayed tests do not themselves create a stopping-rule conflict. No treatment identity or individual-level data is inferred. Graphical reading precision is explicitly bounded. Findings1; excluded observations1; relationships85; uncovered units0.
