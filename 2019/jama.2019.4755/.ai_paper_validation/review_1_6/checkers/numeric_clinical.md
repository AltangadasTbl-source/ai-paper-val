# Clinical numeric consistency review

Fresh runtime agent ID: 01a12869-4940-75a1-9683-5c660f25dc14. Fixed model/effort: gpt-6.1-sol/medium. Exact disjoint scope: REPORT DOC-001 main article physical pp.1–7, REPORT DOC-004 non-plan results supplement physical pp.1–8, REPORT DOC-005 retrospective availability p.1. PLAN relationships exclusively belong to the separate N501 onward shard. Sources/reused assets preserved. No web, old candidate/report/checker conclusions, arbitrary Python, or external raw data were used.

120 relationships N001–N120 are NUMERIC_CHECK_COMPLETE in numeric_relationship_inventory.md. Five distinct lane-local observations are emitted below, without stable C IDs, severity, validity, dispositions or adjudication. Every observation requires human adjudication. Numeric outcomes in the inventory are checks of printed inputs, not scientific acceptance decisions.

## Complete checks and limitations

All Table1 characteristics, all Figure flow branches, all nine Table2 diagnostic rows, all eighteen Table3 predictive-value relationships, all20 eTable2 sample rows, allnine eTable3 combined-test rows, allnine eTable4 per-protocol rows, alleighteen eTable5 predictive relationships, allnine eTable6 site rows and their18 SD/P pairs were checked. Clinical counts, displayed percentages and differences reconcile within their stated precision. Detection rows were checked for both arm totals, disease/non-disease denominators, allfour men+women count sums and cutoff nesting. Any sample rows equal each of ten column totals across four scheduled rows; sample counts were not confused with unique people. ITS/PP, randomized/analyzed and scheduled/actual-day populations were kept distinct. Every clinical diagnostic arm percentage and every printable raw contrast agrees with its matched counts.

Exact integers use zero tolerance. One-decimal probabilities/percentage-point contrasts use ±0.05 percentage points, integer displays ±0.5; tie endpoints are allowed. Raw count ratios are differenced before rounding. For example Table2 all quantitative17 gives32/112×100−23/102×100=6.02241 points, coherently printed6.0 despite28.6−22.5=6.1 at rounded arm precision. eTable5 women qualitative placebo10/32×100=31.25 is compatible31.2 under tie rounding. No candidate arises from these displays.

eTable6 SD zeros are boundary parameter estimates and are not P zeros. All18 source P values are between .16 and .50, consistent with main p5. The B069 SD/P locator labels already match the source; no map correction is required. There is no display-zero-P candidate. P-test formula, adjusted interval calculations and inferential narrative scope receive independent statistical coverage; no model/variance/test was invented here.

The abstract1219men refers grammatically to2422randomized;1219/2422=50.3303% coherently rounds50%. Table1's1075men refer to2134analyzed, so these are not demonstrated contradictory counts. Approximately4% primary exclusions can describe92/2134=4.31% lost quantitative samples or10/224=4.46% disease-positive losses. Its exact subset is unspecified; alternative numerically compatible readings preclude inventing a denominator contradiction. Screening78%/diagnostic22% match known indication denominator2048 with86missing. Safety11/7 and6/5 are event/person counts, not rates or impossible percentages.

Direct-source images inspected: main PDF p5 through immutable source-linked Poppler full-page render .ai_paper_validation/document_outputs/doc-799606a72443/ocr_pages/page-5.png; results supplement p7 through current Poppler180dpi render .ai_paper_validation/review_1_6/preprocessing/support-b-results-7.png. Direct visual content controls candidate descriptions. Native text is a locator/diagnostic aid only. No fresh derivative was written by this reviewer. Missing participant-level ages, raw data/code, historical denominators, primary P-test formula and precise approximately4% subset are explicit limits. No scientific source-coverage gap in assigned clinical scope.

## NUM-01 — Missing test identity in the men's third predictive-value row

- Relationships: N048 andN049, two measures sharing exactly one missing Test cell.
- Compared locations/roles: REPORT [main p5 Table3 men third row Test cell, cutoff10.2](../../../jama_brenner_2019_oi_190039.pdf#page=5); REPORT [same p5 Table2 men qualitative10.2 row](../../../jama_brenner_2019_oi_190039.pdf#page=5). Both locations are within one report.
- Printed inputs: Table3 has blank Test cell, cutoff10.2, aspirin PPV27.5/NPV89.2, placebo PPV20/NPV90.3; contrasts7.5[-6.4,20.2] and−1.1[-5.3,3.0]. The preceding two rows explicitly say Quantitative at10.2 and17.0. Table2 men Qualitative10.2 supplies aspirin TP28,FN43,TN354,FP74; placebo TP12,FN43,TN400,FP48.
- Rule/calculation/tolerance: preserve test identity when mapping a numeric diagnostic row. Proposed qualitative alignment yields PPV28/(28+74)×100=27.45098 and12/(12+48)×100=20; NPV354/(354+43)×100=89.16877 and400/(400+43)×100=90.29345. Both displayed predictive values and contrasts reconcile within0.05points. The defect is missing measure/test identification, not incorrect arithmetic.
- Direct observation versus inference: the Test cell is visibly blank. Its qualitative identity is diagnostic inference from matching counts, numerical values and row ordering; it is not a printed label.
- Alternatives/missing definition: an intentional continuation of the preceding Quantitative label is visually possible, but conflicts with the numeric qualitative matches and would duplicate a Quantitative10.2 row; source does not declare an omitted-label convention. The missing definition is the test identity intended for this exact row.
- Quality-control relevance: a downstream extractor could assign these PPV/NPV values to the wrong test at the same cutoff. No conclusion impact is asserted.
- Exact human question: Which test is intended for the men's third Table3 row at10.2, and is the blank Test cell an omitted label requiring clarification?

## NUM-02 — Women's quantitative10.2 PPV contrast lacks a visible magnitude

- Relationship: N106.
- Compared locations/roles: REPORT [results supplement p7 eTable5 women Quantitative10.2, Difference in PPV](../../../joi190039supp3_prod.pdf#page=7); REPORT [p6 eTable4 matched women Quantitative10.2 count cells](../../../joi190039supp3_prod.pdf#page=6). Both are within one results report.
- Printed inputs: visible aspirin PPV15.9, placebo34.1, contrast cell shows only a minus glyph;95%CI[-34.7,-1.3]. Matched per-protocol counts aspirin TP11/FP58, placebo TP14/FP27.
- Rule/calculation/tolerance: displayed arm probabilities imply a finite negative contrast. Raw-count contrast100×(11/69−14/41)=−18.20431points, coherent with an approximately−18.2 one-decimal contrast;±0.05point rounding tolerance. No magnitude is visibly printed in that contrast cell.
- Direct observation versus inference: missing visible digits are direct visual evidence. Native extraction has displaced fragment18.2; this corroborates possible source-layout displacement but does not establish a visibly displayed estimate. The calculated contrast is a reconstruction, not a proposed correction.
- Alternatives/missing definition: the dash could deliberately mark an unavailable estimate, but a signed interval and complete arm probabilities are supplied; no dash-as-missing convention is given. A reader using extraction may recover hidden digits unavailable in ordinary source display. Missing definition: whether the dash is intentional or a displaced/truncated estimate.
- Quality-control relevance: the point contrast may be omitted or inconsistently recovered during evidence extraction; no clinical effect judgment is made.
- Exact human question: Does this source cell intentionally omit the PPV point contrast, or should a magnitude be visible alongside its95% interval?

## NUM-03 — Women's quantitative17.0 PPV contrast lacks a visible magnitude

- Relationship: N108.
- Compared locations/roles: REPORT [results supplement p7 eTable5 women Quantitative17.0, Difference in PPV](../../../joi190039supp3_prod.pdf#page=7); REPORT [p6 eTable4 matched women Quantitative17.0 count cells](../../../joi190039supp3_prod.pdf#page=6).
- Printed inputs: aspirin PPV17.1, placebo42.9; contrast visibly minus glyph only;95%CI[-48.4,-0.7]. Per-protocol counts aspirin TP6/FP29, placebo TP9/FP12.
- Rule/calculation/tolerance:100×(6/35−9/21)=−25.71429points, coherently approximately−25.7 at one-decimal precision±0.05point. The visible contrast cell supplies no magnitude.
- Direct observation versus inference: direct absence of visible digits; native displaced fragment25.7 is a transcription aid only; count-derived contrast is diagnostic.
- Alternatives/missing definition: dash-as-unavailable versus layout truncation; the signed interval is present and no dash convention supplied. Missing definition is the intended visible point estimate/reporting convention for this cell.
- Quality-control relevance: this is a different test threshold/result fromNUM-02 and must remain a separately traceable observation.
- Exact human question: Is a numeric PPV contrast intended to be shown in this quantitative17.0 cell, and what explains the visible minus-only display?

## NUM-04 — Women's qualitative10.2 PPV contrast lacks a visible magnitude

- Relationship: N110.
- Compared locations/roles: REPORT [results supplement p7 eTable5 women Qualitative10.2, Difference in PPV](../../../joi190039supp3_prod.pdf#page=7); REPORT [p6 eTable4 matched women Qualitative10.2 count cells](../../../joi190039supp3_prod.pdf#page=6).
- Printed inputs: aspirin PPV9.7, placebo31.2; contrast visibly minus glyph only;95%CI[-38.9,-3.9]. Per-protocol counts aspirin TP6/FP56, placebo TP10/FP22.
- Rule/calculation/tolerance:100×(6/62−10/32)=−21.57258points, coherently approximately−21.6 at one-decimal precision±0.05point.31.2 placebo is compatible with31.25% at rounding tie; this is not a separate arithmetic mismatch.
- Direct observation versus inference: visible digits absent; native displaced fragment21.6 is not substituted into visible source. Count reconstruction is diagnostic.
- Alternatives/missing definition: intentional dash for omitted contrast versus source-layout displacement; signed interval and both arm estimates are available; missing convention for dash-as-unavailable.
- Quality-control relevance: distinct qualitative-test result could be omitted or recovered differently in downstream extraction; no paper-level conclusion claim.
- Exact human question: Should the qualitative10.2 women's PPV cell display a numeric contrast with this interval, or does the dash have an intentional reporting meaning?

## NUM-05 — eTable5 cutoff header displays an incomplete concentration unit

- Relationship: N094, with the same source unit applying allnine eTable5 rows N094–N111; one shared header defect rather than nine duplicate candidates.
- Compared locations/roles: REPORT [results supplement p7 eTable5 Cutoff header](../../../joi190039supp3_prod.pdf#page=7); REPORT [p6 eTable4 Cutoff header](../../../joi190039supp3_prod.pdf#page=6); REPORT [main p5 Tables2/3 cutoff header](../../../jama_brenner_2019_oi_190039.pdf#page=5). The discrepancy is the incomplete visible header inside the results supplement; main article provides corroboration of intended unit.
- Printed inputs: eTable5 visible header reads Cutoff followed by [µg with no visible Hb/g] closure/denominator; row thresholds10.2 and17.0. eTable4 and main tables identify cutoff μg Hb/g. eTable5 abbreviation list separately defines g andHb. Native extraction supplies Hb/g] at a displaced position rather than the visible header.
- Rule/calculation/tolerance: these same cutoff numbers require the same dimensional concentration label: μg hemoglobin pergramfeces. μg alone denotes mass, not concentration. This is a dimensional/label identity check; numeric rounding tolerance is not applicable.
- Direct observation versus inference: the visible unit truncation is direct. A concentration-unit intention is inferred from matched cutoffs, neighboring table and extraction; no numeric concentration conversion is invented.
- Alternatives/missing definition: PDF rendering/clipping or misplaced font text could explain the omission, or the header may deliberately be abbreviated; no unit-abbreviation convention makes μg alone dimensionally equivalent to μgHb/g. Missing definition: intended complete unit and whether the source layout is truncated.
- Quality-control relevance: a cutoff can be copied with incomplete units despite numerically matching another table. This is bounded reporting/extraction risk.
- Exact human question: Is the eTable5 cutoff unit intended to be μg Hb/g, and should its full concentration denominator be visible in this header?

## Handoff

All120clinical N relationships complete; five lane-local observations NUM-01–NUM-05. All locations classify REPORT by content. No stable C IDs, category assignment, relationship-type assignment, evidence-state/disposition assignment or scientific adjudication occurs in this lane. The coordinator may merge genuine duplicate checker observations only when printed inputs, comparator and rule are identical, retaining all provenance. Source recheck should reproduce blank/missing source display directly rather than treating native hidden text as the final authority.

