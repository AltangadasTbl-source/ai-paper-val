# Workflow 1.6 Exact-Source Evidence Recheck

Scope: every assigned stable ID C001 through C030, separately rechecked; C029/C030 were rechecked by a distinct fresh appended-ID agent. All remain **Pending Human Adjudication**. Evidence states describe the evidence record. Suggested review dispositions below are mechanical pre-fills under QUALITY_CONTROL_SCOPE.md and are not adjudications.

Authority and method: read QUALITY_CONTROL_SCOPE.md, workflow_1_6/review_contract.md, tooling_record.md, and the current ledger. Locator records did not establish source truth. Fresh direct Poppler `pdftotext -layout` extraction of each of the four supplied PDFs was written to `preprocessing/recheck/main-layout.txt`, `protocol-layout.txt`, `sap-layout.txt`, and `results-layout.txt`. Form-feed-delimited physical pages were read separately. Direct `pdftoppm` rendering of main physical pages 7 and 8 and results-supplement physical page 2 supplied visual authority for figure colors, line styles, horizontal coordinates, and rotated Table 3 labels. Derivatives are `preprocessing/recheck/main-page7.png`, `preprocessing/recheck/main-page8.png`, and `preprocessing/recheck/results-page2.png`. Engines: Poppler pdftotext/pdftoppm 25.03.0; mawk 1.3.4 20250131 arithmetic, CPU only. Commands were `pdftotext -layout SOURCE DESTINATION`, `pdftoppm -f N -l N -singlefile -r DPI -png SOURCE PREFIX` (main p8:110 DPI; results p2:120 DPI; main p7:100 DPI), and explicit awk arithmetic expressions reproduced below. No OCR, Python package installation, external evidence, or source modification was needed. Poppler issued font-weight warnings during protocol text extraction; the necessary text remained legible, with no observed candidate-input disagreement.

Links from this artifact to a direct PDF use ../../../ because this file is in review_1_6/verification. Every page number below is the physical PDF page, not an inferred printed page.

## Recheck classification table

| ID | Primary category | Relationship type | All relationships | Compared document roles | Review domain | Evidence state | Suggested review disposition |
|---|---|---|---|---|---|---|---|
| C001 | Measure, label, or scale inconsistency | S_W | S_W | REPORT main Figure 2 legend versus caption | report_internal_inconsistency | recorded_candidate | retain |
| C002 | Measure, label, or scale inconsistency | S_W | S_W | REPORT results eFigure 1 legend versus caption | report_internal_inconsistency | recorded_candidate | retain |
| C003 | Measure, label, or scale inconsistency | S_C | S_C, S_W | REPORT main Figure 2 axis versus caption and REPORT results eFigure 1/eTable 2 | report_internal_inconsistency | recorded_candidate | retain |
| C004 | Cross-document numeric inconsistency | S_C | S_C | REPORT main Figure 1 versus REPORT results eTable 3 | report_internal_inconsistency | recorded_candidate | retain |
| C005 | Cross-document numeric inconsistency | S_C | S_C | REPORT main Figure 1 versus REPORT results eTable 2 | report_internal_inconsistency | recorded_candidate | retain |
| C006 | Cross-document numeric inconsistency | P_R | P_R | REPORT results anticipated power inputs versus PLAN protocol participating-site data | protocol_report | record_input_error | discuss |
| C007 | Measure, label, or scale inconsistency | P_P | P_P | PLAN protocol appendix versus sample-size summary | plan_material | recorded_candidate | retain |
| C008 | Measure, label, or scale inconsistency | P_P | P_P | PLAN protocol intensity definition/Table 5 versus Table 6 legend | plan_material | recorded_candidate | retain |
| C009 | Measure, label, or scale inconsistency | P_P | P_P | PLAN protocol strict threshold versus enumeration/Table 7 | plan_material | recorded_candidate | retain |
| C010 | Rate-versus-count inconsistency | P_P | P_P | PLAN protocol annual input versus historical two-year dataset | plan_material | record_input_error | discuss |
| C011 | Measure, label, or scale inconsistency | S_C | S_C | REPORT main SCDE threshold versus REPORT results definition | report_internal_inconsistency | recorded_candidate | retain |
| C012 | Measure, label, or scale inconsistency | P_R | P_R | PLAN protocol circulatory conjunction versus REPORT main/results disjunction | protocol_report | recorded_candidate | retain |
| C013 | Measure, label, or scale inconsistency | S_C | S_C, S_W | REPORT main ICU-rate wording versus main patient narrative and REPORT results patient summaries | report_internal_inconsistency | recorded_candidate | retain |
| C014 | Denominator, proportion, or total inconsistency | P_R | P_R, P_P | PLAN protocol hospital-discharge denominator versus PLAN SAP and REPORT main ICU-discharge denominator | protocol_report | recorded_candidate | retain |
| C015 | Measure, label, or scale inconsistency | P_R | P_R, P_P | PLAN SAP discharge label versus its patient aggregation and REPORT results patient denominator | protocol_report | recorded_candidate | retain |
| C016 | Measure, label, or scale inconsistency | P_R | P_R | PLAN SAP ICU-readmission Poisson shell versus REPORT main logistic OR | protocol_report | recorded_candidate | retain |
| C017 | Measure, label, or scale inconsistency | P_R | P_R, P_P | PLAN SAP hospital-readmission Poisson shell versus PLAN protocol logit and REPORT main logistic OR | protocol_report | recorded_candidate | retain |
| C018 | Denominator, proportion, or total inconsistency | P_P | P_P | PLAN historical numerator/ICU discharge denominator versus percentage | plan_material | recorded_candidate | retain |
| C019 | Denominator, proportion, or total inconsistency | P_P | P_P | PLAN historical numerator/hospital discharge denominator versus rate | plan_material | recorded_candidate | retain |
| C020 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN stat-call baseline/relative reduction versus absolute reduction | plan_material | recorded_candidate | retain |
| C021 | Measure, label, or scale inconsistency | P_P | P_P | PLAN code-blue rate reduction versus nested printed unit | plan_material | recorded_candidate | retain |
| C022 | Measure, label, or scale inconsistency | P_P | P_P | PLAN SAP exposure columns versus coefficient scale description | plan_material | recorded_candidate | retain |
| C023 | Numeric or arithmetic inconsistency | S_W | S_W | REPORT results PIM example versus supplied inverse-logit formula | statistical_results | recorded_candidate | retain |
| C024 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT main hospital total versus overnight ICU category counts | statistical_results | record_input_error | discuss |
| C025 | Measure, label, or scale inconsistency | P_P | P_P | PLAN SAP Continuous outcomes heading versus count/rate rows and taxonomy | plan_material | recorded_candidate | retain |
| C026 | Measure, label, or scale inconsistency | P_P | P_P | PLAN historical AUC endpoint versus AUC scale labeling | plan_material | recorded_candidate | retain |
| C027 | Measure, label, or scale inconsistency | S_W | S_W | REPORT main generic adjusted label versus baseline-unadjusted SCDE footnote | report_internal_inconsistency | record_input_error | discuss |
| C028 | Measure, label, or scale inconsistency | S_W | S_W | REPORT main generic adjusted label versus baseline-unadjusted physician-call footnote | report_internal_inconsistency | record_input_error | discuss |
| C029 | Measure, label, or scale inconsistency | S_C | S_C | REPORT main ICU-readmission hours label versus REPORT results calendar cutoff | report_internal_inconsistency | recorded_candidate | retain |
| C030 | Measure, label, or scale inconsistency | S_C | S_C | REPORT main hospital-readmission hours label versus REPORT results calendar cutoff | report_internal_inconsistency | recorded_candidate | retain |

Classification correction: C016 removes P_P and the purported protocol ICU-readmission logit comparator. Protocol p16's explicitly enumerated identical-logit outcomes contain **hospital** readmission, ICU mortality, and DNR mortality, but not ICU readmission. C017 retains P_P because its hospital-readmission shell directly contradicts the separately specified protocol logit model; this is an independently reproducible plan-plan comparison, rather than adding a plan merely because it corroborates the report. All other roles, categories, primary relationships, and domains are confirmed. Residual registration relationships are preserved even where an unsupported input assumption determines record_input_error.

## C001 — Main figure group encoding

- **Location found:** Yes: [main Figure 2 legend and caption, p8](../../../jama_parshuram_2018_oi_180015.pdf#page=8); visual inspection of fresh render.
- **Source value/text matched:** Legend assigns BedsidePEWS to blue-gray circles/solid line and usual care to orange circles/dashed line.
- **Comparator matched:** Caption assigns intervention hospitals to the dashed orange line and usual care to the solid blue line; slopes 0.57 and 0.53 are printed.
- **Consistency rule applicable:** Yes. A single figure's group-to-line encoding must agree between legend and explanatory caption.
- **Calculation/logical comparison reproduced:** The two group-to-color/style mappings are reversed. The plot's rightmost blue-gray point near (6.03,0.8) also matches intervention hospital C in [results eTable 2, p9](../../../joi180015supp3_prod.pdf#page=9).
- **Necessary inputs available:** Yes for the encoding comparison. Exact fitted model outputs are unavailable and unnecessary to establish the reversed descriptions.
- **Exact missing inputs/definitions:** Which encoding the authors intended for group-specific slopes; underlying fitted-line output if slope attribution is to be resolved.
- **Source-grounded alternative:** Caption descriptors may be transposed, or legend/plot descriptors may be transposed. Hospital letters/table coordinates support the plotted group encoding but do not prescribe a correction.
- **Direct observation versus inferred explanation:** Reversed printed/visual encodings are direct. A production transposition is inferred.
- **Remaining human question:** Which group-to-line assignment and slope attribution are intended?
- **Classification:** REPORT versus REPORT within main article; S_W only; category Measure, label, or scale inconsistency; report_internal_inconsistency. Results table is corroboration, not an additional discrepancy relationship. No classification ambiguity.
- **Evidence state:** recorded_candidate, determined by directly observed reversed encodings. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C002 — Supplemental figure group encoding

- **Location found:** Yes: [results eFigure 1, p2](../../../joi180015supp3_prod.pdf#page=2) visually rendered and [caption, p3](../../../joi180015supp3_prod.pdf#page=3).
- **Source value/text matched:** Legend usual care is salmon/red dotted; BedsidePEWS is turquoise dashed. H and C are turquoise; U is salmon.
- **Comparator matched:** Caption identifies A–J as BedsidePEWS and K–U as usual care, but says intervention salmon/dotted and usual care blue/dashed.
- **Consistency rule applicable:** Yes, identity of group/color/style for the same quantitative graph.
- **Calculation/logical comparison reproduced:** H (2.47,5.21) and U (2.77,3.13) match [eTable 2, p9](../../../joi180015supp3_prod.pdf#page=9) and their plotted colors; caption colors/styles reverse both legend groups.
- **Necessary inputs available:** Yes for direct encoding comparison and point confirmation.
- **Exact missing inputs/definitions:** Author-intended figure descriptors and fitted plotting code, if the mechanism is to be determined.
- **Source-grounded alternative:** Caption rather than plotted group encoding may be transposed; this does not identify a final correction.
- **Direct observation versus inferred explanation:** Source-rendered group encodings and caption words are direct; a transposition mechanism is inferred.
- **Remaining human question:** Which color/style wording is intended for each fitted group line?
- **Classification:** Both discrepant locations REPORT in the same results supplement; S_W only; Measure, label, or scale inconsistency; report_internal_inconsistency. eTable 2 only corroborates group identity. No ambiguity.
- **Evidence state:** recorded_candidate, determined by directly reversed group descriptors. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C003 — Main figure horizontal-period label

- **Location found:** Yes: [main Figure 2, p8](../../../jama_parshuram_2018_oi_180015.pdf#page=8), [results eFigure 1, p2](../../../joi180015supp3_prod.pdf#page=2), and [eTable 2 hospital C, p9](../../../joi180015supp3_prod.pdf#page=9).
- **Source value/text matched:** Main x-axis says deaths per 1000 discharges during baseline **and intervention** periods; its caption says coordinates are baseline and intervention rates.
- **Comparator matched:** Supplement x-axis says baseline period. C has baseline 4/663 (6.03), intervention 1/1250 (0.8), total discharges 1913.
- **Consistency rule applicable:** Yes: a plotted baseline rate and a combined-period rate have different denominators/time definitions.
- **Calculation/logical comparison reproduced:** 4000/663=6.03318; 5000/1913=2.61370. Both fresh-rendered plots put C near x=6.03,y=0.8, not x=2.61.
- **Necessary inputs available:** Yes for rates and visual discrimination; exact plotting coordinates not supplied as structured data, but the difference is far larger than graphical resolution.
- **Exact missing inputs/definitions:** Whether the main horizontal label intends a combined rate or simply inadvertently names both displayed periods.
- **Source-grounded alternative:** The axis may be a loose description of the two-dimensional display; the caption and supplemental baseline axis define the actual horizontal quantity.
- **Direct observation versus inferred explanation:** Axis words, table counts, and point position are direct; an extra axis phrase is an inferred production explanation.
- **Remaining human question:** What exact time basis should the main x-axis communicate?
- **Classification:** Main axis/caption produce S_W; main versus distinct REPORT results supplement produces S_C. Primary S_C by precedence; All relationships S_C, S_W; Measure, label, or scale inconsistency; report_internal_inconsistency. No role ambiguity.
- **Evidence state:** recorded_candidate, determined by incompatible literal horizontal time label and directly corroborated baseline coordinates. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C004 — Usual-care baseline patient-day minimum

- **Location found:** Yes: [main Figure 1 baseline box, p3](../../../jama_parshuram_2018_oi_180015.pdf#page=3) and [results eTable 3, p11](../../../joi180015supp3_prod.pdf#page=11).
- **Source value/text matched:** Main usual-care baseline range 6665–31575; total 162497.
- **Comparator matched:** Table baseline K–U values 10164,6655,8941,8917,11705,12126,13335,16077,14304,28698,31575; L is 6655.
- **Consistency rule applicable:** Yes, integer minimum among the same eleven usual-care hospitals/period.
- **Calculation/logical comparison reproduced:** Minimum=6655; sum=162497; printed flow minimum differs by 10. Matching total, maximum, group, and phase support alignment.
- **Necessary inputs available:** Yes, all eleven counts and total.
- **Exact missing inputs/definitions:** Which original count or extremum is intended; no missing input prevents the printed comparison.
- **Source-grounded alternative:** One hospital row or flow extremum may contain a transcription difference; a distinct 10-day definition is not disclosed.
- **Direct observation versus inferred explanation:** Values and minimum/sum arithmetic are direct/reproducible; transcription mechanism is inferred.
- **Remaining human question:** Which baseline minimum is intended, and do the two sources intentionally use different hospital-day definitions?
- **Classification:** REPORT main versus REPORT results supplement; S_C only; Cross-document numeric inconsistency; report_internal_inconsistency; no ambiguity.
- **Evidence state:** recorded_candidate, determined by reproduced 10-day extremum mismatch with matching cohort totals. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C005 — Usual-care intervention discharge maximum

- **Location found:** Yes: [main Figure 1 intervention/analysis boxes, p3](../../../jama_parshuram_2018_oi_180015.pdf#page=3) and [results eTable 2, p9](../../../joi180015supp3_prod.pdf#page=9).
- **Source value/text matched:** Main twice gives range 3672–29956 and total 94366.
- **Comparator matched:** Table K–U intervention discharges 7285,5642,3811,3672,4638,5471,6440,7327,5886,26956,17238.
- **Consistency rule applicable:** Yes, maximum among the same eleven hospitals/phase.
- **Calculation/logical comparison reproduced:** Maximum=26956; sum=94366; flow maximum exceeds table maximum by 3000. Minimum also agrees at 3672.
- **Necessary inputs available:** Yes, all site counts, group total, and period definition.
- **Exact missing inputs/definitions:** Intended source discharge maximum, if either printed count is to be changed.
- **Source-grounded alternative:** Flow extremum or T row may be transcribed differently; matching total/minimum strongly supports the registered alignment.
- **Direct observation versus inferred explanation:** Source values and extremum calculation are observed/reproduced; a typographic cause is inferred.
- **Remaining human question:** Which intervention maximum is intended, and does Figure 1 deliberately use a different site dataset?
- **Classification:** REPORT main versus REPORT results supplement; S_C only; Cross-document numeric inconsistency; report_internal_inconsistency; no ambiguity.
- **Evidence state:** recorded_candidate, determined by exact 3000-discharge maximum disagreement. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C006 — Anticipated bed inputs and unsupported common-basis assumption

- **Location found:** Yes: [results eTable 5, p14](../../../joi180015supp3_prod.pdf#page=14), [protocol sample-size section, p14](../../../joi180015supp1_prod.pdf#page=14), and [power appendix, p29](../../../joi180015supp1_prod.pdf#page=29).
- **Source value/text matched:** Results anticipated 20 hospitals/2397 ward beds, 99389 discharges/397556 days; caption explicitly tabulates power assumptions including constant cluster size.
- **Comparator matched:** Protocol p14 says available participating-hospital data indicate 2322 beds and the same 99389 admissions/397556 days. Appendix sets n=20 and average bed size 119.85.
- **Consistency rule applicable:** Conditional only. Equality would apply if the bed rows represented the same participating-site census, but the report explicitly frames its column as power assumptions.
- **Calculation/logical comparison reproduced:** 2397−2322=75; 20×119.85=2397 exactly. These are different numbers with a supplied alternative basis, not a reproduced common-basis bed discrepancy.
- **Necessary inputs available:** Yes for both printed numbers and power-derived 2397; no for establishing identical bed-population/basis.
- **Exact missing inputs/definitions:** Whether the report's anticipated bed row is an actual census or constant-cluster power input; source mapping of each anticipated row.
- **Source-grounded alternative:** 2397 is the constant-cluster power total derived directly from the protocol appendix, while 2322 is the available participating-site count. Shared admissions/day inputs do not make every row a census.
- **Direct observation versus inferred explanation:** Printed counts and exact power product are direct/reproduced; equating their bed basis is an unsupported registered assumption.
- **Remaining human question:** Does the anticipated bed row intend the constant-cluster power total, and should its basis be explicitly distinguished from the available-site census?
- **Classification:** REPORT results versus PLAN protocol by content; residual comparison P_R only; Cross-document numeric inconsistency; protocol_report. Ambiguity is common basis, not roles. The appendix corroborates a supported power basis and creates no separate P_P discrepancy.
- **Evidence state:** record_input_error, determined by unsupported bed-row alignment and exact source-supported alternative power total. Whether any residual labeling discrepancy exists remains unsettled. **Suggested review disposition:** discuss. **Human status:** Pending Human Adjudication.

## C007 — Mortality absolute-reduction scale

- **Location found:** Yes: [protocol p29 appendix](../../../joi180015supp1_prod.pdf#page=29), [p14 sample size](../../../joi180015supp1_prod.pdf#page=14), and [p1 summary](../../../joi180015supp1_prod.pdf#page=1).
- **Source value/text matched:** Appendix says 18% relative reduction corresponds to absolute risk reduction 0.9%; baseline 5.1/1000; more precise RRR 0.178 also printed.
- **Comparator matched:** p14 says 18% relative and absolute 0.09%; p1 says 0.9 deaths/1000.
- **Consistency rule applicable:** Yes, matched mortality power scenario and percent/per-thousand conversion.
- **Calculation/logical comparison reproduced:** 5.1×0.18=0.918 deaths/1000=0.0918%; 0.9/1000=0.09%; 0.9%=9/1000. RRR0.178 gives0.9078/1000 and does not rescue the percentage.
- **Necessary inputs available:** Yes for arithmetic and unit comparison; no original power execution needed.
- **Exact missing inputs/definitions:** Whether an unreported alternative scenario generated the appendix percentage.
- **Source-grounded alternative:** Decimal/unit transcription or another baseline; no alternative baseline matching this 18% scenario is supplied.
- **Direct observation versus inferred explanation:** Printed percentage disagreement and conversion are direct/reproduced; a decimal transcription is inferred.
- **Remaining human question:** Which absolute percentage belongs to this mortality power scenario?
- **Classification:** All conflicting locations PLAN; P_P only; Measure, label, or scale inconsistency; plan_material. [Main p4](../../../jama_parshuram_2018_oi_180015.pdf#page=4) supports 0.9/1000 only and adds no discrepancy relationship.
- **Evidence state:** recorded_candidate, determined by tenfold percentage scale difference. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C008 — Cardiac-arrest intensity codes

- **Location found:** Yes: [protocol p11 clinical definition](../../../joi180015supp1_prod.pdf#page=11), [Table 5 p24](../../../joi180015supp1_prod.pdf#page=24), and [Table 6 legend p27](../../../joi180015supp1_prod.pdf#page=27).
- **Source value/text matched:** Definition rates cardiac arrests 6 or 7 on the Children's Resuscitation Intensity Scale.
- **Comparator matched:** Table 6 legend names cardiac arrest scale rating 4 or 5. Table 5 assigns 4 to circulatory support, 5 to respiratory/circulatory support, 6 to chest compressions/ECMO, 7 to death.
- **Consistency rule applicable:** Yes, discrete codes on the same named endpoint intensity scale.
- **Calculation/logical comparison reproduced:** {4,5} differs from {6,7}; their treatment definitions are visibly different. No rounding applies.
- **Necessary inputs available:** Yes for code mapping. Event-level coding is unavailable and not needed for the printed comparison.
- **Exact missing inputs/definitions:** Whether Table 6 refers to an undisclosed prior intensity scale; the actual review-form code version.
- **Source-grounded alternative:** A stale legend or alternate unlabelled scale may explain it; no such scale is supplied in the bound plan.
- **Direct observation versus inferred explanation:** Codes/definitions are direct; a stale legend is inferred.
- **Remaining human question:** Which intensity codes were intended to trigger the Table 6 cardiac-arrest abstraction?
- **Classification:** PLAN throughout; P_P only; Measure, label, or scale inconsistency; plan_material. No role ambiguity; alternate-scale ambiguity remains named.
- **Evidence state:** recorded_candidate, determined by inconsistent endpoint-to-code assignment. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C009 — Preventability threshold boundary

- **Location found:** Yes: [protocol p11](../../../joi180015supp1_prod.pdf#page=11) and [Table 7 p28](../../../joi180015supp1_prod.pdf#page=28).
- **Source value/text matched:** p11 says consensus rating “at >4.”
- **Comparator matched:** The immediately following sentence expressly includes ratings 4,5,6; Table 7 legend says a rating of 4 or more.
- **Consistency rule applicable:** Yes, membership at integer boundary 4 on the same six-point scale.
- **Calculation/logical comparison reproduced:** >4 selects {5,6}; 4 or more selects {4,5,6}. Rating 4 fails the first and satisfies the second.
- **Necessary inputs available:** Yes for boundary comparison; no event ratings to quantify its consequences.
- **Exact missing inputs/definitions:** Applied operational cutoff and number of events rated 4; neither is inferred from 21/27 or 29/32.
- **Source-grounded alternative:** A strict-symbol typo rather than a different analysis threshold; no correction assigned.
- **Direct observation versus inferred explanation:** Conflicting membership definitions are direct; possible typographic cause is inferred.
- **Remaining human question:** Was rating 4 included in the applied preventability dichotomy?
- **Classification:** PLAN/PLAN, P_P only; Measure, label, or scale inconsistency; plan_material. [Results p6](../../../joi180015supp3_prod.pdf#page=6) and [main p7](../../../jama_parshuram_2018_oi_180015.pdf#page=7) corroborate inclusion of 4 and do not create extra P_R discrepancy relationships.
- **Evidence state:** recorded_candidate, determined by reproduced boundary contradiction. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C010 — Annual versus two-year historical admissions

- **Location found:** Yes: [protocol p14](../../../joi180015supp1_prod.pdf#page=14) and [historical appendix p30](../../../joi180015supp1_prod.pdf#page=30).
- **Source value/text matched:** p14 describes 1052 urgent ICU admissions/year from four Ontario pediatric hospitals, without identifying a year or dataset period.
- **Comparator matched:** p30 explicitly describes 1052 admissions in two years following 31 January 2007 from the four largest Ontario pediatric referral hospitals, alongside 55963 discharges and 150 code-blue events.
- **Consistency rule applicable:** Only if the counts represent the same historical cohort. Count/year and two-year count cannot otherwise be equated solely by numerical identity.
- **Calculation/logical comparison reproduced:** For the p30 cohort, 1052/2=526/year; labeling that aggregate 1052/year would double annualization. The calculation is conditional; it does not establish p14's cohort identity.
- **Necessary inputs available:** Yes for p30's annualized count; no definitive identification of p14's historical series/year.
- **Exact missing inputs/definitions:** The reference period/source dataset for p14 and whether it is the p30 2007–2008 aggregate.
- **Source-grounded alternative:** The same four centers could supply another annual series or estimate of 1052; p14 does not give the dates that would exclude this.
- **Direct observation versus inferred explanation:** Printed periods/counts are direct. Registering a same-cohort annualization contradiction assumes an alignment not established by the supplied text.
- **Remaining human question:** Are both occurrences 1052 drawn from the same two-year dataset, or is p14 a separate annual cohort/estimate?
- **Classification:** Historical material remains PLAN by content; P_P only; Rate-versus-count inconsistency; plan_material. Ambiguity is matching historical periods, not source roles.
- **Evidence state:** record_input_error, determined by unsupported historical-series alignment. Exact dates of p14 remain missing, so a residual discrepancy cannot be settled. **Suggested review disposition:** discuss. **Human status:** Pending Human Adjudication.

## C011 — Fluid-resuscitation threshold

- **Location found:** Yes: [main Study Outcomes p4](../../../jama_parshuram_2018_oi_180015.pdf#page=4) and [results eTable 1 p6](../../../joi180015supp3_prod.pdf#page=6).
- **Source value/text matched:** Main lists fluid boluses of 60 mL/kg or greater within the 12 hours before ICU admission.
- **Comparator matched:** Results definition gives >60 mL/kg in the 12 hours before transfer.
- **Consistency rule applicable:** Yes, strict versus inclusive numerical threshold for the matched SCDE component.
- **Calculation/logical comparison reproduced:** Exactly 60 mL/kg with no other qualifying component satisfies ≥60 but fails >60.
- **Necessary inputs available:** Yes for threshold logic; boundary-patient data are absent.
- **Exact missing inputs/definitions:** Operational fluid threshold/tolerance and counts of events exactly 60 without another qualifying component.
- **Source-grounded alternative:** Threshold wording/symbol may be inexact, or measurement tolerance may govern classification. Neither resolves printed inclusion/exclusion.
- **Direct observation versus inferred explanation:** Printed threshold difference is direct; changes in SCDE event totals are not established.
- **Remaining human question:** Which threshold governed event classification at exactly 60 mL/kg?
- **Classification:** REPORT main versus REPORT results supplement; S_C only; Measure, label, or scale inconsistency; report_internal_inconsistency. [Protocol Table 5 p24](../../../joi180015supp1_prod.pdf#page=24) only corroborates the strict boundary and adds no P_R relationship.
- **Evidence state:** recorded_candidate, determined by reproduced boundary membership difference. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C012 — Circulatory component conjunction

- **Location found:** Yes: [protocol Table 5 p24](../../../joi180015supp1_prod.pdf#page=24), [main p4](../../../jama_parshuram_2018_oi_180015.pdf#page=4), and [results eTable 1 p6](../../../joi180015supp3_prod.pdf#page=6).
- **Source value/text matched:** Protocol level 4 requires >60 mL/kg fluid and administration of inotrope/vasopressor; it is SCDE Yes.
- **Comparator matched:** Results says >60 fluid and/or inotrope/vasopressor; main composite of one or more components separately lists vasoactive medication or qualifying fluid boluses.
- **Consistency rule applicable:** Yes, AND versus OR for the matched circulatory component, independent of C011's numerical boundary.
- **Calculation/logical comparison reproduced:** Fluid-only or vasoactive-only without another component satisfies report disjunction and fails protocol conjunction.
- **Necessary inputs available:** Yes for logical comparison, no event-level treatment patterns or amendment history.
- **Exact missing inputs/definitions:** Final operational conjunction, a documented change if any, and affected treatment combinations.
- **Source-grounded alternative:** Definition amended or plan conjunction imprecise; no supplied amendment resolves which explanation applies.
- **Direct observation versus inferred explanation:** Different Boolean definitions are direct; amendment mechanism and count effect are unestablished.
- **Remaining human question:** Which circulatory rule was applied, and does the textual difference reflect an amendment or description error?
- **Classification:** PLAN versus REPORT main/results; P_R only; Measure, label, or scale inconsistency; protocol_report. Main and results agree on disjunction, so no additional S_C. No role ambiguity.
- **Evidence state:** recorded_candidate, determined by reproduced logical membership difference. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C013 — ICU rate wording versus patient duration summaries

- **Location found:** Yes: [main Data Analyses p4](../../../jama_parshuram_2018_oi_180015.pdf#page=4), [main patient narrative p6](../../../jama_parshuram_2018_oi_180015.pdf#page=6), [results eTable 4 p12](../../../joi180015supp3_prod.pdf#page=12), and [footnotes p13](../../../joi180015supp3_prod.pdf#page=13).
- **Source value/text matched:** Main says patient outcomes are expressed per 1000 patient-days in ICU (ICU outcomes).
- **Comparator matched:** eTable 4 is expressly per-patient; 686/967 patients, total-LOS means 9.4/9 days, ventilator-free means 23.9/24 days, MV means 4.1/3.7 days; footnotes define per-patient totals/means and continuous mean differences. Main p6 explicitly describes 1653 patients remaining in ICU for 15212 days.
- **Consistency rule applicable:** Yes, the literal blanket rate denominator has dimensions different from day totals/means per patient. Its intended scope is conditional.
- **Calculation/logical comparison reproduced:** Mean duration=sum of patient durations/number of patients, measured in days; it is not events per 1000 ICU patient-days. The table's Gaussian mean differences 1.28,0.26,0.69 are dimensionally day differences.
- **Necessary inputs available:** Yes for outcome dimensions and patient summary definitions; raw patient durations are unnecessary for this label comparison.
- **Exact missing inputs/definitions:** Which subset of ICU outcomes the main per-1000-day statement intends to describe.
- **Source-grounded alternative:** Main statement may apply only to selected event outcomes, with patient resource summaries exempt; that scope is not explicitly qualified locally.
- **Direct observation versus inferred explanation:** General denominator statement and patient-summary dimensions are direct; an intended scope restriction is inferred.
- **Remaining human question:** Precisely which ICU outcomes should carry the per-1000-ICU-day label, and which are patient duration means?
- **Classification:** REPORT main/internal patient narrative produces S_W; main versus REPORT results supplement produces S_C; primary S_C; All relationships S_C, S_W; Measure, label, or scale inconsistency; report_internal_inconsistency. [SAP p7](../../../joi180015supp2_prod.pdf#page=7) corroborates per-patient aggregation only and adds no P_R. Scope ambiguity recorded.
- **Evidence state:** recorded_candidate, determined by literal denominator/dimension mismatch pending named scope definition. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C014 — ICU-readmission denominator

- **Location found:** Yes: [protocol p12](../../../joi180015supp1_prod.pdf#page=12), [SAP shell p5](../../../joi180015supp2_prod.pdf#page=5), and [main Table 3 p7](../../../jama_parshuram_2018_oi_180015.pdf#page=7), visually checked.
- **Source value/text matched:** Protocol says PICU mortality and unplanned re-admission (hospital,PICU) per thousand hospital discharges.
- **Comparator matched:** SAP ICU-readmission row denominator PatientDischargesICU. Main ICU readmission <48h: 94(28.40)/108(21.25), rates per 1000 ICU discharges in footnote h; hospital discharges 50173/94366.
- **Consistency rule applicable:** Yes, explicit hospital-discharge versus ICU-discharge units for the same ICU-readmission endpoint.
- **Calculation/logical comparison reproduced:** Hospital denominators would give 94000/50173=1.87352 and108000/94366=1.14448, rather than28.40 and21.25. No hospital-to-ICU denominator substitution is justified.
- **Necessary inputs available:** Yes for printed unit contrast and diagnostic hospital rates; unrounded ICU-rate reconstruction is not needed.
- **Exact missing inputs/definitions:** Documented final denominator revision and any populations excluded from the stated ICU-discharge denominator.
- **Source-grounded alternative:** Later SAP revises an overgeneralized protocol statement; the report and SAP agree. This is not evidence of a protocol violation.
- **Direct observation versus inferred explanation:** Opposing denominator labels are direct; historical change mechanism is inferred.
- **Remaining human question:** What original/final ICU-readmission denominator was intended, and is its change documented?
- **Classification:** PLAN protocol versus REPORT main establishes P_R; PLAN protocol versus PLAN SAP is independently conflicting P_P. Primary P_R; All relationships P_R, P_P; Denominator, proportion, or total inconsistency; protocol_report. Roles confirmed; no extra S_W.
- **Evidence state:** recorded_candidate, determined by directly different endpoint denominator definitions. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C015 — Predicted-mortality patient/discharge label

- **Location found:** Yes: [SAP ICU analysis p7](../../../joi180015supp2_prod.pdf#page=7), [results eTable 4 p12](../../../joi180015supp3_prod.pdf#page=12), [prediction footnote p13](../../../joi180015supp3_prod.pdf#page=13), and [main admission-event row p7](../../../jama_parshuram_2018_oi_180015.pdf#page=7).
- **Source value/text matched:** SAP label “PIM II Prediction Mortality (/1000 urgent ICU discharges)” accompanies average probability across admissions and an explicit one-record-per-patient analysis.
- **Comparator matched:** Results footnote sums each patient's inverse-logit and presents predicted numbers rounded to integer, percentages of total patients. Table post predicted38(5.5%)/44(4.6%), with686/967 patients. Main urgent admission events828/1178.
- **Consistency rule applicable:** Yes: averaging within patient then across patients defines a patient probability, not a per-urgent-ICU-discharge rate when patients may have multiple admissions. Percent versus per1000 conversion alone cannot change the population unit.
- **Calculation/logical comparison reproduced:** Rounded-count diagnostics38/686×100=5.53936% and44/967×100=4.55016%, compatible with printed patient percentages. Admission-event diagnostics38/828×1000=45.89372 and44/1178×1000=37.35144 differ from approximately55/46 per1000 patients; these event counts are not asserted to equal every eligible urgent discharge count.
- **Necessary inputs available:** Yes for denominator definitions and dimensional comparison; no underlying probability sums or precise urgent-discharge subset.
- **Exact missing inputs/definitions:** Intended SAP row denominator, final unrounded predicted sums, and urgent-discharge population if a separate discharge analysis was intended.
- **Source-grounded alternative:** SAP row may retain an admission/discharge label while its implemented aggregation and report use patient predictions; an undisclosed separate discharge quantity may exist.
- **Direct observation versus inferred explanation:** Opposing denominator labels and patient aggregation are direct; the printed-count ratios are diagnostics because the prediction counts are rounded. No inferential mean difference is reconstructed.
- **Remaining human question:** Is this outcome a patient probability/percentage, or was a distinct discharge-based prediction intended in the SAP label?
- **Classification:** PLAN SAP internally conflicts (P_P); PLAN SAP discharge label versus REPORT results patient definition conflicts (P_R). Primary P_R; All relationships P_R, P_P; Measure, label, or scale inconsistency; protocol_report. Repeat-admission handling limits exact rate reconstruction, not role assignment.
- **Evidence state:** recorded_candidate, determined by source-defined patient aggregation opposing the discharge row label. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C016 — ICU-readmission Poisson versus logistic label

- **Location found:** Yes: [SAP shell p5](../../../joi180015supp2_prod.pdf#page=5), [main Table 3/footnote d p7](../../../jama_parshuram_2018_oi_180015.pdf#page=7), and [protocol analysis p16](../../../joi180015supp1_prod.pdf#page=16).
- **Source value/text matched:** SAP Unplanned ICU Readmissions uses ICU-discharge denominators and “Poisson.” SAP pp1–3 define binomial logit versus Poisson log-rate model families.
- **Comparator matched:** Main ICU readmission<48h gives OR1.11(0.77–1.61), P=.58; footnote d explicitly names logistic regression. The registered claim that protocol p16 specifies an identical logit model for ICU readmission is **not matched**: that list does not contain ICU readmission.
- **Consistency rule applicable:** Yes to the SAP/report named model/measure identity. No to a nonexistent protocol ICU-readmission model comparator.
- **Calculation/logical comparison reproduced:** Poisson shell label and logistic OR label differ for the matched ICU-readmission endpoint. A Poisson log-rate model produces a rate-ratio scale and a logistic model an odds-ratio scale; no aggregate-count conversion is performed.
- **Necessary inputs available:** Yes for SAP/report printed labels and source-defined family distinctions. Final production code, outputs, and explicit shell-row link are absent.
- **Exact missing inputs/definitions:** Whether the SAP shell is generic/outdated, a distinct intended analysis, or a subsequently revised model specification.
- **Source-grounded alternative:** Shell uses Poisson generically despite the SAP's separate binomial section, or the final model was revised. The protocol cannot corroborate this row's logit specification because its list omits ICU readmission.
- **Direct observation versus inferred explanation:** Model names and OR are direct; production-model change or shell obsolescence is inferred. The unsupported protocol comparison is a discovered registration input error within provenance, while the independent SAP/report mismatch remains.
- **Remaining human question:** Which model specification generated the reported ICU-readmission OR, and how should the SAP Poisson shell row be interpreted?
- **Classification:** PLAN SAP versus REPORT main; primary P_R; All relationships **P_R only**; Measure, label, or scale inconsistency; protocol_report. Correction: remove P_P because the registered protocol ICU-readmission logit statement is absent. Preserve that assertion in historical discovery provenance, explicitly removed from the final comparison; no stable ID is deleted. Roles themselves are confirmed.
- **Evidence state:** recorded_candidate, determined by surviving direct SAP/report model-label comparison after removal of unsupported corroboration. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C017 — Hospital-readmission Poisson versus logistic label

- **Location found:** Yes: [SAP shell p5](../../../joi180015supp2_prod.pdf#page=5), [main Table 3/footnote d p7](../../../jama_parshuram_2018_oi_180015.pdf#page=7), and [protocol p16](../../../joi180015supp1_prod.pdf#page=16).
- **Source value/text matched:** SAP Unplanned Hospital Readmission uses hospital-discharge denominators and Poisson.
- **Comparator matched:** Main hospital readmission<48h gives OR0.93(0.61–1.41), P=.74 and logistic-regression footnote. Protocol explicitly lists unplanned hospital re-admission within48h among outcomes analyzed with an identical logit model.
- **Consistency rule applicable:** Yes, same endpoint/discharge denominator with differing named model families and measure labels.
- **Calculation/logical comparison reproduced:** Poisson shell versus report logistic OR and separately versus protocol logit are two independently checkable label comparisons. No OR-to-rate-ratio conversion attempted.
- **Necessary inputs available:** Yes for both comparisons; final execution code and explicit shell-row link absent.
- **Exact missing inputs/definitions:** Whether shell Poisson label denotes a separate planned analysis, a generic placeholder, or a revision.
- **Source-grounded alternative:** Generic/stale shell table or changed final specification; other SAP binomial pages and original protocol support logistic, but do not identify the production history.
- **Direct observation versus inferred explanation:** Model labels are direct; shell revision mechanism inferred.
- **Remaining human question:** How should the planned shell Poisson row be reconciled with the protocol logit specification and reported logistic OR?
- **Classification:** P_R between PLAN SAP and REPORT main; P_P between PLAN SAP and PLAN protocol independently conflicting labels. Primary P_R; All relationships P_R, P_P; Measure, label, or scale inconsistency; protocol_report. P_P retained because its exact hospital-readmission comparison exists, unlike C016. The protocol also corroborates the report; corroboration alone was not used to add P_P.
- **Evidence state:** recorded_candidate, determined by reproducible same-endpoint model-label differences. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C018 — Historical ICU-admission percentage

- **Location found:** Yes: [protocol historical table p30](../../../joi180015supp1_prod.pdf#page=30).
- **Source value/text matched:** Unplanned PICU admits1052; PICU discharges7300.
- **Comparator matched:** Printed14.5% per PICU discharges.
- **Consistency rule applicable:** Yes, table's directly identified numerator/denominator percentage; rounding comparison is conditional on displayed counts being the exact inputs.
- **Calculation/logical comparison reproduced:** 100×1052/7300=14.4109589%, which rounds to14.4% to one decimal;14.5% differs by0.0890411 percentage points, exceeding ordinary nearest-rounding tolerance0.05.
- **Necessary inputs available:** Yes for displayed arithmetic. It is not stated whether7300 is a rounded historical aggregate.
- **Exact missing inputs/definitions:** Whether7300 is exact, a different eligible ICU-discharge denominator, and historical percentage rounding rule.
- **Source-grounded alternative:** Historical denominator may be rounded or subset-adjusted. For numerator1052, a14.5%-rounded result would require denominator approximately7230–7280, rather than exact7300.
- **Direct observation versus inferred explanation:** Counts and percentage are direct; arithmetic is reproduced; different denominator production is inferred.
- **Remaining human question:** Which exact denominator and rounding rule produced14.5%?
- **Classification:** PLAN historical material throughout; P_P only; Denominator, proportion, or total inconsistency; plan_material. No report relationship. Exactness ambiguity named.
- **Evidence state:** recorded_candidate, determined by nonreconciliation of directly labeled printed inputs under ordinary nearest rounding, pending named historical-input definition. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C019 — Historical admissions per hospital discharges

- **Location found:** Yes: [protocol historical table/narrative p30](../../../joi180015supp1_prod.pdf#page=30).
- **Source value/text matched:**1052 unplanned PICU admissions; table Hospital Admissions55963 and narrative explicitly55963 Hospital Discharges for the two-year period.
- **Comparator matched:**18 per1000 Hospital Discharges.
- **Consistency rule applicable:** Yes for table/narrative same-period count/denominator; integer-rate rounding convention remains unspecified.
- **Calculation/logical comparison reproduced:**1000×1052/55963=18.7981345; nearest integer is19, not18. Difference0.7981345 exceeds0.5 nearest-rounding tolerance.
- **Necessary inputs available:** Yes for displayed fraction; no percentage/rate formatting policy.
- **Exact missing inputs/definitions:** Intentional truncation versus nearest rounding, or an alternative eligible discharge denominator.
- **Source-grounded alternative:** Truncating18.798 to an integer gives18 exactly. Other table rates can round ordinarily (150/55963×1000=2.68 shown3), so one consistent truncation rule is not established.
- **Direct observation versus inferred explanation:** Counts/rate are direct; nearest-rounding calculation is diagnostic, not an asserted source formatting policy.
- **Remaining human question:** Was18 deliberately truncated, or does its source numerator/denominator differ from the displayed two-year counts?
- **Classification:** PLAN historical material, P_P only; Denominator, proportion, or total inconsistency; plan_material. Conditional formatting ambiguity remains named.
- **Evidence state:** recorded_candidate, determined by registered conditional nearest-rounding discrepancy reproduced with explicit truncation alternative. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C020 — Stat-call absolute reduction arithmetic

- **Location found:** Yes: [protocol p30 Stat Calls paragraph](../../../joi180015supp1_prod.pdf#page=30).
- **Source value/text matched:** Baseline8.13 stat calls/1000 patient-days; relative reduction0.181; Poisson regression named.
- **Comparator matched:** Absolute reduction1.45 calls/1000 patient-days in the same paragraph.
- **Consistency rule applicable:** Yes, absolute reduction=baseline rate×relative reduction for the same endpoint and rate scale.
- **Calculation/logical comparison reproduced:**8.13×0.181=1.47153. Printed-precision intervals8.125–8.135 and0.1805–0.1815 yield products1.4665625–1.4765025;1.45's nearest-rounding interval1.445–1.455 does not overlap.
- **Necessary inputs available:** Yes for arithmetic; original power outputs not supplied and not reconstructed.
- **Exact missing inputs/definitions:** Any alternate unprinted baseline/power scenario or conversion used for1.45.
- **Source-grounded alternative:** Absolute reduction may refer to another scenario; required relative reduction1.45/8.13≈0.17835 differs from0.181 beyond its printed rounding precision.
- **Direct observation versus inferred explanation:** Three printed inputs and multiplication are direct/reproduced; a power-scenario mismatch is inferred.
- **Remaining human question:** Do all three printed quantities use the same baseline and scenario, and what explains the nonoverlapping arithmetic?
- **Classification:** PLAN internal; P_P only; Numeric or arithmetic inconsistency; plan_material; no role ambiguity.
- **Evidence state:** recorded_candidate, determined by reproduced product disagreement beyond printed rounding tolerance. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C021 — Code-blue nested denominator wording

- **Location found:** Yes: [protocol p30 Code Blue paragraph](../../../joi180015supp1_prod.pdf#page=30).
- **Source value/text matched:** Baseline0.75/1000 patient-days and relative reduction0.41.
- **Comparator matched:** Absolute reduction “0.3/1000 events per thousand patient days.”
- **Consistency rule applicable:** Yes for dimensional unit wording; numerical0.3 alone is coherent.
- **Calculation/logical comparison reproduced:**0.75×0.41=0.3075 events/1000days, which rounds0.3. Reading both printed divisors literally gives0.0003 events/1000days, a further factor1000.
- **Necessary inputs available:** Yes for arithmetic/unit reading; no need for power recalculation.
- **Exact missing inputs/definitions:** Whether /1000 is an intentionally redundant unit cue rather than an additional division.
- **Source-grounded alternative:** Conventional redundant unit phrasing may intend one per-thousand denominator; then the numeric reduction is coherent.
- **Direct observation versus inferred explanation:** Both unit cues are direct; applying an additional divisor is a literal dimensional reading, not evidence the analysts actually used that divisor.
- **Remaining human question:** What single event/person-time unit is intended by this phrase?
- **Classification:** PLAN internal, P_P only; Measure, label, or scale inconsistency; plan_material. Unit-phrase interpretation ambiguity explicitly preserved.
- **Evidence state:** recorded_candidate, determined by the reproduced nested-unit labeling question; no erroneous power implementation is inferred. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C022 — Identity-Poisson coefficient exposure scale

- **Location found:** Yes: [SAP code/comments p3 lines114–131](../../../joi180015supp2_prod.pdf#page=3).
- **Source value/text matched:** Comment names Nlin coefficient usual-care intercept and NlinG coefficient rate difference. Code defines Nlin=N/1000; GNlin=N×(Group==BedsidePEWS); BNlin=N×Baseline; model x~Nlin+GNlin+BNlin−1 with Poisson identity.
- **Comparator matched:** Exposure columns scale intercept by N/1000 but treatment by N. NlinG/GNlin name reversal and EPOCH$$BNlin syntax are printed but are not registered as independent syntax candidates.
- **Consistency rule applicable:** Yes as a symbolic dimensional check. Any interpretation of intercept and difference on one per1000-day rate scale requires a conversion because the printed columns scale them differently.
- **Calculation/logical comparison reproduced:** Let coefficients be α,β,γ: expected x=Nα/1000+NIβ+NBγ. Dividing by N/1000 gives rate per1000days=α+1000Iβ+1000Bγ. The treatment coefficient β is per-day difference, requiring1000β for per1000days; α is per1000days.
- **Necessary inputs available:** Yes for exact symbolic column scaling; actual fitted coefficients, run code, and post-fit conversions unavailable.
- **Exact missing inputs/definitions:** Unit intended by the generic “rate difference” comment and any production column scaling/coefficient rescaling.
- **Source-grounded alternative:** The comment may intend β in per-day units and a later1000 conversion, or draft code may differ from implementation. The source does not explicitly state that every coefficient is already per1000days.
- **Direct observation versus inferred explanation:** Unequal exposure scalings and exact conversion factor are direct/reproduced. Treating the comment as an already-per1000 rate difference is conditional, and no fitted reported number is alleged to have the wrong scale.
- **Remaining human question:** What units govern the Nlin/GNlin coefficients, and was the treatment coefficient multiplied by1000 before reporting per1000-day differences?
- **Classification:** PLAN SAP code versus PLAN SAP explanatory comments; P_P only; Measure, label, or scale inconsistency; plan_material. Generic coefficient-unit ambiguity remains named; no additional report discrepancy asserted.
- **Evidence state:** recorded_candidate, determined by reproduced unequal coefficient scales with the registered conditional reporting-scale question pending the named conversion definition. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C023 — PIM upper-example display probability

- **Location found:** Yes: [results eTable 1 p7](../../../joi180015supp3_prod.pdf#page=7) and [eTable 4 footnotes b/c p13](../../../joi180015supp3_prod.pdf#page=13).
- **Source value/text matched:** PIM score+9.7778 gives printed predicted mortality99.9%; PaO2=40 and BE=−35. The minus sign on p13 wraps at the line end; p7 also explicitly reads−35, so no sign discrepancy exists.
- **Comparator matched:** Footnote b supplies inverse-logit1/(1+exp(−PIM)); minimum−8.4137 is shown as0.02%.
- **Consistency rule applicable:** Yes for formula/example consistency; nearest-decimal display rule is a conditional diagnostic because the source only expressly specifies nearest-integer rounding for predicted counts, not the upper example percentage.
- **Calculation/logical comparison reproduced:**100/(1+exp(−9.7778))=99.9943306823%. Nearest0.1 percentage point is100.0%, not99.9%; difference0.0943307 exceeds0.05. Lower example gives approximately0.02218%, coherent at0.02%. Score±0.00005 has negligible impact on the upper diagnostic.
- **Necessary inputs available:** Yes for score/formula; full scoring coefficients are unnecessary because the given score is the input.
- **Exact missing inputs/definitions:** Percentage truncation/capping rule, especially whether99.9% is an intentional upper display cap.
- **Source-grounded alternative:** Truncation to one decimal or a99.9% cap yields the printed value and avoids display100%; neither policy is stated. No interpretation of100% as actual certainty is imposed.
- **Direct observation versus inferred explanation:** Score, formula, and printed percentage are direct; nearest rounding is a conditional diagnostic, and a display cap is a possible explanation.
- **Remaining human question:** Is99.9% an intentional truncation/cap, or should the example follow another documented percentage display rule?
- **Classification:** REPORT within one results supplement; S_W only; Numeric or arithmetic inconsistency; statistical_results. Display-policy ambiguity explicitly preserved.
- **Evidence state:** recorded_candidate, determined by reproduced registered conditional formula/nearest-rounding discrepancy pending the named display rule. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C024 — Overnight ICU categories and unsupported exhaustiveness

- **Location found:** Yes: [main Table 1 p5](../../../jama_parshuram_2018_oi_180015.pdf#page=5).
- **Source value/text matched:** BedsidePEWS10 hospitals; most senior ICU physician in-house overnight: staff2(20%), fellow5(50%), resident1(10%).
- **Comparator matched:** Usual-care counts1+3+7=11. Eligibility footnote says all had pediatric ICU staff; continuous-in-house wording in footnote d is attached to the **ward** physician row, not a claim that each ICU has an in-house overnight physician.
- **Consistency rule applicable:** Sum-to10 is conditional on exhaustive overnight ICU categories and every hospital having an in-house overnight ICU physician. Neither is stated by the source.
- **Calculation/logical comparison reproduced:**2+5+1=8;20+50+10=80%. The two-hospital residual is reproduced as coverage of displayed categories, but not as an established denominator contradiction. Individual percentages correctly use10.
- **Necessary inputs available:** Yes for displayed counts/percentages; no category exhaustiveness or missing/no-in-house status for two hospitals.
- **Exact missing inputs/definitions:** Whether all hospitals had a most-senior in-house overnight ICU physician; categories for absence, other staffing, or missing data.
- **Source-grounded alternative:** Two hospitals may have no ICU physician in-house overnight, another category, or missing information. Having ICU staff physicians generally does not require in-house overnight presence.
- **Direct observation versus inferred explanation:** Displayed categories cover8/10 directly. Treating this as an exhaustive-category contradiction is an unsupported registration assumption; no staffing defect is inferred.
- **Remaining human question:** What overnight ICU presence/category or missing-data status describes the remaining two hospitals, and was the displayed list intended to be exhaustive?
- **Classification:** REPORT within main Table 1; S_W only; Denominator, proportion, or total inconsistency; statistical_results. Registered residual classification preserved; ambiguity is exhaustiveness, not roles.
- **Evidence state:** record_input_error, determined by unsupported category-exhaustiveness/presence assumption. The residual reporting-completeness question cannot be settled from this table. **Suggested review disposition:** discuss. **Human status:** Pending Human Adjudication.

## C025 — Continuous-outcomes shell heading

- **Location found:** Yes: [SAP Shell Tables p5](../../../joi180015supp2_prod.pdf#page=5), [binary/count taxonomy p1](../../../joi180015supp2_prod.pdf#page=1), [Poisson count definition p2](../../../joi180015supp2_prod.pdf#page=2), and [Gaussian individual outcomes pp3–4](../../../joi180015supp2_prod.pdf#page=3).
- **Source value/text matched:** Shell heading Continuous outcomes precedes resuscitation calls, stat calls, urgent ICU consultations, urgent ICU admissions, ICU readmissions, and hospital readmission.
- **Comparator matched:** All six rows show count/denominator expressions and Poisson; earlier SAP distinguishes count from binary outcomes and separately labels individual continuous outcomes with Gaussian models.
- **Consistency rule applicable:** Yes as a response-type/quantity-label check; interpretation of the heading as referring to continuous derived rates rather than modeled counts remains conditional.
- **Calculation/logical comparison reproduced:** Discrete event numerators modeled by Poisson are count responses; dividing by patient-days yields rate summaries and by discharge counts yields proportions. These summaries differ from the explicitly described patient Gaussian continuous outcomes.
- **Necessary inputs available:** Yes for printed heading, numerators/denominators, and source model taxonomy; no heading-author intent.
- **Exact missing inputs/definitions:** Whether Continuous means hospital rate-summary variables rather than modeled outcome responses.
- **Source-grounded alternative:** Hospital rates may be treated as continuous summaries, so the heading could describe summaries instead of response distributions. It does not establish incorrect estimates.
- **Direct observation versus inferred explanation:** Heading, row formulas, and Poisson labels are direct; an inherited/unqualified heading is a possible explanation.
- **Remaining human question:** Does the heading identify derived hospital rate summaries or actual modeled response types, and what type description should readers extract?
- **Classification:** PLAN internal; P_P only; Measure, label, or scale inconsistency; plan_material. Heading-semantics ambiguity retained.
- **Evidence state:** recorded_candidate, determined by the registered conditional heading/model-taxonomy difference reproduced with its alternative interpretation. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C026 — Historical AUC endpoint scale

- **Location found:** Yes: [protocol p6 systematic-review paragraph](../../../joi180015supp1_prod.pdf#page=6), with probability-scale comparison supplied by [protocol p1 AUC labels](../../../joi180015supp1_prod.pdf#page=1).
- **Source value/text matched:** Printed “AUCROC 0.83-86” for adult scores distinguishing ICU from high-dependency patients.
- **Comparator matched:** Same plan uses AUCROC0.91 and0.87; conventional area/probability scale is bounded0–1.
- **Consistency rule applicable:** Yes for explicit AUC endpoint scale, subject to abbreviated-range notation rather than literal86.
- **Calculation/logical comparison reproduced:** Literal86 exceeds upper probability bound1 by85. Reading86 as the abbreviated suffix of0.86 gives a coherent0.83–0.86 range.
- **Necessary inputs available:** Yes for exact printed string and scale diagnostic. The cited historical review is not supplied and was not consulted.
- **Exact missing inputs/definitions:** Intended upper endpoint and whether abbreviated-decimal range notation is intentional.
- **Source-grounded alternative:** Compressed decimal suffix notation may intentionally mean0.86. This is a printed extraction/scale ambiguity, not evidence that the historical AUC computation was86.
- **Direct observation versus inferred explanation:** Literal printed string is direct; the intended expanded endpoint is inferred, not assigned as a correction.
- **Remaining human question:** Should86 be interpreted as an intentionally abbreviated0.86 endpoint, or does another scale convention apply?
- **Classification:** Historical/background data inside PLAN; P_P only; Measure, label, or scale inconsistency; plan_material. Endpoint shorthand ambiguity retained.
- **Evidence state:** recorded_candidate, determined by reproduced explicit-scale ambiguity in the registered AUC range. **Suggested review disposition:** retain. **Human status:** Pending Human Adjudication.

## C027 — Generic adjusted label versus baseline-unadjusted SCDE difference

- **Location found:** Yes: [main abstract p1](../../../jama_parshuram_2018_oi_180015.pdf#page=1), [SCDE narrative p6](../../../jama_parshuram_2018_oi_180015.pdf#page=6), [Table 3 footnote a p7](../../../jama_parshuram_2018_oi_180015.pdf#page=7), and [GEE fallback explanation p5](../../../jama_parshuram_2018_oi_180015.pdf#page=5).
- **Source value/text matched:** Abstract/narrative says adjusted between-group rate difference−0.34(−0.73,0.05)/1000 patient-days. Narrative separately explicitly calls the0.77 rate ratio baseline-adjusted.
- **Comparator matched:** Table 3 footnote a says the SCDE difference model was not adjusted for baseline values. Main p4–5 states models account for hospital clustering; [Table 2 footnote c p6](../../../jama_parshuram_2018_oi_180015.pdf#page=6) explicitly uses “adjusted for clustering by hospital.”
- **Consistency rule applicable:** No categorical contradiction follows unless generic adjusted is defined as baseline-adjusted. Baseline-unadjusted GEE can still account for hospital clustering; the source uses adjustment language for clustering elsewhere.
- **Calculation/logical comparison reproduced:** Estimate and CI are identical at all compared locations, so numerical alignment holds. Logical equivalence “adjusted = adjusted for baseline” is not supplied. The footnote excludes baseline, not cluster accounting; separate rate-ratio P=.03 is not assigned to the identity-link difference.
- **Necessary inputs available:** Yes for same-result words, footnote, and clustering framework; no local definition of generic adjusted in this SCDE sentence.
- **Exact missing inputs/definitions:** Which adjustment dimension the abstract/narrative's generic word denotes; final output identifying variance/clustering and covariates if terminology is to be resolved.
- **Source-grounded alternative:** Adjusted refers to cluster accounting, while baseline-adjusted is reserved for the ratio; the article's own Table 2 phrasing supports this distinction. No contradiction in the printed−0.34/CI is reproduced.
- **Direct observation versus inferred explanation:** Different specificity of the words is direct. Treating generic adjusted as necessarily baseline-adjusted is the unsupported registered semantic assumption.
- **Remaining human question:** Does adjusted for the−0.34 difference mean hospital clustering, and should it be explicitly qualified to prevent baseline-adjustment misclassification?
- **Classification:** REPORT within main article; S_W only; Measure, label, or scale inconsistency; report_internal_inconsistency. Roles confirmed; residual relationship retained with explicit semantic ambiguity.
- **Evidence state:** record_input_error, determined by unsupported equivalence of generic adjustment and baseline adjustment. A residual terminology question cannot be settled without the local definition; this is not a proven baseline-label contradiction. **Suggested review disposition:** discuss. **Human status:** Pending Human Adjudication.

## C028 — Generic adjusted label versus baseline-unadjusted physician-call difference

- **Location found:** Yes: [main Other Outcomes p8](../../../jama_parshuram_2018_oi_180015.pdf#page=8), [Table 3 footnote a p7](../../../jama_parshuram_2018_oi_180015.pdf#page=7), and [GEE fallback p5](../../../jama_parshuram_2018_oi_180015.pdf#page=5).
- **Source value/text matched:** Narrative says adjusted between-group rate difference3.10(−1.92,8.11)/1000 patient-days; separate adjusted rate ratio1.17(0.73,1.88), P=.52.
- **Comparator matched:** Table 3 footnote a says immediate-call-for-physician difference model was not adjusted for baseline. GEE framework accounts for center clustering; [Table 2 footnote c p6](../../../jama_parshuram_2018_oi_180015.pdf#page=6) explicitly describes adjustment for clustering by hospital.
- **Consistency rule applicable:** No categorical contradiction without defining generic adjusted as baseline-adjusted. Cluster accounting does not imply baseline covariate inclusion, and baseline removal does not imply clustering removal.
- **Calculation/logical comparison reproduced:** Difference/CI match exactly between narrative and table. No numerator, estimate, or CI mismatch exists. The baseline-unadjusted GEE difference can coexist with an adjusted-for-clustering description; separate ratio/P value not conflated with the difference.
- **Necessary inputs available:** Yes for textual/result alignment and framework; no explicit local adjustment definition in the physician-call narrative.
- **Exact missing inputs/definitions:** Meaning of generic adjusted for this identity-link difference, including what clustering/variance accounting persisted after baseline removal.
- **Source-grounded alternative:** Adjusted denotes cluster accounting; article uses that sense elsewhere. Alternatively the narrative may intend an imprecise blanket baseline label, but source does not determine which interpretation.
- **Direct observation versus inferred explanation:** Words and same-result identity are direct. Inferring baseline adjustment solely from generic adjusted is an unsupported semantic alignment.
- **Remaining human question:** Which adjustment does the3.10 narrative label denote, and should the text distinguish clustering from baseline covariates?
- **Classification:** REPORT internal; S_W only; Measure, label, or scale inconsistency; report_internal_inconsistency. No role correction; semantic ambiguity explicit.
- **Evidence state:** record_input_error, determined by unsupported generic-adjusted/baseline-adjusted equivalence, with residual terminology unresolved. **Suggested review disposition:** discuss. **Human status:** Pending Human Adjudication.

## Scope and unresolved-input summary

All 28 stable IDs have separate source, comparator, rule, reproduction, input, alternative, observation/inference, human-question, classification, and evidence-state records. Counts: **23 recorded_candidate; 5 record_input_error; 0 not_reproduced; 0 repaired_residual**. record_input_error IDs: C006, C010, C024, C027, C028. Suggested pre-fills therefore retain23 and discuss5. Every ID remains Pending Human Adjudication.

Unresolved inputs are bounded per card: intended figure encodings/axis scope; original extrema; anticipated bed basis; historic cohort dates/count exactness/rounding; final operational thresholds and conjunctions; ICU-unit scope; denominator/model-version history; patient-versus-discharge PIM definition; coefficient conversion; example probability cap/truncation; ICU category exhaustiveness; shell-heading semantics; AUC shorthand; and clustering-versus-baseline meaning of generic adjusted. These do not represent missing direct-source inspection: every cited comparison location was found and inspected. No effect on paper-level conclusions or downstream estimates is inferred.

No candidate is solely a display-zero P-value observation. No assigned ID was deleted, renumbered, merged, or adjudicated. Sole classification correction is C016 All relationships P_R, removing the nonexistent protocol ICU-readmission logit comparator from the final comparison while retaining historical discovery provenance.


## Appended-ID recheck wave

Fresh distinct runtime /root/recheck_append confirms C029/C030. The protocol explicitly operationalizes its own within-48-hours name using the third following midnight; this strengthens the intentional-shorthand alternative without making literal elapsed time identical to the calendar rule. Canonical classification totals:25 recorded_candidate and5 record_input_error; all30 remain Pending Human Adjudication.

## C029 — ICU-readmission elapsed-hours label versus calendar-day cutoff

- **Cited location found:** Yes. [Main article, physical PDF p. 7, Table 3 ICU readmission row](../../../jama_parshuram_2018_oi_180015.pdf#page=7); [results supplement, physical PDF p. 6, eTable 1 Unplanned ICU Readmission row](../../../joi180015supp3_prod.pdf#page=6); and [protocol, physical PDF p. 12, outcome 4](../../../joi180015supp1_prod.pdf#page=12). All three were inspected as fresh direct-source page images and layout text.
- **Source printed value/text matched:** Yes. Main Table 3 prints “ICU readmission <48 h” with footnote h. The intervention-period BedsidePEWS and usual-care event counts are 94 and 108, their rates are 28.40 and 21.25, adjusted between-group rate difference is 4.95 (−1.62 to 11.52), adjusted ratio is OR, 1.11 (0.77 to 1.61), and P value is .58. Footnote h states that rates are expressed per 1000 discharges from the ICU. These numbers identify the row; this candidate does not assert a numerical disagreement in them.
- **Comparator printed value/text matched:** Yes. Results eTable 1 prints “Re-admission before midnight of the second full calendar day after ICU discharge. Thus, re-admission occurred before the 3rd midnight following ICU discharge.” Protocol outcome 4 prints “Unplanned PICU readmission within 48 hours of PICU discharge” and expressly operationalizes that wording as before midnight of the second complete day following discharge, alternatively before the third midnight. The protocol therefore supplies an explicit source-grounded reason that hours wording may be an operational shorthand.
- **Consistency rule applicable:** Yes for the endpoint time-window label. A literal strict elapsed interval <48 hours and a calendar cutoff before the third following midnight are different membership rules. The ICU readmission outcome name aligns the main row with the supplement definition; the source does not require a statistical-model assumption for this comparison. Applying the same unplanned, otherwise eligible constructed readmission to both rules isolates the time condition.
- **Calculation or logical comparison reproduced:** Yes. On a constructed ordinary calendar week without a clock change, discharge Monday 01:00 and unplanned ICU readmission Wednesday 23:00 yield 24 + 24 + 22 = 70 elapsed hours. The first following midnight is Tuesday 00:00, the second Wednesday 00:00, and the third Thursday 00:00. Wednesday 23:00 is before Thursday 00:00 and is after 48 elapsed hours, so it satisfies the calendar condition and fails <48 hours. For this discharge, the third midnight is 71 hours after discharge. On ordinary 24-hour days, that cutoff varies approximately from 48 to 72 elapsed hours with discharge time. This is a constructed logical counterexample, not a trial event or a reanalysis.
- **Necessary inputs available, with missing inputs named:** The exact label, full calendar definition, outcome identity, and temporal rule are available and sufficient to reproduce the label membership difference. Missing for an actual count or estimate comparison are patient discharge/readmission timestamps, event-level eligibility and unplanned-status classifications, final case-report/analysis implementation of the cutoff, and an explicit report-side definition of whether “<48 h” denotes literal elapsed time or the protocol's calendar shorthand. Without those inputs, neither affected events nor a revised count, rate, OR, confidence interval, or P value can be calculated.
- **Source-grounded alternative interpretation:** The protocol itself names “within 48 hours” and immediately declares the third-midnight operational rule. This supports an intentional abbreviated endpoint name rather than an actual difference in event classification. The result supplement could be documenting that same convention while Table 3 compresses it to “<48 h.” The protocol explanation does not make literal <48 elapsed hours identical to the calendar rule; it supplies a possible intended meaning. No event or effect change is inferred.
- **Direct observation separated from inferred explanation:** Direct observations are the main label, supplement definition, protocol operationalization, printed row values and rate footnote. The 70-hour membership difference is reproduced logical reasoning. Intentional shorthand and the rule actually applied to 94/108 events are possible explanations or unknown facts, not direct observations. No trial participant is asserted to have the constructed timing.
- **Exact remaining human question:** For the ICU-readmission result with intervention-period events 94/108, was the implemented endpoint literal elapsed <48 hours or the before-third-midnight calendar operationalization, and should the report's “<48 h” label be interpreted as shorthand for that calendar rule?
- **Document role of every compared location:** Main Table 3 is REPORT because it presents observed study outcomes and fitted results. Results eTable 1 is REPORT because it defines the outcomes used in the non-plan results supplement. Protocol outcome 4 is PLAN because its content is a prospective research protocol describing what will be recorded and how the outcome will be operationalized. These assignments come from content, not filenames.
- **Relationship type and all relationships:** Confirmed primary S_C; all relationships S_C. The discrepancy is the time-window label versus operational definition across two different REPORT documents. The PLAN location corroborates and explains the calendar convention and adds no separate discrepancy relationship. Precedence P_R > P_P > S_C > S_W therefore does not change S_C. Category is Measure, label, or scale inconsistency; derived review domain is report_internal_inconsistency. Classification ambiguity: None for roles or relationship; intended label meaning remains the named human question.
- **Evidence state and determining recheck fact:** recorded_candidate. The direct source confirms both cited statements and reproduces the registered literal-hours versus calendar-cutoff membership difference. The exact implemented endpoint and intended hours shorthand remain missing definitions as registered. No source transcription or alignment was disproven; the strong protocol shorthand alternative limits interpretation without settling the report-side label question.

## C030 — Hospital-readmission elapsed-hours label versus calendar-day cutoff

- **Cited location found:** Yes. [Main article, physical PDF p. 7, Table 3 hospital readmission row](../../../jama_parshuram_2018_oi_180015.pdf#page=7); [results supplement, physical PDF p. 6, eTable 1 Unplanned Hospital Readmission row](../../../joi180015supp3_prod.pdf#page=6); and [protocol, physical PDF p. 12, outcome 3](../../../joi180015supp1_prod.pdf#page=12). All three were inspected as fresh direct-source page images and layout text.
- **Source printed value/text matched:** Yes. Main Table 3 prints “Hospital readmission <48 h” with footnote c. The intervention-period BedsidePEWS and usual-care event counts are 170 and 387, their rates are 3.39 and 4.10, adjusted between-group rate difference is −0.71 (−4.92 to 3.49), adjusted ratio is OR, 0.93 (0.61 to 1.41), and P value is .74. Footnote c states that rates are expressed per 1000 patient discharges from the hospital. These values identify the row; no numerical inferential disagreement is asserted by this candidate.
- **Comparator printed value/text matched:** Yes. Results eTable 1 prints “Re-admission to any inpatient area in the hospital before midnight of the second day full calendar day after discharge. Thus, re-admission occurred before the 3rd midnight following hospital discharge.” The awkward “second day full calendar day” word order is present visually and was not silently normalized. Protocol outcome 3 names “Unplanned re-admission to hospital within 48 hours of hospital discharge,” then states that the outcome will be operationalized before midnight of the second day of discharge and expressly before the third midnight following discharge. The explicit third-midnight sentence is the corroborating temporal comparator; the protocol wording is not used to infer another event boundary.
- **Consistency rule applicable:** Yes for the endpoint time-window label. A strict <48-hour elapsed-time condition and before-third-midnight calendar condition do not have identical membership. Hospital readmission in the main row aligns with the supplement's hospital readmission definition. A constructed otherwise eligible unplanned return to an inpatient hospital area can satisfy all non-time conditions for both rules, leaving only the temporal membership comparison.
- **Calculation or logical comparison reproduced:** Yes. In a constructed ordinary calendar week without a clock change, hospital discharge Monday 01:00 and unplanned hospital readmission Wednesday 23:00 give 24 + 24 + 22 = 70 elapsed hours. Following midnights are Tuesday 00:00, Wednesday 00:00, and Thursday 00:00. Wednesday 23:00 is before the third midnight Thursday 00:00 and fails the <48-hour test. The third-midnight cutoff is 71 hours after this discharge; on ordinary 24-hour days it is approximately 48–72 hours after discharge depending on discharge time. This reproduces a definition-level counterexample without claiming any actual event count difference.
- **Necessary inputs available, with missing inputs named:** The main label, supplement calendar cutoff, matching outcome identity, and protocol operationalization suffice for the logical rule comparison. Missing for implementation and numerical consequences are patient discharge/readmission timestamps, eligibility and unplanned-event classifications, final case-report/analysis cutoff implementation, and an explicit report-side definition resolving literal elapsed <48 hours versus calendar shorthand. These missing inputs prevent identifying affected events or calculating changes to 170/387 counts, rates, differences, ORs, intervals, or P values.
- **Source-grounded alternative interpretation:** The protocol explicitly treats “within 48 hours” as a name to be operationalized by the third following midnight. The Table 3 hours label may be an abbreviated name for that same outcome and the supplement may describe the implemented operational convention. This is stronger support for shorthand than a merely hypothetical explanation. It does not establish that the literal elapsed-hours reading and calendar membership are equal, and no change to an actual event or effect estimate follows from the supplied comparison.
- **Direct observation separated from inferred explanation:** Directly observed are the exact main label, supplement wording including its unusual word order, protocol operationalization, counts, rates, estimates and footnote c. The constructed 70-hour membership comparison is derived logic. Intentional shorthand, actual implementation, and whether any trial event lies between the two cutoffs remain inferred possibilities or unknown. No patient is attributed the constructed timestamps.
- **Exact remaining human question:** For the hospital-readmission result with intervention-period events 170/387, did event classification use literal elapsed <48 hours or the before-third-midnight calendar rule, and what quantitative time window should a data extractor take from the “<48 h” label?
- **Document role of every compared location:** Main Table 3 is REPORT because it reports observed outcomes and model estimates. Results eTable 1 is REPORT because it defines the outcomes in a non-plan results supplement. Protocol outcome 3 is PLAN because the prospective protocol specifies how an outcome will be operationalized. Content, rather than supplement numbering or filename, determines these roles.
- **Relationship type and all relationships:** Confirmed primary S_C; all relationships S_C. The substantive comparison is a REPORT label against a different REPORT's calendar definition. PLAN protocol outcome 3 corroborates the calendar convention and supports shorthand; it is not an additional discrepancy relationship. Precedence P_R > P_P > S_C > S_W leaves S_C. Category is Measure, label, or scale inconsistency; derived review domain is report_internal_inconsistency. Classification ambiguity: None for document roles or relationship; intended label meaning remains the exact human question.
- **Evidence state and determining recheck fact:** recorded_candidate. Fresh direct-source reading confirms the registered label and operational definition, including the supplement's awkward wording, and reproduces the literal-hours/calendar membership difference. The implementation and label meaning remain the registered unresolved definitions. No transcription or source alignment is disproven. Protocol-supported shorthand is an alternative interpretation, not proof that the literal label denotes the same elapsed-time set.

## Direct-source Derivative Provenance

CPU-only direct Poppler 25.03.0 commands, all outputs newly written below preprocessing/recheck_append:

```bash
pdftotext -layout -f 7 -l 7 "jama_parshuram_2018_oi_180015.pdf" ".ai_paper_validation/review_1_6/preprocessing/recheck_append/main-p7.txt"
pdftotext -layout -f 6 -l 6 "joi180015supp3_prod.pdf" ".ai_paper_validation/review_1_6/preprocessing/recheck_append/results-p6.txt"
pdftotext -layout -f 12 -l 12 "joi180015supp1_prod.pdf" ".ai_paper_validation/review_1_6/preprocessing/recheck_append/protocol-p12.txt"
pdftoppm -f 7 -l 7 -singlefile -r 100 -png "jama_parshuram_2018_oi_180015.pdf" ".ai_paper_validation/review_1_6/preprocessing/recheck_append/main-p7"
pdftoppm -f 6 -l 6 -singlefile -r 120 -png "joi180015supp3_prod.pdf" ".ai_paper_validation/review_1_6/preprocessing/recheck_append/results-p6"
pdftoppm -f 12 -l 12 -singlefile -r 120 -png "joi180015supp1_prod.pdf" ".ai_paper_validation/review_1_6/preprocessing/recheck_append/protocol-p12"
```

All commands succeeded. The results supplement emitted an Invalid Font Weight warning during extraction and rendering; its relevant text and visual rows are readable and agree. No OCR or fallback was needed. No supplied source or reused derivative was modified. Unresolved scope is the two precisely named endpoint-implementation/label questions, with no mechanical coverage limitation.
