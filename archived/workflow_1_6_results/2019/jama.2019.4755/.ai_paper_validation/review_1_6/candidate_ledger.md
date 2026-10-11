# Workflow 1.6 Candidate Ledger

**Pending Human Adjudication.** Sixteen distinct candidates are registered without severity or adjudication. Discovery restarted from all 88 supplied-source pages. These records include conditional questions with named missing definitions; proposed calculations are diagnostics rather than final corrections. Every assigned ID must remain in all later artifacts, including when a source recheck disproves its comparison.

## Registration and genuine duplicate merge

Numeric REPORT checker emitted five observations, numeric PLAN checker eleven, cross-source checker six, and statistical pass 1 five. The same blank main Test cell, same eTable 5 cutoff header, same three distinct eTable 5 women's PPV cells, and same SAP 10.2 unit label were merged only when their exact printed inputs, comparators, and rules matched. All lane provenance is retained per ID. The three women's rows remain separate because the thresholds/tests, inputs and contrasts differ. Pharmacovigilance subtotal and overall budget are separate because their compared totals and rules differ. No observation was merged merely for a shared cause or topic. This produces 16 stable IDs C001-C016. The coordinator assigns category and relationship from the actual compared locations, rather than the originating checker lane. No P-display-zero candidate exists; actual eTable 6 P values are .16-.50.

## Document-role classification table

Final classification after fresh direct-source recheck. Suggested dispositions are mechanical human-review pre-fills, not adjudications. Thirteen records are recorded_candidate and three are record_input_error. Every ID remains Pending Human Adjudication.

| ID | Primary category | Relationship type | All relationships | Compared document roles | Review domain | Evidence state | Suggested review disposition |
|---|---|---|---|---|---|---|---|
| C001 | Measure, label, or scale inconsistency | S_W | S_W | REPORT main Table 3 vs REPORT main Table 2 | report_internal_inconsistency | recorded_candidate | retain |
| C002 | Measure, label, or scale inconsistency | S_W | S_W | REPORT results eTable 5 vs REPORT results eTable 4 | report_internal_inconsistency | recorded_candidate | retain |
| C003 | Numeric or arithmetic inconsistency | S_W | S_W | REPORT results eTable 5 vs REPORT results eTable 4 | statistical_results | recorded_candidate | retain |
| C004 | Numeric or arithmetic inconsistency | S_W | S_W | REPORT results eTable 5 vs REPORT results eTable 4 | statistical_results | recorded_candidate | retain |
| C005 | Numeric or arithmetic inconsistency | S_W | S_W | REPORT results eTable 5 vs REPORT results eTable 4 | statistical_results | recorded_candidate | retain |
| C006 | Measure, label, or scale inconsistency | P_P | P_P | PLAN SAP p. 6 section 3.2 paired 17 µg Hb/g expression vs PLAN SAP p. 6 section 3.2 10.2 Hb/g expression; PLAN SAP p. 8 complete FD threshold unit corroborates only | plan_material | recorded_candidate | retain |
| C007 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol duration field vs PLAN dated schedule | plan_material | recorded_candidate | retain |
| C008 | Measure, label, or scale inconsistency | P_P | P_P | PLAN protocol working-day phrase vs PLAN parenthetical hours | plan_material | recorded_candidate | retain |
| C009 | Measure, label, or scale inconsistency | P_P | P_P | PLAN protocol summary volumes vs PLAN tube-specific options | plan_material | recorded_candidate | retain |
| C010 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol category 6 total vs PLAN components and total definition | plan_material | recorded_candidate | retain |
| C011 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol supplies total vs PLAN tube-price/quantity footnote | plan_material | record_input_error | discuss |
| C012 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol insurance amount vs PLAN attached formula | plan_material | recorded_candidate | retain |
| C013 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol 16 category totals vs PLAN overall budget | plan_material | recorded_candidate | retain |
| C014 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol printing line vs PLAN linked printing footnote | plan_material | recorded_candidate | retain |
| C015 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol meeting total vs PLAN linked cost/frequency footnote | plan_material | record_input_error | discuss |
| C016 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol center incentive vs PLAN practice-related budget footnote | plan_material | record_input_error | discuss |

## C001 — Missing test identity in the men's third predictive-value row

**Candidate statement:** Missing test identity in the men's third predictive-value row; requires human adjudication of the printed comparison and any named conditional basis.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table 3 vs REPORT main Table 2

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both conflicting locations are within one REPORT document. A separate source that merely corroborates the intended label does not create an S_C or P_R discrepancy relationship.

**Classification ambiguity:** None for document role or relationship type; conditional comparator applicability is stated in the source-grounded alternatives below.

**Checker provenance:** NUM-01; XS01; SP1-LABEL-1; N048, N049; S029, S030. Numeric checker primary records preserved below; cross-source and statistical candidate records remain complete in their canonical checker artifacts.

- Relationships: N048 andN049, two measures sharing exactly one missing Test cell.
- Compared locations/roles: REPORT [main p5 Table3 men third row Test cell, cutoff10.2](../../jama_brenner_2019_oi_190039.pdf#page=5); REPORT [same p5 Table2 men qualitative10.2 row](../../jama_brenner_2019_oi_190039.pdf#page=5). Both locations are within one report.
- Printed inputs: Table3 has blank Test cell, cutoff10.2, aspirin PPV27.5/NPV89.2, placebo PPV20/NPV90.3; contrasts7.5[-6.4,20.2] and−1.1[-5.3,3.0]. The preceding two rows explicitly say Quantitative at10.2 and17.0. Table2 men Qualitative10.2 supplies aspirin TP28,FN43,TN354,FP74; placebo TP12,FN43,TN400,FP48.
- Rule/calculation/tolerance: preserve test identity when mapping a numeric diagnostic row. Proposed qualitative alignment yields PPV28/(28+74)×100=27.45098 and12/(12+48)×100=20; NPV354/(354+43)×100=89.16877 and400/(400+43)×100=90.29345. Both displayed predictive values and contrasts reconcile within0.05points. The defect is missing measure/test identification, not incorrect arithmetic.
- Direct observation versus inference: the Test cell is visibly blank. Its qualitative identity is diagnostic inference from matching counts, numerical values and row ordering; it is not a printed label.
- Alternatives/missing definition: an intentional continuation of the preceding Quantitative label is visually possible, but conflicts with the numeric qualitative matches and would duplicate a Quantitative10.2 row; source does not declare an omitted-label convention. The missing definition is the test identity intended for this exact row.
- Quality-control relevance: a downstream extractor could assign these PPV/NPV values to the wrong test at the same cutoff. No conclusion impact is asserted.
- Exact human question: Which test is intended for the men's third Table3 row at10.2, and is the blank Test cell an omitted label requiring clarification?

**Mechanical evidence recheck:** Completed by fresh gpt-6.1-sol/high agent 01a12871-ed60-7951-bfc9-08725b3b7034. Visibly blank Test cell; qualitative count values reproduce its arm predictive values. Full separate facts: [evidence recheck](verification/evidence_recheck.md).

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Incomplete visible concentration unit in eTable 5

**Candidate statement:** Incomplete visible concentration unit in eTable 5; requires human adjudication of the printed comparison and any named conditional basis.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results eTable 5 vs REPORT results eTable 4

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both conflicting locations are within one REPORT document. A separate source that merely corroborates the intended label does not create an S_C or P_R discrepancy relationship.

**Classification ambiguity:** None for document role or relationship type; conditional comparator applicability is stated in the source-grounded alternatives below.

**Checker provenance:** NUM-05; XS03; SP1-LABEL-2; N094-N111; S073-S090. Numeric checker primary records preserved below; cross-source and statistical candidate records remain complete in their canonical checker artifacts.

- Relationship: N094, with the same source unit applying allnine eTable5 rows N094–N111; one shared header defect rather than nine duplicate candidates.
- Compared locations/roles: REPORT [results supplement p7 eTable5 Cutoff header](../../joi190039supp3_prod.pdf#page=7); REPORT [p6 eTable4 Cutoff header](../../joi190039supp3_prod.pdf#page=6); REPORT [main p5 Tables2/3 cutoff header](../../jama_brenner_2019_oi_190039.pdf#page=5). The discrepancy is the incomplete visible header inside the results supplement; main article provides corroboration of intended unit.
- Printed inputs: eTable5 visible header reads Cutoff followed by [µg with no visible Hb/g] closure/denominator; row thresholds10.2 and17.0. eTable4 and main tables identify cutoff μg Hb/g. eTable5 abbreviation list separately defines g andHb. Native extraction supplies Hb/g] at a displaced position rather than the visible header.
- Rule/calculation/tolerance: these same cutoff numbers require the same dimensional concentration label: μg hemoglobin pergramfeces. μg alone denotes mass, not concentration. This is a dimensional/label identity check; numeric rounding tolerance is not applicable.
- Direct observation versus inference: the visible unit truncation is direct. A concentration-unit intention is inferred from matched cutoffs, neighboring table and extraction; no numeric concentration conversion is invented.
- Alternatives/missing definition: PDF rendering/clipping or misplaced font text could explain the omission, or the header may deliberately be abbreviated; no unit-abbreviation convention makes μg alone dimensionally equivalent to μgHb/g. Missing definition: intended complete unit and whether the source layout is truncated.
- Quality-control relevance: a cutoff can be copied with incomplete units despite numerically matching another table. This is bounded reporting/extraction risk.
- Exact human question: Is the eTable5 cutoff unit intended to be μg Hb/g, and should its full concentration denominator be visible in this header?

**Mechanical evidence recheck:** Completed by fresh gpt-6.1-sol/high agent 01a12871-ed60-7951-bfc9-08725b3b7034. Visible eTable 5 unit stops at [µg; eTable 4 shows [µg Hb/g]. Full separate facts: [evidence recheck](verification/evidence_recheck.md).

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Women's quantitative 10.2 PPV contrast lacks a visible magnitude

**Candidate statement:** Women's quantitative 10.2 PPV contrast lacks a visible magnitude; requires human adjudication of the printed comparison and any named conditional basis.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results eTable 5 vs REPORT results eTable 4

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both conflicting locations are within one REPORT document. A separate source that merely corroborates the intended label does not create an S_C or P_R discrepancy relationship.

**Classification ambiguity:** None for document role or relationship type; conditional comparator applicability is stated in the source-grounded alternatives below.

**Checker provenance:** NUM-02; XS04; SP1-CLIP-1; N106; S085. Numeric checker primary records preserved below; cross-source and statistical candidate records remain complete in their canonical checker artifacts.

- Relationship: N106.
- Compared locations/roles: REPORT [results supplement p7 eTable5 women Quantitative10.2, Difference in PPV](../../joi190039supp3_prod.pdf#page=7); REPORT [p6 eTable4 matched women Quantitative10.2 count cells](../../joi190039supp3_prod.pdf#page=6). Both are within one results report.
- Printed inputs: visible aspirin PPV15.9, placebo34.1, contrast cell shows only a minus glyph;95%CI[-34.7,-1.3]. Matched per-protocol counts aspirin TP11/FP58, placebo TP14/FP27.
- Rule/calculation/tolerance: displayed arm probabilities imply a finite negative contrast. Raw-count contrast100×(11/69−14/41)=−18.20431points, coherent with an approximately−18.2 one-decimal contrast;±0.05point rounding tolerance. No magnitude is visibly printed in that contrast cell.
- Direct observation versus inference: missing visible digits are direct visual evidence. Native extraction has displaced fragment18.2; this corroborates possible source-layout displacement but does not establish a visibly displayed estimate. The calculated contrast is a reconstruction, not a proposed correction.
- Alternatives/missing definition: the dash could deliberately mark an unavailable estimate, but a signed interval and complete arm probabilities are supplied; no dash-as-missing convention is given. A reader using extraction may recover hidden digits unavailable in ordinary source display. Missing definition: whether the dash is intentional or a displaced/truncated estimate.
- Quality-control relevance: the point contrast may be omitted or inconsistently recovered during evidence extraction; no clinical effect judgment is made.
- Exact human question: Does this source cell intentionally omit the PPV point contrast, or should a magnitude be visible alongside its95% interval?

**Mechanical evidence recheck:** Completed by fresh gpt-6.1-sol/high agent 01a12871-ed60-7951-bfc9-08725b3b7034. Minus-only visible point cell; counts reproduce -18.20431248 percentage points. Full separate facts: [evidence recheck](verification/evidence_recheck.md).

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Women's quantitative 17.0 PPV contrast lacks a visible magnitude

**Candidate statement:** Women's quantitative 17.0 PPV contrast lacks a visible magnitude; requires human adjudication of the printed comparison and any named conditional basis.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results eTable 5 vs REPORT results eTable 4

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both conflicting locations are within one REPORT document. A separate source that merely corroborates the intended label does not create an S_C or P_R discrepancy relationship.

**Classification ambiguity:** None for document role or relationship type; conditional comparator applicability is stated in the source-grounded alternatives below.

**Checker provenance:** NUM-03; XS05; SP1-CLIP-2; N108; S087. Numeric checker primary records preserved below; cross-source and statistical candidate records remain complete in their canonical checker artifacts.

- Relationship: N108.
- Compared locations/roles: REPORT [results supplement p7 eTable5 women Quantitative17.0, Difference in PPV](../../joi190039supp3_prod.pdf#page=7); REPORT [p6 eTable4 matched women Quantitative17.0 count cells](../../joi190039supp3_prod.pdf#page=6).
- Printed inputs: aspirin PPV17.1, placebo42.9; contrast visibly minus glyph only;95%CI[-48.4,-0.7]. Per-protocol counts aspirin TP6/FP29, placebo TP9/FP12.
- Rule/calculation/tolerance:100×(6/35−9/21)=−25.71429points, coherently approximately−25.7 at one-decimal precision±0.05point. The visible contrast cell supplies no magnitude.
- Direct observation versus inference: direct absence of visible digits; native displaced fragment25.7 is a transcription aid only; count-derived contrast is diagnostic.
- Alternatives/missing definition: dash-as-unavailable versus layout truncation; the signed interval is present and no dash convention supplied. Missing definition is the intended visible point estimate/reporting convention for this cell.
- Quality-control relevance: this is a different test threshold/result fromNUM-02 and must remain a separately traceable observation.
- Exact human question: Is a numeric PPV contrast intended to be shown in this quantitative17.0 cell, and what explains the visible minus-only display?

**Mechanical evidence recheck:** Completed by fresh gpt-6.1-sol/high agent 01a12871-ed60-7951-bfc9-08725b3b7034. Minus-only visible point cell; counts reproduce -25.71428571 percentage points. Full separate facts: [evidence recheck](verification/evidence_recheck.md).

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Women's qualitative 10.2 PPV contrast lacks a visible magnitude

**Candidate statement:** Women's qualitative 10.2 PPV contrast lacks a visible magnitude; requires human adjudication of the printed comparison and any named conditional basis.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results eTable 5 vs REPORT results eTable 4

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both conflicting locations are within one REPORT document. A separate source that merely corroborates the intended label does not create an S_C or P_R discrepancy relationship.

**Classification ambiguity:** None for document role or relationship type; conditional comparator applicability is stated in the source-grounded alternatives below.

**Checker provenance:** NUM-04; XS06; SP1-CLIP-3; N110; S089. Numeric checker primary records preserved below; cross-source and statistical candidate records remain complete in their canonical checker artifacts.

- Relationship: N110.
- Compared locations/roles: REPORT [results supplement p7 eTable5 women Qualitative10.2, Difference in PPV](../../joi190039supp3_prod.pdf#page=7); REPORT [p6 eTable4 matched women Qualitative10.2 count cells](../../joi190039supp3_prod.pdf#page=6).
- Printed inputs: aspirin PPV9.7, placebo31.2; contrast visibly minus glyph only;95%CI[-38.9,-3.9]. Per-protocol counts aspirin TP6/FP56, placebo TP10/FP22.
- Rule/calculation/tolerance:100×(6/62−10/32)=−21.57258points, coherently approximately−21.6 at one-decimal precision±0.05point.31.2 placebo is compatible with31.25% at rounding tie; this is not a separate arithmetic mismatch.
- Direct observation versus inference: visible digits absent; native displaced fragment21.6 is not substituted into visible source. Count reconstruction is diagnostic.
- Alternatives/missing definition: intentional dash for omitted contrast versus source-layout displacement; signed interval and both arm estimates are available; missing convention for dash-as-unavailable.
- Quality-control relevance: distinct qualitative-test result could be omitted or recovered differently in downstream extraction; no paper-level conclusion claim.
- Exact human question: Should the qualitative10.2 women's PPV cell display a numeric contrast with this interval, or does the dash have an intentional reporting meaning?

**Mechanical evidence recheck:** Completed by fresh gpt-6.1-sol/high agent 01a12871-ed60-7951-bfc9-08725b3b7034. Minus-only visible point cell; counts reproduce -21.57258065 percentage points. Full separate facts: [evidence recheck](verification/evidence_recheck.md).

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — SAP lower FIT threshold lacks its mass-unit symbol

**Candidate statement:** SAP lower FIT threshold lacks its mass-unit symbol; requires human adjudication of the printed comparison and any named conditional basis.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN SAP p. 6 section 3.2 paired 17 µg Hb/g expression vs PLAN SAP p. 6 section 3.2 10.2 Hb/g expression; PLAN SAP p. 8 complete FD threshold unit corroborates only

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both conflicting locations are inside supplied PLAN material. Historical, operational and financial content remains PLAN. No REPORT location is a conflicting comparator; any report corroboration does not create P_R.

**Classification ambiguity:** None for document role or relationship type; conditional comparator applicability is stated in the source-grounded alternatives below.

**Registration correction after source recheck:** The original p. 8 lower-cutoff comparator was described as the same primary threshold. Direct recheck identifies it as qualitative FD Hb/Hp content. The registered visible-unit omission remains within p. 6, with p. 8 unit context corroborating only. Category and P_P relationship remain confirmed.

**Checker provenance:** PN04; XS02; N544. Numeric checker primary records preserved below; cross-source and statistical candidate records remain complete in their canonical checker artifacts.

- **Relationship:** N544.
- **Compared locations and document roles:** [SAP p. 6](../../joi190039supp2_prod.pdf#page=6) section 3.2 paired threshold expressions: 17 µg Hb/g feces versus 10.2 Hb/g feces, both PLAN. [SAP p. 8](../../joi190039supp2_prod.pdf#page=8) provides a complete unit for the qualitative FD Hb/Hp threshold as corroborating context only.
- **Printed inputs:** SAP p. 6 prints 17 µg Hb/g feces and 10.2 Hb/g feces in the FOBGold categorical-variable definition. SAP p. 8 prints complete 10.2 µg Hb/g feces for the qualitative FD Hb/Hp threshold. Identical test-specific endpoint alignment is not asserted.
- **Reproducible rule, calculation, tolerance, observation/inference:** Exact dimensional-label comparison: numeric 10.2 agrees, but µg is missing before Hb/g on p. 6. Visual source inspection confirms the omission rather than OCR loss. No rounding tolerance for a missing unit; no buffer-to-feces conversion attempted.
- **Source-grounded alternatives and missing definitions:** Reader can inherit µg from preceding 17 µg threshold, so intended unit is inferable; standalone printed lower-threshold label remains incomplete.
- **Exact human question:** Should 10.2 in the primary-variable definition explicitly carry µg Hb/g feces, or is the symbol deliberately shared with the preceding threshold?
- **Quality-control relevance:** A cutoff extracted separately may lose its intended mass unit.

**Mechanical evidence recheck:** Completed by fresh gpt-6.1-sol/high agent 01a12871-ed60-7951-bfc9-08725b3b7034. p. 6 directly omits µg before 10.2 Hb/g in its paired-threshold expression. Full separate facts: [evidence recheck](verification/evidence_recheck.md).

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Total trial duration and dated timeline use an unspecified basis

**Candidate statement:** Total trial duration and dated timeline use an unspecified basis; requires human adjudication of the printed comparison and any named conditional basis.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol duration field vs PLAN dated schedule

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both conflicting locations are inside supplied PLAN material. Historical, operational and financial content remains PLAN. No REPORT location is a conflicting comparator; any report corroboration does not create P_R.

**Classification ambiguity:** None for document role or relationship type; conditional comparator applicability is stated in the source-grounded alternatives below.

**Checker provenance:** PN01; N516. Numeric checker primary records preserved below; cross-source and statistical candidate records remain complete in their canonical checker artifacts.

- **Relationship:** N516.
- **Compared locations and document roles:** [Protocol p. 14](../../joi190039supp1_prod.pdf#page=14) section 3.11; PLAN duration field versus PLAN preparation/completion dates.
- **Printed inputs:** Total duration 60 months; preparation January 2012; last subject out June 2017, defined as study end; report March 2018. Clinical phase June 2013 to June 2017 is 48 months.
- **Reproducible rule, calculation, tolerance, observation/inference:** Preparation-to-end: 12×(2017−2012)+(6−1)=65 months. Preparation-to-report: 74 months. Clinical interval is 48 and agrees. ±1 month for unspecified within-month dates cannot explain five-month difference. Printed fields direct; proposed total-duration endpoints inferred.
- **Source-grounded alternatives and missing definitions:** Total duration could mean a funded period starting June 2012 or exclude early preparation; no such endpoint definition supplied. Report completion need not be study end.
- **Exact human question:** Which start/end milestones define the 60-month total, and should the total-duration field or dated schedule be clarified?
- **Quality-control relevance:** Duration labels can enter plan summaries; this does not establish any actual recruitment discrepancy.

**Mechanical evidence recheck:** Completed by fresh gpt-6.1-sol/high agent 01a12871-ed60-7951-bfc9-08725b3b7034. 60-month total beside January 2012 preparation and June 2017 study-end schedule; intended total endpoints missing. Full separate facts: [evidence recheck](verification/evidence_recheck.md).

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Three working days are equated with 72 hours

**Candidate statement:** Three working days are equated with 72 hours; requires human adjudication of the printed comparison and any named conditional basis.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol working-day phrase vs PLAN parenthetical hours

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both conflicting locations are inside supplied PLAN material. Historical, operational and financial content remains PLAN. No REPORT location is a conflicting comparator; any report corroboration does not create P_R.

**Classification ambiguity:** None for document role or relationship type; conditional comparator applicability is stated in the source-grounded alternatives below.

**Checker provenance:** PN02; N536. Numeric checker primary records preserved below; cross-source and statistical candidate records remain complete in their canonical checker artifacts.

- **Relationship:** N536.
- **Compared locations and document roles:** [Protocol p. 53](../../joi190039supp1_prod.pdf#page=53) Appendix 1, second assessor's return deadline; PLAN phrase versus PLAN parenthetical time quantity.
- **Printed inputs:** Second assessment returned within the next 3 working days (72 hours). Nearby fatal/other SUSAR deadlines explicitly use calendar days.
- **Reproducible rule, calculation, tolerance, observation/inference:** Three calendar days = 3×24 =72 hours. Under a Monday–Friday working week, a Friday-to-next-Wednesday interval spans the next three working days but 120 elapsed hours. Exact unit comparison; no rounding. Phrase direct, weekend example diagnostic rather than recorded event.
- **Source-grounded alternatives and missing definitions:** With weekend-free intervals or all days treated as working days, the quantities coincide. Working-calendar convention is absent. Separate investigator 24-hour/next-working-day alternatives are explicit and not challenged.
- **Exact human question:** Does the parenthesis mean 72 elapsed hours or 3 working days, and which calendar convention governs that equivalence?
- **Quality-control relevance:** Concrete operational time-unit ambiguity; no legal-compliance or clinical-safety judgment.

**Mechanical evidence recheck:** Completed by fresh gpt-6.1-sol/high agent 01a12871-ed60-7951-bfc9-08725b3b7034. Literal 3 working days (72 hours) equivalence printed without a working-calendar definition. Full separate facts: [evidence recheck](verification/evidence_recheck.md).

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — General blood-tube range excludes a listed serum-tube volume

**Candidate statement:** General blood-tube range excludes a listed serum-tube volume; requires human adjudication of the printed comparison and any named conditional basis.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol summary volumes vs PLAN tube-specific options

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both conflicting locations are inside supplied PLAN material. Historical, operational and financial content remains PLAN. No REPORT location is a conflicting comparator; any report corroboration does not create P_R.

**Classification ambiguity:** None for document role or relationship type; conditional comparator applicability is stated in the source-grounded alternatives below.

**Checker provenance:** PN03; N541. Numeric checker primary records preserved below; cross-source and statistical candidate records remain complete in their canonical checker artifacts.

- **Relationship:** N541.
- **Compared locations and document roles:** [Protocol p. 56](../../joi190039supp1_prod.pdf#page=56) Appendix 2 opening paragraph versus serum-specific tube list; both PLAN.
- **Printed inputs:** Four extra tubes of blood 9–10 mL each (2 EDTA and 2 serum); serum 8.5–9 mL with listed Vacutainer 8.5 mL option; EDTA 9–10 mL.
- **Reproducible rule, calculation, tolerance, observation/inference:** 8.5 mL is below the stated 9 mL minimum for each tube. Minimum specific total 2×8.5+2×9=35 mL versus opening 4×9=36 mL. Specific 8.5 is printed to 0.1 mL, but opening integer 9 may be a rounded summary. Values direct; total diagnostic.
- **Source-grounded alternatives and missing definitions:** General range could intentionally round 8.5 upward or give nominal approximate volumes; opening text does not say approximately or identify an exception. Manufacturers are explicit alternatives.
- **Exact human question:** Should the general per-tube range include 8.5 mL or explicitly state rounding/a serum-tube exception?
- **Quality-control relevance:** Summary versus specific volume label could affect extraction of planned sample burden.

**Mechanical evidence recheck:** Completed by fresh gpt-6.1-sol/high agent 01a12871-ed60-7951-bfc9-08725b3b7034. General 9-10 mL each versus explicitly listed 8.5 mL serum option. Full separate facts: [evidence recheck](verification/evidence_recheck.md).

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — Pharmacovigilance subtotal depends on an ambiguous component separator

**Candidate statement:** Pharmacovigilance subtotal depends on an ambiguous component separator; requires human adjudication of the printed comparison and any named conditional basis.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol category 6 total vs PLAN components and total definition

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both conflicting locations are inside supplied PLAN material. Historical, operational and financial content remains PLAN. No REPORT location is a conflicting comparator; any report corroboration does not create P_R.

**Classification ambiguity:** None for document role or relationship type; conditional comparator applicability is stated in the source-grounded alternatives below.

**Checker provenance:** PN05; N565. Numeric checker primary records preserved below; cross-source and statistical candidate records remain complete in their canonical checker artifacts.

- **Relationship:** N565.
- **Compared locations and document roles:** [Protocol p. 60](../../joi190039supp1_prod.pdf#page=60) row 6 subtotal and its six components; [Protocol p. 61](../../joi190039supp1_prod.pdf#page=61) double-asterisk total definition; all PLAN.
- **Printed inputs:** Subtotal 28,922 EUR; components 884; 2,272; 15,600; 8,616; 1.704; 1,548 EUR. Listing component visibly has a dot; surrounding thousands use commas.
- **Reproducible rule, calculation, tolerance, observation/inference:** If 1.704 means 1704, sum =30,624 EUR, 1,702 above subtotal. If decimal 1.704 EUR, sum=28,921.704 EUR, rounding to 28,922. Whole-euro ±0.50 tolerance reconciles only latter. Punctuation and inputs direct; locale interpretation conditional.
- **Source-grounded alternatives and missing definitions:** Decimal interpretation exactly reconciles rounded subtotal. German thousands punctuation supports 1704, with different magnitude. No monetary locale/fractional precision rule supplied. Do not silently normalize the separator.
- **Exact human question:** Does 1.704 denote 1704 EUR or 1.704 EUR, and what subtotal and separator convention should this component use?
- **Quality-control relevance:** Arithmetic and magnitude ambiguity within a budget line; no financial-adjudication claim.

**Mechanical evidence recheck:** Completed by fresh gpt-6.1-sol/high agent 01a12871-ed60-7951-bfc9-08725b3b7034. Dot in 1.704 confirmed; decimal branch rounds to subtotal, thousands branch differs by 1702 EUR. Full separate facts: [evidence recheck](verification/evidence_recheck.md).

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — Blood-tube supplies total requires an unspecified procurement basis

**Candidate statement:** Blood-tube supplies total requires an unspecified procurement basis; requires human adjudication of the printed comparison and any named conditional basis.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol supplies total vs PLAN tube-price/quantity footnote

**Review domain:** plan_material

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Both conflicting locations are inside supplied PLAN material. Historical, operational and financial content remains PLAN. No REPORT location is a conflicting comparator; any report corroboration does not create P_R.

**Classification ambiguity:** None for document role or relationship type; conditional comparator applicability is stated in the source-grounded alternatives below.

**Registration interpretation after source recheck:** No purchasing participant base; optional consent directly prevents assuming 2400 purchases. The original conditional calculation below is preserved as provenance, not a reproduced source discrepancy. The residual question is unresolved; this record remains Pending Human Adjudication.

**Checker provenance:** PN06; N574. Numeric checker primary records preserved below; cross-source and statistical candidate records remain complete in their canonical checker artifacts.

- **Relationship:** N574.
- **Compared locations and document roles:** [Protocol p. 60](../../joi190039supp1_prod.pdf#page=60) row 12 supplies; [Protocol p. 61](../../joi190039supp1_prod.pdf#page=61) footnote 9; [Protocol p. 14](../../joi190039supp1_prod.pdf#page=14) planned sample sizes; all PLAN.
- **Printed inputs:** Supplies 2,388 EUR; 2 plasma +2 serum tubes/person; 100 plasma tubes cost 27.7 EUR, 100 serum 26.6 EUR (source image); randomized target 2400, analyzed 2000. Adjacent budget formulas explicitly use 2400.
- **Reproducible rule, calculation, tolerance, observation/inference:** For 2400, 48 packs each: 48×27.7+48×26.6=2606.4 EUR; gap 218.4. For 2000,2172 EUR also differs. Per-person 1.086 EUR gives implied 2388/1.086≈2198.895 people. Whole-euro ±0.5 plus pack-price ±0.05×96=±4.8, below gap. Printed formula inputs direct; 2400 purchasing base conditional.
- **Source-grounded alternatives and missing definitions:** Blood is optional. Uptake below 2400, stocks or discounts could reduce purchases; footnote 9 itself supplies no participant denominator. Reused locator says 26.9 but source image says 26.6; latter controls. The quantities/prices require an unstated purchasing base; no unconditional discrepancy is reproduced. The original comparison is preserved as provenance and the evidence state is record_input_error.
- **Exact human question:** What participant number, optional uptake fraction, or procurement modifier reconciles 2388 EUR with 2+2 tubes/person and 27.7/26.6 EUR per 100?
- **Quality-control relevance:** Conditional linked budget formula question; not a claim every randomized person gave blood.

**Mechanical evidence recheck:** Completed by fresh gpt-6.1-sol/high agent 01a12871-ed60-7951-bfc9-08725b3b7034. No purchasing participant base; optional consent directly prevents assuming 2400 purchases. Full separate facts: [evidence recheck](verification/evidence_recheck.md).

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C012 — Insurance amount differs from its printed per-person formula

**Candidate statement:** Insurance amount differs from its printed per-person formula; requires human adjudication of the printed comparison and any named conditional basis.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol insurance amount vs PLAN attached formula

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both conflicting locations are inside supplied PLAN material. Historical, operational and financial content remains PLAN. No REPORT location is a conflicting comparator; any report corroboration does not create P_R.

**Classification ambiguity:** None for document role or relationship type; conditional comparator applicability is stated in the source-grounded alternatives below.

**Checker provenance:** PN07; N580. Numeric checker primary records preserved below; cross-source and statistical candidate records remain complete in their canonical checker artifacts.

- **Relationship:** N580.
- **Compared locations and document roles:** [Protocol p. 61](../../joi190039supp1_prod.pdf#page=61) row 15 versus [Protocol p. 62](../../joi190039supp1_prod.pdf#page=62) footnote 15; both PLAN.
- **Printed inputs:** Insurance total 67,116 EUR; attached formula 23.50 EUR/person×2400. Overhead/tax/combined-budget fields on p 61 are blank.
- **Reproducible rule, calculation, tolerance, observation/inference:** 23.50×2400=56,400 EUR; gap 10,716 EUR. 67,116/56,400=1.19 exactly; total implies 27.965 EUR/person. Rate-cent uncertainty±0.005×2400=±12 EUR plus total±0.5 cannot explain gap. Ratio diagnostic, not evidence of a tax rule.
- **Source-grounded alternatives and missing definitions:** An unprinted 19% modifier could reconcile values. Package does not state insurance tax/overhead convention, and no external rule imported; footnote has no modifier. Blank general tax/overhead fields are not zeros.
- **Exact human question:** Does 67,116 EUR include an unprinted 19% addition or other adjustment, and what modifier/unit rate belongs in footnote 15?
- **Quality-control relevance:** Explicit formula and budget amount otherwise yield different numeric extractions.

**Mechanical evidence recheck:** Completed by fresh gpt-6.1-sol/high agent 01a12871-ed60-7951-bfc9-08725b3b7034. 23.50 x 2400 = 56400, whereas attached total is 67116; exact ratio 1.19 has no printed modifier. Full separate facts: [evidence recheck](verification/evidence_recheck.md).

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C013 — Overall budget differs from the sum of its 16 category totals

**Candidate statement:** Overall budget differs from the sum of its 16 category totals; requires human adjudication of the printed comparison and any named conditional basis.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol 16 category totals vs PLAN overall budget

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both conflicting locations are inside supplied PLAN material. Historical, operational and financial content remains PLAN. No REPORT location is a conflicting comparator; any report corroboration does not create P_R.

**Classification ambiguity:** None for document role or relationship type; conditional comparator applicability is stated in the source-grounded alternatives below.

**Checker provenance:** PN08; N585. Numeric checker primary records preserved below; cross-source and statistical candidate records remain complete in their canonical checker artifacts.

- **Relationship:** N585.
- **Compared locations and document roles:** [Protocol p. 59](../../joi190039supp1_prod.pdf#page=59) category totals 1–4; [Protocol p. 60](../../joi190039supp1_prod.pdf#page=60) totals 5–12; [Protocol p. 61](../../joi190039supp1_prod.pdf#page=61) totals 13–16 and study budget; all PLAN.
- **Printed inputs:** Category totals:13,383;153,000;30,950;24,790;3,000;28,922;40,642;12,731;60,000;3,400;2,430;24,881;500;6,800;67,116;35,060 EUR. Study budget 505,570 EUR.
- **Reproducible rule, calculation, tolerance, observation/inference:** Sum =507,605 EUR; difference 2,035. Use printed row 6 subtotal 28,922, not its reconstructed components, so independent from PN05. Maximum 16×0.5+0.5=8.5 EUR rounding tolerance much below difference. Nested components not counted again.
- **Source-grounded alternatives and missing definitions:** A credit, excluded category, overlap or prior budget version might account for adjustment, but no such rule printed. Blank overhead/tax/funds fields do not supply adjustment. All displayed top-level totals directly sourced; sum diagnostic.
- **Exact human question:** Which stated inclusion rule or adjustment reconciles 505,570 EUR with 507,605 EUR summed from 16 category totals?
- **Quality-control relevance:** Independent total-arithmetic observation in PLAN financial material.

**Mechanical evidence recheck:** Completed by fresh gpt-6.1-sol/high agent 01a12871-ed60-7951-bfc9-08725b3b7034. Printed category sum 507605 differs from 505570 by 2035 EUR. Full separate facts: [evidence recheck](verification/evidence_recheck.md).

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C014 — Printing amount differs between its budget line and linked footnote

**Candidate statement:** Printing amount differs between its budget line and linked footnote; requires human adjudication of the printed comparison and any named conditional basis.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol printing line vs PLAN linked printing footnote

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both conflicting locations are inside supplied PLAN material. Historical, operational and financial content remains PLAN. No REPORT location is a conflicting comparator; any report corroboration does not create P_R.

**Classification ambiguity:** None for document role or relationship type; conditional comparator applicability is stated in the source-grounded alternatives below.

**Checker provenance:** PN09; N581. Numeric checker primary records preserved below; cross-source and statistical candidate records remain complete in their canonical checker artifacts.

- **Relationship:** N581.
- **Compared locations and document roles:** [Protocol p. 61](../../joi190039supp1_prod.pdf#page=61) row 16 printing subitem linked tofootnote 16 versus [Protocol p. 62](../../joi190039supp1_prod.pdf#page=62) footnote 16; both PLAN.
- **Printed inputs:** Printing orders 3,000 EUR; linked footnote states printing of all study documents 3,500 EUR, plus further possible color costs. Flyer 350–500 and questionnaire 1045 EUR are ancillary estimates.
- **Reproducible rule, calculation, tolerance, observation/inference:** Matched line and linked all-documents estimate differ 500 EUR; ±0.5 each cannot explain. Do not sum ancillary prices as exhaustive components. Amounts/direct attachment observed.
- **Source-grounded alternatives and missing definitions:** Table could cover narrower documents or older estimate; linked footnote does not distinguish a scope/version. Possible further color costs are additional to stated 3500, not a displayed reconciliation with 3000.
- **Exact human question:** Is the 3000 EUR printing line a different subset/estimate from its attached 3500 EUR all-documents footnote, and what value/scope should be communicated?
- **Quality-control relevance:** Matched monetary text/table discrepancy can yield differing extracted budgets.

**Mechanical evidence recheck:** Completed by fresh gpt-6.1-sol/high agent 01a12871-ed60-7951-bfc9-08725b3b7034. Attached printing estimates 3000 and 3500 EUR differ by 500; scope/version absent. Full separate facts: [evidence recheck](verification/evidence_recheck.md).

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C015 — Meeting frequency and cost bundle require an attendance basis

**Candidate statement:** Meeting frequency and cost bundle require an attendance basis; requires human adjudication of the printed comparison and any named conditional basis.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol meeting total vs PLAN linked cost/frequency footnote

**Review domain:** plan_material

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Both conflicting locations are inside supplied PLAN material. Historical, operational and financial content remains PLAN. No REPORT location is a conflicting comparator; any report corroboration does not create P_R.

**Classification ambiguity:** None for document role or relationship type; conditional comparator applicability is stated in the source-grounded alternatives below.

**Registration interpretation after source recheck:** 480 + 500 = 980 reconciles printed bundle; applying 480 separately to all four meetings is unsupported. The original conditional calculation below is preserved as provenance, not a reproduced source discrepancy. The residual question is unresolved; this record remains Pending Human Adjudication.

**Checker provenance:** PN10; N583. Numeric checker primary records preserved below; cross-source and statistical candidate records remain complete in their canonical checker artifacts.

- **Relationship:** N583.
- **Compared locations and document roles:** [Protocol p. 61](../../joi190039supp1_prod.pdf#page=61) row 16 meeting/hotel linked footnote 18 versus [Protocol p. 62](../../joi190039supp1_prod.pdf#page=62) footnote 18; both PLAN.
- **Printed inputs:** Table 980 EUR; footnote one meeting/year,4 meetings total; hotel 80 EUR and travel 80 EUR for 3 people=480 EUR; further possible 500 EUR.
- **Reproducible rule, calculation, tolerance, observation/inference:** (80+80)×3=480;480+500=980 equals table. If cost bundle applies per meeting,4×480+500=2420, gap 1440. Exact 4 meeting count and single-bundle amounts observed; per-meeting applicability explicitly conditional, not silently imposed. Rounding under±several EUR cannot explain conditional gap.
- **Source-grounded alternatives and missing definitions:** 80+80 may be aggregate across meetings, only one may require travel for 3 people, other meetings may be remote/local, or funded in other lines. Per-meeting/aggregate attendance basis absent, so no assertion all 4 incur identical costs. Concrete linked frequency plus table total motivates question.
- **Exact human question:** Do 80 EUR hotel and 80 EUR travel for 3 people apply per meeting or across all 4, and what attendance/allocation rule reconciles 980 EUR with 4 meeting description?
- **Quality-control relevance:** Conditional frequency-versus-cost-bundle label question; not an allegation of omitted actual spending.

**Mechanical evidence recheck:** Completed by fresh gpt-6.1-sol/high agent 01a12871-ed60-7951-bfc9-08725b3b7034. 480 + 500 = 980 reconciles printed bundle; applying 480 separately to all four meetings is unsupported. Full separate facts: [evidence recheck](verification/evidence_recheck.md).

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C016 — Study-center and practice payment rates require component matching

**Candidate statement:** Study-center and practice payment rates require component matching; requires human adjudication of the printed comparison and any named conditional basis.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol center incentive vs PLAN practice-related budget footnote

**Review domain:** plan_material

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Both conflicting locations are inside supplied PLAN material. Historical, operational and financial content remains PLAN. No REPORT location is a conflicting comparator; any report corroboration does not create P_R.

**Classification ambiguity:** None for document role or relationship type; conditional comparator applicability is stated in the source-grounded alternatives below.

**Registration interpretation after source recheck:** 30 x 2000 = 60000 reconciles; identity with the 75-EUR study-center incentive is not established. The original conditional calculation below is preserved as provenance, not a reproduced source discrepancy. The residual question is unresolved; this record remains Pending Human Adjudication.

**Checker provenance:** PN11; N569. Numeric checker primary records preserved below; cross-source and statistical candidate records remain complete in their canonical checker artifacts.

- **Relationship:** N569.
- **Compared locations and document roles:** [Protocol p. 26](../../joi190039supp1_prod.pdf#page=26) section 6.9 versus [Protocol p. 60](../../joi190039supp1_prod.pdf#page=60) practice-related compensation row 9 and [Protocol p. 61](../../joi190039supp1_prod.pdf#page=61) footnote 6; all PLAN.
- **Printed inputs:** Study centers 75 EUR per recruited patient, payable after colonoscopy/histology or completed study without colonoscopy within 3 months. Practice compensation 60,000 EUR; footnote 30 EUR/completed case×2000.
- **Reproducible rule, calculation, tolerance, observation/inference:** 30×2000=60000 reconciles budget; per-case rate 75 versus 30 differs 45 EUR for a recruited case meeting the narrative completion trigger. Same 2000 casesat 75→150000;2400 recruitedat 75→180000, but different eligibility bases not silently aligned. ±0.5 perrate allows±1,below 45.
- **Source-grounded alternatives and missing definitions:** 30 could be a partial component, different recipient, or older estimate. Recruited versus completed denominators differ; whether either payment triggers the other is not established. Row 9 includes practices wording; linked footnote doesnot clarify separate component/recipient. Identity conditional; differing printed rates are retained as provenance without establishing a same-payment contradiction.
- **Exact human question:** Is 30 EUR/completed case practice compensation the same payment as 75 EUR/recruited patient study-center incentive, or a distinct component/recipient, and how should amount and payment denominator be distinguished?
- **Quality-control relevance:** Concrete unit-rate/recipient labeling question within PLAN; no claim about actual payments.

**Mechanical evidence recheck:** Completed by fresh gpt-6.1-sol/high agent 01a12871-ed60-7951-bfc9-08725b3b7034. 30 x 2000 = 60000 reconciles; identity with the 75-EUR study-center incentive is not established. Full separate facts: [evidence recheck](verification/evidence_recheck.md).

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

