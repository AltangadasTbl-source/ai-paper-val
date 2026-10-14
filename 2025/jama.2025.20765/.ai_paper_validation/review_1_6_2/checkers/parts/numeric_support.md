# Numeric consistency checker: support shard

Runtime: 01a12c43-8381-77c0-a329-6a6ab73645eb. Model: gpt-6.1-sol. Reasoning effort: medium. Exact scope: within-document numeric relationships in DOC-003 REPORT PDF pages 1–16 and DOC-002 PLAN PDF pages 1–109. Coverage: 125 of 125 mapped support units reviewed; 93 relationship bundles checked; four findings; twelve excluded observations; zero scientific gaps. Relationship inventory: relationships/parts/numeric_support.md. Main-article internal relationships and cross-document matching are assigned to separate reviewers. Inferential tests, confidence-interval methods, sample-power reconstruction and analysis-model logic are covered by the independent statistical reviewers.

The complete scope and review contract were read. No web or earlier scientific conclusions were used. Every report table cell was reviewed from the new source-linked support map; apparent issues were confirmed against direct-source pages. Fresh CPU renders use the pinned fallback interpreter, bundled pdf_tools.py, PyMuPDF 1.26.4, 200 dpi. Confirmation images are preprocessing/numeric_support_p006.png, numeric_support_p009.png, numeric_support_p013.png, numeric_support_plan_p16.png and numeric_support_plan_p53.png. Additional plan pages 62–64 were directly rendered and inspected to confirm arithmetic and printed labels. Existing text/images are transcription aids, not final authority.

## Findings

### F-NUM-101

**Title:** Two usual-care cause-of-death percentages do not reconcile with their counts and death total.

**Exact source locations and document roles:** DOC-003 REPORT, [PDF page 6, eTable 4](../../../../joi250093supp2_prod_1768590553.09463.pdf#page=6), usual-care “Drug user” and “Severe pneumonia” cells, compared with the usual-care “Total deaths” cell in the same display. Both affected cells print 1(7.4%); total deaths prints 27. Same display usual-care Stroke prints 2(7.4%) and History of fall prints 1(3.7%). Direct-source render confirms both affected readings.

**Printed inputs:** n=1, N=27, displayed p=7.4% at each of the two locations. All cause counts sum to 27; the overall counts for each affected cause are 1 and mHealth counts are 0.

**Rule and calculation:** Cause percentage=100 n/N. Exact count ratio gives 100/27=3.703704%. Mandated half-unit intervals n∈[0.5,1.5], N∈[26.5,27.5] produce [1.818182%,5.660377%]; displayed 7.4% permits [7.35%,7.45%]. Gap=1.689623 percentage points; relative discrepancy=1.689623/7.4=0.228327, above 0.05. Each other usual-care cause cell fits its count/27 denominator under the same rule. Both affected rows constitute one repeated pattern.

**Focus area:** A, counts and denominators. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W.

**Qualifying route:** Route A, category 3.

**Affected result or extracted value:** Usual-care proportions of deaths associated with drug use and severe pneumonia; a reader can extract 7.4% or the count-derived 3.7%.

**Why context does not resolve it:** This is an always-register count/denominator/percentage inconsistency within one table. The adjoining rows indicate how the percentage could have been formed, but do not remove the two printed percentages.

**Alternatives and missing definition:** The percentages could correspond to two deaths, or the counts could be one and the percentages based on a different denominator. No cause-specific denominator is stated. The row/column sums corroborate one death per cause but do not establish a correction.

**Exact human question:** For the usual-care Drug user and Severe pneumonia rows in eTable 4, which counts and percentages should be used, and what denominator was used for each printed 7.4%?

### F-NUM-102

**Title:** The site 2008 death count and percentage differ from the table’s uniform denominator pattern.

**Exact source locations and document roles:** DOC-003 REPORT, [PDF page 9, eTable 6](../../../../joi250093supp2_prod_1768590553.09463.pdf#page=9), control site 2008 cell 5(7.5), compared with the same display’s count/percentage rule across all other sites. DOC-003 REPORT [PDF page 8, eTable 5](../../../../joi250093supp2_prod_1768590553.09463.pdf#page=8), site 2008 recruitment and ITT denominators 40, corroborates the denominator. The page-9 direct-source render confirms 5(7.5).

**Printed inputs:** Site 2008 deaths=5 and percentage=7.5%; cluster population=40. Every other death cell implies the same N=40, including count 3 with 7.5%, count 4 with 10.0%, and count 5 with 12.5% at site 2012. Site 2008 has 35 observed month-6 contributors in eTable 5, which also cannot produce 7.5% from five deaths.

**Rule and calculation:** 100×5/40=12.5%. Allowing n∈[4.5,5.5] and N∈[39.5,40.5] produces [11.111111%,13.924051%]; printed 7.5% allows [7.45%,7.55%]. Gap=3.561111 percentage points; relative discrepancy=3.561111/7.5=0.474815, above 0.05. All other rows reproduce the same denominator-40 rule.

**Focus area:** A, counts and denominators. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W.

**Qualifying route:** Route A, category 3.

**Affected result or extracted value:** The site 2008 cluster-specific mortality proportion and its death count.

**Why context does not resolve it:** This is an always-register count/percentage inconsistency within the site death display. Denominator 40 is supported by all other rows and corroborated by the same site’s explicit recruitment/ITT counts.

**Alternatives and missing definition:** The percentage 7.5% corresponds to three deaths among 40; the count five corresponds to 12.5%. Another site-specific denominator is possible only if separately defined; no such denominator is supplied. All site death counts sum to the reported 52 and to usual-care 27/mHealth 25, which corroborates the count while preserving the printed discrepancy.

**Exact human question:** What death count, denominator and mortality percentage should be used for control site 2008 in eTable 6?

### F-NUM-103

**Title:** The treatment-failure absolute difference reverses the sign of the display’s arm contrast.

**Exact source locations and document roles:** DOC-003 REPORT, [PDF page 13, eTable 9](../../../../joi250093supp2_prod_1768590553.09463.pdf#page=13), Treatment Failures row, compared with the arm percentages and all preceding absolute-difference rows in the same display; [PDF page 14, footnote b](../../../../joi250093supp2_prod_1768590553.09463.pdf#page=14) defines b as absolute difference. Both are REPORT.

**Printed inputs:** mHealth 1/695, 0.1%(0.01–0.8); usual care 2/333, 0.6%(0.1–2.2); absolute difference +0.5 percentage points, interval −0.4 to +1.3. Other rows use mHealth minus usual care: 43.2−16.5=26.7, 38.0−11.4=26.6, 50.8−22.5=28.3, 57.5−24.6=32.9, and 3.2−2.1=1.1.

**Rule and calculation:** Same-table arm difference=100(1/695−2/333)=−0.456716 percentage points. Half-unit count/denominator inputs produce [−0.679989,−0.233792] percentage points. Printed +0.5 permits [+0.45,+0.55]. Gap=0.683792; relative discrepancy=0.683792/0.5=1.367585, above 0.05. Separately, printed arm percentages permit mHealth−usual care in [−0.60,−0.40], again disjoint from the positive difference interval. The count-derived sign is unchanged under either precision calculation. The interval is retained as printed for the statistical lane’s method review.

**Focus areas:** A and B, count-derived contrast and direction. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** Treatment-failure risk difference in the sensitivity analysis excluding deaths; the positive printed value changes its direction relative to the other rows.

**Why context does not resolve it:** A printed sign changing the direction is always registered after reproduction. The intended sign may be inferred from the displayed risks, but the positive value remains available for extraction.

**Alternatives and missing definition:** “Absolute difference” might mean the unsigned magnitude only for this row, or the row might reverse the reference group. All other rows use the signed mHealth-minus-usual-care contrast, and the interval has negative as well as positive limits; no row-specific contrast change is stated. A different model-based absolute contrast is another possibility, but no such definition accompanies the column. This finding concerns the point-value sign under the displayed common contrast, rather than assuming a confidence-interval method.

**Exact human question:** Does eTable 9 use mHealth minus usual care for Treatment Failures, and what signed difference and corresponding interval should be used for that row?

### F-NUM-104

**Title:** The protocol SMS totals do not reconcile with their printed daily schedules.

**Exact source locations and document roles:** DOC-002 PLAN, [PDF page 16, lines 386–390](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=16), total 178 SMS versus the schedule in the same paragraph; DOC-002 PLAN, [PDF page 53, lines 1526–1530](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=53), total 134 SMS versus the schedule in the same paragraph. Both locations are protocol plan content. Both within-paragraph readings were confirmed against fresh direct-source renders. The bundle labels the first passage earlier protocol and the second latest protocol; the running headers and disclosed change statement are retained without conflating versions.

**Printed inputs:** Page 16: 178 messages over six months; first two months 4–5 per day, next two months 2–3 per day, last two months 1–2 per week. Page 53: 134 messages over six months; first two months 4–5 per day, next two months 1–2 per day, last two months 1 per week.

**Rule and calculation:** Sum duration×frequency across the three consecutive segments. With a conservative 28-day month, nominal lower bounds are page 16: 56×4+56×2+8×1=344 messages; page 53: 56×4+56×1+8×1=288 messages. To apply the mandated half-unit rule generously to every printed numeric duration and rate endpoint, each two-month duration permits 1.5–2.5 months; each endpoint permits ±0.5 messages per stated period. With calendar months bounded by 28–31 days, an enclosing page-16 schedule interval is [213,725.179] messages: lower=42×3.5+42×1.5+6×0.5, upper=77.5×5.5+77.5×3.5+(77.5/7)×2.5. Page 53’s enclosing interval is [171,636.608]: lower=42×3.5+42×0.5+6×0.5, upper=77.5×5.5+77.5×2.5+(77.5/7)×1.5. These deliberately relaxed bounds allow segment durations independently; imposing the printed total six months cannot enlarge them or lower the minima. Printed totals permit [177.5,178.5] and [133.5,134.5]. Minimum gaps are 34.5/178=0.193820 and 36.5/134=0.272388, both above 0.05. A calendar-specific calculation strengthens the discrepancy; it is not needed to reproduce it.

**Focus area:** D, randomized intervention dose specification relied on in interpreting the primary efficacy comparison. **Proposed review domain:** plan_material. **Proposed relationship type:** P_P.

**Qualifying route:** Route B.

**Affected result or extracted value:** The planned mHealth message dose for the superiority comparison and the correspondence of the delivered intervention to its planned dose.

**Why context does not resolve it:** The paragraph explicitly states each participant receives the total and specifies the transmission frequency. Each version has an internal discrepancy independent of the amendment between versions. The calendar-day convention cannot reduce even the relaxed interval to the printed total. The bundle’s SAP gives a different schedule and the SMS catalog gives 134 message IDs with tobacco-specific branches; these provide possible dose interpretations, but do not identify which numeric schedule governs the protocol’s stated exposure.

**Alternatives and missing definition:** Total might describe distinct message templates rather than transmissions, or the durations/rate periods might denote another unit. No such definition is supplied in the affected paragraphs. Page 77 discloses updated design and several intervention changes but does not reconcile these internal dose totals with their printed frequency segments. No preferred schedule is proposed.

**Exact human question:** In the two protocol passages, do 178 and 134 represent transmitted messages per participant or distinct message templates, and what durations and frequencies define the planned per-participant dose?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-003 REPORT p3, eTable 1 | Ineligibility reason counts total 13856, above 8146 ineligible participants; reasons are not stated to be mutually exclusive and can occur together. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 REPORT p4, eTable 2 | Site 2012 appears in later site tables but has no prior-quit-attempt row here; no printed total or analysis-population size is contradicted by this descriptive table omission. | PERIPHERAL_COMPARISON |
| DOC-003 REPORT p5, eTable 3 | Monthly mean sums174.19/177.7 differ from printed total174.3/178.0; the printed input and total half-unit intervals overlap. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 REPORT pp6,8,15–16, eTables 4,5,10 | Small percentage deviations, including overall heart-attack8/52 with15.2%, recruitment40/527 with7.5%, and symptom percentages rounded to whole or one-decimal units, fit input intervals or have remaining relative discrepancy≤0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 REPORT pp3,8, eTables 1,5 | Site recruitment-screening denominators sum9240 versus screening total9232; half-unit output gap7 and relative7/9232=.000758 are below0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 REPORT pp15–16, eTable 10 | Epigastric-pain category count sum698 mHealth versus699 implied by other symptoms; no explicit same-table denominator is printed and percentages fit both totals; even a one-person total difference is below0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 REPORT pp13–14, eTable 9 | Crude RR values differ from unclustered risk ratios, including300/695 versus55/333 yielding2.6135 rather than2.9. Crude and adjusted cluster ICCs and the mixed-model context do not establish that this column is the simple unclustered ratio. | MODEL_VERSUS_CRUDE |
| DOC-002 PLAN pp63–64, lines1894–1907 and1936–1943 | Printed attrition/product results704,1036,1080,1620 differ from arithmetic704.4,1036.8,1056,1616.16; half-unit input intervals overlap or remaining relative discrepancy≤0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-002 PLAN p62, lines1866–1868 and pilot diagram | “In each site n=16” differs from diagram total16 across4 sites; the immediately adjoining figure and first16 pilot statement show the aggregate reading. The observation depends on site-level wording. | TERMINOLOGY_OR_WORDING |
| DOC-002 PLAN p64, line1948 | A phase-4 diagram box says “Phase 3 (Superiority trial)” while its surrounding title, arm labels, 36 sites and1620 participants consistently identify phase4; the numeric values themselves are unchanged. | TERMINOLOGY_OR_WORDING |
| DOC-002 PLAN p85, MPSS description | Five domains and a5-point scale are described with total5–35; the scale description is a wording/terminology observation without a reported numeric result that can be reconstructed from printed participant values. | TERMINOLOGY_OR_WORDING |
| DOC-002 PLAN pp54–55, TAM table | Process-substudy table says30% while prose and country counts use20%; this does not determine a reported primary/key-secondary result, analysis-population size or statistical decision rule. | PERIPHERAL_COMPARISON |

## Completion and limitations

All assigned within-document numeric relationships were checked, including every row/column/subgroup partition and all matching within-supplement counts. No scientific coverage gap remains. Source page 13 of DOC-002 clips part of the earlier Bangladesh phase-3 diagram; visible numbers are checked and the unmapped invisible text is not invented. That source truncation is a limitation of available evidence, not omitted review. No supplied raw data or participant-level denominator file exists; denominators not printed or inferable from a reproducible display pattern are not fabricated. Unknown models are not replaced by crude ratios. Findings remain proposals for the independent inclusion screen and human questions, with no candidate IDs or adjudication labels.

Scope counts: 125 support PDF units; 93 stable relationship bundles; four findings; twelve excluded observations; zero gaps.

