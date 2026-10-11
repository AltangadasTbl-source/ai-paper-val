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

# Numeric consistency review — exclusive PLAN shard

Status: COMPLETE. Fresh runtime 01a12869-f6ef-7c82-8875-cf8b909c098a; gpt-6.1-sol/medium. Exclusive DOC-002 physical pages 1–62 and DOC-003 pages 1–10. All 72 source units mapped and checked. Inventory N501–N586:86 relationships; eleven distinct local observations PN01–PN11. PN keys are handoff identifiers, not stable C IDs. All observations Pending Human Adjudication. No severity, validity or disposition assigned.

Complete current source maps and source-linked native/layout evidence were locators. Candidate pages directly inspected through current source renders; fresh Poppler 26.01.0 derivatives plan-numeric-p14.png,p 26.png,p 60.png and current mapper renders protocol 30,53,56,61(detail),62 and SAP6 visually checked. Fresh rasterization commands and provenance recorded in relationships/numeric_plan_inventory.md. Protocol physical 49 is signed approval;physical 50 duplicates printed 49;physical 51–62 print 50–61. Evidence links always physical. No source/reused asset changed; no old candidate/checker/report conclusions, web, GPU or arbitrary Python used.

## Non-candidate checks completed

Every 86 inventory row has completed numeric checks. Reconciliations include 185/100 million×100=.000185%; explicit protocol day 3→SAP day 2 renumbering; dose-to-colonoscopy 5 elapsed days=4 full intervening days;2400 randomized−2000 analyzed=400 planned difference;10%×2000=200 advanced neoplasms=100/arm;4 blood tubes=2+2;8 kits=4 occasions×2 tests. Historical diagnostic percentages lack disease denominators; total cohort 1979 is not substituted. Statistical power/CI checks referred to statistics, with simple specificity precision diagnostic compatible 88–92% given 900 nondiseased/arm.

Budget sums 1,3,4,7,8,12,16 exactly reconcile. Salary 30000×3+21000×3=153000; training 1950+240+240=2430; courier.3×2×2400=1440; protective materials 19200/500×133+1000=6107.2 rounds 6107; delivery 3.5×52×3=546; measurement 1.5×4×2400=14400; postage 3480+21600+6000=31080. Safety event cost 100×150+2×300=15600 on implied 2000 base:2400 would different counts, but missing budget base alone is insufficient for a candidate. Two costed blood samples may be two specimen bundles rather than four tubes. Fee 6800 can equal 1700+3×1000+3×700; three budget years not assumed identical to full 48 month clinical coverage. Minimum monitoring 2076 below budget 3000 is not a contradiction. Blanks for overhead/tax/funds do not imply zeros. No supplied PLAN trial-results cells/subject-level data allow raw-data or observed population reconciliation.

## PN01 — Total trial duration and dated timeline

- **Relationship:** N516.
- **Compared locations and document roles:** [Protocol p. 14](../../../joi190039supp1_prod.pdf#page=14) section 3.11; PLAN duration field versus PLAN preparation/completion dates.
- **Printed inputs:** Total duration 60 months; preparation January 2012; last subject out June 2017, defined as study end; report March 2018. Clinical phase June 2013 to June 2017 is 48 months.
- **Reproducible rule, calculation, tolerance, observation/inference:** Preparation-to-end: 12×(2017−2012)+(6−1)=65 months. Preparation-to-report: 74 months. Clinical interval is 48 and agrees. ±1 month for unspecified within-month dates cannot explain five-month difference. Printed fields direct; proposed total-duration endpoints inferred.
- **Source-grounded alternatives and missing definitions:** Total duration could mean a funded period starting June 2012 or exclude early preparation; no such endpoint definition supplied. Report completion need not be study end.
- **Exact human question:** Which start/end milestones define the 60-month total, and should the total-duration field or dated schedule be clarified?
- **Quality-control relevance:** Duration labels can enter plan summaries; this does not establish any actual recruitment discrepancy.

## PN02 — Three working days equated with 72 hours

- **Relationship:** N536.
- **Compared locations and document roles:** [Protocol p. 53](../../../joi190039supp1_prod.pdf#page=53) Appendix 1, second assessor's return deadline; PLAN phrase versus PLAN parenthetical time quantity.
- **Printed inputs:** Second assessment returned within the next 3 working days (72 hours). Nearby fatal/other SUSAR deadlines explicitly use calendar days.
- **Reproducible rule, calculation, tolerance, observation/inference:** Three calendar days = 3×24 =72 hours. Under a Monday–Friday working week, a Friday-to-next-Wednesday interval spans the next three working days but 120 elapsed hours. Exact unit comparison; no rounding. Phrase direct, weekend example diagnostic rather than recorded event.
- **Source-grounded alternatives and missing definitions:** With weekend-free intervals or all days treated as working days, the quantities coincide. Working-calendar convention is absent. Separate investigator 24-hour/next-working-day alternatives are explicit and not challenged.
- **Exact human question:** Does the parenthesis mean 72 elapsed hours or 3 working days, and which calendar convention governs that equivalence?
- **Quality-control relevance:** Concrete operational time-unit ambiguity; no legal-compliance or clinical-safety judgment.

## PN03 — General blood-volume range and listed serum-tube option

- **Relationship:** N541.
- **Compared locations and document roles:** [Protocol p. 56](../../../joi190039supp1_prod.pdf#page=56) Appendix 2 opening paragraph versus serum-specific tube list; both PLAN.
- **Printed inputs:** Four extra tubes of blood 9–10 mL each (2 EDTA and 2 serum); serum 8.5–9 mL with listed Vacutainer 8.5 mL option; EDTA 9–10 mL.
- **Reproducible rule, calculation, tolerance, observation/inference:** 8.5 mL is below the stated 9 mL minimum for each tube. Minimum specific total 2×8.5+2×9=35 mL versus opening 4×9=36 mL. Specific 8.5 is printed to 0.1 mL, but opening integer 9 may be a rounded summary. Values direct; total diagnostic.
- **Source-grounded alternatives and missing definitions:** General range could intentionally round 8.5 upward or give nominal approximate volumes; opening text does not say approximately or identify an exception. Manufacturers are explicit alternatives.
- **Exact human question:** Should the general per-tube range include 8.5 mL or explicitly state rounding/a serum-tube exception?
- **Quality-control relevance:** Summary versus specific volume label could affect extraction of planned sample burden.

## PN04 — Lower FIT threshold missing mass unit

- **Relationship:** N544.
- **Compared locations and document roles:** [SAP p. 6](../../../joi190039supp2_prod.pdf#page=6) primary-variable threshold label versus [SAP p. 8](../../../joi190039supp2_prod.pdf#page=8) primary-analysis threshold; both PLAN.
- **Printed inputs:** SAP p. 6 prints 17 µg Hb/g feces and 10.2 Hb/g feces; p. 8 prints 17 µg Hb/g feces and 10.2 µg Hb/g feces.
- **Reproducible rule, calculation, tolerance, observation/inference:** Exact dimensional-label comparison: numeric 10.2 agrees, but µg is missing before Hb/g on p. 6. Visual source inspection confirms the omission rather than OCR loss. No rounding tolerance for a missing unit; no buffer-to-feces conversion attempted.
- **Source-grounded alternatives and missing definitions:** Reader can inherit µg from preceding 17 µg threshold, so intended unit is inferable; standalone printed lower-threshold label remains incomplete.
- **Exact human question:** Should 10.2 in the primary-variable definition explicitly carry µg Hb/g feces to match the primary-analysis statement?
- **Quality-control relevance:** A cutoff extracted separately may lose its intended mass unit.

## PN05 — Pharmacovigilance subtotal and component separator

- **Relationship:** N565.
- **Compared locations and document roles:** [Protocol p. 60](../../../joi190039supp1_prod.pdf#page=60) row 6 subtotal and its six components; [Protocol p. 61](../../../joi190039supp1_prod.pdf#page=61) double-asterisk total definition; all PLAN.
- **Printed inputs:** Subtotal 28,922 EUR; components 884; 2,272; 15,600; 8,616; 1.704; 1,548 EUR. Listing component visibly has a dot; surrounding thousands use commas.
- **Reproducible rule, calculation, tolerance, observation/inference:** If 1.704 means 1704, sum =30,624 EUR, 1,702 above subtotal. If decimal 1.704 EUR, sum=28,921.704 EUR, rounding to 28,922. Whole-euro ±0.50 tolerance reconciles only latter. Punctuation and inputs direct; locale interpretation conditional.
- **Source-grounded alternatives and missing definitions:** Decimal interpretation exactly reconciles rounded subtotal. German thousands punctuation supports 1704, with different magnitude. No monetary locale/fractional precision rule supplied. Do not silently normalize the separator.
- **Exact human question:** Does 1.704 denote 1704 EUR or 1.704 EUR, and what subtotal and separator convention should this component use?
- **Quality-control relevance:** Arithmetic and magnitude ambiguity within a budget line; no financial-adjudication claim.

## PN06 — Blood-tube supplies and specified pack prices

- **Relationship:** N574.
- **Compared locations and document roles:** [Protocol p. 60](../../../joi190039supp1_prod.pdf#page=60) row 12 supplies; [Protocol p. 61](../../../joi190039supp1_prod.pdf#page=61) footnote 9; [Protocol p. 14](../../../joi190039supp1_prod.pdf#page=14) planned sample sizes; all PLAN.
- **Printed inputs:** Supplies 2,388 EUR; 2 plasma +2 serum tubes/person; 100 plasma tubes cost 27.7 EUR, 100 serum 26.6 EUR (source image); randomized target 2400, analyzed 2000. Adjacent budget formulas explicitly use 2400.
- **Reproducible rule, calculation, tolerance, observation/inference:** For 2400, 48 packs each: 48×27.7+48×26.6=2606.4 EUR; gap 218.4. For 2000,2172 EUR also differs. Per-person 1.086 EUR gives implied 2388/1.086≈2198.895 people. Whole-euro ±0.5 plus pack-price ±0.05×96=±4.8, below gap. Printed formula inputs direct; 2400 purchasing base conditional.
- **Source-grounded alternatives and missing definitions:** Blood is optional. Uptake below 2400, stocks or discounts could reduce purchases; footnote 9 itself supplies no participant denominator. Reused locator says 26.9 but source image says 26.6; latter controls. Purchasing-base absence alone is not candidate: attached total versus stated quantities/prices is concrete comparison.
- **Exact human question:** What participant number, optional uptake fraction, or procurement modifier reconciles 2388 EUR with 2+2 tubes/person and 27.7/26.6 EUR per 100?
- **Quality-control relevance:** Conditional linked budget formula question; not a claim every randomized person gave blood.

## PN07 — Insurance subtotal and explicit formula

- **Relationship:** N580.
- **Compared locations and document roles:** [Protocol p. 61](../../../joi190039supp1_prod.pdf#page=61) row 15 versus [Protocol p. 62](../../../joi190039supp1_prod.pdf#page=62) footnote 15; both PLAN.
- **Printed inputs:** Insurance total 67,116 EUR; attached formula 23.50 EUR/person×2400. Overhead/tax/combined-budget fields on p 61 are blank.
- **Reproducible rule, calculation, tolerance, observation/inference:** 23.50×2400=56,400 EUR; gap 10,716 EUR. 67,116/56,400=1.19 exactly; total implies 27.965 EUR/person. Rate-cent uncertainty±0.005×2400=±12 EUR plus total±0.5 cannot explain gap. Ratio diagnostic, not evidence of a tax rule.
- **Source-grounded alternatives and missing definitions:** An unprinted 19% modifier could reconcile values. Package does not state insurance tax/overhead convention, and no external rule imported; footnote has no modifier. Blank general tax/overhead fields are not zeros.
- **Exact human question:** Does 67,116 EUR include an unprinted 19% addition or other adjustment, and what modifier/unit rate belongs in footnote 15?
- **Quality-control relevance:** Explicit formula and budget amount otherwise yield different numeric extractions.

## PN08 — Overall study-budget sum

- **Relationship:** N585.
- **Compared locations and document roles:** [Protocol p. 59](../../../joi190039supp1_prod.pdf#page=59) category totals 1–4; [Protocol p. 60](../../../joi190039supp1_prod.pdf#page=60) totals 5–12; [Protocol p. 61](../../../joi190039supp1_prod.pdf#page=61) totals 13–16 and study budget; all PLAN.
- **Printed inputs:** Category totals:13,383;153,000;30,950;24,790;3,000;28,922;40,642;12,731;60,000;3,400;2,430;24,881;500;6,800;67,116;35,060 EUR. Study budget 505,570 EUR.
- **Reproducible rule, calculation, tolerance, observation/inference:** Sum =507,605 EUR; difference 2,035. Use printed row 6 subtotal 28,922, not its reconstructed components, so independent from PN05. Maximum 16×0.5+0.5=8.5 EUR rounding tolerance much below difference. Nested components not counted again.
- **Source-grounded alternatives and missing definitions:** A credit, excluded category, overlap or prior budget version might account for adjustment, but no such rule printed. Blank overhead/tax/funds fields do not supply adjustment. All displayed top-level totals directly sourced; sum diagnostic.
- **Exact human question:** Which stated inclusion rule or adjustment reconciles 505,570 EUR with 507,605 EUR summed from 16 category totals?
- **Quality-control relevance:** Independent total-arithmetic observation in PLAN financial material.

## PN09 — Printing total in table and its footnote

- **Relationship:** N581.
- **Compared locations and document roles:** [Protocol p. 61](../../../joi190039supp1_prod.pdf#page=61) row 16 printing subitem linked tofootnote 16 versus [Protocol p. 62](../../../joi190039supp1_prod.pdf#page=62) footnote 16; both PLAN.
- **Printed inputs:** Printing orders 3,000 EUR; linked footnote states printing of all study documents 3,500 EUR, plus further possible color costs. Flyer 350–500 and questionnaire 1045 EUR are ancillary estimates.
- **Reproducible rule, calculation, tolerance, observation/inference:** Matched line and linked all-documents estimate differ 500 EUR; ±0.5 each cannot explain. Do not sum ancillary prices as exhaustive components. Amounts/direct attachment observed.
- **Source-grounded alternatives and missing definitions:** Table could cover narrower documents or older estimate; linked footnote does not distinguish a scope/version. Possible further color costs are additional to stated 3500, not a displayed reconciliation with 3000.
- **Exact human question:** Is the 3000 EUR printing line a different subset/estimate from its attached 3500 EUR all-documents footnote, and what value/scope should be communicated?
- **Quality-control relevance:** Matched monetary text/table discrepancy can yield differing extracted budgets.

## PN10 — Meeting frequency and cost-bundle arithmetic

- **Relationship:** N583.
- **Compared locations and document roles:** [Protocol p. 61](../../../joi190039supp1_prod.pdf#page=61) row 16 meeting/hotel linked footnote 18 versus [Protocol p. 62](../../../joi190039supp1_prod.pdf#page=62) footnote 18; both PLAN.
- **Printed inputs:** Table 980 EUR; footnote one meeting/year,4 meetings total; hotel 80 EUR and travel 80 EUR for 3 people=480 EUR; further possible 500 EUR.
- **Reproducible rule, calculation, tolerance, observation/inference:** (80+80)×3=480;480+500=980 equals table. If cost bundle applies per meeting,4×480+500=2420, gap 1440. Exact 4 meeting count and single-bundle amounts observed; per-meeting applicability explicitly conditional, not silently imposed. Rounding under±several EUR cannot explain conditional gap.
- **Source-grounded alternatives and missing definitions:** 80+80 may be aggregate across meetings, only one may require travel for 3 people, other meetings may be remote/local, or funded in other lines. Per-meeting/aggregate attendance basis absent, so no assertion all 4 incur identical costs. Concrete linked frequency plus table total motivates question.
- **Exact human question:** Do 80 EUR hotel and 80 EUR travel for 3 people apply per meeting or across all 4, and what attendance/allocation rule reconciles 980 EUR with 4 meeting description?
- **Quality-control relevance:** Conditional frequency-versus-cost-bundle label question; not an allegation of omitted actual spending.

## PN11 — Study-center incentive versus practice budget rate

- **Relationship:** N569.
- **Compared locations and document roles:** [Protocol p. 26](../../../joi190039supp1_prod.pdf#page=26) section 6.9 versus [Protocol p. 60](../../../joi190039supp1_prod.pdf#page=60) practice-related compensation row 9 and [Protocol p. 61](../../../joi190039supp1_prod.pdf#page=61) footnote 6; all PLAN.
- **Printed inputs:** Study centers 75 EUR per recruited patient, payable after colonoscopy/histology or completed study without colonoscopy within 3 months. Practice compensation 60,000 EUR; footnote 30 EUR/completed case×2000.
- **Reproducible rule, calculation, tolerance, observation/inference:** 30×2000=60000 reconciles budget; per-case rate 75 versus 30 differs 45 EUR for a recruited case meeting the narrative completion trigger. Same 2000 casesat 75→150000;2400 recruitedat 75→180000, but different eligibility bases not silently aligned. ±0.5 perrate allows±1,below 45.
- **Source-grounded alternatives and missing definitions:** 30 could be a partial component, different recipient, or older estimate. Recruited versus completed denominators differ, but recruited cases that complete also trigger 75. Row 9 includes practices wording; linked footnote doesnot clarify separate component/recipient. Identity conditional, exact amount conflict retained for human definition.
- **Exact human question:** Is 30 EUR/completed case practice compensation the same payment as 75 EUR/recruited patient study-center incentive, or a distinct component/recipient, and how should amount and payment denominator be distinguished?
- **Quality-control relevance:** Concrete unit-rate/recipient labeling question within PLAN; no claim about actual payments.

## Complete coverage and limitations

All 62 protocolpages and 10SAPpages covered, including administrative no-result units, historical data, schedules/safety units, sample quantities/handling, all 16 budgetcategory identities and footnotes, and SAPdenominator/unit definitions. Scope is disjoint from primary numeric REPORT review; no REPORT-plan comparisons emitted. No scientific coverage gap. Missing historical disease denominators, graphical ROCcoordinates, optional blood uptake/budget procurement bases, monetary locale, working-day convention, total-duration endpoints and some cost scopes remain named limitations. Missing definitions alone never generate observations: eachcard includes concrete comparedprinted values/labels and names conditional applicability. Results do not adjudicate clinical conclusions, study design, safety or finances.

# Numeric coverage-repair checks


| Relationship ID | Exact locations and roles | Printed inputs | Comparator/scope rule and reproducible check | Outcome and missing definition |
|---|---|---|---|---|
| N121 | REPORT [main p6 Discussion dose/timing](../../../jama_brenner_2019_oi_190039.pdf#page=6), mapping M085; REPORT [main p2 Interventions](../../../jama_brenner_2019_oi_190039.pdf#page=2) and [p3 Randomization](../../../jama_brenner_2019_oi_190039.pdf#page=3) | Current study uses one 300 mg aspirin dose; discussion proposes future lower 75 mg or 100 mg doses, and single or multiple tablets over days. | Match dose quantity with exposure context: 75<300 and 100<300, so both satisfy the stated lower-dose direction. Future proposals are not reported study-arm exposures; multiple future tablets do not contradict the observed single tablet. No diagnostic efficacy, event count, or duration equivalence is implied across regimens. | NUMERIC_CHECK_COMPLETE; CONTEXTUAL_PROPOSAL_RECONCILES. No supplied contradictory value. Future efficacy/safety outcomes and precise future schedule are not reported and are not needed for this label/direction check. No candidate. |
| N587 | PLAN [protocol p16 historical drug context](../../../joi190039supp1_prod.pdf#page=16), mapping A019; PLAN [protocol p1 version/date](../../../joi190039supp1_prod.pdf#page=1) | Drug marketed for >100 years/since 1899; protocol version 1.5 dated 24 July 2015. | Supplied-year arithmetic 2015−1899=116 years, greater than 100. Approximate historical age statement is coherent at protocol date; the identifier year 1899 is not a trial recruitment year, participant age, or dose. Within-year market date is absent but cannot reduce 116 calendar years below 100. No external history is used. | NUMERIC_CHECK_COMPLETE; HISTORICAL_DURATION_RECONCILES. Exact original marketing day is not supplied and not needed for the >100 bound. No candidate. |
| N588 | PLAN [protocol p26 recruitment feasibility](../../../joi190039supp1_prod.pdf#page=26), mapping A029; PLAN [protocol p14 planned sample size](../../../joi190039supp1_prod.pdf#page=14) | Earlier BliTz study 4150 participants since January 2006; ASTER planned 2400 randomized and 2000 primary-endpoint analyzed. | Match cohort identity before count comparison: 4150 belongs to the earlier feasibility cohort, while 2400/2000 are prospective ASTER populations. No same-cohort total identity applies. Historical 4150 is a participant count, not a sensitivity denominator, positive-test count, annual rate, or observed ASTER result. Source supplies no component counts with which to reconstruct 4150. | NUMERIC_CHECK_COMPLETE; DISTINCT_HISTORICAL_COHORT_WITH_NAMED_INPUT_LIMIT. Missing historical component counts/disease denominators prevent further arithmetic reconstruction, not the supplied cohort-label check. No candidate. |
| N589 | PLAN [protocol p32 dose rationale](../../../joi190039supp1_prod.pdf#page=32), mapping A040; PLAN [protocol p24 study medication](../../../joi190039supp1_prod.pdf#page=24) | Historical daily 100 mg aspirin with maximum suppression at approximately 5 days; planned study uses single 300 mg uncoated aspirin; routine loading 500 mg is separate context. | Match quantity, regimen and endpoint: 100 mg/day is a repeated historical exposure and approximately 5 days is its pharmacodynamic timing; 300 mg is one study dose, 500 mg a different loading context. No supplied same-regimen equality rule requires 100=300 or 5 days to equal the study's 2-day sampling interval. | NUMERIC_CHECK_COMPLETE; DISTINCT_HISTORICAL_REGIMEN_WITH_NAMED_INPUT_LIMIT. Exact daily schedule and original pharmacodynamic data are not supplied; no independent efficacy reconstruction or biological equivalence is asserted. No candidate. |

All four rows are complete numeric checking records and source-grounded scope checks. They are additional coverage evidence, not stable C IDs, scientific dispositions, or old-candidate recovery. Original clinical120 and PLAN86 rows remain unchanged; the coordinator owns canonical integration of this disjoint four-row repair part.

